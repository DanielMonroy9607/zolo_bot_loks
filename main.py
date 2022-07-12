#pip3 install flask
#pip3 install pywhatkit

import pywhatkit #importamos el paquete pywhatkit

from datetime import datetime #importamos las librerias de tiempo
import time

seconds = time.time() + 60 #en la variable segundos guardamos los segundos actuales

date = datetime.fromtimestamp(seconds) #los segundos los transformamos a una fecha

pywhatkit.sendwhatmsg("+573142299798", "hola mi nombre es frailejon", date.hour, date.minute) #enviamos un mensaje al numero de telefono
 
time.sleep(5) #espero 5 segundos
pywhatkit.sendwhats_image("+573142299798", "frailejon.jpg") #enviamos una imagen


pywhatkit.sendwhatmsg_instantly()


