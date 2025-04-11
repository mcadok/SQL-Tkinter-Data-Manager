import mysql.connector as sql
import tkinter as tk
from tkinter import ttk
from tkinter import *

from tabele import (
    otworz_dostawcy,
    otworz_faktury,
    otworz_klienci,
    otworz_produkty,
    otworz_sprzedaz_z_hurtowni,
    otworz_szczegolt_zam_do_hurtowni,
    otworz_szczegoly_sprz_z_hurtowni,
    otworz_zam_do_hurtowni
    )
from dodaj_wiersz import (
    otworz_DODAWANIE_dostawcy,
    otworz_DODAWANIE_faktury,
    otworz_DODAWANIE_klienci,
    otworz_DODAWANIE_produktow,
    otworz_DODAWANIE_sprzedaz_z_hurtowni,
    otworz_DODAWANIE_szczegoly_sprzedazy_z_hurtowni,
    otworz_DODAWANIE_szczegoly_zamowienia_do_hurtowni,
    otworz_DODAWANIE_zamowienia_do_hurtowni
    )
from usun_wiersz import (
    usuwanie_wierszy
)

# dane do polaczenia sie z DB
connect = sql.connect(
    host = '127.0.0.1',
    user = 'Admin',
    password = 'zaq1@WSX',
    database = 'hurtownia_mat_bud'
)

# inicjacja kursora
kursor = connect.cursor()
# tworzenie glownego okna
root_glowny = tk.Tk()
 
# ---------- ROOT GŁÓWNY ---------- #

napis_tablice_root_glowny = tk.Label(root_glowny,text='- - - -  TABLICE  - - - -',font=('Arial', 12, 'bold')).grid(row=0,column=0)

# guzik wlacz tabele
b_dostawcy = tk.Button(root_glowny,text='DOSTAWCY',command=lambda: otworz_dostawcy(root_glowny, kursor),width=50).grid(row=1, column=0, padx=5, pady=5)
b_produkty = tk.Button(root_glowny,text='PRODUKTY',command=lambda: otworz_produkty(root_glowny, kursor),width=50).grid(row=2, column=0, padx=5, pady=5)
b_klienci = tk.Button(root_glowny,text='KLIENCI',command=lambda: otworz_klienci(root_glowny, kursor),width=50).grid(row=3, column=0, padx=5, pady=5)
b_faktury = tk.Button(root_glowny,text='FAKTURY',command=lambda: otworz_faktury(root_glowny, kursor),width=50).grid(row=4, column=0, padx=5, pady=5)
b_zam_do_hurtowni = tk.Button(root_glowny,text='ZAMÓWIENIA',command=lambda: otworz_zam_do_hurtowni(root_glowny, kursor),width=50).grid(row=5, column=0, padx=5, pady=5)
b_sz_z_do_h = tk.Button(root_glowny,text='SZCZEGÓŁY ZAMÓWIEŃ',command=lambda: otworz_szczegolt_zam_do_hurtowni(root_glowny, kursor),width=50).grid(row=6, column=0, padx=5, pady=5)
b_sprz_z_hurtowni = tk.Button(root_glowny,text='SPRZEDAŻ',command=lambda: otworz_sprzedaz_z_hurtowni(root_glowny, kursor),width=50).grid(row=7, column=0, padx=5, pady=5)
b_sz_s_z_h = tk.Button(root_glowny,text='SZCZEGÓŁY SPRZEDAŻY',command=lambda: otworz_szczegoly_sprz_z_hurtowni(root_glowny, kursor),width=50).grid(row=8, column=0, padx=5, pady=5)

# guzik dodaj wiersz
b_dod_dostawcy = tk.Button(root_glowny,text='➕',command=lambda: otworz_DODAWANIE_dostawcy(root_glowny, kursor, connect),width=3).grid(row=1, column=1, padx=5, pady=5)
b_dod_produkty = tk.Button(root_glowny,text='➕',command=lambda: otworz_DODAWANIE_produktow(root_glowny, kursor, connect),width=3).grid(row=2, column=1, padx=5, pady=5)
b_dod_klienci = tk.Button(root_glowny,text='➕',command=lambda: otworz_DODAWANIE_klienci(root_glowny, kursor, connect),width=3).grid(row=3, column=1, padx=5, pady=5)
b_dod_faktury = tk.Button(root_glowny,text='➕',command=lambda: otworz_DODAWANIE_faktury(root_glowny, kursor, connect),width=3).grid(row=4, column=1, padx=5, pady=5)
b_dod_zam_do_hurtowni = tk.Button(root_glowny,text='➕',command=lambda: otworz_DODAWANIE_zamowienia_do_hurtowni(root_glowny, kursor, connect),width=3).grid(row=5, column=1, padx=5, pady=5)
b_dod_sz_z_do_h = tk.Button(root_glowny,text='➕',command=lambda: otworz_DODAWANIE_szczegoly_zamowienia_do_hurtowni(root_glowny, kursor, connect),width=3).grid(row=6, column=1, padx=5, pady=5)
b_dod_sprz_z_hurtowni = tk.Button(root_glowny,text='➕',command=lambda: otworz_DODAWANIE_sprzedaz_z_hurtowni(root_glowny, kursor, connect),width=3).grid(row=7, column=1, padx=5, pady=5)
b_dod_sz_s_z_h = tk.Button(root_glowny,text='➕',command=lambda: otworz_DODAWANIE_szczegoly_sprzedazy_z_hurtowni(root_glowny, kursor, connect),width=3).grid(row=8, column=1, padx=5, pady=5)

# guzik usuwanie wierszy
b_usuwanie_wierszy = tk.Button(root_glowny, text="USUWANIE REKORDÓW", command=lambda: usuwanie_wierszy(root_glowny, kursor, connect), width=50, bg="red", fg="white")
b_usuwanie_wierszy.grid(row=9, column=0, padx=5, pady=(30, 5), sticky="ew")



root_glowny.mainloop()
connect.close()