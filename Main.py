#! python
# -*- coding: utf-8 -*-

# GUI fuer Gantry 
from Stepper import *
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import font
from datetime import datetime, timedelta
from threading import *
import atexit
from time import sleep, time, strftime
import Limits
from pprint import pprint

class Gui():
    def __init__(self, root):
        """Do GUI stuff and attach to ObserverPattern"""
        self.root = root

        #Root Window
        self.root.title ("ArmInator")
        self.root.geometry("600x600+0+0")

        #Change default Textfont
        standart_font = font.nametofont("TkDefaultFont")
        standart_font.configure(size=9, family="Segoe UI")
        root.option_add("*Font", standart_font)
  

        #*************************  Left  ******************************
        self.label_anzahl_beh =         Label(root, text="Anzahl Behälter")
        self.label_wiederholung =       Label(root, text="Anzahl Wiederholungen")
        self.label_eintauchzeit =       Label(root, text=" Eintauchzeiten ", font=("Segoe UI underline", 15, "underline"))
        self.label_lagern =             Label(root, text="Am Ende Probe hier lagern" )
        self.label_dauer_1 =            Label(root, text="Behälter - 1")
        self.label_dauer_2 =            Label(root, text="Behälter - 2")
        self.label_dauer_3 =            Label(root, text="Behälter - 3")
        self.label_dauer_4 =            Label(root, text="Behälter - 4")
        self.label_dauer_5 =            Label(root, text="Behälter - 5")
        self.label_dauer_6 =            Label(root, text="Behälter - 6")
        self.label_dauer_7 =            Label(root, text="Behälter - 7")
        self.label_dauer_8 =            Label(root, text="Behälter - 8")        
        #OptionMenu
        self.var_anzahl_beh = StringVar(root) 
        self.var_anzahl_beh.set(8)
        self.var_anzahl_beh.trace_add('write', self.behaelter_anzahl_changed)
        options = [2,3,4,5,6,7,8] 
        self.option_anzahl_beh = OptionMenu(root, self.var_anzahl_beh, *options)
        #Counter variable
        self.counter = 0
        self.var_counter = StringVar(root)
        self.var_counter.set("Test: _ / _ ")
        #Entries
        self.var_wiederholung = StringVar()
        self.entry_wiederholung =       Entry(root, width = 10, textvariable = self.var_wiederholung, validate="key")
        self.entry_wiederholung.configure(validatecommand = (self.entry_wiederholung.register(self.test_user_input),'%P','%d'))
        self.entry_wiederholung.insert(0, "2")

        self.var_eintauchzeit1 = StringVar()
        self.entry_eintauchzeit1 =       Entry(root, width = 10, textvariable = self.var_eintauchzeit1, validate="key")
        self.entry_eintauchzeit1.configure(validatecommand = (self.entry_eintauchzeit1.register(self.test_user_input),'%P','%d'))
        self.entry_eintauchzeit1.insert(0, "1") 
        self.var_eintauchzeit2 = StringVar()
        self.entry_eintauchzeit2 =       Entry(root, width = 10, textvariable = self.var_eintauchzeit2, validate="key")
        self.entry_eintauchzeit2.configure(validatecommand = (self.entry_eintauchzeit2.register(self.test_user_input),'%P','%d'))
        self.entry_eintauchzeit2.insert(0, "2") 
        self.var_eintauchzeit3 = StringVar()
        self.entry_eintauchzeit3 =       Entry(root, width = 10, textvariable = self.var_eintauchzeit3, validate="key")
        self.entry_eintauchzeit3.configure(validatecommand = (self.entry_eintauchzeit3.register(self.test_user_input),'%P','%d'))
        self.entry_eintauchzeit3.insert(0, "3") 
        self.var_eintauchzeit4 = StringVar()
        self.entry_eintauchzeit4 =       Entry(root, width = 10, textvariable = self.var_eintauchzeit4, validate="key")
        self.entry_eintauchzeit4.configure(validatecommand = (self.entry_eintauchzeit4.register(self.test_user_input),'%P','%d'))
        self.entry_eintauchzeit4.insert(0, "4") 
        self.var_eintauchzeit5 = StringVar()
        self.entry_eintauchzeit5 =       Entry(root, width = 10, textvariable = self.var_eintauchzeit5, validate="key")
        self.entry_eintauchzeit5.configure(validatecommand = (self.entry_eintauchzeit5.register(self.test_user_input),'%P','%d'))
        self.entry_eintauchzeit5.insert(0, "5")
        self.var_eintauchzeit6 = StringVar()
        self.entry_eintauchzeit6 =       Entry(root, width = 10, textvariable = self.var_eintauchzeit6, validate="key")
        self.entry_eintauchzeit6.configure(validatecommand = (self.entry_eintauchzeit6.register(self.test_user_input),'%P','%d'))
        self.entry_eintauchzeit6.insert(0, "6")
        self.var_eintauchzeit7 = StringVar()
        self.entry_eintauchzeit7 =       Entry(root, width = 10, textvariable = self.var_eintauchzeit7, validate="key")
        self.entry_eintauchzeit7.configure(validatecommand = (self.entry_eintauchzeit7.register(self.test_user_input),'%P','%d'))
        self.entry_eintauchzeit7.insert(0, "7")
        self.var_eintauchzeit8 = StringVar()
        self.entry_eintauchzeit8 =       Entry(root, width = 10, textvariable = self.var_eintauchzeit8, validate="key")
        self.entry_eintauchzeit8.configure(validatecommand = (self.entry_eintauchzeit8.register(self.test_user_input),'%P','%d'))
        self.entry_eintauchzeit8.insert(0, "8")

        self.entry_array =  (self.var_eintauchzeit1,
                             self.var_eintauchzeit2,
                             self.var_eintauchzeit3,
                             self.var_eintauchzeit4,
                             self.var_eintauchzeit5,
                             self.var_eintauchzeit6,
                             self.var_eintauchzeit7,
                             self.var_eintauchzeit8
                             )
        #Radiobutton
        self.var_testende = StringVar(value="8")         #Initial Value for radiobuttons
        self.radiobutton_enlager_1 =   Radiobutton(root, text="", variable = self.var_testende, value="1")
        self.radiobutton_enlager_2 =   Radiobutton(root, text="", variable = self.var_testende, value="2")
        self.radiobutton_enlager_3 =   Radiobutton(root, text="", variable = self.var_testende, value="3")
        self.radiobutton_enlager_4 =   Radiobutton(root, text="", variable = self.var_testende, value="4")
        self.radiobutton_enlager_5 =   Radiobutton(root, text="", variable = self.var_testende, value="5")
        self.radiobutton_enlager_6 =   Radiobutton(root, text="", variable = self.var_testende, value="6")
        self.radiobutton_enlager_7 =   Radiobutton(root, text="", variable = self.var_testende, value="7")
        self.radiobutton_enlager_8 =   Radiobutton(root, text="", variable = self.var_testende, value="8")
        #Units
        self.label_einheit_1 =         Label(root, text="Sekunden")
        self.label_einheit_2 =         Label(root, text="Sekunden")   
        self.label_einheit_3 =         Label(root, text="Sekunden")
        self.label_einheit_4 =         Label(root, text="Sekunden")
        self.label_einheit_5 =         Label(root, text="Sekunden")
        self.label_einheit_6 =         Label(root, text="Sekunden")
        self.label_einheit_7 =         Label(root, text="Sekunden")
        self.label_einheit_8 =         Label(root, text="Sekunden")
        #Buttons
        self.button_start =            Button(root, text="Start", fg="green", command=self.start_test, width = 20)
        #self.button_pause =            Button(root, text="Pause", fg="orange" ,command=self.pause_test, width = 20)
        self.button_abbrechen =        Button(root, text="Abbrechen", fg="red" ,command=self.stop_test, width = 20)
        self.button_status =           Button(root, textvariable = self.var_counter, 
            bg = "gray85", relief = GROOVE, borderwidth = 4, width = 20, height= 4)

        #Place label Left
        space = 40
        self.label_anzahl_beh.place          (x= 10,  y = space*1)     
        self.label_wiederholung.place        (x= 10,  y = space*2)
        self.label_eintauchzeit.place        (x= 10,  y = space*3)
        self.label_lagern.place              (x= 300, y = space*4)
        self.label_dauer_1.place             (x= 10,  y = space*5)
        self.label_dauer_2.place             (x= 10,  y = space*6)
        self.label_dauer_3.place             (x= 10,  y = space*7)
        self.label_dauer_4.place             (x= 10,  y = space*8)
        self.label_dauer_5.place             (x= 10,  y = space*9)
        self.label_dauer_6.place             (x= 10,  y = space*10)
        self.label_dauer_7.place             (x= 10,  y = space*11)
        self.label_dauer_8.place             (x= 10,  y = space*12)   
        #OptionMenu
        self.option_anzahl_beh.place         (x= 200, y = space*1, width= 50)
        #Entries
        self.entry_wiederholung.place        (x= 200, y = space*2, width= 50)  
        self.entry_eintauchzeit1.place       (x= 150, y = space*5, width= 50)
        self.entry_eintauchzeit2.place       (x= 150, y = space*6, width= 50)
        self.entry_eintauchzeit3.place       (x= 150, y = space*7, width= 50)
        self.entry_eintauchzeit4.place       (x= 150, y = space*8, width= 50)
        self.entry_eintauchzeit5.place       (x= 150, y = space*9, width= 50)
        self.entry_eintauchzeit6.place       (x= 150, y = space*10, width= 50)
        self.entry_eintauchzeit7.place       (x= 150, y = space*11, width= 50)
        self.entry_eintauchzeit8.place       (x= 150, y = space*12, width= 50)
        #Radiobuttons
        self.radiobutton_enlager_1.place     (x= 350, y = space*5)
        self.radiobutton_enlager_2.place     (x= 350, y = space*6)
        self.radiobutton_enlager_3.place     (x= 350, y = space*7)
        self.radiobutton_enlager_4.place     (x= 350, y = space*8)
        self.radiobutton_enlager_5.place     (x= 350, y = space*9)
        self.radiobutton_enlager_6.place     (x= 350, y = space*10)
        self.radiobutton_enlager_7.place     (x= 350, y = space*11)
        self.radiobutton_enlager_8.place     (x= 350, y = space*12)
        #Units
        self.label_einheit_1.place           (x= 220, y = space*5)
        self.label_einheit_2.place           (x= 220, y = space*6)
        self.label_einheit_3.place           (x= 220, y = space*7)
        self.label_einheit_4.place           (x= 220, y = space*8)
        self.label_einheit_5.place           (x= 220, y = space*9)
        self.label_einheit_6.place           (x= 220, y = space*10)
        self.label_einheit_7.place           (x= 220, y = space*11)
        self.label_einheit_8.place           (x= 220, y = space*12)
        #Buttons
        self.button_status.place             (x= 380,  y = space*1)
        self.button_start.place              (x= 10,  y = space*13) 
        #self.button_pause.place              (x= 200, y = space*13)
        self.button_abbrechen.place          (x= 380, y = space*13)

        #Init motors
        self.stepper_Z = Stepper("Z-axis", mm_per_step = 0.05, pin_dir = 35, pin_step = 31, polarity="normal", actual=0)
        self.stepper_X = Stepper("X-axis", mm_per_step = 0.22, pin_dir = 37, pin_step = 33, polarity="reversed", actual=0)


    def behaelter_anzahl_changed(self, var, index, mode):
        print("Behälter anzahl")
        self.entry_eintauchzeit1.config(state="disabled")
        self.radiobutton_enlager_1.config(state="disabled")
        self.entry_eintauchzeit2.config(state="disabled")
        self.radiobutton_enlager_2.config(state="disabled")
        self.entry_eintauchzeit3.config(state="disabled")
        self.radiobutton_enlager_3.config(state="disabled")
        self.entry_eintauchzeit4.config(state="disabled")
        self.radiobutton_enlager_4.config(state="disabled")
        self.entry_eintauchzeit5.config(state="disabled")
        self.radiobutton_enlager_5.config(state="disabled")
        self.entry_eintauchzeit6.config(state="disabled")
        self.radiobutton_enlager_6.config(state="disabled")
        self.entry_eintauchzeit7.config(state="disabled")
        self.radiobutton_enlager_7.config(state="disabled")
        self.entry_eintauchzeit8.config(state="disabled")
        self.radiobutton_enlager_8.config(state="disabled")
        if self.var_anzahl_beh.get() == "1":
            print("eins")
            self.entry_eintauchzeit1.config(state="normal")
            self.radiobutton_enlager_1.config(state="normal")
            self.radiobutton_enlager_1.select()
        elif self.var_anzahl_beh.get() == "2":
            print("zwei")
            self.entry_eintauchzeit1.config(state="normal")
            self.radiobutton_enlager_1.config(state="normal")
            self.entry_eintauchzeit2.config(state="normal")
            self.radiobutton_enlager_2.config(state="normal")
            self.radiobutton_enlager_2.select()
        elif self.var_anzahl_beh.get() == "3":
            print("drei")
            self.entry_eintauchzeit1.config(state="normal")
            self.radiobutton_enlager_1.config(state="normal")
            self.entry_eintauchzeit2.config(state="normal")
            self.radiobutton_enlager_2.config(state="normal")
            self.entry_eintauchzeit3.config(state="normal")
            self.radiobutton_enlager_3.config(state="normal")
            self.radiobutton_enlager_3.select()
        elif self.var_anzahl_beh.get() == "4":
            print("vier")
            self.entry_eintauchzeit1.config(state="normal")
            self.radiobutton_enlager_1.config(state="normal")
            self.entry_eintauchzeit2.config(state="normal")
            self.radiobutton_enlager_2.config(state="normal")
            self.entry_eintauchzeit3.config(state="normal")
            self.radiobutton_enlager_3.config(state="normal")
            self.entry_eintauchzeit3.config(state="normal")
            self.radiobutton_enlager_3.config(state="normal")
            self.entry_eintauchzeit4.config(state="normal")
            self.radiobutton_enlager_4.config(state="normal")
            self.radiobutton_enlager_4.select()
        elif self.var_anzahl_beh.get() == "5":
            print("fünf")
            self.entry_eintauchzeit1.config(state="normal")
            self.radiobutton_enlager_1.config(state="normal")
            self.entry_eintauchzeit2.config(state="normal")
            self.radiobutton_enlager_2.config(state="normal")
            self.entry_eintauchzeit3.config(state="normal")
            self.radiobutton_enlager_3.config(state="normal")
            self.entry_eintauchzeit3.config(state="normal")
            self.radiobutton_enlager_3.config(state="normal")
            self.entry_eintauchzeit4.config(state="normal")
            self.radiobutton_enlager_4.config(state="normal")           
            self.entry_eintauchzeit5.config(state="normal")
            self.radiobutton_enlager_5.config(state="normal")
            self.radiobutton_enlager_5.select()
        elif self.var_anzahl_beh.get() == "6":
            print("sechs")
            self.entry_eintauchzeit1.config(state="normal")
            self.radiobutton_enlager_1.config(state="normal")
            self.entry_eintauchzeit2.config(state="normal")
            self.radiobutton_enlager_2.config(state="normal")
            self.entry_eintauchzeit3.config(state="normal")
            self.radiobutton_enlager_3.config(state="normal")
            self.entry_eintauchzeit3.config(state="normal")
            self.radiobutton_enlager_3.config(state="normal")
            self.entry_eintauchzeit4.config(state="normal")
            self.radiobutton_enlager_4.config(state="normal")           
            self.entry_eintauchzeit5.config(state="normal")
            self.radiobutton_enlager_5.config(state="normal")
            self.entry_eintauchzeit6.config(state="normal")
            self.radiobutton_enlager_6.config(state="normal")
            self.radiobutton_enlager_6.select()
        elif self.var_anzahl_beh.get() == "7":  
            print("sieben")
            self.entry_eintauchzeit1.config(state="normal")
            self.radiobutton_enlager_1.config(state="normal")
            self.entry_eintauchzeit2.config(state="normal")
            self.radiobutton_enlager_2.config(state="normal")
            self.entry_eintauchzeit3.config(state="normal")
            self.radiobutton_enlager_3.config(state="normal")
            self.entry_eintauchzeit3.config(state="normal")
            self.radiobutton_enlager_3.config(state="normal")
            self.entry_eintauchzeit4.config(state="normal")
            self.radiobutton_enlager_4.config(state="normal")           
            self.entry_eintauchzeit5.config(state="normal")
            self.radiobutton_enlager_5.config(state="normal")
            self.entry_eintauchzeit6.config(state="normal")
            self.radiobutton_enlager_6.config(state="normal")
            self.entry_eintauchzeit7.config(state="normal")
            self.radiobutton_enlager_7.config(state="normal")
            self.radiobutton_enlager_7.select()
        elif self.var_anzahl_beh.get() == "8":
            print("acht")
            self.entry_eintauchzeit1.config(state="normal")
            self.radiobutton_enlager_1.config(state="normal")
            self.entry_eintauchzeit2.config(state="normal")
            self.radiobutton_enlager_2.config(state="normal")
            self.entry_eintauchzeit3.config(state="normal")
            self.radiobutton_enlager_3.config(state="normal")
            self.entry_eintauchzeit3.config(state="normal")
            self.radiobutton_enlager_3.config(state="normal")
            self.entry_eintauchzeit4.config(state="normal")
            self.radiobutton_enlager_4.config(state="normal")           
            self.entry_eintauchzeit5.config(state="normal")
            self.radiobutton_enlager_5.config(state="normal")
            self.entry_eintauchzeit6.config(state="normal")
            self.radiobutton_enlager_6.config(state="normal")
            self.entry_eintauchzeit7.config(state="normal")
            self.radiobutton_enlager_7.config(state="normal")
            self.entry_eintauchzeit8.config(state="normal")
            self.radiobutton_enlager_8.config(state="normal")
            self.radiobutton_enlager_8.select()

    def test_user_input(self, inStr, acttyp):
        if acttyp == '1': #insert
            if not inStr.isdigit():
                return False
        return True

    def move(self, commands):  
        for command in commands:
            if self.stop_testing == True:
                return
            if command[0] == "X":
                self.stepper_X.goto_pos(command[1])
            elif command[0] == "Z":
                self.stepper_Z.goto_pos(command[1])
            elif command[0] == "Sleep":
                self.stepper_X.pause(command[1])
            elif command[0] == "Counter":
                self.counter += 1
                self.var_counter.set("Test: " + str(self.counter) + " / " + self.var_wiederholung.get())
                
 
       
    def flash(self):
        #self.button_status.configure(text= self.counter)
        if self.button_status.cget("bg") == "gray85":
            self.button_status.config(bg = 'blue')
        else:
            self.button_status.config(bg = 'gray85')
        self.button_blinking = root.after(700, self.flash)

    def start_test(self):
        print("Start")
        commands = []
        self.flash()
        self.button_start.configure(state=DISABLED)
        self.stop_testing = False  

        arm_lenght = Limits.ARM_LEFT_RIGHT_MAX  # The free distanze to move at X-axis 
        arm_down =   Limits.ARM_UP_DOWN_MAX
        anzahl_behaelter = int(self.var_anzahl_beh.get())
        x_move = round(arm_lenght / (anzahl_behaelter - 1))

        #Commands for one run
        for behaelter in range(anzahl_behaelter):
            immerse_time = int(self.entry_array[behaelter].get())
            single_command = [["X", x_move*behaelter],["Sleep", 3], ["Z", arm_down], ["Sleep", immerse_time], ["Z", 0], ["Sleep", 3]]
            commands.extend(single_command)

        #Cycel counter
        commands.extend([["Counter", 1]])

        #Multiply runs
        commands = commands * int(self.var_wiederholung.get())

        #Add commands for storage position at testend
        store_nr = int(self.var_testende.get())
        position = store_nr - 1
        commands.extend([["X", x_move*position],["Sleep",3], ["Z",arm_down]])

        #OPTION if storage in air is needed
        #commands.extend([["Z", 0], ["Sleep", 3], ["X", 0]])
        
        pprint(commands)

        t1 = Thread(target=self.move, args=(commands,))
        t1.daemon = True
        t1.start()
        
    def stop_test(self):
        print("Stop")
        self.counter = 0
        self.var_counter.set("Test: _ / _ ")
        self.stop_testing = True 
        self.stepper_X.stopping()
        self.stepper_Z.stopping()
        sleep(2)

        print(str(self.stepper_X.get_actual_steps()) + "STEPS")
        self.stepper_Z.goto_pos(0)
        self.stepper_X.pause(5)
        self.stepper_X.goto_pos(0)
        self.button_start.configure(state=NORMAL)
        try:
            root.after_cancel(self.button_blinking)
        except AttributeError:
            print("Closing with Error in self.button_blinking")

    def cleanup(self):
        """End APP"""
        print("Close GUI")
        finish = messagebox.askquestion("Abbruch", "Bitte nur beenden wenn Arm auf Null-Position steht " +"\n" +"\n"
                               + "Jetz zum Nullpunkt und Beenden ?")
        if finish == "yes":
            self.stop_test()
            self.root.destroy()


if __name__ == "__main__":

    root=Tk()
    gui = Gui(root)
    root.protocol('WM_DELETE_WINDOW',gui.cleanup)
    root.mainloop()

