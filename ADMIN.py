'''
Created on Oct 15, 2022

@author: ASUS
'''
import mysql.connector
from tkinter import *
from DangNhap import *
from tkinter.ttk import *
from tkinter import scrolledtext
import tkinter as tk 
from tkinter import messagebox

def administrator():
    
    mydbAD = mysql.connector.connect(
        host = "LAPTOP-JSUGHU76",
        user = "tamkem",
        password = "05112002",
        database = "qlsvdhcn"
    )
    
    mycursorAD = mydbAD.cursor()
    
    
    winAD = tk.Tk()
    winAD.title('ADMIN')
    winAD.geometry('1200x500')

    tab_control = Notebook(winAD)
    
    tabSV = Frame(tab_control)
    tabLop = Frame(tab_control)
    tabKhoa = Frame(tab_control)
    tabTK = Frame(tab_control)
    
    tab_control.add(tabSV,text = 'Sinh Viên')
    tab_control.add(tabLop,text = 'Lớp')
    tab_control.add(tabKhoa,text = 'Khoa')
    tab_control.add(tabTK,text = 'Tài Khoản')
    tab_control.pack(expand = 1,fill = BOTH)
    
    def PrevLogin():
        winAD.destroy()
        login()      
        
        
    backLogin = tk.Button(tabSV,text = "Quay Lại Đăng Nhập",bg = "white",font = ('Times New Roman',8),command = PrevLogin)
    backLogin.place(x=0,y=0)
    backLogin = tk.Button(tabLop,text = "Quay Lại Đăng Nhập",bg = "white",font = ('Times New Roman',8),command = PrevLogin)
    backLogin.place(x=0,y=0)
    backLogin = tk.Button(tabKhoa,text = "Quay Lại Đăng Nhập",bg = "white",font = ('Times New Roman',8),command = PrevLogin)
    backLogin.place(x=0,y=0)
    backLogin = tk.Button(tabTK,text = "Quay Lại Đăng Nhập",bg = "white",font = ('Times New Roman',8),command = PrevLogin)
    backLogin.place(x=0,y=0)
    
    #xem sinh viên
    ShowDataSinhVienAD = tk.Listbox(tabSV,width = 130,height = 20,selectmode = tk.SINGLE)
    ShowDataSinhVienAD.place(x = 20,y = 100)
    infoSV = []
    import re
    def showSVAD():
        sql = "select * from SinhVien"
        mycursorAD.execute(sql)
        result = mycursorAD.fetchall()
        arr = []
        arr.append("{:^10} {:^30} {:^30} {:^30} {:^30} {:^30} {:^30}".format('MSV','Họ Tên','Ngày Sinh','Giới Tính','Địa Chỉ','SDT','Mã Lớp'))
        for i in result:
            #arr.append('{:->150}'.format(' '))
            #arr.append(f"{i[0]}     {i[1]}     {i[2]}     {i[3]}     {i[4]}     {i[5]}     {i[6]}")
            arr.append("{:^10} {:^30} {} {:^40} {:^20} {:^20} {:>20}".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
            infoSV.append([i[0],i[1],str(i[2]),i[3],i[4],i[5],i[6]])
        print(infoSV)
        value = tk.Variable(value = arr)
        ShowDataSinhVienAD['listvariable'] = value
    btnXemSVAD = tk.Button(tabSV,width = 12,text = 'Xem Sinh Viên',font = ('Times New Roman',10),bg='#8fbc8f',command = showSVAD)
    btnXemSVAD.place(x = 30,y = 50)
    
    
    #thêm,sửa xóa sinh viên
    frameSV = tk.Frame(tabSV,bg = '#e6e6fa',bd = '2',width = 310,height = 300,highlightcolor = 'red')
    frameSV.place(x = 850,y = 100)
    
    ''' phần nhập mã sinh viên '''
    lbMSVThem = tk.Label(frameSV,text = 'Mã Sinh Viên : ',font = ('Times New Roman',10))
    lbMSVThem.place(x=10,y=10)
    txbMSVThem = tk.Entry(frameSV,width = 20,font = ('Times New Roman',12))
    txbMSVThem.place(x = 120,y = 10)
    
    
    ''' phần nhập họ tên '''
    lbHoTenThem = tk.Label(frameSV,text = 'Họ Tên : ',font = ('Times New Roman',10))
    lbHoTenThem.place(x=10,y=50)
    txbHoTenThem = tk.Entry(frameSV,width = 20,font = ('Times New Roman',12))
    txbHoTenThem.place(x = 120,y = 50)
    
    ''' phần nhập Ngày Sinh '''
    lbNgaySinhThem = tk.Label(frameSV,text = 'Ngày Sinh : ',font = ('Times New Roman',10))
    lbNgaySinhThem.place(x=10,y=90)
    txbNgaySinhThem = tk.Entry(frameSV,width = 20,font = ('Times New Roman',12))
    txbNgaySinhThem.place(x = 120,y = 90)
    
    ''' phần nhập giới tính '''
    lbGioiTinhThem = tk.Label(frameSV,text = 'Giới Tính : ',font = ('Times New Roman',10))
    lbGioiTinhThem.place(x=10,y=130)
    #lưu lại giá trị khi click chọn
    gt = StringVar()
    #tạo 2 radio button để chọn giới tính
    def getGT():
        return gt.get()
    rdGioiTinhNamThem= tk.Radiobutton(frameSV,text = 'Nam',variable=gt,value = 'Nam',command = getGT)
    rdGioiTinhNamThem.place(x =120,y=130)
    rdGioiTinhNamThem.select()
    rdGioiTinhNuThem= tk.Radiobutton(frameSV,text = 'Nữ',variable = gt,value = 'Nữ',command = getGT)
    rdGioiTinhNuThem.place(x =200,y=130)
    
    ''' phần nhập Địa Chỉ '''
    lbDiaChiThem = tk.Label(frameSV,text = 'Địa Chỉ : ',font = ('Times New Roman',10))
    lbDiaChiThem.place(x=10,y=170)
    cbbDiaChiThem = Combobox(frameSV,width = 18,font = ('Times New Roman',12))
    cbbDiaChiThem['value'] = ('Phú Thọ','Hà Nội','Hải Dương','Nam Định','Bắc Giang','Yên Bái','Hải Phòng','Nghệ An','Thanh Hóa','Vĩnh Phúc','Sơn La','Lào Cai','Thái Bình','Quảng Ninh')
    cbbDiaChiThem.current(0)
    cbbDiaChiThem.place(x = 120,y = 170)
    
    
    ''' phần nhập SDT '''
    lbSDTThem = tk.Label(frameSV,text = 'SDT : ',font = ('Times New Roman',10))
    lbSDTThem.place(x=10,y=210)
    txbSDTThem = tk.Entry(frameSV,width = 20,font = ('Times New Roman',12))
    txbSDTThem.place(x = 120,y = 210)
    
    ''' phần nhập Mã Lớp '''
    lbMaLopThem = tk.Label(frameSV,text = 'Mã Lớp : ',font = ('Times New Roman',10))
    lbMaLopThem.place(x=10,y=250)
    cbMaLopThem = Combobox(frameSV,width = 18,font = ('Times New Roman',12))
    mycursorAD.execute("select MaLop from Lop")
    getTenLop = mycursorAD.fetchall()
    cbMaLopThem['value'] = [i[0] for i in getTenLop]
    cbMaLopThem.current(0)
    cbMaLopThem.place(x = 120,y = 250)
    
    def select_item(event): #bắt buộc phải có tham số event
        

        items = ShowDataSinhVienAD.curselection() #lấy ra tất cả các chỉ số đã chọn
        for i in items:
            txbMSVThem.delete(0,len(txbMSVThem.get()))
            txbHoTenThem.delete(0,len(txbHoTenThem.get()))
            txbNgaySinhThem.delete(0,len(txbNgaySinhThem.get()))
            txbSDTThem.delete(0,len(txbSDTThem.get()))
            if(i != 0):
                result = ShowDataSinhVienAD.get(i)
                #result = ([ShowDataSinhVienAD.get(i) for i in items])
                msv = result[0:9]
                
                sql = f'select * from SinhVien where Msv = {msv}'
                val = (msv,)
                mycursorAD.execute(sql)
                value = mycursorAD.fetchone()
                ma_sv = value[0]
                ho_ten = value[1]
                ngay_sinh = value[2]
                gioi_tinh = value[3]
                dia_chi = value[4]
                sdt = value[5]
                ma_lop = value[6]
                
                txbMSVThem.insert(0,ma_sv)
                txbHoTenThem.insert(0,ho_ten)
                txbNgaySinhThem.insert(0,ngay_sinh)
                txbSDTThem.insert(0,sdt)
                if(gioi_tinh == "Nam"):
                    rdGioiTinhNamThem.select()
                else:
                    rdGioiTinhNuThem.select()
                    
                mycursorAD.execute(f"select stt from SinhVien sv join Lop l\
                on sv.MaLop = l.MaLop\
                where Msv = {ma_sv} ")
                stt = mycursorAD.fetchone()
                cbMaLopThem.current(int(stt[0])-1)

    
    
#gọi event để thực hiện sự kiện click chọn giá trị
    ShowDataSinhVienAD.bind('<<ListboxSelect>>', select_item)

    
    def ThemSV():
        masv = txbMSVThem.get()
        hoten = txbHoTenThem.get()
        ngaysinh = txbNgaySinhThem.get()
        gioitinh = getGT()
        diachi = cbbDiaChiThem.get()
        sdt = txbSDTThem.get()
        malop = cbMaLopThem.get()
        if(masv =="" or hoten =="" or ngaysinh == "" or diachi == "" or sdt == ""):
            messagebox.showinfo('Thông Báo', 'Không Được Bỏ Trống Các Trường')
        else:
            sql = "insert into SinhVien(Msv,HoTen,NgaySinh,GioiTinh,DiaChi,SDT,MaLop) values\
            (%s,%s,%s,%s,%s,%s,%s)"
            val = (masv,hoten,ngaysinh,gioitinh,diachi,sdt,malop)
            mycursorAD.execute(sql,val)
            mydbAD.commit()
            messagebox.showinfo('Thông Báo','Thêm Mới Thành Công')
            showSVAD()
    
    btnThemSVAD = tk.Button(tabSV,text = 'Thêm',width = 12,font = ('Times New Roman',10),bg='#8fbc8f',command = ThemSV)
    btnThemSVAD.place(x= 850,y = 70)
    
    def SuaSV():
        masv = txbMSVThem.get()
        hoten = txbHoTenThem.get()
        ngaysinh = txbNgaySinhThem.get()
        gioitinh = getGT()
        diachi = cbbDiaChiThem.get()
        sdt = txbSDTThem.get()
        malop = cbMaLopThem.get()
        if(masv =="" or hoten =="" or ngaysinh == "" or diachi == "" or sdt == ""):
            messagebox.showinfo('Thông Báo', 'Không Được Bỏ Trống Các Trường')
        else:
            sql = f"update SinhVien set HoTen = '{hoten}',NgaySinh = '{ngaysinh}',GioiTinh = '{gioitinh}',DiaChi = '{diachi}',MaLop = '{malop}' where Msv = '{masv}'"
            val = (hoten,ngaysinh,gioitinh,diachi,sdt,malop,masv)
            mycursorAD.execute(sql)
            mydbAD.commit()
            messagebox.showinfo('Thông Báo','Cập Nhật Thành Công')
            showSVAD()
    
    btnSuaSVAD = tk.Button(tabSV,text = 'Sửa',width = 12,font = ('Times New Roman',10),bg='#8fbc8f',command = SuaSV)
    btnSuaSVAD.place(x= 955,y = 70)
    
    lbNoteSuaSV = tk.Label(tabSV,text = 'Chú ý : sửa sinh viên thì không được bỏ trống trường nào',fg= 'red',font = ('Times New Roman',10))
    lbNoteSuaSV.place(x = 850,y = 400)
    
    def XoaSV():
        masv = txbMSVThem.get()
        if(masv ==""):
            messagebox.showinfo('Thông Báo', 'Không Được Bỏ Trống Các Trường')
        else:
            sql = f"delete from SinhVien where Msv = '{masv}'"
            mycursorAD.execute(sql)
            mydbAD.commit()
            messagebox.showinfo('Thông Báo','Xóa Thành Công')
            showSVAD()
        
    
    btnXoaSVAD = tk.Button(tabSV,text = 'Xóa',width = 12,font = ('Times New Roman',10),bg='#8fbc8f',command = XoaSV)
    btnXoaSVAD.place(x= 1060,y = 70)
    
    
    
    #xem lớp
    ShowDataLopAD = Listbox(tabLop,width = 90,height = 20)
    ShowDataLopAD.place(x = 20,y = 100)
    def showLopAD():
        sql = "select * from Lop"
        mycursorAD.execute(sql)
        result = mycursorAD.fetchall()
        arr = []
        arr.append("{:^10} {:^30} {:^50} {:^10} {:^10}".format('Mã Lớp','Tên Lớp','Sĩ Số','Mã Khoa','STT'))
        for i in result:
            #arr.append(f"{i[0]}     {i[1]}     {i[2]}     {i[3]}     {i[4]}     {i[5]}     {i[6]}")
            arr.append("{:^0}  {:^30}  {:^30}  {:^40}  {:^10}".format(i[0],i[1],i[2],i[3],i[4]))
        
        value = tk.Variable(value = arr)
        ShowDataLopAD['listvariable'] = value
    btnXemLopAD = tk.Button(tabLop,width = 12,text = 'Xem Lớp',font = ('Times New Roman',10),bg='#8fbc8f',command = showLopAD)
    btnXemLopAD.place(x = 30,y = 50)
    
    
    

    #thêm,sửa xóa Lop
    frameLop = tk.Frame(tabLop,bg = '#e6e6fa',bd = '2',width = 310,height = 300,highlightcolor = 'red')
    frameLop.place(x = 650,y = 100)
    
    ''' phần nhập mã Lớp '''
    
    lbMaLopThem = tk.Label(frameLop,text = 'Mã Lớp : ',font = ('Times New Roman',10))
    lbMaLopThem.place(x=10,y=10)
    txbMaLopThem = tk.Entry(frameLop,width = 20,font = ('Times New Roman',12))
    txbMaLopThem.place(x = 120,y = 10)
    
    
    ''' phần nhập tên lớp '''
    lbTenLopThem = tk.Label(frameLop,text = 'Tên Lớp : ',font = ('Times New Roman',10))
    lbTenLopThem.place(x=10,y=50)
    txbTenLopThem = tk.Entry(frameLop,width = 20,font = ('Times New Roman',12))
    txbTenLopThem.place(x = 120,y = 50)
    
    ''' phần nhập Sĩ số '''
    lbSiSoThem = tk.Label(frameLop,text = 'Sĩ Số : ',font = ('Times New Roman',10))
    lbSiSoThem.place(x=10,y=90)
    txbSiSoThem = tk.Entry(frameLop,width = 20,font = ('Times New Roman',12))
    txbSiSoThem.place(x = 120,y = 90)
    
    lbThemKhoaThem = tk.Label(frameLop,text = 'Mã Khoa : ',font = ('Times New Roman',10))
    lbThemKhoaThem.place(x=10,y=130)
    
    cbMaKhoaThem = Combobox(frameLop,width = 18,font = ('Times New Roman',12))
    mycursorAD.execute("select MaKhoa from Khoa")
    getMaKhoa = mycursorAD.fetchall()
    cbMaKhoaThem['value'] = [i[0] for i in getMaKhoa]
    cbMaKhoaThem.current(0)
    cbMaKhoaThem.place(x = 120,y = 130)
    
    def select_item_Lop(event):
        items = ShowDataLopAD.curselection()#chọn dòng được click
        #result = ','.join([items.get(i) for i in items])
        for i in items:
            txbMaLopThem.delete(0,len(txbMaLopThem.get()))
            txbTenLopThem.delete(0,len(txbTenLopThem.get()))
            txbSiSoThem.delete(0,len(txbSiSoThem.get()))
            if(i != 0):
                x = ShowDataLopAD.get(i).find(" ")
                ma_lop = ShowDataLopAD.get(i)[0:x]
                sql = f"select * from Lop where MaLop = '{ma_lop}'"
                mycursorAD.execute(sql)
                result = mycursorAD.fetchone()
                txbMaLopThem.insert(0, result[0])
                txbTenLopThem.insert(0, result[1])
                txbSiSoThem.insert(0, result[2])
                mk = f"select k.MaKhoa from Khoa k join Lop l\
                        on k.MaKhoa = l.MaKhoa\
                        where MaLop = '{ma_lop}'"
                mycursorAD.execute(mk)
                ma_khoa = mycursorAD.fetchone()
                cbMaKhoaThem.current(ma_khoa[0]-1)
            
            
        #result = ([ShowDataSinhVienAD.get(i) for i in items])
        #print(result)
        
    ShowDataLopAD.bind('<<ListboxSelect>>', select_item_Lop)
    
    
    def ThemLop():
        ma_lop = txbMaLopThem.get()
        ten_lop = txbTenLopThem.get()
        si_so = txbSiSoThem.get()
        ma_khoa = cbMaKhoaThem.get()
        sql = f"Call ThemMoiLop('{ma_lop}','{ten_lop}','{si_so}','{ma_khoa}')"
        mycursorAD.execute(sql)
        mydbAD.commit()
        messagebox.showerror('Thông Báo','Thêm Mới Thành Công')
        showLopAD()
        #show lớp mới ra mục mã lớp của sinh viên
        mycursorAD.execute("select MaLop from Lop")
        getTenLop = mycursorAD.fetchall()
        cbMaLopThem['value'] = [i[0] for i in getTenLop]
        
    btnThemLopAD = tk.Button(tabLop,text = 'Thêm',width = 12,font = ('Times New Roman',10),bg='#8fbc8f',command=ThemLop)
    btnThemLopAD.place(x= 650,y = 70)
    

    def SuaLop():
        ma_lop = txbMaLopThem.get()
        ten_lop = txbTenLopThem.get()
        si_so = txbSiSoThem.get()
        ma_khoa = cbMaKhoaThem.get()
        if(ma_lop == "" or ten_lop == "" or si_so == ""):
            messagebox.showerror("Thông Báo",'Không được bỏ trống trường nào trừ STT và Sĩ Số')
        else:
            mycursorAD.execute(f"update Lop set MaLop = '{ma_lop}',TenLop = '{ten_lop}',MaKhoa = {ma_khoa} where MaLop = '{ma_lop}'")
            mydbAD.commit()
            messagebox.showinfo('Thông Báo','Cập Nhật Thành Công')
            showLopAD()
            #show lớp mới ra mục mã lớp của sinh viên
            mycursorAD.execute("select MaLop from Lop")
            getTenLop = mycursorAD.fetchall()
            cbMaLopThem['value'] = [i[0] for i in getTenLop]
    btnSuaLopAD = tk.Button(tabLop,text = 'Sửa',width = 12,font = ('Times New Roman',10),bg='#8fbc8f',command = SuaLop)
    btnSuaLopAD.place(x= 750,y = 70)
    
    def XoaLop():
        ma_lop = txbMaLopThem.get()
        if(ma_lop != ""):
            sql = f"call XoaLop('{ma_lop}')"
            mycursorAD.execute(sql)
            mydbAD.commit()
            messagebox.showinfo('Thông Báo', 'Xóa Thành Công')
            showLopAD()
            #xóa đi lớp ở mục sinh viên
            mycursorAD.execute("select MaLop from Lop")
            getTenLop = mycursorAD.fetchall()
            cbMaLopThem['value'] = [i[0] for i in getTenLop]
        else:
            messagebox.showinfo('Thông Báo','Không Được Bỏ Trống Mã Lớp')
    btnXoaLopAD = tk.Button(tabLop,text = 'Xóa',width = 12,font = ('Times New Roman',10),bg='#8fbc8f',command = XoaLop)
    btnXoaLopAD.place(x= 850,y = 70)
    
    
    
    #xem Khoa
    

    
    ShowDataKhoaAD = Listbox(tabKhoa,width = 90,height = 20)
    ShowDataKhoaAD.place(x = 20,y = 100)
    
    def showKhoaAD():
        sql = "select * from Khoa"
        mycursorAD.execute(sql)
        result = mycursorAD.fetchall()
        arr = []
        arr.append("{:^10} {:^30} {:^30}".format('Mã Khoa','Tên Khoa','Trưởng Khoa'))
        for i in result:
            #arr.append(f"{i[0]}     {i[1]}     {i[2]}     {i[3]}     {i[4]}     {i[5]}     {i[6]}")
            arr.append("{:^0} {:^30} {:^30}".format(i[0],i[1],i[2]))
        
        value = tk.Variable(value = arr)
        ShowDataKhoaAD['listvariable'] = value
        

        
    btnXemKhoaAD = tk.Button(tabKhoa,width = 12,text = 'Xem Khoa',font = ('Times New Roman',10),bg='#8fbc8f',command = showKhoaAD)
    btnXemKhoaAD.place(x = 30,y = 50)
    #thêm,sửa xóa Khoa
    frameKhoa = tk.Frame(tabKhoa,bg = '#e6e6fa',bd = '2',width = 350,height = 320,highlightcolor = 'red')
    frameKhoa.place(x = 650,y = 100)
    
    ''' phần nhập mã Khoa '''
    lbMaKhoaThem = tk.Label(frameKhoa,text = 'Mã Khoa : ',font = ('Times New Roman',10))
    lbMaKhoaThem.place(x=10,y=10)
    txbMaKhoaThem = tk.Entry(frameKhoa,width = 25,font = ('Times New Roman',12))
    txbMaKhoaThem.place(x = 120,y = 10)
    
    
    ''' phần nhập tên Khoa '''
    lbTenKhoaThem = tk.Label(frameKhoa,text = 'Tên Khoa : ',font = ('Times New Roman',10))
    lbTenKhoaThem.place(x=10,y=50)
    txbTenKhoaThem = tk.Entry(frameKhoa,width = 25,font = ('Times New Roman',12))
    txbTenKhoaThem.place(x = 120,y = 50)
    
    ''' phần nhập Trưởng Khoa '''
    lbTruongKhoaThem = tk.Label(frameKhoa,text = 'Trưởng Khoa : ',font = ('Times New Roman',10))
    lbTruongKhoaThem.place(x=10,y=90)
    txbTruongKhoaThem = tk.Entry(frameKhoa,width = 25,font = ('Times New Roman',12))
    txbTruongKhoaThem.place(x = 120,y = 90)
    
    def select_item_Khoa(event):
        txbMaKhoaThem.delete(0,len(txbMaKhoaThem.get()))
        txbTenKhoaThem.delete(0,len(txbTenKhoaThem.get()))
        txbTruongKhoaThem.delete(0,len(txbTruongKhoaThem.get()))
        items = ShowDataKhoaAD.curselection() #chọn dòng click vào
        for i in items:
            ma_khoa = ShowDataKhoaAD.get(i)[0:1]
            sql = f'select * from Khoa where MaKhoa = {ma_khoa}'
            mycursorAD.execute(sql)
            result = mycursorAD.fetchone()
            ten_khoa = result[1]
            truong_khoa = result[2]
            txbMaKhoaThem.insert(0,ma_khoa)
            txbTenKhoaThem.insert(0,ten_khoa)
            txbTruongKhoaThem.insert(0,truong_khoa)
                
            
    ShowDataKhoaAD.bind('<<ListboxSelect>>',select_item_Khoa)
    
    
    def ThemKhoaAD():
        ma_khoa = txbMaKhoaThem.get()
        ten_khoa = txbTenKhoaThem.get()
        truong_khoa = txbTruongKhoaThem.get()
        
        sql = "insert into Khoa(MaKhoa,TenKhoa,TruongKhoa) values\
        (%s,%s,%s)"
        val = (ma_khoa,ten_khoa,truong_khoa)
        mycursorAD.execute(sql,val)
        mydbAD.commit()
        messagebox.showinfo('Thông Báo','Thêm Mới Thành Công')
        #cập nhật lại mã khoa ở mục lớp
        mycursorAD.execute("select MaKhoa from Khoa")
        getMaKhoa = mycursorAD.fetchall()
        cbMaKhoaThem['value'] = [i[0] for i in getMaKhoa]
    
    btnThemKhoaAD = tk.Button(tabKhoa,text = 'Thêm',width = 12,font = ('Times New Roman',10),bg='#8fbc8f',command = ThemKhoaAD)
    btnThemKhoaAD.place(x= 650,y = 70)
    
    def SuaKhoaAD():
        ma_khoa = txbMaKhoaThem.get()
        ten_khoa = txbTenKhoaThem.get()
        truong_khoa = txbTruongKhoaThem.get()
        if(ma_khoa != ""):
            sql = f"Update Khoa set TenKhoa = '{ten_khoa}',TruongKhoa = '{truong_khoa}' where MaKhoa = '{ma_khoa}'"
            mycursorAD.execute(sql)
            mydbAD.commit()
            messagebox.showinfo('Thông Báo', 'Cập Nhật Thành Công')
            showKhoaAD()
            #cập nhật lại mã khoa ở mục Lớp
            mycursorAD.execute("select MaKhoa from Khoa")
            getMaKhoa = mycursorAD.fetchall()
            cbMaKhoaThem['value'] = [i[0] for i in getMaKhoa]
    
    btnSuaKhoaAD = tk.Button(tabKhoa,text = 'Sửa',width = 12,font = ('Times New Roman',10),bg='#8fbc8f',command = SuaKhoaAD)
    btnSuaKhoaAD.place(x= 750,y = 70)
    
    def XoaKhoaAD():
        ma_khoa = txbMaKhoaThem.get()
        sql = f'call XoaKhoa({int(ma_khoa)})'
        mycursorAD.execute(sql)
        mydbAD.commit()
        messagebox.showinfo('Thông Báo','Xóa Thành Công')
    
    btnXoaKhoaAD = tk.Button(tabKhoa,text = 'Xóa',width = 12,font = ('Times New Roman',10),bg='#8fbc8f',command = XoaKhoaAD)
    btnXoaKhoaAD.place(x= 850,y = 70)
    
    
    
    #xem tài khoản
    ShowDataTaiKhoanAD = Listbox(tabTK,width = 35,height = 20,selectmode = tk.SINGLE)
    ShowDataTaiKhoanAD.place(x = 20,y = 100)
    def ShowTKAD():
        sql = "select * from TaiKhoan"
        mycursorAD.execute(sql)
        result = mycursorAD.fetchall()
        arr = []
        arr.append("{:^10} {:^30}".format('Tên Đăng Nhập','Mật Khẩu'))
        for i in result:
            #arr.append(f"{i[0]}     {i[1]}     {i[2]}     {i[3]}     {i[4]}     {i[5]}     {i[6]}")
            arr.append("{:^0} {:^50}".format(i[0],i[1]))
        
        value = tk.Variable(value = arr)
        ShowDataTaiKhoanAD['listvariable'] = value
        
    btnXemTKAD = tk.Button(tabTK,width = 12,text = 'Xem Tài Khoản',font = ('Times New Roman',10),bg='#8fbc8f',command = ShowTKAD)
    btnXemTKAD.place(x = 30,y = 50)
    

    #thêm,sửa xóa Tài Khoản
    frameTK = tk.Frame(tabTK,bg = '#e6e6fa',bd = '2',width = 310,height = 320,highlightcolor = 'red')
    frameTK.place(x = 350,y = 100)
    
    ''' phần nhập Tên Đăng nhập '''
    lbTDNThem = tk.Label(frameTK,text = 'Tên Đăng Nhập : ',font = ('Times New Roman',10))
    lbTDNThem.place(x=10,y=10)
    txbTDNThem = tk.Entry(frameTK,width = 20,font = ('Times New Roman',12))
    txbTDNThem.place(x = 120,y = 10)
    
    
    ''' phần nhập mật khẩu '''
    lbMatKhauThem = tk.Label(frameTK,text = 'Mật Khẩu : ',font = ('Times New Roman',10))
    lbMatKhauThem.place(x=10,y=50)
    txbMatKhauThem = tk.Entry(frameTK,width = 20,font = ('Times New Roman',12))
    txbMatKhauThem.place(x = 120,y = 50)
    
    

    def select_item_TK(event):
        txbMatKhauThem.delete(0,len(txbMatKhauThem.get()))
        txbTDNThem.delete(0,len(txbTDNThem.get()))
        items = ShowDataTaiKhoanAD.curselection()#lấy ra dữ liệu click
        for i in items:
            x = ShowDataTaiKhoanAD.get(i).find(" ")
            TDN = ShowDataTaiKhoanAD.get(i)[0:x]
            sql = f"select * from TaiKhoan where TenDN = '{TDN}'"
            mycursorAD.execute(sql)
            result = mycursorAD.fetchone()
            mat_khau = result[1]
            txbMatKhauThem.insert(0,mat_khau)
            txbTDNThem.insert(0,TDN)
            
    ShowDataTaiKhoanAD.bind('<<ListboxSelect>>',select_item_TK)
    
    def kiemTraMSVDK(ten_dn):
        sql = "select Msv from SinhVien"
        mycursorAD.execute(sql)
        result = mycursorAD.fetchall()
        count = 0
        for i in result:
            ten_dn = i[0];
            if(txbTDNThem.get() == ten_dn):
                count=count+1
        if(count == 1):
            return 1
    def kiemTraMSVTontai(ten_dn):
        sql = "select TenDN from TaiKhoan"
        mycursorAD.execute(sql)
        result = mycursorAD.fetchall()
        count = 0
        for i in result:
            ten_dn = i[0];
            if(txbTDNThem.get() == ten_dn):
                count=count+1
        if(count==0):
            return 1
    
    '''sự kiện click đăng ký '''
    def ThemTaiKhoan():
        tdn = txbTDNThem.get()
        if(kiemTraMSVDK(tdn) == 1 and kiemTraMSVTontai(tdn) == 1):
            sql = "insert into TaiKhoan(TenDN,MatKhau,LoaiTK) values (%s,%s,%s)"
            val = (txbTDNThem.get(),txbMatKhauThem.get(),1)
            mycursorAD.execute(sql,val)
            mydbAD.commit()
            messagebox.showinfo('Thông Báo', 'Thêm Thành Công')
            ShowDataTaiKhoanAD()
        else:
            messagebox.showerror('Thông Báo', "Tên Đăng Nhập Đã Tồn Tại Hoặc Mật Khẩu Chưa Hợp Lệ !") 
        
    btnThemTKAD = tk.Button(tabTK,text = 'Thêm',width = 12,font = ('Times New Roman',10),bg='#8fbc8f',command = ThemTaiKhoan)
    btnThemTKAD.place(x= 370,y = 70)
    
    
    
    def SuaTK():
        tdn = txbTDNThem.get()
        mk = txbMatKhauThem.get()
        
        if(kiemTraMSVTontai(tdn) != 1):        
            sql = f"update TaiKhoan set MatKhau = '{mk}' where TenDN = '{tdn}'"
            mycursorAD.execute(sql)
            mydbAD.commit()
            messagebox.showinfo('Thông Báo','Cập Nhật Thành Công')
            ShowDataTaiKhoanAD()
        else:
            messagebox.showerror('Thông báo','Tên Đăng Nhập Không Tồn Tại' )
    
    btnSuaTKAD = tk.Button(tabTK,text = 'Sửa',width = 12,font = ('Times New Roman',10),bg='#8fbc8f',command = SuaTK)
    btnSuaTKAD.place(x= 470,y = 70)
    
    def XoaTK():
        tdn = txbTDNThem.get()
        if(kiemTraMSVTontai(tdn) != 1):        
            sql = f"delete from TaiKhoan where TenDN = '{tdn}'"
            mycursorAD.execute(sql)
            mydbAD.commit()
            messagebox.showinfo('Thông Báo','Xóa Thành Công')
            ShowDataTaiKhoanAD()
        else:
            messagebox.showerror('Thông báo','Tên Đăng Nhập Không Tồn Tại' )
    
    btnXoaTKAD = tk.Button(tabTK,text = 'Xóa',width = 12,font = ('Times New Roman',10),bg='#8fbc8f',command = XoaTK)
    btnXoaTKAD.place(x= 570,y = 70)
    
    
    winAD.mainloop()

def main():
    administrator()
    
if (__name__=="__main__"):
    main()




















































