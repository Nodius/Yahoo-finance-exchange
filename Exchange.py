from tkinter import *
from io import BytesIO
from PIL import Image, ImageTk
import requests
import webbrowser
import urllib
import urllib.request

#запрос на данные биржи
def request(event):
    tex1.delete(1.0,END)
    global st1,st2
    st1=ent1.get()
    st2=ent2.get()
    s='http://chartapi.finance.yahoo.com/instrument/1.1/'+st1+'/chartdata;type=quote;range='+st2+'d/csv'
    r=requests.get(s)
    tex1.insert(1.0,r.text)
    tex1.delete(1.0,3.0)
    graph(event)

#график с данными    
def graph(event):
    top=Toplevel()
    top.title('Graph')
    d='http://chartapi.finance.yahoo.com/z?s='+st1+'&t='+st2+'&q=l&l=on&z=s&'
    #'http://chartapi.finance.yahoo.com/z?s=goog&t=1m&q=l&l=on&z=s&p=m50,m300'#
    with urllib.request.urlopen(d) as u:
        raw_data = u.read()
    im = Image.open(BytesIO(raw_data))
    image = ImageTk.PhotoImage(im)
    label = Label(top,image=image)
    label.pack()
    top.mainloop()

#скачивание кодов биржи     
def tickerlist(event):
    url="http://investexcel.net/wp-content/uploads/2013/12/Yahoo-Ticker-Symbols-Jan-2015.zip"
    webbrowser.open(url)

     
root=Tk()
root.title('Exchange')
root.geometry('1000x565+450+200')
root.resizable('0','0')

lab1=Label(root,text='Yahoo Finance',font="Arial 18",fg="Red")
lab2=Label(root,text='Введите биржевой код')
lab3=Label(root,text='Объем данных в днях')

ent1=Entry(root)
ent2=Entry(root)

but1=Button(root,text="Запрос",width=30,bg="white",fg="blue")

but2=Button(root,text="Скачать биржевые коды",width=30,bg="white",fg="blue") 

tex1=Text(root,font="Verdana 12",wrap=WORD,width=100)

but1.bind("<Button-1>",request)
but2.bind("<Button-1>",tickerlist)

lab1.pack()
ent1.pack()
lab2.pack()
ent2.pack()
lab3.pack()
but1.pack()
but2.place(x=800,y=50)
tex1.pack()
root.mainloop()
