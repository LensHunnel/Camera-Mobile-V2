# -*- coding: cp1252 -*-
import socket
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
left_in1_pin = 7
left_in2_pin = 8
right_in1_pin = 23
right_in2_pin = 24
hote = '192.168.105.106'
port = 12801
class Motor(object):
        
        def __init__(self, in1_pin, in2_pin):
                self.in1_pin = in1_pin
                self.in2_pin = in2_pin
                self.counter = 0
               
                GPIO.setup(self.in1_pin, GPIO.OUT)
                GPIO.setup(self.in2_pin, GPIO.OUT)
                
       
        def clockwise(self):
                GPIO.output(self.in1_pin, True)    
                GPIO.output(self.in2_pin, False)
                self.delayES(3)
        def counter_clockwise(self):
                GPIO.output(self.in1_pin, False)
                GPIO.output(self.in2_pin, True)
                time.sleep(1)
               
        def stop(self):
                GPIO.output(self.in1_pin, False)    
                GPIO.output(self.in2_pin, False)
                time.sleep(1)
        """def delayES(self,tmp):
                """
class servTimer (object):
        def __init__(self):
                self.counter= 0
        def run():
                if (self.counter > 0) 
                        self.counter--;
                        if (self.counter == 0)
                        
                                print("Emergency STOP !");
                                Motor.stop();
                        	
                
                else
                
                        print("Stanby");
                
                
        
connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

connexion_avec_client, infos_connexion = connexion_principale.accept()
left_motor=Motor(left_in1_pin, left_in2_pin)
right_motor=Motor(right_in1_pin, right_in2_pin)
msg_recu = b""
while msg_recu != b"fin":
    msg_recu = connexion_avec_client.recv(1024)
    # L'instruction ci-dessous peut lever une exception si le message
    # Réceptionné comporte des accents
    cmd=msg_recu.decode()
    connexion_avec_client.send(b"5 / 5")
    print(cmd)
    if len(cmd) > 0:
        direction = cmd
    if direction == "f":
        left_motor.clockwise()
        right_motor.clockwise()
    elif direction == "r":
        left_motor.counter_clockwise()
        right_motor.counter_clockwise()
    elif direction == "o": # opposite1
        left_motor.counter_clockwise()
        right_motor.clockwise()
    elif direction == "p":
        left_motor.clockwise()
        right_motor.counter_clockwise()        
    else:
        left_motor.stop()
        right_motor.stop()
print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()
