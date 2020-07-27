# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:16:39 2020

@author: Dezha Martha
"""

import threading

from fpdf import FPDF

#########################################################################################################
##################################### Data Pribadi ######################################################
#########################################################################################################

def nama(c):
    return("Nama Lengkap        : %s \n" %c)
    
def almt(n):
    return("Alamat Sekarang     : %s \n" %n)
    
def noKtp(w):
    return("No KTP       : %s \n" %w)
    
def noRek(z):
    return("No Rekening     : 09199%s \n" %z)
    
def noHp(k):
    return("No Handphone        : %s \n" %k)
    
def email(e):
    return ("Alamat E-mail               : %s \n" %e)

def jk():
    print("\n")
    print("-----Jenis Kelamin-----")
    print("[1] Laki - Laki")
    print("[2] Perempuan")
    j = int(input("Pilih Jenis Kelamin : "))
    if(j == 1):    
        return ("Laki-Laki")
    elif(j==2):    
        return ("Perempuan")
    else :    
        return ("Dipertanyakan")
    
def agama():
    print("\n")
    print("-----Agama-----")
    print("[1] Islam")
    print("[2] Kristen")
    print("[3] Hindu")
    print("[4] Budha")
    a = int(input("Pilih Agama : "))
    if(a == 1):   
        return ("Islam")
    elif(a == 2):   
        return ("Kristen")
    elif(a == 3):   
        return ("Hindu")
    elif(a == 4):   
        return ("Budha")
    else:   
        return ("Dipertanyakan")

#########################################################################################################
##################################### Data Bank ######################################################
#########################################################################################################
        
def gopay(gp):
    return("No go-Pay       : %s \n" %gp)
    
def saldo(s):
    return("Saldo       : %s \n" %s)

def jmlBayar(jb):
    return("Jumlah Bayar       : %s \n" %jb)
    
def sisa(s, jb):
    return (s - jb)

def ket(kt):
    return("Keterangan Pembayaran   : %s \n" %kt)
    
def reff(rf):
    return("Keterangan Transfer   : %s \n" %rf)
    
def noTujuan(nt):
    return("No Tujuan   : %s \n" %nt)
    
def jumlah(jl):
    return("Jumlah yang ditransfer   : %s \n" %jl)
#########################################################################################################
##################################### Fungsi menu ######################################################
#########################################################################################################
def menu():
    
    print("\n")
    print("Selamat Datang di web bank Indonesia")
    print("-----Silahkan pilih Bank berikut-----")
    print("[1] BRI")
    print("[2] BNI")
    print("[3] BCA")
    print("[4] Mandiri")
    print("[5] BJB")
    
    mnu = int(input("Pilih Jawaban : "))
    if(mnu == 1): 
        menu_bank_bri()
    elif(mnu == 2):      
        menu_bank_bni()
    elif(mnu == 3):      
        menu_bank_bca()
    elif(mnu == 4):      
        menu_bank_mandiri()
    elif(mnu == 5):      
        menu_bank_bjb()
    else:      
        return ("Mohon pilih salah satu Bank di atas!!! \n")


#########################################################################################################
##################################### Fungsi BANK BRI ######################################################
#########################################################################################################
        
def menu_bank_bri():
    
    print("\n")
    print("Selamat Datang di BANK BRI")
    print("-----Silahkan pilih menu berikut-----")
    print("[1] Buka Rekening Baru")
    print("[2] Top up Go-pay")
    print("[3] Transfer")
    print("[4] Kembali")
    
    mnu_bank = int(input("Pilih Jawaban : "))
    
    if(mnu_bank == 1): 
        menu1_bri()

    elif(mnu_bank == 2):      
        menu2_bri()
    
    elif(mnu_bank == 3):      
        menu3_bri()
        
    elif(mnu_bank == 4):      
        menu()
    else:      
        return ("Mohon pilih salah satu menu diatas !!! \n")

        
def menu1_bri():
    
        print("\n")
        print("---Untuk Membuat Rekening Baru Silahkan Isi data berikut---")
        print("\n")
        
        inama = input("Masukan Nama Anda     : ")

        ialmt = input("Alamat Sekarang        : ")
        
        inoKtp = input("No KTP        : ")
        
        inoHp = int(input("Masukan No HP Anda : "))

        iemail = input("Masukan Email Anda    : ")
        
        inoRek  = input("Masukkan 5 digit no Rekening sesuka anda : ")
        
        ijenke = jk()
        
        iagm = agama()
        
                
        nama(inama)

        almt(ialmt)

        noKtp(inoKtp)

        noRek(inoRek)

        noHp(inoHp)
      
        email(iemail)
        
        t1 = threading.Thread(target=rekening_bri,args=(inama,ialmt,inoKtp,inoRek,inoHp,ijenke,iemail,iagm))
        
        t2 = threading.Thread(target=rekening_bri_cli,args=(inama,ialmt,inoKtp,inoRek,inoHp,ijenke,iemail,iagm))
        
        cetak = input("Cetak atau Tidak (y/n)? ")
        if(cetak == 'y'):
            print("Bukti telah dicetak")
            t1.start()
            t2.start()
        elif(cetak == 'n'):        
            return ("Terima kasih telah membuat rekening di bank kami :)")
        else:
            return ("pilihan hanya y/n")
            
def menu2_bri():
    
        print("\n")
        print("-----------Top Up Go-Pay------------")
        print("\n")
            
        igopay = input("Masukkan no go-pay       : 03130 - ")
        
        iket = input("Masukkan keterangan    : ")
        
        isaldo = int(input("Saldo anda     : "))
        
        ijmlBayar = int(input("Jumlah dibayarkan     : "))
        
        gopay(igopay)
        
        ket(iket)
        
        saldo(isaldo)
        
        jmlBayar(ijmlBayar)
        
        t1 = threading.Thread(target=topup_bri_cli,args=(igopay,iket,isaldo,ijmlBayar))

        t2 = threading.Thread(target=topup_bri,args=(igopay,iket,isaldo,ijmlBayar))
        
        cetak = input("Cetak atau Tidak (y/n)? ")
        if(cetak == 'y'):
            print("Bukti telah dicetak")
            t2.start()
            t1.start()
        elif(cetak == 'n'):        
            return ("Terima kasih telah melakukan top up :)")
        else:
            return ("pilihan hanya y/n")
        
def menu3_bri():
    
        print("\n")
        print("-----------Tranfer-----------")
        print("Kode Bank")
        print("BRI = 021")
        print("BNI = 009")
        print("BCA = 022")
        print("BJB = 123")
        print("Mandiri = 892")
        print("\n")
        
        inoTujuan = input("Masukkan no Rek.Tujuan    : ")
        
        ijumlah = int(input("Jumlah     : "))
        
        ireff = input("Masukkan keterangan   : ")

        noTujuan(inoTujuan)
        
        jumlah(ijumlah)
        
        reff(ireff)
        
        t1 = threading.Thread(target=tf_bri_cli,args=(inoTujuan,ijumlah,ireff))
        
        t2 = threading.Thread(target=tf_bri,args=(inoTujuan,ijumlah,ireff))
        
        cetak = input("Cetak atau Tidak (y/n)? ")
        if(cetak == 'y'):
            print("Bukti telah dicetak")
            t1.start()
            t2.start()    
        elif(cetak == 'n'):        
            return ("Terima kasih telah melakukan top up :)")
        else:
            return ("pilihan hanya y/n")
        
def rekening_bri(c,n,w,z,k,e,jk,agm):
    name = nama(c)
    tempat = almt(n)
    noktp = noKtp(w)
    norekk = noRek(z)
    nohp = noHp(k)
    jenkel = jk
    Agama = agm
    eMail = email(e)

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Buat Rekening Baru", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Data Rekening Bank BRI", ln=3,align="L")
    pdf.cell(200,10,txt=name, ln=4,align="L")
    pdf.cell(200,10,txt=tempat, ln=4,align="L")
    pdf.cell(200,10,txt=noktp, ln=4,align="L")
    pdf.cell(200,10,txt=norekk, ln=4,align="L")
    pdf.cell(200,10,txt=nohp, ln=4,align="L")
    pdf.cell(200,10,txt="Jenis Kelamin          : "+jenkel, ln=4,align="L")
    pdf.cell(200,10,txt="Agama                     : "+Agama, ln=4,align="L")
    pdf.cell(200,10,txt=eMail, ln=4,align="L")
    pdf.output("rekbaru bri.pdf")

def rekening_bri_cli(c,n,w,z,k,e,jk,agm):
    name = nama(c)
    tempat = almt(n)
    noktp = noKtp(w)
    norekk = noRek(z)
    nohp = noHp(k)
    jenkel = jk
    Agama = agm
    eMail = email(e)

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Buat Rekening Baru", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Data Rekening Bank BRI", ln=3,align="L")
    pdf.cell(200,10,txt=name, ln=4,align="L")
    pdf.cell(200,10,txt=tempat, ln=4,align="L")
    pdf.cell(200,10,txt=noktp, ln=4,align="L")
    pdf.cell(200,10,txt=norekk, ln=4,align="L")
    pdf.cell(200,10,txt=nohp, ln=4,align="L")
    pdf.cell(200,10,txt="Jenis Kelamin          : "+jenkel, ln=4,align="L")
    pdf.cell(200,10,txt="Agama                     : "+Agama, ln=4,align="L")
    pdf.cell(200,10,txt=eMail, ln=4,align="L")
    hasil = name + tempat + noktp + norekk + nohp + jenkel + Agama + eMail
    print(hasil)
    
def topup_bri(gp,s,kt,jb):
    gofay = gopay(gp)
    sldo = saldo(s)
    kett = ket(kt)
    jbl = jmlBayar(jb)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Top-up Gopay BRI ", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=gofay, ln=4,align="L")
    pdf.cell(200,10,txt=sldo, ln=4,align="L")
    pdf.cell(200,10,txt=kett, ln=4,align="L")
    pdf.cell(200,10,txt=jbl, ln=4,align="L")
    pdf.output("top-up bri.pdf")
    
def topup_bri_cli(gp,s,kt,jb):
    gofay = gopay(gp)
    sldo = saldo(s)
    kett = ket(kt)
    jbl = jmlBayar(jb)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Top-up Gopay BRI ", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=gofay, ln=4,align="L")
    pdf.cell(200,10,txt=sldo, ln=4,align="L")
    pdf.cell(200,10,txt=kett, ln=4,align="L")
    pdf.cell(200,10,txt=jbl, ln=4,align="L")
    hasil = gofay + sldo + kett + jbl
    print(hasil)
    
def tf_bri(nt,rf,jl):
    nomorTj = noTujuan(nt)
    ref = reff(rf)
    jumlh = jumlah(jl)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Transfer Bank BRI", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=nomorTj, ln=4,align="L")
    pdf.cell(200,10,txt=ref, ln=4,align="L")
    pdf.cell(200,10,txt=jumlh, ln=4,align="L")
    pdf.output("transfer bri.pdf")
    
def tf_bri_cli(nt,rf,jl):
    nomorTj = noTujuan(nt)
    ref = reff(rf)
    jumlh = jumlah(jl)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Transfer Bank BRI", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=nomorTj, ln=4,align="L")
    pdf.cell(200,10,txt=ref, ln=4,align="L")
    pdf.cell(200,10,txt=jumlh, ln=4,align="L")
    hasil = nomorTj + ref + jumlh
    print(hasil)

#########################################################################################################
##################################### Fungsi BANK BNI ######################################################
#########################################################################################################
    
    
def menu_bank_bni():
    
    print("\n")
    print("Selamat Datang di BANK BNI")
    print("-----Silahkan pilih menu berikut-----")
    print("[1] Buka Rekening Baru")
    print("[2] Top up Go-pay")
    print("[3] Transfer")
    print("[4] Kembali")
    
    mnu_bank = int(input("Pilih Jawaban : "))
    
    if(mnu_bank == 1): 
        menu1_bni()

    elif(mnu_bank == 2):      
        menu2_bni()
    
    elif(mnu_bank == 3):      
        menu3_bni()
        
    elif(mnu_bank == 4):      
        menu()
    else:      
        return ("Mohon pilih salah satu menu diatas !!! \n")

        
def menu1_bni():
    
        print("\n")
        print("---Untuk Membuat Rekening Baru Silahkan Isi data berikut---")
        print("\n")
        
        inama = input("Masukan Nama Anda     : ")

        ialmt = input("Alamat Sekarang        : ")
        
        inoKtp = input("No KTP        : ")
        
        inoHp = int(input("Masukan No HP Anda : "))

        iemail = input("Masukan Email Anda    : ")
        
        inoRek  = input("Masukkan 5 digit no Rekening sesuka anda : ")
        
        ijenke = jk()
        
        iagm = agama()
        
                
        nama(inama)

        almt(ialmt)

        noKtp(inoKtp)

        noRek(inoRek)

        noHp(inoHp)
      
        email(iemail)
        
        t1 = threading.Thread(target=rekening_bni,args=(inama,ialmt,inoKtp,inoRek,inoHp,ijenke,iemail,iagm))
        
        t2 = threading.Thread(target=rekening_bni_cli,args=(inama,ialmt,inoKtp,inoRek,inoHp,ijenke,iemail,iagm))
        
        cetak = input("Cetak atau Tidak (y/n)? ")
        if(cetak == 'y'):
            print("Bukti telah dicetak")
            t1.start()    
            t2.start()
        elif(cetak == 'n'):        
            return ("Terima kasih telah membuat rekening di bank kami :)")
        else:
            return ("pilihan hanya y/n")
            
def menu2_bni():
    
        print("\n")
        print("-----------Top Up Go-Pay------------")
        print("\n")
            
        igopay = input("Masukkan no go-pay       : 910290 - ")
        
        iket = input("Masukkan keterangan    : ")
        
        isaldo = int(input("Saldo anda     : "))
        
        ijmlBayar = int(input("Jumlah dibayarkan     : "))
        
        gopay(igopay)
        
        ket(iket)
        
        saldo(isaldo)
        
        jmlBayar(ijmlBayar)
        
        t1 = threading.Thread(target=topup_bni_cli,args=(igopay,iket,isaldo,ijmlBayar))
        
        t2 = threading.Thread(target=topup_bni,args=(igopay,iket,isaldo,ijmlBayar))
        
        cetak = input("Cetak atau Tidak (y/n)? ")
        if(cetak == 'y'):
            print("Bukti telah dicetak")
            t1.start()
            t2.start()    
        elif(cetak == 'n'):        
            return ("Terima kasih telah melakukan top up :)")
        else:
            return ("pilihan hanya y/n")
        
def menu3_bni():
    
        print("\n")
        print("-----------Tranfer-----------")
        print("Kode Bank")
        print("BRI = 021")
        print("BNI = 009")
        print("BCA = 022")
        print("BJB = 123")
        print("Mandiri = 892")
        print("\n")
        
        inoTujuan = input("Masukkan no Rek.Tujuan    : ")
        
        ijumlah = int(input("Jumlah     : "))
        
        ireff = input("Masukkan keterangan   : ")

        noTujuan(inoTujuan)
        
        jumlah(ijumlah)
        
        reff(ireff)
        
        t1 = threading.Thread(target=tf_bni,args=(inoTujuan,ijumlah,ireff))
        
        t2 = threading.Thread(target=tf_bni_cli,args=(inoTujuan,ijumlah,ireff))
        
        cetak = input("Cetak atau Tidak (y/n)? ")
        if(cetak == 'y'):
            print("Bukti telah dicetak")
            t1.start()
            t2.start()
        elif(cetak == 'n'):        
            return ("Terima kasih telah melakukan top up :)")
        else:
            return ("pilihan hanya y/n")
        
def rekening_bni(c,n,w,z,k,e,jk,agm):
    name = nama(c)
    tempat = almt(n)
    noktp = noKtp(w)
    norekk = noRek(z)
    nohp = noHp(k)
    jenkel = jk
    Agama = agm
    eMail = email(e)

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Buat Rekening Baru", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Data Rekening Bank BNI", ln=3,align="L")
    pdf.cell(200,10,txt=name, ln=4,align="L")
    pdf.cell(200,10,txt=tempat, ln=4,align="L")
    pdf.cell(200,10,txt=noktp, ln=4,align="L")
    pdf.cell(200,10,txt=norekk, ln=4,align="L")
    pdf.cell(200,10,txt=nohp, ln=4,align="L")
    pdf.cell(200,10,txt="Jenis Kelamin          : "+jenkel, ln=4,align="L")
    pdf.cell(200,10,txt="Agama                     : "+Agama, ln=4,align="L")
    pdf.cell(200,10,txt=eMail, ln=4,align="L")
    pdf.output("rekbaru bni.pdf")
    
def rekening_bni_cli(c,n,w,z,k,e,jk,agm):
    name = nama(c)
    tempat = almt(n)
    noktp = noKtp(w)
    norekk = noRek(z)
    nohp = noHp(k)
    jenkel = jk
    Agama = agm
    eMail = email(e)

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Buat Rekening Baru", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Data Rekening Bank BNI", ln=3,align="L")
    pdf.cell(200,10,txt=name, ln=4,align="L")
    pdf.cell(200,10,txt=tempat, ln=4,align="L")
    pdf.cell(200,10,txt=noktp, ln=4,align="L")
    pdf.cell(200,10,txt=norekk, ln=4,align="L")
    pdf.cell(200,10,txt=nohp, ln=4,align="L")
    pdf.cell(200,10,txt="Jenis Kelamin          : "+jenkel, ln=4,align="L")
    pdf.cell(200,10,txt="Agama                     : "+Agama, ln=4,align="L")
    pdf.cell(200,10,txt=eMail, ln=4,align="L")
    hasil = name + tempat + noktp + norekk + nohp + jenkel + Agama + eMail
    print(hasil)
    
def topup_bni(gp,s,kt,jb):
    gofay = gopay(gp)
    sldo = saldo(s)
    kett = ket(kt)
    jbl = jmlBayar(jb)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Top-up Gopay BNI ", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=gofay, ln=4,align="L")
    pdf.cell(200,10,txt=sldo, ln=4,align="L")
    pdf.cell(200,10,txt=kett, ln=4,align="L")
    pdf.cell(200,10,txt=jbl, ln=4,align="L")
    pdf.output("top-up bni.pdf")
    
def topup_bni_cli(gp,s,kt,jb):
    gofay = gopay(gp)
    sldo = saldo(s)
    kett = ket(kt)
    jbl = jmlBayar(jb)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Top-up Gopay BNI ", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=gofay, ln=4,align="L")
    pdf.cell(200,10,txt=sldo, ln=4,align="L")
    pdf.cell(200,10,txt=kett, ln=4,align="L")
    pdf.cell(200,10,txt=jbl, ln=4,align="L")
    hasil = gofay + sldo + kett + jbl
    print(hasil)
    
def tf_bni(nt,rf,jl):
    nomorTj = noTujuan(nt)
    ref = reff(rf)
    jumlh = jumlah(jl)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Transfer Bank BNI", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=nomorTj, ln=4,align="L")
    pdf.cell(200,10,txt=ref, ln=4,align="L")
    pdf.cell(200,10,txt=jumlh, ln=4,align="L")
    pdf.output("transfer bni.pdf")
    
def tf_bni_cli(nt,rf,jl):
    nomorTj = noTujuan(nt)
    ref = reff(rf)
    jumlh = jumlah(jl)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Transfer Bank BNI", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=nomorTj, ln=4,align="L")
    pdf.cell(200,10,txt=ref, ln=4,align="L")
    pdf.cell(200,10,txt=jumlh, ln=4,align="L")
    hasil = nomorTj + ref + jumlh
    print(hasil)
    
#########################################################################################################
##################################### Fungsi BANK BCA ######################################################
#########################################################################################################
    
        
    
def menu_bank_bca():
    
    print("\n")
    print("Selamat Datang di BANK BCA")
    print("-----Silahkan pilih menu berikut-----")
    print("[1] Buka Rekening Baru")
    print("[2] Top up Go-pay")
    print("[3] Transfer")
    print("[4] Kembali")
    
    mnu_bank = int(input("Pilih Jawaban : "))
    
    if(mnu_bank == 1): 
        menu1_bca()

    elif(mnu_bank == 2):      
        menu2_bca()
    
    elif(mnu_bank == 3):      
        menu3_bca()
        
    elif(mnu_bank == 4):      
        menu()
    else:      
        return ("Mohon pilih salah satu menu diatas !!! \n")

        
def menu1_bca():
    
        print("\n")
        print("---Untuk Membuat Rekening Baru Silahkan Isi data berikut---")
        print("\n")
        
        inama = input("Masukan Nama Anda     : ")

        ialmt = input("Alamat Sekarang        : ")
        
        inoKtp = input("No KTP        : ")
        
        inoHp = int(input("Masukan No HP Anda : "))

        iemail = input("Masukan Email Anda    : ")
        
        inoRek  = input("Masukkan 5 digit no Rekening sesuka anda : ")
        
        ijenke = jk()
        
        iagm = agama()
        
                
        nama(inama)

        almt(ialmt)

        noKtp(inoKtp)

        noRek(inoRek)

        noHp(inoHp)
      
        email(iemail)
        
        t1 = threading.Thread(target=rekening_bca,args=(inama,ialmt,inoKtp,inoRek,inoHp,ijenke,iemail,iagm))
        
        t2 = threading.Thread(target=rekening_bca_cli,args=(inama,ialmt,inoKtp,inoRek,inoHp,ijenke,iemail,iagm))
        
        cetak = input("Cetak atau Tidak (y/n)? ")
        if(cetak == 'y'):
            print("Bukti telah dicetak")
            t1.start()  
            t2.start()
        elif(cetak == 'n'):        
            return ("Terima kasih telah membuat rekening di bank kami :)")
        else:
            return ("pilihan hanya y/n")
            
def menu2_bca():
    
        print("\n")
        print("-----------Top Up Go-Pay------------")
        print("\n")
            
        igopay = input("Masukkan no go-pay       : 910290 - ")
        
        iket = input("Masukkan keterangan    : ")
        
        isaldo = int(input("Saldo anda     : "))
        
        ijmlBayar = int(input("Jumlah dibayarkan     : "))
        
        gopay(igopay)
        
        ket(iket)
        
        saldo(isaldo)
        
        jmlBayar(ijmlBayar)
        
        t1 = threading.Thread(target=topup_bca,args=(igopay,iket,isaldo,ijmlBayar))
        
        t2 = threading.Thread(target=topup_bca_cli,args=(igopay,iket,isaldo,ijmlBayar))
        
        cetak = input("Cetak atau Tidak (y/n)? ")
        if(cetak == 'y'):
            print("Bukti telah dicetak")
            t1.start()
            t2.start()    
        elif(cetak == 'n'):        
            return ("Terima kasih telah melakukan top up :)")
        else:
            return ("pilihan hanya y/n")
        
def menu3_bca():
    
        print("\n")
        print("-----------Tranfer-----------")
        print("Kode Bank")
        print("BRI = 021")
        print("BNI = 009")
        print("BCA = 022")
        print("BJB = 123")
        print("Mandiri = 892")
        print("\n")
        
        inoTujuan = input("Masukkan no Rek.Tujuan    : ")
        
        ijumlah = int(input("Jumlah     : "))
        
        ireff = input("Masukkan keterangan   : ")

        noTujuan(inoTujuan)
        
        jumlah(ijumlah)
        
        reff(ireff)
        
        t1 = threading.Thread(target=tf_bca_cli,args=(inoTujuan,ijumlah,ireff))
        
        t3 = threading.Thread(target=tf_bca,args=(inoTujuan,ijumlah,ireff))
        
        cetak = input("Cetak atau Tidak (y/n)? ")
        if(cetak == 'y'):
            print("Bukti telah dicetak")
            t1.start()
            t3.start()    
        elif(cetak == 'n'):        
            return ("Terima kasih telah melakukan top up :)")
        else:
            return ("pilihan hanya y/n")
        
def rekening_bca(c,n,w,z,k,e,jk,agm):
    name = nama(c)
    tempat = almt(n)
    noktp = noKtp(w)
    norekk = noRek(z)
    nohp = noHp(k)
    jenkel = jk
    Agama = agm
    eMail = email(e)

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Buat Rekening Baru", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Data Rekening Bank BCA", ln=3,align="L")
    pdf.cell(200,10,txt=name, ln=4,align="L")
    pdf.cell(200,10,txt=tempat, ln=4,align="L")
    pdf.cell(200,10,txt=noktp, ln=4,align="L")
    pdf.cell(200,10,txt=norekk, ln=4,align="L")
    pdf.cell(200,10,txt=nohp, ln=4,align="L")
    pdf.cell(200,10,txt="Jenis Kelamin          : "+jenkel, ln=4,align="L")
    pdf.cell(200,10,txt="Agama                     : "+Agama, ln=4,align="L")
    pdf.cell(200,10,txt=eMail, ln=4,align="L")
    pdf.output("rekbaru bca.pdf")
    
def rekening_bca_cli(c,n,w,z,k,e,jk,agm):
    name = nama(c)
    tempat = almt(n)
    noktp = noKtp(w)
    norekk = noRek(z)
    nohp = noHp(k)
    jenkel = jk
    Agama = agm
    eMail = email(e)

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Buat Rekening Baru", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Data Rekening Bank BCA", ln=3,align="L")
    pdf.cell(200,10,txt=name, ln=4,align="L")
    pdf.cell(200,10,txt=tempat, ln=4,align="L")
    pdf.cell(200,10,txt=noktp, ln=4,align="L")
    pdf.cell(200,10,txt=norekk, ln=4,align="L")
    pdf.cell(200,10,txt=nohp, ln=4,align="L")
    pdf.cell(200,10,txt="Jenis Kelamin          : "+jenkel, ln=4,align="L")
    pdf.cell(200,10,txt="Agama                     : "+Agama, ln=4,align="L")
    pdf.cell(200,10,txt=eMail, ln=4,align="L")
    hasil = name + tempat + noktp + norekk + nohp + jenkel + Agama + eMail
    print(hasil)
    
def topup_bca(gp,s,kt,jb):
    gofay = gopay(gp)
    sldo = saldo(s)
    kett = ket(kt)
    jbl = jmlBayar(jb)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Top-up Gopay BCA ", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=gofay, ln=4,align="L")
    pdf.cell(200,10,txt=sldo, ln=4,align="L")
    pdf.cell(200,10,txt=kett, ln=4,align="L")
    pdf.cell(200,10,txt=jbl, ln=4,align="L")
    pdf.output("top-up bca.pdf")
    
def topup_bca_cli(gp,s,kt,jb):
    gofay = gopay(gp)
    sldo = saldo(s)
    kett = ket(kt)
    jbl = jmlBayar(jb)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Top-up Gopay BCA ", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=gofay, ln=4,align="L")
    pdf.cell(200,10,txt=sldo, ln=4,align="L")
    pdf.cell(200,10,txt=kett, ln=4,align="L")
    pdf.cell(200,10,txt=jbl, ln=4,align="L")
    hasil = gofay + sldo + kett + jbl
    print(hasil)
    
def tf_bca(nt,rf,jl):
    nomorTj = noTujuan(nt)
    ref = reff(rf)
    jumlh = jumlah(jl)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Transfer Bank BCA", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=nomorTj, ln=4,align="L")
    pdf.cell(200,10,txt=ref, ln=4,align="L")
    pdf.cell(200,10,txt=jumlh, ln=4,align="L")
    pdf.output("transfer bca.pdf")
    
def tf_bca_cli(nt,rf,jl):
    nomorTj = noTujuan(nt)
    ref = reff(rf)
    jumlh = jumlah(jl)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Transfer Bank BCA", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=nomorTj, ln=4,align="L")
    pdf.cell(200,10,txt=ref, ln=4,align="L")
    pdf.cell(200,10,txt=jumlh, ln=4,align="L")
    hasil = nomorTj + ref + jumlh
    print(hasil)
    
    #########################################################################################################
##################################### Fungsi BANK Mandiri ######################################################
#########################################################################################################
         
    
def menu_bank_mandiri():
    
    print("\n")
    print("Selamat Datang di BANK Mandiri")
    print("-----Silahkan pilih menu berikut-----")
    print("[1] Buka Rekening Baru")
    print("[2] Top up Go-pay")
    print("[3] Transfer")
    print("[4] Kembali")
    
    mnu_bank = int(input("Pilih Jawaban : "))
    
    if(mnu_bank == 1): 
        menu1_mandiri()

    elif(mnu_bank == 2):      
        menu2_mandiri()
    
    elif(mnu_bank == 3):      
        menu3_mandiri()
        
    elif(mnu_bank == 4):      
        menu()
    else:      
        return ("Mohon pilih salah satu menu diatas !!! \n")

        
def menu1_mandiri():
    
        print("\n")
        print("---Untuk Membuat Rekening Baru Silahkan Isi data berikut---")
        print("\n")
        
        inama = input("Masukan Nama Anda     : ")

        ialmt = input("Alamat Sekarang        : ")
        
        inoKtp = input("No KTP        : ")
        
        inoHp = int(input("Masukan No HP Anda : "))

        iemail = input("Masukan Email Anda    : ")
        
        inoRek  = input("Masukkan 5 digit no Rekening sesuka anda : ")
        
        ijenke = jk()
        
        iagm = agama()
        
                
        nama(inama)

        almt(ialmt)

        noKtp(inoKtp)

        noRek(inoRek)

        noHp(inoHp)
      
        email(iemail)
        
        t1 = threading.Thread(target=rekening_mandiri,args=(inama,ialmt,inoKtp,inoRek,inoHp,ijenke,iemail,iagm))
        
        t2 = threading.Thread(target=rekening_mandiri_cli,args=(inama,ialmt,inoKtp,inoRek,inoHp,ijenke,iemail,iagm))
        
        cetak = input("Cetak atau Tidak (y/n)? ")
        if(cetak == 'y'):
            print("Bukti telah dicetak")
            t1.start()    
            t2.start()
        elif(cetak == 'n'):        
            return ("Terima kasih telah membuat rekening di bank kami :)")
        else:
            return ("pilihan hanya y/n")
            
def menu2_mandiri():
    
        print("\n")
        print("-----------Top Up Go-Pay------------")
        print("\n")
            
        igopay = input("Masukkan no go-pay       : 001 - ")
        
        iket = input("Masukkan keterangan    : ")
        
        isaldo = int(input("Saldo anda     : "))
        
        ijmlBayar = int(input("Jumlah dibayarkan     : "))
        
        gopay(igopay)
        
        ket(iket)
        
        saldo(isaldo)
        
        jmlBayar(ijmlBayar)
        
        t1 = threading.Thread(target=topup_mandiri,args=(igopay,iket,isaldo,ijmlBayar))

        t2 = threading.Thread(target=topup_mandiri_cli,args=(igopay,iket,isaldo,ijmlBayar))
        
        cetak = input("Cetak atau Tidak (y/n)? ")
        if(cetak == 'y'):
            print("Bukti telah dicetak")
            t1.start()
            t2.start()    
        elif(cetak == 'n'):        
            return ("Terima kasih telah melakukan top up :)")
        else:
            return ("pilihan hanya y/n")
        
def menu3_mandiri():
    
        print("\n")
        print("-----------Tranfer-----------")
        print("Kode Bank")
        print("BRI = 021")
        print("BNI = 009")
        print("BCA = 022")
        print("BJB = 123")
        print("Mandiri = 892")
        print("\n")
        
        inoTujuan = input("Masukkan no Rek.Tujuan    : ")
        
        ijumlah = int(input("Jumlah     : "))
        
        ireff = input("Masukkan keterangan   : ")

        noTujuan(inoTujuan)
        
        jumlah(ijumlah)
        
        reff(ireff)
        
        t1 = threading.Thread(target=tf_mandiri,args=(inoTujuan,ijumlah,ireff))
        
        t2 = threading.Thread(target=tf_mandiri_cli,args=(inoTujuan,ijumlah,ireff))
        
        cetak = input("Cetak atau Tidak (y/n)? ")
        if(cetak == 'y'):
            print("Bukti telah dicetak")
            t1.start()
            t2.start()    
        elif(cetak == 'n'):        
            return ("Terima kasih telah melakukan top up :)")
        else:
            return ("pilihan hanya y/n")
        
def rekening_mandiri(c,n,w,z,k,e,jk,agm):
    name = nama(c)
    tempat = almt(n)
    noktp = noKtp(w)
    norekk = noRek(z)
    nohp = noHp(k)
    jenkel = jk
    Agama = agm
    eMail = email(e)

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Buat Rekening Baru", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Data Rekening Bank Mandiri", ln=3,align="L")
    pdf.cell(200,10,txt=name, ln=4,align="L")
    pdf.cell(200,10,txt=tempat, ln=4,align="L")
    pdf.cell(200,10,txt=noktp, ln=4,align="L")
    pdf.cell(200,10,txt=norekk, ln=4,align="L")
    pdf.cell(200,10,txt=nohp, ln=4,align="L")
    pdf.cell(200,10,txt="Jenis Kelamin          : "+jenkel, ln=4,align="L")
    pdf.cell(200,10,txt="Agama                     : "+Agama, ln=4,align="L")
    pdf.cell(200,10,txt=eMail, ln=4,align="L")
    pdf.output("rekbaru mandiri.pdf")
    
def rekening_mandiri_cli(c,n,w,z,k,e,jk,agm):
    name = nama(c)
    tempat = almt(n)
    noktp = noKtp(w)
    norekk = noRek(z)
    nohp = noHp(k)
    jenkel = jk
    Agama = agm
    eMail = email(e)

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Buat Rekening Baru", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Data Rekening Bank Mandiri", ln=3,align="L")
    pdf.cell(200,10,txt=name, ln=4,align="L")
    pdf.cell(200,10,txt=tempat, ln=4,align="L")
    pdf.cell(200,10,txt=noktp, ln=4,align="L")
    pdf.cell(200,10,txt=norekk, ln=4,align="L")
    pdf.cell(200,10,txt=nohp, ln=4,align="L")
    pdf.cell(200,10,txt="Jenis Kelamin          : "+jenkel, ln=4,align="L")
    pdf.cell(200,10,txt="Agama                     : "+Agama, ln=4,align="L")
    pdf.cell(200,10,txt=eMail, ln=4,align="L")
    hasil = name + tempat + noktp + norekk + nohp + jenkel + Agama + eMail
    print(hasil)
    
def topup_mandiri(gp,s,kt,jb):
    gofay = gopay(gp)
    sldo = saldo(s)
    kett = ket(kt)
    jbl = jmlBayar(jb)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Top-up Gopay Mandiri ", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=gofay, ln=4,align="L")
    pdf.cell(200,10,txt=sldo, ln=4,align="L")
    pdf.cell(200,10,txt=kett, ln=4,align="L")
    pdf.cell(200,10,txt=jbl, ln=4,align="L")
    pdf.output("top-up mandiri.pdf")
    
def topup_mandiri_cli(gp,s,kt,jb):
    gofay = gopay(gp)
    sldo = saldo(s)
    kett = ket(kt)
    jbl = jmlBayar(jb)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Top-up Gopay Mandiri ", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=gofay, ln=4,align="L")
    pdf.cell(200,10,txt=sldo, ln=4,align="L")
    pdf.cell(200,10,txt=kett, ln=4,align="L")
    pdf.cell(200,10,txt=jbl, ln=4,align="L")
    hasil = gofay + sldo + kett + jbl
    print(hasil)
    
def tf_mandiri(nt,rf,jl):
    nomorTj = noTujuan(nt)
    ref = reff(rf)
    jumlh = jumlah(jl)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Transfer Bank Mandiri", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=nomorTj, ln=4,align="L")
    pdf.cell(200,10,txt=ref, ln=4,align="L")
    pdf.cell(200,10,txt=jumlh, ln=4,align="L")
    pdf.output("transfer mandiri.pdf")
    
def tf_mandiri_cli(nt,rf,jl):
    nomorTj = noTujuan(nt)
    ref = reff(rf)
    jumlh = jumlah(jl)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Transfer Bank Mandiri", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=nomorTj, ln=4,align="L")
    pdf.cell(200,10,txt=ref, ln=4,align="L")
    pdf.cell(200,10,txt=jumlh, ln=4,align="L")
    hasil = nomorTj + ref + jumlh
    print(hasil)
    #########################################################################################################
##################################### Fungsi BANK BCA ######################################################
#########################################################################################################
    
        
    
def menu_bank_bjb():
    
    print("\n")
    print("Selamat Datang di BANK BJB")
    print("-----Silahkan pilih menu berikut-----")
    print("[1] Buka Rekening Baru")
    print("[2] Top up Go-pay")
    print("[3] Transfer")
    print("[4] Kembali")
    
    mnu_bank = int(input("Pilih Jawaban : "))
    
    if(mnu_bank == 1): 
        menu1_bjb()

    elif(mnu_bank == 2):      
        menu2_bjb()
    
    elif(mnu_bank == 3):      
        menu3_bjb()
        
    elif(mnu_bank == 4):      
        menu()
    else:      
        return ("Mohon pilih salah satu menu diatas !!! \n")

        
def menu1_bjb():
    
        print("\n")
        print("---Untuk Membuat Rekening Baru Silahkan Isi data berikut---")
        print("\n")
        
        inama = input("Masukan Nama Anda     : ")

        ialmt = input("Alamat Sekarang        : ")
        
        inoKtp = input("No KTP        : ")
        
        inoHp = int(input("Masukan No HP Anda : "))

        iemail = input("Masukan Email Anda    : ")
        
        inoRek  = input("Masukkan 5 digit no Rekening sesuka anda : ")
        
        ijenke = jk()
        
        iagm = agama()
        
                
        nama(inama)

        almt(ialmt)

        noKtp(inoKtp)

        noRek(inoRek)

        noHp(inoHp)
      
        email(iemail)
        
        t1 = threading.Thread(target=rekening_bjb,args=(inama,ialmt,inoKtp,inoRek,inoHp,ijenke,iemail,iagm))
        
        t2 = threading.Thread(target=rekening_bjb_cli,args=(inama,ialmt,inoKtp,inoRek,inoHp,ijenke,iemail,iagm))
        
        cetak = input("Cetak atau Tidak (y/n)? ")
        if(cetak == 'y'):
            print("Bukti telah dicetak")
            t1.start()
            t2.start()
        elif(cetak == 'n'):        
            return ("Terima kasih telah membuat rekening di bank kami :)")
        else:
            return ("pilihan hanya y/n")
            
def menu2_bjb():
    
        print("\n")
        print("-----------Top Up Go-Pay------------")
        print("\n")
            
        igopay = input("Masukkan no go-pay       : 123214 - ")
        
        iket = input("Masukkan keterangan    : ")
        
        isaldo = int(input("Saldo anda     : "))
        
        ijmlBayar = int(input("Jumlah dibayarkan     : "))
        
        gopay(igopay)
        
        ket(iket)
        
        saldo(isaldo)
        
        jmlBayar(ijmlBayar)
        
        t1 = threading.Thread(target=topup_bjb,args=(igopay,iket,isaldo,ijmlBayar))
        
        t2 = threading.Thread(target=topup_bjb_cli,args=(igopay,iket,isaldo,ijmlBayar))
        
        cetak = input("Cetak atau Tidak (y/n)? ")
        if(cetak == 'y'):
            print("Bukti telah dicetak")
            t1.start()
            t2.start()    
        elif(cetak == 'n'):        
            return ("Terima kasih telah melakukan top up :)")
        else:
            return ("pilihan hanya y/n")
        
def menu3_bjb():
    
        print("\n")
        print("-----------Tranfer-----------")
        print("Kode Bank")
        print("BRI = 021")
        print("BNI = 009")
        print("BCA = 022")
        print("BJB = 123")
        print("Mandiri = 892")
        print("\n")
        
        inoTujuan = input("Masukkan no Rek.Tujuan    : ")
        
        ijumlah = int(input("Jumlah     : "))
        
        ireff = input("Masukkan keterangan   : ")

        noTujuan(inoTujuan)
        
        jumlah(ijumlah)
        
        reff(ireff)
        
        t1 = threading.Thread(target=tf_bjb,args=(inoTujuan,ijumlah,ireff))
        
        t2 = threading.Thread(target=tf_bjb_cli,args=(inoTujuan,ijumlah,ireff))
        
        cetak = input("Cetak atau Tidak (y/n)? ")
        if(cetak == 'y'):
            print("Bukti telah dicetak")
            t1.start()
            t2.start()    
        elif(cetak == 'n'):        
            return ("Terima kasih telah melakukan top up :)")
        else:
            return ("pilihan hanya y/n")
        
def rekening_bjb(c,n,w,z,k,e,jk,agm):
    name = nama(c)
    tempat = almt(n)
    noktp = noKtp(w)
    norekk = noRek(z)
    nohp = noHp(k)
    jenkel = jk
    Agama = agm
    eMail = email(e)

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Buat Rekening Baru", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Data Rekening Bank BJB", ln=3,align="L")
    pdf.cell(200,10,txt=name, ln=4,align="L")
    pdf.cell(200,10,txt=tempat, ln=4,align="L")
    pdf.cell(200,10,txt=noktp, ln=4,align="L")
    pdf.cell(200,10,txt=norekk, ln=4,align="L")
    pdf.cell(200,10,txt=nohp, ln=4,align="L")
    pdf.cell(200,10,txt="Jenis Kelamin          : "+jenkel, ln=4,align="L")
    pdf.cell(200,10,txt="Agama                     : "+Agama, ln=4,align="L")
    pdf.cell(200,10,txt=eMail, ln=4,align="L")
    pdf.output("rekbaru bjb.pdf")
    
def rekening_bjb_cli(c,n,w,z,k,e,jk,agm):
    name = nama(c)
    tempat = almt(n)
    noktp = noKtp(w)
    norekk = noRek(z)
    nohp = noHp(k)
    jenkel = jk
    Agama = agm
    eMail = email(e)

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Buat Rekening Baru", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Data Rekening Bank BJB", ln=3,align="L")
    pdf.cell(200,10,txt=name, ln=4,align="L")
    pdf.cell(200,10,txt=tempat, ln=4,align="L")
    pdf.cell(200,10,txt=noktp, ln=4,align="L")
    pdf.cell(200,10,txt=norekk, ln=4,align="L")
    pdf.cell(200,10,txt=nohp, ln=4,align="L")
    pdf.cell(200,10,txt="Jenis Kelamin          : "+jenkel, ln=4,align="L")
    pdf.cell(200,10,txt="Agama                     : "+Agama, ln=4,align="L")
    pdf.cell(200,10,txt=eMail, ln=4,align="L")
    hasil = name + tempat + noktp + norekk + nohp + jenkel + Agama + eMail
    print(hasil)
    
def topup_bjb(gp,s,kt,jb):
    gofay = gopay(gp)
    sldo = saldo(s)
    kett = ket(kt)
    jbl = jmlBayar(jb)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Top-up Gopay BJB ", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=gofay, ln=4,align="L")
    pdf.cell(200,10,txt=sldo, ln=4,align="L")
    pdf.cell(200,10,txt=kett, ln=4,align="L")
    pdf.cell(200,10,txt=jbl, ln=4,align="L")
    pdf.output("top-up bjb.pdf")
    
def topup_bjb_cli(gp,s,kt,jb):
    gofay = gopay(gp)
    sldo = saldo(s)
    kett = ket(kt)
    jbl = jmlBayar(jb)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Top-up Gopay BJB ", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=gofay, ln=4,align="L")
    pdf.cell(200,10,txt=sldo, ln=4,align="L")
    pdf.cell(200,10,txt=kett, ln=4,align="L")
    pdf.cell(200,10,txt=jbl, ln=4,align="L")
    hasil = gofay + sldo + kett + jbl
    print(hasil)
    
def tf_bjb(nt,rf,jl):
    nomorTj = noTujuan(nt)
    ref = reff(rf)
    jumlh = jumlah(jl)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Transfer Bank BJB", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=nomorTj, ln=4,align="L")
    pdf.cell(200,10,txt=ref, ln=4,align="L")
    pdf.cell(200,10,txt=jumlh, ln=4,align="L")
    pdf.output("transfer bjb.pdf")
   
def tf_bjb_cli(nt,rf,jl):
    nomorTj = noTujuan(nt)
    ref = reff(rf)
    jumlh = jumlah(jl)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Transfer Bank BJB", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=nomorTj, ln=4,align="L")
    pdf.cell(200,10,txt=ref, ln=4,align="L")
    pdf.cell(200,10,txt=jumlh, ln=4,align="L")
    hasil = nomorTj + ref + jumlh
    print(hasil)
    
menu()

        

        



  

