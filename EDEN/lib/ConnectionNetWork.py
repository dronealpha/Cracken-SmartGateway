#Autor:Diego Silva
#Data:22/11/2018
#Descrição:Retornar objetos paa conexão

#importando biblioteca para trabalhar com socket
from socket import *
import time
#cria conexões com servidor via rede
class Communication:
    def __init__(self, host, port):
        self.host= host
        self.port = port
        
    def Connectserver(self):
        soc = socket(AF_INET, SOCK_STREAM)
        soc.connect((self.host, self.port))
        #soc.send(b'A')
        #print(soc.recv(1024))
        time.sleep(5)
        soc.close()
