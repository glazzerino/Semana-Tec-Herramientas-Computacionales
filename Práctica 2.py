# Con este código enviamos y recibios mensajes a un tópico mqtt fijo
# nos sirve para aprender mqtt básico y observar cómo funciona.

import time
import paho.mqtt.client as mqtt

# Callback Function on Connection with MQTT Server
# Función Callback que se ejecuta cuando se conectó con el servidor MQTT
def on_connect( client, userdata, flags, rc):
    print ("Connected with Code :" +str(rc))
    # Subscribe Topic from here
    # Aprovechando que se conectó, hacemos un subscribe a los tópicos
    client.subscribe("eqp3_iot")
    

# Callback Function on Receiving the Subscribed Topic/Message
# Cuando nos llega un mensaje a los tópicos suscritos, se ejecuta
# esta función.
# Recibimos un mensaje y lo imprimimos en pantalla junto con su tópico

def on_message( client, userdata, msg):
    # print the message received from the subscribed topic

    topic = msg.topic
    m_decode = str(msg.payload.decode("utf-8","ignore"))

    print()
    print('----------------------------------------')
    print('Mensaje de llegada:', m_decode)
    print('Tópico: ', topic)
    print('----------------------------------------')

# En esta función pedimos datos al usuario un mensaje y lo enviamos al tópico en mqtt

def envia_mensaje():
    print('----------------------------------------')
    mensaje_salida = input('Mensaje:')
    client.publish("eqp3_iot",mensaje_salida)
    print('----------------------------------------')
    #time.sleep(4)

def envia_mensaje_prueba():
    print('----------------------------------------')
    mensaje_salida = 'Prueba'
    client.publish("eqp3_iot",mensaje_salida)
    print('Enviado mensaje de prueba: "Prueba"')
    print('----------------------------------------')
    #time.sleep(4)


# Generamos el cliente y las funciones para recibir mensajes y
# cuando se genera la conexión.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# Hacemos la conexión al Broker
client.connect("broker.mqtt-dashboard.com", port=1883)
# Las siguientes instrucciones son para el caso que requiera password
# client.username_pw_set("setsmjwc", "apDnKqHRgAjA")
# y para ejecutar un loop forever, nosotros haremos un loop_start()
# solamente
# client.loop_forever()
# Iniciamos el ciclo del cliente MQTT
# Por lo que se va a conectar y le damos tres segundos
client.loop_start()
time.sleep(3)

#Programa principal
opc = 'x'
while opc != 's':
    opc = input('e)nvía p)rueba s)alir ')
    if opc == 'e':
        envia_mensaje()
    elif opc == 'p':
        envia_mensaje_prueba()
    #time.sleep(1)    
  
  
# al salir paramos el loop y nos desconectamos
client.loop_stop()
client.disconnect()