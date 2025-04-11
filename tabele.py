import mysql.connector as sql
import tkinter as tk
from tkinter import ttk
from tkinter import *

# ---------- DEF TWORZENIA ZAKŁADEK DO ODCZYTU ---------- #

# ----- otworz_dostawcy ----- #

def otworz_dostawcy(root_glowny,kursor):
    root_dostawcy = tk.Toplevel(root_glowny)
    root_dostawcy.title('TABELA DOSTAWCÓW')

    def odswiez_dostawcow():
        drzewo_dostawcy.delete(*drzewo_dostawcy.get_children())
        kursor.execute('select * from dostawcy')      
        wiersz_dostawcy = kursor.fetchall()                 
        for x in wiersz_dostawcy:                       
            drzewo_dostawcy.insert("", tk.END, values=x)      

    kursor.execute('select * from dostawcy')
    wiersz_dostawcy = kursor.fetchall()
    drzewo_dostawcy = ttk.Treeview(root_dostawcy,columns=('id','nazwa','adres','telefon','NIP','REGON','status'),show="headings")

    drzewo_dostawcy.heading("id", text="id")  
    drzewo_dostawcy.heading("nazwa", text="nazwa")  
    drzewo_dostawcy.heading("adres", text="adres")
    drzewo_dostawcy.heading("telefon", text="telefon")
    drzewo_dostawcy.heading("NIP", text="NIP")
    drzewo_dostawcy.heading("REGON", text="REGON")
    drzewo_dostawcy.heading("status", text="status")

    drzewo_dostawcy.column("id", width=15)
    drzewo_dostawcy.column("nazwa", width=150)
    drzewo_dostawcy.column("adres", width=300)
    drzewo_dostawcy.column("telefon", width=100)
    drzewo_dostawcy.column("NIP", width=100)
    drzewo_dostawcy.column("REGON", width=100)
    drzewo_dostawcy.column("status", width=100)

    for x in wiersz_dostawcy:
        drzewo_dostawcy.insert("", tk.END, values=x)
    drzewo_dostawcy.pack(expand=True, fill="both")
    b_odswiez = tk.Button(root_dostawcy, text="🔄 Odśwież", command=odswiez_dostawcow)
    b_odswiez.pack(pady=5)
    
# ----- otworz_produkty ----- #

def otworz_produkty(root_glowny,kursor):
    root_produkty = tk.Toplevel(root_glowny)
    root_produkty.title('TABELA PRODUKTÓW')

    def odswiez_produkty():
        drzewo_produkty.delete(*drzewo_produkty.get_children())
        kursor.execute('select * from produkty')
        wiersz_produkty = kursor.fetchall()
        for x in wiersz_produkty:
            drzewo_produkty.insert("", tk.END, values=x)

    kursor.execute('select * from produkty')
    wiersz_produkty = kursor.fetchall()
    drzewo_produkty = ttk.Treeview(root_produkty, columns=('id', 'id_dostawcy', 'cena_netto', 'cena_brutto', 'jednostka_miary', 'nazwa_produktu', 'status_zamowienia'), show="headings")

    drzewo_produkty.heading("id", text="id")
    drzewo_produkty.heading("id_dostawcy", text="id_dostawcy")
    drzewo_produkty.heading("cena_netto", text="cena_netto")
    drzewo_produkty.heading("cena_brutto", text="cena_brutto")
    drzewo_produkty.heading("jednostka_miary", text="jednostka_miary")
    drzewo_produkty.heading("nazwa_produktu", text="nazwa_produktu")
    drzewo_produkty.heading("status_zamowienia", text="status_zamowienia")

    drzewo_produkty.column("id", width=15)
    drzewo_produkty.column("id_dostawcy", width=100)
    drzewo_produkty.column("cena_netto", width=100)
    drzewo_produkty.column("cena_brutto", width=100)
    drzewo_produkty.column("jednostka_miary", width=120)
    drzewo_produkty.column("nazwa_produktu", width=200)
    drzewo_produkty.column("status_zamowienia", width=150)

    for x in wiersz_produkty:
        drzewo_produkty.insert("", tk.END, values=x)
    drzewo_produkty.pack(expand=True, fill="both")

    b_odswiez = tk.Button(root_produkty, text="🔄 Odśwież", command=odswiez_produkty)
    b_odswiez.pack(pady=5)

# ----- otworz_klienci ----- #

