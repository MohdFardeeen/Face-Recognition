from tkinter import *

root=Tk()
canvas = Canvas(root, width = 1920, height = 1080)      
canvas.pack()     
img = PhotoImage(file="image2.png")      
canvas.create_image(900,500,image=img) 
root.title("FACE RECOGNITION")
root.geometry('1920x1080')
root.minsize(100,50)
root.configure(bg='blue')
def a():
    print("hello")
#app name
app_name=Label(text="WELCOME",height='1',width='18',font=('courier',30),bg='blue')
app_name.pack()
#button for select the image in file
btn=Button(text='choose the image',width='40',height='1',font=('comicsansms 12 bold'),fg='white',bg='dark gray',borderwidth=10,command=a)
btn.place(x=200,y=380)
btn=Button(text='open camera',width='40',height='1',font=('comicsansms 12 bold'),fg='white',bg='dark grey',borderwidth=10)
btn.place(x=200,y=440)
btn=Button(text='select video',width='40',height='1',font=('comicsansms 12 bold'),fg='white',bg='dark gray',borderwidth=10)
btn.place(x=200,y=500)
btn=Button(text='Exit',width='40',height='1',font=('comicsansms 12 bold'),fg='white',bg='dark gray',borderwidth=10)
btn.place(x=200,y=560)
btn=Button(text='file',width='5',height='1',font=('comicsansms 12 bold'),fg='white',bg='dark gray',borderwidth=3)
btn.place(x=0,y=0)
btn=Button(text='Help',width='5',height='1',font=('comicsansms 12 bold'),fg='white',bg='dark gray',borderwidth=3)
btn.place(x=70,y=0)
root.mainloop()

