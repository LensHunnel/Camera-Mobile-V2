# coding: utf8
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

left_in1_pin = 7
left_in2_pin = 8
right_in1_pin = 23
right_in2_pin = 24

# definition des GPIO que nous allons utiliser
GPIO_TRIGGER = 25
GPIO_ECHO = 18


class Ultrason(object):
    def __init__(self):
        self.distance = -1
        GPIO.setup(GPIO_TRIGGER, GPIO.OUT)  # Trigger
        GPIO.setup(GPIO_ECHO, GPIO.IN)  # Echo
        print(" mise a zero de trigger")
        GPIO.output(GPIO_TRIGGER, False)
        time.sleep(0.5)

    def getdistance(self):
        print("Ultrasonic Measurement")
        n = 0
        all_distances = []
        while n < 10:
            # print "Envoie d'une impulsion de 10uS a  la broche Trigger"
            GPIO.output(GPIO_TRIGGER, True)
            time.sleep(0.00001)
            GPIO.output(GPIO_TRIGGER, False)
            start = time.time()
            while GPIO.input(GPIO_ECHO) == 0:
                start = time.time()

            while GPIO.input(GPIO_ECHO) == 1:
                stop = time.time()

            # print "Calcul de la longueur de l'impulsion de la broche Echo"
            elapsed = stop - start

            # print"""Distance pulse travelled in that time is time
            # multipliÃ© par la vitesse du son (cm/s)"""
            # print "That was the distance there and back so halve the value"
            all_distances.append(elapsed * 34000 / 2)
            n = n + 1
        all_distances.remove(min(all_distances))
        all_distances.remove(max(all_distances))
        self.distance = sum(all_distances)/len(all_distances)

        print("Distance : %.3f" % self.distance)
        return self.distance


class Motor(object):
    """
    Model Motor permettant la gestion d'un moteur
    """
    def __init__(self, in1_pin, in2_pin):
        self.in1_pin = in1_pin
        self.in2_pin = in2_pin
        self.counter = 0
        GPIO.setup(self.in1_pin, GPIO.OUT)
        GPIO.setup(self.in2_pin, GPIO.OUT)
    def clockwise(self):
        GPIO.output(self.in1_pin, True)
        GPIO.output(self.in2_pin, False)
    def counter_clockwise(self):
        GPIO.output(self.in1_pin, False)
        GPIO.output(self.in2_pin, True)
    def stop(self):
        GPIO.output(self.in1_pin, False)
        GPIO.output(self.in2_pin, False)      
        
u = Ultrason()
m2 = Motor(right_in1_pin, right_in2_pin)
m1 = Motor(left_in1_pin, left_in2_pin)
