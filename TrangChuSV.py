'''
Created on Oct 15, 2022

@author: ASUS
'''

import mysql.connector
from DangNhap import *
from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
import tkinter as tk 
import mysql.connector


def PageAd():
    mydbTT = mysql.connector.connect(
        host = "LAPTOP-JSUGHU76",
        user = "tamkem",
        password = "05112002",
        database = "qlsvdhcn"
    )
    mycursorTT = mydbTT.cursor()
    winTT = tk.Tk()
    winTT.title('Trang Chủ Sinh Viên')
    winTT.geometry('800x400')
    winTT['bg'] = 'white'
    
    lbtitleTT = Label(winTT,text = 'TRANG CHỦ',font = ('Times New Roman',14))
    lbtitleTT.pack()
    
    def PrevLogin():
        winTT.destroy()
        login()      
        
        
    backLogin = tk.Button(winTT,text = "Quay Lại Đăng Nhập",bg = "white",font = ('Times New Roman',8),command = PrevLogin)
    backLogin.place(x=0,y=0)
    
    #thêm button xem thông tin
    
    def showKhoa():
        sql = "select * from Khoa"
        mycursorTT.execute(sql)
        result = mycursorTT.fetchall()
        arr = []
        arr.append("{:^10} {:^30} {:^30}".format('Mã Khoa','Tên Khoa','Trưởng Khoa'))
        for i in result:
            arr.append('{:->100}'.format(' '))
            #arr.append(f"{i[0]}     {i[1]}     {i[2]}     {i[3]}     {i[4]}     {i[5]}     {i[6]}")
            arr.append("{:^10} {:^30} {:^30}".format(i[0],i[1],i[2]))
        
        value = tk.Variable(value = arr)
        showData['listvariable'] = value
        
    def clickShowKhoa():
        showKhoa()
    
    
    btnXemKhoa = tk.Button(winTT,text = 'Xem Khoa',width = 15,font = ('Times New Roman',10),bg = '#8fbc8f',command = clickShowKhoa)
    btnXemKhoa.place(x = 30,y=50)
    
    
    def showLop():
        sql = "select * from Lop"
        mycursorTT.execute(sql)
        result = mycursorTT.fetchall()
        arr = []
        arr.append("{:^10} {:^30} {:^50} {:^10} {:^30}".format('Mã Lớp','Tên Lớp','Sĩ Số','Mã Khoa','STT'))
        for i in result:
            arr.append('{:->100}'.format(' '))
            #arr.append(f"{i[0]}     {i[1]}     {i[2]}     {i[3]}     {i[4]}     {i[5]}     {i[6]}")
            arr.append("{:^10} {:^30} {:^30} {:^40} {:^30}".format(i[0],i[1],i[2],i[3],i[4]))
        
        value = tk.Variable(value = arr)
        showData['listvariable'] = value
        
    def clickShowLop():
        showLop()
        
    btnXemLop= tk.Button(winTT,text = 'Xem Lớp',width = 15,font = ('Times New Roman',10),bg = '#8fbc8f',command = clickShowLop)
    btnXemLop.place(x = 160,y=50)
    
    showData = tk.Listbox(winTT,width = 120,height = 17)
    showData.place(x = 30,y = 100)
    def showSV():
        sql = "select * from SinhVien"
        mycursorTT.execute(sql)
        result = mycursorTT.fetchall()
        arr = []
        arr.append("{:^10} {:^30} {:^30} {:^30} {:^30} {:^30} {:^30}".format('MSV','Họ Tên','Ngày Sinh','Giới Tính','Địa Chỉ','SDT','Mã Lớp'))
        for i in result:
            arr.append('{:->150}'.format(' '))
            #arr.append(f"{i[0]}     {i[1]}     {i[2]}     {i[3]}     {i[4]}     {i[5]}     {i[6]}")
            arr.append("{:^10} {:^30} {} {:^40} {:^20} {:^20} {:>20}".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        
        value = tk.Variable(value = arr)
        showData['listvariable'] = value
        
    def clickShowSV():
        showSV()
    btnXemSV= tk.Button(winTT,text = 'Xem Sinh Viên',width = 15,font = ('Times New Roman',10),bg = '#8fbc8f',command = clickShowSV)
    btnXemSV.place(x = 290,y=50)
    
    #thanh input tìm kiếm
        
    txbTimKiemTenSV = tk.Entry(winTT,width = 18,font = ('Times New Roman',14),bg = '#c1ffc1')
    txbTimKiemTenSV.place(x = 420,y = 50)
    
    def searchNamSV():
        sql = 'select * from SinhVien where HoTen = %s'
        val = (txbTimKiemTenSV.get(),)
        mycursorTT.execute(sql,val)
        result = mycursorTT.fetchone();
        if(result != None):
            arr = (f"Mã Sinh Viên : {result[0]}", f"Họ Tên : {result[1]}", f"Ngày Sinh : {result[2]}", f"Giới Tính: {result[3]}",f"Địa Chỉ : {result[4]}", f"SDT : {result[5]}", f"Mã Lớp : {result[6]}")
            value = tk.Variable(value = arr)
            showData['listvariable'] = value
    btnTimSV= tk.Button(winTT,text = 'Tìm',width = 8,font = ('Times New Roman',10),bg = '#8fbc8f',command = searchNamSV)
    btnTimSV.place(x = 605,y=50)
    
    
    winTT.mainloop()
    
def main():
    PageAd()
if(__name__ == "__main__"):
    main()
