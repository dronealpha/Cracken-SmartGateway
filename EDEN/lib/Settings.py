#Autor:Diego Silva
#Data:22/11/2018
#Descrição:Script para carregar configurações do gateway

#criando Classe para dados de rede
class SettingsNetWork:
    #declarando atributos privados
    def __init__(self):
        __ssid = None
        __password = None
        __port = None
        __host = None

    #métodos para retornar o ssid da rede
    def setSSID(self, vssid):
       self.__ssid = vssid
    def getSSID(self):
       return self.__ssid

    #métodos para retornar o p de comunicação com assword da rede
    def setPassword(self, vpass):
        self.__password = vpass
    def getPassword(self):
        return self.__password

    #métodos para retornar o porta da rede para comunicação com servidor
    def setPort(self, vport):
        self.__port = vport
    def getPort(self):
        return self.__port

    #métodos para retornar host do servidor
    def setHost(self, vhost):
        self.__host = vhost
    def getHost(self):
        return self.__host
