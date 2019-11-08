"""
Paquetería par aloja la información de los usuarios en cada grupo para
NeroBot
@author Erick Muñiz Morales

"""

import json


def read_nerobot():
    with open("nerobotdb/nerobot.json","r",encoding='utf-8') as file:
        dic = json.load(file)
        file.close()
        return dic

def write_nerobot(new_data):
    with open("nerobotdb/nerobot.json","w",encoding='utf-8') as file:
        json.dump(new_data,file)
        file.close()


def read_comandos():
    with open("nerobotdb/comandos.json","r",encoding='utf-8') as file:
        dic = json.load(file)
        file.close()
        return dic

def read_group(name):
    with open("nerobotdb/groups/{}.json".format(name),"r",encoding='utf-8') as file:
        dic = json.load(file)
        file.close()
        return dic

def write_group(name,data):
    with open("nerobotdb/groups/{}.json".format(name),"w",encoding='utf-8') as file:
        json.dump(data,file)
        file.close()