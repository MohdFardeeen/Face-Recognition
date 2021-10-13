from tkinter import *
#from tkinter import font

root=Tk()
root.title("FACE RECOGNITION")
root.geometry('400x200')
root.minsize(100,50)
#app name
app_name=Label(text="FACE RECOGNITION",height='1',width='18',font=('courier',20))
app_name.pack()
#button for select the image in file
btn=Button(text='select the image',width='20',height='1',font=('comicsansms 12 bold'),fg='white',bg='gray',borderwidth=10)
btn.pack(side='top')
btn=Button(text='open camera',width='20',height='1',font=('comicsansms 12 bold'),fg='white',bg='gray',borderwidth=10)
btn.pack(side='top')
btn=Button(text='select video',width='20',height='1',font=('comicsansms 12 bold'),fg='white',bg='gray',borderwidth=10)
btn.pack(side='top')
root.mainloop()

