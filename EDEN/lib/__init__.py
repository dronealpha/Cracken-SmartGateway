import network
from Settings import *
from ConnectionNetWork import *


#instaciando classe para configurações de rede
conf = SettingsNetWork()
conf.setHost('192.168.15.69')
conf.setPort(50001)
conf.setSSID('Casa21')
conf.setPassword('Dlink22a4')

#instanciando classe para trabalhar com access point ou station
ap_if = network.WLAN(network.AP_IF)
sta_if = network.WLAN(network.STA_IF)

#desabilitando modo accesspoint/habilitando station
ap_if.active(False)
sta_if.active(True)

msg="Conexão OK"
try:
    #conectando ao roteador
    print('Conectando a rede')
    sta_if.connect('LABORATORIO 05','lab05iot')
    #instanciando classe para criação e comunicação na rede
    cr = Communication(conf.getHost(),conf.getPort())
    print(sta_if.ifconfig())
    print('Conectando com servidor')
    cr.Connectserver()
    print('Desconectando com servidor')
    #deconnectando
    print('Desconectando roteador')
    sta_if.disconnect()
    print(sta_if.ifconfig())
except:
    msg="Erro com a conexão com o servidor"
finally:
    print(msg)

