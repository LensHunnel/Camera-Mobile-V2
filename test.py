import time
import threading
class servTimer (object):
    counter=0
    def __init__(self):
            counter= 0
    @staticmethod
    def run():
        global counter
        if (counter > 0):
            counter -=counter
            if (counter == 0):
                print("Emergency STOP !")
                #Motor.stop();
        else:
            print("Stanby")
        print counter
class Motor(object):
        
        def __init__(self, in1_pin, in2_pin):
                self.in1_pin = in1_pin
                self.in2_pin = in2_pin

                
       
        def clockwise(self):
                print("""GPIO.output(self.in1_pin, True)    
                GPIO.output(self.in2_pin, False)
                self.delayES(3)""")
                self.delayES(7)
        def counter_clockwise(self):
                print("""GPIO.output(self.in1_pin, False)
                GPIO.output(self.in2_pin, True)
                time.sleep(1)""")
                self.delayES(7)
        @staticmethod       
        def stop():
                print("""stop""")
                
        def delayES(self,tmp):
            t = threading.Timer(tmp,hello)
            t.start()
def hello():
    print "stop"
if __name__=="__main__":
    counter = 0
    t = threading.Timer(1.0,servTimer.run)
    t.start()
    m1=Motor(1,2)
    m2=Motor(3,4)
    m1.clockwise()
    print servTimer.counter
    m2.counter_clockwise()
    print servTimer.counter
    i=0
    while True:
        print "i: ",i
        i+=1
        if i%5==0:
            t = threading.Timer(3.0,Motor.stop)
            t.start()
        time.sleep(1)
