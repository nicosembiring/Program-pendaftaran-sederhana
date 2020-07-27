# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:39:04 2020

@author: Nico Sembiring
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
    
def tglLahir(w):
    return("Tanggal Lahir      : %s \n" %w)
    
def noNisn(z):
    return("No NISN     : %s \n" %z)
    
def noHp(k):
    return("No Handphone        : %s \n" %k)
    
def email(e):
    return ("Alamat E-mail               : %s \n" %e)

def sde(sd):
    return ("Sekolah Dasar               : %s \n" %sd)

def smpe(smp):
    return ("Sekolah Menengah Pertama               : %s \n" %smp)

def esma(sma):
    return ("Sekolah Menengah Atas               : %s \n" %sma)

def tptLahir(p):
    return ("Tempat Lahir               : %s \n" %p)

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
    
def bayar(by):
    return("Bayar      : %s \n" %by)
    
def angka(ak):
    return("Nominal      : %s \n" %ak)

def jmlBayar(jb):
    return("Jumlah Bayar       : %s \n" %jb)

def ket(kt):
    return("Keterangan Pembayaran   : %s \n" %kt)   
#########################################################################################################
##################################### Data Kampus ######################################################
#########################################################################################################  
    

def jurusan():
    print("\n")
    print("-----Jurusan-----")
    print("[1] Teknik")
    print("[2] Manajemen")
    print("[3] Ekonomi")
    print("[4] Sastra")
    a = int(input("Pilih Jurusan : "))
    if(a == 1):   
        return ("Teknik")
    elif(a == 2):   
        return ("Manajemen")
    elif(a == 3):   
        return ("Ekonomi")
    elif(a == 4):   
        return ("Sastra")
    else:   
        return ("Pilih Salah Satu")
 #########################################################################################################
##################################### Fungsi menu ######################################################
#########################################################################################################  
def menu():
    
    print("\n")
    print("Selamat Datang di Sistem Pendaftaran Online Perguruan Tinggi Negeri")
    print("-----Silahkan pilih Perguruan Tinggi Negeri-----")
    print("[1] Universitas Indonesia")
    print("[2] Institut Teknologi Bandung")
    print("[3] Universitas Gajah Mada")
    print("[4] Universitas Diponegoro")
    print("[5] Universitas Pendidikan Indonesia")
    print("[6] Universitas Padjajaran")
    print("[7] Universitas Brawijaya")
    print("[8] Universitas Negeri Malang")
    
    mnu = int(input("Pilih Jawaban : "))
    if(mnu == 1): 
        menu_ui()
    elif(mnu == 2):      
        menu_itb()
    elif(mnu == 3):      
        menu_ugm()
    elif(mnu == 4):      
        menu_undip()
    elif(mnu == 5):      
        menu_upi()
    elif(mnu == 6):      
        menu_unpad()
    elif(mnu == 7):      
        menu_unibraw()
    elif(mnu == 8):      
        menu_unm()
    else:      
        return ("Mohon pilih salah satu Kampus di atas!!! \n")
#########################################################################################################
##################################### Fungsi UI ######################################################
#########################################################################################################
        
def menu_ui():
    
    print("\n")
    print("Selamat Datang di Universitas Indonesia")
    print("-----Silahkan pilih menu berikut-----")
    print("[1] Pendaftaran")
    print("[2] Pembayaran")
    print("[3] Cek Kelulusan")
    print("[4] Kembali")
    
    mnu_kps_ui = int(input("Pilih Jawaban : "))
    
    if(mnu_kps_ui == 1): 
        menu1_ui()

    elif(mnu_kps_ui == 2):      
        menu2_ui()
    
    elif(mnu_kps_ui == 3):      
        menu3_ui()
        
    elif(mnu_kps_ui == 4):      
        menu()
    else:      
        return ("Mohon pilih salah satu menu diatas !!! \n")    

def menu1_ui():
    
        print("\n")
        print("---Untuk Melakukan Pendaftaran, Silahkan Isi data berikut---")
        print("\n")
        
        namai = input("Masukan Nama Anda     : ")
        
        tmpti = input("Masukan Tempat Lahir Anda     : ")
        
        tgli = input("Masukan Tanggal Lahir Anda     : ")

        almti = input("Alamat Sekarang        : ")
        
        noNisni = input("No NISN        : ")
        
        noHpi = int(input("Masukan No HP Anda : "))

        emaili = input("Masukan Email Anda    : ")
        
        jenkei = jk()
        
        agmi = agama()
        
        sdi  = input("Masukkan Nama Sekolah Dasar : ")
        
        smpi  = input("Masukkan Nama Sekolah Menengah Pertama : ")
        
        smai  = input("Masukkan Nama Sekolah menengah Atas : ")
        
        juri = jurusan()
        
        nama(namai)
        
        tptLahir(tmpti)
        
        tglLahir(tgli)

        almt(almti)
        
        noNisn(noNisni)
        
        noHp(noHpi)
        
        email(emaili)
        
        sde(sdi)
        
        smpe(smpi)
        
        esma(smai)

        
        t1 = threading.Thread(target=daftar_ui,args=(namai,tmpti,tgli,almti,noNisni,noHpi,emaili,jenkei,agmi,sdi,smpi,smai,juri))
        
        t2 = threading.Thread(target=daftar_ui_cli,args=(namai,tmpti,tgli,almti,noNisni,noHpi,emaili,jenkei,agmi,sdi,smpi,smai,juri))
        
        cetak = input("Cetak Bukti Pendaftaran (y/n)? ")
        if(cetak == 'y'):
            print("Bukti Pendaftaran telah dicetak")
            t1.start()  
            t2.start()
        elif(cetak == 'n'):        
            return ("Terima kasih telah Mendaftar UI :)")
        else:
            return ("pilihan hanya y/n")
        
def menu2_ui():
    
        print("\n")
        print("-----------Bukti Pembayaran------------")
        print("\n")
            
        ibayar = input("Masukkan no rekening panitia       : 03130 - ")
        
        iket = input("Masukkan keterangan    : ")
        
        iangka = int(input("Jumlah Nominal     : "))
        
        ijmlBayar = input("Jumlah Dibayarkan     : ")
        
        bayar(ibayar)
        
        ket(iket)
        
        angka(iangka)
        
        jmlBayar(ijmlBayar)
        
        t1 = threading.Thread(target=pembayaran_ui,args=(ibayar,iket,iangka,ijmlBayar))

        t2 = threading.Thread(target=pembayaran_ui_cli,args=(ibayar,iket,iangka,ijmlBayar))
        
        cetak = input("Cetak bukti pembayaran (y/n)? ")
        if(cetak == 'y'):
            print("Bukti telah dicetak")
            t1.start()
            t2.start()    
        elif(cetak == 'n'):        
            return ("Terima kasih telah melakukan Pembayaran :)")
        else:
            return ("pilihan hanya y/n")
        
def menu3_ui():
    print("\n")
    print("-----------Hasil Kelulusan diumumkan pada 18 Juli 2020------------")
    print("\n")
    
def daftar_ui(c,p,w,n,z,k,e,jk,agm,sd,smp,sma,jur):
    name = nama(c)
    tptlhr =  tptLahir(p)
    tgllhr = tglLahir(w)
    alm = almt(n)
    nisn = noNisn(z)
    hp = noHp(k)
    eMail = email(e)
    jenkel = jk
    Agama = agm
    esde = sde(sd)
    esempe = smpe(smp)
    esema = esma(sma)
    jurs = jur

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pendaftaran Mahasiswa Baru UI", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Data Pendaftar", ln=3,align="L")
    pdf.cell(200,10,txt=name, ln=4,align="L")
    pdf.cell(200,10,txt=tptlhr, ln=4,align="L")
    pdf.cell(200,10,txt=tgllhr, ln=4,align="L")
    pdf.cell(200,10,txt=alm, ln=4,align="L")
    pdf.cell(200,10,txt=nisn, ln=4,align="L")
    pdf.cell(200,10,txt=hp, ln=4,align="L")
    pdf.cell(200,10,txt=eMail, ln=4,align="L")
    pdf.cell(200,10,txt="Jenis Kelamin          : "+jenkel, ln=4,align="L")
    pdf.cell(200,10,txt="Agama                     : "+Agama, ln=4,align="L")
    pdf.cell(200,10,txt=esde, ln=4,align="L")
    pdf.cell(200,10,txt=esempe, ln=4,align="L")
    pdf.cell(200,10,txt=esema, ln=4,align="L")
    pdf.cell(200,10,txt="Jurusan                     : "+jurs, ln=4,align="L")
    pdf.output("Bukti Pendaftaran UI.pdf")
    
