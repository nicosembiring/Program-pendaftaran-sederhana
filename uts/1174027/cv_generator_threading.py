# -*- coding: utf-8 -*-

"""

Created on Wed Apr 15 15:07:00 2020

@author: Harun Ar - Rasyid

"""

#########################################################################################################
##################################### Import Library ####################################################
#########################################################################################################

import threading

import subprocess

from fpdf import FPDF

#########################################################################################################
##################################### End Import Library ################################################
#########################################################################################################

#########################################################################################################
##################################### Data Pribadi ######################################################
#########################################################################################################

def nama(c):
    
    return("Nama Lengkap        : %s \n" %c)


def almt(n):
    
    return("Alamat Sekarang     : %s \n" %n)


def noHp(k):
    
    return("No Handphone        : %s \n" %k)


def email(e):
    
    return ("Email               : %s \n" %e)


def hobi(h):
    
    return ("Hobi                : %s \n" %h)


def lsPendidikan(lp):
    
    return ("Pendidikan Terakhir : %s \n" %lp)


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
    

def status():
    
    print("\n")
    
    print("-----Status Pernikahan-----")
    
    print("[1] Belum Menikah")
    
    print("[2] Menikah")
    
    print("[3] Duda")
    
    print("[4] Janda")
    
    st = int(input("Pilih Status : "))
    
    if(st == 1):
        
        return ("Belum Menikah")
    
    elif(st == 2):
        
        return ("Menikah")
    
    elif(st == 3):
        
        return ("Duda")
    
    elif(st == 4):
        
        return ("Janda")
    
    else:
        
        return ("Dipertanyakan")
    
    
#########################################################################################################
##################################### End Data Pribadi ##################################################
#########################################################################################################
        
#########################################################################################################
##################################### Data Pendidikan ###################################################
#########################################################################################################

def penSD(sd):
    
    return ("SD               : %s \n" %sd)

def penSMP(smp):
    
    return ("SMP              : %s \n" %smp)

def penSMA(sma):
    
    return ("SMA              : %s \n" %sma)

def penTing(unv):
    
    return ("Perguruan Tinggi : %s \n" %unv)

#########################################################################################################
##################################### End Data Pendidikan ###############################################
#########################################################################################################

#########################################################################################################
##################################### Spesial Fungsi ####################################################
#########################################################################################################
def mantan(jm):
    
    if(jm == 0):
        
        return ("Jumlah Mantan : %s Pertahankan \n"%jm)
    
    elif(jm > 0 and jm < 5):
        
        return ("Jumlah Mantan : %s Kamu Liar \n"%jm)
    
    else :
        
        return ("Jumlah Mantan : %s Fakboi \n"%jm)
    

def pacar(agm):
    print("\n")
    
    print("-----Status Pacaran-----")
    
    print("[1] Ya, Punya Pacar")
    
    print("[2] Tidak Punya")
    
    pcr = int(input("Pilih Jawaban : "))
    
    if(pcr == 1):
        
        if(agm == 1):
            
            return ("Janganlah Kamu Mendekati Zina \n")
        
        else:
            
            return ("Putusin Sebelum Dompetmu Kering \n")
        
    elif(pcr == 2):
        
        if(agm == 1):
            
            return ("Antep Weh, Dijagaan Batur Keneh Sugan \n")
        
        else:
            
            return ("Kalem Da Jodo Mah Moal Kamana \n")
    
    
#########################################################################################################
##################################### End Fungsi ########################################################
#########################################################################################################

#########################################################################################################
##################################### Fungsi Proses #####################################################
#########################################################################################################
    
def biodata(c,n,np,jk,agm,st,e,h,ls,SD,SMP,SMA,KULI,pcr,mntn):
    
    name = nama(c)
    
    tempat = almt(n)
    
    nohp = noHp(np)
    
    jenkel = "Jenis Kelamin       : "+jk+"\n"
    
    Agama = "Agama               : "+agm+"\n"
    
    Status = "Status              : "+st+"\n"
    
    eMail = email(e)
    
    hb = hobi(h)
    
    lp = lsPendidikan(ls)
    
    sd = penSD(SD)
    
    smp = penSMP(SMP)
    
    sma = penSMA(SMA)
    
    kuli = penTing(KULI)
    
    kbgh = "Pacar     : "+pcr
    
    MANtn = "Mantan    : "+ mantan(mntn)
    
    hasil = name + tempat + nohp + jenkel + Agama + Status+ eMail + hb + lp + sd + smp + sma + kuli + kbgh + MANtn
    
    print(hasil)
    
    output = subprocess.check_output(['ls','-1'])
    
    print("Have %d bytes in output " % len(output))
    
    print(output)
    
    

