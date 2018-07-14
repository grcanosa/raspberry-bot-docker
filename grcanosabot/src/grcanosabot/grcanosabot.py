#!/usr/bin/python3

import os
import logging

from basebot.tokens import TOKEN_GRCANOSABOT,CID_GRCANOSA
from basebot.basebot import BaseBot

from basebot.handlers.piropos import PiropoList
from basebot.users.userregistry import UserRegistry

from grcanosabot.sarapiropos import SaraPiropoList

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)




class GrcanosaBot(BaseBot):
    def __init__(self,logfolder,datafolder):
        super().__init__(TOKEN_GRCANOSABOT)
        self._logFile = os.path.join(logfolder,"grcanosa.users.reg")
        self._datafolder = datafolder
        self._userR = UserRegistry(self._logFile,admin_cid=CID_GRCANOSA)
        self.install_handlers()

    def install_handlers(self):
        self._userR.install(self._updater)


        PiropoList(cmdget="dimealgobonito",cmdadd="addpiropo",
                    filename=os.path.join(self._datafolder,"piropos.txt"),
                    updater=self._updater,userR=self._userR,priority=50)

        # CatGifList(cmdget="cat",cmdadd="",
        #             filename=self._datafolder+"/cats",
        #             updater=self._updater,userR=self._userR,priority=50)

        SaraPiropoList(cmdget="dimealgorealmentebonito",cmdadd="addpiroposara",
                    filename=os.path.join(self._datafolder,"sarapiropos.txt"),
                    updater=self._updater,userR=self._userR,priority=50)

        # RandomEmoji(cmdget="randomemoji",cmdadd="addemoji",
        #             filename=self._datafolder+"/emojis.txt",
        #             updater=self._updater,userR=self._userR,priority=50)

        # FixedResponse(cmd="help",response=self.get_help(),
        #                 updater=self._updater,userR=self._userR,priority=50)



    def get_help(self):
        text = "Soy grcanosabot, y esto es lo que puedo hacer: \n"
        text += "/help - Muestra esta ayuda. \n"
        text += "/dimealgobonito - Pide un piropo, o si añades Nombre Apellidos manda un piropo a otra persona. \n"
        # text += "/addpiropo - Añade un piropo a la lista escribiendo el piropo después del comando.\n"
        # text += "/randomemoji - Pide un emoji aleatorio \n"
        # #text += "/addemoji EMOJI A AÑADIR -  Añade un emoji a la lista \n"
        # text += "/cat - Pide un gato!! \n"

        return text



def main(*args, **kw):
    n = GrcanosaBot("","/data/")
    n.start()
    n.idle()