def daftar_ui_cli(c,p,w,n,z,k,e,jk,agm,sd,smp,sma,jur):
    name = nama(c)
    tptlhr =  tptLahir(p)
    tgllhr = tglLahir(w)
    alm = almt(n)
    nisn = noNisn(z)
    hp = noHp(k)
    eMail = email(e)
    jenkel = jk
    Agama = agm
    esde = sde(sd)
    esempe = smpe(smp)
    esema = esma(sma)
    jurs = jur

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pendaftaran Mahasiswa Baru UI", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Data Pendaftar", ln=3,align="L")
    pdf.cell(200,10,txt=name, ln=4,align="L")
    pdf.cell(200,10,txt=tptlhr, ln=4,align="L")
    pdf.cell(200,10,txt=tgllhr, ln=4,align="L")
    pdf.cell(200,10,txt=alm, ln=4,align="L")
    pdf.cell(200,10,txt=nisn, ln=4,align="L")
    pdf.cell(200,10,txt=hp, ln=4,align="L")
    pdf.cell(200,10,txt=eMail, ln=4,align="L")
    pdf.cell(200,10,txt="Jenis Kelamin          : "+jenkel, ln=4,align="L")
    pdf.cell(200,10,txt="Agama                     : "+Agama, ln=4,align="L")
    pdf.cell(200,10,txt=esde, ln=4,align="L")
    pdf.cell(200,10,txt=esempe, ln=4,align="L")
    pdf.cell(200,10,txt=esema, ln=4,align="L")
    pdf.cell(200,10,txt="Jurusan                     : "+jurs, ln=4,align="L")
    hasil = name + tptlhr + tgllhr + alm + nisn + hp + eMail + jenkel + Agama + esde + esempe + esema + jurs
    print(hasil)
    
def pembayaran_ui(by,kt,ak,jb):
    bayars = bayar(by)
    kett = ket(kt)
    agk = angka(ak)
    jbl = jmlBayar(jb)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pembayaran ", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=bayars, ln=4,align="L")
    pdf.cell(200,10,txt=kett, ln=4,align="L")
    pdf.cell(200,10,txt=agk, ln=4,align="L")
    pdf.cell(200,10,txt=jbl, ln=4,align="L")
    pdf.output("Bukti Pembayaran UI.pdf")

def pembayaran_ui_cli(by,kt,ak,jb):
    bayars = bayar(by)
    kett = ket(kt)
    agk = angka(ak)
    jbl = jmlBayar(jb)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pembayaran ", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=bayars, ln=4,align="L")
    pdf.cell(200,10,txt=kett, ln=4,align="L")
    pdf.cell(200,10,txt=agk, ln=4,align="L")
    pdf.cell(200,10,txt=jbl, ln=4,align="L")
    hasil = bayars + kett + agk + jbl
    print(hasil)
    
#########################################################################################################
##################################### Fungsi Institut Teknologi Bandung ######################################################
#########################################################################################################

def menu_itb():
    
    print("\n")
    print("Selamat Datang di Institut Teknologi Bandung")
    print("-----Silahkan pilih menu berikut-----")
    print("[1] Pendaftaran")
    print("[2] Pembayaran")
    print("[3] Cek Kelulusan")
    print("[4] Kembali")
    
    mnu_kps_itb = int(input("Pilih Jawaban : "))
    
    if(mnu_kps_itb == 1): 
        menu1_itb()

    elif(mnu_kps_itb == 2):      
        menu2_itb()
    
    elif(mnu_kps_itb == 3):      
        menu3_itb()
        
    elif(mnu_kps_itb == 4):      
        menu()
    else:      
        return ("Mohon pilih salah satu menu diatas !!! \n")    

def menu1_itb():
    
        print("\n")
        print("---Untuk Melakukan Pendaftaran, Silahkan Isi data berikut---")
        print("\n")
        
        namai = input("Masukan Nama Anda     : ")
        
        tmpti = input("Masukan Tempat Lahir Anda     : ")
        
        tgli = input("Masukan Tanggal Lahir Anda     : ")

        almti = input("Alamat Sekarang        : ")
        
        noNisni = input("No NISN        : ")
        
        noHpi = int(input("Masukan No HP Anda : "))

        emaili = input("Masukan Email Anda    : ")
        
        jenkei = jk()
        
        agmi = agama()
        
        sdi  = input("Masukkan Nama Sekolah Dasar : ")
        
        smpi  = input("Masukkan Nama Sekolah Menengah Pertama : ")
        
        smai  = input("Masukkan Nama Sekolah menengah Atas : ")
        
        juri = jurusan()
        
        nama(namai)
        
        tptLahir(tmpti)
        
        tglLahir(tgli)

        almt(almti)
        
        noNisn(noNisni)
        
        noHp(noHpi)
        
        email(emaili)
        
        sde(sdi)
        
        smpe(smpi)
        
        esma(smai)

        
        t1 = threading.Thread(target=daftar_itb,args=(namai,tmpti,tgli,almti,noNisni,noHpi,emaili,jenkei,agmi,sdi,smpi,smai,juri))
        
        t2 = threading.Thread(target=daftar_itb_cli,args=(namai,tmpti,tgli,almti,noNisni,noHpi,emaili,jenkei,agmi,sdi,smpi,smai,juri))

        cetak = input("Cetak Bukti Pendaftaran (y/n)? ")
        if(cetak == 'y'):
            print("Bukti Pendaftaran telah dicetak")
            t1.start()    
            t2.start()
        elif(cetak == 'n'):        
            return ("Terima kasih telah Mendaftar ITB :)")
        else:
            return ("pilihan hanya y/n")
        
def menu2_itb():
    
        print("\n")
        print("-----------Bukti Pembayaran------------")
        print("\n")
            
        ibayar = input("Masukkan no rekening panitia       : 03130 - ")
        
        iket = input("Masukkan keterangan    : ")
        
        iangka = int(input("Jumlah Nominal     : "))
        
        ijmlBayar = input("Jumlah Dibayarkan     : ")
        
        bayar(ibayar)
        
        ket(iket)
        
        angka(iangka)
        
        jmlBayar(ijmlBayar)
        
        t1 = threading.Thread(target=pembayaran_itb,args=(ibayar,iket,iangka,ijmlBayar))

        t2 = threading.Thread(target=pembayaran_itb_cli,args=(ibayar,iket,iangka,ijmlBayar))
        
        cetak = input("Cetak bukti pembayaran (y/n)? ")
        if(cetak == 'y'):
            print("Bukti telah dicetak")
            t1.start()
            t2.start()    
        elif(cetak == 'n'):        
            return ("Terima kasih telah melakukan Pembayaran :)")
        else:
            return ("pilihan hanya y/n")
        
def menu3_itb():
    print("\n")
    print("-----------Hasil Kelulusan diumumkan pada 18 Juli 2020------------")
    print("\n")
    
def daftar_itb(c,n,w,z,k,e,jk,agm,sd,smp,sma,p,jur):
    name = nama(c)
    tptlhr =  tptLahir(p)
    tgllhr = tglLahir(w)
    alm = almt(n)
    nisn = noNisn(z)
    hp = noHp(k)
    eMail = email(e)
    jenkel = jk
    Agama = agm
    esde = sde(sd)
    esempe = smpe(smp)
    esema = esma(sma)
    jurs = jur

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pendaftaran Mahasiswa Baru ITB", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Data Pendaftar", ln=3,align="L")
    pdf.cell(200,10,txt=name, ln=4,align="L")
    pdf.cell(200,10,txt=tptlhr, ln=4,align="L")
    pdf.cell(200,10,txt=tgllhr, ln=4,align="L")
    pdf.cell(200,10,txt=alm, ln=4,align="L")
    pdf.cell(200,10,txt=nisn, ln=4,align="L")
    pdf.cell(200,10,txt=hp, ln=4,align="L")
    pdf.cell(200,10,txt=eMail, ln=4,align="L")
    pdf.cell(200,10,txt="Jenis Kelamin          : "+jenkel, ln=4,align="L")
    pdf.cell(200,10,txt="Agama                     : "+Agama, ln=4,align="L")
    pdf.cell(200,10,txt=esde, ln=4,align="L")
    pdf.cell(200,10,txt=esempe, ln=4,align="L")
    pdf.cell(200,10,txt=esema, ln=4,align="L")
    pdf.cell(200,10,txt="Jurusan                     : "+jurs, ln=4,align="L")
    pdf.output("Bukti Pendaftaran ITB.pdf")
    
