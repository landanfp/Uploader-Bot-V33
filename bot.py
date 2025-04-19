#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import asyncio
import time
from datetime import datetime, timezone

import ntplib
from pyrogram import Client as Tellybots
from pyrogram import filters
from pyrogram.idle import idle

from plugins.config import Config

# تنظیمات لاگ
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# سینک کردن ساعت با NTP
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

# تعریف بات با افزونه‌ها
plugins = dict(root="plugins")
app = Tellybots(
    "Uploader Bot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    plugins=plugins
)

# تابع اصلی async
async def main():
    # ساخت دایرکتوری دانلود اگر وجود ندارد
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)

    print("Waiting to sync time with Telegram servers...")
    await asyncio.sleep(3)  # تأخیر برای جلوگیری از BadMsgNotification در Koyeb

    await app.start()
    print("Bot started successfully.")
    await idle()
    await app.stop()

# اجرای برنامه
if __name__ == "__main__":
    asyncio.run(main())
