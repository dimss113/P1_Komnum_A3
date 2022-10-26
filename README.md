# Praktikum Komputasi Numerik Modul 1
**<br>Dimas Fadilah Akbar_5025211010**
**<br>Abdullah Yaskyur Bifadhlil Midror_5025211035**
**<br>Achmad Khosyi' Assajjad Ramandanta_5025211007**
**<br>Arkana Bilal Imani_5025211010**
**<br>Duevano Fairuz Pandya_5025211052**


## Requirement
- Python 3.9.12
- Code Editor

## Instalasi Library
- numpy
- math
- matplotlib
> Pada praktikum komputasi numerik modul 1 membutuhkan 2 instalasi library yaitu numpy dan matplotlib. Kita bisa lakukan instalasi dengan menggunaka pip.
``` 
pip install numpy
pip install matplotlib
```

## Soal Praktikum
> Implementasikan algoritma metode Bolzano menjadi sebuah program komputer yang dapat
menampilkan proses iteratif numerik, lengkap dengan grafik fungsinya.

## Penjelasan Kode 
#### import library yang dibutuhkan
```py
import numpy as np
import matplotlib.pyplot as plt
import math
```
library numpy dibutuhan untuk membuat array dengan isi sekumpulan nilai xr dan juga berisi banyak iterasi yang kita lakukan. library matplotlib digunakan untuk membuat grafik dengan parameter array yang diberikan.

### Membuat inputan
```py
xl = float(input("masukkan x lower: "))
xu = float(input("masukkan x upper: "))
iterate = int(input("masukkan jumlah interasi: "))
xt = 1.26611328125
```
code diatas merupakan inputan untuk x lower, x upper, dan jumlah iterasi yang kita inginkan. Kemudian juga di deklarasi x true nya yaitu 1.26611328125 yang digunakan untuk mencari error truenya.

### Membuat list
```py
list_xr = list()
list_iterate = list()
```
list_xr merupakan array yang akan menyimpan value dari xr untuk tiap iterasi, sedangkan list_iterate akan menyimpan nilai iterasinya.

### Deklarasi fungsinya
```py
def function(x):
    return x*x + 9*x - 13
```

### Program Bolzano atau Biseksi  
```py
def bisection():
    global xl, xu
    for i in range(iterate):
        xr = (xl+xu)/2
        list_xr.append(xr)
        list_iterate.append(i+1)
        
        print(f"iterasi ke - {i+1}")
        print(f"xu dan xl: {xu} || {xl}")
        print(f"xr dan xt: {xr} || {xt}")

        et = round(math.fabs((xt-xr)/xt), 5)
        print(f"et: {et}\n")

        fxl = function(xl)
        fxr = function(xr)

        mul = round(fxl * fxr, 3)
        if(mul == 0):
            print(f"hasil faktor: {xr} ")
            return
        elif (mul) < 0:
            xu = xr
        elif mul > 0:
            xl = xr
```