def daftar_itb_cli(c,n,w,z,k,e,jk,agm,sd,smp,sma,p,jur):
    name = nama(c)
    tptlhr =  tptLahir(p)
    tgllhr = tglLahir(w)
    alm = almt(n)
    nisn = noNisn(z)
    hp = noHp(k)
    eMail = email(e)
    jenkel = jk
    Agama = agm
    esde = sde(sd)
    esempe = smpe(smp)
    esema = esma(sma)
    jurs = jur

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pendaftaran Mahasiswa Baru ITB", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Data Pendaftar", ln=3,align="L")
    pdf.cell(200,10,txt=name, ln=4,align="L")
    pdf.cell(200,10,txt=tptlhr, ln=4,align="L")
    pdf.cell(200,10,txt=tgllhr, ln=4,align="L")
    pdf.cell(200,10,txt=alm, ln=4,align="L")
    pdf.cell(200,10,txt=nisn, ln=4,align="L")
    pdf.cell(200,10,txt=hp, ln=4,align="L")
    pdf.cell(200,10,txt=eMail, ln=4,align="L")
    pdf.cell(200,10,txt="Jenis Kelamin          : "+jenkel, ln=4,align="L")
    pdf.cell(200,10,txt="Agama                     : "+Agama, ln=4,align="L")
    pdf.cell(200,10,txt=esde, ln=4,align="L")
    pdf.cell(200,10,txt=esempe, ln=4,align="L")
    pdf.cell(200,10,txt=esema, ln=4,align="L")
    pdf.cell(200,10,txt="Jurusan                     : "+jurs, ln=4,align="L")
    hasil = name + tptlhr + tgllhr + alm + nisn + hp + eMail + jenkel + Agama + esde + esempe + esema + jurs
    print(hasil)
    
def pembayaran_itb(by,ak,kt,jb):
    bayars = bayar(by)
    agk = angka(ak)
    kett = ket(kt)
    jbl = jmlBayar(jb)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pembayaran ", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=bayars, ln=4,align="L")
    pdf.cell(200,10,txt=agk, ln=4,align="L")
    pdf.cell(200,10,txt=kett, ln=4,align="L")
    pdf.cell(200,10,txt=jbl, ln=4,align="L")
    pdf.output("Bukti Pembayaran ITB.pdf")
    
def pembayaran_itb_cli(by,ak,kt,jb):
    bayars = bayar(by)
    agk = angka(ak)
    kett = ket(kt)
    jbl = jmlBayar(jb)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pembayaran ", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=bayars, ln=4,align="L")
    pdf.cell(200,10,txt=agk, ln=4,align="L")
    pdf.cell(200,10,txt=kett, ln=4,align="L")
    pdf.cell(200,10,txt=jbl, ln=4,align="L")
    hasil = bayars + agk +  kett + jbl
    print(hasil)
    
#########################################################################################################
##################################### Fungsi Universitas Gajah Mada ######################################################
#########################################################################################################

def menu_ugm():
    
    print("\n")
    print("Selamat Datang di Universitas Gajah Mada")
    print("-----Silahkan pilih menu berikut-----")
    print("[1] Pendaftaran")
    print("[2] Pembayaran")
    print("[3] Cek Kelulusan")
    print("[4] Kembali")
    
    mnu_kps_ugm = int(input("Pilih Jawaban : "))
    
    if(mnu_kps_ugm == 1): 
        menu1_ugm()

    elif(mnu_kps_ugm == 2):      
        menu2_ugm()
    
    elif(mnu_kps_ugm == 3):      
        menu3_ugm()
        
    elif(mnu_kps_ugm == 4):      
        menu()
    else:      
        return ("Mohon pilih salah satu menu diatas !!! \n")    

def menu1_ugm():
    
        print("\n")
        print("---Untuk Melakukan Pendaftaran, Silahkan Isi data berikut---")
        print("\n")
        
        namai = input("Masukan Nama Anda     : ")
        
        tmpti = input("Masukan Tempat Lahir Anda     : ")
        
        tgli = input("Masukan Tanggal Lahir Anda     : ")

        almti = input("Alamat Sekarang        : ")
        
        noNisni = input("No NISN        : ")
        
        noHpi = int(input("Masukan No HP Anda : "))

        emaili = input("Masukan Email Anda    : ")
        
        jenkei = jk()
        
        agmi = agama()
        
        sdi  = input("Masukkan Nama Sekolah Dasar : ")
        
        smpi  = input("Masukkan Nama Sekolah Menengah Pertama : ")
        
        smai  = input("Masukkan Nama Sekolah menengah Atas : ")
        
        juri = jurusan()
        
        nama(namai)
        
        tptLahir(tmpti)
        
        tglLahir(tgli)

        almt(almti)
        
        noNisn(noNisni)
        
        noHp(noHpi)
        
        email(emaili)
        
        sde(sdi)
        
        smpe(smpi)
        
        esma(smai)

        
        t1 = threading.Thread(target=daftar_ugm,args=(namai,tmpti,tgli,almti,noNisni,noHpi,emaili,jenkei,agmi,sdi,smpi,smai,juri))
        
        t2 = threading.Thread(target=daftar_ugm_cli,args=(namai,tmpti,tgli,almti,noNisni,noHpi,emaili,jenkei,agmi,sdi,smpi,smai,juri))

        cetak = input("Cetak Bukti Pendaftaran (y/n)? ")
        if(cetak == 'y'):
            print("Bukti Pendaftaran telah dicetak")
            t1.start()  
            t2.start()
        elif(cetak == 'n'):        
            return ("Terima kasih telah Mendaftar UGM :)")
        else:
            return ("pilihan hanya y/n")
        
def menu2_ugm():
    
        print("\n")
        print("-----------Bukti Pembayaran------------")
        print("\n")
            
        ibayar = input("Masukkan no rekening panitia       : 03130 - ")
        
        iket = input("Masukkan keterangan    : ")
        
        iangka = int(input("Jumlah Nominal     : "))
        
        ijmlBayar = input("Jumlah Dibayarkan     : ")
        
        bayar(ibayar)
        
        ket(iket)
        
        angka(iangka)
        
        jmlBayar(ijmlBayar)
        
        t1 = threading.Thread(target=pembayaran_ugm,args=(ibayar,iket,iangka,ijmlBayar))
        
        t2 = threading.Thread(target=pembayaran_ugm_cli,args=(ibayar,iket,iangka,ijmlBayar))
        
        cetak = input("Cetak bukti pembayaran (y/n)? ")
        if(cetak == 'y'):
            print("Bukti telah dicetak")
            t1.start()
            t2.start()    
        elif(cetak == 'n'):        
            return ("Terima kasih telah melakukan Pembayaran :)")
        else:
            return ("pilihan hanya y/n")
        
def menu3_ugm():
    print("\n")
    print("-----------Hasil Kelulusan diumumkan pada 18 Juli 2020------------")
    print("\n")
    
def daftar_ugm(c,n,w,z,k,e,jk,agm,sd,smp,sma,p,jur):
    name = nama(c)
    tptlhr =  tptLahir(p)
    tgllhr = tglLahir(w)
    alm = almt(n)
    nisn = noNisn(z)
    hp = noHp(k)
    eMail = email(e)
    jenkel = jk
    Agama = agm
    esde = sde(sd)
    esempe = smpe(smp)
    esema = esma(sma)
    jurs = jur

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pendaftaran Mahasiswa Baru UGM", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Data Pendaftar", ln=3,align="L")
    pdf.cell(200,10,txt=name, ln=4,align="L")
    pdf.cell(200,10,txt=tptlhr, ln=4,align="L")
    pdf.cell(200,10,txt=tgllhr, ln=4,align="L")
    pdf.cell(200,10,txt=alm, ln=4,align="L")
    pdf.cell(200,10,txt=nisn, ln=4,align="L")
    pdf.cell(200,10,txt=hp, ln=4,align="L")
    pdf.cell(200,10,txt=eMail, ln=4,align="L")
    pdf.cell(200,10,txt="Jenis Kelamin          : "+jenkel, ln=4,align="L")
    pdf.cell(200,10,txt="Agama                     : "+Agama, ln=4,align="L")
    pdf.cell(200,10,txt=esde, ln=4,align="L")
    pdf.cell(200,10,txt=esempe, ln=4,align="L")
    pdf.cell(200,10,txt=esema, ln=4,align="L")
    pdf.cell(200,10,txt="Jurusan                     : "+jurs, ln=4,align="L")
    pdf.output("Bukti Pendaftaran UGM.pdf")
    
def daftar_ugm_cli(c,n,w,z,k,e,jk,agm,sd,smp,sma,p,jur):
    name = nama(c)
    tptlhr =  tptLahir(p)
    tgllhr = tglLahir(w)
    alm = almt(n)
    nisn = noNisn(z)
    hp = noHp(k)
    eMail = email(e)
    jenkel = jk
    Agama = agm
    esde = sde(sd)
    esempe = smpe(smp)
    esema = esma(sma)
    jurs = jur

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pendaftaran Mahasiswa Baru UGM", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Data Pendaftar", ln=3,align="L")
    pdf.cell(200,10,txt=name, ln=4,align="L")
    pdf.cell(200,10,txt=tptlhr, ln=4,align="L")
    pdf.cell(200,10,txt=tgllhr, ln=4,align="L")
    pdf.cell(200,10,txt=alm, ln=4,align="L")
    pdf.cell(200,10,txt=nisn, ln=4,align="L")
    pdf.cell(200,10,txt=hp, ln=4,align="L")
    pdf.cell(200,10,txt=eMail, ln=4,align="L")
    pdf.cell(200,10,txt="Jenis Kelamin          : "+jenkel, ln=4,align="L")
    pdf.cell(200,10,txt="Agama                     : "+Agama, ln=4,align="L")
    pdf.cell(200,10,txt=esde, ln=4,align="L")
    pdf.cell(200,10,txt=esempe, ln=4,align="L")
    pdf.cell(200,10,txt=esema, ln=4,align="L")
    pdf.cell(200,10,txt="Jurusan                     : "+jurs, ln=4,align="L")
    hasil = name + tptlhr + tgllhr + alm + nisn + hp + eMail + jenkel + Agama + esde + esempe + esema + jurs
    print(hasil)
    
