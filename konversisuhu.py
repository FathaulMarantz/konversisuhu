""""
CREDIT : A U L Techplay | 2023

-- RUMUS --
Reamur (4)
Celcius (5)
Farenheit = 9/(r/c) + 32
Kelvin = Celcius + 273
Rankine = Fahrenheit + 460
"""

angka = int(input("Masukan angka: "))
print("""
Lakukan perintah di bawah ini:
1. Ketikan key 'r' untuk Reamur
2. Ketikan key 'C' untuk Celcius
3. Ketikan key 'F' untuk Farenheit
4. Ketikan key 'K' untuk Kelvin
5. Ketikan key 'R' untuk Rankine
""")
base = str(input("Pilih pengukuran yang diinginkan: "))
konversi = str(input("Pilih konversi yang diinginkan: "))

if (base == konversi):
    print(f"Yang anda masukan tidak dikonvesi sehingga hasilnya tetap sama yakni, {angka} {base}")
elif (base != konversi):
    # REAMUR
    if (base == "r"):
        if (konversi == "C"):
            print(angka*(5/4), "Celcius")
        elif (konversi == "F"):
            print(angka*(9/4)+32, "Farenheit")
        elif (konversi == "K"):
            print(angka*(5/4)+(273), "Kelvin")
        elif (konversi == "R"):
            print((angka*(9/4)+32)+460, "Rankine")
    # CELCIUS
    elif (base == "C"):
        if (konversi == "r"):
            print(angka*(4/5), "Reamur")
        elif (konversi == "F"):
            print(angka*(9/5)+32, "Farenheit")
        elif (konversi == "K"):
            print(angka+(273), "Kelvin")
        elif (konversi == "R"):
            print((angka*(9/5)+32)+460, "Rankine")
    # FARENHEIT
    elif (base == "F"):
        if (konversi == "r"):
            print((angka-32)*4/9, "Reamur")
        elif (konversi == "C"):
            print((angka-32)*5/9, "Celcius")
        elif (konversi == "K"):
            print(((angka-32)*5/9)+(273), "Kelvin")
        elif (konversi == "R"):
            print(angka+460, "Rankine")
    # KELVIN
    elif (base == "K"):
        if (konversi == "r"):
            print((angka-273)*(4/5), "Reamur")
        elif (konversi == "C"):
            print((angka-273), "Celcius")
        elif (konversi == "F"):
            print((angka-273)*(9/5)+32, "Farenheit")
        elif (konversi == "R"):
            print((angka-273)*(9/5)+32+460, "Rankine")
    # RANKINE
    elif (base == "R"):
        if (konversi == "r"):
            print(((angka-460)-32)*(4/9), "Reamur")
        elif (konversi == "C"):
            print(((angka-460)-32)*(5/9), "Celcius")
        elif (konversi == "F"):
            print((angka-460), "Farenheit")
        elif (konversi == "K"):
            print(((angka-460)-32)*(5/9)+(273), "Kelvin")