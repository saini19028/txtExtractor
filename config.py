#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN","7212422592:AAEvCT6zaZbzDiDRTcIH_-RkxXgnxylUqnc")
    API_ID = int(os.environ.get("API_ID", "28235190"))
    API_HASH = os.environ.get("API_HASH", "a685e1bccefafc462baf123cff9a1be3")
    AUTH_USERS = os.environ.get("AUTH_USERS", "7944235618")