def otworz_klienci(root_glowny,kursor):
    root_klienci = tk.Toplevel(root_glowny)
    root_klienci.title('TABELA KLIENTÓW')

    def odswiez_klientow():
        drzewo_klienci.delete(*drzewo_klienci.get_children())
        kursor.execute('select * from klienci')
        wiersz_klienci = kursor.fetchall()
        for x in wiersz_klienci:
            drzewo_klienci.insert("", tk.END, values=x)

    kursor.execute('select * from klienci')
    wiersz_klienci = kursor.fetchall()
    drzewo_klienci = ttk.Treeview(root_klienci, columns=('id', 'nazwa', 'biznes_tak_nie', 'NIP', 'REGON', 'PESEL', 'adres', 'telefon', 'email', 'status'), show="headings")

    drzewo_klienci.heading("id", text="id")
    drzewo_klienci.heading("nazwa", text="nazwa")
    drzewo_klienci.heading("biznes_tak_nie", text="biznes_tak_nie")
    drzewo_klienci.heading("NIP", text="NIP")
    drzewo_klienci.heading("REGON", text="REGON")
    drzewo_klienci.heading("PESEL", text="PESEL")
    drzewo_klienci.heading("adres", text="adres")
    drzewo_klienci.heading("telefon", text="telefon")
    drzewo_klienci.heading("email", text="email")
    drzewo_klienci.heading("status", text="status")

    drzewo_klienci.column("id", width=15)
    drzewo_klienci.column("nazwa", width=150)
    drzewo_klienci.column("biznes_tak_nie", width=100)
    drzewo_klienci.column("NIP", width=100)
    drzewo_klienci.column("REGON", width=100)
    drzewo_klienci.column("PESEL", width=120)
    drzewo_klienci.column("adres", width=200)
    drzewo_klienci.column("telefon", width=120)
    drzewo_klienci.column("email", width=180)
    drzewo_klienci.column("status", width=100)

    for x in wiersz_klienci:
        drzewo_klienci.insert("", tk.END, values=x)
    drzewo_klienci.pack(expand=True, fill="both")

    b_odswiez = tk.Button(root_klienci, text="🔄 Odśwież", command=odswiez_klientow)
    b_odswiez.pack(pady=5)

# ----- otworz_faktury ----- #

def otworz_faktury(root_glowny,kursor):
    root_faktury = tk.Toplevel(root_glowny)
    root_faktury.title('TABELA FAKTUR')

    def odswiez_faktury():
        drzewo_faktury.delete(*drzewo_faktury.get_children())
        kursor.execute('select * from faktury')
        wiersz_faktury = kursor.fetchall()
        for x in wiersz_faktury:
            drzewo_faktury.insert("", tk.END, values=x)

    kursor.execute('select * from faktury')
    wiersz_faktury = kursor.fetchall()
    drzewo_faktury = ttk.Treeview(root_faktury, columns=('id', 'numer', 'data_wystawienia', 'data_sprzedazy', 'id_klienta', 'id_dostawcy', 'kwota_netto', 'kwota_brutto', 'sposob_platnosci'), show="headings")

    drzewo_faktury.heading("id", text="id")
    drzewo_faktury.heading("numer", text="numer")
    drzewo_faktury.heading("data_wystawienia", text="data_wystawienia")
    drzewo_faktury.heading("data_sprzedazy", text="data_sprzedazy")
    drzewo_faktury.heading("id_klienta", text="id_klienta")
    drzewo_faktury.heading("id_dostawcy", text="id_dostawcy")
    drzewo_faktury.heading("kwota_netto", text="kwota_netto")
    drzewo_faktury.heading("kwota_brutto", text="kwota_brutto")
    drzewo_faktury.heading("sposob_platnosci", text="sposob_platnosci")

    drzewo_faktury.column("id", width=15)
    drzewo_faktury.column("numer", width=100)
    drzewo_faktury.column("data_wystawienia", width=100)
    drzewo_faktury.column("data_sprzedazy", width=100)
    drzewo_faktury.column("id_klienta", width=100)
    drzewo_faktury.column("id_dostawcy", width=100)
    drzewo_faktury.column("kwota_netto", width=100)
    drzewo_faktury.column("kwota_brutto", width=100)
    drzewo_faktury.column("sposob_platnosci", width=180)

    for x in wiersz_faktury:
        drzewo_faktury.insert("", tk.END, values=x)
    drzewo_faktury.pack(expand=True, fill="both")

    b_odswiez = tk.Button(root_faktury, text="🔄 Odśwież", command=odswiez_faktury)
    b_odswiez.pack(pady=5)

