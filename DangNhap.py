'''
Created on Oct 15, 2022

@author: ASUS
'''
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from TrangChuSV import *
from Dang_Ky import *
import mysql.connector
from ADMIN import administrator


def login():
    mydb = mysql.connector.connect(
        host = "LAPTOP-JSUGHU76",
        user = "tamkem",
        password = "05112002",
        database = "qlsvdhcn"
    )
    mycursor = mydb.cursor()
    winDN = tk.Tk()
    winDN.title("Đăng Nhập")
    winDN.geometry("450x300")
    
    goi_y = tk.Label(winDN,text = "Nếu Bạn Chưa có tài khoản : ",font = ('Times New Roman',10),fg = 'red')
    goi_y.place(x = 50,y=250)
    
    def nextDK():
        winDN.destroy()
        subrice()
        
    
    btnDK = tk.Button(winDN,text = "Đăng Ký",font = ('Times New Romans',10),command = nextDK)
    btnDK.place(x = 215,y = 245)
    
    #tạo tiêu đề đăng ký
    lbTieuDeDN = tk.Label(winDN,font = ('Times New Roman',20),fg = 'black',text = "ĐĂNG NHẬP")
    lbTieuDeDN.pack()
    
    #tạo textbox MaSV 
    lbMSVDN = Label(winDN,text = 'Tên Đăng Nhập : ',font = ('Times Neu Roman',10))
    lbMSVDN.place(x = 20,y = 65)
    
    txbMSVDN = Entry(winDN,width = 30,font = ('Times New Roman',12))
    txbMSVDN.place(x = 150,y = 60)
    txbMSVDN.focus()
    
    #tạo textbox Mật Khẩu
    lbMatKhauDN = Label(winDN,text = 'Mật Khẩu : ',font = ('Times Neu Roman',10))
    lbMatKhauDN.place(x = 20,y = 125)
    
    txbMatKhauDN = Entry(winDN,width = 30,font = ('Times New Roman',12))
    txbMatKhauDN.place(x = 150,y = 120)
    
    errorDN = tk.Label(winDN,fg = 'red',font = ('Times New Roman',10))
    errorDN.place(x=150 ,y=150)
    #hàm kiểm tra tài khoản
    def KiemTraTK():
        sql = "Select TenDN from TaiKhoan"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        count = 0
        for i in result:
            tdn = i[0]
            if(txbMSVDN.get() == tdn):
                count = count + 1
        if(count == 1 and txbMSVDN != "ADMIN"):
            return 1 
        else:
            return 0  
        
    def KiemTraMK():
        sql = "Select MatKhau from TaiKhoan where TenDN = %s"
        val = (txbMSVDN.get(),)
        mycursor.execute(sql,val)
        result = mycursor.fetchall()
        count = 0
        for i in result:
            tdn = i[0]
            if(txbMatKhauDN.get() == tdn):
                count = count + 1
        if(count == 1):
            return 1 
        else:
            return 0      
    
    #tạo nút đăng kí
    def ClickDangNhap():
        if(txbMSVDN.get() == "ADMIN" and txbMatKhauDN.get() == "1"):
            winDN.destroy()
            administrator()
        elif(KiemTraTK()==1 and KiemTraMK() ==1):
            winDN.destroy()
            PageAd()
        else:
            errorDN['text'] = "Tài Khoản Hoặc Mật Khẩu Không Chính Xác"
    btnDangNhap = tk.Button(winDN,text = "Đăng Nhập",width = 20,bg='#7fffd4',command = ClickDangNhap)
    btnDangNhap.place(x = 20,y = 185)
    
    btnHuyDangNhap = tk.Button(winDN,text = "Hủy Bỏ",width = 20,bg='#ff4040')
    btnHuyDangNhap.place(x = 245,y = 185)
    
    winDN.mainloop()


def main():
    login()


if(__name__ == "__main__"):
    main()
