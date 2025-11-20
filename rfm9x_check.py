# SPDX-FileCopyrightText: 2018 Brent Rubell for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
Wiring Check, Pi Radio w/RFM9x

Learn Guide: https://learn.adafruit.com/lora-and-lorawan-for-raspberry-pi
Author: Brent Rubell for Adafruit Industries
"""
import time
import logging
import busio
from digitalio import DigitalInOut, Direction, Pull
import board

# Import the RFM9x radio module.
import adafruit_rfm9x

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configure RFM9x LoRa Radio
CS = DigitalInOut(board.D25)
RESET = DigitalInOut(board.D18)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

while True:

    # Attempt to set up the RFM9x Module
    try:
        rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
        logger.info('RFM9x: Detected')
    except RuntimeError as error:
        # Thrown on version mismatch
        logger.error(f'RFM9x Error: {error}')

    time.sleep(5)

