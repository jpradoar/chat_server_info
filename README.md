# chat_server_info
chat para obtener info de servers usando Gtalk o hangout


INSTALAR Hangouts (Gtalk) utilizo gtalk o hangouts para enviar comandos y ejecutar acciones


apt-get install centerim screen

# Creo el directorio
root@raspberrypi:~# mkdir .centerim

# Creo el archivo de configuración donde estará la cuenta
root@raspberrypi:~# vim /root/.centerim/config

screensocketpath	/var/run/screen
chatmode icq yahoo msn aim irc jab gg
fromcharset	
tocharset	
smtp	localhost:25
browser	mozilla
ptp	0-65535
protocolormode
sort_by_status_and_activity
left_panel_width	25
log_panel_height	6
defaultauthmessage	Please accept my authorization to add you to my contact list.

jab_nick	cuenta_de_gmail@gmail.com
jab_pass	password_de_gmail
jab_server	talk.google.com:5223
jab_osinfo	1
jab_prio	4
jab_ssl	1





# Creo los comandos que va a responder.
root@raspberrypi:~# vim /root/.centerim/external

%action contestador automagico
event msg
proto all
status all
options stdin stdout
%exec
msg=`cat`
python /root/chat.py $msg
