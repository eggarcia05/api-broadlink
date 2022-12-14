#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : PI Integracion de sistemas IoT (Pilco - García)
# Created Date: 30/7/22
# version ='1.0'

import sys
import requests
import broadlink
import time
import kaiTemp as kaiterra

macRM=bytes(b'$\xdf\xa7P\x12\x14')
temp=0.0

#Señales IR

on = b'&\x00\xbc\x01r8\x10\r\x0c-\x0e\x0e\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0e\x0f\x10\x0c\x0f\x0e\x0f\x0e\x0e*\x0f\x0e\x0e\x0e\x0e\x0f\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\r,\x10)\x0f*\x0f\x0e\x0e\x0e\x0f*\x10\r\r\x0f\x0f\x0e\x0e\x0e\x0f\x0e\r\x0f\x0f\x0e\r\x0f\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\r\x0f\x10\r\r\x0f\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x10\r\r\x0f\x0f\x0e\x0c\x10\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\r\x0f\x10)\x0e+\x0f\x0e\x0f\r\x10\r\x0c\x10\x0f\x0e\x0f\x00\x01Tr9\x0e\x0e\x0e+\x0e\x0f\x0f\r\x10\r\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x10\x0c\x0e\x0f\x0e\x0e\x0e\x0f\x0f*\x0f\r\x0e\x0f\x0e\x0e\r\x10\r\x0f\x0f\x0e\x0f\r\x0f*\x0f*\x0e+\x0f\x0e\x0f\r\x0f*\x0e\x0f\x0f\r\x0e\x0f\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x12\n\x10\r\x0f\x0e\x0e\x0e\x0f*\x0f\x0e\r\x0f\x0f\x0e\x0e+\x0e+\x10\x0c\r\x10\x10\x0c\x0e\x0f\r\x0f\x0f\x0e\x0e+\r,\x0f\r\r\x10\x0e\x0e\x0f\x0e\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0f\r\x0f*\x0f*\x11(\x0e+\x0f*\x0f*\x0e\x0f\x0f*\x10\x0c\x0f\x0e\x0f\r\x0f\x0e\x0e\x0e\x0e\x0f\x0f\r\x0e\x0f\r\x0f\x0f\x0e\x0f\x0e\x0e\x0e\x0f\r\r\x10\x0e\x0e\x10\r\x0f\x0e\x0e\x0e\x0f*\x0f*\x13\t\x10\r\x0f\x0e\x0e\x0e\x0f\x0e\x10\x0c\x0f\x0e\x0e\x0e\x0e\x0f\x10\x0c\x0f*\x0f*\x13\n\x10\x0c\x0e\x0f\x0e\x0e\x0f\x0e\x0f\r\x0f\x0e\x0e\x0e\r\x10\x0e\x0e\x11\x0c\x0f\r\x0f\x0e\x0f\r\x0e\x0f\x0f\r\x0e\x0f\x0f*\x0f\r\x0f\x0e\x0f\r\r\x10\x0e\x0e\x11\x0c\r,\x0f\r\x0f\x0e\x0f\r\x0e\x0f\x0f\r\x0e\x0f\x12\n\x0f\x0e\x0f\x0e\x0e\x0e\x0e\x0e\r\x10\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0f*\x0f\x0e\r,\x0e+\x0e\x0e\x0f*\x10\r\x0e\x0e\x0e\x00\r\x05'

off = b'&\x00\xbc\x01r8\x0f\x0e\x0f*\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f*\x0f\x0e\x0f\r\x0f\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f*\x0f*\x0f*\x0f\x0e\x0e\x0e\x0f*\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e*\x0f*\x0f\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x00\x01Tr9\x0f\r\x0f*\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\x0e\x0e\x0e\x0f*\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e+\x0e+\x0f*\x0f\r\x0f\x0e\x0f*\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f*\x0f*\x0f\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e+\x0e+\x0e\x0e\x0f*\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f*\x0f*\x0f*\x0f*\x0f*\x0f*\x0f*\x0f*\x0f\r\x0f\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f*\x0f*\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f*\x0f*\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f*\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f*\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\x0e\x0e\x0e\x0f*\x0f\x0e\x0e\x0e\x0f*\x0f\x0e\x0e\x00\r\x05'

