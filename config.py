#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7038615431:AAHb5ttKWpQYHjoI16GHS38_mB5vzgIxSEI")
    API_ID = int(os.environ.get("API_ID", "26197891"))
    API_HASH = os.environ.get("API_HASH", "8f8042a517fa74243ddf8203a5acaf9e")
    AUTH_USERS = os.environ.get("AUTH_USERS", "5860841520")
