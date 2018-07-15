#!/usr/bin/python3

import logging
import random
import os

from telegram.ext import CommandHandler;
from telegram import Bot,Update;
from telegram.ext import Updater;

logger = logging.getLogger(__name__)

class FixedResponse:
    def __init__(self,cmd = "",response = "",updater=None,userR = None,phrasetype = "message",priority = 50):
        self._cmd = cmd;
        self._response = response
        self._type = phrasetype;
        self._userR = userR;
        self._up = updater;
        self._priority = priority;
        logger.debug("Creating fixed reponse for cmd: "+self._cmd);
        self.install_handler();


    def install_handler(self):
        if self._cmd is not "":
            self._up.dispatcher.add_handler(CommandHandler(self._cmd,self.process),self._priority);

    def process(self,bot,update):
        self._userR.inc_cmd(update.message.from_user.id,self._cmd);
        if self._type == "message":
            bot.send_message(chat_id=update.message.chat_id,text=self._response);
        elif self._type == "gif":
            bot.send_document(chat_id=update.message.chat_id,document=open(self._resp,'rb'));
        elif self._type == "voice":
            bot.sendVoice(chat_id=update.message.chat_id,voice=self._resp)
        elif self._type == "audio":
            bot.send_audio(chat_id=update.message.chat_id,audio=self._resp);