def pembayaran_ugm(by,ak,kt,jb):
    bayars = bayar(by)
    agk = angka(ak)
    kett = ket(kt)
    jbl = jmlBayar(jb)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pembayaran ", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=bayars, ln=4,align="L")
    pdf.cell(200,10,txt=agk, ln=4,align="L")
    pdf.cell(200,10,txt=kett, ln=4,align="L")
    pdf.cell(200,10,txt=jbl, ln=4,align="L")
    pdf.output("Bukti Pembayaran UGM.pdf")
    
def pembayaran_ugm_cli(by,ak,kt,jb):
    bayars = bayar(by)
    agk = angka(ak)
    kett = ket(kt)
    jbl = jmlBayar(jb)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pembayaran ", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=bayars, ln=4,align="L")
    pdf.cell(200,10,txt=agk, ln=4,align="L")
    pdf.cell(200,10,txt=kett, ln=4,align="L")
    pdf.cell(200,10,txt=jbl, ln=4,align="L")
    hasil = bayars + agk + kett + jbl
    print(hasil)
    
#########################################################################################################
##################################### Fungsi Universitas Diponegoro ######################################################
#########################################################################################################

def menu_undip():
    
    print("\n")
    print("Selamat Datang di Universitas Diponegoro")
    print("-----Silahkan pilih menu berikut-----")
    print("[1] Pendaftaran")
    print("[2] Pembayaran")
    print("[3] Cek Kelulusan")
    print("[4] Kembali")
    
    mnu_kps_undip = int(input("Pilih Jawaban : "))
    
    if(mnu_kps_undip == 1): 
        menu1_undip()

    elif(mnu_kps_undip == 2):      
        menu2_undip()
    
    elif(mnu_kps_undip == 3):      
        menu3_undip()
        
    elif(mnu_kps_undip == 4):      
        menu()
    else:      
        return ("Mohon pilih salah satu menu diatas !!! \n")    

def menu1_undip():
    
        print("\n")
        print("---Untuk Melakukan Pendaftaran, Silahkan Isi data berikut---")
        print("\n")
        
        namai = input("Masukan Nama Anda     : ")
        
        tmpti = input("Masukan Tempat Lahir Anda     : ")
        
        tgli = input("Masukan Tanggal Lahir Anda     : ")

        almti = input("Alamat Sekarang        : ")
        
        noNisni = input("No NISN        : ")
        
        noHpi = int(input("Masukan No HP Anda : "))

        emaili = input("Masukan Email Anda    : ")
        
        jenkei = jk()
        
        agmi = agama()
        
        sdi  = input("Masukkan Nama Sekolah Dasar : ")
        
        smpi  = input("Masukkan Nama Sekolah Menengah Pertama : ")
        
        smai  = input("Masukkan Nama Sekolah menengah Atas : ")
        
        juri = jurusan()
        
        nama(namai)
        
        tptLahir(tmpti)
        
        tglLahir(tgli)

        almt(almti)
        
        noNisn(noNisni)
        
        noHp(noHpi)
        
        email(emaili)
        
        sde(sdi)
        
        smpe(smpi)
        
        esma(smai)

        
        t1 = threading.Thread(target=daftar_undip,args=(namai,tmpti,tgli,almti,noNisni,noHpi,emaili,jenkei,agmi,sdi,smpi,smai,juri))
        
        t2 = threading.Thread(target=daftar_undip_cli,args=(namai,tmpti,tgli,almti,noNisni,noHpi,emaili,jenkei,agmi,sdi,smpi,smai,juri))

        cetak = input("Cetak Bukti Pendaftaran (y/n)? ")
        if(cetak == 'y'):
            print("Bukti Pendaftaran telah dicetak")
            t1.start()  
            t2.start()
        elif(cetak == 'n'):        
            return ("Terima kasih telah Mendaftar UNDIP :)")
        else:
            return ("pilihan hanya y/n")
        
def menu2_undip():
    
        print("\n")
        print("-----------Bukti Pembayaran------------")
        print("\n")
            
        ibayar = input("Masukkan no rekening panitia       : 03130 - ")
        
        iket = input("Masukkan keterangan    : ")
        
        iangka = int(input("Jumlah Nominal     : "))
        
        ijmlBayar = input("Jumlah Dibayarkan     : ")
        
        bayar(ibayar)
        
        ket(iket)
        
        angka(iangka)
        
        jmlBayar(ijmlBayar)
        
        t1 = threading.Thread(target=pembayaran_undip,args=(ibayar,iket,iangka,ijmlBayar))
        
        t2 = threading.Thread(target=pembayaran_undip_cli,args=(ibayar,iket,iangka,ijmlBayar))
        
        cetak = input("Cetak bukti pembayaran (y/n)? ")
        if(cetak == 'y'):
            print("Bukti telah dicetak")
            t1.start()
            t2.start()    
        elif(cetak == 'n'):        
            return ("Terima kasih telah melakukan Pembayaran :)")
        else:
            return ("pilihan hanya y/n")
        
def menu3_undip():
    print("\n")
    print("-----------Hasil Kelulusan diumumkan pada 18 Juli 2020------------")
    print("\n")
    
def daftar_undip(c,n,w,z,k,e,jk,agm,sd,smp,sma,p,jur):
    name = nama(c)
    tptlhr =  tptLahir(p)
    tgllhr = tglLahir(w)
    alm = almt(n)
    nisn = noNisn(z)
    hp = noHp(k)
    eMail = email(e)
    jenkel = jk
    Agama = agm
    esde = sde(sd)
    esempe = smpe(smp)
    esema = esma(sma)
    jurs = jur

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pendaftaran Mahasiswa Baru Undip", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Data Pendaftar", ln=3,align="L")
    pdf.cell(200,10,txt=name, ln=4,align="L")
    pdf.cell(200,10,txt=tptlhr, ln=4,align="L")
    pdf.cell(200,10,txt=tgllhr, ln=4,align="L")
    pdf.cell(200,10,txt=alm, ln=4,align="L")
    pdf.cell(200,10,txt=nisn, ln=4,align="L")
    pdf.cell(200,10,txt=hp, ln=4,align="L")
    pdf.cell(200,10,txt=eMail, ln=4,align="L")
    pdf.cell(200,10,txt="Jenis Kelamin          : "+jenkel, ln=4,align="L")
    pdf.cell(200,10,txt="Agama                     : "+Agama, ln=4,align="L")
    pdf.cell(200,10,txt=esde, ln=4,align="L")
    pdf.cell(200,10,txt=esempe, ln=4,align="L")
    pdf.cell(200,10,txt=esema, ln=4,align="L")
    pdf.cell(200,10,txt="Jurusan                     : "+jurs, ln=4,align="L")
    pdf.output("Bukti Pendaftaran Undip.pdf")
    
def daftar_undip_cli(c,n,w,z,k,e,jk,agm,sd,smp,sma,p,jur):
    name = nama(c)
    tptlhr =  tptLahir(p)
    tgllhr = tglLahir(w)
    alm = almt(n)
    nisn = noNisn(z)
    hp = noHp(k)
    eMail = email(e)
    jenkel = jk
    Agama = agm
    esde = sde(sd)
    esempe = smpe(smp)
    esema = esma(sma)
    jurs = jur

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pendaftaran Mahasiswa Baru Undip", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Data Pendaftar", ln=3,align="L")
    pdf.cell(200,10,txt=name, ln=4,align="L")
    pdf.cell(200,10,txt=tptlhr, ln=4,align="L")
    pdf.cell(200,10,txt=tgllhr, ln=4,align="L")
    pdf.cell(200,10,txt=alm, ln=4,align="L")
    pdf.cell(200,10,txt=nisn, ln=4,align="L")
    pdf.cell(200,10,txt=hp, ln=4,align="L")
    pdf.cell(200,10,txt=eMail, ln=4,align="L")
    pdf.cell(200,10,txt="Jenis Kelamin          : "+jenkel, ln=4,align="L")
    pdf.cell(200,10,txt="Agama                     : "+Agama, ln=4,align="L")
    pdf.cell(200,10,txt=esde, ln=4,align="L")
    pdf.cell(200,10,txt=esempe, ln=4,align="L")
    pdf.cell(200,10,txt=esema, ln=4,align="L")
    pdf.cell(200,10,txt="Jurusan                     : "+jurs, ln=4,align="L")
    hasil = name + tptlhr + tgllhr + alm + nisn + hp + eMail + jenkel + Agama + esde + esempe + esema + jurs
    print(hasil)
    
