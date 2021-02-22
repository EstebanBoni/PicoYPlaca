import sys
import datetime
from tkinter import *
from PIL import Image, ImageTk

def inTime(cTime):
    return ((cTime >= datetime.time(7,00) and cTime <= datetime.time(9,30)) or (cTime >= datetime.time(16,00) and cTime <= datetime.time(19,30)))

def canDrive(detNumber, dayOfweek,cTime):
    if detNumber < 3 and detNumber > 0:
        if dayOfweek == 0 and inTime(cTime):
            return "No puede circular"
    elif detNumber < 5:
        if dayOfweek == 1 and inTime(cTime):
            return "No puede circular"
    elif detNumber < 7:
        if dayOfweek == 2 and inTime(cTime):
            return "No puede circular"
    elif detNumber < 9:
        if dayOfweek == 3 and inTime(cTime):
            return "No puede circular"
    else:
        if dayOfweek == 4 and inTime(cTime):
            return "No puede circular"
    return "Puede circular"


def verify():
    global app
    try:
        idate = app.txtDate.get()
        cDate = datetime.date(int(idate[6:]),int(idate[3:5]), int(idate[:2])) 
        dayOfweek = cDate.weekday()
    except:
        messagebox.showerror('Error','La fecha debe estar en formato: dd-mm-aaaa')
        return
    
    try:
        itime = app.txtTime.get()
        cTime = datetime.time(int(itime[:2]),int(itime[3:]))
    except:
        messagebox.showerror('Error','La hora debe estar en formato hh:mm')
        
    placa = app.txtPlate.get()
    
    if (len(placa)==7):
        
        try:
            detNumber = int(placa[-1])
        except:
            messagebox.showerror('Error','La placa no es valida')
            
        messagebox.showinfo('Resultado',canDrive(detNumber,dayOfweek,cTime))
    else:
        messagebox.showerror('Error','La placa debe tener 7 digitos')
        

#UI

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        load = Image.open("./content/main.png")
        load = load.resize((350, 120), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
        img.width = 350

        self.lblPlate = Label(self, text="Ingrese la placa")
        self.lblPlate.place(x=30, y=150)
        self.txtPlate = Entry(self,width=10)
        self.txtPlate.place(x=200, y=150)
        self.lblTime = Label(self, text="Ingrese la hora")
        self.lblTime.place(x=30, y=200)
        self.txtTime = Entry(self,width=10)
        self.txtTime.place(x=200, y=200)
        self.lblDate = Label(self, text="Ingrese la fecha")
        self.lblDate.place(x=30, y=250)
        self.txtDate = Entry(self,width=10)
        self.txtDate.place(x=200, y=250)

        btnVerify = Button(self, text="Verificar", command=verify, width=10)
        btnVerify.place(x=135,y=300)
        
root = Tk()
app = Window(root)
root.wm_title("Pico y placa")
root.geometry("350x350")
root.mainloop()


window.mainloop()

sys.argv[0]