from tkinter import * 
from tkinter import messagebox 
import customtkinter 

papa = customtkinter.CTk()
papa.title('BIRTHDAY CODE FOR YOU! ')
papa.geometry('600x500')
papa.config(bg= 'pink')
papa.resizable(False, False)

font = ('Bodoni MT Black', 75)
font_one = ('Bodoni MT Black', 75)
font_two= ('Bodoni MT Black', 75)

def happy():
    global popshie 
    popshie = customtkinter. CTkToplevel()
    popshie.title('HAPPY BIRTHDAY MY PAPA')
    popshie.geometry('700x650')
    popshie.config(bg = 'orange')
    popshie.resizable(False, False)
    image = PhotoImage(file=r'pics/me and papa.png')
    image= customtkinter.CTkLabel(popshie, image= image, compound=TOP, anchor= N, text='' )
    image.place(x=50, y=110)
    iloveyou = PhotoImage(file=r'pics/i love you.png')
    greet= customtkinter.CTkLabel(popshie, image= iloveyou, compound=TOP, anchor=N, text='', fg_color='orange')
    greet.place(x=400, y=100)
    hbd = PhotoImage(file=r'pics/hbd logo.png')
    greet_one = customtkinter.CTkLabel(popshie, text='', image=hbd, compound=TOP, anchor=N, fg_color='orange')
    greet_one.place(x=100, y=0)



def birthday():
    messagebox.showwarning(title='BIRTHDAY MESSAGE', message='HELLO PAPA, HOPE YOU LIKE MY GIFT FOR YOU! HAPPY BIRTHDAY! THANK YOU FOR SUPPORTING US SA MGA GUSTO NAMIN, PAPA. THANK YOU FOR  WORKING SO HARD FOR US TO SUSTAIN OR SUPPORT OUR NEEDS AND SA PAG SUPPORT SA AMIN WHEN IT COMES TO ACADEMICS. THANK YOU SA PAGHATID SUNDO SA AKIN PA,  APPRECIATE KO PO/NAMIN YON. ALSO, THANK YOU FOR ALWAYS CHECKING UP ON US. WE LOVE YOU ALWAYS PA. MORE BIRTHDAY TO CELEBRATE WITH YOU, MY PAPA. I LOVE YOU ALWAYS! AND LAST, HAPPY BIRTHDAY, PAPA!! I LOVE YOU ALWAYS -ERICH' )

def father():
    global bestfather
    bestfather= customtkinter.CTkToplevel()
    bestfather.title('HAPPY BIRTHDAY BEST FATHER!')
    bestfather.geometry('800x730')
    bestfather.config(bg='#26CBF4')
    image= PhotoImage(file=r'pics/me and him1.png')
    me= customtkinter.CTkLabel(bestfather, image= image, compound=TOP, anchor=N, text='')
    me.place(x=250, y=20)
    hbd_text= PhotoImage(file=r'pics/hbd.png')
    hbd_text= customtkinter.CTkLabel(bestfather, text='', image= hbd_text, compound=TOP, anchor=N, fg_color='#26CBF4')
    hbd_text.place(x=0, y=20)
    ily_text= PhotoImage(file=r'pics/iloveyou message.png')
    ily_text= customtkinter.CTkLabel(bestfather, text='', image= ily_text, compound=TOP, anchor=N,fg_color='#26CBF4')
    ily_text.place(x=400, y=600)
    emoji = PhotoImage(file=r'pics/bday sticker.png')
    emoji= customtkinter.CTkLabel(bestfather, image= emoji, text='', fg_color='#26CBF4', compound=TOP, anchor=N)
    emoji.place(x=0, y=400)
    






happy= customtkinter.CTkButton(papa, text= 'HAPPY', text_color='black', height=100, width=100, font= font, command= happy)
happy.place(x=45, y=45)

birthday= customtkinter.CTkButton(papa, text= 'BIRTHDAY', text_color='black',height=100, width=100, font= font_one, command=birthday)
birthday.place(x=100, y= 200)

father = customtkinter.CTkButton(papa, text= 'PAPA!', text_color='black', height=100, width=100, font= font_one, command= father)
father.place(x=45, y= 350)





papa.mainloop()