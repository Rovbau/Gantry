try:    
  import RPi.GPIO as GPIO
except:
    #Use FakeGPIO if no Raspberry-Pi is available
    import FakeGPIO as GPIO
    GPIO.VERBOSE = False
from time import sleep
from threading import *

GPIO.setwarnings(False)

class Stepper():
    """Controls a Stepper Motor with the Modul A4988"""
    def __init__(self, name, mm_per_step, pin_dir, pin_step, polarity, actual):
        self.name = name
        self.mm_per_step = mm_per_step
        self.pin_dir = pin_dir
        self.pin_step = pin_step
        self.actual_steps = int(actual)
        self.stop = False
        self.polarity = polarity
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin_dir,GPIO.OUT)
        GPIO.setup(pin_step,GPIO.OUT)
        GPIO.output(pin_dir, False)
        GPIO.output(pin_step, False)

    def get_actual_steps(self):
        """Get the actual Motor Position"""
        return(self.name, self.actual_steps)

    def set_actual_steps(self, actual_steps):
        """Set the actual Motor Position"""
        self.actual_steps = actual_steps

    def stopping(self):
        print("Stepper gets Stop command")
        self.stop = True

    def pause(self, sleep_time):
        for i in range(sleep_time): 
            if self.stop == True:
                return
            sleep(1)
               
    def goto_pos(self, lenght):
        """Set Motor to desired position. Input: lentht[mm]"""
        self.stop = False

        if self.polarity == "reversed":
            lenght = lenght * (-1)
        elif self.polarity == "normal":
            pass
        else:
            print("Motor direction wrong, nust be 'normal' or 'reversed'")
    
        steps = int(lenght / self.mm_per_step)
        print(str(self.name) + " " + str(lenght) + " mm")
        while steps != self.actual_steps:
            print(str(self.name) + " " + str(self.actual_steps))
            if self.stop == True:
                return
            
            if steps >= self.actual_steps:
                self.do_step(1)
                self.actual_steps += 1
            else:
                self.do_step(-1)
                self.actual_steps -= 1
        print(self.name + " stopped")
          
    def do_step(self, steps, speed = 0.002):
        """Do Motor Steps. +steps or -steps changes direction)"""
        if steps > 0:
            GPIO.output(self.pin_dir, True)
        elif steps < 0:
            GPIO.output(self.pin_dir, False)
        else:
            return

        for x in range(abs(steps)):
            GPIO.output(self.pin_step, True)
            sleep(speed / 2)
            GPIO.output(self.pin_step, False)
            sleep(speed / 2)


if __name__ == "__main__":
    
    stepper1 = Stepper("Z-axis", mm_per_step = 0.05, pin_dir = 35, pin_step = 31, polarity = "normal", actual=0)
    stepper2 = Stepper("X-axis", mm_per_step = 0.22, pin_dir = 37, pin_step = 33, polarity = "reversed", actual=0)
    for i in range(5):
        stepper1.goto_pos(-200)
        sleep(3)
        stepper1.goto_pos(0)
        sleep(3)
        stepper2.goto_pos(300)
        sleep(7)
        stepper2.goto_pos(0)
        sleep(7)
        print("loop")
    print(stepper1.get_actual_steps())

    #stepper2 = Stepper("Right", mm_per_step = 0.10, pin_dir = 31, pin_step = 33, actual = 0)
    #stepper2.goto_pos(-200)
