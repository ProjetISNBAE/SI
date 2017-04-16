import tkinter as tk
master = tk.Tk()
master.title("Simulation Graphique")
master.geometry("600x800")

top = tk.Frame(master)
top.pack()
middle = tk.Frame(master)
middle.place(rely=.6)
bottom = tk.Frame(master)
bottom.place(rely=.8)

#c = tk.Canvas(main, width="500", height="300", bg="white",relief="sunken")
#c.pack()

############################ DATA ENTRY  ###############################

#t=2

lp=[] #liste des positions
lt=[] #liste du temps

time=tk.Entry(middle, bg="grey")
position=tk.Entry(middle, bg="grey")
time.grid(column=1, row=0)
time.insert(0, "Base de temps (s)")
position.grid(column=3, row=0)
position.insert(0, "Position (rad)")
empty_ml=tk.Label(middle)
empty_ml.grid(column=0,row=0, padx=55)
empty_mc=tk.Label(middle)
empty_mc.grid(column=2,row=0, padx=55)
empty_mr=tk.Label(middle)
empty_mr.grid(column=4,row=0, padx=40)
                                                                    
def clear_timebox(event): 
    time.delete(0, "end")
    return None

def clear_positionbox(event): 
    position.delete(0, "end")
    return None

time.bind("<Button-1>", clear_timebox)
position.bind("<Button-1>", clear_positionbox)
                                                                    
def timef():
    global t #t: base de temps
    global ct  #ct: current time (temps pour laquelle on entre la position)
    ct=int(0)
    t=time.get()
    t=int(t)
                                                                                                                                     
def data_entry(event):
    global ct
    ct=int(ct)+int(t)
    time.delete(0, "end")
    time.insert(1, ct)
    print(ct)
    
    lp.append(position.get())
    position.delete(0, "end")
    lt.append(time.get())
    print(lt)
    print(lp)
    
master.bind('<Return>', data_entry)
  
b_set_bdt = tk.Button(middle,text="Set",width=10,height=1, command=timef)
b_set_bdt.grid(column=1, row=1, sticky="E")

############################ CALCULS  ###############################
lv=[]
la=[]
lp=[]

def vitesse(base_temps, lis_p):
    global lv

    for i in range(len(lis_p)-1):
        if i==0:
            lv.append(0)
        elif i==1:
            lv.append((float(lis_p[1])-float(lis_p[0]))/(base_temps))
        else:
            v=(float(lis_p[i+1])-float(lis_p[i-1]))/(2*base_temps)
            lv.append(v)
    print(lv)


def acceleration(base_temps):
    global la
    global lv
    
    for i in range(len(lv)-1):
        if i<=1:
            la.append(0)
        elif i==2:
            la.append((float(lv[2])-float(lv[1]))/base_temps)
        else:
            a=((float(lv[i+1])-float(lv[i-1]))/(2*base_temps))
            la.append(a)
    print(la)


def v_and_a():
    vitesse(t, lp)
    acceleration(t)
    create_line(lt,0)
    create_line(lp,1)
    create_line(lv,2)
    create_line(la,3)

b_enter = tk.Button(bottom,text="Done",width=20,height=4, command=v_and_a)
b_enter.grid(column=1, row=0)
empty_bl=tk.Label(bottom, width=30)
empty_bl.grid(column=0,row=0)
empty_br=tk.Label(bottom, width=20)
empty_br.grid(column=2,row=0)

############################ TABLE  ###############################
emptyt0=tk.Label(top)
emptyt0.grid(column=0,row=1)
h_t=tk.Entry(top, bg="grey")
h_t.grid(column=0, row=2)
h_t.insert(0, "Temps(s)")
h_p=tk.Entry(top, bg="grey")
h_p.grid(column=1, row=2)
h_p.insert(0, "Position(rad)")
h_v=tk.Entry(top, bg="grey")
h_v.grid(column=2, row=2)
h_v.insert(0, "Vitesse(rad/s)")
h_a=tk.Entry(top, bg="grey")
h_a.grid(column=3, row=2)
h_a.insert(0, "Acceleration(rad/s²)")

def create_line(l,c):
    for i in range(len(l)):
        ti=tk.Entry(top)
        ti.grid(column=c, row=int(i+3))
        ti.insert(0, float(l[i]))

############################ READ CSV  ###############################

def imprt():
    global locate_file
    global file_name
    
    importcsv.destroy()
    locate_file=tk.Entry(top, bg="grey")
    locate_file.grid(column=0, row=0)
    locate_file.insert(0, "Emplacement du fichier")
    file_name=tk.Entry(top, bg="grey")
    file_name.grid(column=1, row=0)
    file_name.insert(0, "Nom du fichier")

    def delete_location(event): 
        locate_file.delete(0, "end")
        return None

    def delete_filename(event): 
        file_name.delete(0, "end")
        return None

    locate_file.bind("<Button-1>", delete_location)
    file_name.bind("<Button-1>", delete_filename)

    def find():
        fl=locate_file.get()
        fn=file_name.get()
        opencsv(fl,fn)

    find = tk.Button(top,text="Find",width=10,height=1, command=find)
    find.grid(column=3, row=0, sticky="E")
        
importcsv = tk.Button(top,text="Import",width=10,height=1, command=imprt)
importcsv.grid(column=0, row=0, sticky="W")
    
def opencsv(location, name):
    global d
    import os
    global lv
    global la
    global i_lt
    
    os.chdir(location)

    f=open(name)
    t=f.readlines()
    print(t,'\n\n')

    b=[]
    d=[]
    i_lt=[]
    i_ct=0
    for i in t:
        b.append(i.split('\n')[0])

    print('b=',b,'\n\n')
    c=b[len(b)-2]
    print('c=',c,'\n\n')
    d=c.split(',')
    print(d)
    d.remove('Angle')

    e=b[len(b)-1]
    bt=e.split(',')
    bt.remove('Base')
    bt=int(bt[0])
    
    print(d, bt)
    
    i_lt=[]
    for j in range(len(d)):
        i_ct = int(i_ct)+int(bt)
        i_lt.append(i_ct)
        
    print("time:", i_lt)
    
    vitesse(bt, d)
    acceleration(bt)
    
    create_line(i_lt,0)
    create_line(d,1)
    create_line(lv,2)
    create_line(la,3)
                
    
############################ WRITE CSV  ###############################
c=open('CSV counter.txt','w')
c.write('0')

def write_csv():
    global c
    global i_lt
    if lp==[]:
        lis_t=i_lt
        lis_p=d
    else:
        lis_t=lt
        lis_p=lp
    
    c=open('CSV counter.txt')
    n=c.readlines()
    for i in n:
        int_n=i
        
    str_n=int(int_n)+1
    str_n=str(str_n)
    c=open('CSV counter.txt', 'w')
    c.write(str_n)
    
    r=open('Tableau'+str_n+'.csv','w')
    
    r.write('Temps(s),')
    for i in range(len(lis_t)):
        r.write(str(lis_t[i]))
        r.write(",")
    r.write('\nPosition(rad),')
    for j in range(len(lis_p)):
        r.write(str(lis_p[j]))
        r.write(",")
    r.write('\nVitesse(rad/s),')
    for k in range(len(lv)):
        r.write(str(lv[k]))
        r.write(",")
    r.write('\nAcceleration(rad/s²),')
    for l in range(len(la)):
        r.write(str(la[l]))
        r.write(",")
        


export = tk.Button(bottom,text="Export",width=20,height=4, command=write_csv)
export.grid(column=1, row=1)

##############################################################
master.mainloop()
