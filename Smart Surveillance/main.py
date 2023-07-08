import tkinter as tk
import tkinter.font as font
from PIL import Image, ImageTk

from in_out import in_out
from find_motion import find_motion
from parking import parking
from identify import maincall


window = tk.Tk()
window.title("Smart Surveillance")
window.iconphoto(False, tk.PhotoImage(file='icons/camera.png'))
window.geometry('1280x720')

frame1 = tk.Frame(window)

label_title = tk.Label(frame1, text="Smart Surveillance")
label_font = font.Font(size=35, weight='bold',family='Helvetica')
label_title['font'] = label_font
label_title.grid(pady=(10,10), column=2)


icon = Image.open('icons/camera.png')
icon = icon.resize((150,150), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(row=1, pady=(5,10), column=2)

btn1_image = Image.open('icons/lamp.png')
btn1_image = btn1_image.resize((50,50), Image.ANTIALIAS)
btn1_image = ImageTk.PhotoImage(btn1_image)

btn2_image = Image.open('icons/parking.jpg')
btn2_image = btn2_image.resize((50,50), Image.ANTIALIAS)
btn2_image = ImageTk.PhotoImage(btn2_image)

btn3_image = Image.open('icons/exit.png')
btn3_image = btn3_image.resize((50,50), Image.ANTIALIAS)
btn3_image = ImageTk.PhotoImage(btn3_image)

btn4_image = Image.open('icons/in_out.png')
btn4_image = btn4_image.resize((50,50), Image.ANTIALIAS)
btn4_image = ImageTk.PhotoImage(btn4_image)

btn5_image = Image.open('icons/identity.png')
btn5_image = btn5_image.resize((50,50), Image.ANTIALIAS)
btn5_image = ImageTk.PhotoImage(btn5_image)



btn_font = font.Font(size=25)
btn1 = tk.Button(frame1, text='Monitor', height=110, width=270, fg='black',command = find_motion, image=btn1_image, compound='left')
btn1['font'] = btn_font
btn1.grid(row=3, pady=(20,10))

btn2 = tk.Button(frame1, text='Parking Space', height=110, width=270, fg='black', command= parking, compound='left', image=btn2_image)
btn2['font'] = btn_font
btn2.grid(row=3, pady=(20,10), column=3, padx=(20,5))

btn3 = tk.Button(frame1,text='Exit', height=110, width=270, fg='black', command=window.quit, image=btn3_image)
btn3['font'] = btn_font
btn3.grid(row=6, pady=(20,10), column=2)

btn4 = tk.Button(frame1, text='In-Out', height=110, width=270, fg='black', command=in_out, image=btn4_image, compound='left')
btn4['font'] = btn_font
btn4.grid(row=5, pady=(20,10), column=3)

btn5 = tk.Button(frame1, text="Identify", fg="black",command=maincall, compound='left', image=btn5_image, height=110, width=270)
btn5['font'] = btn_font
btn5.grid(row=5, pady=(20,10))

frame1.pack()
window.mainloop()