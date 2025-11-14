# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Example using Interrupts to send a message and then wait indefinitely for messages
# to be received. Interrupts are used only for receive. sending is done with polling.
# This example is for systems that support interrupts like the Raspberry Pi with "blinka"
# CircuitPython does not support interrupts so it will not work on  Circutpython boards
# Author: Tony DiCola, Jerry Needell
import socket
import time

import adafruit_rfm9x
import board
import busio
import digitalio
import RPi.GPIO as io

# Setup UDP socket for logging
UDP_HOST = "localhost"
UDP_PORT = 1337
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def send_udp_message(message):
    """Send a message to the UDP socket."""
    try:
        udp_socket.sendto(message.encode("utf-8"), (UDP_HOST, UDP_PORT))
    except Exception as e:
        # Fallback to print if UDP fails
        print(f"UDP send failed: {e}")


# setup interrupt callback function
def rfm9x_callback(rfm9x_irq):
    global packet_received  # noqa: PLW0603
    print("IRQ detected ", rfm9x_irq, rfm9x.rx_done)
    # check to see if this was a rx interrupt - ignore tx
    if rfm9x.rx_done:
        packet = rfm9x.receive(timeout=None)
        if packet is not None:
            packet_received = True
            # Received a packet!
            # Print out the raw bytes of the packet:
            send_udp_message(packet)
            print(packet)


# Define radio parameters.
RADIO_FREQ_MHZ = 915.0  # Frequency of the radio in Mhz. Must match your
# module! Can be a value like 915.0, 433.0, etc.

# Define pins connected to the chip, use these if wiring up the breakout according to the guide:
CS = digitalio.DigitalInOut(board.CE1)
RESET = digitalio.DigitalInOut(board.D25)

# Initialize SPI bus.
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Initialze RFM radio
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ, agc=True)

# config
rfm9x.preamble_length = 8
rfm9x.signal_bandwidth = 125000
rfm9x.coding_rate = 5
rfm9x.spreading_factor = 9
rfm9x.enable_crc = True

# You can however adjust the transmit power (in dB).  The default is 13 dB but
# high power radios like the RFM95 can go up to 23 dB:
rfm9x.tx_power = 5

# configure the interrupt pin and event handling.
RFM9X_G0 = 22
io.setmode(io.BCM)
io.setup(RFM9X_G0, io.IN, pull_up_down=io.PUD_DOWN)  # activate input
io.add_event_detect(RFM9X_G0, io.RISING)
io.add_event_callback(RFM9X_G0, rfm9x_callback)

packet_received = False
# Send a packet.  Note you can only send a packet up to 252 bytes in length.
# This is a limitation of the radio packet size, so if you need to send larger
# amounts of data you will need to break it into smaller send calls.  Each send
# call will wait for the previous one to finish before continuing.
rfm9x.send(bytes("Hello world!\r\n", "utf-8"), keep_listening=True)
send_udp_message("Sent Hello World message!")

# Wait to receive packets.  Note that this library can't receive data at a fast
# rate, in fact it can only receive and process one 252 byte packet at a time.
# This means you should only use this for low bandwidth scenarios, like sending
# and receiving a single message at a time.
send_udp_message("Waiting for packets...")
while True:
    time.sleep(0.1)
    if packet_received:
        send_udp_message("received message!")
        packet_received = False