# ----- otworz_zam_do_hurtowni ----- #

def otworz_zam_do_hurtowni(root_glowny,kursor):
    root_zam_do_hurtowni = tk.Toplevel(root_glowny)
    root_zam_do_hurtowni.title('ZAMÓWIENIA')

    def odswiez_zam_do_hurtowni():
        drzewo_zam_do_hurtowni.delete(*drzewo_zam_do_hurtowni.get_children())
        kursor.execute('select * from zam_do_hurtowni')
        wiersz_zam_do_hurtowni = kursor.fetchall()
        for x in wiersz_zam_do_hurtowni:
            drzewo_zam_do_hurtowni.insert("", tk.END, values=x)

    kursor.execute('select * from zam_do_hurtowni')
    wiersz_zam_do_hurtowni = kursor.fetchall()
    drzewo_zam_do_hurtowni = ttk.Treeview(root_zam_do_hurtowni, columns=('id', 'id_dostawcy', 'data_zamowienia', 'status', 'calkowita_kwota'), show="headings")

    drzewo_zam_do_hurtowni.heading("id", text="id")
    drzewo_zam_do_hurtowni.heading("id_dostawcy", text="id_dostawcy")
    drzewo_zam_do_hurtowni.heading("data_zamowienia", text="data_zamowienia")
    drzewo_zam_do_hurtowni.heading("status", text="status")
    drzewo_zam_do_hurtowni.heading("calkowita_kwota", text="calkowita_kwota")

    drzewo_zam_do_hurtowni.column("id", width=15)
    drzewo_zam_do_hurtowni.column("id_dostawcy", width=100)
    drzewo_zam_do_hurtowni.column("data_zamowienia", width=100)
    drzewo_zam_do_hurtowni.column("status", width=180)
    drzewo_zam_do_hurtowni.column("calkowita_kwota", width=200)

    for x in wiersz_zam_do_hurtowni:
        drzewo_zam_do_hurtowni.insert("", tk.END, values=x)
    drzewo_zam_do_hurtowni.pack(expand=True, fill="both")

    b_odswiez = tk.Button(root_zam_do_hurtowni, text="🔄 Odśwież", command=odswiez_zam_do_hurtowni)
    b_odswiez.pack(pady=5)

# ----- otworz_szczegolt_zam_do_hurtowni ----- #

def otworz_szczegolt_zam_do_hurtowni(root_glowny,kursor):
    root_szczegoly_zam_do_hurtowni = tk.Toplevel(root_glowny)
    root_szczegoly_zam_do_hurtowni.title('SZCZEGÓŁY ZAMÓWIENI')

    def odswiez_szczegoly_zam_do_hurtowni():
        drzewo_szczegoly.delete(*drzewo_szczegoly.get_children())
        kursor.execute('select * from szczegoly_zam_do_hurtowni')
        wiersz_szczegoly = kursor.fetchall()
        for x in wiersz_szczegoly:
            drzewo_szczegoly.insert("", tk.END, values=x)

    kursor.execute('select * from szczegoly_zam_do_hurtowni')
    wiersz_szczegoly = kursor.fetchall()
    drzewo_szczegoly = ttk.Treeview(root_szczegoly_zam_do_hurtowni, columns=('id', 'id_zam_do_hurt', 'id_produktu', 'ilosc', 'cena_suma'), show="headings")

    drzewo_szczegoly.heading("id", text="id")
    drzewo_szczegoly.heading("id_zam_do_hurt", text="id_zam_do_hurt")
    drzewo_szczegoly.heading("id_produktu", text="id_produktu")
    drzewo_szczegoly.heading("ilosc", text="ilosc")
    drzewo_szczegoly.heading("cena_suma", text="cena_suma")

    drzewo_szczegoly.column("id", width=15)
    drzewo_szczegoly.column("id_zam_do_hurt", width=100)
    drzewo_szczegoly.column("id_produktu", width=100)
    drzewo_szczegoly.column("ilosc", width=100)
    drzewo_szczegoly.column("cena_suma",width=100)

    for x in wiersz_szczegoly:
        drzewo_szczegoly.insert("", tk.END, values=x)
    drzewo_szczegoly.pack(expand=True, fill="both")

    b_odswiez = tk.Button(root_szczegoly_zam_do_hurtowni, text="🔄 Odśwież", command=odswiez_szczegoly_zam_do_hurtowni)
    b_odswiez.pack(pady=5)

