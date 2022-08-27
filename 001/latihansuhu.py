from ast import While

#Versi pertama
'''again = "True"
while bool(again) == True:
    convert = 0
    while convert < 1 or convert > 3:
        print("\nLatihan Konversi Suhu")
        print("=====================")
        convert = int(input("\nPilih Konversi Yang Diinginkan:\n1. Celcius -> Reamur\n2. Celcius -> Fahrenheit\n3. Celcius -> Kelvin\nPilihan Anda: "))

    if convert == 1:
        suhu = float(input('\nSuhu yang ingin dikonversi: '))
        print('\nHasil Konversi C->R adalah ',suhu,' -> ',(4/5)*suhu)

    if convert == 2:
        suhu = float(input('\nSuhu yang ingin dikonversi: '))
        print('\nHasil Konversi C->F adalah ',suhu,' -> ',(9/5)*suhu+32)
        
    if convert == 3:
        suhu = float(input('\nSuhu yang ingin dikonversi: '))
        print('\nHasil Konversi C->K adalah ',suhu,' -> ',suhu+273)
    again=input("\nType any to reConvert: ")'''


#Versi Kedua
reconv = True
while reconv is True:
    pilih = 0
    while pilih < 1 or pilih > 4:
        print("\nLatihan Konversi Suhu")
        print("=====================")
        pilih = int(input('\nSatuan Suhu Yang Digunakan\n1. Celcius\n2. Reamur\n3. Fahrenheit\n4. Kelvin\n\nPilihan Anda: '))
        if pilih == 1:
            suhu = float(input("\nSuhu Celsius yang ingin dikonversi: "))
            print('\nBerikut adalah hasil konversi:\n1. Celcius ke Reamur     :',(4/5)*suhu,'\n2. Celcius ke Fahrenheit :',(9/5)*suhu+32,'\n3. Celcius ke Kelvin     :', suhu+273)
            print("--------------------------\n")
        
        if pilih == 2:
            suhu = float(input("\nSuhu Reamur yang ingin dikonversi: "))
            print('\nBerikut adalah hasil konversi:\n1. Reamur ke Celcius    :',(5/4)*suhu,'\n2. Reamur ke Fahrenheit :',(9/4)*suhu+32,'\n3. Reamur ke Kelvin     :', (5/4)*suhu+273)
            print("--------------------------\n")
        
        if pilih == 3:
            suhu = float(input("\nSuhu Fahrenheit yang ingin dikonversi: "))
            print('\nBerikut adalah hasil konversi:\n1. Fahrenheit ke Celcius :',(5/9)*(suhu-32),'\n2. Fahrenheit ke Reamur  :',(4/9)*(suhu-32),'\n3. Fahrenheit ke Kelvin  :', 'belum dapat rumus')
            print("--------------------------\n")

        if pilih == 4:
            suhu = float(input("\nSuhu Kelvin yang ingin dikonversi: "))
            print('\nBerikut adalah hasil konversi:\n1. Kelvin ke Celcius    :',suhu-273,'\n2. Kelvin ke Reamur     :',(4/5)*(suhu-273),'\n3. Kelvin ke Fahrenheit :', 'belum dapat rumus')
            print("--------------------------\n")
            
    reconv=bool(input("Type any to ReConvert -> "))        