subirTemp = b'&\x00\xbc\x01r8\x10\r\x0c-\x0e\x0e\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0e\x0f\x10\x0c\x0f\x0e\x0f\x0e\x0e*\x0f\x0e\x0e\x0e\x0e\x0f\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\r,\x10)\x0f*\x0f\x0e\x0e\x0e\x0f*\x10\r\r\x0f\x0f\x0e\x0e\x0e\x0f\x0e\r\x0f\x0f\x0e\r\x0f\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\r\x0f\x10\r\r\x0f\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x10\r\r\x0f\x0f\x0e\x0c\x10\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\r\x0f\x10)\x0e+\x0f\x0e\x0f\r\x10\r\x0c\x10\x0f\x0e\x0f\x00\x01Tr9\x0e\x0e\x0e+\x0e\x0f\x0f\r\x10\r\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x10\x0c\x0e\x0f\x0e\x0e\x0e\x0f\x0f*\x0f\r\x0e\x0f\x0e\x0e\r\x10\r\x0f\x0f\x0e\x0f\r\x0f*\x0f*\x0e+\x0f\x0e\x0f\r\x0f*\x0e\x0f\x0f\r\x0e\x0f\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x12\n\x10\r\x0f\x0e\x0e\x0e\x0f*\x0f\x0e\r\x0f\x0f\x0e\x0e+\x0e+\x10\x0c\r\x10\x10\x0c\x0e\x0f\r\x0f\x0f\x0e\x0e+\r,\x0f\r\r\x10\x0e\x0e\x0f\x0e\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0f\r\x0f*\x0f*\x11(\x0e+\x0f*\x0f*\x0e\x0f\x0f*\x10\x0c\x0f\x0e\x0f\r\x0f\x0e\x0e\x0e\x0e\x0f\x0f\r\x0e\x0f\r\x0f\x0f\x0e\x0f\x0e\x0e\x0e\x0f\r\r\x10\x0e\x0e\x10\r\x0f\x0e\x0e\x0e\x0f*\x0f*\x13\t\x10\r\x0f\x0e\x0e\x0e\x0f\x0e\x10\x0c\x0f\x0e\x0e\x0e\x0e\x0f\x10\x0c\x0f*\x0f*\x13\n\x10\x0c\x0e\x0f\x0e\x0e\x0f\x0e\x0f\r\x0f\x0e\x0e\x0e\r\x10\x0e\x0e\x11\x0c\x0f\r\x0f\x0e\x0f\r\x0e\x0f\x0f\r\x0e\x0f\x0f*\x0f\r\x0f\x0e\x0f\r\r\x10\x0e\x0e\x11\x0c\r,\x0f\r\x0f\x0e\x0f\r\x0e\x0f\x0f\r\x0e\x0f\x12\n\x0f\x0e\x0f\x0e\x0e\x0e\x0e\x0e\r\x10\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0f*\x0f\x0e\r,\x0e+\x0e\x0e\x0f*\x10\r\x0e\x0e\x0e\x00\r\x05'

bajarTemp = b'&\x00\xbc\x01r8\x0f\x0e\x0f*\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f*\x0f\x0e\x0f\r\x0f\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f*\x0f*\x0f*\x0f\x0e\x0e\x0e\x0f*\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e*\x0f*\x0f\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x00\x01Tr9\x0f\r\x0f*\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\x0e\x0e\x0e\x0f*\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e+\x0e+\x0f*\x0f\r\x0f\x0e\x0f*\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f*\x0f*\x0f\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e+\x0e+\x0e\x0e\x0f*\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f*\x0f*\x0f*\x0f*\x0f*\x0f*\x0f*\x0f*\x0f\r\x0f\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f*\x0f*\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f*\x0f*\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f*\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f*\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\x0e\x0e\x0e\x0f*\x0f\x0e\x0e\x0e\x0f*\x0f\x0e\x0e\x00\r\x05'


def search(rm):
    dev = broadlink.discover() #se descubre la lista de dispositivos Broadlink en red local
    if len(dev)>0:
        for i in range(0,len(dev)):
            if macRM == dev[i].mac: #comparamos la mac de nuestro dispositivo
                rm.append(dev[i]) #redefinimos el divice final con el que se trabajará
                rm[1].auth()
                rm[1].set_name("CONTROL AC LST")
                print("Conectando a red...")
                time.sleep(2)
                print(rm[1].name,"conectado a: Lab. Telemática...", "IP:",rm[1].host[0])
                rm[0] = False
                return rm
            else:
                print("No se encontro su dispositivo","\nVerifique la conexión a la red local \"Lab. Telemática\"")
    else:
        print("Ningún dispositivo encontrado","\nVerificar que su Broadlink esté conectado a la red local \"Lab. Telemática\"")
    
def controlAC(temp, tempReq, rm):
    variarTemp = int(abs(temp-tempReq))
    #Control de temperatura
    if temp < tempReq: #se tiene que incrementar la temperatura tempReq-temp veces
        rm[1].send_data(on) #Encender AC
        time.sleep(2)
        for i in range(variarTemp):
            rm[1].send_data(subirTemp)
            time.sleep(2)
        print("Se ha subido",variarTemp,"°C la temperatura")
    elif temp > tempReq:  #se tiene que disminuir la temperatura temp-tempReq veces
        rm[1].send_data(on) #Encender AC
        time.sleep(2)
        for i in range(variarTemp):
            rm[1].send_data(bajarTemp)
            time.sleep(2)
        print("Se ha disminuido",variarTemp,"°C la temperatura")
    else:
        print("Temperatura de LST (IDEAL)")
        rm[1].send_data(off) #Apagar AC
                
if __name__ == "__main__":
    tempReq=23.0 #Se obtiene por seteo de usuario (desde Interfaz)
    rm=[True]
    while rm[0]:
        rm=search(rm)
    
    while True:
        temp=kaiterra.summarize_laser_egg("dd85475c-a5ef-4a15-b00f-206e408528b2") #obtener valor de temp <float>
        controlAC(temp, tempReq, rm)
        time.sleep(60)
        