# ----- otworz_sprzedaz_z_hurtowni ----- #

def otworz_sprzedaz_z_hurtowni(root_glowny,kursor):
    root_sprzedaz_z_hurtowni = tk.Toplevel(root_glowny)
    root_sprzedaz_z_hurtowni.title('SPRZEDAŻ')

    def odswiez_sprzedaz_z_hurtowni():
        drzewo_sprzedaz.delete(*drzewo_sprzedaz.get_children())
        kursor.execute('select * from sprzedaz_z_hurtowni')
        wiersz_sprzedaz = kursor.fetchall()
        for x in wiersz_sprzedaz:
            drzewo_sprzedaz.insert("", tk.END, values=x)

    kursor.execute('select * from sprzedaz_z_hurtowni')
    wiersz_sprzedaz = kursor.fetchall()
    drzewo_sprzedaz = ttk.Treeview(root_sprzedaz_z_hurtowni, columns=('id', 'id_klienta', 'data', 'status', 'kwota'), show="headings")

    drzewo_sprzedaz.heading("id", text="id")
    drzewo_sprzedaz.heading("id_klienta", text="id_klienta")
    drzewo_sprzedaz.heading("data", text="data")
    drzewo_sprzedaz.heading("status", text="status")
    drzewo_sprzedaz.heading("kwota", text="kwota")

    drzewo_sprzedaz.column("id", width=15)
    drzewo_sprzedaz.column("id_klienta", width=100),
    drzewo_sprzedaz.column("data",width=100)
    drzewo_sprzedaz.column("status", width=180)
    drzewo_sprzedaz.column("kwota", width=180)

    for x in wiersz_sprzedaz:
        drzewo_sprzedaz.insert("", tk.END, values=x)
    drzewo_sprzedaz.pack(expand=True, fill="both")

    b_odswiez = tk.Button(root_sprzedaz_z_hurtowni, text="🔄 Odśwież", command=odswiez_sprzedaz_z_hurtowni)
    b_odswiez.pack(pady=5)

# ----- otworz_szczegoly_sprz_z_hurtowni ----- #

def otworz_szczegoly_sprz_z_hurtowni(root_glowny,kursor):
    root_szczegoly_sprz_z_hurtowni = tk.Toplevel(root_glowny)
    root_szczegoly_sprz_z_hurtowni.title('SZCZEGÓŁY SPRZEDAŻY')

    def odswiez_szczegoly_sprz_z_hurtowni():
        drzewo_szczegoly.delete(*drzewo_szczegoly.get_children())
        kursor.execute('select * from szczegoly_sprz_z_hurtowni')
        wiersz_szczegoly = kursor.fetchall()
        for x in wiersz_szczegoly:
            drzewo_szczegoly.insert("", tk.END, values=x)

    kursor.execute('select * from szczegoly_sprz_z_hurtowni')
    wiersz_szczegoly = kursor.fetchall()
    drzewo_szczegoly = ttk.Treeview(root_szczegoly_sprz_z_hurtowni, columns=('id', 'id_sprz_z_hurt', 'id_produktu', 'ilosc', 'cena_suma'), show="headings")

    drzewo_szczegoly.heading("id", text="id")
    drzewo_szczegoly.heading("id_sprz_z_hurt", text="id_sprz_z_hurt")
    drzewo_szczegoly.heading("id_produktu", text="id_produktu")
    drzewo_szczegoly.heading("ilosc", text="ilosc")
    drzewo_szczegoly.heading("cena_suma", text="cena_suma")

    drzewo_szczegoly.column("id", width=15)
    drzewo_szczegoly.column("id_sprz_z_hurt", width=100)
    drzewo_szczegoly.column("id_produktu", width=100)
    drzewo_szczegoly.column("ilosc", width=100)
    drzewo_szczegoly.column("cena_suma", width=100)

    for x in wiersz_szczegoly:
        drzewo_szczegoly.insert("", tk.END, values=x)
    drzewo_szczegoly.pack(expand=True, fill="both")

    b_odswiez = tk.Button(root_szczegoly_sprz_z_hurtowni, text="🔄 Odśwież", command=odswiez_szczegoly_sprz_z_hurtowni)
    b_odswiez.pack(pady=5)
