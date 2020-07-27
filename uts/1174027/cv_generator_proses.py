# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:08:04 2020

@author: Harun Ar - Rasyid
"""

#########################################################################################################
##################################### Import Library ####################################################
#########################################################################################################

import qrcode
from fpdf import FPDF
import mysql.connector
import os

#########################################################################################################
##################################### End Import Library ################################################
#########################################################################################################

#########################################################################################################
##################################### Database ##########################################################
#########################################################################################################

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="cv_generator"
)

def insert_data(db,nm,almt,tmpt,lhr,no,email,jk,hb,agm,sk,lp,sd,smp,sma,pt,jm,jp,qm,qp):
    val = (nm,almt,tmpt,lhr,no,email,jk,hb,agm,sk,lp,sd,smp,sma,pt,jm,jp,qm,qp)
    cursor = db.cursor()
    sql = "INSERT INTO biodata (nama, alamat, tlahir, tgl_lahir,nohp,email,jenkel,hobi,agama,status_kawin,last_pendidikan,sd,smp,sma,penting,jmantan,jpacar,quote_mantan,quote_paca) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil disimpan".format(cursor.rowcount))

def show_last_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM biodata ORDER BY id_bio DESC"
    cursor.execute(sql)
    results = cursor.fetchone()
  
    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)

#########################################################################################################
##################################### END - Database ####################################################
#########################################################################################################

#########################################################################################################
##################################### Data Pribadi ######################################################
#########################################################################################################

def nama(c):
    return("Nama Lengkap        : %s \n" %c)

def almt(n):
    return("Alamat Sekarang     : %s \n" %n)

def tmpt(t):
    return("Tempat Lahir        : %s \n" %t)

def lhr(tl):
    return("Tanggal Lahir       : %s \n" %tl)

def noHp(k):
    return("No Handphone        : %s \n" %k)

def email(e):
    return ("Email               : %s \n" %e)

def hobi(h):
    return ("Hobi                : %s \n" %h)

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

def lsPendidikan(lp):
    return ("Pendidikan Terakhir : %s \n" %lp)

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

