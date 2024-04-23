from cProfile import label
from cgitb import text
from fileinput import filename
import tkinter as tk
from tkinter import messagebox 
from tkinter import StringVar
from tkinter import *


window = tk.Tk()


class keluar:
    def keluar():
        
        
        exit(0)




def book():
    step = 1
    if len(stringnama.get()) == 0:
        messagebox.showerror("Error!!!","BELUM MENGISI NAMA ANDA")
        step = 0
    if len(stringalamat.get()) == 0:
        messagebox.showerror("Error!!!","BELUM MENGISI ALAMAT ANDA")
        step = 0
    if len(stringpekerjaan.get()) == 0:
        messagebox.showerror("Error!!!","BELUM MENGISI PEKERJAAN ANDA")
        step = 0
    if len(stringnomortelepon.get()) == 0:
        messagebox.showerror("Error!!!","BELUM MENGISI NOMOR TELEPON ANDA")
        step = 0
    if tujuan.get() == 0:
        messagebox.showerror("Eror!!!","BELUM MEMILIH JENIS MOBIL")
    if verifikasi.get() == 0:
        messagebox.showerror("EROR!!!","PASTIKAN TERLEBIH DAHULU SEBELUM MEMBELI")
    else:
        while step == 1:
            if tujuan.get()==1:
                harga="450.000.000"
                jenis="Fortuner 1GD 2.8 Diesel"
                
            elif tujuan.get()==2:
                harga="300.000.000"
                jenis="Innova Reborn Venturer 2.4 "
                
            elif tujuan.get()==3:
                harga="180.000.000"
                jenis="Avanza Veloz 1.5 "
              
            elif tujuan.get()==4:
                harga="158.000.000"  
                jenis="BRIO E Satya 1.2"

            elif tujuan.get()==5:
                harga="260.000.000"  
                jenis="City Hatchback 1.5 "
            
            elif tujuan.get()==6:
                harga="120.000.000"  
                jenis="Cayla 1.2"
           
            elif tujuan.get()==7:
                harga="500.000.000"
                jenis="HRV 1.5 TURBO RS "
                
            elif tujuan.get()==8:
                harga="245.000.000"
                jenis="Jazz 1.5 RS "
              
            elif tujuan.get()==9:
                harga="540.000.000"  
                jenis="Pajero Sport 2.4 DAKAR ULTIMATE "

            elif tujuan.get()==10:
                harga="475.000.000"  
                jenis="BMW 330i Msport 2000cc Turbo"
           
            elif tujuan.get()==11:
                harga="760.000.000"  
                jenis="Mercedes Benz C300 AMG Line"
           
            elif tujuan.get()==12:
                harga="1.100.000.000"  
                jenis="Alphard 2.4 Bensin G"


#Tampilan  
window.title("Miracle's Used Premium Cars Market ")
window.geometry("1500x700")
window.configure(bg="gray")



#label
label1 = tk.Label(bg="#FFCF45", text ="Miracle's Used Premium Cars Market").place(x=600, y=10)  
label2 = tk.Label(bg="#60acbd", text ="Pilih Mobil Yang Ingin Anda Beli\t:").place(x=600, y=170)
label3 = tk.Label(text = "Nama Pembeli").place(x=500, y=50)
label4 = tk.Label(text = "Alamat").place(x=500, y=80)
label5 = tk.Label(text = "Pekerjaan").place(x=500, y=110)
label6 = tk.Label(text = "Nomor telepon yang dihubungi").place(x=500, y=140)

#Jenis mobil 
tujuan  = IntVar()
button1 = Checkbutton(window, bg="#e9ffde", text="Fortuner 1GD 2.8 Diesel ", variable=tujuan, onvalue=1, offvalue=0).place(x=500, y=200)
button2 = Checkbutton(window, bg="#e9ffde", text="Innova Reborn Venturer 2.4 ", variable=tujuan, onvalue=2, offvalue=0).place(x=500, y=220)  
button3 = Checkbutton(window, bg="#e9ffde", text="Avanza Veloz 1.5 ", variable=tujuan, onvalue=3, offvalue=0).place(x=500, y=240)  
button4 = Checkbutton(window, bg="#e9ffde", text="BRIO E Satya 1.2 ", variable=tujuan, onvalue=4, offvalue=0).place(x=500, y=260)  
button5 = Checkbutton(window, bg="#e9ffde", text="City Hatchback 1.5 ", variable=tujuan, onvalue=5, offvalue=0).place(x=500, y=280) 
button6 = Checkbutton(window, bg="#e9ffde", text="Cayla 1.2", variable=tujuan, onvalue=6, offvalue=0).place(x=500, y=300) 
button7 = Checkbutton(window, bg="#e9ffde", text="HRV 1.5 TURBO RS ", variable=tujuan, onvalue=7, offvalue=0).place(x=800, y=200)  
button8 = Checkbutton(window, bg="#e9ffde", text="Jazz 1.5 RS ", variable=tujuan, onvalue=8, offvalue=0).place(x=800, y=220)  
button9 = Checkbutton(window, bg="#e9ffde", text="Pajero Sport 2.4 DAKAR ULTIMATE ", variable=tujuan, onvalue=9, offvalue=0).place(x=800, y=240)  
button10 = Checkbutton(window, bg="#e9ffde", text="BMW 330i Msport 2000cc Turbo ", variable=tujuan, onvalue=10, offvalue=0).place(x=800, y=260)  
button11 = Checkbutton(window, bg="#e9ffde", text="Mercedes Benz C300 AMG Line ", variable=tujuan, onvalue=11, offvalue=0).place(x=800, y=280) 
button12 = Checkbutton(window, bg="#e9ffde", text="Alphard 2.4 Bensin G", variable=tujuan, onvalue=12, offvalue=0).place(x=800, y=300) 

#Verifikasi
verifikasi = IntVar()
button1 = Checkbutton(window, bg="#60bd79", text="Verifikasi", variable=verifikasi, onvalue=1, offvalue=0).place(x=680, y=380)


    

#Nama pembeli 
stringnama = StringVar()
NAMA = Entry(width = 20, textvariable=stringnama).place(x = 600, y = 50) 

#Alamat
stringalamat = StringVar()
ALAMAT = Entry(width = 20, textvariable=stringalamat).place(x = 600, y = 80)

#Pekerjaan
stringpekerjaan= StringVar()
PEKERJAAN = Entry(width = 20, textvariable=stringpekerjaan).place(x = 600, y = 110)

#Nomor telepon
stringnomortelepon = StringVar()
NOMORTELEPON = Entry(width = 20, textvariable=stringnomortelepon).place(x = 700, y = 140)

#Tombol button bagian pesan dan keluar
button1 = Button(window, bg="yellow", command = book, text="PESAN").place(x=500,y=450)
exitbutton = Button(window, bg="#F05A3A", command = exit, text="KELUAR").place(x=870,y=450)



window.mainloop()