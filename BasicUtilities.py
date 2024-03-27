SYSVERSION = '2.31.1'
SNAPSHOT = False
SNAPSHOTVERSION = 0
ASSEMBLEDVERSION = f"Basic Utilities {SYSVERSION}"
if SNAPSHOT:
    ASSEMBLEDVERSION += f" Beta {SNAPSHOTVERSION}"

print(ASSEMBLEDVERSION,'(c) 2021-2022 Enderbyte Programs')
print("Initializing core functions",end="\r")
import os
os.system("")
from tkinter import messagebox, Tk
import sys
try:
    testtk = Tk()
    testtk.withdraw()
except:
    CLI = True
else:
    testtk.update()
    testtk.destroy()
    del testtk
    CLI = False
if "--noclicheck" in sys.argv:
    CLI = False
elif "--nogui" in sys.argv:
    CLI = True
def toplevelerror(message,title='Error'):
    title = str(title)
    message = str(message)
    root = Tk()
    root.wm_attributes("-topmost",True)
    root.withdraw()
    messagebox.showerror(title,message)

def consoleask(message) -> bool:
    """
    Asks the user a question in the console. Returns true if they say yes, returns false if they say no.
    """
    while True:
        xkl = input(str(message)+" (y/n): ")
        if xkl.lower().startswith("y"):
            return True
            break
        elif xkl.lower().startswith("n"):
            return False
            break
        else:
            print("Invalid. Please type 'yes' or 'no'")
def pinit(text):
    print(" "*100,end="\r")
    print(text,end="\r")
pinit("Preparing Libraries")
try:
    from pytube import *
except Exception as e:
    print('An error occured in Basic Utilities. ERROR:\n'+str(e)+'\nSome features may work incorrectly or fail')
try:
    import keyboard
except Exception as e:
    print('An error occured in Basic Utilities. ERROR:\n'+str(e)+'\nSome features may work incorrectly or fail')
try:
    import urllib.request
except Exception as e:
    print('An error occured in Basic Utilities. ERROR:\n'+str(e)+'\nSome features may work incorrectly or fail')
try:
    from awesome_progress_bar import ProgressBar
except Exception as e:
    print('An error occured in Basic Utilities. ERROR:\n'+str(e)+'\nSome features may work incorrectly or fail')
try:
    import termcolor
except Exception as e:
    print('An error occured in Basic Utilities. ERROR:\n'+str(e)+'\nSome features may work incorrectly or fail')
    HASTC = False
else:
    HASTC = True

from traceback import format_tb

import json
import collections
try:
    import psutil
except:
    print("Library psutil could not be found. Please run check_dependencies.py to install it.")
try:
    from pynput.mouse import Controller
    from pynput.mouse import Button as MButton
except:
    print("Library pymouse could not be found. Please run check_dependencies.py to install it.")
import socket #Totally not suspicious
try:
    import PIL.Image
except:
    print("Could not use pil lib.")

pinit("Defining core functions part 2")
os.system("color")
INFO = "info"
WARN = "warn"
ERROR = "error"
FATAL = "fatal"
def log(stuff_to_log,level=INFO):
    if level == "info":
        l = "INFO"
    if level == "warn":
        l = "WARN"
    if level == "error":
        l = "ERROR"
    if level == "fatal":
        l = "FATAL"
    try:
        f = open('log_000.log','a+')

        f.write(str(str(str(datetime.datetime.now())[0:len(str(datetime.datetime.now()))-3])+' '+l+" "+stuff_to_log)+'\n')
        f.close()
    except PermissionError:
        raise RuntimeError("Access is denied.")
def handle_exception(type,value,traceback):
    global ASSEMBLEDVERSION
    if issubclass(type, KeyboardInterrupt):
        pass
    else:
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
        os.system("color 17")
        
        l = format_tb(traceback)
        x = ""
        for item in l:
            x += item
            x += "\n"
        try:
            log(str(type).split(" ")[1].replace("'","").replace(">","")+'\n'+str(value)+'\n'+str(x),FATAL)
        except:
            pass
        
        print(':(                              \n\nBasic Utilities has encountered a critical error. \nIf you didn\'t expect this, please send the following text to the developer:'+'\n'+str(type)+'\n'+str(value)+'\n'+x+"\nDir: "+os.getcwd()+"\nSystem: "+platform.platform())
        print("Preparing dump of variables...")
        crashtypes = ["Oh no, not again!","HA HA HA HA HA! I CRASH A LOT!","GEEGEGGEGEOOOGOOGA","An unhandled exception? I don't see any around here!","Basic Utilities: Completely free of crashes"]#These are from my little sister
        vars = globals().items()
        print("Creating crash report...")
        try:
            if not os.path.isdir("crash_reports"):
                os.mkdir("crash_reports")
            with open(os.getcwd()+"/crash_reports/"+"crash_"+str(datetime.datetime.now()).replace(":","").replace(" ","_")+".txt","w+") as f:
                f.write("-----Basic Utilities Crash Report-----\n")
                f.write(random.choice(crashtypes)+"\n\n")
                f.write("CWD: "+os.getcwd())
                f.write("\nPlatform: "+platform.system())
                f.write("\nPlatformVersion: "+platform.version()+"\n")
                f.write("Version: "+ASSEMBLEDVERSION+"\n")
                for item in list(vars):
                    f.write(str(item[0]))
                    f.write(" : ")
                    f.write(str(item[1]))
                    f.write("\n")
                f.write("End of crash report")
        except:
            print("Failed to create crash report")
        print("Crash report and variable dump complete")
        del vars
        input("Press enter or return to exit")
        os.system("color 07")
        
from tkinter import *
def get_pixel_color(x, y):
    try:
        global BACKGROUND
    except:
        pass
    # canvas use different coordinates than turtle
    y = -y

    # get access to tkinter.Canvas
    canvas = turtle.getcanvas()
    
    # find IDs of all objects in rectangle (x, y, x, y)
    ids = canvas.find_overlapping(x, y, x, y)
    
    # if found objects
    if ids: 
        # get ID of last object (top most)
        index = ids[-1]
        
        # get its color
        color = canvas.itemcget(index, "fill")
        
        # if it has color then return it
        if color:
            return color
    
    # if there was no object then return "white" - background color in turtle
    try:
        return BACKGROUND
    except:
        return "#ffffff" # default color
if SNAPSHOT:
    try:
        termcolor.cprint("Warning! You are using a beta version of Basic Utilities! There may be lots of bugs.","yellow")
    except:
        print("Warning! You are using a beta version of Basic Utilities. There may be unexpected issues.")
pinit("Initializing libraries part 2")
import tarfile
import datetime
sys.excepthook = handle_exception

try:
    import winsound
except:
    print('Your device does not support Winsound. Some features may be broken.') 

import os

import webbrowser

import platform

import random
try:
    from packaging import version
except:
    print('The update command WILL NOT WORK. ')
    haspkg = False
else:
    haspkg = True


from time import sleep
try:
    from playsound import playsound
except:
    print('Your device does not support playsound. Some features may be broken')

import turtle

import threading
reqins = False


from tkinter import filedialog

import shutil

import subprocess

sw = False
gamees_played = 0
gamees_won = 0
pi = 3.14
hasarg = True
playedg2 = False
hasarg2 = True
pid = os.getpid()

def forcekill():
    log('Program stopped with exit code 0')
    global pid
    os.system('taskkill /F /PID '+str(pid)+' /T')
def forcekillnl():
    global pid
    os.system('taskkill /F /PID '+str(pid)+' /T')
try:
    arguments = sys.argv
    openfile_dir = arguments[1]
    xxx = arguments[2]
except:
    hasarg= False

try:
    arguments = sys.argv
    fto = sys.argv[1]
except:
    hasarg2 = False
if str(platform.system()) == 'Windows':
    sysslash = '\\'
    
else:
    sysslash = '/'
pinit("Scanning arguments") 
if (hasarg and xxx == '--translate') or (hasarg and xxx == "-t"):
    
    try:
        f = open(openfile_dir,'r')
        mes = f.read()
        print('')
        print("encoded message is",len(mes),"bytes")
    except:
        Tk().wihdraw()
        messagebox.showerror('Basic utilities','we could not open the file for you. It may have been deleted, moved, unreadable, or we lack permissions.')
    else:
        tra = mes.replace('GLHAC.P','z').replace('EXE','y').replace('ENDER','x').replace('BITLY','w').replace('OTW','v')\
    .replace('MOM','u').replace('CUED','t').replace('GHQ[W]','s').replace('QYIF','r').replace('FKUWEUI','q').replace('VAN','p')\
    .replace('NYX','o').replace('/-/','n').replace('LOL','m').replace('AXZ','l').replace('AVOO','k').replace('DYE','j')\
    .replace('NNQP','i').replace('BU#','h').replace('MDD','g').replace('XML','f').replace('*U&P/HTPS','e').replace('QUIE','d')\
    .replace('CEXC','c').replace('MPE','b').replace('NJ','a').replace('8','9').replace('7','8').replace('6','7').replace('5','6')\
    .replace('4','5').replace('3','4').replace('2','3').replace('1','2').replace('0','1').replace('NULL','0').replace('PWSAC',' ')
    print('')
    print('Tranlation:',tra)
    print('size:',len(tra),'bytes')
    wt = consoleask("Do you want to write this to a file?")
    if wt:
        print('What folder to save to?')
        Tk().withdraw()
        fexx = filedialog.askdirectory()
        print("What should the file name be? (no extension needed)")
        fex = input()
        fex = fex + '.txt'
        
        fex = fexx + sysslash + fex
        try:
            f = open(fex,'x')
            f.write(tra)
            f.close()
            print("written to",fex)
        except:
            try:
                f = open(fex,'w')
                f.write(tra)
                f.close()
                print("written to",fex)
            except:
                Tk().withdraw()
                messagebox.showerror('Error','Could not write')
    print('Press enter to quit program.')
    input()
    forcekillnl()
elif (hasarg and xxx == "-d") or (hasarg and xxx == "--draw"):
    if CLI:
        print("Program is not correctly initialized for this function.")
        sys.exit(1)
    print("Turtle Drawing Loader for Basic Utilities")
    s = turtle.getscreen()
    t = turtle.Turtle()
    turtle.hideturtle()
    t.hideturtle()
    t.speed(0)
    fto = arguments[1]
    if not os.path.isfile(fto):
        toplevelerror("Could not find file.")
        os.system("taskkill /f /pid "+str(os.getpid()))
    try:
        with open(fto) as f:
            data = f.read()
    except:
        toplevelerror("Failed to read file")
        os.system("taskkill /f /pid "+str(os.getpid()))
    inslen = len(data.split("\n"))
    print(f"Data file has {inslen} instructions.")
    ee = 0
    turtle.tracer(False)
    print("Drawing... The turtle window may stop responding, but this is normal. YOur drawing will appear when it is ready.")
    bar = ProgressBar(len(data.split("\n")),bar_length=100,prefix="Drawing",fill="#",spinner_type="s")
    for instruction in data.split("\n"):
        ee += 1
        try:
            l = instruction.split(" ")
            if instruction.split(" ")[0] == "b":
                turtle.Screen().bgcolor(str(l[1]))
            elif l[0] == "p":
                t.penup()
                t.goto(float(l[1]),float(l[2]))
                t.pencolor(" ".join(l[3:len(l)]))
                t.pendown()
                t.forward(1)
            elif l[0] == "t":
                t.penup()
                t.goto(float(l[1]),float(l[2]))
                t.pendown()
                txk = ""
                for item in l[3:len(l)]:
                    txk += " " + item
                t.write(txk)
        except TclError:
            print("Unexpected Tk error. Exiting")
            os.system("taskkill /f /pid "+str(os.getpid()))
        except Exception as ex:
            print(f"\rFailed to draw instruction {ee}:",str(ex))
        bar.iter()
        bar.suffix = " "+str(ee)+"/"+str(bar.total)
    bar.wait()
    print("Done!")
    turtle.tracer(True)   
    window = Tk()
    window.title('LetsDraw')
    window.geometry('800x500')
    turtle.title("Let's Draw Canvas")
    def go_forward():
        global txt
        res = txt.get()
        try:
            res = float(res)
        except ValueError:
            error(1)
        else:
            try:
                t.forward(res)
            except:
                error(0)

    def go_backward():
        global txt1
        res = txt1.get()
        try:
            res = float(res)
        except:
            error(1)
        else:
            try:
                t.backward(res)
            except:
                error(0)

    def turn_left():
        global txt2
        res = txt2.get()
        try:
            res = float(res)
        except:
            error(1)
        else:
            try:
                t.left(res)
            except:
                error(0)
    def turn_right():
        global txt3
        res = txt3.get()
        try:
            res = float(res)
        except:
            error(1)
        else:
            try:
                t.right(res)
            except:
                error(0)

    def changecolor():
        global txt4
        res = txt4.get()
        try:
            t.pencolor(res)
        except:
            error(1)

    def changefill():
        global txt5
        res = txt5.get()
        try:
            t.fillcolor(res)
        except:
            error(1)

    def go_to():
        global txt6
        global txt7
        res = txt6.get()
        res1 = txt7.get()
        try:
            res = int(res)
            res1 = int(res1)
        except:
            error(1)
        else:
            try:
                t.goto(res,res1)
            except:
                error(0)

    def pensize():
        global txt8
        res = txt8.get()
        try:
            res = int(res)
        except:
            error(1)
        else:
            try:
                t.pensize(res)
            except:
                error(0)

    def dot():
        global txt9
        res = txt9.get()
        try:
            res = int(res)
        except:
            error(1)
        else:
            try:
                t.dot(res)
            except:
                error(0)

    def dsave():
        global txt10
        res = txt10.get()
        res1 = ".eps"
        res = res + res1
        s.getcanvas().postscript(file=res)
    def dconv2():
        webbrowser.open("https://epsviewer.org/onlineviewer.aspx")
    def circ():
        global txt11
        res = txt11.get()
        try:
            res = int(res)
        except:
            error(1)
        else:
            try:
                t.circle(res)
            except:
                error(0)
    def square():
        global txt12
        res = txt12.get()
        try:
            res = float(res)
        except:
            error(1)
        else:
            for i in range(4):
                try:
                    t.forward(res)
                    t.right(90)
                except:
                    error(0)

    def byebye():
        global tcrash
        window.quit()
        window.destroy()
        turtle.bye()
        tcrash = True
    turtle.hideturtle()
    BACKGROUND = "#ffffff"

    lbl = Label(window,text='Lets Draw',font=("Arial Bold",12))
    lbl.grid(column=0,row=0)
    btn = Button(window,text='Exit',command=byebye,bg="red")
    btn.grid(column=1,row=0)

    txt = Entry(window,width=10)
    txt.grid(column=0,row=1)
    btn1 = Button(window,text='Go',command=go_forward,bg="green")
    btn1.grid(column=1,row=1)
    lbl1 = Label(window,text='Go forward this many units')
    lbl1.grid(column=2,row=1)

    txt1 = Entry(window,width=10)
    txt1.grid(column=0,row=2)
    btn2 = Button(window,text='Go',command=go_backward,bg="green")
    btn2.grid(column=1,row=2)
    lbl2 = Label(window,text='Go backward this many units')
    lbl2.grid(column=2,row=2)


    txt2 = Entry(window,width=10)
    txt2.grid(column=0,row=3)
    btn3 = Button(window,text='Go',command=turn_left,bg="green")
    btn3.grid(column=1,row=3)
    lbl3 = Label(window,text='Turn left this many degrees')
    lbl3.grid(column=2,row=3)

    txt3 = Entry(window,width=10)
    txt3.grid(column=0,row=4)
    btn4 = Button(window,text='Go',command=turn_right,bg="green")
    btn4.grid(column=1,row=4)
    lbl4 = Label(window,text='Turn right this many degrees')
    lbl4.grid(column=2,row=4)
    btn5 = Button(window,text='pen up',command=t.penup)
    btn5.grid(column=0,row=5)
    btn6 = Button(window,text='pen down',command=t.pendown)
    btn6.grid(column=1,row=5)
    btn7 = Button(window,text='undo',command=t.undo,bg="yellow")
    btn7.grid(column=2,row=5)
    btn8 = Button(window,text='clear canvas',command=t.clear,bg="orange")
    btn8.grid(column=3,row=5)
    btn9 = Button(window,text='Start fill',command=t.begin_fill)
    btn9.grid(column=0,row=6)
    btn10 = Button(window,text='End fill',command=t.end_fill)
    btn10.grid(column=1,row=6)
    lbl5 = Label(window,text='Press start fill, draw a closed shape, and press end fill to fill.')
    lbl5.grid(column=2,row=6)
    txt4 = Entry(window,width=20)
    txt4.grid(column=0,row=7)
    btn11 = Button(window,text='go',command=changecolor,bg="green")
    btn11.grid(column=1,row=7)
    lbl6 = Label(window,text='Change the pen colour (use a valid hex code starting with #)')
    lbl6.grid(column=2,row=7)
    txt5 = Entry(window,width=20)
    txt5.grid(column=0,row=8)
    btn12 = Button(window,text='go',command=changefill,bg="green")
    btn12.grid(column=1,row=8)
    lbl7 = Label(window,text='Change the fill colour (use a valid hex code starting with #)')
    lbl7.grid(column=2,row=8)

    txt6 = Entry(window,width=10)
    txt6.grid(column=0,row=9)
    txt7 = Entry(window,width=10)
    txt7.grid(column=1,row=9)

    btn13 = Button(window,text='go',command=go_to,bg="green")
    btn13.grid(column=2,row=9)
    lbl8 = Label(window,text='Change draw to this location (x y)')
    lbl8.grid(column=3,row=9)

    txt8 = Entry(window,width=10)
    txt8.grid(column=0,row=10)
    btn14 = Button(window,text='go',command=pensize,bg="green")
    btn14.grid(column=1,row=10)
    lbl9 = Label(window,text='Change the pen size')
    lbl9.grid(column=2,row=10)

    txt9 = Entry(window,width=10)
    txt9.grid(column=0,row=11)
    btn15 = Button(window,text='go',command=dot,bg="green")
    btn15.grid(column=1,row=11)
    lbl10= Label(window,text='Draw a dot of this size')
    lbl10.grid(column=2,row=11)

    txt10 = Entry(window,width=20)
    txt10.grid(column=0,row=12)
    btn16 = Button(window,text='Export',command=dsave,bg="blue")
    btn16.grid(column=1,row=12)
    lbl11 = Label(window,text='Export your drawing to .eps')
    lbl11.grid(column=2,row=12)
    btn18 = Button(window,text='Convert eps',command=dconv2)
    btn18.grid(column=3,row=12)
    txt11 = Entry(window,width=10)
    txt11.grid(column=0,row=13)
    btn19 = Button(window,text='Go',command=circ,bg="green")
    btn19.grid(column=1,row=13)
    lbl12 = Label(window,text='Draw a circle of this radius')
    lbl12.grid(column=2,row=13)

    txt12 = Entry(window,width=10)
    txt12.grid(column=0,row=14)
    btn20 = Button(window,text='Go',command=square,bg="green")
    btn20.grid(column=1,row=14)
    lbl13 = Label(window,text='Draw a square with a side length of this.')
    lbl13.grid(column=2,row=14)
    def tsave():
        print("saving...")
        
        global BACKGROUND
        
        t.hideturtle()
        try:
            
            e = []
            print("Assembling list...")
            for x in range(int(-400),int(400)):
                for y in range(int(-400),int(400)):
                    e.append((x,y))
            files = [('Turtle file','*.trt')]
            print("Please select save file")    
            
            print("Writing...")
            with open(fto,"w+") as f:
                f.write("b "+BACKGROUND+"\n")
                for coord in e:
                    l = get_pixel_color(coord[0],coord[1])
                    if l != BACKGROUND:
                        f.write("p "+str(coord[0])+" "+str(coord[1])+" "+l+"\n")
            
            print("Finished")
        except Exception as ex:
            toplevelerror("Failed to save "+str(ex))
        finally:
            t.showturtle()
    def sbk():
        global BACKGROUND
        global ent
        e = ent.get()
        try:
            turtle.Screen().bgcolor(e)
        except:
            pass
        else:
            BACKGROUND = e
    btn21 = Button(window,text="Save",bg="lime green",command=tsave)
    lbl13 = Label(window,text="Save drawing as a later-editable .trt file")
    lbl13.grid(column=0,row=15)
    btn21.grid(column=1,row=15)
    ent = Entry(window,width=20)
    ent.grid(column=0,row=16)
    lbl14 = Label(window,text="Set the background (must be a valid hex code starting with #)")
    lbl14.grid(column=2,row=16)
    btn22 = Button(window,text="Go",bg="green",command=sbk)
    btn22.grid(column=1,row=16)
    ent1 = Entry(window,width=30)
    ent2 = Entry(window,width=10)
    ent3 = Entry(window,width=10)
    lbl15 = Label(window,text="Insert text")
    lbl16 = Label(window,text="at xy")
    def wtx():
        x = t.pos()
        global ent1
        global ent2
        global ent3
        try:
            t.penup()
            t.goto(int(ent2.get()),int(ent3.get()))
            t.pendown()
            t.write(ent1.get())
            t.penup()
            t.goto(x[0],x[1])
        except Exception as ex:
            toplevelerror("Failed to complete write: "+str(ex))
    btn23 = Button(window,text="Go",bg="green",command=wtx)
    lbl15.place(y=440,x=0)
    ent1.place(y=440,x=70)
    lbl16.place(x=250,y=440)
    ent2.place(x=280,y=440)
    ent3.place(x=350,y=440)
    btn23.place(x=400,y=440)
    window.mainloop()

    
    os.system("taskkill /f /pid "+str(os.getpid()))

