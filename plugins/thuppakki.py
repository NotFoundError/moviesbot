#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Anand PS Kerala

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import json
import math
import os
import requests
import subprocess
import time

from pyrogram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.chat_base import TRChatBase


@pyrogram.Client.on_message(pyrogram.Filters.regex(pattern=".*Thuppakki.*"))
def thupaki(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/thupaki")
    # bot.send_chat_action(
    #     chat_id=update.chat.id,
    #     action="typing"
    # )
    logger.info(update.from_user)
    keyboard = [[pyrogram.InlineKeyboardButton(text="Test File", url="https://t.me/tbk_official/457")]]
    if str(update.from_user.id) not in Config.BANNED_USERS:
        bot.send_message(
            chat_id=update.chat.id,
            text=Translation.THUPPAKKI,
            reply_markup = pyrogram.InlineKeyboardMarkup(keyboard),
            reply_to_message_id=update.message_id,
          )
          return

          
          


            