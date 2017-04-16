import tkinter as tk
#import RPi.GPIO as GPIO
#import time
#GPIO.setmode(GPIO.BOARD)	# notation board plutôt que BCM(GPIO)
#GPIO.setup(pin, GPIO.OUT)		#config sortie
#################### HOME Window ##################### 

home = tk.Tk()
home.title("Home")
home.geometry("480x360")
home.configure(background='white')

###
def off():
    liste=[home, cp_window]
    for i in range(len(liste)):
        liste[i].destroy()
def h_kill():
    home.destroy()
def turn():
    print('continuous turning')

###
"""
def initialisationtrigo():

    global rapport 
    rapport= 5	
    global pin     #en pourcentage
    pin = 21,20,26
    global frequence
    frequence = 50
    GPIO.setmode(GPIO.BOARD)	# notation board plutôt que BCM(GPIO)
    GPIO.setup(pin, GPIO.OUT)	
    global pwm         #config sortie
    pwm = GPIO.PWM(pin, frequence)	#config (pin, freq)

def initialisationhor():
    import RPi.GPIO as GPIO
    global rapport
    rapport= 8	
    global pin      #en pourcentage
    pin = 21,20,26
    global frequence
    frequence = 50
    GPIO.setmode(GPIO.BOARD)	# notation board plutôt que BCM(GPIO)
    GPIO.setup(pin, GPIO.OUT)	
    global pwm          #config sortie
    pwm = GPIO.PWM(pin, frequence)	#config (pin, freq)
"""
    
def cp_90() :         
    """"
    initialisationtrigo()
    tps = 100 #temps necessaire avec un rapport cyclique donné por tourner de 90deg
    pwm.start(rapport)
    time.sleep(tps)
    pwm.stop(rapport)
    """
    print("+90")

def cp_180() : 
    print("+180")
    
def cp_270() : 
    print("+270")
    
def cp_450() : 
    print("-90")

def cp_r() : 
    print("random")
    
def cp_kill():
    cp_window.destroy()
    
def cp_menu() :
    global cp_window
    cp_window = tk.Toplevel()        
    cp_window.title("Change Position") 
    cp_window.geometry("480x360")
    cp_window.configure(background='white')

    
    bottom = tk.Frame(cp_window, background='white') #création de la partie du haut
    bottom.pack(side="bottom")
    middle = tk.Frame(cp_window, background='white') #création de la partie du milieu
    middle.pack(side="top")     
                                                                            
    button_90 = tk.Button(middle,text="+90",command=cp_90, width=20,height=4)
    button_90.grid(row=0,column=0,pady=30,padx=40,sticky="w")
    button_180 = tk.Button(middle,text="+180",command=cp_180,width=20,height=4)
    button_180.grid(row=0,column=1,pady=30,padx=40)
    button_270 = tk.Button(middle,text="+270",command=cp_270,width=20,height=4)
    button_270.grid(row=1,column=0,pady=30,padx=40,sticky="w")
    button_450 = tk.Button(middle,text="-90",command=cp_450,width=20,height=4)
    button_450.grid(row=1,column=1,pady=30,padx=40)
    buttonh = tk.Button(bottom,text="Home",command=cp_kill,width=15,height=3)
    buttonh.grid(row=0,column=0,sticky=tk.W, padx=0)
    buttonoff = tk.Button(bottom,text="Off",command=off,width=15,height=3, fg="red")
    buttonoff.grid(row=0,column=1,sticky=tk.E, padx=250)
   

bouton_cp = tk.Button(home,text="Change Position",command=cp_menu,width=20,height=4)
bouton_cp.place(relx=.35, rely=.2)
bouton_off = tk.Button(home,text="Off",command=h_kill, fg="red",width=15,height=3)
bouton_off.place(relx=.76, rely=.847)
bouton_turn = tk.Button(home,text="Tourner en continu",command=turn, width=20,height=4)
bouton_turn.place(relx=.35, rely=.55)
###    


home.mainloop()