def pembayaran_undip(by,ak,kt,jb):
    bayars = bayar(by)
    agk = angka(ak)
    kett = ket(kt)
    jbl = jmlBayar(jb)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pembayaran ", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=bayars, ln=4,align="L")
    pdf.cell(200,10,txt=agk, ln=4,align="L")
    pdf.cell(200,10,txt=kett, ln=4,align="L")
    pdf.cell(200,10,txt=jbl, ln=4,align="L")
    pdf.output("Bukti Pembayaran Undip.pdf")
    
def pembayaran_undip_cli(by,ak,kt,jb):
    bayars = bayar(by)
    agk = angka(ak)
    kett = ket(kt)
    jbl = jmlBayar(jb)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pembayaran ", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=bayars, ln=4,align="L")
    pdf.cell(200,10,txt=agk, ln=4,align="L")
    pdf.cell(200,10,txt=kett, ln=4,align="L")
    pdf.cell(200,10,txt=jbl, ln=4,align="L")
    hasil = bayars + agk + kett + jbl
    print(hasil)
    
#########################################################################################################
##################################### Fungsi Universitas Pendidikan Indonesia ######################################################
#########################################################################################################

def menu_upi():
    
    print("\n")
    print("Selamat Datang di Universitas Pendidikan Indonesia")
    print("-----Silahkan pilih menu berikut-----")
    print("[1] Pendaftaran")
    print("[2] Pembayaran")
    print("[3] Cek Kelulusan")
    print("[4] Kembali")
    
    mnu_kps_upi = int(input("Pilih Jawaban : "))
    
    if(mnu_kps_upi == 1): 
        menu1_upi()

    elif(mnu_kps_upi == 2):      
        menu2_upi()
    
    elif(mnu_kps_upi == 3):      
        menu3_upi()
        
    elif(mnu_kps_upi == 4):      
        menu()
    else:      
        return ("Mohon pilih salah satu menu diatas !!! \n")    

def menu1_upi():
    
        print("\n")
        print("---Untuk Melakukan Pendaftaran, Silahkan Isi data berikut---")
        print("\n")
        
        namai = input("Masukan Nama Anda     : ")
        
        tmpti = input("Masukan Tempat Lahir Anda     : ")
        
        tgli = input("Masukan Tanggal Lahir Anda     : ")

        almti = input("Alamat Sekarang        : ")
        
        noNisni = input("No NISN        : ")
        
        noHpi = int(input("Masukan No HP Anda : "))

        emaili = input("Masukan Email Anda    : ")
        
        jenkei = jk()
        
        agmi = agama()
        
        sdi  = input("Masukkan Nama Sekolah Dasar : ")
        
        smpi  = input("Masukkan Nama Sekolah Menengah Pertama : ")
        
        smai  = input("Masukkan Nama Sekolah menengah Atas : ")
        
        juri = jurusan()
        
        nama(namai)
        
        tptLahir(tmpti)
        
        tglLahir(tgli)

        almt(almti)
        
        noNisn(noNisni)
        
        noHp(noHpi)
        
        email(emaili)
        
        sde(sdi)
        
        smpe(smpi)
        
        esma(smai)

        
        t1 = threading.Thread(target=daftar_upi,args=(namai,tmpti,tgli,almti,noNisni,noHpi,emaili,jenkei,agmi,sdi,smpi,smai,juri))
        
        t2 = threading.Thread(target=daftar_upi_cli,args=(namai,tmpti,tgli,almti,noNisni,noHpi,emaili,jenkei,agmi,sdi,smpi,smai,juri))

        cetak = input("Cetak Bukti Pendaftaran (y/n)? ")
        if(cetak == 'y'):
            print("Bukti Pendaftaran telah dicetak")
            t1.start() 
            t2.start()
        elif(cetak == 'n'):        
            return ("Terima kasih telah Mendaftar UPI :)")
        else:
            return ("pilihan hanya y/n")
        
def menu2_upi():
    
        print("\n")
        print("-----------Bukti Pembayaran------------")
        print("\n")
            
        ibayar = input("Masukkan no rekening panitia       : 03130 - ")
        
        iket = input("Masukkan keterangan    : ")
        
        iangka = int(input("Jumlah Nominal     : "))
        
        ijmlBayar = input("Jumlah Dibayarkan     : ")
        
        bayar(ibayar)
        
        ket(iket)
        
        angka(iangka)
        
        jmlBayar(ijmlBayar)
        
        t1 = threading.Thread(target=pembayaran_upi,args=(ibayar,iket,iangka,ijmlBayar))

        t2 = threading.Thread(target=pembayaran_upi_cli,args=(ibayar,iket,iangka,ijmlBayar))
        
        cetak = input("Cetak bukti pembayaran (y/n)? ")
        if(cetak == 'y'):
            print("Bukti telah dicetak")
            t1.start()
            t2.start()    
        elif(cetak == 'n'):        
            return ("Terima kasih telah melakukan Pembayaran :)")
        else:
            return ("pilihan hanya y/n")
        
def menu3_upi():
    print("\n")
    print("-----------Hasil Kelulusan diumumkan pada 18 Juli 2020------------")
    print("\n")
    
def daftar_upi(c,n,w,z,k,e,jk,agm,sd,smp,sma,p,jur):
    name = nama(c)
    tptlhr =  tptLahir(p)
    tgllhr = tglLahir(w)
    alm = almt(n)
    nisn = noNisn(z)
    hp = noHp(k)
    eMail = email(e)
    jenkel = jk
    Agama = agm
    esde = sde(sd)
    esempe = smpe(smp)
    esema = esma(sma)
    jurs = jur

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pendaftaran Mahasiswa Baru UPI", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Data Pendaftar", ln=3,align="L")
    pdf.cell(200,10,txt=name, ln=4,align="L")
    pdf.cell(200,10,txt=tptlhr, ln=4,align="L")
    pdf.cell(200,10,txt=tgllhr, ln=4,align="L")
    pdf.cell(200,10,txt=alm, ln=4,align="L")
    pdf.cell(200,10,txt=nisn, ln=4,align="L")
    pdf.cell(200,10,txt=hp, ln=4,align="L")
    pdf.cell(200,10,txt=eMail, ln=4,align="L")
    pdf.cell(200,10,txt="Jenis Kelamin          : "+jenkel, ln=4,align="L")
    pdf.cell(200,10,txt="Agama                     : "+Agama, ln=4,align="L")
    pdf.cell(200,10,txt=esde, ln=4,align="L")
    pdf.cell(200,10,txt=esempe, ln=4,align="L")
    pdf.cell(200,10,txt=esema, ln=4,align="L")
    pdf.cell(200,10,txt="Jurusan                     : "+jurs, ln=4,align="L")
    pdf.output("Bukti Pendaftaran UPI.pdf")
    
def daftar_upi_cli(c,n,w,z,k,e,jk,agm,sd,smp,sma,p,jur):
    name = nama(c)
    tptlhr =  tptLahir(p)
    tgllhr = tglLahir(w)
    alm = almt(n)
    nisn = noNisn(z)
    hp = noHp(k)
    eMail = email(e)
    jenkel = jk
    Agama = agm
    esde = sde(sd)
    esempe = smpe(smp)
    esema = esma(sma)
    jurs = jur

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pendaftaran Mahasiswa Baru UPI", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Data Pendaftar", ln=3,align="L")
    pdf.cell(200,10,txt=name, ln=4,align="L")
    pdf.cell(200,10,txt=tptlhr, ln=4,align="L")
    pdf.cell(200,10,txt=tgllhr, ln=4,align="L")
    pdf.cell(200,10,txt=alm, ln=4,align="L")
    pdf.cell(200,10,txt=nisn, ln=4,align="L")
    pdf.cell(200,10,txt=hp, ln=4,align="L")
    pdf.cell(200,10,txt=eMail, ln=4,align="L")
    pdf.cell(200,10,txt="Jenis Kelamin          : "+jenkel, ln=4,align="L")
    pdf.cell(200,10,txt="Agama                     : "+Agama, ln=4,align="L")
    pdf.cell(200,10,txt=esde, ln=4,align="L")
    pdf.cell(200,10,txt=esempe, ln=4,align="L")
    pdf.cell(200,10,txt=esema, ln=4,align="L")
    pdf.cell(200,10,txt="Jurusan                     : "+jurs, ln=4,align="L")
    hasil = name + tptlhr + tgllhr + alm + nisn + hp + eMail + jenkel + Agama + esde + esempe + esema + jurs
    print(hasil)
    
