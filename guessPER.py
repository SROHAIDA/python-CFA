#!/usr/bin/env python

import random

# Senarai perkataan untuk permainan
perkataan = ["merah", "hijau", "kuning", "hitam", "putih", "biru"]

# Pilih perkataan secara rawak dari senarai
perkataan_terpilih = random.choice(perkataan)

# mengisytiharkan pembolehubah
percubaan = 3
huruf_diteka = []
huruf_betul = []

# Paparkan mesej permulaan
print("Selamat datang ke Permainan MENEKA WARNA KEGEMARAN!")
print(f"Teka perkataan {len(perkataan_terpilih)} huruf.")

# Pusingan utama permainan
while percubaan > 0:
    # Paparkan perkataan dengan garisan bawah untuk huruf yang belum diteka
    paparan_perkataan = ""
    for huruf in perkataan_terpilih:
        if huruf in huruf_betul:
            paparan_perkataan += huruf
        else:
            paparan_perkataan += "_"
    print(f"Perkataan: {paparan_perkataan}")

    # Tanya pengguna untuk meneka huruf
    tekaan = input("Masukkan huruf: ").lower()

    # Semak jika tekaan adalah sah (hanya satu huruf)
    if len(tekaan) != 1 or not tekaan.isalpha():
        print("Input tidak sah. Sila masukkan satu huruf.")
        continue

    # Semak jika tekaan betul
    if tekaan in perkataan_terpilih:
        print("Tekaan betul!")
        huruf_betul.append(tekaan)
    else:
        print("Tekaan salah.")
        percubaan -= 1

    # Semak jika pengguna telah menebak keseluruhan perkataan
    if set(huruf_betul) == set(perkataan_terpilih):
        print(f"Tahniah! Anda telah MENEKA WARNA: {perkataan_terpilih}")
        break

# Akhir permainan
if percubaan == 0:
    print(f"Permainan tamat! WARNA adalah: {perkataan_terpilih}")
