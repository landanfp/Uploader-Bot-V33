#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import ntplib
import time
from datetime import datetime, timezone

def sync_ntp_time():
    try:
        ntp_client = ntplib.NTPClient()
        response = ntp_client.request('pool.ntp.org')
        current_time = datetime.fromtimestamp(response.tx_time, timezone.utc)
        print(f"[Time Sync] NTP Time: {current_time}")
        time_offset = response.tx_time - time.time()
        print(f"[Time Sync] Time offset: {time_offset:.2f} seconds")
    except Exception as e:
        print(f"[Time Sync] NTP sync failed: {e}")

sync_ntp_time()

import os
from plugins.config import Config

from pyrogram import Client as Tellybots
from pyrogram import filters
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)

    plugins = dict(root="plugins")
    Tellybots = Tellybots(
        "Uploader Bot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    Tellybots.run()