def pembayaran_upi(by,ak,kt,jb):
    bayars = bayar(by)
    agk = angka(ak)
    kett = ket(kt)
    jbl = jmlBayar(jb)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pembayaran ", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=bayars, ln=4,align="L")
    pdf.cell(200,10,txt=agk, ln=4,align="L")
    pdf.cell(200,10,txt=kett, ln=4,align="L")
    pdf.cell(200,10,txt=jbl, ln=4,align="L")
    pdf.output("Bukti Pembayaran UPI.pdf")
    
def pembayaran_upi_cli(by,ak,kt,jb):
    bayars = bayar(by)
    agk = angka(ak)
    kett = ket(kt)
    jbl = jmlBayar(jb)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pembayaran ", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=bayars, ln=4,align="L")
    pdf.cell(200,10,txt=agk, ln=4,align="L")
    pdf.cell(200,10,txt=kett, ln=4,align="L")
    pdf.cell(200,10,txt=jbl, ln=4,align="L")
    hasil = bayars + agk + kett + jbl
    print(hasil)
    
#########################################################################################################
##################################### Fungsi Universitas Padjajaran ######################################################
#########################################################################################################

def menu_unpad():
    
    print("\n")
    print("Selamat Datang di Universitas Padjajaran")
    print("-----Silahkan pilih menu berikut-----")
    print("[1] Pendaftaran")
    print("[2] Pembayaran")
    print("[3] Cek Kelulusan")
    print("[4] Kembali")
    
    mnu_kps_unpad = int(input("Pilih Jawaban : "))
    
    if(mnu_kps_unpad == 1): 
        menu1_unpad()

    elif(mnu_kps_unpad == 2):      
        menu2_unpad()
    
    elif(mnu_kps_unpad == 3):      
        menu3_unpad()
        
    elif(mnu_kps_unpad == 4):      
        menu()
    else:      
        return ("Mohon pilih salah satu menu diatas !!! \n")    

def menu1_unpad():
    
        print("\n")
        print("---Untuk Melakukan Pendaftaran, Silahkan Isi data berikut---")
        print("\n")
        
        namai = input("Masukan Nama Anda     : ")
        
        tmpti = input("Masukan Tempat Lahir Anda     : ")
        
        tgli = input("Masukan Tanggal Lahir Anda     : ")

        almti = input("Alamat Sekarang        : ")
        
        noNisni = input("No NISN        : ")
        
        noHpi = int(input("Masukan No HP Anda : "))

        emaili = input("Masukan Email Anda    : ")
        
        jenkei = jk()
        
        agmi = agama()
        
        sdi  = input("Masukkan Nama Sekolah Dasar : ")
        
        smpi  = input("Masukkan Nama Sekolah Menengah Pertama : ")
        
        smai  = input("Masukkan Nama Sekolah menengah Atas : ")
        
        juri = jurusan()
        
        nama(namai)
        
        tptLahir(tmpti)
        
        tglLahir(tgli)

        almt(almti)
        
        noNisn(noNisni)
        
        noHp(noHpi)
        
        email(emaili)
        
        sde(sdi)
        
        smpe(smpi)
        
        esma(smai)

        
        t1 = threading.Thread(target=daftar_unpad,args=(namai,tmpti,tgli,almti,noNisni,noHpi,emaili,jenkei,agmi,sdi,smpi,smai,juri))
        
        t2 = threading.Thread(target=daftar_unpad_cli,args=(namai,tmpti,tgli,almti,noNisni,noHpi,emaili,jenkei,agmi,sdi,smpi,smai,juri))

        cetak = input("Cetak Bukti Pendaftaran (y/n)? ")
        if(cetak == 'y'):
            print("Bukti Pendaftaran telah dicetak")
            t1.start() 
            t2.start()
        elif(cetak == 'n'):        
            return ("Terima kasih telah Mendaftar Unpad :)")
        else:
            return ("pilihan hanya y/n")
        
def menu2_unpad():
    
        print("\n")
        print("-----------Bukti Pembayaran------------")
        print("\n")
            
        ibayar = input("Masukkan no rekening panitia       : 03130 - ")
        
        iket = input("Masukkan keterangan    : ")
        
        iangka = int(input("Jumlah Nominal     : "))
        
        ijmlBayar = input("Jumlah Dibayarkan     : ")
        
        bayar(ibayar)
        
        ket(iket)
        
        angka(iangka)
        
        jmlBayar(ijmlBayar)
        
        t1 = threading.Thread(target=pembayaran_unpad,args=(ibayar,iket,iangka,ijmlBayar))

        t2 = threading.Thread(target=pembayaran_unpad_cli,args=(ibayar,iket,iangka,ijmlBayar))
        
        cetak = input("Cetak bukti pembayaran (y/n)? ")
        if(cetak == 'y'):
            print("Bukti telah dicetak")
            t1.start()
            t2.start()    
        elif(cetak == 'n'):        
            return ("Terima kasih telah melakukan Pembayaran :)")
        else:
            return ("pilihan hanya y/n")
        
def menu3_unpad():
    print("\n")
    print("-----------Hasil Kelulusan diumumkan pada 18 Juli 2020------------")
    print("\n")
    
def daftar_unpad(c,n,w,z,k,e,jk,agm,sd,smp,sma,p,jur):
    name = nama(c)
    tptlhr =  tptLahir(p)
    tgllhr = tglLahir(w)
    alm = almt(n)
    nisn = noNisn(z)
    hp = noHp(k)
    eMail = email(e)
    jenkel = jk
    Agama = agm
    esde = sde(sd)
    esempe = smpe(smp)
    esema = esma(sma)
    jurs = jur

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pendaftaran Mahasiswa Baru Unpad", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Data Pendaftar", ln=3,align="L")
    pdf.cell(200,10,txt=name, ln=4,align="L")
    pdf.cell(200,10,txt=tptlhr, ln=4,align="L")
    pdf.cell(200,10,txt=tgllhr, ln=4,align="L")
    pdf.cell(200,10,txt=alm, ln=4,align="L")
    pdf.cell(200,10,txt=nisn, ln=4,align="L")
    pdf.cell(200,10,txt=hp, ln=4,align="L")
    pdf.cell(200,10,txt=eMail, ln=4,align="L")
    pdf.cell(200,10,txt="Jenis Kelamin          : "+jenkel, ln=4,align="L")
    pdf.cell(200,10,txt="Agama                     : "+Agama, ln=4,align="L")
    pdf.cell(200,10,txt=esde, ln=4,align="L")
    pdf.cell(200,10,txt=esempe, ln=4,align="L")
    pdf.cell(200,10,txt=esema, ln=4,align="L")
    pdf.cell(200,10,txt="Jurusan                     : "+jurs, ln=4,align="L")
    pdf.output("Bukti Pendaftaran Unpad.pdf")
    
def daftar_unpad_cli(c,n,w,z,k,e,jk,agm,sd,smp,sma,p,jur):
    name = nama(c)
    tptlhr =  tptLahir(p)
    tgllhr = tglLahir(w)
    alm = almt(n)
    nisn = noNisn(z)
    hp = noHp(k)
    eMail = email(e)
    jenkel = jk
    Agama = agm
    esde = sde(sd)
    esempe = smpe(smp)
    esema = esma(sma)
    jurs = jur

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pendaftaran Mahasiswa Baru Unpad", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Data Pendaftar", ln=3,align="L")
    pdf.cell(200,10,txt=name, ln=4,align="L")
    pdf.cell(200,10,txt=tptlhr, ln=4,align="L")
    pdf.cell(200,10,txt=tgllhr, ln=4,align="L")
    pdf.cell(200,10,txt=alm, ln=4,align="L")
    pdf.cell(200,10,txt=nisn, ln=4,align="L")
    pdf.cell(200,10,txt=hp, ln=4,align="L")
    pdf.cell(200,10,txt=eMail, ln=4,align="L")
    pdf.cell(200,10,txt="Jenis Kelamin          : "+jenkel, ln=4,align="L")
    pdf.cell(200,10,txt="Agama                     : "+Agama, ln=4,align="L")
    pdf.cell(200,10,txt=esde, ln=4,align="L")
    pdf.cell(200,10,txt=esempe, ln=4,align="L")
    pdf.cell(200,10,txt=esema, ln=4,align="L")
    pdf.cell(200,10,txt="Jurusan                     : "+jurs, ln=4,align="L")
    hasil = name + tptlhr + tgllhr + alm + nisn + hp + eMail + jenkel + Agama + esde + esempe + esema + jurs
    print(hasil)
    
def pembayaran_unpad(by,ak,kt,jb):
    bayars = bayar(by)
    agk = angka(ak)
    kett = ket(kt)
    jbl = jmlBayar(jb)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pembayaran ", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=bayars, ln=4,align="L")
    pdf.cell(200,10,txt=agk, ln=4,align="L")
    pdf.cell(200,10,txt=kett, ln=4,align="L")
    pdf.cell(200,10,txt=jbl, ln=4,align="L")
    pdf.output("Bukti Pembayaran Unpad.pdf")
    
