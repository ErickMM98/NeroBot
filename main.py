"""
Nuevo modelo de ÑeroBot

@author Erick Muñiz - ErickMM98
31/12/18
"""

import nerobotdb
from time import sleep
from threading import Thread,enumerate
from fbchat import log, Client
from fbchat import models

class NeroBot(Client):

    """

    BEGIN BASICS

    """
    def __init__(self,email,password):
        super(NeroBot,self).__init__(email,password)
        self.data = nerobotdb.read_nerobot()
        self.comandos = nerobotdb.read_comandos()
        self.patron = self.searchForUsers("Erick Muñiz")[0]
        self.limite = -50

    def _parseMessage(self, content):
        Thread(target=super(NeroBot,self)._parseMessage,args=(content,)).start()
    """
    END BASICS

    """


    """
    BEGIN FUNCIONS PROPIAS
    
    """

    def elimina_jugador(self,uid,gruop):
        pass


    """
    
    END FUNCIONES PROPIAS
    
    """


    """
    
    BEGIN MESSAGES
    
    """

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        #SI ESTÁ EN LOS COMANDOS DE EL ARCHIVO
        if message_object.text in self.comandos:
            c = models.Message(self.comandos[message_object.text])
            self.send(c, thread_id=thread_id, thread_type=thread_type)
            log.info("Comando {} usado".format(message_object.text))

        if message_object.text == "ADIOS":
            self.send(models.Message("Adios bb de luz"), thread_id=thread_id, thread_type=thread_type)
            log.info("ÑeroBot está muerto")
            self.stopListening()
            print(enumerate())






    """
    END MESSAGES
    """




if __name__ == '__main__':
    data = nerobotdb.read_nerobot()
    NeroBot(data["email"],data["pass"]).listen()