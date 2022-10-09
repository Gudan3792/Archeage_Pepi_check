from asyncio.windows_events import NULL
import json
from msilib.schema import ComboBox
from multiprocessing.sharedctypes import Value
from tkinter import *
import tkinter.ttk as ttk
from turtle import width

with open('ID.json', 'r') as f:
    json_data = json.load(f)
    # print(json_data['Num1']['PW']) // 값 한개 꺼낼때 이거로 ㅇ
    # json_data['Num1'] = {'UserID':'Edma','PW':'123'}
    # json_data['Num2'] = {'UserID':'Edm2a','PW':'123'}
    # json_data['Num3'] = {'UserID':'Edm22a','PW':'123'}
# print(json.dumps(json_data,ensure_ascii=False,indent="\t"))
    
tk = Tk()
tk.title('아이디 저장용 프로그램')
tk.geometry('400x120')
tk.resizable(False, False)

def Save():
    json_data['Num'+ str(list_var.get())] = {'ID' : entry1.get(), 'PW' : entry2.get()}
    with open('ID.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f,ensure_ascii = False, indent="\t")
    ID_Box_redirected()

def Delete():
    json_data['Num'+ str(list_var.get())] = {'ID' : "ex@example.com", 'PW' : "123456789"}
    with open('ID.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent="\t")
    ID_Box_redirected()

def ID_Box_redirected():
    listbox.delete(0,4)
    x = 0
    while x <= (len(json_data)-1):
        listbox.insert(x,json_data['Num'+str(x)]['ID'])
        x=x+1

      
label1 = Label(tk,text='ID').place(x=1, y=15)
label2 = Label(tk,text='PW').place(x=1, y=40)
entry1 = Entry(tk, width=22)
entry1.place(x=30, y=15)
entry2 = Entry(tk, width=22)
entry2.place(x=30, y=40)
btn1 = Button(tk,text='저장',command=Save, width=10).place(x=30, y=65)
btn2 = Button(tk,text='삭제',command=Delete, width=10).place(x=110, y=65)

# number = StringVar()
# number_chosen = ttk.Combobox(tk, width=20, textvariable=number, state='readonly')
# number_chosen['values'] = json_data['Num1']['ID'] , json_data['Num2']['ID'] , json_data['Num3']['ID'], json_data['Num4']['ID'], json_data['Num5']['ID']
# number_chosen.place(x=200, y=15)
# number_chosen.current(0)

listbox = Listbox(tk, selectmode='single',height=0,width=20)
x = 0
while x <= (len(json_data)-1):
    listbox.insert(x,json_data['Num'+str(x)]['ID'])
    x = x+1


listbox.place(x=200,y=15)

list_var = IntVar()
radio1 = ttk.Radiobutton(tk, text="1번", value=0, variable=list_var).place(x=350,y=5)
radio2 = ttk.Radiobutton(tk, text="2번", value=1, variable=list_var).place(x=350,y=25)
radio3 = ttk.Radiobutton(tk, text="3번", value=2, variable=list_var).place(x=350,y=45)
radio4 = ttk.Radiobutton(tk, text="4번", value=3, variable=list_var).place(x=350,y=65)
radio5 = ttk.Radiobutton(tk, text="5번", value=4, variable=list_var).place(x=350,y=85)

tk.mainloop()
