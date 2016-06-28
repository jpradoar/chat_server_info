#!/usr/bin/env python
import sys
import os
import datetime
import time
import subprocess

comando = ""
i = 0
for arg in sys.argv:
 if i != 0:
  comando = comando + arg + " "
 i = i + 1
comando = comando[0:len(comando)-1]

if comando == "help":
        print "Comandos \n help\n voz\n txt\n  espacio\n uptime\n date\n w\n load\n mem\n lan\n wlan\n cal\n "

if '.txt' in comando:
    	texto = comando[0:len(comando)-4]
	print texto

if '.voz' in comando:
    	texto = comando[0:len(comando)-4]
	os.system("echo " + texto + " | festival --tts --language spanish")

if comando == "hola":
	print "Hola, soy un Linux.\n Escribe help para ver los comandos disponibles"

if comando == "espacio":
	os.system("df -ha | awk '{print $1, $5, $6}' | grep -i /dev/sd")

if comando == "uptime":
	os.system("uptime -p")

if comando == "date":
	os.system("date")

if comando == "w":
	os.system("who")

if comando == "load":
	os.system("uptime | awk {'print $7 $8 $9 $10 $11'}")

if comando == "lan":
	os.system("ifconfig eth0 |  grep Direc. | grep -v inet6 |  cut -f2 -d':' | awk {'print $1'}")

if comando == "wlan":
	os.system("ifconfig wlan0 |  grep Direc. | grep -v inet6 |  cut -f2 -d':' | awk {'print $1'}")

if comando == "cal":
	os.system("cal")

if comando == "voz":
    print "Comando: risas mujeres => ejecuta un mp3 con sonido de risas de mujeres \n "
    print "Comando:  cualquier string o texto que termine con .voz sera hablado por el sistema"

if comando == "risas mujeres":
    os.system("mpg123 /root/sonidos/risas.mp3")