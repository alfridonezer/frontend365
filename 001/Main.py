from posixpath import split
import time
start_time = time.time()

nama = input("Nama Anda : ")
print(nama)


#Tipe data pada umumnya


integer = 0
print(integer, type(integer))

float = 1.5
print(float, type(float))

string = "I Love You"
print(string, type(string))

boolean = False
print(boolean, type(boolean))


##Tipe Data Khusus

#Bilangan Complex
complex = complex(3,19)
print(complex,type(complex))


"""
Menggunakan Tipe data dari Bahasa C
"""
from ctypes import c_double, c_char, c_long

data_c_double = c_double(3.19)
print(data_c_double,type(data_c_double))

data_c_char = c_char(69)
print(data_c_char, type(data_c_char))

data_c_long = c_long(1995100320220310001)
print(data_c_long,type(data_c_long))



print ("Waktu Compile: ",time.time()-start_time,"detik")