def pembayaran_unpad_cli(by,ak,kt,jb):
    bayars = bayar(by)
    agk = angka(ak)
    kett = ket(kt)
    jbl = jmlBayar(jb)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pembayaran ", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=bayars, ln=4,align="L")
    pdf.cell(200,10,txt=agk, ln=4,align="L")
    pdf.cell(200,10,txt=kett, ln=4,align="L")
    pdf.cell(200,10,txt=jbl, ln=4,align="L")
    hasil = bayars + agk + kett + jbl
    print(hasil)

#########################################################################################################
##################################### Fungsi Universitas Brawijaya ######################################################
#########################################################################################################

def menu_unibraw():
    
    print("\n")
    print("Selamat Datang di Universitas Brawijaya")
    print("-----Silahkan pilih menu berikut-----")
    print("[1] Pendaftaran")
    print("[2] Pembayaran")
    print("[3] Cek Kelulusan")
    print("[4] Kembali")
    
    mnu_kps_unibraw = int(input("Pilih Jawaban : "))
    
    if(mnu_kps_unibraw == 1): 
        menu1_unibraw()

    elif(mnu_kps_unibraw == 2):      
        menu2_unibraw()
    
    elif(mnu_kps_unibraw == 3):      
        menu3_unibraw()
        
    elif(mnu_kps_unibraw == 4):      
        menu()
    else:      
        return ("Mohon pilih salah satu menu diatas !!! \n")    

def menu1_unibraw():
    
        print("\n")
        print("---Untuk Melakukan Pendaftaran, Silahkan Isi data berikut---")
        print("\n")
        
        namai = input("Masukan Nama Anda     : ")
        
        tmpti = input("Masukan Tempat Lahir Anda     : ")
        
        tgli = input("Masukan Tanggal Lahir Anda     : ")

        almti = input("Alamat Sekarang        : ")
        
        noNisni = input("No NISN        : ")
        
        noHpi = int(input("Masukan No HP Anda : "))

        emaili = input("Masukan Email Anda    : ")
        
        jenkei = jk()
        
        agmi = agama()
        
        sdi  = input("Masukkan Nama Sekolah Dasar : ")
        
        smpi  = input("Masukkan Nama Sekolah Menengah Pertama : ")
        
        smai  = input("Masukkan Nama Sekolah menengah Atas : ")
        
        juri = jurusan()
        
        nama(namai)
        
        tptLahir(tmpti)
        
        tglLahir(tgli)

        almt(almti)
        
        noNisn(noNisni)
        
        noHp(noHpi)
        
        email(emaili)
        
        sde(sdi)
        
        smpe(smpi)
        
        esma(smai)

        
        t1 = threading.Thread(target=daftar_unibraw,args=(namai,tmpti,tgli,almti,noNisni,noHpi,emaili,jenkei,agmi,sdi,smpi,smai,juri))
        
        t2 = threading.Thread(target=daftar_unibraw_cli,args=(namai,tmpti,tgli,almti,noNisni,noHpi,emaili,jenkei,agmi,sdi,smpi,smai,juri))

        cetak = input("Cetak Bukti Pendaftaran (y/n)? ")
        if(cetak == 'y'):
            print("Bukti Pendaftaran telah dicetak")
            t1.start() 
            t2.start()
        elif(cetak == 'n'):        
            return ("Terima kasih telah Mendaftar unibraw :)")
        else:
            return ("pilihan hanya y/n")
        
def menu2_unibraw():
    
        print("\n")
        print("-----------Bukti Pembayaran------------")
        print("\n")
            
        ibayar = input("Masukkan no rekening panitia       : 03130 - ")
        
        iket = input("Masukkan keterangan    : ")
        
        iangka = int(input("Jumlah Nominal     : "))
        
        ijmlBayar = input("Jumlah Dibayarkan     : ")
        
        bayar(ibayar)
        
        ket(iket)
        
        angka(iangka)
        
        jmlBayar(ijmlBayar)
        
        t1 = threading.Thread(target=pembayaran_unibraw,args=(ibayar,iket,iangka,ijmlBayar))

        t2 = threading.Thread(target=pembayaran_unibraw_cli,args=(ibayar,iket,iangka,ijmlBayar))
        
        cetak = input("Cetak bukti pembayaran (y/n)? ")
        if(cetak == 'y'):
            print("Bukti telah dicetak")
            t1.start()
            t2.start()    
        elif(cetak == 'n'):        
            return ("Terima kasih telah melakukan Pembayaran :)")
        else:
            return ("pilihan hanya y/n")
        
def menu3_unibraw():
    print("\n")
    print("-----------Hasil Kelulusan diumumkan pada 18 Juli 2020------------")
    print("\n")
    
def daftar_unibraw(c,n,w,z,k,e,jk,agm,sd,smp,sma,p,jur):
    name = nama(c)
    tptlhr =  tptLahir(p)
    tgllhr = tglLahir(w)
    alm = almt(n)
    nisn = noNisn(z)
    hp = noHp(k)
    eMail = email(e)
    jenkel = jk
    Agama = agm
    esde = sde(sd)
    esempe = smpe(smp)
    esema = esma(sma)
    jurs = jur

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pendaftaran Mahasiswa Baru Universitas Brawijaya", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Data Pendaftar", ln=3,align="L")
    pdf.cell(200,10,txt=name, ln=4,align="L")
    pdf.cell(200,10,txt=tptlhr, ln=4,align="L")
    pdf.cell(200,10,txt=tgllhr, ln=4,align="L")
    pdf.cell(200,10,txt=alm, ln=4,align="L")
    pdf.cell(200,10,txt=nisn, ln=4,align="L")
    pdf.cell(200,10,txt=hp, ln=4,align="L")
    pdf.cell(200,10,txt=eMail, ln=4,align="L")
    pdf.cell(200,10,txt="Jenis Kelamin          : "+jenkel, ln=4,align="L")
    pdf.cell(200,10,txt="Agama                     : "+Agama, ln=4,align="L")
    pdf.cell(200,10,txt=esde, ln=4,align="L")
    pdf.cell(200,10,txt=esempe, ln=4,align="L")
    pdf.cell(200,10,txt=esema, ln=4,align="L")
    pdf.cell(200,10,txt="Jurusan                     : "+jurs, ln=4,align="L")
    pdf.output("Bukti Pendaftaran Unibraw.pdf")
    
def daftar_unibraw_cli(c,n,w,z,k,e,jk,agm,sd,smp,sma,p,jur):
    name = nama(c)
    tptlhr =  tptLahir(p)
    tgllhr = tglLahir(w)
    alm = almt(n)
    nisn = noNisn(z)
    hp = noHp(k)
    eMail = email(e)
    jenkel = jk
    Agama = agm
    esde = sde(sd)
    esempe = smpe(smp)
    esema = esma(sma)
    jurs = jur

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pendaftaran Mahasiswa Baru Universitas Brawijaya", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Data Pendaftar", ln=3,align="L")
    pdf.cell(200,10,txt=name, ln=4,align="L")
    pdf.cell(200,10,txt=tptlhr, ln=4,align="L")
    pdf.cell(200,10,txt=tgllhr, ln=4,align="L")
    pdf.cell(200,10,txt=alm, ln=4,align="L")
    pdf.cell(200,10,txt=nisn, ln=4,align="L")
    pdf.cell(200,10,txt=hp, ln=4,align="L")
    pdf.cell(200,10,txt=eMail, ln=4,align="L")
    pdf.cell(200,10,txt="Jenis Kelamin          : "+jenkel, ln=4,align="L")
    pdf.cell(200,10,txt="Agama                     : "+Agama, ln=4,align="L")
    pdf.cell(200,10,txt=esde, ln=4,align="L")
    pdf.cell(200,10,txt=esempe, ln=4,align="L")
    pdf.cell(200,10,txt=esema, ln=4,align="L")
    pdf.cell(200,10,txt="Jurusan                     : "+jurs, ln=4,align="L")
    hasil = name + tptlhr + tgllhr + alm + nisn + hp + eMail + jenkel + Agama + esde + esempe + esema + jurs
    print(hasil)
    
def pembayaran_unibraw(by,ak,kt,jb):
    bayars = bayar(by)
    agk = angka(ak)
    kett = ket(kt)
    jbl = jmlBayar(jb)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pembayaran ", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=bayars, ln=4,align="L")
    pdf.cell(200,10,txt=agk, ln=4,align="L")
    pdf.cell(200,10,txt=kett, ln=4,align="L")
    pdf.cell(200,10,txt=jbl, ln=4,align="L")
    pdf.output("Bukti Pembayaran Unibraw.pdf")
    
def pembayaran_unibraw_cli(by,ak,kt,jb):
    bayars = bayar(by)
    agk = angka(ak)
    kett = ket(kt)
    jbl = jmlBayar(jb)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pembayaran ", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=bayars, ln=4,align="L")
    pdf.cell(200,10,txt=agk, ln=4,align="L")
    pdf.cell(200,10,txt=kett, ln=4,align="L")
    pdf.cell(200,10,txt=jbl, ln=4,align="L")
    hasil = bayars + agk + kett + jbl
    print(hasil)

