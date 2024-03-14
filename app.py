from tkinter import *
from tkinter import messagebox
from timeit import default_timer

import difflib
import requests


window=Tk()
window.geometry('850x530')
window.title('Speed Tester')



def Started():
    paragraphs = 1
    max_length=400
    api_url = 'https://api.api-ninjas.com/v1/loremipsum?paragraphs={}&max_length={}'.format(paragraphs,max_length)
    response = requests.get(api_url, headers={'X-Api-Key': '2reSDwEA0Bp/JtL3sA7ljg==ibBvL62FmQecu526'})
    sentence = response.json()
    paragraph_text = sentence.get('text', '')
    with open('message.txt','w') as file:
        file.write(paragraph_text)
    start.config(text='next')
    content.config(text=paragraph_text)



def Result():
    global text
    global starttime

    string=f'{text.get(1.0,END)}'
    end=default_timer()
    time=round(end-starttime,2)

    with open('message.txt','r') as file:
        paragraph_text=file.read()

    speed=round(len(paragraph_text.split())*60/time,2)

    accuracy=difflib.SequenceMatcher(None,paragraph_text,string).ratio()
    accuracy=str(round(accuracy*100))
    print(accuracy)

    message=f'Time= {time}seconds, Speed = {speed}wpm ,Acurracy= {accuracy}%'

    messagebox.showinfo('Result',message)

def Exit():
    window.destroy()



welcome=Label(window,text='Speed Tester',font=('ariel',25))
welcome.place(x=625,y=30)

content=Label( window,wraplength=500,justify="left",font=('ariel',13),bd=0)
content.place(x=10,y=10)

text=Text(window,height=14,width=58,bd=0,font=('ariel',13))
text.place(x=30,y=250)


start=Button(window,text='start',bg='#D2F59F',bd=0,command=Started)
start.place(x=602,y=410)

result=Button(window,text='result',bg='#D2F59F',bd=0,command=Result)
result.place(x=602,y=350)

exit=Button(window,text='exit',bg='#D2F59F',bd=0,command=Exit)
exit.place(x=602,y=475)


starttime=default_timer()


mainloop()