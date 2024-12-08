import os
import sys
import PIL.Image
import PIL.ImageFilter as pif
import PIL.ImageTk
import tkinter as Tk
import tkinter.filedialog

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def button_click():
    print("!Click!")
    
def resize_button():
    x = resize_var.get()
    export = checkExport_var.get()
    go = False
    try:
        if (x == '' or x == ' '):
            return
        if any(not ch.isdigit() for ch in x):
            resizebox.delete(0, "end")
            Tk.messagebox.showinfo('Üzenet', 'Nem szám vagy nem megfelelő szám')  
            return
        elif (int(x) < 1):
            Tk.messagebox.showinfo('Üzenet', 'Túl kis szám')
        else:
            go = True
    except Exception as ep:
        Tk.messagebox.showerror('error', ep)

    if (go):
        per = float(x)/100
        neww = orig_width*per
        newh = orig_height*per       
        resized_image = image_base.resize((int(neww), int(newh)), PIL.Image.BILINEAR )
        newreslabel.config(text = 'Új méret:' + str(resized_image.width) + 'x' + str(resized_image.height))
        if (export):   
            resized_image.save(path_ext[0] + '_re' + str(x) + '.' + path_ext[1])
            Tk.messagebox.showinfo('Üzenet', 'Sikeres átméretezés és exportálás.') 

def gablur_button():
    x = gablur_var.get()
    export = checkExport_var.get()
    go = False

    try:
        if (x == '' or x == ' '):
            return
        if any(not ch.isdigit() for ch in x):
            resizebox.delete(0, "end")
            Tk.messagebox.showinfo('Üzenet', 'Nem szám vagy nem megfelelő szám')  
            return
        elif (int(x) < 1):
            image_display.configure(image=image)
            image_display.image = image
            if(export):
                 Tk.messagebox.showwarning('Info', 'Nem exportált, mivel a kép nem változik ezzel.')
            return
        else:
            go = True
    except Exception as ep:
        Tk.messagebox.showerror('error', ep)

    if (go):
        blur_image = image_base.filter(pif.GaussianBlur(radius = int(x)))
        if (export):            
            blur_image.save(path_ext[0] + '_gablur' + str(x) + '.' + path_ext[1])
            Tk.messagebox.showinfo('Üzenet', 'Sikeres Gauss-blur operáció és exportálás.')             
            
        nimage = PIL.ImageTk.PhotoImage(blur_image)
        image_display.configure(image=nimage)
        image_display.image = nimage

def rotate_button(rot):
    rotarg = ''
    rotstring = 'null'
    if (rot == 0):
        rotarg = PIL.Image.ROTATE_90
        rotstring = 'bal90'
    elif (rot == 1):
        rotarg = PIL.Image.ROTATE_270
        rotstring = 'jobb90'
    elif (rot == 2):
        rotarg = PIL.Image.ROTATE_180
        rotstring = '180'
        
    rot_image = image_base.transpose(rotarg)
    rot_image.save(path_ext[0] + '_' + rotstring + '.' + path_ext[1])
    Tk.messagebox.showinfo('Üzenet', 'Sikeres forgatás és exportálás.')  
            
root = Tk.Tk()
root.title("Képfeldolgozó")
root.geometry('%dx%d+%d+%d' % (700, 900, root.winfo_screenwidth()/2-350, root.winfo_screenmmheight()/2-100))
root.after(1, lambda: root.focus_force())

try:
    image = Tk.filedialog.askopenfile()
    original_path = image.name
    path_ext = original_path.split('.')
except:
    Exception()

try:
    print(image.name)
    print(type(image))
    f = open(image.name, "rb")
except AttributeError:
    root.destroy()
    
try:
    image = PIL.Image.open(f)
    orig_width=image.width
    orig_height=image.height
    size = 700, 700
    dimage = image
    dimage.thumbnail(size)
except PIL.UnidentifiedImageError:
    Tk.messagebox.showerror("Error", "Nem kép. Kérlek válassz egy képfájlt miután a program újraindult.")
    restart_program()
except Exception() as ep:
    Tk.messagebox.showerror("Error", ep)
    restart_program()

prev = Tk.Label(root, text="Megnyitott fájl:")
prev.pack(side=Tk.TOP, anchor="nw")

image_base = image
dimage = PIL.ImageTk.PhotoImage(dimage)
image_display = Tk.Label(root, image=dimage)
image_display.pack(side=Tk.TOP)

resize_var = Tk.StringVar()
gablur_var = Tk.StringVar()
checkExport_var = Tk.BooleanVar()

brotl90 = Tk.Button(root, text="forgatás BAL 90°", command=lambda: rotate_button(0))
brotl90.pack(side=Tk.TOP, anchor="nw")
brotr90 = Tk.Button(root, text="forgatás JOBB 90°", command=lambda: rotate_button(1))
brotr90.pack(side=Tk.TOP, anchor="nw")
brot180 = Tk.Button(root, text="forgatás 180°", command=lambda: rotate_button(2))
brot180.pack(side=Tk.TOP, anchor="nw")

checkbox_export = Tk.Checkbutton(root,
                text='Exportálás?',
                variable=checkExport_var,
                onvalue=True,
                offvalue=False)
checkbox_export.pack(pady=10)

resizebox = Tk.Entry(root, textvariable=resize_var, font=('arial', 12))
resizebox.pack(side=Tk.TOP)
resizebox.config(state='normal')
resizebox.focus_set()

reslabel = Tk.Label(root, text="%")
reslabel.pack()

origreslabel = Tk.Label(root, text='Eredeti méret: ' + str(orig_width) + 'x' + str(orig_height))
origreslabel.pack()

newreslabel = Tk.Label(root, text='')
newreslabel.pack()

bresval = Tk.Button(
    root,
    text='Átméretez',
    command=resize_button
)
bresval.pack(pady=10)

gablurbox = Tk.Entry(root, textvariable=gablur_var, font=('arial', 12))
gablurbox.pack(side=Tk.TOP)
gablurbox.config(state='normal')

gablabel = Tk.Label(root, text="rádiusz")
gablabel.pack()

bgablur = Tk.Button(
    root,
    text='Gauss-Blur',
    command=gablur_button
)
bgablur.pack(pady=10)


root.mainloop()