elif hasarg2 == True:
    if CLI:
        print("Program is not correctly initialized")
        sys.exit(1)
    print("Notpad Text Editor for Basic Utilities")
    cwd = os.getcwd()
    fto = sys.argv[1]
    if fto == '--new' or fto == '-n':
        
        def saveas():
            global txt
            global fname
            global prevsavedata
            global issy
            global menu1
            try:
                files = [('All Files','*.*')]
                file = filedialog.asksaveasfile(filetypes=files,defaultextension=files)
            except:
                Tk().withdraw()
                messagebox.showerror('Could not write')
            else:
                try:
                    fname = file.name
                except:
                    q = 0
                else:
                    try:
                        file = open(fname,'w',encoding="utf-8")
                        file.write(txt.get('1.0','end-1c'))
                        file.close()
                    except:
                        Tk().withdraw()
                        messagebox.showerror('notpad','Cannot Write data')
                    else:
                        root.title('Notpad-'+fname)
                        Tk().withdraw()
                        issy = True
                        menu1['menu'].entryconfigure(8,state='normal')
                        messagebox.showinfo('notpad','Writing sucessfull')
                        prevsavedata = txt.get('1.0','end-1c')
        def save():
            global txt
            global fname
            global prevsavedata
            
            try:
                file = open(fname,'w',encoding="utf-8")
            except:
                saveas()
            else:
                file.write(txt.get('1.0','end-1c'))
                file.close()
                prevsavedata = txt.get('1.0','end-1c')

        def opennew():
            
            if os.path.isfile('BasicUtilities.exe'):
                Tk().withdraw()
                x = filedialog.askopenfilename()
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                    
                CREATE_NEW_PROCESS_GROUP = 0x00000200
                DETACHED_PROCESS = 0x00000008
                
                p = subprocess.Popen(["BasicUtilities.exe", x],stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=False,creationflags=subprocess.CREATE_NO_WINDOW | DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP)
            else:
                Tk().withdraw()
                messagebox.showerror('Notpad','Could not find BasicUtilities.exe. Did you delete or rename it?')

        def ats():
            global txt
            
            txt.insert(END,' '+str(datetime.datetime.now()))

        def canaconv():
            global txt
            data = txt.get('1.0','end-1c')
            txt.delete("1.0","end")
            data = data.replace('color','colour')
            data = data.replace('Color','Colour')
            data = data.replace('harbor','harbour')
            data = data.replace('Harbor','Harbour')
            data = data.replace('center','centre')
            data = data.replace('Center','Centre')
            data = data.replace('Armor','Armour')
            data = data.replace('armor','armour')
            data = data.replace('restroom','washroom')
            data = data.replace('Restroom','Washroom')
            txt.insert(END,data)

        def txconv():
            global txt
            data = txt.get('1.0','end-1c')
            txt.delete("1.0","end")
            data = data.replace('you','u')
            data = data.replace('You','u')
            data = data.replace('YOU','u')
            data = data.replace('are','r')
            data = data.replace('Are','r')
            data = data.replace('ARE','r')
            data = data.replace('skate','sk8')
            data = data.replace('Skate','sk8')
            data = data.replace('your','ur')
            data = data.replace('Your','ur')
            data = data.replace('YOUR','UR')
            data = data.replace('I','i')
            data = data.replace('i know right','ikr')
            data = data.replace('i know, right','ikr')
            data = data.replace('i Know Right','ikr')
            data = data.replace('i Know, Right','ikr')
            data = data.replace('in real life','irl')
            data = data.replace('in Real Life','irl')
            data = data.replace('laugh','lol')
            data = data.replace('Laugh','lol')
            txt.insert(END,data)

        def amconv():
            global txt
            data = txt.get('1.0','end-1c')
            txt.delete("1.0","end")
            data = data.replace('all of you',"y'all")
            data = data.replace('All of you',"Y'all")
            data = data.replace('you all',"y'all")
            data = data.replace('You all',"Y'all")
            data = data.replace('yes',"yes'm")
            data = data.replace('Yes',"Yes'm")
            data = data.replace('ng',"n'")
            data = data.replace('NG',"N'")
            data = data.replace('er than',"er than "+str(random.randint(1,20))+' '+random.choice(['pigs','cows','chickens','computers','dogs','cats','pythons'])+' in a '+random.choice(['pigpen','farm','doghouse','chicken coop','Root directory']))
            txt.insert(END,data)

        def owoconv():
            global txt
            data = txt.get('1.0','end-1c')
            txt.delete("1.0","end")
            #Why did I make this????
            #WHY!?!?!?!?!?!
            data = data.replace('w','w-w')
            data = data.replace('W','w-w')
            data = data.replace('d','d-d')
            data = data.replace('D','d-d')
            data = data.replace('.','~')
            data = data.replace('dog','doggo')
            data = data.replace('pl','pw')
            data = data.replace('Pl','Pw')
            data = data.replace('r','w')
            data = data.replace('R','W')
            data = data.replace('l','w')
            data = data.replace('L','W')
            txt.insert(END,data)

        def terminat():
            global txt
            global prevsavedata
            global pid
            global istr
            data = txt.get('1.0','end-1c')
            if data == prevsavedata:
                istr = False
                forcekillnl()
            else:
                Tk().withdraw()
                x = messagebox.askyesnocancel('Text Editor','You have unsaved work. Do you want to save before closing?')
                if x == True:
                    if prevsavedata == '':
                        saveas()
                        if prevsavedata == '':
                            pass
                        else:
                            istr = False
                            forcekillnl()
                    else:
                        save()
                        istr = False
                        forcekillnl()
                elif x == False:
                    
                    forcekillnl()

        
        def scanautosave():
            try:
                global chkc
            except:
                pass
            global istr
            global issy
            while True:
                sleep(10)
                try:
                    if int(chkc.get()) == 1 and issy == True:
                        save()
                        
                except:
                    pass
                if istr == False:
                    break
        def encd():
            global txt
            data = txt.get('1.0','end-1c')
            txt.delete("1.0","end")
            data = data.replace('a','NJ').replace('b','MPE').replace('c','CEXC').replace('d','QUIE').replace('e','*U&P/HTPS')\
            .replace('f','XML').replace('g','MDD').replace('h','BU#').replace('i','NNQP').replace('j','DYE').replace('k','AVOO').replace('l','AXZ')\
            .replace('m','LOL').replace('n','/-/').replace('o','NYX').replace('p','VAN').replace('q','FKUWEUI').replace('r','QYIF')\
            .replace('s','GHQ[W]').replace('t','CUED').replace('u','MOM').replace('v','OTW').replace('w','BITLY').replace('x','ENDER')\
            .replace('y','EXE').replace('z','GLHAC.P').replace('0','NULL').replace('1','0').replace('2','1').replace('3','2')\
            .replace('4','3').replace('5','4').replace('6','5').replace('7','6').replace('8','7').replace('9','8').replace(' ','PWSAC')
            txt.insert(END,data)

        def dcd():
            global txt
            data = txt.get('1.0','end-1c')
            txt.delete("1.0","end")
            data = data.replace('GLHAC.P','z').replace('EXE','y').replace('ENDER','x').replace('BITLY','w').replace('OTW','v')\
            .replace('MOM','u').replace('CUED','t').replace('GHQ[W]','s').replace('QYIF','r').replace('FKUWEUI','q').replace('VAN','p')\
            .replace('NYX','o').replace('/-/','n').replace('LOL','m').replace('AXZ','l').replace('AVOO','k').replace('DYE','j')\
            .replace('NNQP','i').replace('BU#','h').replace('MDD','g').replace('XML','f').replace('*U&P/HTPS','e').replace('QUIE','d')\
            .replace('CEXC','c').replace('MPE','b').replace('NJ','a').replace('8','9').replace('7','8').replace('6','7').replace('5','6')\
            .replace('4','5').replace('3','4').replace('2','3').replace('1','2').replace('0','1').replace('NULL','0').replace('PWSAC',' ')
            txt.insert(END,data)
        
        def dai():
            global ent
            global txt
            data = txt.get('1.0','end-1c')
            txt.delete("1.0","end")
            todel = ent.get()
            data = data.replace(todel,'')
            txt.insert(END,data)
        def dfw():
            global ent
            global txt
            data = txt.get('1.0','end-1c')
            txt.delete("1.0","end")
            todel = ' '+ent.get()+' '
            data = data.replace(todel,'')
            txt.insert(END,data)
        def repw():
            global ent
            global ent2
            global txt
            data = txt.get('1.0','end-1c')
            txt.delete("1.0","end")
            
            data = data.replace(ent.get(),ent2.get())
            txt.insert(END,data)

        def cio():
            global ent3
            global txt
            data = txt.get('1.0','end-1c')
            messagebox.showinfo('Text Editor','Instances of '+str(ent3.get())+': '+str(data.count(ent3.get()))+' ('+(str(data.count(ent3.get())/(len(data)+1)*100)+'%)'))

        def writestat():
            try:
                global fname
                global txt
                data = txt.get('1.0','end-1c')
                file = open(fname+'stat','w+')
                file.write('Data for file '+fname+'\n')
                file.write('At '+str(datetime.datetime.now())+'\n')
                file.write('File Length: '+str(len(data))+' bytes\n')
                file.write('File size: '+str(os.path.getsize(fname))+' bytes\n')
                file.write('Instances of A: '+str((data.count('a')+data.count('A')))+' '+str((data.count('a')+data.count('A'))/len(data)*100)+'%\n')
                file.write('Instances of b: '+str((data.count('b')+data.count('B')))+' '+str((data.count('b')+data.count('B'))/len(data)*100)+'%\n')
                file.write('Instances of c: '+str((data.count('c')+data.count('C')))+' '+str((data.count('c')+data.count('C'))/len(data)*100)+'%\n')
                file.write('Instances of d: '+str((data.count('d')+data.count('D')))+' '+str((data.count('d')+data.count('D'))/len(data)*100)+'%\n')
                file.write('Instances of e: '+str((data.count('e')+data.count('E')))+' '+str((data.count('e')+data.count('E'))/len(data)*100)+'%\n')
                file.write('Instances of f: '+str((data.count('f')+data.count('F')))+' '+str((data.count('f')+data.count('F'))/len(data)*100)+'%\n')
                file.write('Instances of g: '+str((data.count('g')+data.count('G')))+' '+str((data.count('g')+data.count('G'))/len(data)*100)+'%\n')
                file.write('Instances of h: '+str((data.count('h')+data.count('H')))+' '+str((data.count('h')+data.count('H'))/len(data)*100)+'%\n')
                file.write('Instances of i: '+str((data.count('i')+data.count('I')))+' '+str((data.count('i')+data.count('I'))/len(data)*100)+'%\n')
                file.write('Instances of j: '+str((data.count('j')+data.count('J')))+' '+str((data.count('j')+data.count('J'))/len(data)*100)+'%\n')
                file.write('Instances of k: '+str((data.count('k')+data.count('K')))+' '+str((data.count('k')+data.count('K'))/len(data)*100)+'%\n')
                file.write('Instances of l: '+str((data.count('l')+data.count('L')))+' '+str((data.count('l')+data.count('L'))/len(data)*100)+'%\n')
                file.write('Instances of m: '+str((data.count('m')+data.count('M')))+' '+str((data.count('m')+data.count('M'))/len(data)*100)+'%\n')
                file.write('Instances of n: '+str((data.count('n')+data.count('N')))+' '+str((data.count('n')+data.count('N'))/len(data)*100)+'%\n')
                file.write('Instances of o: '+str((data.count('o')+data.count('O')))+' '+str((data.count('o')+data.count('O'))/len(data)*100)+'%\n')
                file.write('Instances of p: '+str((data.count('p')+data.count('P')))+' '+str((data.count('p')+data.count('P'))/len(data)*100)+'%\n')
                file.write('Instances of q: '+str((data.count('q')+data.count('Q')))+' '+str((data.count('q')+data.count('Q'))/len(data)*100)+'%\n')
                file.write('Instances of r: '+str((data.count('r')+data.count('R')))+' '+str((data.count('r')+data.count('R'))/len(data)*100)+'%\n')
                file.write('Instances of s: '+str((data.count('s')+data.count('S')))+' '+str((data.count('s')+data.count('S'))/len(data)*100)+'%\n')
                file.write('Instances of t: '+str((data.count('t')+data.count('T')))+' '+str((data.count('t')+data.count('T'))/len(data)*100)+'%\n')
                file.write('Instances of u: '+str((data.count('u')+data.count('U')))+' '+str((data.count('u')+data.count('U'))/len(data)*100)+'%\n')
                file.write('Instances of v: '+str((data.count('v')+data.count('V')))+' '+str((data.count('v')+data.count('V'))/len(data)*100)+'%\n')
                file.write('Instances of w: '+str((data.count('w')+data.count('W')))+' '+str((data.count('w')+data.count('W'))/len(data)*100)+'%\n')
                file.write('Instances of x: '+str((data.count('x')+data.count('X')))+' '+str((data.count('x')+data.count('X'))/len(data)*100)+'%\n')
                file.write('Instances of y: '+str((data.count('y')+data.count('Y')))+' '+str((data.count('y')+data.count('Y'))/len(data)*100)+'%\n')
                file.write('Instances of z: '+str((data.count('z')+data.count('Z')))+' '+str((data.count('z')+data.count('Z'))/len(data)*100)+'%\n')
                file.write('Instances of NUM: '+str((data.count('0')+data.count('1')+data.count('2')+data.count('3')+data.count('4')+data.count('5')+data.count('6')+data.count('7')+data.count('8')+data.count('9')))+' '+str((data.count('0')+data.count('1')+data.count('2')+data.count('3')+data.count('4')+data.count('5')+data.count('6')+data.count('7')+data.count('8')+data.count('9'))/len(data)*100)+'%\n')
                file.write('Instances of SPACE: '+str(data.count(' '))+' '+str(data.count(' ')/len(data)*100)+'%\n')
                file.write('Instances of SYM: '+str((data.count('!')+data.count('@')+data.count('#')+data.count('$')+data.count('%')+data.count('^')+data.count('&')+data.count('*')+data.count('(')+data.count(')')+data.count('-')+data.count('_')+data.count('/')+data.count(';')+data.count(',')+data.count('.')))+' '+str((data.count('!')+data.count('@')+data.count('#')+data.count('$')+data.count('%')+data.count('^')+data.count('&')+data.count('*')+data.count('(')+data.count(')')+data.count('-')+data.count('_')+data.count('/')+data.count(';')+data.count(',')+data.count('.'))/len(data)*100)+'%\n')
                
                
                file.close()
            except:
                try:
                    file.close()
                except:
                    pass
                Tk().withdraw()
                messagebox.showerror('Text Editor','Failed to write statistics file')
            else:
                Tk().withdraw()
                messagebox.showinfo('Text Editor','Wrote Statistics file to '+fname+'stat')

        def reverse():
            global txt
            data = txt.get('1.0','end-1c')
            txt.delete('1.0',"end")
            datalen = len(data)
            data = data[datalen::-1]
            txt.insert(END,data)
                
        def charcountthr():
            while True:
                global istr
                global lbl1
                global lbl2
                global lbl3
                global lbl4
                global lbl5
                global txt
                global isdef
                if istr and isdef:
                    try:
                        data = txt.get('1.0','end-1c')
                        lbl1.config(text="char: "+str(len(data)))
                        lbl2.config(text="line: "+str(len(data.split("\n"))))
                        lbl3.config(text="word: "+str(len(data.split(" "))))
                        ln = str(txt.index(INSERT)).split(".")[0]
                        char = str(txt.index(INSERT)).split(".")[1]
                        lbl4.config(text="ln: "+ln)
                        lbl5.config(text="col: "+char)

                    except Exception as e:
                        print(e)
                        break
                sleep(0.1)

        prevsavedata = ''
        istr = True
        issy = False
        isdef = False
        try:
            keyboard.add_hotkey('ctrl+q',terminat)
            keyboard.add_hotkey('ctrl+shift+s',saveas)
            keyboard.add_hotkey('ctrl+s',save)
            keyboard.add_hotkey('ctrl+alt+o',opennew)
        except:
            pass
        scaus = threading.Thread(target=scanautosave)
        scaus.start()
        scalen = threading.Thread(target=charcountthr).start()
        root = Tk()
        root.title('Notpad [new file]')
        root.geometry("800x600")
        def chk_menu1(val):
            global OptionVar0
            OptionVar0.set('File Options')
            if val == 'Exit (ctrl+q)':
                terminat()
            elif val == 'Save As (ctrl+shift+s)':
                saveas()
            elif val == 'Save (ctrl+s)':
                save()
            elif val == 'Open (ctrl+alt+o)':
                opennew()
            
        
        scr = Scrollbar(root)
        scr.pack(side='right',fill='y',expand=False)

        OptionVar0 = StringVar(root)
        OptionVar0.set('File Options')
        menu = OptionMenu(root,OptionVar0,"Exit (ctrl+q)","Save As (ctrl+shift+s)","Save (ctrl+s)","Open (ctrl+alt+o)","All key shortcuts used WILL AFFECT TO ALL OTHER COPIES OF THIS PROGRAM CURRENTLY RUNNING",command=chk_menu1)
        menu.pack(side=TOP,anchor=NW)
        menu['menu'].entryconfigure(4,state='disabled')
        def chk_menu2(val):
            global OptionVar1
            OptionVar1.set('Text Options')
            if val == 'Append Time Stamp (alt+s)':
                ats()
            elif val == 'Reverse (ctrl+alt+r)':
                reverse()
            elif val == 'Convert to Canadian English (alt+c)':
                canaconv()
            elif val == 'Convert to Text Slang (alt+t)':
                txconv()
            elif val == 'Convert to American English (alt+a)':
                amconv()
            elif val == 'Convert to Owo Text (alt+o)':
                owoconv()
            elif val == 'Encode (alt+e)':
                encd()
            elif val == 'Decode (alt+d)':
                dcd()
            elif val == 'Write Statistics File (ctrl+alt+w)':
                writestat()
        try:
            keyboard.add_hotkey('alt+s',ats)
            keyboard.add_hotkey('ctrl+alt+r',reverse)
            keyboard.add_hotkey('alt+c',canaconv)
            keyboard.add_hotkey('alt+t',txconv)
            keyboard.add_hotkey('alt+a',amconv)
            keyboard.add_hotkey('alt+o',owoconv)
            keyboard.add_hotkey('alt+e',encd)
            keyboard.add_hotkey('alt+d',dcd)
            keyboard.add_hotkey('ctrl+alt+w',writestat)
        except:
            pass
        OptionVar1 = StringVar(root)
        OptionVar1.set('Text Options')

        menu1 = OptionMenu(root,OptionVar1,"Append Time Stamp (alt+s)","Reverse (ctrl+alt+r)",'Convert to Canadian English (alt+c)','Convert to Text Slang(alt+t)',
        "Convert to American English (alt+a)",
        "Convert to Owo Text (alt+o)",
        "Encode (alt+e)",
        "Decode (alt+d)",
        "Write Statistics File (ctrl+alt+w)",
        "All key shortcuts used WILL AFFECT ALL OTHER COPIES OF THIS PROGRAM CURRENTLY RUNNING",
        command=chk_menu2)
        menu1['menu'].entryconfigure(8,state='disabled')
        menu1['menu'].entryconfigure(9,state='disabled')
        menu1.pack(side=TOP,anchor=NW)
        
        txt = Text(root,wrap=NONE)
        txt.pack(expand=True,fill='both')
        fontt = ("Times new Roman",12)
        txt.config(font=fontt)
       
        chkc = IntVar(root)
        chkbx = Checkbutton(root,text='Autosave (10 s)',variable=chkc)
        chkbx.place(x=390,y=30)
        
        txt.config(yscrollcommand=scr.set)
        scr.config(command=txt.yview)
        scr1 = Scrollbar(root,orient='horizontal')
        scr1.pack(side='bottom',fill='x',expand=False)
        txt.config(xscrollcommand=scr1.set)
        scr1.config(command=txt.xview)
        lbl = Label(root,text='Will save to directory in title')
        lbl.place(x=120,y=30)
        ent = Entry(root,width=20)
        ent.place(x=120,y=0)
        btn11 = Button(root,text='Delete all instances',command=dai,bg='skyblue')
        btn11.place(x=250,y=0)
        btn12 = Button(root,text='Delete full words only',command=dfw,bg='blue',fg='white')
        btn12.place(x=360,y=0)
        btn13 = Button(root,text='Replace with',bg='black',fg='white',command=repw)
        ent2 = Entry(root,width=20)
        btn13.place(x=500,y=0)
        ent2.place(x=600,y=0)
        ent3 = Entry(root,width=10)
        ent3.place(x=510,y=30)
        btn14 = Button(root,text='Count instances',command=cio)
        btn14.place(x=580,y=30)
        lbl1 = Label(root,text="char: waiting...")
        lbl1.place(x=680,y=15)
        lbl2 = Label(root,text="line: waiting...")
        lbl2.place(x=680,y=30)
        lbl3 = Label(root,text="word: waiting...")
        lbl3.place(x=680,y=45)
        lbl4 = Label(root,text="ln: waiting...")
        lbl4.place(x=300,y=25)
        lbl5 = Label(root,text="col: waiting...")
        lbl5.place(x=300,y=40)
        
        root.protocol("WM_DELETE_WINDOW",terminat)
        isdef = True
        root.mainloop()
        istr = False
        isdef = False
        forcekillnl()
    else:
        try:
            f = open(fto)
        except:
            Tk().withdraw()
            messagebox.showerror('notpad','Could not open file. May not exist, access denied, or unreadable.')
        else:
            def saveas():
                global txt
                global fname
                global prevsavedata
                try:
                    files = [('All Files','*.*')]
                    file = filedialog.asksaveasfile(filetypes=files,defaultextension=files)
                except:
                    Tk().withdraw()
                    messagebox.showerror('Could not write')
                else:
                    try:
                        fname = file.name
                    except:
                        q = 0
                    else:
                        try:
                            file = open(fname,'w',encoding="utf-8")
                            file.write(txt.get('1.0','end-1c'))
                            file.close()
                        except:
                            Tk().withdraw()
                            messagebox.showerror('notpad','Cannot Write data')
                        else:
                            
                            Tk().withdraw()
                            messagebox.showinfo('notpad','Writing sucessfull')
                            prevsavedata = txt.get('1.0','end-1c')

            def save():
                global txt
                global fto
                global prevsavedata
                try:
                    file = open(fto,'w',encoding="utf-8")
                except:
                    saveas()
                else:
                    file.write(txt.get('1.0','end-1c'))
                    file.close()
                    prevsavedata = txt.get('1.0','end-1c')

            def ats():
                global txt
            
                txt.insert(END,' '+str(datetime.datetime.now()))

            def canaconv():
                global txt
                data = txt.get('1.0','end-1c')
                txt.delete("1.0","end")
                data = data.replace('color','colour')
                data = data.replace('Color','Colour')
                data = data.replace('harbor','harbour')
                data = data.replace('Harbor','Harbour')
                data = data.replace('center','centre')
                data = data.replace('Center','Centre')
                data = data.replace('Armor','Armour')
                data = data.replace('armor','armour')
                data = data.replace('restroom','washroom')
                data = data.replace('Restroom','Washroom')
                txt.insert(END,data)

            def txconv():
                global txt
                data = txt.get('1.0','end-1c')
                txt.delete("1.0","end")
                data = data.replace('you','u')
                data = data.replace('You','u')
                data = data.replace('YOU','u')
                data = data.replace('are','r')
                data = data.replace('Are','r')
                data = data.replace('ARE','r')
                data = data.replace('skate','sk8')
                data = data.replace('Skate','sk8')
                data = data.replace('your','ur')
                data = data.replace('Your','ur')
                data = data.replace('YOUR','UR')
                data = data.replace('I','i')
                data = data.replace('i know right','ikr')
                data = data.replace('i know, right','ikr')
                data = data.replace('i Know Right','ikr')
                data = data.replace('i Know, Right','ikr')
                data = data.replace('in real life','irl')
                data = data.replace('in Real Life','irl')
                data = data.replace('laugh','lol')
                data = data.replace('Laugh','lol')
                txt.insert(END,data)

            def amconv():
                global txt
                data = txt.get('1.0','end-1c')
                txt.delete("1.0","end")
                data = data.replace('all of you',"y'all")
                data = data.replace('All of you',"Y'all")
                data = data.replace('you all',"y'all")
                data = data.replace('You all',"Y'all")
                data = data.replace('yes',"yes'm")
                data = data.replace('Yes',"Yes'm")
                data = data.replace('er than',"er than "+str(random.randint(1,20))+' '+random.choice(['pigs','cows','chickens','computers','dogs','cats','pythons'])+' in a '+random.choice(['pigpen','farm','doghouse','chicken coop','Root directory']))
                txt.insert(END,data)

            def owoconv():
                global txt
                data = txt.get('1.0','end-1c')
                txt.delete("1.0","end")
                #Why did I make this????
                #WHY!?!?!?!?!?!
                data = data.replace('w','w-w')
                data = data.replace('W','w-w')
                data = data.replace('d','d-d')
                data = data.replace('D','d-d')
                data = data.replace('.','~')
                data = data.replace('dog','doggo')
                data = data.replace('pl','pw')
                data = data.replace('Pl','Pw')
                data = data.replace('r','w')
                data = data.replace('R','W')
                data = data.replace('l','w')
                data = data.replace('L','W')
                txt.insert(END,data)

            def terminat():
                global txt
                global prevsavedata
                data = txt.get('1.0','end-1c')
                if data == prevsavedata:
                    forcekillnl()
                else:
                    Tk().withdraw()
                    x = messagebox.askyesnocancel('Text Editor','You have unsaved work. Do you want to save before closing?')
                    if x == True:
                        save()
                        forcekillnl()
                    elif x == False:
                        forcekillnl()

            def scanautosave():
                try:
                    global chkc
                except:
                    pass
                global istr
                global issy
                while True:
                    sleep(10)
                    try:
                        if int(chkc.get()) == 1 and issy == True:
                            save()
                            
                    except:
                        pass
                    if istr == False:
                        break
            def encd():
                global txt
                data = txt.get('1.0','end-1c')
                txt.delete("1.0","end")
                data = data.replace('a','NJ').replace('b','MPE').replace('c','CEXC').replace('d','QUIE').replace('e','*U&P/HTPS')\
                .replace('f','XML').replace('g','MDD').replace('h','BU#').replace('i','NNQP').replace('j','DYE').replace('k','AVOO').replace('l','AXZ')\
                .replace('m','LOL').replace('n','/-/').replace('o','NYX').replace('p','VAN').replace('q','FKUWEUI').replace('r','QYIF')\
                .replace('s','GHQ[W]').replace('t','CUED').replace('u','MOM').replace('v','OTW').replace('w','BITLY').replace('x','ENDER')\
                .replace('y','EXE').replace('z','GLHAC.P').replace('0','NULL').replace('1','0').replace('2','1').replace('3','2')\
                .replace('4','3').replace('5','4').replace('6','5').replace('7','6').replace('8','7').replace('9','8').replace(' ','PWSAC')
                txt.insert(END,data)

            def dcd():
                global txt
                data = txt.get('1.0','end-1c')
                txt.delete("1.0","end")
                data = data.replace('GLHAC.P','z').replace('EXE','y').replace('ENDER','x').replace('BITLY','w').replace('OTW','v')\
                .replace('MOM','u').replace('CUED','t').replace('GHQ[W]','s').replace('QYIF','r').replace('FKUWEUI','q').replace('VAN','p')\
                .replace('NYX','o').replace('/-/','n').replace('LOL','m').replace('AXZ','l').replace('AVOO','k').replace('DYE','j')\
                .replace('NNQP','i').replace('BU#','h').replace('MDD','g').replace('XML','f').replace('*U&P/HTPS','e').replace('QUIE','d')\
                .replace('CEXC','c').replace('MPE','b').replace('NJ','a').replace('8','9').replace('7','8').replace('6','7').replace('5','6')\
                .replace('4','5').replace('3','4').replace('2','3').replace('1','2').replace('0','1').replace('NULL','0').replace('PWSAC',' ')
                txt.insert(END,data)

            def dai():
                global ent
                global txt
                data = txt.get('1.0','end-1c')
                txt.delete("1.0","end")
                todel = ent.get()
                data = data.replace(todel,'')
                txt.insert(END,data)
            def dfw():
                global ent
                global txt
                data = txt.get('1.0','end-1c')
                txt.delete("1.0","end")
                todel = ' '+ent.get()+' '
                data = data.replace(todel,'')
                txt.insert(END,data)
            def repw():
                global ent
                global ent2
                global txt
                data = txt.get('1.0','end-1c')
                txt.delete("1.0","end")
                
                data = data.replace(ent.get(),ent2.get())
                txt.insert(END,data)

            def cio():
                global ent3
                global txt
                data = txt.get('1.0','end-1c')
                messagebox.showinfo('Text Editor','Instances of '+str(ent3.get())+': '+str(data.count(ent3.get()))+' ('+(str(data.count(ent3.get())/len(data)*100)+'%)'))

            def writestat():
                try:
                    global fto
                    global txt
                    data = txt.get('1.0','end-1c')
                    file = open(fto+'stat','w+')
                    file.write('Data for file '+fto+'\n')
                    file.write('At '+str(datetime.datetime.now())+'\n')
                    file.write('File Length: '+str(len(data))+' bytes\n')
                    file.write('File size: '+str(os.path.getsize(fto))+' bytes\n')
                    file.write('Instances of A: '+str((data.count('a')+data.count('A')))+' '+str((data.count('a')+data.count('A'))/len(data)*100)+'%\n')
                    file.write('Instances of b: '+str((data.count('b')+data.count('B')))+' '+str((data.count('b')+data.count('B'))/len(data)*100)+'%\n')
                    file.write('Instances of c: '+str((data.count('c')+data.count('C')))+' '+str((data.count('c')+data.count('C'))/len(data)*100)+'%\n')
                    file.write('Instances of d: '+str((data.count('d')+data.count('D')))+' '+str((data.count('d')+data.count('D'))/len(data)*100)+'%\n')
                    file.write('Instances of e: '+str((data.count('e')+data.count('E')))+' '+str((data.count('e')+data.count('E'))/len(data)*100)+'%\n')
                    file.write('Instances of f: '+str((data.count('f')+data.count('F')))+' '+str((data.count('f')+data.count('F'))/len(data)*100)+'%\n')
                    file.write('Instances of g: '+str((data.count('g')+data.count('G')))+' '+str((data.count('g')+data.count('G'))/len(data)*100)+'%\n')
                    file.write('Instances of h: '+str((data.count('h')+data.count('H')))+' '+str((data.count('h')+data.count('H'))/len(data)*100)+'%\n')
                    file.write('Instances of i: '+str((data.count('i')+data.count('I')))+' '+str((data.count('i')+data.count('I'))/len(data)*100)+'%\n')
                    file.write('Instances of j: '+str((data.count('j')+data.count('J')))+' '+str((data.count('j')+data.count('J'))/len(data)*100)+'%\n')
                    file.write('Instances of k: '+str((data.count('k')+data.count('K')))+' '+str((data.count('k')+data.count('K'))/len(data)*100)+'%\n')
                    file.write('Instances of l: '+str((data.count('l')+data.count('L')))+' '+str((data.count('l')+data.count('L'))/len(data)*100)+'%\n')
                    file.write('Instances of m: '+str((data.count('m')+data.count('M')))+' '+str((data.count('m')+data.count('M'))/len(data)*100)+'%\n')
                    file.write('Instances of n: '+str((data.count('n')+data.count('N')))+' '+str((data.count('n')+data.count('N'))/len(data)*100)+'%\n')
                    file.write('Instances of o: '+str((data.count('o')+data.count('O')))+' '+str((data.count('o')+data.count('O'))/len(data)*100)+'%\n')
                    file.write('Instances of p: '+str((data.count('p')+data.count('P')))+' '+str((data.count('p')+data.count('P'))/len(data)*100)+'%\n')
                    file.write('Instances of q: '+str((data.count('q')+data.count('Q')))+' '+str((data.count('q')+data.count('Q'))/len(data)*100)+'%\n')
                    file.write('Instances of r: '+str((data.count('r')+data.count('R')))+' '+str((data.count('r')+data.count('R'))/len(data)*100)+'%\n')
                    file.write('Instances of s: '+str((data.count('s')+data.count('S')))+' '+str((data.count('s')+data.count('S'))/len(data)*100)+'%\n')
                    file.write('Instances of t: '+str((data.count('t')+data.count('T')))+' '+str((data.count('t')+data.count('T'))/len(data)*100)+'%\n')
                    file.write('Instances of u: '+str((data.count('u')+data.count('U')))+' '+str((data.count('u')+data.count('U'))/len(data)*100)+'%\n')
                    file.write('Instances of v: '+str((data.count('v')+data.count('V')))+' '+str((data.count('v')+data.count('V'))/len(data)*100)+'%\n')
                    file.write('Instances of w: '+str((data.count('w')+data.count('W')))+' '+str((data.count('w')+data.count('W'))/len(data)*100)+'%\n')
                    file.write('Instances of x: '+str((data.count('x')+data.count('X')))+' '+str((data.count('x')+data.count('X'))/len(data)*100)+'%\n')
                    file.write('Instances of y: '+str((data.count('y')+data.count('Y')))+' '+str((data.count('y')+data.count('Y'))/len(data)*100)+'%\n')
                    file.write('Instances of z: '+str((data.count('z')+data.count('Z')))+' '+str((data.count('z')+data.count('Z'))/len(data)*100)+'%\n')
                    file.write('Instances of NUM: '+str((data.count('0')+data.count('1')+data.count('2')+data.count('3')+data.count('4')+data.count('5')+data.count('6')+data.count('7')+data.count('8')+data.count('9')))+' '+str((data.count('0')+data.count('1')+data.count('2')+data.count('3')+data.count('4')+data.count('5')+data.count('6')+data.count('7')+data.count('8')+data.count('9'))/len(data)*100)+'%\n')
                    file.write('Instances of SPACE: '+str(data.count(' '))+' '+str(data.count(' ')/len(data)*100)+'%\n')
                    file.write('Instances of SYM: '+str((data.count('!')+data.count('@')+data.count('#')+data.count('$')+data.count('%')+data.count('^')+data.count('&')+data.count('*')+data.count('(')+data.count(')')+data.count('-')+data.count('_')+data.count('/')+data.count(';')+data.count(',')+data.count('.')))+' '+str((data.count('!')+data.count('@')+data.count('#')+data.count('$')+data.count('%')+data.count('^')+data.count('&')+data.count('*')+data.count('(')+data.count(')')+data.count('-')+data.count('_')+data.count('/')+data.count(';')+data.count(',')+data.count('.'))/len(data)*100)+'%\n')
                    
                    
                    file.close()
                except:
                    try:
                        file.close()
                    except:
                        pass
                    Tk().withdraw()
                    messagebox.showerror('Text Editor','Failed to write statistics file')
                else:
                    Tk().withdraw()
                    messagebox.showinfo('Text Editor','Wrote Statistics file to '+fto+'stat')
            def reverse():
                global txt
                data = txt.get('1.0','end-1c')
                txt.delete('1.0',"end")
                datalen = len(data)
                data = data[datalen::-1]
                txt.insert(END,data)

            def charcountthr():
                while True:
                    global istr
                    global lbl1
                    global lbl2
                    global lbl3
                    global lbl4
                    global lbl5
                    global txt
                    global isdef
                    if istr and isdef:
                        try:
                            data = txt.get('1.0','end-1c')
                            lbl1.config(text="char: "+str(len(data)))
                            lbl2.config(text="line: "+str(len(data.split("\n"))))
                            lbl3.config(text="word: "+str(len(data.split(" "))))
                            ln = str(txt.index(INSERT)).split(".")[0]
                            char = str(txt.index(INSERT)).split(".")[1]
                            lbl4.config(text="ln: "+ln)
                            lbl5.config(text="col: "+char)
                        except Exception as e:
                            print(e)
                            break
                    sleep(0.1)

            try:
                prevsavedata = f.read()
            except:
                Tk().withdraw()
                ee = messagebox.askyesno('Text Editor','This file contains unreadable characters. Do you wish to read it? (unreadable characters will be replaced)')
                if not ee:
                    forcekillnl()
                elif ee:
                    f.close()
                    f = open(fto,"rb")
                    ddt = f.read()
                    prevsavedata = ddt.decode("ASCII",errors="replace")

            istr = True
            issy = True
            isdef = False
            try:
                keyboard.add_hotkey('ctrl+q',terminat)
                keyboard.add_hotkey('ctrl+shift+s',saveas)
                keyboard.add_hotkey('ctrl+s',save)
            except:
                pass
            
            scaus = threading.Thread(target=scanautosave)
            scaus.start()
            scalen = threading.Thread(target=charcountthr).start()
            root = Tk()
            root.title('Notpad: '+str(fto))
            root.geometry("800x600")
            def chk_menu1(val):
                global OptionVar0
                OptionVar0.set('File Options')
                if val == 'Exit (ctrl+q)':
                    terminat()
                elif val == 'Save As (ctrl+shift+s)':
                    saveas()
                elif val == 'Save (ctrl+s)':
                    save()
                
                
            
            scr = Scrollbar(root)
            scr.pack(side='right',fill='y',expand=False)

            OptionVar0 = StringVar(root)
            OptionVar0.set('File Options')
            menu = OptionMenu(root,OptionVar0,"Exit (ctrl+q)","Save As (ctrl+shift+s)","Save (ctrl+s)","All key shortcuts used WILL AFFECT TO ALL OTHER COPIES OF THIS PROGRAM CURRENTLY RUNNING",command=chk_menu1)
            menu.pack(side=TOP,anchor=NW)
            menu['menu'].entryconfigure(3,state='disabled')

            def chk_menu2(val):
                global OptionVar1
                OptionVar1.set('Text Options')
                if val == 'Append Time Stamp (alt+s)':
                    ats()
                elif val == 'Reverse (ctrl+alt+r)':
                    reverse()
                elif val == 'Convert to Canadian English (alt+c)':
                    canaconv()
                elif val == 'Convert to Text Slang (alt+t)':
                    txconv()
                elif val == 'Convert to American English (alt+a)':
                    amconv()
                elif val == 'Convert to Owo Text (alt+o)':
                    owoconv()
                elif val == 'Encode (alt+e)':
                    encd()
                elif val == 'Decode (alt+d)':
                    dcd()
                elif val == 'Write Statistics File (ctrl+alt+w)':
                    writestat()

            try:

                keyboard.add_hotkey('alt+s',ats)
                keyboard.add_hotkey('ctrl+alt+r',reverse)
                keyboard.add_hotkey('alt+c',canaconv)
                keyboard.add_hotkey('alt+t',txconv)
                keyboard.add_hotkey('alt+a',amconv)
                keyboard.add_hotkey('alt+o',owoconv)
                keyboard.add_hotkey('alt+e',encd)
                keyboard.add_hotkey('alt+d',dcd)
                keyboard.add_hotkey('ctrl+alt+w',writestat)
            except:
                pass
            
            OptionVar1 = StringVar(root)
            OptionVar1.set('Text Options')

            menu1 = OptionMenu(root,OptionVar1,"Append Time Stamp (alt+s)","Reverse (ctrl+alt+r)",'Convert to Canadian English (alt+c)','Convert to Text Slang(alt+t)',
            "Convert to American English (alt+a)",
            "Convert to Owo Text (alt+o)",
            "Encode (alt+e)",
            "Decode (alt+d)",
            "Write Statistics File (ctrl+alt+w)",
            "All key shortcuts used WILL AFFECT ALL OTHER COPIES OF THIS PROGRAM CURRENTLY RUNNING",
            command=chk_menu2)
            
            menu1['menu'].entryconfigure(9,state='disabled')
            menu1.pack(side=TOP,anchor=NW)

            txt = Text(root,wrap=NONE)
            txt.pack(expand=True,fill='both')
            fontt = ("Times new Roman",12)
            txt.config(font=fontt)
            try:
                txt.insert(END,prevsavedata)
            except:
                Tk().withdraw()
                messagebox.showerror('Notpad','Could not read file')
                forcekillnl()

        
            chkc = IntVar(root)
            chkbx = Checkbutton(root,text='Autosave (10 s)',variable=chkc)
            chkbx.place(x=390,y=30)
            
            txt.config(yscrollcommand=scr.set)
            scr.config(command=txt.yview)
            scr1 = Scrollbar(root,orient='horizontal')
            scr1.pack(side='bottom',fill='x',expand=False)
            txt.config(xscrollcommand=scr1.set)
            scr1.config(command=txt.xview)
            lbl = Label(root,text='Will save to directory in title.')
            lbl.place(x=120,y=30)
            ent = Entry(root,width=20)
            ent.place(x=120,y=0)
            btn11 = Button(root,text='Delete all instances',command=dai,bg='skyblue')
            btn11.place(x=250,y=0)
            btn12 = Button(root,text='Delete full words only',command=dfw,bg='blue',fg='white')
            btn12.place(x=360,y=0)
            btn13 = Button(root,text='Replace with',bg='black',fg='white',command=repw)
            ent2 = Entry(root,width=20)
            btn13.place(x=500,y=0)
            ent2.place(x=600,y=0)
            ent3 = Entry(root,width=10)
            ent3.place(x=510,y=30)
            btn14 = Button(root,text='Count instances',command=cio)
            btn14.place(x=580,y=30)
            lbl1 = Label(root,text="char: waiting...")
            lbl1.place(x=680,y=15)
            lbl2 = Label(root,text="line: waiting...")
            lbl2.place(x=680,y=30)
            lbl3 = Label(root,text="word: waiting...")
            lbl3.place(x=680,y=45)
            lbl4 = Label(root,text="ln: waiting...")
            lbl4.place(x=300,y=25)
            lbl5 = Label(root,text="col: waiting...")
            lbl5.place(x=300,y=40)
            root.protocol("WM_DELETE_WINDOW",terminat)
            isdef = True
            root.mainloop()
            try:
                f.close()
                
            except:
                ool = []
            istr = False
            isdef = False
            forcekillnl()
    sys.exit()