#########################################################################################################
##################################### Fungsi Universitas Negeri Malang ######################################################
#########################################################################################################

def menu_unm():
    
    print("\n")
    print("Selamat Datang di Universitas Negeri Malang")
    print("-----Silahkan pilih menu berikut-----")
    print("[1] Pendaftaran")
    print("[2] Pembayaran")
    print("[3] Cek Kelulusan")
    print("[4] Kembali")
    
    mnu_kps_unm = int(input("Pilih Jawaban : "))
    
    if(mnu_kps_unm == 1): 
        menu1_unm()

    elif(mnu_kps_unm == 2):      
        menu2_unm()
    
    elif(mnu_kps_unm == 3):      
        menu3_unm()
        
    elif(mnu_kps_unm == 4):      
        menu()
    else:      
        return ("Mohon pilih salah satu menu diatas !!! \n")    

def menu1_unm():
    
        print("\n")
        print("---Untuk Melakukan Pendaftaran, Silahkan Isi data berikut---")
        print("\n")
        
        namai = input("Masukan Nama Anda     : ")
        
        tmpti = input("Masukan Tempat Lahir Anda     : ")
        
        tgli = input("Masukan Tanggal Lahir Anda     : ")

        almti = input("Alamat Sekarang        : ")
        
        noNisni = input("No NISN        : ")
        
        noHpi = int(input("Masukan No HP Anda : "))

        emaili = input("Masukan Email Anda    : ")
        
        jenkei = jk()
        
        agmi = agama()
        
        sdi  = input("Masukkan Nama Sekolah Dasar : ")
        
        smpi  = input("Masukkan Nama Sekolah Menengah Pertama : ")
        
        smai  = input("Masukkan Nama Sekolah menengah Atas : ")
        
        juri = jurusan()
        
        nama(namai)
        
        tptLahir(tmpti)
        
        tglLahir(tgli)

        almt(almti)
        
        noNisn(noNisni)
        
        noHp(noHpi)
        
        email(emaili)
        
        sde(sdi)
        
        smpe(smpi)
        
        esma(smai)

        
        t1 = threading.Thread(target=daftar_unibraw,args=(namai,tmpti,tgli,almti,noNisni,noHpi,emaili,jenkei,agmi,sdi,smpi,smai,juri))
        
        t2 = threading.Thread(target=daftar_unibraw_cli,args=(namai,tmpti,tgli,almti,noNisni,noHpi,emaili,jenkei,agmi,sdi,smpi,smai,juri))

        cetak = input("Cetak Bukti Pendaftaran (y/n)? ")
        if(cetak == 'y'):
            print("Bukti Pendaftaran telah dicetak")
            t1.start() 
            t2.start()
        elif(cetak == 'n'):        
            return ("Terima kasih telah Mendaftar UNM :)")
        else:
            return ("pilihan hanya y/n")
        
def menu2_unm():
    
        print("\n")
        print("-----------Bukti Pembayaran------------")
        print("\n")
            
        ibayar = input("Masukkan no rekening panitia       : 03130 - ")
        
        iket = input("Masukkan keterangan    : ")
        
        iangka = int(input("Jumlah Nominal     : "))
        
        ijmlBayar = input("Jumlah Dibayarkan     : ")
        
        bayar(ibayar)
        
        ket(iket)
        
        angka(iangka)
        
        jmlBayar(ijmlBayar)
        
        t1 = threading.Thread(target=pembayaran_unm,args=(ibayar,iket,iangka,ijmlBayar))

        t2 = threading.Thread(target=pembayaran_unm_cli,args=(ibayar,iket,iangka,ijmlBayar))
        
        cetak = input("Cetak bukti pembayaran (y/n)? ")
        if(cetak == 'y'):
            print("Bukti telah dicetak")
            t1.start()
            t2.start()    
        elif(cetak == 'n'):        
            return ("Terima kasih telah melakukan Pembayaran :)")
        else:
            return ("pilihan hanya y/n")
        
def menu3_unm():
    print("\n")
    print("-----------Hasil Kelulusan diumumkan pada 18 Juli 2020------------")
    print("\n")
    
def daftar_unm(c,n,w,z,k,e,jk,agm,sd,smp,sma,p,jur):
    name = nama(c)
    tptlhr =  tptLahir(p)
    tgllhr = tglLahir(w)
    alm = almt(n)
    nisn = noNisn(z)
    hp = noHp(k)
    eMail = email(e)
    jenkel = jk
    Agama = agm
    esde = sde(sd)
    esempe = smpe(smp)
    esema = esma(sma)
    jurs = jur

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pendaftaran Mahasiswa Baru Universitas Negeri Malang", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Data Pendaftar", ln=3,align="L")
    pdf.cell(200,10,txt=name, ln=4,align="L")
    pdf.cell(200,10,txt=tptlhr, ln=4,align="L")
    pdf.cell(200,10,txt=tgllhr, ln=4,align="L")
    pdf.cell(200,10,txt=alm, ln=4,align="L")
    pdf.cell(200,10,txt=nisn, ln=4,align="L")
    pdf.cell(200,10,txt=hp, ln=4,align="L")
    pdf.cell(200,10,txt=eMail, ln=4,align="L")
    pdf.cell(200,10,txt="Jenis Kelamin          : "+jenkel, ln=4,align="L")
    pdf.cell(200,10,txt="Agama                     : "+Agama, ln=4,align="L")
    pdf.cell(200,10,txt=esde, ln=4,align="L")
    pdf.cell(200,10,txt=esempe, ln=4,align="L")
    pdf.cell(200,10,txt=esema, ln=4,align="L")
    pdf.cell(200,10,txt="Jurusan                     : "+jurs, ln=4,align="L")
    pdf.output("Bukti Pendaftaran UNM.pdf")
    
def daftar_unm_cli(c,n,w,z,k,e,jk,agm,sd,smp,sma,p,jur):
    name = nama(c)
    tptlhr =  tptLahir(p)
    tgllhr = tglLahir(w)
    alm = almt(n)
    nisn = noNisn(z)
    hp = noHp(k)
    eMail = email(e)
    jenkel = jk
    Agama = agm
    esde = sde(sd)
    esempe = smpe(smp)
    esema = esma(sma)
    jurs = jur

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pendaftaran Mahasiswa Baru Universitas Negeri Malang", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Data Pendaftar", ln=3,align="L")
    pdf.cell(200,10,txt=name, ln=4,align="L")
    pdf.cell(200,10,txt=tptlhr, ln=4,align="L")
    pdf.cell(200,10,txt=tgllhr, ln=4,align="L")
    pdf.cell(200,10,txt=alm, ln=4,align="L")
    pdf.cell(200,10,txt=nisn, ln=4,align="L")
    pdf.cell(200,10,txt=hp, ln=4,align="L")
    pdf.cell(200,10,txt=eMail, ln=4,align="L")
    pdf.cell(200,10,txt="Jenis Kelamin          : "+jenkel, ln=4,align="L")
    pdf.cell(200,10,txt="Agama                     : "+Agama, ln=4,align="L")
    pdf.cell(200,10,txt=esde, ln=4,align="L")
    pdf.cell(200,10,txt=esempe, ln=4,align="L")
    pdf.cell(200,10,txt=esema, ln=4,align="L")
    pdf.cell(200,10,txt="Jurusan                     : "+jurs, ln=4,align="L")
    hasil = name + tptlhr + tgllhr + alm + nisn + hp + eMail + jenkel + Agama + esde + esempe + esema + jurs
    print(hasil)
    
def pembayaran_unm(by,ak,kt,jb):
    bayars = bayar(by)
    agk = angka(ak)
    kett = ket(kt)
    jbl = jmlBayar(jb)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pembayaran ", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=bayars, ln=4,align="L")
    pdf.cell(200,10,txt=agk, ln=4,align="L")
    pdf.cell(200,10,txt=kett, ln=4,align="L")
    pdf.cell(200,10,txt=jbl, ln=4,align="L")
    pdf.output("Bukti Pembayaran UNM.pdf")
    
def pembayaran_unm_cli(by,ak,kt,jb):
    bayars = bayar(by)
    agk = angka(ak)
    kett = ket(kt)
    jbl = jmlBayar(jb)
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Bukti Pembayaran ", ln=1,align="C")
    pdf.cell(200,10,txt="", ln=2,align="L")
    pdf.cell(200,10,txt="Informasi", ln=3,align="L")
    pdf.cell(200,10,txt=bayars, ln=4,align="L")
    pdf.cell(200,10,txt=agk, ln=4,align="L")
    pdf.cell(200,10,txt=kett, ln=4,align="L")
    pdf.cell(200,10,txt=jbl, ln=4,align="L")
    hasil = bayars + agk + kett + jbl
    print(hasil)

menu()