def laporan(c,n,np,jk,agm,st,e,h,ls,SD,SMP,SMA,KULI,pcr,mntn):
    
    name = nama(c)
    
    tempat = almt(n)
    
    nohp = noHp(np)
    
    jenkel = jk
    
    Agama = agm
    
    Status = st
    
    eMail = email(e)
    
    hb = hobi(h)
    
    lp = lsPendidikan(ls)
    
    sd = penSD(SD)
    
    smp = penSMP(SMP)
    
    sma = penSMA(SMA)
    
    kuli = penTing(KULI)
    
    kbgh = pcr
    
    MANtn = mantan(mntn)
    
    pdf=FPDF()
    
    pdf.add_page()
    
    pdf.set_font("Arial",size=12)
    
    pdf.cell(200,10,txt="Curicullum Vitae", ln=1,align="C")
    
    pdf.cell(200,10,txt="", ln=2,align="L")
    
    pdf.cell(200,10,txt="Data Pribadi", ln=3,align="L")
    
    pdf.cell(200,10,txt=name, ln=4,align="L")
    
    pdf.cell(200,10,txt=tempat, ln=4,align="L")
    
    pdf.cell(200,10,txt=nohp, ln=4,align="L")
    
    pdf.cell(200,10,txt="Jenis Kelamin          : "+jenkel, ln=4,align="L")
    
    pdf.cell(200,10,txt="Agama                     : "+Agama, ln=4,align="L")
    
    pdf.cell(200,10,txt="Status                      : "+Status, ln=4,align="L")
    
    pdf.cell(200,10,txt=eMail, ln=4,align="L")
    
    pdf.cell(200,10,txt=hb, ln=4,align="L")
    
    pdf.cell(200,10,txt=lp, ln=4,align="L")
    
    pdf.cell(200,10,txt="", ln=2,align="L")
    
    pdf.cell(200,10,txt="Pendidikan Tinggi", ln=2,align="L")
    
    pdf.cell(200,10,txt=sd, ln=2,align="L")
    
    pdf.cell(200,10,txt=smp, ln=2,align="L")
    
    pdf.cell(200,10,txt=sma, ln=2,align="L")
    
    pdf.cell(200,10,txt=kuli, ln=2,align="L")
    
    pdf.cell(200,10,txt="", ln=2,align="L")
    
    pdf.cell(200,10,txt="Hubungan Saat Ini", ln=2,align="L")
    
    pdf.cell(200,10,txt="Pacar       : "+kbgh, ln=2,align="L")
    
    pdf.cell(200,10,txt="Mantan     : "+MANtn, ln=2,align="L")
    
    pdf.output("cv.pdf")
    

#########################################################################################################
##################################### End Fungsi Proses #################################################
#########################################################################################################
    
#########################################################################################################
##################################### Memanngil Fungsi ##################################################
#########################################################################################################
    
##################################### Data Diri #########################################################
    
iname = input("Masukan Nama Anda     : ")

tmpL = input("Alamat Sekarang        : ")

noHP = int(input("Masukan No HP Anda : "))

Email = input("Masukan Email Anda    : ")

Hobi = input("Masukan Hobi Anda      : ")

last = input("Pendidikan Terakhir    : ")

nama(iname)

almt(tmpL)

noHp(noHP)

jenke = jk()

AGAMA = agama()

STATUS = status()

email(Email)

hobi(Hobi)

lsPendidikan(last)

##################################### Pendidikan Formal ################################################

sd = input("Sekolah Dasar            : ")

smp = input("Sekolah Menengah Pertama: ")

sma = input("Sekolah Menengah Atas   : ")

univ = input("Perguruan Tinggi       : ")

penSD(sd)

penSMP(smp)

penSMA(sma)

penTing(univ)

##################################### Percintaan ########################################################

mntn = int(input("Masukan Jumlah Mantan : "))

mantan(mntn)

pcr = pacar(AGAMA)


#########################################################################################################
##################################### End Memanngil Fungsi ##############################################
#########################################################################################################

#########################################################################################################
########################################### Threading ###################################################
#########################################################################################################

t1 = threading.Thread(target=biodata,args=(iname,tmpL,noHP,jenke,AGAMA,STATUS,Email,Hobi,last,sd,smp,sma,
                                           univ,pcr,mntn))

t2 = threading.Thread(target=laporan,args=(iname,tmpL,noHP,jenke,AGAMA,STATUS,Email,Hobi,last,sd,smp,sma,
                                           univ,pcr,mntn))

t1.start()

t2.start()

##########################################################################################################
########################################### End Threading ################################################
##########################################################################################################
