import time #ini untuk mengambil data waktu dari system
start_time = time.time()
a = 10

print("Hello World !!!")
print("Disini Saya akan memulai perjalanan coding saya, lagi.")

#gunakan tanda '#' untuk membuat comment

"""
Gunakan tanda kutip 2 sebanyak 3 kali
untuk membuat comment multiline atau paragraf
"""

print(a)

print(time.time() - start_time, "detik")

"""
Python dapat dicompile dengan menggunakan ByteCode
Cara untuk mengcompile adalah buka terminal, pastikan berada di direktori Main.py, lalu ketikkan python -m py_compile Main.py untuk membytecode

setiap terjadi perubahan code maka perlu dilakukan bytecode untuk pengcompailan ulang

setelah selesai di bytecode maka bisa untuk mengcompile buka terminal ketikkan python .\__pychace__\Main.cpython-310.pyc
"""
