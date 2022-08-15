# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 06:55:07 2020

@author: Dooo
"""


#input
rumus = input("Luas segitiga atau lingkaran :")

#proses

if rumus == "segitiga":
    a = input("Masukkan Alas : ")
    t = input("Masukkan tinggi : ")
    l = (int(a) * int(t)) / 2
    print ("Luas Segitiga adalah : ",l)
elif rumus == "lingkaran":
    phi = input("Masukkan nilai phi : ")
    r = input("Masukkan Jari jari : ")
    lo = float(phi) * int(r) * int(r)
    print("Luas Lingkaran adalah : ",lo)
else:
    print("Data belum ditambahkan")

