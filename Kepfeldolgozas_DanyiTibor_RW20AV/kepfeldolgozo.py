import os
import sys
import PIL.Image
import PIL.ImageFilter as pif
import PIL.ImageEnhance as pie
import PIL.ImageTk
import tkinter as Tk
import tkinter.filedialog

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def button_click():
    print("!Click!")
    
def bnw_button():
    export = checkExport_var.get()
    
    bnw_image = pie.Color(image)
    bnw_image = bnw_image.enhance(0.0)
    if (export):            
        bnw_image.save(path_ext[0] + '_bnw.' + path_ext[1])
        Tk.messagebox.showinfo('Üzenet', 'Sikeres fekete-fehér konverzió és exportálás.')  
    
    nimage = PIL.ImageTk.PhotoImage(bnw_image.resize( (int(disp_size[0]), int(disp_size[1])) ))
    image_display.configure(image=nimage)
    image_display.image = nimage
    
def ee_button():
    export = checkExport_var.get()
    
    ee_image = image.filter(pif.EDGE_ENHANCE())
    if (export):            
        ee_image.save(path_ext[0] + '_ee.' + path_ext[1])
        Tk.messagebox.showinfo('Üzenet', 'Sikeres élesítés és exportálás.')  
    
    nimage = PIL.ImageTk.PhotoImage(ee_image.resize( (int(disp_size[0]), int(disp_size[1])) ))
    image_display.configure(image=nimage)
    image_display.image = nimage    
    
def resize_button():
    x = resize_var.get()
    export = checkExport_var.get()
    go = False
    try:
        if (x == '' or x == ' '):
            return
        if any(not ch.isdigit() for ch in x):            
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
            Tk.messagebox.showinfo('Üzenet', 'Nem szám vagy nem megfelelő szám')  
            return
        elif (int(x) < 1):
            image_display.configure(image=dimage)
            image_display.image = dimage
            if(export):
                 Tk.messagebox.showwarning('Info', 'Nem exportált, mivel a kép nem változik ezzel.')
            return
        else:
            go = True
    except Exception as ep:
        Tk.messagebox.showerror('error', ep)

    if (go):
        blur_image = image.filter(pif.GaussianBlur(radius = int(x)))
        if (export):            
            blur_image.save(path_ext[0] + '_gablur' + str(x) + '.' + path_ext[1])
            Tk.messagebox.showinfo('Üzenet', 'Sikeres Gauss-blur operáció és exportálás.')          
           
        nimage = PIL.ImageTk.PhotoImage(blur_image.resize( (int(disp_size[0]), int(disp_size[1])) ))
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

root.geometry('%dx%d+%d+%d' % (700, 1080, root.winfo_screenwidth()/2-350, root.winfo_screenmmheight()-290))

root.after(1, lambda: root.focus_force())

def imreset_button():        
    nimage = PIL.ImageTk.PhotoImage(image.resize( (int(disp_size[0]), int(disp_size[1])) ))
    image_display.configure(image=nimage)
    image_display.image = nimage

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
    
    im_ar = orig_width / orig_height
    if (orig_width > orig_height):        
        disp_size = 700, 700/im_ar    
    elif (orig_width < orig_height):
        disp_size = 700*im_ar, 700  
    else:
        disp_size = 700, 700
        
    dimage = image.resize((int(disp_size[0]), int(disp_size[1])))
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

bim_reset = Tk.Button(root, text='Eredeti kép betöltése', command=imreset_button)
bim_reset.pack(side=Tk.TOP, anchor="n", pady=10, padx=0)

brotl90 = Tk.Button(root, text="forgatás BAL 90°", command=lambda: rotate_button(0))
brotl90.pack(fill='none', anchor="nw")
brotr90 = Tk.Button(root, text="forgatás JOBB 90°", command=lambda: rotate_button(1))
brotr90.pack(fill='none', anchor="nw")
brot180 = Tk.Button(root, text="forgatás 180°", command=lambda: rotate_button(2))
brot180.pack(fill='none', anchor="nw")
bbnw = Tk.Button(root, text='Fekete-Fehér', command=bnw_button)
bbnw.pack(fill='none', anchor="nw", pady=10, padx=0)
bee = Tk.Button(root, text='Élesítés', command=ee_button)
bee.pack(fill='none', anchor="nw", pady=10, padx=0)

checkbox_export = Tk.Checkbutton(root,
                text='Exportálás?',
                variable=checkExport_var,
                onvalue=True,
                offvalue=False)
checkbox_export.pack(pady=10)

resizebox = Tk.Entry(root, textvariable=resize_var, font=('arial', 12))
resizebox.pack(fill='none')
resizebox.config(state='normal')
resizebox.focus_set()

reslabel = Tk.Label(root, text="%")
reslabel.pack(fill='none')

origreslabel = Tk.Label(root, text='Eredeti méret: ' + str(orig_width) + 'x' + str(orig_height))
origreslabel.pack(fill='none')

newreslabel = Tk.Label(root, text='')
newreslabel.pack(fill='none')

bresval = Tk.Button(
    root,
    text='Átméretez',
    command=resize_button
)
bresval.pack(pady=10)

gablurbox = Tk.Entry(root, textvariable=gablur_var, font=('arial', 12))
gablurbox.pack(fill='none')
gablurbox.config(state='normal')

gablabel = Tk.Label(root, text="rádiusz")
gablabel.pack(fill='none')

bgablur = Tk.Button(
    root,
    text='Gauss-Blur',
    command=gablur_button
)
bgablur.pack(fill='none')

root.mainloop()