##@@##@@
log('Basic Utilities is starting. Running version '+ASSEMBLEDVERSION)
STIME = datetime.datetime.now()
pinit("Loading Appdata")
if os.path.isfile("appdata.json"):
    log("Loading Appdata")
    with open("appdata.json") as appdat:
        try:
            APPDATA = json.load(appdat)
        except json.decoder.JSONDecodeError:
            epo = 0
        else:
            epo = 1
        if epo == 0 or str(type(APPDATA)).split("'")[1] != "dict":
            epo = 0
    if epo == 0:
        log("Appdata is corrupt. Regenerating",ERROR)
        os.remove("appdata.json")
        
isported = False
if not os.path.isfile("appdata.json") and os.path.isfile("bcount.txt"):
    print("You are using an old version of appdata (<2.23). Would you like to port it?")
    pa = input()
    apd = {"besttime": 0, "bcount" : 0, "btime": {"year": None, "month": None, "day": None, "hour": None, "minute": None, "second": None}, "bday": {"month": None, "day": None}, "webhistory": [], "username": "DefaultUser", "showCommandsRun": False, "gamehealth": 100, "gamexp": 0, "startsound": None, "useDownloadedSounds" : True, "useColouredText" : True, "legacyStartups" : False,
    "commandsRun" : 0,"climode":CLI}

    if not HASTC:
        apd["useColouredText"] = False
    if pa.lower().startswith("y"):
        log("Porting Appdata")
        isported = True
        if os.path.isfile("appdata.txt"):
            with open("appdata.txt") as ad:
                besttime = ad.read()
            try:
                besttime = int(besttime)
            except:
                pass
            else:
                apd["besttime"] = besttime

        if os.path.isfile("bcount.txt"):

            with open("bcount.txt") as ad2:
                bcount = ad2.read()
            try:
                bcount = int(bcount)
            except:
                pass
            else:
                apd["bcount"] = bcount

        if os.path.isfile("bday.txt"):

            with open("bday.txt") as ad3:
                bday = ad3.readlines()
                
                bmt = bday[0]
                bdy = bday[1]
            try:
                bmt = int(bmt)
                bdy = int(bdy)
            except:
                print("failed to port birthday")
            else:
                apd["bday"]["month"] = bmt
                apd["bday"]["day"] = bdy
        if os.path.isfile("notifs.txt"):
            with open("notifs.txt") as ad:
                nt = ad.read()
                if nt == "0" or nt == "false":
                    apd["showCommandsRun"] = False
                elif nt == "1" or nt == "true":
                    apd["showCommandsRun"] = True
                else:
                    Tk().withdraw()
                    mpo0 = messagebox.askyesno("Appdata Porting","Do you want to see how many commands you have run?")
                    if mpo0:
                        apd["showCommandsRun"] = True
                    else:
                        apd["showCommandsRun"] = False

        if os.path.isfile("username.txt"):
            with open("username.txt") as ad:
                sysuser = ad.read()
                apd["username"] = sysuser

        if os.path.isfile("health.txt"):
            with open("health.txt") as ad:
                hl = ad.read()
                try:
                    hl = float(hl)
                except:
                    pass
                else:
                    apd["gamehealth"] = hl

        if os.path.isfile("xp.txt"):
            with open("xp.txt") as ad:
                xp = ad.read()
                try:
                    xp = float(xp)
                except:
                    pass
                else:
                    apd["gamexp"] = xp

        if os.path.isfile("btime.txt"):
            with open("btime.txt") as ad:
                btime = ad.readlines()
                try:
                    b0 = int(btime[0])
                except:
                    pass
                else:
                    apd["btime"]["year"] = b0
                try:
                    b1 = int(btime[1])
                except:
                    pass
                else:
                    apd["btime"]["month"] = b1
                try:
                    b2 = int(btime[2])
                except:
                    pass
                else:
                    apd["btime"]["day"] = b2
                try:
                    b3 = int(btime[3])
                except:
                    pass
                else:
                    apd["btime"]["hour"] = b3
                try:
                    b4 = int(btime[4])
                except:
                    pass
                else:
                    apd["btime"]["minute"] = b4
                try:
                    b5 = int(btime[5])
                except:
                    pass
                else:
                    apd["btime"]["second"] = b5

        if os.path.isfile("startsound.dat"):
            with open("startsound.dat") as ad:
                ss = ad.read()
                if os.path.isfile(ss):
                    apd["startsound"] = ss

        if os.path.isfile("history.txt"):
            with open("history.txt") as ad:
                hs = ad.readlines()
                for webentry in hs:
                    apd["webhistory"].append(webentry.replace("\n",""))

        apf = ["appdata.txt","bcount.txt","btime.txt","history.txt","startsound.dat","xp.txt","health.txt","notifs.txt","username.txt"]
        for file in apf:
            if os.path.isfile(file):
                os.remove(file)
        #reloading appdata
        with open("appdata.json","w+") as ad:
            ad.write(str(json.dumps(apd)))
        with open("appdata.json") as appdat:
            APPDATA = json.load(appdat)
        
if not os.path.isfile("appdata.json") and not isported:
    log("Could not find Appdata file.",WARN)
    with open("appdata.json","w+") as apt:
        
        apt.write('{"besttime": 0, "bcount" : 0, "btime": {"year": null, "month": null, "day": null, "hour": null, "minute": null, "second": null}, "bday": {"month": null, "day": null}, "webhistory": [], "username": "DefaultUser", "showCommandsRun": false, "gamehealth": 100, "gamexp": 0, "startsound": null, "useDownloadedSounds" : true, "useColouredText" : true, "legacyStartups" : false, "commandsRun" : 0,"climode":false}')


    with open("appdata.json") as appdat:
        APPDATA = json.load(appdat)

if os.path.isfile("appdata.json") and os.path.isfile("bcount.txt"):
    log("Deleting old appdata")
    apf = ["appdata.txt","bcount.txt","btime.txt","history.txt","startsound.dat","xp.txt","health.txt","notifs.txt","username.txt"]
    for file in apf:
        if os.path.isfile(file):
            os.remove(file)

if not "useColouredText" in APPDATA:
    APPDATA["useColouredText"] = True
if not "legacyStartups" in APPDATA:
    APPDATA["legacyStartups"] = False
if not "commandsRun" in APPDATA:
    APPDATA["commandsRun"] = 0
if not "climode" in APPDATA:
    APPDATA["climode"] = CLI
CLI = APPDATA["climode"]
def updateappdata():
    global APPDATA
    global INFO
    
    with open("appdata.json","w+") as ad:
        ad.write(str(json.dumps(APPDATA)))
    
log("Appdata initialization is complete")
updateappdata()
if str(platform.system()) == 'Windows':
    sysslash = '\\'
else:
    sysslash = '/'
    if not APPDATA["legacyStartups"]:
        print(f"Warning: The operating system you are running is not supported. Reccomended is Windows 10 +. You are on {str(platform.platform())}")

pinit("Requesting data from server (1/5) (update data)")
try:   
    from requests import get
    import requests
except:
    print('Some features may be broken because you dont have requests installed.')

    try:
        SYSVERDATA = get('https://pastebin.com/raw/eTQC8inZ').json()
        reqins = True
    except:
        if not APPDATA["legacyStartups"]:
            print('Error','Some features may work improperly or fail because you are not connected to the internet. (ip, ip6, update)')

xae = True
tcrash = False
accessdenied = False
cmd_run = 0
CAL = True
FCON = False
ASSETS = os.getcwd()+"/assets"
try:
    ewqueo = requests.get("https://www.google.com")
except (requests.ConnectionError,requests.Timeout):
    if not APPDATA["legacyStartups"]:
        if APPDATA["useColouredText"]:
            termcolor.cprint("You are not connected to the internet. Some commands may not work as intended.","yellow")
        else:
            print("You are not connected to the internet. Some commands may not work as intended")
    APPDATA["useDownloadedSounds"] = False
    updateappdata()
    log("User is not connected to the internet",WARN)
    MESSAGE = "No message- Failed to get message."
except NameError:
    MESSAGE = "No message- Library not found."
    print("Please install requests library to use downloaded sounds")
    APPDATA["useDownloadedSounds"] = False
    updateappdata()
else:
    log("User is connected to the internet",INFO)
    pinit("Requesting data from server (2/5) (extra files)")
    if not os.path.isdir("assets"):
        log("Failed to find assets directory.",WARN)
        os.mkdir("assets")
    pinit("Requesting data from server (2/5) (extra files) [1/2] [warning.mp3]")
    if not os.path.isfile(os.getcwd()+"/assets/"+"warning.mp3"):
        log("Could not find sound file. Downloading",WARN)
        urllib.request.urlretrieve("https://github.com/Enderbyte-Programs/Basic-Utilities/raw/main/warning.mp3",ASSETS+"/warning.mp3")
    pinit("Requesting data from server (2/5) (extra files) [2/2] [gameboard.jpg]")
    if not os.path.isfile(os.getcwd()+"/assets/"+"gameboard.jpg"):
        log("Could not find gameboard file. Downloading",WARN)
        urllib.request.urlretrieve("https://github.com/Enderbyte-Programs/Basic-Utilities/raw/main/gameboard.jpg",ASSETS+"/gameboard.jpg")
    
    try:
        SYSVERDATA = get('https://pastebin.com/raw/eTQC8inZ').json()
        reqins = True
    except Exception as e:
        
        print('Failed to get Update data',str(e))
        log(str(e),ERROR)
    else:
        pinit("Requesting data from server (3/5) (message)")
        MESSAGE = get("https://pastebin.com/raw/zYfU8JAP").text
    pinit("Requesting data from server (4/5)")
    try:
        RESTRICTIONS = requests.get("https://pastebin.com/raw/W7qMKqru").json()
    except requests.ConnectionError as e:
        print("Failed to get data",str(e))
        if "restrictions" in APPDATA:
        
            FCON = True
        else:
            RESTRICTIONS = {
            "disabled" : [

            ],
            "note" : {

            }
            }
    except json.decoder.JSONDecodeError:
        RESTRICTIONS = {
            "disabled" : [

            ],
            "note" : {

            }
        }
        FCON = True
    #Totally nothing to see here. NO illegal activities or you know, sending your IP address to Enderbyte Programs Server
    pinit("Requesting data from server (5/5) (Server IP)")
    try:
        SERVERIP = requests.get("https://pastebin.com/raw/RTCMAf6S").text
        log(f"Server ip is {SERVERIP}")
    except:
        log("Failed to get server ip!",ERROR)
    else:
        pinit("Sending data to server...")
        def sd():
            try:
                s = socket.socket()
                s.connect((SERVERIP.split(":")[0],int(SERVERIP.split(":")[1])))
                s.sendall(bytearray(f"&&BU${str(SYSVERSION)}${platform.platform()}",'utf-8'))
            except Exception as e:
                log(f"Failed to send data! {e}",ERROR)
        threading.Thread(target=sd).start()

try:
    besttime = int(APPDATA["besttime"])
except:
    besttime = 0
    APPDATA["besttime"] = 0
    updateappdata()
###
bootcount = APPDATA["bcount"]
try:
    bootcount = int(bootcount)
except:
    bootcount = 1
    APPDATA["bcount"] = bootcount
    updateappdata()
else:
    APPDATA["bcount"] = bootcount + 1
    updateappdata()

pinit("Loading functions part 3")

def error(erc):
    erc = str(erc)
    erm = "An error has occured. Error code "
    erm = erm + erc
    print(erm)
    log(erc,ERROR)

#Porting pyutils39
def toplevelquestion(message,title='Question'):
    title = str(title)
    message = str(message)
    root = Tk()
    root.wm_attributes("-topmost",True)
    root.withdraw()
    x = messagebox.askyesno(title,message)
    return x



def toplevelerror(message,title='Error'):
    title = str(title)
    message = str(message)
    root = Tk()
    root.wm_attributes("-topmost",True)
    root.withdraw()
    messagebox.showerror(title,message)

def newwindow():

    c = consoleask("You have executed a long/infinite command. Do you wish to open a new windows of Basic Utilities?")
    if c:
        try:
            os.startfile("BasicUtilities.exe")
        except Exception as e:
            print("ERROR",e)

def tkkill(windowname):
    windowname.quit()
    windowname.destroy()

def clipboardadd(value):
    """
    Copies a value to the clipboard, not suitable for CLI mode.
    """
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(value)
    r.update()
    r.destroy()

class conv():
    
    def __init__(self,start,end,formula):
        self.start = start
        self.end = end
        self.formula = formula
        self.root = Tk()
        self.root.title("Converter")
        self.lbl = Label(self.root,text=f"Converting {self.start} to {self.end}")
        self.lbl.grid(column=0,row=0)
        self.ent = Entry(self.root,width=50)
        self.ent.grid(column=0,row=1)
        
        self.ent2 = Entry(self.root,width=50)
        self.ent2.grid(column=0,row=2)
        
        self.btn = Button(self.root,text="Exit",command=self.root.destroy)
        self.btn.grid(column=1,row=0)
        while True:
            try:
                e = self.ent.get()
                
                self.ent2.delete(0,END)
                try:
                    e = float(e)
                except Exception as ex:
                    self.ent2.insert(END,"Error "+str(ex))
                else:
                    try:
                        self.ent2.insert(END,str(eval(str(e)+formula)))
                    except Exception as ex:
                        self.ent2.insert(END,"Error "+str(ex))
                
                sleep(0.1)
                self.root.update()
            except:
                break
def reload():
    try:
        os.startfile("BasicUtilities.exe")
    except:
        print("Could not start Basic Utilities")
    else:
        sys.exit()


def startsound():
    data = APPDATA["startsound"]
    if data is not None:
        if os.path.isfile(data):
            try:
                playsound(data)
            except Exception as e:
                if not APPDATA["legacyStartups"]:
                    print("Could not play startsound:",e)
        else:
            if not APPDATA["legacyStartups"]:
                print("Could not find start sound file")
    else:
        if not APPDATA["legacyStartups"]:
            log('You currently do not have a startup sound set. Set one via the startsound command\n')
ss_po = threading.Thread(target=startsound)
ss_po.start()       
def runfile(filename):
    try:
        os.startfile(filename)
    except:
        error(2)
##US
sysuser = APPDATA["username"]
pinit("Checking dates (1/4) (Birthday)")
try:
    mt = APPDATA["bday"]["month"]
    dy = APPDATA["bday"]["day"]
except:
    pass
else:
    t = datetime.datetime.now()
    p = t.month
    o = t.day
    try:
        mt = int(mt)
        dy = int(dy)
    except:
        pass
    else:
        try:
            l = datetime.datetime(t.year,mt,dy,0,0,0)
        except:
            print('Warning: Bday out of range',end='\r')
        else:
            if mt == p and dy ==o:
                pinit("")
                print("Happy birthday to you!")
                print("Happy birthday to you!")
                print(f"Happy birthday, dear {sysuser}")
                print("Happy birthday to you!")
                print("")
                print('press enter to continue to the command menu')
                input()
pinit("Checking dates (2/4) (Holidays)")
t = datetime.datetime.now()
y = t.year
p = t.month
o = t.day
if p == 1 and o ==1:
    print(f'Happy New Year, {sysuser} (gregorian calendar)')
elif y == 2022 and p == 2 and o == 1:
    print('Happy Lunar New Year!')
elif y == 2023 and p == 1 and o == 22:
    print('Happy Lunar New Year!')
elif y == 2024 and p == 2 and o == 10:
    print('Happy Lunar New Year!')
elif y == 2025 and p == 1 and o == 29:
    print('Happy Lunar New Year!')
elif p == 12 and o == 25:
    print(f'Happy Holidays, {sysuser}')
elif p == 12 and o == 24:
    print(f'Happy Holidays, {sysuser}')
elif p == 12 and o == 26:
    print(f'Happy Holidays, {sysuser}')
elif p == 2 and o == 15:
    print(f'Happy Parinirvana Day, {sysuser} (If you are buddhist)')
elif p == 10 and o == 31:
    print(f'Happy Halloween, {sysuser}!')
elif p == 4 and o == 14:
    print(f"Happy Vaisakhi if you are sikh")
#Couldn't find any more fixed-date holidays that are recognized globally. I am trying to be as inclusive as possible.
pinit("Checking dates (3/4) (Times booted)")
if not APPDATA["legacyStartups"]:
    print('You have booted up Basic Utilities',bootcount+1,'times.')
x = datetime.datetime.now()
if x.month == 4 and x.day == 1 and x.hour < 12:
    webbrowser.open('https://www.youtube.com/watch?v=xvFZjo5PgG0')
if x.month == 7 and x.day == 1:
    print(f'Happy Canada Day, {sysuser}!')
if x.month == 7 and x.day == 4:
    print(f'Happy American Day, {sysuser} ( if you are american)')
pinit("Checking dates (4/4) (Start dates)")
try:
    
    a = APPDATA["btime"]["year"]
    b = APPDATA["btime"]["month"]
    c = APPDATA["btime"]["day"]
    d = APPDATA["btime"]["hour"]
    e = APPDATA["btime"]["minute"]
    g = APPDATA["btime"]["second"]
except:
    APPDATA["btime"]["year"] = x.year
    APPDATA["btime"]["month"] = x.month
    APPDATA["btime"]["day"] = x.day
    APPDATA["btime"]["hour"] = x.hour
    APPDATA["btime"]["minute"] = x.minute
    APPDATA["btime"]["second"] = x.second
    a = x.year
    b = x.month
    c = x.day
    d = x.hour
    e = x.minute
    g = x.second
else:
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        e = int(e)
        g = int(g)
    except:
        APPDATA["btime"]["year"] = x.year
        APPDATA["btime"]["month"] = x.month
        APPDATA["btime"]["day"] = x.day
        APPDATA["btime"]["hour"] = x.hour
        APPDATA["btime"]["minute"] = x.minute
        APPDATA["btime"]["second"] = x.second
        a = x.year
        b = x.month
        c = x.day
        d = x.hour
        e = x.minute
        g = x.second
try:
    d0 = datetime.datetime(a,b,c,d,e,g)
except:
    if not APPDATA["legacyStartups"]:
        print("Invalid btime!")
    d0 = datetime.datetime(x.year,x.month,x.day,x.hour,x.minute,x.second)
d1 = datetime.datetime(x.year,x.month,x.day,x.hour,x.minute,x.second)
diff = d1-d0
ts = diff.total_seconds()
if not APPDATA["legacyStartups"]:
    print('You opened Basic Utilities for the first time in',ts,'seconds!')
APPDATA["btime"]["year"] = x.year
APPDATA["btime"]["month"] = x.month
APPDATA["btime"]["day"] = x.day
APPDATA["btime"]["hour"] = x.hour
APPDATA["btime"]["minute"] = x.minute
APPDATA["btime"]["second"] = x.second
updateappdata()
if not APPDATA["legacyStartups"]:
    print('')
    print("Welcome to Basic Utilities,",sysuser)

x = datetime.datetime.now()
if not APPDATA["legacyStartups"]:
    if x.hour > 0 and x.hour < 12:
        print('Good morning,',sysuser)
    elif x.hour > 11 and x.hour < 18:
        print('Good afternoon,',sysuser)
    elif x.hour > 17 and x.hour < 22:
        print('Good evening,',sysuser)
    else:
        print('Good night,',sysuser)
nua = False
if reqins == True and haspkg:
    SYSVERNUM = version.parse(SYSVERDATA["version"])
    SYSVERSION = version.parse(SYSVERSION)
    if SYSVERNUM > SYSVERSION:
        if not APPDATA["legacyStartups"]:
            if APPDATA["useColouredText"]:
                termcolor.cprint('New update found. Run the update command to download it',"green")
            else:
                print("A new update has been found. Run the update command to download it.")

        log('Found new update '+SYSVERDATA["version"])
        nua = True
if not APPDATA["legacyStartups"]:
    if APPDATA["useColouredText"]:
        termcolor.cprint("TODAY'S MESSAGE: "+MESSAGE,"blue")
    else:
        print("Today's Mesasge:",MESSAGE)
pinit("Preparing functions part 4")
class fconv():
    
    def __init__(self,start,end,formula):
        self.start = start
        self.end = end
        self.formula = formula
        self.root = Tk()
        self.root.title("Converter")
        self.lbl = Label(self.root,text=f"Converting {self.start} to {self.end}")
        self.lbl.grid(column=0,row=0)
        self.ent = Entry(self.root,width=50)
        self.ent.grid(column=0,row=1)
        
        self.ent2 = Entry(self.root,width=50)
        self.ent2.grid(column=0,row=2)
        
        self.btn = Button(self.root,text="Exit",command=self.root.destroy)
        self.btn.grid(column=1,row=0)
        while True:
            try:
                e = self.ent.get()
                
                self.ent2.delete(0,END)
                try:
                    e = int(e)
                except Exception as ex:
                    self.ent2.insert(END,"Error "+str(ex))
                else:
                    try:
                        self.ent2.insert(END,str(eval(formula)))
                    except Exception as ex:
                        self.ent2.insert(END,"Error "+str(ex))
                
                sleep(0.1)
                self.root.update()
            except:
                break

class fconv():
    
    def __init__(self,start,end,formula):
        self.start = start
        self.end = end
        self.formula = formula
        self.root = Tk()
        self.root.title("Converter")
        self.lbl = Label(self.root,text=f"Converting {self.start} to {self.end}")
        self.lbl.grid(column=0,row=0)
        self.ent = Entry(self.root,width=50)
        self.ent.grid(column=0,row=1)
        
        self.ent2 = Entry(self.root,width=50)
        self.ent2.grid(column=0,row=2)
        
        self.btn = Button(self.root,text="Exit",command=self.root.destroy)
        self.btn.grid(column=1,row=0)
        while True:
            try:
                e = self.ent.get()
                
                self.ent2.delete(0,END)
                try:
                    e = int(e)
                except Exception as ex:
                    self.ent2.insert(END,"Error "+str(ex))
                else:
                    try:
                        self.ent2.insert(END,str(eval(formula)))
                    except Exception as ex:
                        self.ent2.insert(END,"Error "+str(ex))
                
                sleep(0.1)
                self.root.update()
            except:
                break
class dconv():
    
    def __init__(self,start,end,formula):
        self.start = start
        self.end = end
        self.formula = formula
        self.root = Tk()
        self.root.title("Converter")
        self.lbl = Label(self.root,text=f"Converting {self.start} to {self.end}")
        self.lbl.grid(column=0,row=0)
        self.ent = Entry(self.root,width=50)
        self.ent.grid(column=0,row=1)
        
        self.ent2 = Entry(self.root,width=50)
        self.ent2.grid(column=0,row=2)
        
        self.btn = Button(self.root,text="Exit",command=self.root.destroy)
        self.btn.grid(column=1,row=0)
        
        while True:
            try:
                e = self.ent.get()
                
                self.ent2.delete(0,END)
                try:
                    if self.start.lower().startswith("b") and self.end.lower().startswith("h"):
                        e = "0b"+str(e)
                        
                        e = int(e,base=2)
                        
                        e = hex(e)
                    elif self.start.lower().startswith("h") and self.end.lower().startswith("b"):
                        e = "0x"+str(e)
                        
                        e = int(e,base=16)
                        
                        e = bin(e)
                        
                    elif self.start.lower().startswith("b"):
                        e = "0b"+str(int(e))
                        
                        e = int(e,base=2)
                    elif self.start.lower().startswith("h"):
                        e = "0x"+e
                        e = int(e,base=16)
                    
                except Exception as ex:
                    self.ent2.insert(END,"Error "+str(ex))
                else:
                    try:
                        self.ent2.insert(END,str(e))
                    except Exception as ex:
                        self.ent2.insert(END,"Error "+str(ex))
                
                sleep(0.1)
                self.root.update()
            except:
                break
#Imported from Jsontree module (c) 2022 Enderbyte Programs
_space = "    "
def printhi(data):
    print("JSON:")
    gethi(data)
def gethi(dictdata,level=1):
    for it in dictdata.items():
        item = it[1]
        if isinstance(item,dict):
            print(level*"    "+it[0]+":")
            gethi(item,level=level+1)
        elif isinstance(item,list):
            print(level*"    "+it[0]+":")
            gethilist(item,level=level+1)
        else:
            print((level*"    ")+str(item))

def gethilist(data,level=1):
    for item in data:
        if isinstance(item,dict):
            print(level*_space+"obj:")
            gethi(item,level=level+1)
        elif isinstance(item,list):
            print(level*_space+"list:")
            gethilist(item,level=level+1)
        else:
            print((level*_space+str(item)))



if not FCON:
    try:
        APPDATA["restrictions"] = RESTRICTIONS
    except:
        RESTRICTIONS = {
            "disabled" : [

            ],
            "note" : {

            }
        }
        APPDATA["restrictions"] = RESTRICTIONS
