'''
Created on Oct 15, 2022

@author: ASUS
'''
'''
Created on Oct 1, 2022

@author: ASUS
'''
import mysql.connector
from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
import tkinter as tk 

#host : Máy chủ lưu trữ nơi đặt máy chủ CSDL
#user : Tên người dùng để đăng nhập -> tamkem
#password : mật khẩu để sử dụng -> 05112002
#database : CSDL để sử dụng , nếu ko thêm thì sẽ không sử dụng 1 csdl cụ thể 
#port : cổng MySQL để sử dụng mặc định thường là OK (3306)
mydb = mysql.connector.connect(
  host="localhost",
  user="tamkem",
  password="05112002",
  database = "QuanLySinhVien"
)

mycursor = mydb.cursor() #-> trỏ để cơ sở dữ liệu hiện tại

sql = "select * from SinhVien"
mycursor.execute(sql)
result = mycursor.fetchall()
arr = []
for i in result:
    arr.append('--------------------------')
    arr.append(f"{i[0]}          {i[1]}")

win = tk.Tk()
win.geometry('900x400')


txb = Entry(win,width = 30,font = ('Times New Roman',12))
txb.place(x = 10,y = 120)

value = tk.Variable(value = arr)
listbox = tk.Listbox(win,
                     width = 250,
                     height = 20,#tạo chiều cao cho list
                     listvariable = value,#tạo giá trị cho list -> dùng cách này thay cho dùng insert
                     selectmode = tk.BROWSE)#chọn chế độ : cho phép bấm chọn bất kì dòng nào
listbox.place(x=0,y=0)
    
    
win.mainloop()


