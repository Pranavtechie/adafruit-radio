# SPDX-FileCopyrightText: 2018 Brent Rubell for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
Example for using the RFM9x Radio with Raspberry Pi.

Learn Guide: https://learn.adafruit.com/lora-and-lorawan-for-raspberry-pi
Author: Brent Rubell for Adafruit Industries
"""
# Import Python System Libraries
import time
import logging
# Import Blinka Libraries
import busio
from digitalio import DigitalInOut, Direction, Pull
import board

# Import RFM9x
import adafruit_rfm9x

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configure LoRa Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)

# config
rfm9x.signal_bandwidth = 125000
rfm9x.coding_rate = 7 
rfm9x.spreading_factor = 9
rfm9x.enable_crc = True
rfm9x.preamble_length = 8
rfm9x.tx_power = 5
prev_packet = None

it = 0
while True:
   # if it % 100 == 0:
    #    rfm9x.send(bytes(f"Ping {it // 100}", "utf-8"))

    packet = None
    logger.debug('RasPi LoRa')

    # check for packet rx
    packet = rfm9x.receive()
    if packet is None:
        logger.debug('- Waiting for PKT -')
    else:
        # Display the packet text and rssi
        prev_packet = packet
        packet_text = str(prev_packet, "utf-8")
        logger.info(f'RX: {packet_text}')
        time.sleep(1)

    time.sleep(0.1)