updateappdata()
pinit("Finishing up")
ETIME = datetime.datetime.now()
stimetotal = ETIME - STIME
log(f"Startup is finished. Took {int(stimetotal.total_seconds()*1000)} milliseconds")
pinit("")
#now it begins...
print("\nType the command you wish to execute and press enter")
while xae == True:
    crashed = False
    CAL = True
    if not os.path.isdir(".temp"):
        log("Could not find temp dir",WARN)
        os.mkdir(".temp")
    CLIBANNED = ["te","art","letsdraw","clrclp","clipboard","rem","ytdownload","ytaudio","ytplaylist","ytplaylista","tar","untar","startsound","clock","diran","cmaj","permaping","ping","encode","translate","color","colour","cpg","timer","draw","sw","prank","browser"]
    CLICHG = ["allext","allextval","searchext","webdownload","search","scanall","folmem","filemem","rev","settings","config","cfg","options","clean your room","png2jpg","jpg2png"]
    command = input("Basic Utilities> ") 
    if command != "":
        log(f'{sysuser} executed command '+command)
    for note in APPDATA["restrictions"]["note"].items():
        if note[0] == "*":
            print("Note for this command:",note[1])
            break
        elif note[0] == command:
            print("Note for this command:",note[1])
    for restrict in APPDATA["restrictions"]["disabled"]:
        if restrict == "*":
            if APPDATA["useColouredText"]:
                termcolor.cprint("This command has been disabled.","red")
            else:
                print("This command has been disabled.")
            CAL = False
            break
        elif command == restrict:
            if APPDATA["useColouredText"]:
                termcolor.cprint("This command has been disabled.","red")
            else:
                print("This command has been disabled.")
            CAL = False
    if CLI:
        if command in CLIBANNED:
            print("This command does not support nogui mode.")
            CAL = False
        elif command in CLICHG:
            command += ".cli"
            log("Command found in CLI change list")
    if CAL:
        
        if command == "help" or command == "?":
            
            print("-----Commands List-----")
            print('-----Misc-----')
            print("help: Shows this list")
            
            print('seelog: View the log')
            
            print("draw: Draw with Turtle!")
            print("opendraw: Open a .trt file")
            print("credits: View credits.")
            print("contact: Get my email and Discord")
            print("colour: Find a colour")
            print("bday: Input your birthday to get a surprise on startup when it matches")
            print("wb: Visit our website")
            print("lockdown: lockdown your screen until you enter a password")
            print('settings: Change your settings')
            print('rev: Reverse the contents of a file')
            print("stat: Get some statistics of this program.")
            print('usr: change your username')
            print('startsound: Set your startup sound')
            print("anim: Get a little animation of a wheel.")
            print("erc: List of error codes")
            print("cmdrun: See how many commands you have run")
            print("msg: View today's message! (Request messages by sending me an email)")
            print("cver: See the current version")
            print('')
            print("-----USELESS COMMANDS-----")
            print("insult: Get insulted")
            print("prank: try it out :P")
            print('')
            print('-----System Interaction-----')
            print("stop: Stops this window")
            print("stopall: stops all BasicUtilities windows")
            print("reload: reloads this program.")
            
            if sysslash == '\\':
                print("logoff: Logs you out.")
                print("restart: Restarts your computer")
                print("shutdown: Shutdown your computer")
            print("browser: Open the Basic Utilities Browser.")
            print("dir: Get the directory that this program is installed to")
            print('')
            print('-----Games-----')
            print("game: Play Beat The Bank")
            print("snl: Play Snakes and Ladders [sc]")
            print("m8b: Magic 8 ball")
            print("cpg: Play the Cartesian Plane Game")
            print('game2: Play Discount Prodigy')
            
            print('')
            print('-----Preset Counters-----')
            print("meter: See how long it has been since COVID infected its first human.(VE COUNTER)")
            print("lnmeter: How long since life was normal?")
            print('progcount: How long since this program existed')
            print('')
            print('-----Clocks & Alarms-----')
            print("alarm: Open the alarm clock")
            print("time: Tells you the exact time")
            print("counter: make a counter")
            print("sw: Stop watch!")
            print("clock: Get an ongoing clock")
            
            print("timer: Pauseable Timer")
            print('')
            print('-----Random Generators-----')
            print("rng: Random Number Generator")
            print("cf: Coin Flip")
            print('hex: Random Hexadecimal Generator (x16)')
            print('hexbi: Random hexadecabinary generator (x62)')
            print('picker: Make a custom random generator')
            print('cpicker: Random colour picker')
            print('npicker: Random Name Picker (NOT TO BE TAKEN SERIOUSLY)')#Todo 1.11 pre 1
            print('tpicker: Random Town Picker (NOT TO BE TAKEN SERIOUSLY)')#Todo 1.11 pre 1
            print('fpicker: Get a randomly generated food product name')
            print('rname: Random Ruby Name Generator')
            #Ruby is my dog and she has a lot of names
            print('art: Get some random art')
            print('')
            print('-----Utility-----')
            print("lag: Measures your computer's lag.")
            print("autoclick: Click at ridiculous speeds")
            
            print("randpass: Get a random password.")
            
            print("encode: encode stuff so no one can read it")
            print("translate: Translate files back to readable") 
            print('ping: Ping an IP address')
            print('ip: Get your IPv4 address')
            print('permaping: Ping an IP address indefinitely')
            print('fstat: Read a file and get an statistics report on it in the form of *.*.fstat')
            print('cmd: Execute something on the Command Prompt')
            print('musplay: Play an audio file in the background')
            print('sysplat: Get your system platform, version, etc.')
            print('sysmem: Get some system memory statistics')
            print('folmem: Get memory statistics about a folder. [Warning for big folders]')
            print('filemem: Ge memory statistics about a file')
            print('bumem: Get a statistic about how much of YOUR memory WE are using!')
            print('tsklst: List all task running on the system')
            print('ip6: Get your Ipv6 address')
            print('update: check for updates')
            print('scanall: Get a list of all files in a directory')
            print('tar: Make tar.gz archive')
            print('untar: Uncompress a tar.gz archive')
            print('search: Search folders for files that contain things you input. Warning: Can take up lots of resources!')
            print('speed: How many equations can your computer do in 1 second?')
            print("webdownload: Download a web page to file")
            print("searchext: Search for files with a certain extension")
            print("allext: Get how many files with each extension are in a directory")
            print("allextval: allext, but values are sorted by value instead of alphabetized.")
            print("cputimes: Get some statistics about how much time your CPU has spent doing things.")
            print("cpuper: Get the cpu utilization percentage")
            print("cputimeg: Get a graph of the percentage of time that your CPU is doing something")
            print("cpucount: Get how many cpu cores you have")
            print("clockspeed: Get the cpu clock speed")
            print("vmem: Get how much RAM you have")
            print("pidlen: See how many PIDS you have running")
            print("progmem: See how much RAM Basic Utilities is using")
            print("procmem: See how much RAM any process is using.")
            print("diskspeed: Find out your disk speed")

            if sysslash == '\\':
                print('diran: Get directory statistics and write to file')
                print('te: Open the Text Editor that comes with this program.')
            
            
            print('')
            print('-----Calculators & Converters-----')
            print("apv: area, perimeter, and volume calculator [sc]")
            print('tempt: Temperature converter')
            print('degp: degrees to percent')
            print('pdeg: percent to degrees')
            print('pi: Get up to 100 digits of pi')    
            print("pa: Add percent")
            print("pr: Remove percent")
            print("pgpa: Percent to GPA")
            print("gpap: GPA to percent")
            print("avg: Get an average calculator")
            print("calc help: Help with the calculator")
            print("calc: Calculator")
            print("quiz: get a multiplication quiz up to 12x12")
            print("decbin: Convert decimal to binary")
            print("dechex: Convert decimal to hexadecimal")
            print("bindec: Convert binary to decimal")
            print("hexdec: Convert hexadecimal to decimal")
            print("binhex: Convert binary to hexadecimal")
            print("hexbin: Convert hexadecimal to binary")
            print("conv len: length converters [sc]")
            print('fibb: Generate the Fibbonacci sequence <-- Spelled wrong but who cares')
            print('prime: Generate all prime numbers up to a number')
            print('jpg2png: Convert a jpg to png')
            print('png2jpg: Convert a png to jpg')
            
            print('sqrpyr: Calculate volume of a rectangular pyramid.')
            print('tripyr: Calculate volume of a triangular pyramid')
            print('emc2: Calcuate th energy(joules) in a given object.')
            print("pyth: Use the pythagorean theorum")
            print("pyth3: Use the 3d pythagorean theorum")
            
            print('')
            print('-----Uninstalling and cleaning-----')
            print("uninstall: Uninstall this program completely")
            print("clr: Reset Basic Utilities' AppData.")
            print("rem: custom app data reset (you choose)")
            print('cln: Clean up files from old versions that you dont need')

            if sysslash == '\\':
                print('-----Sound-----')
                print('beep: Get a beep')
                print('curse: Have this program curse at you (no actual cursing)')

                print('toneup: Make a rising Tone')
                print('rmg: Random Music Generator')
                print('cmaj: Play the ascending C major scale')
                print('alm: Get a nice beepy alarm')
            print('')
            print('-----YouTube-----')
            print('ytdownload: Download a single video from YouTube')
            print("ytaudio: Download a video's audio only")
            print("ytplaylist: Download every video from a playlist")
            print("ytplaylista: Download all audio from every video on a playlist")
            print('')
            print("There are also some easter egg commands :)")
            print("")
            print('-----Debug-----')
            print('crash: Crash this program by raising a RuntimeError()')
            print("relapdat: Reload the appdata of this program (may cause severe issues!)")
            print("pyterm: Execute Python code")
            print("dumpvar: Dump all variables to a file")
            print("cver: See the current version")
            print("adprintout: Print out appdata")
            
            print("")
            print("-----Clipboard-----")
            print("clrclp: Clear the clipboard")
            print("clipboard: Write something to the clipboard")
            print("\n-----Modes-----")
            print("clion: Start CLI only mode")
            print("clioff: Stop CLI only mode")

        elif command == "jpg2png":
            lkk = filedialog.askopenfilename(filetypes=[("JPG images",".jpg")])
            try:
                print(lkk)
                im = PIL.Image.open(lkk)
            except Exception as e:
                print("Invalid filename",e)
            else:
                try:
                    print("Converting")
                    im.save(f"{os.path.splitext(lkk)[0]}.png")
                except:
                    print("Failed to save!")
                else:
                    print("Done!")

        elif command == "jpg2png.cli":
            lkk = input("File to convert: ")
            try:
                print(lkk)
                im = PIL.Image.open(lkk)
            except Exception as e:
                print("Invalid filename",e)
            else:
                try:
                    print("Converting")
                    im.save(f"{os.path.splitext(lkk)[0]}.png")
                except:
                    print("Failed to save!")
                else:
                    print("Done!")

        elif command == "png2jpg":
            lkk = filedialog.askopenfilename(filetypes=[("PNG image","*.png")])
            try:
                print(lkk)
                im = PIL.Image.open(lkk)
            except Exception as e:
                print("Invalid filename",e)
            else:
                try:
                    print("Converting")
                    im.save(f"{os.path.splitext(lkk)[0]}.jpg")
                except:
                    print("Failed to save!")
                else:
                    print("Done!")

        elif command == "png2jpg.cli":
            lkk = input("File to convert: ")
            try:
                print(lkk)
                im = PIL.Image.open(lkk)
            except Exception as e:
                print("Invalid filename",e)
            else:
                try:
                    print("Converting")
                    im.save(f"{os.path.splitext(lkk)[0]}.jpg")
                except:
                    print("Failed to save!")
                else:
                    print("Done!")

        elif command == "clion" :
            APPDATA["climode"] = True
            CLI = True
        elif command == "clioff":
            APPDATA["climode"] = False
            CLI = False

        elif command == "autoclick":
            clickspeed = input("What do you want your CPS to be? (use 0 for as much as possible)")
            try:
                clickspeed = int(clickspeed)
            except:
                print("Please only use numbers")
            else:
                if clickspeed < 0:
                    print("Invalid.")
                else:
                    try:
                        cps = 1/clickspeed
                    except ZeroDivisionError:
                        clickspeed = None
                    input("Press enter to begin autoclicking. Run the keybind ctrl+alt+s to stop it")
                    runnnn = True
                    def srun():
                        global runnnn
                        runnnn  = False
                    keyboard.add_hotkey("ctrl+alt+s",srun)
                    
                    m = Controller()
                    while runnnn:
                        
                        m.click(MButton.left,1)
                        if clickspeed is not None:
                            sleep(cps)

        elif command == "adprintout":
            printhi(APPDATA)

        elif command == "cver":
            print("=====Basic Utilities Version Information=====")
            print("Version",SYSVERSION)
            print("IsBeta",SNAPSHOT)
            print("SnapshotVersion",SNAPSHOTVERSION)
            print("AssembledVersion",ASSEMBLEDVERSION)

        elif command == "diskspeed":
            print("Assembling writeable")
            writreable = 1000000*"o"
            print("What directory do you want to test?")
            dtt = filedialog.askdirectory()
            if dtt != "":
                try:
                    stime0 = datetime.datetime.now()
                    with open(dtt+sysslash+"__speedtest__.null","w+") as f:
                        f.write(writreable)
                    stime1 = datetime.datetime.now()
                    os.remove(dtt+sysslash+"__speedtest__.null")
                    diff = stime1-stime0
                    diffms = diff.total_seconds()*1000
                    del writreable
                    print("Wrote 1 MB to disk in",diffms,"milliseconds")
                    print("Speed:",round(1/diff.total_seconds(),2),"MB/s")
                except PermissionError:
                    print("Error: Permission denied.")
                except ZeroDivisionError:
                    print("Your computer is so fast that we divided by zero.")

        elif command == "procmem":
            proc = input("Process to retrieve: ")
            try:
                proc = int(proc)
            except:
                print("Invalid input")
            else:
                try:
                    process = psutil.Process(proc)
                except:
                    print("Invalid process")
                else:
                    print(process.memory_info().rss/1000000,"MegaBytes")

        elif command == "progmem":
            process = psutil.Process(os.getpid())
            print(process.memory_info().rss/1000000,"MegaBytes")

        elif command == "pidlen":
            ssdsaf = psutil.pids()
            print("=====")
            print(len(ssdsaf))
            print("=====")

        elif command == "vmem":
            vmem = psutil.virtual_memory()
            print("Total:",vmem.total/1000000000,"Gigabytes")
            print("Available:",vmem.available/1000000000,"Gigabytes")
            print("In use:",100-(vmem.available/vmem.total)*100,"%")

        elif command == "clockspeed":
            print("-----")
            clockspeed = psutil.cpu_freq()
            print("Current:",clockspeed.current)
            print("Minimum:",clockspeed.min)
            print("Maximum:",clockspeed.max)
            print("-----")

        elif command == "cpucount":
            print("-----")
            print("Count:",str(psutil.cpu_count()))
            print("Non-logical:",str(psutil.cpu_count(logical=False)))
            print("-----")

        elif command == "cputimes":
            cputimes = psutil.cpu_times()
            print("-----")
            print("User",cputimes.user)
            print("Idle",cputimes.idle)
            print("System",cputimes.system)
            print("All times in seconds.")
            print("-----")

        elif command == "cputimeg":
            newwindow()
            try:
                s = turtle.getscreen()
                t = turtle.Turtle()
            except:
                s = turtle.getscreen()
                t = turtle.Turtle()
            turtle.hideturtle()
            t.hideturtle()
            turtle.tracer(False)
            t.penup()
            t.goto(-300,-100)
            t.pendown()
            t.goto(300,-100)
            t.goto(300,300)
            t.penup()
            t.goto(-300,300)
            t.pendown()
            t.write("100% 1000 ms lag")
            t.goto(-300,-100)
            t.write("0%")
            for i in range(19):
                t.penup()
                t.goto(-300,-100+(i*20+20))
                t.pendown()
                if -100+(i*20+20) < 110:
                    wst = str(int((t.pos()[1]+100)/2))+"%"
                else:
                    wst = "100% "+str(round((i-9)/10*1000))+" ms lag"
                t.write(wst)
                t.goto(300,-100+(i*20+20))
            turtle.update()
            t.penup()
            t.goto(-300,-100)
            cputimes = psutil.cpu_times()
            idle = cputimes.idle
            user = cputimes.user
            systm = cputimes.system
            ipos = t.pos()
            upos = t.pos()
            spos = t.pos()
            bpos = t.pos()
            wpos = -300
            print("\n\n\n")
            while True:
                try:
                    
                    wpos += 10
                    newcputimes = psutil.cpu_times()
                    nidle = newcputimes.idle
                    nuser = newcputimes.user
                    nsystm = newcputimes.system
                    idle = nidle-idle
                    user = nuser-user
                    systm = nsystm-systm
                    
                    idlep = idle / len(psutil.cpu_percent(percpu=True)) * 200
                    userp = user / len(psutil.cpu_percent(percpu=True)) * 200
                    systmp = systm / len(psutil.cpu_percent(percpu=True)) * 200
                    busytime = userp+systmp
                    bustime = user+systm
                    print("\033[F\033[F\033[F\033[F",end="")
                    print(" "*50)
                    print(" "*50)
                    print(" "*50)
                    print(" "*50)
                    print("\033[F\033[F\033[F\033[F",end="")
                    print(f"Idle: {idle/len(psutil.cpu_percent(percpu=True))*100}%")
                    print(f"user: {user/len(psutil.cpu_percent(percpu=True))*100}%")
                    print(f"system: {systm/len(psutil.cpu_percent(percpu=True))*100}%")
                    print(f"Overall busy: {bustime/len(psutil.cpu_percent(percpu=True))*100}%")
                    t.goto(ipos)
                    t.pencolor("red")
                    t.pendown()
                    t.goto(wpos,idlep-100)
                    ipos = t.pos()
                    t.penup()
                    t.pencolor("green")
                    t.goto(upos)
                    t.pendown()
                    t.goto(wpos,userp-100)
                    upos = t.pos()
                    t.penup()
                    t.pencolor("blue")
                    t.goto(spos)
                    t.pendown()
                    t.goto(wpos,systmp-100)
                    spos = t.pos()
                    t.penup()
                    t.pencolor("purple")
                    t.goto(bpos)
                    t.pendown()
                    t.goto(wpos,busytime-100)
                    bpos = t.pos()
                    cputimes = psutil.cpu_times()
                    idle = cputimes.idle
                    user = cputimes.user
                    systm = cputimes.system
                    turtle.update()
                    t.penup()
                    t.goto(ipos)
                    if wpos > 300:
                        t.clear()
                        t.pencolor("black")
                        t.penup()
                        t.goto(-300,-100)
                        t.pendown()
                        t.goto(300,-100)
                        t.goto(300,300)
                        t.penup()
                        t.goto(-300,300)
                        t.pendown()
                        t.write("100% 1000 ms lag")
                        t.goto(-300,-100)
                        t.write("0%")
                        for i in range(19):
                            t.penup()
                            t.goto(-300,-100+(i*20+20))
                            t.pendown()
                            if -100+(i*20+20) < 110:
                                wst = str(int((t.pos()[1]+100)/2))+"%"
                            else:
                                wst = "100% "+str(round((i-9)/10*1000))+" ms lag"
                            t.write(wst)
                            t.goto(300,-100+(i*20+20))
                        turtle.update()
                        t.penup()
                        t.goto(-300,-100)
                        wpos = -300
                        ipos = (-300,idlep-100)
                        upos = (-300,userp-100)
                        spos = (-300,systmp-100)
                        bpos = (-300,busytime-100)
                    sleep(1)
                except:
                    break

        elif command == "cpuper":
            print("Overall:",str(psutil.cpu_percent())+"%")
            cpuperd = psutil.cpu_percent(percpu=True)
            print("cores:")
            o = 0
            for core in cpuperd:
                o += 1
                print(str(o)+":",str(core)+"%")

        elif command == "clrclp":
            cllp = Tk()
            cllp.withdraw()
            cllp.clipboard_clear()
            cllp.clipboard_append("")
            cllp.update()
            cllp.destroy()
            

        elif command == "clipboard":
            clp = input("What to put on the clipboard: ")
            r = Tk()
            r.withdraw()
            r.clipboard_clear()
            r.clipboard_append(clp)
            r.update()
            r.destroy()
            
            
        elif command == "allext":
            print('Please choose directory to search')
            Tk().withdraw()

            root = filedialog.askdirectory()
            allf = []
            
            if os.path.isdir(root):
                print("Scanning... (Please wait, this may take some time.)")
                for path, subdirs, files in os.walk(root):
                    for name in files:
                        e = os.path.join(path,name).replace("/","\\").lower().split("\\")
                        if "." in e[len(e)-1]:
                            try:
                                n = os.path.join(path, name).replace("/","\\").lower().split(".")
                                n = n[len(n)-1]
                            except:
                                pass
                            else:
                                allf.append(n)
                
                print("Counting...")
                
                cval = collections.Counter(allf)
                cval_s = {k: v for k, v in sorted(cval.items(), key=lambda item: item[1])}
                cvals = list(cval_s.keys())
                cvals.sort()
                for item in cvals:
                    print(f"{item}: {cval_s[item]}")
                del allf
                del cval
                del cval_s
                del cvals

        elif command == "allext.cli":
            root = input("Directory to sort: ")
            
            if os.path.isdir(root):
                print("Scanning... (Please wait, this may take some time.)")
                for path, subdirs, files in os.walk(root):
                    for name in files:
                        e = os.path.join(path,name).replace("/","\\").lower().split("\\")
                        if "." in e[len(e)-1]:
                            try:
                                n = os.path.join(path, name).replace("/","\\").lower().split(".")
                                n = n[len(n)-1]
                            except:
                                pass
                            else:
                                allf.append(n)
                
                print("Counting...")
                
                cval = collections.Counter(allf)
                cval_s = {k: v for k, v in sorted(cval.items(), key=lambda item: item[1])}
                cvals = list(cval_s.keys())
                cvals.sort()
                for item in cvals:
                    print(f"{item}: {cval_s[item]}")
                del allf
                del cval
                del cval_s
                del cvals

        elif command == "allextval":
            print('Please choose directory to search')
            Tk().withdraw()

            root = filedialog.askdirectory()
            allf = []
            
            if os.path.isdir(root):
                print("Scanning... (Please wait, this may take some time.)")
                for path, subdirs, files in os.walk(root):
                    for name in files:
                        e = os.path.join(path,name).replace("/","\\").lower().split("\\")
                        if "." in e[len(e)-1]:
                            try:
                                n = os.path.join(path, name).replace("/","\\").lower().split(".")
                                n = n[len(n)-1]
                            except:
                                pass
                            else:
                                allf.append(n)
                
                print("Counting...")
                
                cval = collections.Counter(allf)
                cval_s = {k: v for k, v in sorted(cval.items(), key=lambda item: item[1])}
                
                for item in cval_s.keys():
                    print(f"{item}: {cval_s[item]}")
                del allf
                del cval
                del cval_s

        elif command == "allextval.cli":
            root = input("Directory to sort: ")
            
            if os.path.isdir(root):
                print("Scanning... (Please wait, this may take some time.)")
                for path, subdirs, files in os.walk(root):
                    for name in files:
                        e = os.path.join(path,name).replace("/","\\").lower().split("\\")
                        if "." in e[len(e)-1]:
                            try:
                                n = os.path.join(path, name).replace("/","\\").lower().split(".")
                                n = n[len(n)-1]
                            except:
                                pass
                            else:
                                allf.append(n)
                
                print("Counting...")
                
                cval = collections.Counter(allf)
                cval_s = {k: v for k, v in sorted(cval.items(), key=lambda item: item[1])}
                
                for item in cval_s.keys():
                    print(f"{item}: {cval_s[item]}")
                del allf
                del cval
                del cval_s

        elif command == "searchext":
            print('Please choose directory to search')
            Tk().withdraw()

            root = filedialog.askdirectory()
            wts = input("Search for what extension? (1 extension only, no dot required): ")
            wts = wts.replace(".","")
            how_many_files = 0
            print("Scanning...")
            if os.path.isdir(root):
                for path, subdirs, files in os.walk(root):
                    for name in files:
                        n = os.path.join(path, name)
                        if n.split(".")[len(n.split("."))-1] == wts:
                            print(n.replace("/","\\"))
                            how_many_files += 1
                print(f"{how_many_files} files were found matching your criteria.")
        elif command == "searchext.cli":
            root = input("Directory to search: ")
            wts = input("Search for what extension? (1 extension only, no dot required): ")
            wts = wts.replace(".","")
            how_many_files = 0
            print("Scanning...")
            if os.path.isdir(root):
                for path, subdirs, files in os.walk(root):
                    for name in files:
                        n = os.path.join(path, name)
                        if n.split(".")[len(n.split("."))-1] == wts:
                            print(n.replace("/","\\"))
                            how_many_files += 1
                print(f"{how_many_files} files were found matching your criteria.")
                
        elif command == "dumpvar":
            log("Dumping variables")
            
            #rip my RAM 2017-2022
            LVAR_PRSE = locals().items()
            dprse = str(datetime.datetime.now()).replace(":","").replace(" ","_")
            with open(os.getcwd()+"/.temp/"+f"vardump_{dprse}"+".txt","w+") as f:
                f.write("Variable dump at ")
                f.write(str(datetime.datetime.now()))
                f.write("\n")
                for item in list(LVAR_PRSE):
                    if item[0] != "LVAR_PRSE":
                        f.write(str(item[0]))
                        f.write(" : ")
                        f.write(str(item[1]))
                        f.write("\n")
            
            del LVAR_PRSE
            print("Module variables were dumped to \\.temp\\"+dprse+".txt")


        elif command == "relapdat":
            try:
                with open("appdata.json") as f:
                    a2 = json.load(f)
            except FileNotFoundError:
                print("Failed to find appdata file.")
            except json.decoder.JSONDecodeError:
                print("Appdata file is corrupt.")
            else:
                APPDATA = a2
                print("Appdata reloaded succesfully")

        elif command == "cmdrun":
            print("-----")
            print(APPDATA["commandsRun"])
            print("-----")

        elif command == "opendraw":
            lkk = filedialog.askopenfilename(filetypes=[("Turtle files",".trt")])
            try:
                CREATE_NEW_PROCESS_GROUP = 0x00000200
                DETACHED_PROCESS = 0x00000008
                
                p = subprocess.Popen(["BasicUtilities.exe", lkk,"-d"],stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True,creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP)
            except Exception as ex:
                print(str(ex))

        elif command == "hexbin":
            dconv("Hexadecimal","Binary","int(e)")

        elif command == "binhex":
            dconv("Binary","Hexadecimal","int(e)")

        elif command == "hexdec":
            dconv("Hexadecimal","Decimal","int(e)")

        elif command == "bindec":
            dconv("Binary","Decimal","int(e)")

        elif command == "decbin":
            fconv("Decimal","Binary","bin(e)")
        #code this later

        elif command == "dechex":
            fconv("Decimal","Hexadecimal","hex(e)")

        elif command == "":
            pass

        elif command == "msg":
            print("=====")
            print(MESSAGE)
            print("=====")

        elif command == "ytplaylist":
            ilk = input("Full url to playlist: ")
            try:
                p = Playlist(ilk)
            except Exception as e:
                print("Failed to download playlist:",e)
            else:
                print("Will download:")
                for v in p.video_urls:
                    y = YouTube(v)
                    print(y.title)
                print("What directory to save videos to?")
                lts = filedialog.askdirectory()
                if os.path.isdir(lts):
                    print("Downloading. This can take a few minutes")
                    for video in p.video_urls:
                        y = YouTube(video)
                        try:
                            y.check_availability()
                        except Exception as e:
                            print("Failed to download video",y.title,e)
                        else:
                            try:
                                stream = y.streams.get_highest_resolution()
                                stream.download(lts)
                            except Exception as e:
                                print("Failed to download",e)
                            else:
                                print("Downloaded",y.title)

        elif command == "ytplaylista":
            ilk = input("Full url to playlist: ")
            try:
                p = Playlist(ilk)
            except Exception as e:
                print("Failed to download playlist:",e)
            else:
                print("Will download:")
                for v in p.video_urls:
                    y = YouTube(v)
                    print(y.title)
                print("What directory to save audio to?")
                lts = filedialog.askdirectory()
                if os.path.isdir(lts):
                    print("Downloading. This can take a few minutes")
                    for video in p.video_urls:
                        y = YouTube(video)
                        try:
                            y.check_availability()
                        except Exception as e:
                            print("Failed to download audio for video",y.title,e)
                        else:
                            try:
                                stream = y.streams.get_audio_only()
                                stream.download(lts,filename=y.title+".mp3")
                            except Exception as e:
                                print("Failed to download",e)
                            else:
                                print("Downloaded",y.title)

        elif command == "pyth":
            pya = input("What is the length of A? ")
            try:
                pya = float(pya)
            except:
                print("Please put only numbers here")
            else:
                pyb = input("What is the length of B? ")
                try:
                    pyb = float(pyb)
                except:
                    print("Please put only numbers here")
                else:
                    print("Result:",((pya*pya)+(pyb*pyb))**(1/2))

        elif command == "pyth3":
            pya = input("What is the length of A? ")
            try:
                pya = float(pya)
            except:
                print("Please put only numbers here")
            else:
                pyb = input("What is the length of B? ")
                try:
                    pyb = float(pyb)
                except:
                    print("Please put only numbers here")
                else:
                    pyc = input("What is the length of C? ")
                    try:
                        pyc = float(pyc)
                    except:
                        print("Please put only numbers here")
                    else:
                        print("Result:",((pya*pya)+(pyb*pyb)+(pyc*pyc))**(1/2))

        elif command == "rem":
            Tk().withdraw()
            da0 = messagebox.askyesno("rem","Do you want to reset best quiz time?")
            if da0:
                APPDATA["besttime"] = 0
            Tk().withdraw()
            da1 = messagebox.askyesno("rem","Do you want to reset boot count?")
            if da1:
                APPDATA["bcount"] = 0
            Tk().withdraw()
            da2 = messagebox.askyesno("rem","Do you want to reset boot time?")
            if da2:
                APPDATA["btime"]["year"] = None
                APPDATA["btime"]["month"] = None
                APPDATA["btime"]["day"] = None
                APPDATA["btime"]["hour"] = None
                APPDATA["btime"]["minute"] = None
                APPDATA["btime"]["second"] = None
            Tk().withdraw()
            da3 = messagebox.askyesno("rem","Do you want to reset birthday?")
            if da3:
                APPDATA["bday"]["month"] = None
                APPDATA["bday"]["day"] = None
            Tk().withdraw()
            da4 = messagebox.askyesno("rem","Do you want to reset web history?")
            if da4:
                APPDATA["webhistory"].clear()
            Tk().withdraw()
            da5 = messagebox.askyesno("rem","Do you want to reset username?")
            if da5:
                APPDATA["username"] = "DefaultUser"
            Tk().withdraw()
            da6 = messagebox.askyesno("rem","Do you want to reset customization settings?")
            if da6:
                APPDATA["showCommandsRun"] = False
                APPDATA["useDownloadedSounds"] = True
                APPDATA["useColouredText"] = True
                APPDATA["legacyStartups"] = False
            Tk().withdraw()
            da7 = messagebox.askyesno("rem","Do you want to reset game statistics?")
            if da7:
                APPDATA["gamehealth"] = None
                APPDATA["gamexp"] = None
            Tk().withdraw()
            da8 = messagebox.askyesno("rem","Do you want to reset start-up sound?")
            if da8:
                APPDATA["startsound"] = None
            Tk().withdraw()
            da9 = messagebox.askyesno("rem","Do you want to clear how many commands you have run?")
            if da9:
                APPDATA["commandsRun"] = 0
            Tk().withdraw()
            da10 = messagebox.askyesno("rem","Do you want to clear the temporary directory?")
            if da10:
                shutil.rmtree(".temp")
            da11 = messagebox.askyesno("rem","Do you want to clear the crash report directory?")
            if da11:
                try:
                    shutil.rmtree("crash_reports")
                except:
                    pass
            da12 = messagebox.askyesno("rem","Do you want to clear the lag log?")
            if da12:
                try:
                    os.remove("lag.csv")
                except:
                    pass
            da13 = messagebox.askyesno("rem","Do you want to clear the assets folder?")
            if da13:
                try:
                    shutil.rmtree("assets")
                except:
                    pass
            updateappdata()
            print("Custom AppData cleaning complete")
            if da13:
                if consoleask("Do you want to reload? Not doing so could have unintended consequences."):
                    reload()

        elif command == 'webdownload' :
            wbdl = input("Web page to download: ")
            print("Please select the save file.")
            files = [('html webpage', '*.html')]
            Tk().withdraw()
            file = filedialog.asksaveasfile(filetypes = files, defaultextension = files)
            try:
                urllib.request.urlretrieve(wbdl,file.name)
            except: 
                pass
            else:
                print("Download is complete")
        elif command == 'webdownload.cli' :
            wbdl = input("Web page to download: ")
            file = input("File to save it to: ")
            try:
                urllib.request.urlretrieve(wbdl,file)
            except Exception as e: 
                print(f"Error {e}")
            else:
                print("Download is complete")

        elif command == 'ytdownload':
            print('Please input the full URL to the video of your choice and press enter')
            ytdownld = input()
            try:
                yx = YouTube(ytdownld)
                yx.check_availability()
            except:
                Tk().withdraw()
                messagebox.showerror('Error','Please input a valid video URL')
            else:
                def dlr():
                    global yx
                    ytw.quit()
                    ytw.destroy()
                    print('Preparing')
                    x = yx.streams.get_lowest_resolution()
                    print('Please select save file')
                    files = [('mp4 video', '*.mp4')]
                    Tk().withdraw()
                    file = filedialog.asksaveasfile(filetypes = files, defaultextension = files)
                    
                    print('Downloading')
                    x.download(filename=str(file.name))
                    print('Complete')

                def dhr():
                    global yx
                    ytw.quit()
                    ytw.destroy()
                    print('Preparing')
                    x = yx.streams.get_highest_resolution()
                    print('Please select save file')
                    files = [('mp4 video', '*.mp4')]
                    Tk().withdraw()
                    file = filedialog.asksaveasfile(filetypes = files, defaultextension = files)
                    
                    print('Downloading')
                    x.download(filename=str(file.name))
                    print('Complete')
                    
                ytw = Tk()
                ytw.title('Options')
                lbl = Label(ytw,text='Please select your option')
                lbl.grid(column=0,row=0)
                btn = Button(ytw,text='Cancel',bg='red',command=ytw.destroy)
                btn.grid(column=0,row=1)
                btn1 = Button(ytw,text='Download lowest resolution',bg='yellow',command=dlr)
                btn1.grid(column=1,row=0)
                btn2 = Button(ytw,text='Download highest resolution',bg='lime green',command=dhr)
                btn2.grid(column=1,row=1)
                ytw.mainloop()

        elif command == 'ytaudio':
            print('Please input the full URL to the video of your choice and press enter')
            ytdownld = input()
            try:
                yx = YouTube(ytdownld)
                yx.check_availability()
            except:
                Tk().withdraw()
                messagebox.showerror('Error','Please input a valid video URL')
            else:
                

                def dhr():
                    global yx
                    yta.quit()
                    yta.destroy()
                    print('Preparing')
                    x = yx.streams.get_audio_only()
                    print('Please select save file')
                    files = [('mp3 Audio', '*.mp3')]
                    Tk().withdraw()
                    file = filedialog.asksaveasfile(filetypes = files, defaultextension = files)
                    
                    print('Downloading')
                    x.download(filename=str(file.name))
                    print('Complete')
                    
                yta = Tk()
                yta.title('Options')
                lbl = Label(yta,text='Please select your option')
                lbl.grid(column=0,row=0)
                btn = Button(yta,text='Cancel',bg='red',command=yta.destroy)
                btn.grid(column=0,row=1)
                
                btn2 = Button(yta,text='Download',bg='lime green',command=dhr)
                btn2.grid(column=1,row=0)
                yta.mainloop()

        elif command == 'lockdown':
            Tk().withdraw()
            xlmy = messagebox.askyesno('Q','WARNING! If used improperly, this command can damage your system! Are you sure you want to do this?')
            if xlmy == True:
                print('What password do you want to set? (DO NOT FORGET IT)')
                pswd = input()
                def kill_con():
                    global txt
                    ent = txt.get()
                    global pswd
                    if ent == pswd or ent == 'YOU set' or ent == 'the password YOU set':
                        con.quit()
                        con.destroy()
                def bypass_ev():
                    pass
                con = Tk()
                con.attributes('-fullscreen',True)
                con.wm_attributes('-topmost',True)
                con.config(bg='blue')
                lbl = Label(con,text='This device has been locked down. Input the password YOU set and press exit to exit.',fg='white',bg='blue',font=('Arial',24))
                lbl.pack()
                txt = Entry(con,width=50)
                txt.pack()
                btn = Button(con,text='Exit',bg='lime green',command=kill_con)
                btn.pack()
                con.protocol('WM_DELETE_WINDOW',bypass_ev)
                con.mainloop()

        elif command == 'search':
            print('What to search for?')
            searchfor = input()
            print('Please choose directory')
            Tk().withdraw()

            root = filedialog.askdirectory()
            
            if os.path.isdir(root):
                for path, subdirs, files in os.walk(root):
                    for name in files:
                        fin = os.path.join(path, name)
                        if searchfor.lower() in name.lower():
                            print(fin.replace('/','\\'))
        elif command == 'search.cli':
            print('What to search for?')
            searchfor = input()
            root = input("Directory to search in: ")
            
            if os.path.isdir(root):
                for path, subdirs, files in os.walk(root):
                    for name in files:
                        fin = os.path.join(path, name)
                        if searchfor.lower() in name.lower():
                            print(fin.replace('/','\\'))

        elif command == 'speed':
            has_finished_counting = False
            def count_speed():
                global has_finished_counting
                sleep(1)
                has_finished_counting = True
            counting = 0
            th = threading.Thread(target=count_speed)
            th.start()
            while not has_finished_counting:
                counting += 1
            print('Equations/second:',counting)
                        
                
        elif command == 'tar':
            try:
                f = tarfile.open('archive.tar.gz',mode='x:gz')
            except:
                f = tarfile.open('archive.tar.gz',mode='w:gz')
            print('Please choose files')
            Tk().withdraw()
            files_to_add = filedialog.askopenfilenames()
            
            
            for files in files_to_add:
                f.add(files,arcname=os.path.basename(files))
            f.close()
            print('Please select file save directory')
            Tk().withdraw()
            file_to_save = filedialog.askdirectory()
            print('What should it be called (excluding file extension)')
            file_name = input()
            try:
                os.rename('archive.tar.gz',file_name+'.tar.gz')
                file_to_copy = file_name+'.tar.gz'
                shutil.copyfile(file_to_copy,file_to_save+sysslash+file_to_copy)
                os.remove(file_to_copy)
            except:
                toplevelerror('Error when copying file. You can find your archive as archive.tar.gz in this program"s folder.')

        elif command == 'untar':
            print('Please select file to uncompress')
            Tk().withdraw()
            ftu = filedialog.askopenfilename()
            print('Please select output directory')
            Tk().withdraw()
            ftx = filedialog.askdirectory()

            try:
                f = tarfile.open(ftu)
                f.extractall(ftx)
                f.close()
            except:
                toplevelerror('Could not uncompress')

        elif command == 'scanall':
            print('Please choose directory')
            Tk().withdraw()

            root = filedialog.askdirectory()
            how_many_files = 0
            if os.path.isdir(root):
                for path, subdirs, files in os.walk(root):
                    for name in files:
                        print(os.path.join(path, name).replace('/','\\'))
                        how_many_files += 1
                print('Files:',how_many_files)
                
            else:
            
                print('Invalid directory')
            
        elif command == 'scanall.cli':
            root = input("Directory to scan: ")
            how_many_files = 0
            if os.path.isdir(root):
                for path, subdirs, files in os.walk(root):
                    for name in files:
                        print(os.path.join(path, name).replace('/','\\'))
                        how_many_files += 1
                print('Files:',how_many_files)
                
            else:
            
                print('Invalid directory')
            

        elif command == 'update':
            if nua == True:
                
                Tk().withdraw()
                m = messagebox.askyesno('Update Services','A new update ('+SYSVERDATA["version"]+') is available. Do you want to download and install it?\nChangelog:\n'+SYSVERDATA["changelog"].replace(",","\n"))
                if m == True:
                    print("Preparing...")
                    fname = os.getcwd()+"\\.temp\\update_"+SYSVERDATA["version"]+".exe"
                    print("Downloading...")
                    urllib.request.urlretrieve(SYSVERDATA["link"],fname)
                    log('Downloaded new update '+SYSVERDATA["version"])
                    print("starting...")
                    CREATE_NEW_PROCESS_GROUP = 0x00000200
                    DETACHED_PROCESS = 0x00000008
                    insnm = "install_"+str(datetime.datetime.now()).replace(" ","_").replace(":","_").replace(".","_")+".log"
                    insfn = os.getcwd()+sysslash+".temp"+sysslash+insnm
                    p = subprocess.Popen([fname,"/SILENT","/CLOSEAPPLICATIONS",f"/LOG={insfn}"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP)
                    os.system("taskkill /f /im BasicUtilities.exe")
            else:
                Tk().withdraw()
                messagebox.showinfo('BU','No new updates are available')

        elif command == 'seelog':
            if os.path.isfile("log_000.log"):
                with open("log_000.log") as f:
                    lns = f.readlines()
                for logval in lns:
                    try:
                        if logval.split(" ")[2] == "INFO":
                            print(logval.replace("\n",""))
                        if logval.split(" ")[2] == "WARN":
                            termcolor.cprint(logval.replace("\n",""),"yellow")
                        if logval.split(" ")[2] == "ERROR":
                            termcolor.cprint(logval.replace("\n",""),"red")
                        if logval.split(" ")[2] == "ERROR":
                            termcolor.print(logval.replace("\n",""),"white","on_red")
                    except:
                        termcolor.cprint(logval.replace("\n",""),"white","on_red")
                del lns
        elif command == 'startsound':
            startsound = APPDATA["startsound"]
            if startsound is not None:
                if os.path.isfile(startsound):
                    print("Your startsound is currently",startsound)
                else:
                    print("current startsound contains invalid data.")
            else:
                print("You currently do not have a start sound set")
            print('Please select a start sound')
            print(".wav files and some .mp3 is supported.")
            Tk().withdraw()
            dlf = filedialog.askopenfilename()
            print(dlf)
            
            try:
                playsound(str(dlf))
            except:
                Tk().withdraw()
                messagebox.showerror('BU','File is unreadable')
            else:
                APPDATA["startsound"] = dlf
                updateappdata()
                print('Startup sound set to',dlf)
                log('Changed startsound')

        elif command == 'te':
            
            CREATE_NEW_PROCESS_GROUP = 0x00000200
            DETACHED_PROCESS = 0x00000008
            try:
                p = subprocess.Popen(["BasicUtilities.exe", "-n"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP)
            except:
                Tk().withdraw()
                messagebox.showerror('BU','Unable to start.')

        elif command == 'art':
            try:
                s = turtle.getscreen()
                t = turtle.Turtle()
            except:
                s = turtle.getscreen()
                t = turtle.Turtle()
            t.speed(0)
            t.penup()
            t.goto(-300,-300)
            t.pendown()
            t.goto(-300,300)
            t.goto(300,300)
            t.goto(300,-300)
            t.goto(-300,-300)
            t.penup()
            t.goto(0,0)
            t.pendown()
            colours = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
            'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
            'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
            'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
            'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
            'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
            'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
            'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
            'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
            'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
            'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
            'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
            'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
            'indian red', 'saddle brown', 'sandy brown',
            'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
            'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
            'pale violet red', 'maroon', 'medium violet red', 'violet red',
            'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
            'thistle', 'snow2', 'snow3',
            'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
            'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
            'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
            'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
            'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
            'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
            'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
            'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
            'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
            'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
            'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
            'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
            'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
            'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
            'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
            'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
            'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
            'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
            'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
            'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
            'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
            'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
            'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
            'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
            'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
            'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
            'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
            'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
            'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
            'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
            'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
            'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
            'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
            'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
            'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
            'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
            'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
            'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
            'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
            'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
            'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
            'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
            'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
            'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
            'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
            'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4','gray60']
            for i in range(random.randint(10,200)):
                try:
                    t.pencolor(random.choice(colours))
                    t.pensize(random.randint(1,10))
                    t.goto(random.randint(-300,300),random.randint(-300,300))
                    t.right(random.randint(0,360))
                    exec(random.choice(['t.dot(random.randint(1,20))','t.circle(random.randint(1,20))','print("")','print("")']))
                except:
                    crashed = True
                    break
            if crashed == False:
                Tk().withdraw()
                mmop = messagebox.askyesno('Art','Do you want to export this to a .trt file?')
                if mmop == True:
                    
                    print("saving...")
                
                    BACKGROUND = "#ffffff"
                    
                    t.hideturtle()
                    try:
                        
                        e = []
                        print("Assembling list...")
                        for x in range(int(-300),int(300)):
                            for y in range(int(-300),int(300)):
                                e.append((x,y))
                        files = [('Turtle file','*.trt')]
                        print("Please select save file")    
                        g = filedialog.asksaveasfile(filetypes=files,defaultextension=files)
                        
                        bar = ProgressBar(total=360000,bar_length=100,prefix="Writing",spinner_type="s")
                        with open(g.name,"w+") as f:
                            f.write("b "+BACKGROUND+"\n")
                            for coord in e:
                                l = get_pixel_color(coord[0],coord[1])
                                if l != BACKGROUND:
                                    f.write("p "+str(coord[0])+" "+str(coord[1])+" "+l+"\n")
                                bar.iter()
                                bar.suffix = " "+str(coord[0])+" "+str(coord[1])
                        space = " "
                        bar.stop()
                        print(f"\r{space*100}\rFinished")
                    except Exception as ex:
                        toplevelerror("Failed to save "+str(ex))
                    finally:
                        t.showturtle()
                messagebox.showinfo('BU','Done. Dismiss this messagebox when you are ready to close turtle window')
                turtle.bye()
            


        elif command == 'usr':
            print(f"Your current username is {sysuser}")
            print('Please input your new name')
            sysuser = input()
            APPDATA["username"] = sysuser
            updateappdata()
        

        elif command == 'rname':
            rname = ''
            for i in range(random.randint(1,20)):
                rname += str(random.choice(['Ruby','Roo','Roobster','Doo','By','By','By','Boo','Dy','Doodle','r','oo','oo','dle','oobster']))
            rname = rname.replace('BooB','RooB')
            print(rname)

        elif command == 'clock':
            newwindow()
            isfini = False
            def cloc():
                sleep(1)
                global lbl
                global isfini
                while isfini == False:
                    sleep(0.1)
                    try:
                        lbl.configure(text=str(datetime.datetime.now()))
                    except:
                        break
                    
            def ckill():
                global isfini
                isfini = True
                clk.quit()
                clk.destroy()
                
            th = threading.Thread(target=cloc)
            th.start()
            clk = Tk()
            clk.title('Clock')
            clk.geometry('150x50')
            lbl = Label(clk,text='')
            lbl.grid(column=0,row=0)
            btn = Button(clk,text='Exit',bg='red',command=ckill)
            btn.grid(column=0,row=1)
            clk.mainloop()
            

        elif command == 'fpicker':
            print('-----')
            print(random.choice(['Nutra','nutri','health','good','fod'])+random.choice(['-o-','er','','',''])+random.choice(['loaf','fod','snak','fodder','health','food']))
            print('-----')

        elif command == 'shutdown':
            os.system("shutdown /s /t 0")

        elif command == 'tkdebug':
            
            
            messagebox.showinfo('Basic Utilities','Test')
            Tk().withdraw()
            Tk().destroy()
            Tk().withdraw()
            filedialog.askopenfilename()
            filedialog.askdirectory()

        
        elif command == 'alm':
            for i in range(10):
                winsound.Beep(1500,500)
                winsound.Beep(1000,500)

        elif command == 'diran':
            print('Please select the folder to analyze')
            Tk().withdraw()
            dtoo = filedialog.askdirectory()
            
            cdt = datetime.datetime.now()
            try:
                os.system('cd '+dtoo+'&'+' dir'+'&'+' dir > directoryanalysis.txt')
            except:
                error(0)
            else:
                try:
                    total_size = 0
                    
                    for path, dirs, files in os.walk(dtoo):
                        for f in files:
                            fp = os.path.join(path, f)
                            total_size += os.path.getsize(fp)
                    print("Directory size: " + str(total_size),'Bytes')
                    print('folder is using',(total_size / shutil.disk_usage(sysslash)[1]*100),'% of YOUR used memory ')
                    print('folder is using',(total_size / shutil.disk_usage(sysslash)[0]*100),'% of YOUR total memory ')
                except:
                    Tk().withdraw()
                    messagebox.showerror('Error','Could not access directory to count size')
                try:
                    f = open(dtoo+sysslash+'directoryanalysis.txt','a')
                except:
                    error(0)
                else:
                    f.write('\n')
                    f.write('Directory analysis for '+dtoo+'\n')
                    f.write('Made on '+str(datetime.datetime.now())+'\n')
                    try:
                        f.write('Total Directory Size: '+str(total_size)+' Bytes'+'\n')
                    except:
                        f.write('Could not get total directory size')
                    else:
                        f.write('folder is using '+str((total_size / shutil.disk_usage(sysslash)[1]*100))+' % of YOUR used memory'+'\n')
                        f.write('folder is using '+str((total_size / shutil.disk_usage(sysslash)[0]*100))+' % of YOUR total memory ')
                    f.close()
                    print('Statistics written to '+dtoo+sysslash+'directoryanalysis.txt')
        elif command == 'tsklst':
            os.system('tasklist')


        elif command == 'cln':
            fcln = 0
            try:
                os.remove('pre-uninstall.bat')
                fcln +=1
            except:
                fcln +=0
            try:
                os.remove('logoff.bat')
            except:
                fcln+=0
            else:
                fcln +=1
            try:
                os.remove('restart.bat')
                fcln +=1
            except:
                fcln +=0
            try:
                os.remove('clrapdat.bat')
                fcln +=1
            except:
                fcln +=0
            try:
                os.remove('ping.bat')
                fcln +=1
            except:
                fcln +=0
            try:
                os.remove('permaping.bat')
                fcln +=1
            except:
                fcln +=0
            try:
                os.remove('execute.bat')
                fcln +=1
            except:
                fcln +=0
            try:
                os.remove('stop.bat')
                fcln +=1
            except:
                fcln +=0
            try:
                os.remove('notes.txt')
                fcln +=1
            except:
                fcln +=0
            try:
                os.remove('notice.txt')
                fcln +=1
            except:
                fcln +=0
            try:
                os.remove('changelog.txt')
                fcln +=1
            except:
                fcln +=0
            try:
                os.remove('license.txt')
                fcln +=1
            except:
                fcln +=0
            try:
                os.remove('warning.mp3')
                fcln +=1
            except:
                fcln +=0
            
            print(fcln,' useless files removed.')
            log(f'{sysuser} cleaned out old files')


        elif command == 'emc2':
            print('Mass of Object? (kilograms please)')
            m = input()
            try:
                m = float(m)
            except:
                error(1)
            else:
                c = 299792458
                c2 = c**2
                e = m*c2
                print('Energy: '+str(e))

        elif command == 'sqrpyr':
            print('Length?')
            l = input()
            try:
                l = int(l)
            except:
                error(1)
            else:
                print('Width?')
                w = input()
                try:
                    w = int(w)
                except:
                    error(1)
                else:
                    print('Height?')
                    h = input()
                    try:
                        h = int(h)
                    except:
                        error(1)
                    else:
                        print('The volume is '+str((l*w*h)/3)+' Cubic Units')

        elif command == 'tripyr':
            print('Length?')
            l = input()
            try:
                l = int(l)
            except:
                error(1)
            else:
                print('Width?')
                w = input()
                try:
                    w = int(w)
                except:
                    error(1)
                else:
                    print('Height?')
                    h = input()
                    try:
                        h = int(h)
                    except:
                        error(1)
                    else:
                        print('The volume is '+str(((l*w)/2*h)/3)+' Cubic Units')

        elif command == 'bumem':
            dirpath = os.getcwd()
            try:
                total_size = 0
                
                for path, dirs, files in os.walk(dirpath):
                    for f in files:
                        fp = os.path.join(path, f)
                        total_size += os.path.getsize(fp)
                print("Directory size: " + str(total_size),'Bytes')
                print('we are using',(total_size / shutil.disk_usage(sysslash)[1]*100),'% of YOUR used memory :)')
                print('we are using',(total_size / shutil.disk_usage(sysslash)[0]*100),'% of YOUR total memory :)')
            except:
                print("Basic Utilities in unable to access its own folder. What a shame")

        elif command == 'filemem':
            Tk().withdraw()
            file_path = filedialog.askopenfilename()
            try:
                fsize = os.path.getsize(file_path)
                print('Size:',fsize,'Bytes')
                print('This file accounts for',(fsize / shutil.disk_usage(sysslash)[1]*100),'% of used memory')
                print('This file accounts for',(fsize / shutil.disk_usage(sysslash)[0]*100),'% of total memory')
            except:
                error(1)

        elif command == 'filemem.cli':
            file_path = input("File to scan: ")
            try:
                fsize = os.path.getsize(file_path)
                print('Size:',fsize,'Bytes')
                print('This file accounts for',(fsize / shutil.disk_usage(sysslash)[1]*100),'% of used memory')
                print('This file accounts for',(fsize / shutil.disk_usage(sysslash)[0]*100),'% of total memory')
            except:
                error(1)

        elif command == 'sysmem':
            memory = shutil.disk_usage(sysslash)
            print('Total Memory '+str(memory[0])+' Bytes')
            print('Used Memory '+str(memory[1])+' Bytes')
            print('Free Memory '+str(memory[2])+' Bytes')
            print('You have used',((memory[1]/memory[0])*100),'%')

        elif command == 'folmem':
            total = 0
            Tk().withdraw()
            dirpath = filedialog.askdirectory()
            if str(dirpath) == '()':
                print('')
            else:
                try:
                    total_size = 0
                    
                    for path, dirs, files in os.walk(dirpath):
                        for f in files:
                            fp = os.path.join(path, f)
                            total_size += os.path.getsize(fp)
                    print("Directory size: " + str(total_size),'Bytes')
                    print('This folder accounts for',(total_size / shutil.disk_usage(sysslash)[1]*100),'% of used memory')
                    print('This folder accounts for',(total_size / shutil.disk_usage(sysslash)[0]*100),'% of total memory')
                except Exception as e:
                    print(f"ERROR in command: {e}")

        elif command == 'folmem.cli':
            total = 0
            dirpath = input("Folder to scan: ")
            if str(dirpath) == '()':
                pass
            else:
                try:
                    total_size = 0
                    
                    for path, dirs, files in os.walk(dirpath):
                        for f in files:
                            fp = os.path.join(path, f)
                            total_size += os.path.getsize(fp)
                    print("Directory size: " + str(total_size),'Bytes')
                    print('This folder accounts for',(total_size / shutil.disk_usage(sysslash)[1]*100),'% of used memory')
                    print('This folder accounts for',(total_size / shutil.disk_usage(sysslash)[0]*100),'% of total memory')
                except Exception as e:
                    print(f"ERROR in command: {e}")
        elif command == 'stat':
            print('lines: 7720')
            print('print statements: 1106')
            print('Variables: 1954')
            print('comparisons 2000')
            print('Exception handling loops 313')
            print('While loops 56')
            print('For loop 103')
            print('Commands: 192')
            print('Libraries Imported 28')
            print('files utilized 77')
            print('Tkinter windows used 103')
            print("Functions: 150")
            print("Classes: 4")

        elif command == 'sysplat':
            print('-----')
            print(platform.system())
            print(platform.release())
            print(platform.platform())
            print('-----')

        elif command == 'dir':
            print('-----')
            print(os.getcwd())
            print('-----')

        elif command == 'npicker':
            let = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t''u','v','w','x','y','z']
            print('-----')
            for i in range(random.randint(2,12)):
                print(random.choice(let),end='',flush=True)
            print('')
            print('-----')

        elif command == 'tpicker':
            prefixes = ['she','kensing','park','new','Burn','Squa','Whis','Morton','Farris','Kalmy','Ruby','Fansing','','PArks','Sur','Castle']
            mid = ['field','aby','st','','','','Dooby']
            end = ['ton','ville','vill','don','hood','','Rey']
            print('-----')
            print(random.choice(prefixes)+random.choice(mid)+random.choice(end))
            print('-----')

        elif command == 'musplay':
            newwindow()
            file_path = filedialog.askopenfilename()
            try:
                playsound(file_path)
            except:
                error(1)

        elif command == 'rev':

            Tk().withdraw()
            file_path = filedialog.askopenfilename()
            f = open(file_path)
            data = f.read()
            strlen = len(data)
            newstr = data[strlen::-1]
            print(newstr)
            f.close()
            try:
                f = open(file_path+'rev','x')
            except:
                f = open(file_path+'rev','x')
            f.write(newstr)
            f.close()

        elif command == 'rev.cli':

            file_path = input("File to reverse: ")
            try:
                f = open(file_path)
                data = f.read()
                strlen = len(data)
                newstr = data[strlen::-1]
                print(newstr)
                f.close()
                try:
                    f = open(file_path+'rev','x')
                except:
                    f = open(file_path+'rev','x')
                f.write(newstr)
                f.close()
            except:
                error(1)
        elif command == 'pi':
            print('How many units')
            units = input()
            try:
                units = int(units)
            except:
                error(1)
            else:
                piq = str('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
                print(piq[0:units])

        elif command == 'prime':
            num = 0
            prime = 0
            print('All prime numbers up to what?')
            units = input()
            try:
                units = int(units)
            except:
                error(1)
            else:
                for i in range(units):
                    num += 1
                    if num > 1:
                        for i in range(2,int(num/2)+1):
                            if (num % i) == 0:
                                nqtye = 0
                                break
                        else:
                            print(num)
                            prime += 1
                    else:

                        nqtye = 0
                
                print('There were',prime,'prime numbers in that set')
                try:
                    print('The prime number percent value is',str(prime/units*100)+' percent')
                except:
                    print("We tried to print a percent, but you decided to devide by 0")
        elif command == 'fibb':
            print('How many units?')
            cmz = input()
            try:
                cmz = int(cmz)
            except:
                error(1)
            else:
                a = 0
                b = 1
                if cmz > 0:
                    print(1)
                for i in range(cmz-1):
                    c = a + b
                    print(c)
                    a = b
                    b = c

        elif command == 'cmaj':
            if sysslash == '\\':
                x = 500
                winsound.Beep(261,x)
                winsound.Beep(293,x)
                winsound.Beep(329,x)
                winsound.Beep(349,x)
                winsound.Beep(392,x)
                winsound.Beep(440,x)
                winsound.Beep(493,x)
                winsound.Beep(523,x)
            else:
                Tk().withdraw()
                messagebox.showerror('BU','This command is not compatible with your device')

        elif command == 'fstat':
            fta = input("File to analyze: ")
            try:
                f = open(fta,'r')
            except:
                error(2)
            else:
                try:
                    data = f.read()
                except:
                    f.close()
                    Tk().withdraw()
                    messagebox.showinfo('File Error','Basic Utilities cannot read this file. It may be compressed or unreadable.')
                else:
                    size = len(data)
                    print('Will write file statistics to',fta+'.fstat')
                    if size < 1000:
                        print('PREVIEW:')
                        print('-----')
                        print(data)
                        print('-----')
                    else:
                        print('Oops! File was to large to preview')
                    print('Characters:',size)
                    if size < 1000:
                        fs = size
                        fs = str(str(fs)+' bytes')
                        print('File Size:',size,'bytes')
                    elif size > 1000 and size < 1000000:
                        fs = size/1024
                        print('File Size:',fs,'kilobytes')
                        fs = str(str(fs)+' kilobytes')
                    else:
                        fs = size /1000/1024
                        print('File Size:',fs,'megabytes')
                        fs = str(str(fs)+ ' megabytes')
                    aol = 0
                    f.close()
                    f = open(fta)
                    tiwieyc = f.readlines()
                    while True:
                        try:    
                            x = tiwieyc[aol]
                            aol = aol + 1
                        except:
                            break
                    print('Amount of lines:',aol)
                    tw = fta+'.fstat'
                    print('Writing to',tw)
                    f.close()
                    try:
                        f = open(tw,'x')
                        f.write('Characters = '+str(size)+'\n')
                        f.write('Size = '+str(fs)+'\n')
                        f.write('Lines = '+str(aol)+'\n')
                        
                    except:
                        f = open(tw,'w')
                        f.write('Characters = '+str(size)+'\n')
                        f.write('Size = '+str(fs)+'\n')
                        f.write('Lines = '+str(aol)+'\n')
                        
                    finally:
                        f.close()
                    

        elif command == 'permaping':
            def pgo0():
                global txt
                res = txt.get()
                pping.destroy()
                pping.quit()
                
                try:
                    os.system('ping '+res+' -t')
                except:
                    error(1)
            pping = Tk()
            pping.title('permapinger')
            lbl = Label(pping,text='IP address to ping')
            lbl.grid(column=0,row=0)
            btn = Button(pping,text='Close',command=pping.destroy,bg='yellow')
            btn.grid(column=1,row=0)
            txt = Entry(pping,width=20)
            txt.grid(column=0,row=1)
            btn1 = Button(pping,text='Ping',command=pgo0,bg='green')
            btn1.grid(column=1,row=1)
            pping.mainloop()
            pping.quit()

        elif command =='ping':
            def pgo1():
                global txt
                global txt1
                global btn1
                btn1['state'] = 'disabled'
                res = txt.get()
                res1 = txt1.get()
                try:
                    os.system('ping '+res+' -n '+res1)
                except:
                    error(3)
                btn1['state'] = 'normal'
            ping = Tk()
            ping.title('pinger')
            lbl = Label(ping,text='IP address to ping')
            lbl1 = Label(ping,text='Number of times to ping')
            lbl.grid(column=0,row=0)
            lbl1.grid(column=1,row=0)
            btn = Button(ping,text='Close',command=ping.destroy,bg='Yellow')
            btn.grid(column=2,row=0)
            txt = Entry(ping,width=20)
            txt.grid(column=0,row=1)
            txt1 = Entry(ping,width=10)
            txt1.grid(column=1,row=1)
            btn1 = Button(ping,text='Ping',command=pgo1,bg='green')
            btn1.grid(column=2,row=1)
            ping.mainloop()
            ping.quit()

        
        elif command == 'cmd':
            print("Type 'breakout' to exit back to the command menu. Execute multiple commands at once by seperating them with the & symbol.")
            while True:
                cmdtr = input(platform.platform()+" Command processor: ")
                if cmdtr.lower().replace("'","") == "breakout":
                    break
                else:
                    try:
                        os.system(cmdtr)
                    except Exception as e:
                        print("ERROR",e)
            
        elif command == 'ip':
            try:
                ip = get('https://api.ipify.org').text
                print('Your public IPv4 address is: {}'.format(ip))
            except Exception as e:
                toplevelerror('ERROR\n'+str(e))

        elif command == 'ip6':
            ip = get("http://ip6only.me/api/").text
            ip = ip.split(",")[1]
            print(f"Your ipv6 adress is {ip}")

        elif command == 'rmg':
            if sysslash == '\\':
                for i in range(random.randint(20,50)):
                    winsound.Beep(random.randint(200,1000),random.randint(200,1000))
            else:
                print("This command is only supported on Microsoft Windows (r) devices.")
                

        elif command == 'toneup':
            if sysslash == '\\':
                print('Starting tone? (HZ)')
                st = input()
                try:
                    st = int(st)
                except:
                    error(1)
                else:
                    print('Ending tone? (Hz)')
                    et = input()
                    try:
                        et = int(et)
                    except:
                        error(1)
                    else:
                        while st < et:
                            winsound.Beep(st,100)
                            st = st + 10
                            print('Played tone of',st,'Hertz')
            else:
                print("This command is only supported on Microsoft Windows (r) devices.")

        elif command == 'hex':
            print(random.choice([0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']))
        elif command == 'hexbi':
            print(random.choice([0,1,2,3,4,5,6,7,8,9,'q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']))

        elif command == 'curse':
            if sysslash == '\\':
                for i in range(random.randint(1,10)):
                    winsound.Beep(1000,random.randint(200,1500))
                    print(random.randint(1,10)*'*')
                    sleep(random.randint(1,10)/10)
            else:
                print("This command is only supported on Microsoft Windows (r) devices.")
                

        elif command == 'beep':
            if sysslash == '\\':
                print('What frequency?')
                freq = input()
                try:
                    freq = int(freq)
                except:
                    error(1)
                else:
                    print('How many milliseconds?')
                    playse = input()
                    try:
                        playse = int(playse)
                    except:
                        error(1)
                    else:
                        if playse > 0:
                            winsound.Beep(freq,playse)
                        else:
                            error(1)

            else:
                print("This command is only supported on Microsoft Windows (r) devices.")

        elif command == 'game2':
            newwindow()
            

            print('Welcome',sysuser,'to Discount Prodigy')
            print('Discount prodigy is a game where you cast spells against monsters.')
            print('To cast spells, you must answer simple math problems')
            print('As you cast spells, you earn points.')
            print('Press enter to begin.')
            input()
            fightmonsters = True
            monster_names = ['Black Widow','Wulf','Slayer','Shredder','Magma','The Kraken']
            monsters_battled = 0
            monsters_won = 0
            monsters_lost = 0
            xp = APPDATA["gamexp"]
            try:
                xp = float(xp)
            except:
                xp = 0
                APPDATA["gamexp"] = 0
            
            health = APPDATA["gamehealth"]
            try:
                health = float(health)
            except:
                health = 100
                APPDATA["gamehealth"] = 100
            updateappdata()
            blhealth = health
            blxp = xp
            while fightmonsters == True:
                print('A monster wants to battle you! do you want to battle?(y/n)')
                battle = input()
                if battle.lower().startswith('y'):
                    monsterbattle_name = random.choice(monster_names)
                    monster_health = health//(random.randint(12,24)/10)
                    blmh = monster_health
                    print('Your enemy is',monsterbattle_name)
                    print(monsterbattle_name,'has',monster_health,'health')
                    print('press enter to continue')
                    input()
                    if monsterbattle_name == 'Black Widow':
                        monster_spells = ['Poke','Venom','Crush']
                    elif monsterbattle_name == 'Wulf':
                        monster_spells = ['Claw','Bite','Slaughter']
                    elif monsterbattle_name == 'Slayer':
                        monster_spells = ['Execute','Corrupt','Overwrite the boot sector']
                    elif monsterbattle_name == 'Shredder':
                        monster_spells = ['Shred','Big shred','Ultra Shred']
                        # I am running out of ideas :(
                    elif monsterbattle_name == 'Magma':
                        monster_spells = ['Burn','Roast''Erupt']
                    elif monsterbattle_name == 'The Kraken':
                        monster_spells = ['Wave','Tsunami','Horror of the Deep']
                    else:
                        print("Unrecognized monster name. Reverting")
                        monster_spells = ['spell.placeholder.small','spell.placeholder.med','spell.placeholder.large']
                    spells = ['Wingardium Leviosa','Impedimenta','Avada Kedavra']
                    while monster_health > 0 and health > 0:
                        failed = False
                        print('Your spells are',spells[0],',',spells[1],',',spells[2])
                        print('What spell do you want to use? You may also use numbers 1,2,3.')
                        spell_used = input()
                        if spell_used == spells[0] or spell_used == spells[1] or spell_used == spells[2] or spell_used == '1' or spell_used == '2' or spell_used == '3':
                            if spell_used == spells[0] or spell_used == '1':
                                print('Answer this question')
                                a = random.randint(1,100)
                                b = random.randint(1,100)
                                print('What is',a,'+',b,'?')
                                answ = input()
                                try:
                                    answ = int(answ)
                                except:
                                    error(1)
                                    print('Because we cant kick you to the command menu, we will restart the program')
                                    reload()
                                else:
                                    if answ == a + b:
                                        print('You got it correct')
                                        spell_damage = blhealth /10 * (random.randint(10,20)/10)
                                        print('You did',spell_damage,'damage')
                                        monster_health -= spell_damage
                                    else:
                                        print('You got it wrong')
                                        print('Correct answer was',a+b)
                            elif spell_used == spells[1] or spell_used == '2':
                                print('Answer this question')
                                a = random.randint(1,100)
                                b = random.randint(1,100)
                                while b > a:
                                    b = random.randint(1,100)
                                print('What is',a,'-',b,'?')
                                answ = input()
                                try:
                                    answ = int(answ)
                                except:
                                    error(1)
                                    print('Because we cant kick you to the command menu, we will restart the program')
                                    reload()
                                else:
                                    if answ == a - b:
                                        print('You got it correct')
                                        spell_damage = blhealth /10 * (random.randint(20,50)/10)
                                        print('You did',spell_damage,'damage')
                                        monster_health -= spell_damage
                                        
                                    else:
                                        print('You got it wrong')
                                        print('Correct answer was',a-b)
                            elif spell_used == spells[2] or spell_used == '3':
                                print('Answer this question')
                                a = random.randint(1,12)
                                b = random.randint(1,12)
                                print('What is',a,'*',b,'?')
                                answ = input()
                                try:
                                    answ = int(answ)
                                except:
                                    error(1)
                                    print('Because we cant kick you to the command menu, we will restart the program')
                                    reload()
                                else:
                                    if answ == a * b:
                                        print('You got it correct')
                                        spell_damage = blhealth /10 * (random.randint(50,100)/10)
                                        print('You did',spell_damage,'damage')
                                        monster_health -= spell_damage
                                    else:
                                        print('You got it wrong')
                                        print('Correct answer was',a*b)
                            xp += spell_damage
                            print(monsterbattle_name,'has',monster_health,'health')
                            if monster_health < 1:
                                break
                            print('It is now',monsterbattle_name,'turn')
                            mspell_used = random.choice(monster_spells)
                            print(monsterbattle_name,'used',mspell_used)
                            if mspell_used == monster_spells[0]:
                                mspell_damage = blmh /10 * (random.randint(10,20)/10)
                            elif mspell_used == monster_spells[1]:
                                mspell_damage = blmh /10 * (random.randint(20,50)/10)
                            elif mspell_used == monster_spells[2]:
                                mspell_damage = blmh /10 * (random.randint(50,100)/10)
                            print(monsterbattle_name,'did',mspell_damage,'against you')
                            health -= mspell_damage
                            print('You now have',health,'health')
                    print('Game Over')
                    if health < 1:
                        print('You lost')
                        monsters_lost = monsters_lost + 1
                    elif monster_health < 1:
                        print('You won!')
                        monsters_won += 1
                    monsters_battled += 1
                    print('You gained',xp-blxp,'XP This round for a total of',xp)
                    print('You have won against',monsters_won,'This session')
                    print('You lost against',monsters_lost,'This session')
                    print('For a total of',monsters_battled)
                    print('You have a winning rate of',(str(monsters_won/monsters_battled*100)+' %'))
                    health = blhealth + (random.randint(blmh//8,blmh//5))
                    print('You gained',health-blhealth,'health This round for a total of',health)
                    print('')
                    print('Writing Statistics...',end='\r')
                    APPDATA["gamexp"] = xp
                    APPDATA["gamehealth"] = health
                    updateappdata()
                    print('Writing Statistics...done')
                    print('')
                elif battle == 'n':
                    break
        elif command == 'degp':
            print('How many degrees?')
            der = input()
            try:
                deg = int(der)
            except:
                error(1)
            else:
                deg = deg / 360
                deg = deg * 100
                print(der,'degrees is',deg,'percent.')
        elif command == 'pdeg':
            print('How many percent?')
            der = input()
            try:
                deg = int(der)
            except:
                error(1)
            else:
                deg = deg * 360
                deg = deg / 100
                print(der,'percent is',deg,'degrees.')
        elif command == 'tempt':
            print('Celsius (c), Farenheight (f), or Kelvin (k)')
            tcmd = input()
            if tcmd == 'c' or tcmd == 'f' or tcmd == 'k':
                print('What to convert to? (c,f,k)')
                ccmd = input()
                if ccmd == 'c' or ccmd == 'f' or ccmd == 'k':
                    cmd = tcmd + ccmd
                    print('Value to convert?')
                    vtc = input()
                    try:
                        vtc = float(vtc)
                    except:
                        error(1)
                    else:
                        if cmd == 'cf':
                            res = (vtc*9/5)+32
                            print('Converted is',res)
                        elif cmd == 'fc':
                            res = (vtc-32)*5/9
                            print('Converted is',res)
                        elif cmd == 'ck':
                            res = vtc - 273
                            print('Converted is',res)
                        elif cmd == 'kc':
                            res = vtc + 273
                            print('Converted is',res)
                        else:
                            print("Invalid command")
                else:
                    print("Invalid command")        

        elif command == 'cpicker':
            colours = ['red','orange','yellow','lime','green','turquois','blue','navy','purple','magenta','pink','brown','black','white']
            print('The chosen colour is',random.choice(colours))
        elif command == 'picker':
            pickable = []
            xmxa = False
            while True:
                print('Do you want to add an item? (y/n)')
                makenew = input()
                if makenew.lower().startswith('y'):
                    print('What to add?')
                    poi = input()
                    pickable.append(poi)
                    xmxa = True
                elif makenew == 'n' and xmxa == True:
                    selection = random.choice(pickable)
                    print('Your selection is',selection)
                    break
                else:
                    print('Please make sure that there is more than 0 items on the list and that you typed in a valid command.')
            
        elif command == 'progcount':
            newwindow()
            print('')
            
            if crashed == False:
                while True:
                    x = datetime.datetime.now()
                    a = x.year
                    b = x.month
                    c = x.day
                    d = x.hour
                    e = x.minute
                    f = x.second
                    f2 = x.microsecond
                    d1 = datetime.datetime(a,b,c,d,e,f,f2)
                    d0 = datetime.datetime(2021,4,12,16,0,0,000000)
                    difference = d1 - d0
                    total_seconds = difference.total_seconds()*1000
                    total_seconds = total_seconds/1000
                    total_min = total_seconds / 60
                    total_hr = total_min / 60
                    total_dy = total_hr / 24
                    total_wk = total_dy /7
                    total_yr = total_dy / 365.25
                    total_mt = total_yr * 12
                    print("")
                    print("There are",total_seconds,"seconds since",flush=True)
                    print("There are",total_min,"minutes since",flush=True)
                    print("There are",total_hr,"hours since",flush=True)
                    print("There are",total_dy,"days since",flush=True)
                    print("There are",total_wk,"weeks since",flush=True)
                    print("There are",total_mt,"month since",flush=True)
                    print("There are",total_yr,"years since life was normal.",flush=True)
                    print("\033[F\033[F\033[F\033[F\033[F\033[F\033[F\033[F",end="")
                    
                    sleep(0.1)
                    print(" "*50)
                    print(" "*50)
                    print(" "*50)
                    print(" "*50)
                    print(" "*50)
                    print(" "*50)
                    print(" "*50)
                    print(" "*50)
                    print("\033[F\033[F\033[F\033[F\033[F\033[F\033[F\033[F",end="")
            
        elif command == 'crash':
            raise RuntimeError('Manual Crash')
            
        elif command == 'settings' or command == "options" or command == "config" or command == "cfg":
            def apsave():
                global nf
                global val_inside
                global val_inside_2
                global val_inside_3
                global val_inside_4
                global APPDATA
                if val_inside.get() == "No notifications (default)":
                    APPDATA["showCommandsRun"] = False
                else:
                    APPDATA["showCommandsRun"] = True
                if val_inside_2.get() == "No sound effects":
                    APPDATA["useDownloadedSounds"] = False
                else:
                    APPDATA["useDownloadedSounds"] = True
                if val_inside_3.get() == "No coloured text":
                    APPDATA["useColouredText"] = False
                else:
                    APPDATA["useColouredText"] = True
                if val_inside_4.get() == "Legacy startups":
                    APPDATA["legacyStartups"] = True
                else:
                    APPDATA["legacyStartups"] = False
                updateappdata()
                nf.destroy()
            
            nf = Tk()
            nf.title('Settings')
            lbl = Label(nf,text='Select your notification settings')
            lbl.grid(column=0,row=0)
            lbl = Label(nf,text='Select your Sounds setting')
            lbl.grid(column=0,row=1)
            lbl = Label(nf,text="Select your coloured text setting")
            lbl.grid(column=0,row=2)
            lbl = Label(nf,text="Select your startup setting")
            lbl.grid(column=0,row=3)
            
            options_list = ["No notifications (default)","Show how many commands you've run"]
            options_list_2 = ["No sound effects","Use sound effects (default)"]
            options_list_3 = ["No coloured text","Use coloured text (default)"]
            options_list_4 = ["Detailed startups (default)","Legacy startups"]
            val_inside = StringVar(nf)
            val_inside_2 = StringVar(nf)
            val_inside_3 = StringVar(nf)
            val_inside_4 = StringVar(nf)
            if APPDATA["showCommandsRun"]:
                val_inside.set("Show how many commands you've run")
            else:
                val_inside.set("No notifications (default)")
            if APPDATA["useDownloadedSounds"]:
                val_inside_2.set("Use sound effects (default)")
            else:
                val_inside_2.set("No sound effects")
            if APPDATA["useColouredText"]:
                val_inside_3.set("Use coloured text (default)")
            else:
                val_inside_3.set("No coloured text")
            if APPDATA["legacyStartups"]:
                val_inside_4.set("Legacy startups")
            else:
                val_inside_4.set("Detailed startups (default)")
            #A sound effect is like the beat the bank sound effect.
            qmen = OptionMenu(nf,val_inside,*options_list)
            qmen.grid(column=1,row=0)
            qmen_2 = OptionMenu(nf,val_inside_2,*options_list_2)
            qmen_2.grid(column=1,row=1)
            qmen_3 = OptionMenu(nf,val_inside_3,*options_list_3)
            qmen_3.grid(column=1,row=2)
            qmen_4 = OptionMenu(nf,val_inside_4,*options_list_4)
            qmen_4.grid(column=1,row=3)
            
            btn = Button(nf,text="Done",bg="lime green",command=apsave)
            btn.grid(column=0,row=4)
            nf.mainloop()

        elif command == "settings.cli" or command == "options.cli" or command == "config.cli" or command == "cfg.cli":
            print("Please type in the key name")
            jsonpath = input()
            if jsonpath in APPDATA:
                print("Answer _d to delete or _r to keep existing value. Have _i before a space it to set as integer,have _b0 or _b1 to set as boolean")
                print(f"CURRENT VALUE: {APPDATA[jsonpath]}")
                nv = input(f"New value for {jsonpath}:")
                if nv == "_d":
                    del APPDATA[jsonpath]
                elif nv == "_r":
                    pass
                elif "_i" in nv:
                    try:
                        nv = int(nv.split(" ")[0])
                    except:
                        print("Error")
                        pass
                    else:
                        APPDATA[jsonpath] = nv
                elif "_b0" in nv:
                    APPDATA[jsonpath] = False
                elif "_b1" in nv:
                    APPDATA[jsonpath] = True
                else:
                    APPDATA[jsonpath] = nv
                print("Set value to",APPDATA[jsonpath])
            
        elif command == 'encode':
            print("Please select the file to encode.")
            Tk().withdraw()
            um = filedialog.askopenfilename()
            try:
                f = open(um)
                um = f.read()
                f.close()
            except:
                Tk().withdraw()
                messagebox.showerror(':(','Access denied')
                um = 'Access Denied'
            print('Unencoded Message:',um) 
            print("Message has a size of",len(um),"bytes")
            string = um.lower()
            enc = string.replace('a','NJ').replace('b','MPE').replace('c','CEXC').replace('d','QUIE').replace('e','*U&P/HTPS')\
            .replace('f','XML').replace('g','MDD').replace('h','BU#').replace('i','NNQP').replace('j','DYE').replace('k','AVOO').replace('l','AXZ')\
            .replace('m','LOL').replace('n','/-/').replace('o','NYX').replace('p','VAN').replace('q','FKUWEUI').replace('r','QYIF')\
            .replace('s','GHQ[W]').replace('t','CUED').replace('u','MOM').replace('v','OTW').replace('w','BITLY').replace('x','ENDER')\
            .replace('y','EXE').replace('z','GLHAC.P').replace('0','NULL').replace('1','0').replace('2','1').replace('3','2')\
            .replace('4','3').replace('5','4').replace('6','5').replace('7','6').replace('8','7').replace('9','8').replace(' ','PWSAC')

            print(enc,"is your encoded script")
            print("Size:",len(enc),"bytes")
            print("Do you want to write this to a file?(y/n)")
            sda = input()
            if sda.lower().startswith('y'):
                print('What directory to write to?')
                Tk().withdraw()
                fexx = filedialog.askdirectory()
                if fexx == '()':
                    print('')
                else:
                    print("What file name do you want it to be written to? No extension needed.")
                    fex = input()
                    fex = fex + '.bue'
                    fex = fexx + sysslash +fex
                    try:
                        f = open(fex,'x')
                        f.write(enc)
                        f.close()
                        print("written to",fex)
                    except:
                        try:
                            f = open(fex,'w')
                            f.write(enc)
                            f.close()
                            print("written to",fex)
                        except:
                            Tk().withdraw()
                            messagebox.showerror(':(','Access Denied')
                
        elif command == 'translate':
            print("Please select file to translate.")
            Tk().withdraw()
            file_path = filedialog.askopenfilename()
            
            try:
                f = open(file_path,'r')
                mes = f.read()
                print("encoded message is",len(mes),"bytes")
            except:
                error(1)
            else:
                tra = mes.replace('GLHAC.P','z').replace('EXE','y').replace('ENDER','x').replace('BITLY','w').replace('OTW','v')\
                .replace('MOM','u').replace('CUED','t').replace('GHQ[W]','s').replace('QYIF','r').replace('FKUWEUI','q').replace('VAN','p')\
                .replace('NYX','o').replace('/-/','n').replace('LOL','m').replace('AXZ','l').replace('AVOO','k').replace('DYE','j')\
                .replace('NNQP','i').replace('BU#','h').replace('MDD','g').replace('XML','f').replace('*U&P/HTPS','e').replace('QUIE','d')\
                .replace('CEXC','c').replace('MPE','b').replace('NJ','a').replace('8','9').replace('7','8').replace('6','7').replace('5','6')\
                .replace('4','5').replace('3','4').replace('2','3').replace('1','2').replace('0','1').replace('NULL','0').replace('PWSAC',' ')
                print(tra,'is the translation')
                print('size:',len(tra),'bytes')
                print("Do you want to write this to a txt file?(y/n)")
                wt = input()
                if wt.lower().startswith('y'):
                    print('What directory to write to?')
                Tk().withdraw()
                fexx = filedialog.askdirectory()
                if fexx == '()':
                    print('')
                else:
                    print("What file name do you want it to be written to? No extension needed.")
                    fex = input()
                    fex = fex + '.txt'
                    fex = fexx + sysslash +fex
                    try:
                        f = open(fex,'x')
                        f.write(enc)
                        f.close()
                        print("written to",fex)
                    except:
                        try:
                            f = open(fex,'w')
                            f.write(enc)
                            f.close()
                            print("written to",fex)
                        except:
                            Tk().withdraw()
                            messagebox.showerror(':(','Access Denied')
        elif command == 'bday':
            print('What month is your birthday on?')
            mt = input()
            try:
                mt = int(mt)
            except:
                error(1)
            else:
                print("What day?")
                dy = input()
                try:
                    dy = int(dy)
                except:
                    error(1)
                else:
                    APPDATA["bday"]["month"] = mt
                    APPDATA["bday"]["day"] = dy
                    updateappdata()
            
        elif command == 'colour' or command == 'color':
            try:
                s = turtle.getscreen()
                t = turtle.Turtle()
            except:
                s = turtle.getscreen()
                t = turtle.Turtle()
            def colourchange():
                global txt
                global txt1
                global txt2
                res = txt.get()
                res1 = txt1.get()
                res2 = txt2.get()
                efyi = True
                while efyi == True:
                    try:
                        a = int(res)
                    except:
                        error(1)
                        break
                    
                    try:
                        b = int(res1)
                    except:
                        error(1)
                        break
                    try:
                        c = int(res2)
                    except:
                        error(1)
                        break       
                    wx = turtle.Screen()
                    wx.colormode(255)
                    try:
                        turtle.Screen().bgcolor(a,b,c)
                    except:
                        error(0)
                        error(5)
                    finally:
                        break
            def bby():
                ct.destroy()
                try:
                    turtle.bye()
                except:
                    error(0)
            ct = Tk()
            ct.title('Window')
            txt = Entry(ct,width=10,bg='red')
            txt.grid(column=0,row=0)
            txt1 = Entry(ct,width=10,bg='green')
            txt1.grid(column=1,row=0)
            txt2 = Entry(ct,width=10,bg='blue')
            txt2.grid(column=2,row=0,)
            btn = Button(ct,text='Generate colour',command=colourchange,bg='green')
            btn.grid(column=1,row=1)
            lbl = Label(ct,text='Please enter values between 0 and 255')
            lbl.grid(column=1,row=2)
            btn1 = Button(ct,text='Exit',command=bby,bg='red')
            btn1.grid(column=0,row=1)
            ct.mainloop()
            
        elif command == 'clean your room':
            Tk().withdraw()
            messagebox.showerror('Error','Computers cannot clean their rooms')
        elif command == 'ur mom':
            class ImmatureError(Exception):
                pass
            raise ImmatureError("You are extremely immature.")

        elif command == 'clean your room.cli':
            print("Error: Computers cannot clean their rooms.")
        elif command == 'cpg':
            print("To return to the command menu, make sure all other Tk windows are closed.")
            def rot():
                try:
                    t.right(90)
                except:
                    error(7)

            def bb():
                ct.destroy()
                try:
                    turtle.bye()
                except:
                    error(0)
            def go():
                global txt
                global abh
                res = txt.get()
                try:
                    res = int(res)
                except:
                    error(1)
                else:
                    try:
                        t.forward(res)
                    except:
                        error(7)
                    else:
                        ps = t.pos()
                        print("You are at",ps)
                        print("You need to go to",abh)
                        ps = str(ps)
                        abh = str(abh)
                        if ps == abh:
                            bb()
                            print("Yay! You did it!")

            def undo():
                t.undo()


            try:
                s = turtle.getscreen()
                t = turtle.Turtle()
            except:
                s = turtle.getscreen()
                t = turtle.Turtle()
            a = random.randint(-200,200)
            b = random.randint(-200,200)
            t.penup()
            t.goto(a,b)

            t.stamp()
            abh = t.pos()
            print("Go to",abh)
            amx = random.randint(-200,200)
            amd = random.randint(-200,200)
            t.goto(amd,amx)
            t.pendown()
            t.pencolor('blue')
            ct = Tk()
            ct.title('Control Panel')
            btn = Button(ct,text='rotate 1/4 turn CW',command=rot)
            btn.grid(column=0,row=0)
            btn2 = Button(ct,text='Exit',command=bb,bg='red')
            btn2.grid(column=1,row=0)
            txt = Entry(ct,width=10)
            txt.grid(column=0,row=1)
            btn3 = Button(ct,text='Go',command=go,bg='green')
            btn3.grid(column=1,row=1)
            btn4 = Button(ct,text='Undo',command=undo,bg='yellow')
            btn4.grid(column=0,row=2)
            ct.mainloop()

        elif command == 'clr':
            
            APPDATA["besttime"] = 0
            APPDATA["bcount"] = 0
            APPDATA["btime"]["year"] = None
            APPDATA["btime"]["month"] = None
            APPDATA["btime"]["day"] = None
            APPDATA["btime"]["hour"] = None
            APPDATA["btime"]["minute"] = None
            APPDATA["btime"]["second"] = None
            APPDATA["bday"]["month"] = None
            APPDATA["bday"]["day"] = None
            APPDATA["webhistory"].clear()
            APPDATA["username"] = "DefaultUser"
            APPDATA["showCommandsRun"] = False
            APPDATA["gamehealth"] = None
            APPDATA["gamexp"] = None
            APPDATA["startsound"] = None
            APPDATA["useDownloadedSounds"] = True
            APPDATA["useColouredText"] = True
            APPDATA["legacyStartups"] = False
            APPDATA["commandsRun"] = 0
            shutil.rmtree(".temp")
            try:
                shutil.rmtree("crash_reports") 
            except:
                pass
            try:
                os.remove("lag.csv")
            except:
                pass
            shutil.rmtree("assets")
            updateappdata()
            if consoleask("Would you like to reload now? (Failing to do so may have some unintended consequences)"):
                reload()
        elif command == 'uninstall':
            
            
            try:
                os.startfile('unins000.exe')
                
            except:
                error(2)
                print('Main uninstaller failed to start.')
            else:
                os.system('taskkill /F /IM BasicUtilities.exe')

        elif command == 'wb':
            webbrowser.open('https://bit.ly/enderexe')

        elif command == 'anim':
            for i in range(10):
                print('|',end='\r')
                sleep(0.1)
                print('/',end='\r')
                sleep(0.1)
                print('-',end='\r')
                sleep(0.1)
                print('\ ',end='\r')
                sleep(0.1)
                print('|',end='\r')
                sleep(0.1)
                print("/ ",end='\r')
                sleep(0.1)
                print('-',end='\r')
                sleep(0.1)
                print('\ ',end='\r')
                sleep(0.1)

        elif command == 'conv':
            print("-----Subcommands for Convert-----")
            print("conv len: convert length of things")
            print("conv cmd: Converter command menu")

        elif command == 'conv len':
            print("-----Subcommands for Convert Length-----")
            print("conv len m-f: Metres to Feet")
            print("conv len f-m: Feet to metres")
            print("conv len i-c: Inches to centimeters")
            print("conv len c-i: centimetres to inches")
            print("conv len i-y: inches to yards")
            print("conv len m-y: meters to yards")
            print("conv len c-y: centimeters to yards")
            print("conv len y-i: yards to inches")
            print("conv len y-m: yards to meters")
            print("conv len y-c: yards to centimeters")
            

        elif command == 'conv len i-y':
            conv('inches','yards',"/48")
        elif command == 'conv cmd':
            xay = True
            while xay == True:
                print('-----Converter Command Menu-----')
                print('Type your command under here and press enter')
                mxe = input()
                if mxe == 'help' or mxe =='?':
                    print('-----Commands List for Conv-----')
                    print('help: Shows this list')
                    print('cmd: Go to the command menu')
                    print('km-mi: kilometres to miles')
                    print('mi-km: miles to kilometres')
                    print('kg-lb: Kilograms to pounds')
                    print('lb-kg: pounds to kilograms')

                elif mxe == 'lb-kg':
                    conv('pounds','kilograms','/2.20463')
                    
                
                elif mxe == 'kg-lb':
                    conv('kilograms','pounds','*2.20463')

                elif mxe == 'cmd':
                    break
                elif mxe == 'km-mi':
                    conv('kilometres','miles','/1.609')
                elif mxe == 'mi-km':
                    conv('miles','kilometres','*1.609')
                else:
                    print('You typed in an unrecognized command. \n\
                        Type "help" or "?" for the commands list.')
                cmd_run = cmd_run + 1
                xlm = APPDATA["showCommandsRun"]
                xmls = str(cmd_run)
                if not xlm:
                    pass
                elif xlm:
                    print('')
                    print('You have run',cmd_run,'commands this session')
                
                else:
                    log("Invalid notifs settings",WARN)
                    APPDATA["showCommandsRun"] = True
                    updateappdata()
                    xls = 'You have run this many commands this session: ' + xmls + ". If you don't want to see how many commands you have run, change it with the notifs command."
                    print('')
                    print(xls)

        elif command == 'conv len c-y':
            conv('centimeters','yards','*0.010936')
        elif command == 'conv len y-c':
            conv('yards','centimeters','*91.44')

        elif command == 'conv len y-m':
            conv('yards','meters','*1.093613')

        elif command == 'conv len m-y:':
            conv('meters','yards','/1.093613')

        elif command == 'conv len y-i':
            conv('inches','yards',"*48")

        elif command == 'conv len c-i':
            #/2.54
            conv('centimeters','inches',"/2.54")

        elif command == 'conv len i-c':
            conv('inches','centimeter','*2.54')

        elif command == 'conv len m-f':
            #* 3.28084
            conv('metres','feet','*3.28084')

        elif command == 'conv len f-m':
            conv('feet','meters','/3.28084')

        elif command == "timer":
            newwindow()
            print("How many seconds?")
            sc_tm = input()

            paused = False
            def tmmain():
                global sc_tm
                global paused
                while sc_tm > 0 and paused == False:
                    try:
                        lbl.configure(text=sc_tm)
                    except:
                        break
                    sc_tm = sc_tm - 1
                    sleep(1)
                if sc_tm < 1:
                    tmdone()

            def tmdone():
                global btn23
                global btn22
                global btn25
                btn23['state'] = 'disabled'
                btn22['state'] = 'disabled'
                btn25['state'] = 'normal'
                global btn24
                btn24['state'] = 'normal'
                try:
                    lbl.configure(text='Timer is Done')
                except:
                    error(0)
                print("Your timer is done")
                if APPDATA["useDownloadedSounds"]:
                    try:
                        playsound(ASSETS+"/warning.mp3")
                    except:
                        error(2)
                else:
                    try:
                        winsound.Beep(1000,1000)
                    except:
                        error(2)

            def tmstart():
                global paused
                th = threading.Thread(target=tmmain)
                paused = False
                global btn22
                global btn25
                btn22['state'] = 'disabled'
                btn25['state'] = 'disabled'
                global btn24
                btn24['state'] = 'disabled'
                th.start()

            def tmkill():
                global tm
                global paused
                paused = True
                tm.quit()
                tm.destroy()

            def tmstop():
                global paused
                paused = True
                btn22['state'] = 'normal'
                btn25['state'] = 'normal'
                global btn24
                btn24['state'] = 'normal'

            def tmreset():
                global paused
                global sc_tm
                sc_tm = tm_full
                btn22['state'] = 'normal'
                btn23['state'] = 'normal'

                lbl.configure(text='Waiting for Start')
                paused = False
            try:
                sc_tm = int(sc_tm)
            except:
                error(1)
            else:
                tm_full = sc_tm
                tm = Tk()
                tm.title('Timer')
                tm.geometry("400x100")
                lbl = Label(tm,text='Waiting for start')
                lbl.grid(column=0,row=0)
                btn22 = Button(tm,text='Start',command=tmstart,bg="green")
                btn22.grid(column=0,row=1)
                btn23 = Button(tm,text="Pause",command=tmstop,bg="yellow")
                btn23.grid(column=1,row=1)
                btn24 = Button(tm,text="Stop",command=tmkill,bg='red')
                btn24.grid(column=2,row=1)
                btn25 = Button(tm,text='Reset',command=tmreset,bg='blue')
                btn25.grid(column=3,row=1)
                tm.mainloop()


        elif command == 'draw':
            newwindow()
            print("Please turn your attention to the Tkinter windows. If there are errors, they will be in the console.")
            window = Tk()
            window.title('LetsDraw')
            window.geometry('800x500')
            try:
                s = turtle.getscreen()
                t = turtle.Turtle()
            except:
                s = turtle.getscreen()
                t = turtle.Turtle()
            turtle.title("Let's Draw Canvas")
            def go_forward():
                global txt
                res = txt.get()
                try:
                    res = float(res)
                except ValueError:
                    error(1)
                else:
                    try:
                        t.forward(res)
                    except:
                        error(0)

            def go_backward():
                global txt1
                res = txt1.get()
                try:
                    res = float(res)
                except:
                    error(1)
                else:
                    try:
                        t.backward(res)
                    except:
                        error(0)

            def turn_left():
                global txt2
                res = txt2.get()
                try:
                    res = float(res)
                except:
                    error(1)
                else:
                    try:
                        t.left(res)
                    except:
                        error(0)
            def turn_right():
                global txt3
                res = txt3.get()
                try:
                    res = float(res)
                except:
                    error(1)
                else:
                    try:
                        t.right(res)
                    except:
                        error(0)

            def changecolor():
                global txt4
                res = txt4.get()
                try:
                    t.pencolor(res)
                except:
                    error(1)

            def changefill():
                global txt5
                res = txt5.get()
                try:
                    t.fillcolor(res)
                except:
                    error(1)

            def go_to():
                global txt6
                global txt7
                res = txt6.get()
                res1 = txt7.get()
                try:
                    res = int(res)
                    res1 = int(res1)
                except:
                    error(1)
                else:
                    try:
                        t.goto(res,res1)
                    except:
                        error(0)

            def pensize():
                global txt8
                res = txt8.get()
                try:
                    res = int(res)
                except:
                    error(1)
                else:
                    try:
                        t.pensize(res)
                    except:
                        error(0)

            def dot():
                global txt9
                res = txt9.get()
                try:
                    res = int(res)
                except:
                    error(1)
                else:
                    try:
                        t.dot(res)
                    except:
                        error(0)

            def dsave():
                global txt10
                res = txt10.get()
                res1 = ".eps"
                res = res + res1
                s.getcanvas().postscript(file=res)
            def dconv2():
                webbrowser.open("https://epsviewer.org/onlineviewer.aspx")
            def circ():
                global txt11
                res = txt11.get()
                try:
                    res = int(res)
                except:
                    error(1)
                else:
                    try:
                        t.circle(res)
                    except:
                        error(0)
            def square():
                global txt12
                res = txt12.get()
                try:
                    res = float(res)
                except:
                    error(1)
                else:
                    for i in range(4):
                        try:
                            t.forward(res)
                            t.right(90)
                        except:
                            error(0)

            def byebye():
                global tcrash
                window.quit()
                window.destroy()
                turtle.bye()
                tcrash = True
            turtle.hideturtle()
            BACKGROUND = "#ffffff"

            lbl = Label(window,text='Lets Draw',font=("Arial Bold",12))
            lbl.grid(column=0,row=0)
            btn = Button(window,text='Exit',command=byebye,bg="red")
            btn.grid(column=1,row=0)

            txt = Entry(window,width=10)
            txt.grid(column=0,row=1)
            btn1 = Button(window,text='Go',command=go_forward,bg="green")
            btn1.grid(column=1,row=1)
            lbl1 = Label(window,text='Go forward this many units')
            lbl1.grid(column=2,row=1)

            txt1 = Entry(window,width=10)
            txt1.grid(column=0,row=2)
            btn2 = Button(window,text='Go',command=go_backward,bg="green")
            btn2.grid(column=1,row=2)
            lbl2 = Label(window,text='Go backward this many units')
            lbl2.grid(column=2,row=2)


            txt2 = Entry(window,width=10)
            txt2.grid(column=0,row=3)
            btn3 = Button(window,text='Go',command=turn_left,bg="green")
            btn3.grid(column=1,row=3)
            lbl3 = Label(window,text='Turn left this many degrees')
            lbl3.grid(column=2,row=3)

            txt3 = Entry(window,width=10)
            txt3.grid(column=0,row=4)
            btn4 = Button(window,text='Go',command=turn_right,bg="green")
            btn4.grid(column=1,row=4)
            lbl4 = Label(window,text='Turn right this many degrees')
            lbl4.grid(column=2,row=4)
            btn5 = Button(window,text='pen up',command=t.penup)
            btn5.grid(column=0,row=5)
            btn6 = Button(window,text='pen down',command=t.pendown)
            btn6.grid(column=1,row=5)
            btn7 = Button(window,text='undo',command=t.undo,bg="yellow")
            btn7.grid(column=2,row=5)
            btn8 = Button(window,text='clear canvas',command=t.clear,bg="orange")
            btn8.grid(column=3,row=5)
            btn9 = Button(window,text='Start fill',command=t.begin_fill)
            btn9.grid(column=0,row=6)
            btn10 = Button(window,text='End fill',command=t.end_fill)
            btn10.grid(column=1,row=6)
            lbl5 = Label(window,text='Press start fill, draw a closed shape, and press end fill to fill.')
            lbl5.grid(column=2,row=6)
            txt4 = Entry(window,width=20)
            txt4.grid(column=0,row=7)
            btn11 = Button(window,text='go',command=changecolor,bg="green")
            btn11.grid(column=1,row=7)
            lbl6 = Label(window,text='Change the pen colour (use a valid hex code starting with #)')
            lbl6.grid(column=2,row=7)
            txt5 = Entry(window,width=20)
            txt5.grid(column=0,row=8)
            btn12 = Button(window,text='go',command=changefill,bg="green")
            btn12.grid(column=1,row=8)
            lbl7 = Label(window,text='Change the fill colour (use a valid hex code starting with #)')
            lbl7.grid(column=2,row=8)

            txt6 = Entry(window,width=10)
            txt6.grid(column=0,row=9)
            txt7 = Entry(window,width=10)
            txt7.grid(column=1,row=9)

            btn13 = Button(window,text='go',command=go_to,bg="green")
            btn13.grid(column=2,row=9)
            lbl8 = Label(window,text='Change draw to this location (x y)')
            lbl8.grid(column=3,row=9)

            txt8 = Entry(window,width=10)
            txt8.grid(column=0,row=10)
            btn14 = Button(window,text='go',command=pensize,bg="green")
            btn14.grid(column=1,row=10)
            lbl9 = Label(window,text='Change the pen size')
            lbl9.grid(column=2,row=10)

            txt9 = Entry(window,width=10)
            txt9.grid(column=0,row=11)
            btn15 = Button(window,text='go',command=dot,bg="green")
            btn15.grid(column=1,row=11)
            lbl10= Label(window,text='Draw a dot of this size')
            lbl10.grid(column=2,row=11)

            txt10 = Entry(window,width=20)
            txt10.grid(column=0,row=12)
            btn16 = Button(window,text='Export',command=dsave,bg="blue")
            btn16.grid(column=1,row=12)
            lbl11 = Label(window,text='Export your drawing to .eps')
            lbl11.grid(column=2,row=12)
            btn18 = Button(window,text='Convert eps',command=dconv2)
            btn18.grid(column=3,row=12)
            txt11 = Entry(window,width=10)
            txt11.grid(column=0,row=13)
            btn19 = Button(window,text='Go',command=circ,bg="green")
            btn19.grid(column=1,row=13)
            lbl12 = Label(window,text='Draw a circle of this radius')
            lbl12.grid(column=2,row=13)

            txt12 = Entry(window,width=10)
            txt12.grid(column=0,row=14)
            btn20 = Button(window,text='Go',command=square,bg="green")
            btn20.grid(column=1,row=14)
            lbl13 = Label(window,text='Draw a square with a side length of this.')
            lbl13.grid(column=2,row=14)
            def tsave():
                print("saving...")
                
                global BACKGROUND
                
                t.hideturtle()
                try:
                    
                    e = []
                    print("Assembling list...")
                    for x in range(-1000,1000):
                        for y in range(-1000,1000):
                            e.append((x,y))
                    files = [('Turtle file','*.trt')]
                    print("Please select save file")    
                    g = filedialog.asksaveasfile(filetypes=files,defaultextension=files)
                    bar = ProgressBar(total=4000000,spinner_type="s",bar_length=100,prefix="Writing")
                    with open(g.name,"w+") as f:
                        f.write("b "+BACKGROUND+"\n")
                        for coord in e:
                            l = get_pixel_color(coord[0],coord[1])
                            if l != BACKGROUND:
                                f.write("p "+str(coord[0])+" "+str(coord[1])+" "+l+"\n")
                            bar.iter()
                    del e
                    bar.stop()
                    print("\n")
                    print("Finished")
                except Exception as ex:
                    toplevelerror("Failed to save "+str(ex))
                finally:
                    t.showturtle()
            def sbk():
                global BACKGROUND
                global ent
                e = ent.get()
                try:
                    turtle.Screen().bgcolor(e)
                except:
                    pass
                else:
                    BACKGROUND = e
            btn21 = Button(window,text="Save",bg="lime green",command=tsave)
            lbl13 = Label(window,text="Save drawing as a later-editable .trt file")
            lbl13.grid(column=0,row=15)
            btn21.grid(column=1,row=15)
            ent = Entry(window,width=20)
            ent.grid(column=0,row=16)
            lbl14 = Label(window,text="Set the background (must be a valid hex code starting with #)")
            lbl14.grid(column=2,row=16)
            btn22 = Button(window,text="Go",bg="green",command=sbk)
            btn22.grid(column=1,row=16)
            ent1 = Entry(window,width=30)
            ent2 = Entry(window,width=10)
            ent3 = Entry(window,width=10)
            lbl15 = Label(window,text="Insert text")
            lbl16 = Label(window,text="at xy")
            def wtx():
                x = t.pos()
                global ent1
                global ent2
                global ent3
                try:
                    t.penup()
                    t.goto(int(ent2.get()),int(ent3.get()))
                    t.pendown()
                    t.write(ent1.get())
                    t.penup()
                    t.goto(x[0],x[1])
                except Exception as ex:
                    toplevelerror("Failed to complete write: "+str(ex))
            btn23 = Button(window,text="Go",bg="green",command=wtx)
            lbl15.place(y=440,x=0)
            ent1.place(y=440,x=70)
            lbl16.place(x=250,y=440)
            ent2.place(x=280,y=440)
            ent3.place(x=350,y=440)
            btn23.place(x=400,y=440)
            window.mainloop()

        elif command == "erc":
            print("-----List of Error Codes-----")
            print("error 0: Internal Error. You should usually not see this. Any message that does not have an error code is 0.")
            print("error 1: Conversion Error. This is the most common error, and is usually triggered by you entering letters into a place where only numbers go.")
            print("error 2: File Not Found Error. This is usually found when you rename or delete one of this program's files.")
            print("error 3: Script Error. This happens during the pyterm and calc commands. It is when you have an error in your script.")
            print("error 4: File Corrupt Error. This has yet to happen. If you find something like this, please report the bug.")
            print("error 5: Out Of Range. This happens when you input '13' into a month counter.")
            print("error 6: Invalid URL. This is what happens if you put an invalid url.")
            print("error 7: Turtle error")

        elif command == "sw":

            newwindow()
            print("Please look at the Tkinter window")
            def swkill():
                global window
                window.quit()
                window.destroy()
                global paused
                paused = True
            def swmain():
                global tcount
                global window
                global lbl
                global paused
                global btn
                global btn3
                global btn2
                window = Tk()
                window.title("Stopwatch")
                window.geometry("400x100")
                lbl = Label(window,text="0")
                lbl.grid(column=0,row=0)
                btn = Button(window,text="Start",command=swstart,bg="green")
                btn.grid(column=0,row=1)
                btn1 = Button(window,text="Pause",command=swstop,bg="yellow")
                btn1.grid(column=1,row=1)
                btn2 = Button(window,text="Stop",command=swkill,bg="red")
                btn2.grid(column=2,row=1)
                btn3 = Button(window,text='Reset',command=swreset,bg='blue')
                btn3.grid(column=3,row=1)
                window.mainloop()
                
                paused = True

            def swstart():
                global btn3
                global btn
                global btn2
                btn['state'] = "disabled"
                btn3['state'] = "disabled"
                btn2['state'] = "disabled"
                th0 = threading.Thread(target=swcount)
                th0.start()


            def swcount():
                global lbl
                global paused
                global tcount
                paused = False
                while paused == False:
                    tcount = tcount + 0.1
                    sleep(0.08)
                    try:
                        lbl.configure(text=tcount)
                    except:
                        pass

            def swstop():
                global paused
                global btn
                global btn3
                btn['state'] = "normal"
                btn3['state'] = 'normal'
                btn2['state'] = "normal"
                paused = True

            def swreset():
                global paused
                global tcount
                pasued = False
                tcount = 0
                try:
                    lbl.configure(text=tcount)
                except:
                    error(0)



            tcount = 0
            paused = False
            swmain()

        elif command == "quiz":
            print("Welcome to Multiplication Quiz! Press enter to begin!")
            input()
            isdone = False
            correct = 0
            wrong = 0
            cr = False
            def timer():
                global isdone
                global ttime
                ttime = 0
                while isdone == False:
                    try:
                        sleep(1)
                        ttime = ttime + 1
                    except:
                        break
            th = threading.Thread(target=timer)
            th.start()

            while correct < 10:
                n1 = random.randint(1,12)
                n2 = random.randint(1,12)
                answ = n1 * n2
                print("What is",n1,"x",n2,"?")
                sansw = input()
                try:
                    sansw = int(sansw)
                except:
                    print("Please put only numbers here.")
                    cr = True
                    wrong = wrong + 1
                if cr == False:
                    if sansw == answ:
                        print("correct!")
                        correct = correct + 1
                    else:
                        print("wrong.")
                        wrong = wrong + 1
            if correct > 9:
                isdone = True
            print("You did it in",ttime,"seconds!")
            if besttime == 0 or ttime < besttime:
                print("You have a new best time!")
                APPDATA["besttime"] = ttime
                updateappdata()
            ot = correct + wrong
            print("You did",correct,"correct answers out of",ot)
            ote = correct / ot * 100
            print("Your score is",ote,"%")
        elif command == "calc help":
            print("-----Help With Calculator-----")
            print("This will help you with getting the correct operators")
            print("+: Addition, command usage: 1+1")
            print("-: Subtraction, command usage: 10-8")
            print("*: Multiplication, command usage: 10 * 5")
            print("/: Division, command usage: 10/2")
            print("%: Modulus, command usage: 10 % 3")
            print("**: Exponents, command usage: 10 ** 3")
            print("// Floor Division, command usage: 93 // 12")
            print("() Parentheses, used to execute some math first. Example: (12+6)/3")
            print("You can square-root with **(1/2). For example 9**(1/2) = 3")


        elif command == "calc":
            print("Please look at the tkinter window.")
            def calcu():
                global lbl1
                global txt
                global data
                res = txt.get()
                lbl1.delete(0,END)
                try:
                    data = eval(res)
                                
                    lbl1.insert(END,data)
                except Exception as e:
                    lbl1.insert(END,'error '+str(e))
                
            def ctt():
                global cal
                
                cal.clipboard_clear()
                cal.clipboard_append(str(data))
                cal.update()
            cal = Tk()
            cal.title('Calculator')
            lbl = Label(cal,text='Please input full equation and press calculate')
            lbl.grid(column=0,row=0)
            btn = Button(cal,text='Close',command=cal.destroy,bg='red')
            btn.grid(column=1,row=0)
            txt = Entry(cal,width=50)
            txt.grid(column=0,row=1)
            btn1 = Button(cal,text='Calculate',command=calcu,bg='lime green')
            btn1.grid(column=1,row=1)
            lbl1 = Entry(cal,width=50)
            lbl1.grid(column=0,row=2)
            lbl1.insert(END,"Don't put your equation here please.")
            btn2 = Button(cal,text="Copy",command=ctt,bg="yellow")
            btn2.grid(column=1,row=2)
            cal.mainloop()
            

        elif command == "lnmeter":
            newwindow()
            print('')
            
            if crashed == False:
                while True:
                    x = datetime.datetime.now()
                    a = x.year
                    b = x.month
                    c = x.day
                    d = x.hour
                    e = x.minute
                    f = x.second
                    f2 = x.microsecond
                    d1 = datetime.datetime(a,b,c,d,e,f,f2)
                    d0 = datetime.datetime(2020,3,13,15,30,0,000000)
                    difference = d1 - d0
                    total_seconds = difference.total_seconds()*1000
                    total_seconds = total_seconds/1000
                    total_min = total_seconds / 60
                    total_hr = total_min / 60
                    total_dy = total_hr / 24
                    total_wk = total_dy /7
                    total_yr = total_dy / 365.25
                    total_mt = total_yr * 12
                    print("")
                    print("There are",total_seconds,"seconds since",flush=True)
                    print("There are",total_min,"minutes since",flush=True)
                    print("There are",total_hr,"hours since",flush=True)
                    print("There are",total_dy,"days since",flush=True)
                    print("There are",total_wk,"weeks since",flush=True)
                    print("There are",total_mt,"month since",flush=True)
                    print("There are",total_yr,"years since life was normal.",flush=True)
                    print("\033[F\033[F\033[F\033[F\033[F\033[F\033[F\033[F",end="")
                    
                    sleep(0.1)
                    print(" "*50)
                    print(" "*50)
                    print(" "*50)
                    print(" "*50)
                    print(" "*50)
                    print(" "*50)
                    print(" "*50)
                    print(" "*50)
                    print("\033[F\033[F\033[F\033[F\033[F\033[F\033[F\033[F",end="")

        elif command == "pyterm":
            crashed = False
            
            print("")
            if crashed == False:
                print("Warning: This will give you access to most python commands. This could be dangerous. Make sure you know what you are doing!")
                print("type something in python and press enter. To return to the command menu, type 'breakout' and press enter")
                while True:
                    cmd = input("Python "+str(sys.version).split(" ")[0]+": ")
                    if cmd == "breakout":
                        break
                    if cmd.split(" ")[0] == "raise":
                        exec(cmd)
                    else:
                        try:
                            exec(cmd)
                        except Exception as e:
                            print("ERROR",e)

        elif command == "gpap":
            print("GPA?")
            gpa = input()
            try:
                gpa = float(gpa)
            except:
                error(1)
            else:
                gpa = gpa + 1
                gpa = gpa * 20
                print("Percent =",gpa)

        elif command == "pgpa":
            print("percent?")
            prce = input()
            try:
                prce = float(prce)
            except:
                error(1)
            else:
                gpa = prce / 20 - 1
                print("GPA =",gpa)

        elif command == "pa":
            pa = True
            while pa == True:
                print("Starting number?")
                sn = input()
                try:
                    sn = float(sn)
                except:
                    error(1)
                    break
                print("What percent do you want to add?")
                ap = input()
                try:
                    ap = float(ap)
                except:
                    error(1)
                    break
                ap = ap / 100
                ax = ap * sn
                print("You  are adding",ax)
                tyi = ax + sn
                print("For a total of",tyi)
                pa = False

        elif command == "pr":
            pr = True
            while pr == True:
                print("Starting number?")
                sn = input()
                try:
                    sn = float(sn)
                except:
                    error(1)
                    break
                print("What percent do you want to remove?")
                ap = input()
                try:
                    ap = float(ap)
                except:
                    error(1)
                    break
                ap = ap / 100
                ax = ap * sn
                print("You  are removing",ax)
                tyi = sn - ax
                print("For a total of",tyi)
                pr = False

        elif command == "randpass":
            lleters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            uleters = []
            for letter in lleters:
                uleters.append(letter.upper())
            nums = [0,1,2,3,4,5,6,7,8,9]
            sym = ["!","@","#","$","%","^","&","*","_","-","+","=",",","'","<",">","/","?","\\"]
            hexes = [1,2,3,4,5,6,7,8,9,0,"a","b","c","d","e","f"]
            bins = [0,1]
            def gennp():
                global lleters
                global uleters
                global nums
                global sym
                global ii
                global ii2
                global ii3
                global ii1
                global ent
                global ent2
                e = ent.get()
                try:
                    e = int(e)
                    if e < 1:
                        raise ValueError()
                except:
                    toplevelerror("Invalid input")
                else:
                    valpas = []
                    if ii.get() == 1:
                        valpas += lleters
                    if ii1.get() == 1:
                        valpas += uleters
                    if ii2.get() == 1:
                        valpas += nums
                    if ii3.get() == 1:
                        valpas += sym
                    passw = ""
                    if valpas:
                        for i in range(e):
                            passw += str(random.choice(valpas))
                        print(passw)
                        ent2["state"] = "normal"
                        ent2.delete(0,END)
                        ent2.insert(0,passw)
                    else:
                        toplevelerror("Please check at least one box")
            def gennb():
                global bins
                global ent
                global ent2
                e = ent.get()
                try:
                    e = int(e)
                    if e < 1:
                        raise ValueError()
                except:
                    toplevelerror("Invalid input")
                else:
                    passw = ""
                    for i in range(e):
                        passw += str(random.choice(bins))
                    print(passw)
                    ent2["state"] = "normal"
                    ent2.delete(0,END)
                    ent2.insert(0,passw)
            def gennx():
                global hexes
                global ent
                global ent2
                e = ent.get()
                try:
                    e = int(e)
                    if e < 1:
                        raise ValueError()
                except:
                    toplevelerror("Invalid input")
                else:
                    passw = ""
                    for i in range(e):
                        passw += str(random.choice(hexes))
                    print(passw)
                    ent2["state"] = "normal"
                    ent2.delete(0,END)
                    ent2.insert(0,passw)
            rpw = Tk()
            rpw.title("Random password")
            ent = Entry(rpw,width=10)
            ent.grid(column=0,row=0)
            lbl = Label(rpw,text="The length of the password")
            lbl.grid(column=1,row=0)
            btn = Button(rpw,text="Exit",command=lambda:tkkill(rpw))
            btn.grid(column=2,row=0)
            ii = IntVar(value=1)
            ii1 = IntVar(value=1)
            ii2 = IntVar(value=1)
            ii3 = IntVar(value=1)
            ci = Checkbutton(rpw,text="Allow lowercase letters",variable=ii)
            ci.grid(column=0,row=1)
            c2 = Checkbutton(rpw,text="Allow uppercase letters",variable=ii1)
            c2.grid(column=0,row=2)
            c3 = Checkbutton(rpw,text="Allow numbers",variable=ii2)
            c3.grid(column=0,row=3)
            c4 = Checkbutton(rpw,text="Allow symbols",variable=ii3)
            c4.grid(column=0,row=4)
            btn2 = Button(rpw,text="Generate Password",command=gennp)
            btn2.grid(column=1,row=1)
            btn3 = Button(rpw,text="Generate Binary Password",command=gennb)
            ent2 = Entry(rpw,width=50)
            ent2.grid(column=0,row=5)
            ent2["state"] = "disabled"
            btn3.grid(column=1,row=2)
            btn4 = Button(rpw,text="Copy to clipboard",command=lambda:clipboardadd(str(ent2.get())))
            btn4.grid(column=1,row=4)
            btn5 = Button(rpw,text="Generate Hex Password",command=gennx)
            btn5.grid(column=1,row=3)
            rpw.mainloop()

        elif command == "apv":
            print("-----Subcommands for Area, Perimeter, Volume-----")
            print("apv rec: area and perimeter of a rectangle or square.")
            print("apv cir: area and perimeter of circle")
            print("apv tri: area of triangle")
            print("apv recp: volume of rectangular prism")
            print("apv trip: volume of triangular prism")
            print("apv cyl: volume of cylinder")
            print("apv sph: volume of sphere")

        elif command == "apv rec":
            apvrec = True
            while apvrec == True:
                print("base of rectangle?")
                base = input()
                try:
                    base = float(base)
                except:
                    error(1)
                    break
                print("height of rectangle?")
                height = input()
                try:
                    height = float(height)
                except:
                    error(1)
                    break
                area = base * height
                perimeter = base * 2 + height * 2
                print("The area is",area)
                print("The perimeter is",perimeter)
                apvrec = False

        elif command == "apv cir":
            apvcir = True
            while apvcir == True:
                print("Radius of circle?")
                radius = input()
                try:
                    radius = float(radius)
                except:
                    error(1)
                    break
                diameter = radius * 2
                area = radius * radius * pi
                perimeter = diameter * pi
                print("Area is",area)
                print("Circumfrence is",perimeter)
                apvcir = False

        elif command == "apv tri":
            apvtri = True
            while apvtri == True:
                print("base of triangle?")
                base = input()
                try:
                    base = float(base)
                except:
                    error(1)
                    break
                print("height of triangle?")
                height = input()
                try:
                    height = float(height)
                except:
                    error(1)
                    break
                area = base * height / 2
                print("Area is",area)
                apvtri = False

        elif command == "apv recp":
            apvrecp = True
            while apvrecp == True:
                print("height?")
                height = input()
                try:
                    height = float(height)
                except:
                    error(1)
                    break
                print("width?")
                width = input()
                try:
                    width = float(width)
                except:
                    error(1)
                    break
                print("depth?")
                depth = input()
                try:
                    depth = float(depth)
                except:
                    error(1)
                    break
                volume = height * width

                volume = volume * depth
                print("Volume is",volume)
                apvrecp = False

        elif command == "apv trip":
            apvtrip = True
            while apvtrip == True:
                print("height?")
                height = input()
                try:
                    height = float(height)
                except:
                    error(1)
                    break
                print("width?")
                width = input()
                try:
                    width = float(width)
                except:
                    error(1)
                    break
                print("depth?")
                depth = input()
                try:
                    depth = float(depth)
                except:
                    error(1)
                    break
                volume = height * width

                volume = volume * depth
                volume = volume / 2
                print("Volume is",volume)
                apvtrip = False

        elif command == "apv cyl":
            apvcyl = True
            while apvcyl == True:
                print("radius?")
                radius = input()
                try:
                    radius = float(radius)
                except:
                    error(1)
                    break
                print("length?")
                length = input()
                try:
                    length = float(length)
                except:
                    error(1)
                    break
                volume = radius * radius
                volume = volume * pi
                volume = volume * length
                print("Volume is",volume)
                apvcyl = False

        elif command == "apv sph":
            apvsph = True
            while apvsph == True:
                print("Radius?")
                radius = input()
                try:
                    radius = float(radius)
                except:
                    error(1)
                    break
                thingy = 4 / 3
                volume = radius * radius * radius
                volume = thingy * volume
                volume = volume * pi
                print("Volume is",volume)
                spvsph = False


        elif command == "contact":
            print("Email: enderbyteprograms@gmail.com")
            print("Discord: Enderbyte09#0542")

        elif command == "credits":
            print("Basic Utilities (c) 2021-2022 Enderbyte Programs")
            print("Installer by Inno Setup")
            print("Coded in Python 3.7.3, 3.9.2, 3.9.6, 3.9.7, 3.10.0, 3.10.1, 3.10.2, 3.10.4, 3.10.5 and 3.9.5; compiled in Pyinstaller 4.2, 4.3, 4.4, 4.5.1, 4.6, and 4.7 and 4.8 and 4.10 and 5.0 and 5.1")
            print("Written by Enderbyte09")
            print("With IDLE for 64-bit Windows")
            print("And notepad++")
            print("And Thonny IDE for Raspberry Pi 4")
            print('AND IDLE 3.7.3 for Raspberry Pi 4')
            print('And Visual Studio Code')
            print("Game board pictures by Kdog.")
            print("Insults by Arceus007")
            print("Started on April 12, 2021")
            print("Warning.mp3 sound by MyInstants")


        elif command == "prank":
            def prank():
                x = random.randint(1,4)
                if x == 1:
                    webbrowser.open("https://www.youtube.com/watch?v=oHg5SJYRHA0")
                elif x == 2:
                    webbrowser.open("https://www.sketchywebsite.net")
                elif x == 3:
                    webbrowser.open("https://geekprank.com/fake-virus/")
                elif x == 4:
                    try:
                        winsound.Beep(1000,1000)
                    except:
                        error(2)
            pr = Tk()
            pr.title("The Big Red Button")
            lbl9 = Label(pr,text='Go on. Click the Big Red Button.')
            lbl9.grid(column=0,row=0)
            brb = Button(pr,text='Click me',command=prank,bg="red")
            brb.grid(column=0,row=1)
            pr.mainloop()
        elif command == "stop":
            xae = False
            sys.exit()
            break
        elif command == "stopall":
            try:
                os.system('taskkill /F /IM BasicUtilities.exe')
            except:
                error(2)
        elif command == "game":
            total_money = 500
            times_played = 0
            
            
            print("Welcome",sysuser,"to Enderbyte09's Beat th' Bank!")
            print("enter/return to continue.")
            input()
            print("You will have to open vault doors. You will gain money. However, there is a chance that you will open the ALARM, in which case you will get no money at all.")
            print("press enter/return to begin")
            print("It cost 100 to play.")
            input()
            if sysuser == 'Ruby' or sysuser == 'ruby':
                money = 10000000000000
                print('YOU WON A QUADRILLION DOLLARS')
                print('OHHHHHHHHHH')
            else:
                playagain = "y"
                possible = [10,25,50,75,100,150,200,300,"alarm","alarm"]
                while playagain == "y":
                    total_money = total_money - 100
                    money = 0
                    vaults = 0
                    alarm = False
                    hasstopped = False
                    while alarm == False and hasstopped == False:
                        print("do you want to open vault",vaults,"? (y/n)")
                        openvault = input()
                        if openvault.lower().startswith('y'):

                            moneyadd = random.choice(possible)
                            print("Vault",vaults,"has",moneyadd,"in it.")
                            print("")
                            vaults = vaults + 1
                            if moneyadd == "alarm":
                                alarm = True
                                if APPDATA["useDownloadedSounds"]:
                                    try:
                                        playsound(ASSETS+"/warning.mp3")
                                    except:
                                        log("Could not play sound, will try beep",WARN)
                                        try:
                                            winsound.Beep(1000,1000)
                                        except:
                                            log("Failed to play sound",ERROR)
                                else:
                                    try:
                                        winsound.Beep(1000,1000)
                                    except:
                                        log("Failed to play sound",ERROR)
                            elif alarm == False:
                                money = money + moneyadd
                        if not alarm:
                            print("You have",money,"dollars")
                        if openvault == "n":
                            hasstopped = True
                    if alarm ==  True:
                        money = 0
                    print("You finished with",money,"money!")
                    sleep(1)
                    total_money = total_money + money
                    times_played = times_played + 1
                    print("Thank you for participating in Beat The Bank!")
                    sleep(1)
                    answered = False
                    while answered == False:
                        print("Would you like to see your total statistics?[y/n]")
                        statsee = input()
                        if statsee.lower().startswith('y'):
                            answered = True
                            print("You have played",times_played,"games")
                            print("You have a total of",total_money,"money.")
                        elif statsee == "n":
                            answered = True
                            print("If you say so")
                    print("do you want to play again? (y/n)")
                    print("Typing n returns you to the commands menu.")
                    playagain = input()
                    if playagain.lower().startswith('y'):
                        playagain = 'y'
                        for i in range(1,20):
                            print("")
                        print("Do you want to change name? (y/n)")
                        changename = input()
                        if changename.lower().startswith('y'):
                            print("Please type your new name")
                            name = input()
                            print("Welcome,",name,"to Enderbyte09's Beat The Bank!")
                            for i in range(1,20):
                                print("")
                    else:
                        playagain = 'n'
        elif command == "insult":
            adjec = ["Porkmouthed","Loggerheaded","Beefwitted","Cream-faced","","Stupid","Imbecilic","Rank","Gassy","Pork-witted","Zombified","Gelatin-bottomed","Picklebrained","@$%&TYFt767tT*^TT*%%RFft*^((%^$4&^^4"]
            noun = ["Applejohn","Loon","Creamface","Beefwit","Porkwit","Dummy","Callipygian","Lunatic","Idiot","Yellwe","Monkeybottom","Clackdish","Jellyfish","Nimrod","^%*yuygg&yguguyTUGUT87t83t868%&&^^&*^&*"]
            adjec1 = random.choice(adjec)
            adjec2 = random.choice(adjec)
            noun1 = random.choice(noun)
            filler = "Thou art a"
            same = True
            while same == True:
                if adjec1 == adjec2:
                    adjec2= random.choice(adjec)
                else:
                    break
            exc = "!"
            nothing = False
            if adjec1 == "" or adjec2 == "":
                nothing = True
            print('')
            if nothing == False:
                adjec1 = adjec1 + ","
            noun1 = noun1 + exc
            print("-----")
            print(filler,adjec1,adjec2,noun1)
            print("-----")

        elif command == "reload":
            reload()

        elif command == "meter":
            newwindow()
            print('')
            
            if crashed == False:
                while True:
                    x = datetime.datetime.now()
                    a = x.year
                    b = x.month
                    c = x.day
                    d = x.hour
                    e = x.minute
                    f = x.second
                    f2 = x.microsecond
                    d1 = datetime.datetime(a,b,c,d,e,f,f2)
                    d0 = datetime.datetime(2019,12,31,0,0,0,000000)
                    difference = d1 - d0
                    total_seconds = difference.total_seconds()*1000
                    total_seconds = total_seconds/1000
                    total_min = total_seconds / 60
                    total_hr = total_min / 60
                    total_dy = total_hr / 24
                    total_wk = total_dy /7
                    total_yr = total_dy / 365.25
                    total_mt = total_yr * 12
                    print("")
                    print("There are",total_seconds,"seconds since",flush=True)
                    print("There are",total_min,"minutes since",flush=True)
                    print("There are",total_hr,"hours since",flush=True)
                    print("There are",total_dy,"days since",flush=True)
                    print("There are",total_wk,"weeks since",flush=True)
                    print("There are",total_mt,"month since",flush=True)
                    print("There are",total_yr,"years since life was normal.",flush=True)
                    print("\033[F\033[F\033[F\033[F\033[F\033[F\033[F\033[F",end="")
                    
                    sleep(0.1)
                    print(" "*50)
                    print(" "*50)
                    print(" "*50)
                    print(" "*50)
                    print(" "*50)
                    print(" "*50)
                    print(" "*50)
                    print(" "*50)
                    print("\033[F\033[F\033[F\033[F\033[F\033[F\033[F\033[F",end="")

        elif command == "browser":
            try:
                data = APPDATA["webhistory"][-1]
                if data is None:
                    data = "No History Yet"
            except:
                data = "No History Yet"
            def gourl():
                global txt
                global res
                res = txt.get()
                webbrowser.open(res)
                global data
                data = res
                writehistory()
                
            def sech():
                global txt
                global res
                res = txt.get()
                res = 'https://www.google.com/search?q='+res
                webbrowser.open(res)
                global data
                data = res
                writehistory()
            def sechb():
                global txt
                global res
                res = txt.get()
                res = 'https://www.bing.com/search?q='+res
                webbrowser.open(res)
                global data
                data = res
                writehistory()
            def sechy():
                global txt
                global res
                res = txt.get()
                res = 'https://www.yahoo.com/search?p='+res
                webbrowser.open(res)
                global data
                data = res
                writehistory()
            def sechw():
                global txt
                global res
                res = txt.get()
                res = 'https://en.wikipedia.org/w/index.php?search='+res
                webbrowser.open(res)
                global data
                data = res
                writehistory()
            def sechyo():
                global txt
                global res
                res = txt.get()
                res = 'https://www.youtube.com/results?search_query='+res
                webbrowser.open(res)
                global data
                data = res
                writehistory()
            def vh():
                global data
                if data == 'No History Yet':
                    Tk().withdraw()
                    messagebox.showinfo('Browser','No History Yet')
                else:
                    webbrowser.open(data)
            def writehistory():
                global res
                global lbl1
                APPDATA["webhistory"].append(res)
                lbl1.configure(text=res)
                updateappdata()
            def ddie():
                wbx.destroy()
                wbx.quit()

            def vhi():
                x = datetime.datetime.now()
                ftw = os.getcwd()+r"\.temp\webhistory_"+str(x).replace(" ","_").replace(":","_").replace(".","_")+".txt"
                
                wh = open(ftw,"w+")
                for historyitem in APPDATA["webhistory"]:
                    wh.write(historyitem+"\n")
                wh.close()
                os.startfile(ftw)


            wbx = Tk()
            wbx.title('BU Browser')
            
            lbl = Label(wbx,text='Put your URL or search here')
            lbl.grid(column=0,row=0)
            btn = Button(wbx,text='Close',bg='yellow',command=ddie)
            btn.grid(column=1,row=0)
            txt = Entry(wbx,width=50)
            txt.grid(column=0,row=1)
            btn1 = Button(wbx,text='Go to URL',command=gourl,bg='lime green')
            btn1.grid(column=0,row=2)
            btn2 = Button(wbx,text='Search with Google',command=sech,bg='lime green')
            btn2.grid(column=1,row=2)
            btn5 = Button(wbx,text='Bing',command=sechb,bg='lime green')
            btn5.grid(column=2,row=2)
            btn4 = Button(wbx,text='Yahoo',command=sechy,bg='lime green')
            btn4.grid(column=3,row=2)
            btn5 = Button(wbx,text='Wikipedia',command=sechw,bg='lime green')
            btn5.grid(column=4,row=2)
            btn6 = Button(wbx,text='Youtube',command=sechyo,bg='lime green')
            btn6.grid(column=5,row=2)
            lbl1 = Label(wbx,text=data)
            lbl1.grid(column=0,row=3)
            btn3 = Button(wbx,text='Go to recent search',bg='SkyBlue1',command=vh)
            btn3.grid(column=1,row=3)
            btn4 = Button(wbx,text='View history',bg='SkyBlue1',command=vhi)
            btn4.grid(column=2,row=3)
            wbx.mainloop()

        elif command == "logoff":
            os.system('shutdown /l')
        elif command == "restart":
            os.system('shutdown /r /t 0')

        elif command == "rng":
            afghs = True
            while afghs == True:
                print("Lowest number?")
                botrand = input()
                u = botrand.isnumeric()
                if u == False:
                    error(1)
                    break

                botrand = int(botrand)
                print("Highest number?")
                toprand = input()
                w = toprand.isnumeric()
                if w == False:
                    error(1)
                    break
                toprand = int(toprand)
                randhj = random.randint(botrand,toprand)
                print("-----")
                print(randhj)
                print("-----")
                afghs = False
        elif command == "cf":
            cf = ("heads","tails")
            cfe = random.choice(cf)
            print("-----")
            print(cfe)
            print("-----")
        elif command == "alarm":
            ajh = True
            while ajh == True:
                newwindow()
                print("What year for alarm?")
                g = input()
                m = g.isnumeric()
                if m == False:
                    error(1)
                    break
                g = int(g)
                print("Month?")
                h = input()
                n = h.isnumeric()
                if n == False:
                    error(1)
                    break
                h = int(h)
                if h < 1 or h > 12:
                    error(5)
                    break
                print("Day?")
                i = input()
                nom3 = i.isnumeric()
                if nom3 == False:
                    error(1)
                    break
                i = int(i)
                if h > 31:
                    error(5)
                    break
                print("Hour?")
                j = input()
                nom4 = j.isnumeric()
                if nom4 == False:
                    error(1)
                    break
                j = int(j)
                if j > 23:
                    error(5)
                    break
                print("Minute?")
                k = input()
                nom5 = k.isnumeric()
                if nom5 == False:
                    error(1)
                    break
                k = int(k)
                if k > 59:
                    error(5)
                    break
                print("Second?")
                l = input()
                nom6 = l.isnumeric()
                if nom6 == False:
                    error(1)
                    break
                l = int(l)
                if l > 59:
                    error(5)
                    break
                print("Alarm will ring at",g,"-",h,"-",i,"at",j,":",k,":",l)
                isdone = False
                while True:
                    x = datetime.datetime.now()
                    a = x.year
                    b = x.month
                    c = x.day
                    d = x.hour
                    e = x.minute
                    f = x.second
                    f2 = x.microsecond
                    d0 = datetime.datetime(a,b,c,d,e,f,f2)
                    try:
                        d1 = datetime.datetime(g,h,i,j,k,l,000000)
                    except:
                        error(5)
                        crashed = True
                        break
                    difference = d1 - d0
                    total_seconds = difference.total_seconds()
                    total_seconds = total_seconds * 1000 / 1000
                    total_min = total_seconds / 60
                    total_hr = total_min / 60
                    total_dy = total_hr / 24
                    total_wk = total_dy /7
                    total_yr = total_dy / 365.25
                    total_mt = total_yr * 12
                    print("")
                    print("There are",total_seconds,"seconds left")
                    print("There are",total_min,"minutes left")
                    print("There are",total_hr,"hours left")
                    print("There are",total_dy,"days left")
                    print("There are",total_wk,"weeks left")
                    print("There are",total_mt,"month left")
                    print("There are",total_yr,"years left")
                    print("\033[F\033[F\033[F\033[F\033[F\033[F\033[F\033[F",end="")
                    
                    if d0 == d1 or d0 > d1:
                        print("\n"*7)
                        break
                    if not isdone:
                        sleep(0.1)
                        print(" "*50)
                        print(" "*50)
                        print(" "*50)
                        print(" "*50)
                        print(" "*50)
                        print(" "*50)
                        print(" "*50)
                        print(" "*50)
                        print("\033[F\033[F\033[F\033[F\033[F\033[F\033[F\033[F",end="")
                if crashed == True:
                    break
                print("Your timer is done")
                asdfgh = True
                while asdfgh == True:
                    if APPDATA["useDownloadedSounds"]:
                        try:
                            playsound(ASSETS+"/warning.mp3")
                            asdfgh = False
                        except:
                            try:
                                winsound.Beep(1000,1000)
                            except:
                                print("Could not play sound")
                                crashed = True
                                asdfgh = False
                                break
                    else:
                        try:
                            winsound.Beep(1000,1000)
                        except:
                            print("Could not play sound")
                            crashed = True
                            asdfgh = False
                            break

                for i in range(4):
                    if crashed == False:
                        if APPDATA["useDownloadedSounds"]:
                            try:
                                playsound(ASSETS+"/warning.mp3")
                            except:
                                crashed = True
                        else:
                            try:
                                winsound.Beep(1000,1000)
                            except:
                                crashed=True
                ajh = False
        elif command == "time":
            x = datetime.datetime.now()
            print(x)
        elif command == "counter":
            tgy = True
            while tgy == True:
                newwindow()
                print("counting year?")
                g = input()
                m = g.isnumeric()
                if m == False:
                    error(1)
                    break
                g = int(g)
                print("Month?")
                h = input()
                yu = h.isnumeric()
                if yu == False:
                    error(1)
                    break
                h = int(h)
                if h > 12:
                    error(5)
                    break
                print("Day")
                i = input()
                fh = i.isnumeric()
                if fh == False:
                    error(1)
                    break
                i = int(i)
                if i > 31:
                    error(5)
                    break
                print("Hour?")
                j = input()
                yt = j.isnumeric()
                if yt == False:
                    error(1)
                    break
                j = int(j)
                if j > 23:
                    error(5)
                    break
                print("Minute?")
                k = input()
                er = k.isnumeric()
                if er == False:
                    error(1)
                    break
                k = int(k)
                if k > 59:
                    error(5)
                    break
                print("Second?")
                l = input()
                xie = l.isnumeric()
                if xie == False:
                    error(1)
                    break
                l = int(l)
                if l > 59:
                    error(5)
                    break
                zxcv = True
                while zxcv == True:
                    x = datetime.datetime.now()
                    a = x.year
                    b = x.month
                    c = x.day
                    d = x.hour
                    e = x.minute
                    f = x.second
                    f2 = x.microsecond
                    d0 = datetime.datetime(a,b,c,d,e,f,f2)
                    try:
                        d1 = datetime.datetime(g,h,i,j,k,l,000000)
                    except:
                        error(5)
                        crashed = True
                        tgy = False
                        break

                    difference = d0 - d1
                    total_seconds = difference.total_seconds()
                    total_seconds = total_seconds * 1000 / 1000
                    total_min = total_seconds / 60
                    total_hr = total_min / 60
                    total_dy = total_hr / 24
                    total_wk = total_dy /7
                    total_yr = total_dy / 365.25
                    total_mt = total_yr * 12
                    print("")
                    print("There are",total_seconds,"seconds since")
                    print("There are",total_min,"minutes since")
                    print("There are",total_hr,"hours since")
                    print("There are",total_dy,"days since")
                    print("There are",total_wk,"weeks since")
                    print("There are",total_mt,"month since")
                    print("There are",total_yr,"years since")
                    print("\033[F\033[F\033[F\033[F\033[F\033[F\033[F\033[F",end="")
                    
                    sleep(0.1)
                    print(" "*50)
                    print(" "*50)
                    print(" "*50)
                    print(" "*50)
                    print(" "*50)
                    print(" "*50)
                    print(" "*50)
                    print(" "*50)
                    print("\033[F\033[F\033[F\033[F\033[F\033[F\033[F\033[F",end="")
                if crashed == True:
                    break

        elif command == "lag":
            qwe = datetime.datetime.now()
            qwer = qwe.second
            nogo = False
            if qwer > 55:
                print(":(")
                print("Please try this after the minute rolls over in less than 5 seconds.")
                nogo = True
            if nogo == False:
                newwindow()
                averagelag = 0
                tavglag = 0
                tlagcount = 0
                lagcount = 0
                try:
                    s = turtle.getscreen()
                    t = turtle.Turtle()
                except:
                    s = turtle.getscreen()
                    t = turtle.Turtle()
                turtle.title("Lag Graph")
                turtle.hideturtle()
                
                t.hideturtle()
                turtle.tracer(False)
                def isneg(var):
                    if var < 0:
                        return True
                    else:
                        return False
                def tlwrite(y,colour):
                    global t
                    t.penup()
                    x = 100+y
                    t.goto(-300,y)
                    t.pencolor(colour)
                    t.pendown()
                    
                    t.write(str(x))
                    t.goto(300,y)
                    t.penup()
                t.speed(0)
                t.penup()
                t.goto(-300,-100)
                t.pendown()
                t.goto(300,-100)
                t.penup()
                t.goto(-300,-50)
                t.pendown()
                t.pencolor("green")
                t.write("50")
                t.goto(300,-50)
                t.penup()
                t.goto(-300,0)
                t.pendown()
                t.pencolor("yellow")
                t.write("100")
                t.goto(300,0)
                tlwrite(-60,"green")
                tlwrite(-70,"green")
                tlwrite(-80,"green")
                tlwrite(-90,"green")
                tlwrite(100,"orange")
                tlwrite(200,"red")
                tlwrite(300,"red")
                tlwrite(400,"black")
                t.goto(-300,-150)
                t.pencolor("red")
                t.pendown()
                t.forward(50)
                t.write("lag")
                t.penup()
                t.pencolor("green")
                t.forward(50)
                t.pendown()
                t.forward(50)
                t.write("Average cycle lag")
                t.penup()
                t.pencolor("blue")
                t.forward(50)
                t.pendown()
                t.forward(50)
                t.write("Overall average lag")
                t.penup()
                t.goto(-300,-100)
                t.pendown()
                t.pencolor("red")
                turtle.update()
                lnp = t.pos()
                lanp = t.pos()
                tlan = t.pos()
                noscreen = False
                ttotal = 0
                qwe = datetime.datetime.now()
                if not os.path.isfile("lag.csv"):
                    cycle = 0
                else:
                    with open("lag.csv") as la:
                        lla = la.readlines()
                    cyclee = lla[len(lla)-1].split(",")[5]
                    try:
                        cycle = int(cyclee)+1
                    except:
                        cycle = 0
                sleep(1)
                while True:

                    qwer = qwe.second
                    if qwer > 57:
                        sleep(3)
                        qwe = datetime.datetime.now()
                        qwer = qwe.second
                        sleep(1)
                    fa = qwe.strftime('%S.%f')[:-3]
                    fa = float(fa)
                    lagcount = lagcount + 1
                    tlagcount += 1
                    
                    qwert = datetime.datetime.now()
                    ft = qwert.strftime('%S.%f')[:-3]
                    ft = float(ft)
                    lag = ft - fa
                    lag = lag - 1
                    lag = lag * 1000
                    if lag < 0:
                        lag = 3000
                    lag = int(str(lag).split(".")[0])
                    averagelag = averagelag + lag
                    avglag = averagelag / lagcount
                    avglag = round(avglag,3)
                    tavglag += lag
                    xavglag = tavglag / tlagcount
                    xavglag = round(xavglag,3)
                    
                    try:
                        if noscreen == False:
                            tlag = lag - 100
                            talag = avglag - 100
                            tlg = xavglag - 100
                            ttotal = ttotal + 10
                            tgotototal = ttotal - 300
                            t.goto(tgotototal,tlag)
                            lnp = t.pos()
                            t.penup()
                            t.pencolor("purple")
                            t.goto(lanp[0],lanp[1])
                            t.pendown()
                            t.goto(tgotototal,talag)
                            lanp = t.pos()
                            t.penup()
                            t.pencolor('blue')
                            t.goto(tlan[0],tlan[1])
                            t.pendown()
                            t.goto(tgotototal,tlg)
                            tlan = t.pos()
                            t.penup()
                            t.pencolor('red')
                            t.goto(lnp[0],lnp[1])
                            t.pendown()
                            turtle.update()
                            if tgotototal > 300:                               
                                t.pencolor("red")
                                t.clear()
                                ttotal = 0
                                t.penup()
                                t.goto(-300,-100)
                                t.pendown()
                                t.pencolor("black")
                                t.goto(300,-100)
                                t.penup()
                                t.goto(-300,-50)
                                t.pendown()
                                t.pencolor("green")
                                t.write("50")
                                t.goto(300,-50)
                                t.penup()
                                t.goto(-300,0)
                                t.pendown()
                                t.pencolor("yellow")
                                t.write("100")
                                t.goto(300,0)
                                tlwrite(-60,"green")
                                tlwrite(-70,"green")
                                tlwrite(-80,"green")
                                tlwrite(-90,"green")
                                tlwrite(100,"orange")
                                tlwrite(200,"red")
                                tlwrite(300,"red")
                                tlwrite(400,"black")
                                t.goto(-300,-150)
                                t.pencolor("red")
                                t.pendown()
                                t.forward(50)
                                t.write("lag")
                                t.penup()
                                t.pencolor("purple")
                                t.forward(50)
                                t.pendown()
                                t.forward(50)
                                t.write("Average cycle lag")
                                t.penup()
                                t.pencolor("blue")
                                t.forward(50)
                                t.pendown()
                                t.forward(50)
                                t.write("Overall average lag")
                                t.penup()
                                t.goto(-300,tlag)
                                t.pendown()
                                t.pencolor("red")
                                turtle.update()
                                lnp = (-300,tlag)
                                lanp = (-300,-100)
                                tlan = (-300,tlg)
                                averagelag = 0
                                lagcount = 0
                                cycle += 1
                    except:
                        xsgued = 0
                    oqwe = qwe
                    qwe = datetime.datetime.now()
                    
                    print(" "*80)
                    print(" "*80)
                    print(" "*80)
                    print("\033[F\033[F\033[F",end="")
                    print("your computer is lagging by",lag,"milliseconds")
                    print("Your moving average.60 computer lag is",avglag,"milliseconds")
                    print("Your all-time average computer lag is",xavglag,"milliseconds")
                    print("\033[F\033[F\033[F",end="")
                    if not os.path.isfile("lag.csv"):
                        with open("lag.csv","w+") as l:
                            l.write("m-start,m-end,lag,cycleaverage,allaverage,cycle\n")
                    with open("lag.csv","a") as l:
                        l.write(f"{oqwe},{qwert},{lag},{avglag},{xavglag},{cycle}\n")
                    sleep(1)
        elif command == "avg":
            nums = 0
            total = 0
            avg = 0
            crashed = False
            isdone = False
            while isdone == False:
                print("Do you want to add a data value (y/n)")
                adddata = input()
                if adddata.lower().startswith('y'):
                    print("Please put the value.")
                    addnum = input()
                    try:
                        addnum = float(addnum)
                    except:
                        print("No, NO NO NO!")
                        print("How many times do we have to tell you that you")
                        print("DON'T PUT LETTERS HERE!?!?!?!?!?")
                        print("Please wait while we sort out your TERRIBLE ERROR")
                        print("You will be punished for your INSOLENCE")
                        print("Your average will not work right this time, because YOU decided to input a STRING in a place where only INTEGERS or FLOATS are allowed.")
                        print("If I was you, I'd go back to the command menu and start again")
                        sleep(3)
                        crashed = True
                    if crashed == False:
                        nums = nums + addnum

                        total = total + 1
                elif adddata == "n":
                    isdone = True
            if crashed == False:

                try:
                    avg = nums / total
                    print("Your average is",avg)
                    print("")
                except:
                    print("DON'T DIVIDE BY 0, YOU JERK.")

            else:
                print("Because YOU messed up, YOU have to start OVER AGAIN.")

        elif command == "m8b":
            paty = ("Yes","It is certain","Outlook Good","No","Not a chance","My sources say no","Concentrate and ask again","BasicUtilities.exe has stopped working. Please try again later.")
            print("What do you want to ask The Magic 8 ball?")
            qutchten = input()
            answty = random.choice(paty)
            print("-----")
            print(answty)
            print("-----")

        elif command == "snl":
            print("Subcommands for snl:")
            print("snl manual: Play snakes and ladders")
            print("snl bot: Have a bot play Snakes and Ladders for you. Does not count for points.")
            print("snl stats: View your snakes and ladders statistics.")
            print("-Exiting to the command menu does not lose your statistics, however, closing this program will.-")

        elif command == "snl manual":
            names = ("Jim","Bob","Joe","Jeff","George","Sally","Emily","Doge","Tim","Bottomhead","Ruby")
            opponent = random.choice(names)
            print("Your opponent is",opponent,"!")
            square = 0
            opponent_square = 0
            print("Do you want to see the game board? (y/n)")
            seeboard = input()
            if seeboard.lower().startswith('y'):
                awrt = True
                while awrt == True:
                    try:
                        os.startfile(ASSETS+"/gameboard.jpg")
                    except:
                        print("Oh no! Something went wrong!")
                        
                        print("")
                        sleep(1)
                        break
                    finally:
                        break
            while square < 100 and opponent_square < 100:
                print("")
                print("It is your turn! Press enter to roll the dice!")
                input()
                diceroll = random.randint(1,6)
                print("you rolled a",diceroll,"!")
                square = square + diceroll
                sleep(1)
                print("You landed on square",square)
                print("")
                if square == 3:
                    print("You landed on a ladder square!")
                    square = 35
                    sleep(1)
                    print("You climbed to square",square)
                elif square == 15:
                    print("You landed on a secret ladder square!")
                    square = 65
                    sleep(1)
                    print("You climbed to square",square)
                elif square == 23:
                    print("You landed on a secret snake square!")
                    square = 2
                    sleep(1)
                    print("You slid to square",square)
                elif square == 29:
                    print("You landed on a ladder square!")
                    square = 71
                    sleep(1)
                    print("You climbed to square",square)
                elif square == 54:
                    print("You landed on a ladder square!")
                    square = 84
                    sleep(1)
                    print("You climbed to square",square)
                elif square == 63:
                    print("You landed on a snake square!")
                    square = 22
                    sleep(1)
                    print("You slid to square",square)
                elif square == 78:
                    print("You landed on a snake square!")
                    square = 36
                    sleep(1)
                    print("You slid to square",square)
                elif square == 80:
                    print("You landed on a ladder square!")
                    square = 100
                    sleep(1)
                    print("You climbed to square",square)
                elif square == 89:
                    print("You landed on a snake square!")
                    square = 72
                    sleep(1)
                    print("You slid to square",square)
                elif square == 94:
                    print("You landed on a snake square!")
                    square = 27
                    sleep(1)
                    print("You slid to square",square)
                elif square == 99:
                    print("You landed on a snake square!")
                    square = 21
                    sleep(1)
                    print("You slid to square",square)
                if square > 99:
                    break
                print("It is now",opponent,"'s turn!")
                opponent_diceroll = random.randint(1,6)
                sleep(1)
                print(opponent,"rolled a",opponent_diceroll)
                opponent_square = opponent_square + opponent_diceroll
                sleep(1)
                #todo 1.8 pre-3 fix this
                print(opponent,"landed on square",opponent_square)
                if opponent_square == 3:
                    print(opponent,"landed on a ladder square!")
                    opponent_square = 35
                    sleep(1)
                    print(opponent,"climbed to square",opponent_square)
                elif opponent_square == 15:
                    print(opponent,"landed on a secret ladder square!")
                    opponent_square = 65
                    sleep(1)
                    print(opponent,"climbed to square",opponent_square)
                elif opponent_square == 23:
                    print(opponent," landed on a secret snake square!")
                    opponent_square = 2
                    sleep(1)
                    print(opponent,"slid to square",opponent_square)
                elif opponent_square == 29:
                    print(opponent,"landed on a ladder square!")
                    opponent_square = 71
                    sleep(1)
                    print(opponent,"climbed to square",opponent_square)
                elif opponent_square == 54:
                    print(opponent,"landed on a ladder square!")
                    opponent_square = 84
                    sleep(1)
                    print(opponent,"climbed to square",opponent_square)
                elif opponent_square == 63:
                    print(opponent,"landed on a snake square!")
                    opponent_square = 22
                    sleep(1)
                    print(opponent,"slid to square",opponent_square)
                elif opponent_square == 78:
                    print(opponent,"landed on a snake square!")
                    opponent_square = 36
                    sleep(1)
                    print(opponent,"slid to square",opponent_square)
                elif opponent_square == 80:
                    print(opponent,"landed on a ladder square!")
                    opponent_square = 100
                    sleep(1)
                    print(opponent,"climbed to square",opponent_square)
                elif opponent_square == 89:
                    print(opponent,"landed on a snake square!")
                    opponent_square = 72
                    sleep(1)
                    print(opponent,"slid to square",opponent_square)
                elif opponent_square == 94:
                    print(opponent,"landed on a snake square!")
                    opponent_square = 27
                    sleep(1)
                    print(opponent,"slid to square",opponent_square)
                elif opponent_square == 99:
                    print(opponent,"landed on a snake square!")
                    opponent_square = 21
                    sleep(1)
                    print(opponent,"slid to square",opponent_square)
            if square > 99:
                print("You Won!")
                gamees_won = gamees_won + 1
            if opponent_square > 99:
                print(opponent,"won!")
            gamees_played = gamees_played + 1
        elif command == "snl stats":
            print("-----Snakes And Ladders Statistics-----")
            print("You have played",gamees_played,"games!")
            print("You have won",gamees_won,"games!")

        elif command == "snl bot":
            names = ("Jim","Bob","Joe","Jeff","George","Sally","Emily","Doge","Tim","Bottomhead","Ruby")
            opponent = random.choice(names)
            print("Your opponent is",opponent,"!")
            square = 0
            opponent_square = 0
            print("Do you want to see the game board? (y/n)")
            seeboard = input()
            if seeboard.lower().startswith('y'):
                awrt = True
                while awrt == True:
                    try:
                        os.startfile(ASSETS+"/gameboard.jpg")
                    except:
                        error(2)
                        break
                    finally:
                        break
            while square < 100 and opponent_square < 100:
                print("It is your turn!")

                diceroll = random.randint(1,6)
                print("you rolled a",diceroll,"!")
                square = square + diceroll

                print("You landed on square",square)
                print("")
                if square == 3:
                    print("You landed on a ladder square!")
                    square = 35

                    print("You climbed to square",square)
                elif square == 15:
                    print("You landed on a secret ladder square!")
                    square = 65

                    print("You climbed to square",square)
                elif square == 23:
                    print("You landed on a secret snake square!")
                    square = 2

                    print("You slid to square",square)
                elif square == 29:
                    print("You landed on a ladder square!")
                    square = 71

                    print("You climbed to square",square)
                elif square == 54:
                    print("You landed on a ladder square!")
                    square = 84

                    print("You climbed to square",square)
                elif square == 63:
                    print("You landed on a snake square!")
                    square = 22

                    print("You slid to square",square)
                elif square == 78:
                    print("You landed on a snake square!")
                    square = 36

                    print("You slid to square",square)
                elif square == 80:
                    print("You landed on a ladder square!")
                    square = 100

                    print("You climbed to square",square)
                elif square == 89:
                    print("You landed on a snake square!")
                    square = 72

                    print("You slid to square",square)
                elif square == 94:
                    print("You landed on a snake square!")
                    square = 27

                    print("You slid to square",square)
                elif square == 99:
                    print("You landed on a snake square!")
                    square = 21

                    print("You slid to square",square)
                if square > 99:
                    break
                print("It is now",opponent,"'s turn!")
                opponent_diceroll = random.randint(1,6)

                print(opponent,"rolled a",opponent_diceroll)
                opponent_square = opponent_square + opponent_diceroll

                #todo 1.8 fix this
                print(opponent,"landed on square",opponent_square)
                if opponent_square == 3:
                    print(opponent,"landed on a ladder square!")
                    opponent_square = 35

                    print(opponent,"climbed to square",opponent_square)
                elif opponent_square == 15:
                    print(opponent,"landed on a secret ladder square!")
                    opponent_square = 65

                    print(opponent,"climbed to square",opponent_square)
                elif opponent_square == 23:
                    print(opponent," landed on a secret snake square!")
                    opponent_square = 2

                    print(opponent,"slid to square",opponent_square)
                elif opponent_square == 29:
                    print(opponent,"landed on a ladder square!")
                    opponent_square = 71

                    print(opponent,"climbed to square",opponent_square)
                elif opponent_square == 54:
                    print(opponent,"landed on a ladder square!")
                    opponent_square = 84

                    print(opponent,"climbed to square",opponent_square)
                elif opponent_square == 63:
                    print(opponent,"landed on a snake square!")
                    opponent_square = 22

                    print(opponent,"slid to square",opponent_square)
                elif opponent_square == 78:
                    print(opponent,"landed on a snake square!")
                    opponent_square = 36

                    print(opponent,"slid to square",opponent_square)
                elif opponent_square == 80:
                    print(opponent,"landed on a ladder square!")
                    opponent_square = 100

                    print(opponent,"climbed to square",opponent_square)
                elif opponent_square == 89:
                    print(opponent,"landed on a snake square!")
                    opponent_square = 72

                    print(opponent,"slid to square",opponent_square)
                elif opponent_square == 94:
                    print(opponent,"landed on a snake square!")
                    opponent_square = 27

                    print(opponent,"slid to square",opponent_square)
                #NO!!!!!!!!!!!!!!!!!!! THE IMMATURITY!! I CANT STAND IT!!!!
                elif opponent_square == 99:
                    print(opponent,"landed on a snake square!")
                    opponent_square = 21

                    print(opponent,"slid to square",opponent_square)
            if square > 99:
                print("You Won!")

            if opponent_square > 99:
                print(opponent,"won!")

        else:
            if not APPDATA["useColouredText"]:
                print('Warning: You typed an unrecognized command. If you want to see the commands list, dismiss this message and run the command "help" or "?".')
            else:
                termcolor.cprint('Warning: You typed an unrecognized command. If you want to see the commands list, dismiss this message and run the command "help" or "?".',"yellow")
            #Whew! That's a lot of code!
#Wait! There is more!
    cmd_run = cmd_run + 1
    try:
        xlms = APPDATA["commandsRun"]
    
        xlms += 1
        APPDATA["commandsRun"] = xlms
    except:
        APPDATA["commandsRun"] = 0
    finally:
        updateappdata()
    xlm = APPDATA["showCommandsRun"]
    xmls = str(cmd_run)
    if not xlm:
        pass
    elif xlm and command != "":
        
        print('You have run',cmd_run,'commands')
    
    else:
        log("Invalid notifs",ERROR)
        APPDATA["showCommandsRun"] = True
        updateappdata()
        xls = 'You have run this many commands: ' + xmls + ". If you don't want to see how many commands you have run, change it with the notifs command."
        if command != "":
            print(xls)
    
#NOW we're done        
