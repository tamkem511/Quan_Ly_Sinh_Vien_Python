'''
Created on Oct 15, 2022

@author: ASUS
'''
#from DangNhap import *
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from DangNhap import *
import mysql.connector

def subrice():
    mydbDK = mysql.connector.connect(
        host = "LAPTOP-JSUGHU76",
        user = "tamkem",
        password = "05112002",
        database = "qlsvdhcn"
    )
    
    mycursorDK = mydbDK.cursor()
    
    winDK = tk.Tk()
    winDK.title("Đăng Ký")
    winDK.geometry("450x300")
    
    #tạo tiêu đề đăng ký
    lbTieuDeDK = tk.Label(winDK,font = ('Times New Roman',20),fg = 'black',text = "ĐĂNG KÝ")
    lbTieuDeDK.pack()
    
    #tạo textbox MaSV 
    lbMSVDK = Label(winDK,text = 'Mã Sinh Viên : ',font = ('Times Neu Roman',10))
    lbMSVDK.place(x = 20,y = 65)
    
    txbMSVDK = Entry(winDK,width = 30,font = ('Times New Roman',12))
    txbMSVDK.place(x = 150,y = 60)
    txbMSVDK.focus()
    
    #tạo textbox Mật Khẩu
    lbMatKhauDK = Label(winDK,text = 'Mật Khẩu : ',font = ('Times Neu Roman',10))
    lbMatKhauDK.place(x = 20,y = 125)
    
    txbMatKhauDK = Entry(winDK,width = 30,font = ('Times New Roman',12))
    txbMatKhauDK.place(x = 150,y = 120)
    
    #tạo textbox xác nhận Mật Khẩu
    lbXacNhanMatKhauDK = Label(winDK,text = 'Xác Nhận Mật Khẩu : ',font = ('Times Neu Roman',10))
    lbXacNhanMatKhauDK.place(x = 20,y = 185)
    
    txbXacNhanMatKhauDK = Entry(winDK,width = 30,font = ('Times New Roman',12))
    txbXacNhanMatKhauDK.place(x = 150,y = 180)
    
    errorDK = tk.Label(winDK,fg = 'red',font = ('Times New Roman',10))
    errorDK.place(x=150 ,y=150)
    
    #tạo nút đăng kí
    
    def kiemTraMSVDK():
        sql = "select Msv from SinhVien"
        mycursorDK.execute(sql)
        result = mycursorDK.fetchall()
        count = 0
        for i in result:
            tdn = i[0];
            if(txbMSVDK.get() == tdn):
                count=count+1
        if(count == 1):
            return 1
    def kiemTraMSVTontai():
        sql = "select TenDN from TaiKhoan"
        mycursorDK.execute(sql)
        result = mycursorDK.fetchall()
        count = 0
        for i in result:
            tdn = i[0];
            if(txbMSVDK.get() == tdn):
                count=count+1
        if(count==0):
            return 1
    
    '''sự kiện click đăng ký '''
    def clickDK():
        if(kiemTraMSVDK() == 1 and kiemTraMSVTontai() == 1 and txbMatKhauDK.get() == txbXacNhanMatKhauDK.get()):
            sql = "insert into TaiKhoan(TenDN,MatKhau,LoaiTK) values (%s,%s,%s)"
            val = (txbMSVDK.get(),txbMatKhauDK.get(),1)
            mycursorDK.execute(sql,val)
            mydbDK.commit()
            winDK.destroy()
            login()
        else:
            errorDK['text'] = "Tên Đăng Nhập Đã Tồn Tại Hoặc Mật Khẩu Chưa Hợp Lệ !"
        #winDK.destroy()
        #login()
    btnDangKy = tk.Button(winDK,text = "Đăng Ký",width = 20,bg='#7fffd4',command = clickDK)
    btnDangKy.place(x = 20,y = 240)
    
    btnHuyDangKy = tk.Button(winDK,text = "Hủy Bỏ",width = 20,bg='#ff4040')
    btnHuyDangKy.place(x = 245,y = 240)
    
    winDK.mainloop()
    
def main():
    subrice()


if(__name__ == "__main__"):
    main()

























































































