import mysql.connector as sql
import tkinter as tk
from tkinter import ttk
from tkinter import *

# ---------- DEF NA TWORZENIE "➕" ---------- #

def otworz_DODAWANIE_dostawcy(root_glowny,kursor,connect):
    root_otworz_DODANIE_dostawcy = tk.Toplevel(root_glowny)
    root_otworz_DODANIE_dostawcy.geometry('470x300')
    root_otworz_DODANIE_dostawcy.title('DODAWANIE DANYCH - DOSTAWCY')

    dane_dostawcy = {
        'id': tk.StringVar(),
        'nazwa': tk.StringVar(),
        'adres': tk.StringVar(),
        'telefon': tk.StringVar(),
        'NIP': tk.StringVar(),
        'REGON': tk.StringVar(),
        'status': tk.StringVar()
    }
    
    tk.Label(root_otworz_DODANIE_dostawcy, text="id:").grid(row=0, column=0) # Etykieta
    tk.Label(root_otworz_DODANIE_dostawcy, text="AUTOMATYCZNIE").grid(row=0, column=1, padx=5, pady=5) # Etykieta
    
    tk.Label(root_otworz_DODANIE_dostawcy, text="nazwa:").grid(row=1, column=0) # Etykieta
    pole_nazwa = tk.Entry(root_otworz_DODANIE_dostawcy,textvariable=dane_dostawcy["nazwa"]).grid(row=1, column=1, padx=5, pady=5) # Pole do wpisu
    
    tk.Label(root_otworz_DODANIE_dostawcy, text="adres:").grid(row=2, column=0)
    pole_adres = tk.Entry(root_otworz_DODANIE_dostawcy,textvariable=dane_dostawcy["adres"]).grid(row=2, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_dostawcy, text="telefon:").grid(row=3, column=0)
    pole_tel = tk.Entry(root_otworz_DODANIE_dostawcy,textvariable=dane_dostawcy["telefon"]).grid(row=3, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_dostawcy, text="NIP:").grid(row=4, column=0)
    pole_NIP = tk.Entry(root_otworz_DODANIE_dostawcy,textvariable=dane_dostawcy["NIP"]).grid(row=4, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_dostawcy, text="REGON:").grid(row=5, column=0)
    pole_REGON = tk.Entry(root_otworz_DODANIE_dostawcy,textvariable=dane_dostawcy["REGON"]).grid(row=5, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_dostawcy, text="status:").grid(row=6, column=0)
    pole_status = tk.Entry(root_otworz_DODANIE_dostawcy,textvariable=dane_dostawcy["status"]).grid(row=6, column=1, padx=5, pady=5)

    def ZAPISZ_dostawce():
        kursor.execute("""
            INSERT INTO dostawcy (nazwa_dostawcy, adres, telefon, NIP, REGON, status)
            VALUES (%s, %s, %s, %s, %s, %s)
            """, (
            dane_dostawcy['nazwa'].get(),
            dane_dostawcy['adres'].get(),
            dane_dostawcy['telefon'].get(),
            dane_dostawcy['NIP'].get(),
            dane_dostawcy['REGON'].get(),
            dane_dostawcy['status'].get()
            ))

        connect.commit() # zapisanie zmian w MySql

    guzik_dodaj_dostawce = tk.Button(root_otworz_DODANIE_dostawcy,text='DODAJ',command=ZAPISZ_dostawce,width=20).place(x=300,y=250)


def otworz_DODAWANIE_produktow(root_glowny,kursor,connect):
    root_otworz_DODANIE_produktow = tk.Toplevel(root_glowny)
    root_otworz_DODANIE_produktow.geometry('470x300')
    root_otworz_DODANIE_produktow.title('DODAWANIE PRODUKTÓW')
    
    dane_produktu = {
        'id produktu': tk.StringVar(),
        'id dostawcy': tk.StringVar(),
        'cena netto': tk.StringVar(),
        'cena brutto': tk.StringVar(),
        'jednostka miary': tk.StringVar(),
        'nazwa produktu': tk.StringVar(),
        'status': tk.StringVar()
    }
    
    tk.Label(root_otworz_DODANIE_produktow, text="id produktu:").grid(row=0, column=0)
    tk.Label(root_otworz_DODANIE_produktow, text="AUTOMATYCZNIE").grid(row=0, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_produktow, text="id dostawcy:").grid(row=1, column=0)
    tk.Entry(root_otworz_DODANIE_produktow, textvariable=dane_produktu['id dostawcy']).grid(row=1, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_produktow, text="cena netto:").grid(row=2, column=0)
    tk.Entry(root_otworz_DODANIE_produktow, textvariable=dane_produktu['cena netto']).grid(row=2, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_produktow, text="cena brutto:").grid(row=3, column=0)
    tk.Entry(root_otworz_DODANIE_produktow, textvariable=dane_produktu['cena brutto']).grid(row=3, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_produktow, text="jednostka miary:").grid(row=4, column=0)
    tk.Entry(root_otworz_DODANIE_produktow, textvariable=dane_produktu['jednostka miary']).grid(row=4, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_produktow, text="nazwa produktu:").grid(row=5, column=0)
    tk.Entry(root_otworz_DODANIE_produktow, textvariable=dane_produktu['nazwa produktu']).grid(row=5, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_produktow, text="status:").grid(row=6, column=0)
    tk.Entry(root_otworz_DODANIE_produktow, textvariable=dane_produktu['status']).grid(row=6, column=1, padx=5, pady=5)

    def ZAPISZ_produkt():
        kursor.execute("""
            INSERT INTO produkty (id_dostawcy, cena_netto, cena_brutto, jednostka_miary, nazwa_produktu, status)
            VALUES (%s, %s, %s, %s, %s, %s)
            """, (
            dane_produktu['id dostawcy'].get(),
            dane_produktu['cena netto'].get(),
            dane_produktu['cena brutto'].get(),
            dane_produktu['jednostka miary'].get(),
            dane_produktu['nazwa produktu'].get(),
            dane_produktu['status'].get()
            ))

        connect.commit()

    tk.Button(root_otworz_DODANIE_produktow, text='DODAJ', command=ZAPISZ_produkt, width=20).place(x=300, y=250)

def otworz_DODAWANIE_klienci(root_glowny,kursor,connect):
    root_otworz_DODANIE_klienci = tk.Toplevel(root_glowny)
    root_otworz_DODANIE_klienci.geometry('470x300')
    root_otworz_DODANIE_klienci.title('DODAWANIE DANYCH - KLIENCI')

    dane_klienta = {
        'id': tk.StringVar(),
        'nazwa': tk.StringVar(),
        'biznes tak/nie': tk.StringVar(),
        'NIP': tk.StringVar(),
        'REGON': tk.StringVar(),
        'PESEL': tk.StringVar(),
        'adres': tk.StringVar(),
        'telefon': tk.StringVar(),
        'email': tk.StringVar(),
        'status': tk.StringVar()
    }
    
    tk.Label(root_otworz_DODANIE_klienci, text="id klienta:").grid(row=0, column=0)
    tk.Label(root_otworz_DODANIE_klienci, text="AUTOMATYCZNIE").grid(row=0, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_klienci, text="nazwa:").grid(row=1, column=0)
    tk.Entry(root_otworz_DODANIE_klienci, textvariable=dane_klienta['nazwa']).grid(row=1, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_klienci, text="biznes (tak/nie):").grid(row=2, column=0)
    tk.Entry(root_otworz_DODANIE_klienci, textvariable=dane_klienta['biznes tak/nie']).grid(row=2, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_klienci, text="NIP:").grid(row=3, column=0)
    tk.Entry(root_otworz_DODANIE_klienci, textvariable=dane_klienta['NIP']).grid(row=3, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_klienci, text="REGON:").grid(row=4, column=0)
    tk.Entry(root_otworz_DODANIE_klienci, textvariable=dane_klienta['REGON']).grid(row=4, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_klienci, text="PESEL:").grid(row=5, column=0)
    tk.Entry(root_otworz_DODANIE_klienci, textvariable=dane_klienta['PESEL']).grid(row=5, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_klienci, text="adres:").grid(row=6, column=0)
    tk.Entry(root_otworz_DODANIE_klienci, textvariable=dane_klienta['adres']).grid(row=6, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_klienci, text="telefon:").grid(row=7, column=0)
    tk.Entry(root_otworz_DODANIE_klienci, textvariable=dane_klienta['telefon']).grid(row=7, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_klienci, text="email:").grid(row=8, column=0)
    tk.Entry(root_otworz_DODANIE_klienci, textvariable=dane_klienta['email']).grid(row=8, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_klienci, text="status:").grid(row=9, column=0)
    tk.Entry(root_otworz_DODANIE_klienci, textvariable=dane_klienta['status']).grid(row=9, column=1, padx=5, pady=5)

    def ZAPISZ_klienta():
        kursor.execute("""
            INSERT INTO klienci (nazwa_klienta, biznes_tak_nie, NIP, REGON, PESEL, adres, telefon, email, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
            dane_klienta['nazwa'].get() if dane_klienta['nazwa'].get().strip() else None,
            dane_klienta['biznes tak/nie'].get() if dane_klienta['biznes tak/nie'].get().strip() else None,
            dane_klienta['NIP'].get() if dane_klienta['NIP'].get().strip() else None,
            dane_klienta['REGON'].get() if dane_klienta['REGON'].get().strip() else None,
            dane_klienta['PESEL'].get() if dane_klienta['PESEL'].get().strip() else None,
            dane_klienta['adres'].get() if dane_klienta['adres'].get().strip() else None,
            dane_klienta['telefon'].get() if dane_klienta['telefon'].get().strip() else None,
            dane_klienta['email'].get() if dane_klienta['email'].get().strip() else None,
            dane_klienta['status'].get() if dane_klienta['status'].get().strip() else None
        ))
            
        connect.commit()

    tk.Button(root_otworz_DODANIE_klienci, text='DODAJ', command=ZAPISZ_klienta, width=20).place(x=300,y=250)

def otworz_DODAWANIE_faktury(root_glowny,kursor,connect):
    root_otworz_DODANIE_faktury = tk.Toplevel(root_glowny)
    root_otworz_DODANIE_faktury.geometry('600x400')
    root_otworz_DODANIE_faktury.title('DODAWANIE DANYCH - FAKTURY')

    dane_faktury = {
        'id faktury': tk.StringVar(),
        'nr_faktury': tk.StringVar(),
        'data wystawienia': tk.StringVar(),
        'data sprzedazy': tk.StringVar(),
        'id klienta': tk.StringVar(),
        'id dostawcy': tk.StringVar(),
        'kwota netto': tk.StringVar(),
        'kwota brutto': tk.StringVar(),
        'sposob zaplaty': tk.StringVar()
    }
    
    tk.Label(root_otworz_DODANIE_faktury, text="id:").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(root_otworz_DODANIE_faktury, text="AUTOMATYCZNIE").grid(row=0, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_faktury, text="nr faktury:").grid(row=1, column=0, padx=5, pady=5)
    tk.Entry(root_otworz_DODANIE_faktury, textvariable=dane_faktury['nr_faktury']).grid(row=1, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_faktury, text="data wystawienia:").grid(row=2, column=0, padx=5, pady=5)
    tk.Entry(root_otworz_DODANIE_faktury, textvariable=dane_faktury['data wystawienia']).grid(row=2, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_faktury, text="data sprzedazy:").grid(row=3, column=0, padx=5, pady=5)
    tk.Entry(root_otworz_DODANIE_faktury, textvariable=dane_faktury['data sprzedazy']).grid(row=3, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_faktury, text="id klienta:").grid(row=4, column=0, padx=5, pady=5)
    tk.Entry(root_otworz_DODANIE_faktury, textvariable=dane_faktury['id klienta']).grid(row=4, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_faktury, text="id dostawcy:").grid(row=5, column=0, padx=5, pady=5)
    tk.Entry(root_otworz_DODANIE_faktury, textvariable=dane_faktury['id dostawcy']).grid(row=5, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_faktury, text="kwota netto:").grid(row=6, column=0, padx=5, pady=5)
    tk.Entry(root_otworz_DODANIE_faktury, textvariable=dane_faktury['kwota netto']).grid(row=6, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_faktury, text="kwota brutto:").grid(row=7, column=0, padx=5, pady=5)
    tk.Entry(root_otworz_DODANIE_faktury, textvariable=dane_faktury['kwota brutto']).grid(row=7, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_faktury, text="sposob platnosci:").grid(row=8, column=0, padx=5, pady=5)
    tk.Entry(root_otworz_DODANIE_faktury, textvariable=dane_faktury['sposob zaplaty']).grid(row=8, column=1, padx=5, pady=5)

    def ZAPISZ_fakture():
        kursor.execute("""
            INSERT INTO faktury (nr_faktury, data_wystawienia, data_sprzedazy, id_klienta, id_dostawcy, kwota_netto, kwota_brutto, sposob_platnosci)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
            dane_faktury['nr_faktury'].get(),
            dane_faktury['data wystawienia'].get(),
            dane_faktury['data sprzedazy'].get(),
            dane_faktury['id klienta'].get(),
            dane_faktury['id dostawcy'].get(),
            dane_faktury['kwota netto'].get(),
            dane_faktury['kwota brutto'].get(),
            dane_faktury['sposob zaplaty'].get()
            ))
        connect.commit()

    tk.Button(root_otworz_DODANIE_faktury, text='DODAJ', command=ZAPISZ_fakture, width=20).place(x=300,y=250)

def otworz_DODAWANIE_zamowienia_do_hurtowni(root_glowny,kursor,connect):
    root_otworz_DODANIE_zamowienia = tk.Toplevel(root_glowny)
    root_otworz_DODANIE_zamowienia.geometry('470x300')
    root_otworz_DODANIE_zamowienia.title('DODAWANIE ZAMÓWIENIA DO HURTOWNI')

    dane_zam_do_hurt = {
        'id_zdh': tk.StringVar(),
        'dostawca': tk.StringVar(),
        'data zamowienia': tk.StringVar(),
        'status': tk.StringVar(),
        'calkowita kwota': tk.StringVar()
    }
    
    tk.Label(root_otworz_DODANIE_zamowienia, text="id_zdh:").grid(row=0, column=0)
    tk.Label(root_otworz_DODANIE_zamowienia, text="AUTOMATYCZNIE").grid(row=0, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_zamowienia, text="dostawca:").grid(row=1, column=0)
    tk.Entry(root_otworz_DODANIE_zamowienia, textvariable=dane_zam_do_hurt['dostawca']).grid(row=1, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_zamowienia, text="data_zamowienia:").grid(row=2, column=0)
    tk.Entry(root_otworz_DODANIE_zamowienia, textvariable=dane_zam_do_hurt['data zamowienia']).grid(row=2, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_zamowienia, text="status:").grid(row=3, column=0)
    tk.Entry(root_otworz_DODANIE_zamowienia, textvariable=dane_zam_do_hurt['status']).grid(row=3, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_zamowienia, text="calkowita kwota:").grid(row=4, column=0)
    tk.Entry(root_otworz_DODANIE_zamowienia, textvariable=dane_zam_do_hurt['calkowita kwota']).grid(row=4, column=1, padx=5, pady=5)

    def ZAPISZ_zamownieie_do_hurtowni():
        kursor.execute("""
            INSERT INTO zam_do_hurtowni (dostawca, data_zamowienia, status, calkowita_kwota)
            VALUES (%s, %s, %s, %s)
            """, (
            dane_zam_do_hurt['dostawca'].get(),
            dane_zam_do_hurt['data zamowienia'].get(),
            dane_zam_do_hurt['status'].get(),
            dane_zam_do_hurt['calkowita kwota'].get().replace(",", "."),
            ))

        connect.commit()

    tk.Button(root_otworz_DODANIE_zamowienia, text='DODAJ', command=ZAPISZ_zamownieie_do_hurtowni, width=20).place(x=300,y=250)

def otworz_DODAWANIE_szczegoly_zamowienia_do_hurtowni(root_glowny,kursor,connect):
    root_otworz_DODANIE_szczegoly = tk.Toplevel(root_glowny)
    root_otworz_DODANIE_szczegoly.geometry('470x300')
    root_otworz_DODANIE_szczegoly.title('DODAWANIE SZCZEGÓŁÓW ZAMÓWIENIA DO HURTOWNI')

    dane_szcz_zam_do_hurt = {
        'id_sz_zdh': tk.StringVar(),
        'id_zdh': tk.StringVar(),
        'id_produktu': tk.StringVar(),
        'ilosc': tk.StringVar(),
        'cena_suma': tk.StringVar()
    }
    
    tk.Label(root_otworz_DODANIE_szczegoly, text="id_sz_zdh:").grid(row=0, column=0)
    tk.Label(root_otworz_DODANIE_szczegoly, text="AUTOMATYCZNIE").grid(row=0, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_szczegoly, text="id_zdh:").grid(row=1, column=0)
    tk.Entry(root_otworz_DODANIE_szczegoly, textvariable=dane_szcz_zam_do_hurt['id_zdh']).grid(row=1, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_szczegoly, text="id_produktu:").grid(row=2, column=0)
    tk.Entry(root_otworz_DODANIE_szczegoly, textvariable=dane_szcz_zam_do_hurt['id_produktu']).grid(row=2, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_szczegoly, text="ilość:").grid(row=3, column=0)
    tk.Entry(root_otworz_DODANIE_szczegoly, textvariable=dane_szcz_zam_do_hurt['ilosc']).grid(row=3, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_szczegoly, text="cena_suma:").grid(row=4, column=0)
    tk.Entry(root_otworz_DODANIE_szczegoly, textvariable=dane_szcz_zam_do_hurt['cena_suma']).grid(row=4, column=1, padx=5, pady=5)

    def ZAPISZ_szcz_zam_do_hurt():
        kursor.execute("""
            INSERT INTO szczegoly_zam_do_hurtowni (id_zdh, id_produktu, ilosc, cena_suma)
            VALUES (%s, %s, %s, %s)
            """, (
            dane_szcz_zam_do_hurt['id_zdh'].get(),
            dane_szcz_zam_do_hurt['id_produktu'].get(),
            dane_szcz_zam_do_hurt['ilosc'].get(),
            dane_szcz_zam_do_hurt['cena_suma'].get().replace(",", ".")
            ))
        connect.commit()

    tk.Button(root_otworz_DODANIE_szczegoly, text='DODAJ', command=ZAPISZ_szcz_zam_do_hurt, width=20).place(x=300,y=250)

def otworz_DODAWANIE_sprzedaz_z_hurtowni(root_glowny,kursor,connect):
    root_otworz_DODANIE_sprzedaz = tk.Toplevel(root_glowny)
    root_otworz_DODANIE_sprzedaz.geometry('470x300')
    root_otworz_DODANIE_sprzedaz.title('DODAWANIE SPRZEDAŻY Z HURTOWNI')

    dane_sprz_z_hurt = {
        'id_sprz_zh': tk.StringVar(),
        'id_klienta': tk.StringVar(),
        'data sprzedazy': tk.StringVar(),
        'status': tk.StringVar(),
        'calkowita kwota': tk.StringVar()
    }
    
    tk.Label(root_otworz_DODANIE_sprzedaz, text="id_sprz_zh:").grid(row=0, column=0)
    tk.Label(root_otworz_DODANIE_sprzedaz, text="AUTOMATYCZNIE").grid(row=0, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_sprzedaz, text="id_klienta:").grid(row=1, column=0)
    tk.Entry(root_otworz_DODANIE_sprzedaz, textvariable=dane_sprz_z_hurt['id_klienta']).grid(row=1, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_sprzedaz, text="data sprzedazy:").grid(row=2, column=0)
    tk.Entry(root_otworz_DODANIE_sprzedaz, textvariable=dane_sprz_z_hurt['data sprzedazy']).grid(row=2, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_sprzedaz, text="status:").grid(row=3, column=0)
    tk.Entry(root_otworz_DODANIE_sprzedaz, textvariable=dane_sprz_z_hurt['status']).grid(row=3, column=1, padx=5, pady=5)
    
    tk.Label(root_otworz_DODANIE_sprzedaz, text="calkowita kwota:").grid(row=4, column=0)
    tk.Entry(root_otworz_DODANIE_sprzedaz, textvariable=dane_sprz_z_hurt['calkowita kwota']).grid(row=4, column=1, padx=5, pady=5)

    def ZAPISZ_sprzedaz_z_hurtowni():
        kursor.execute("""
            INSERT INTO sprzedaz_z_hurtowni (klient, data_sprzedazy, status, calkowita_kwota)
            VALUES (%s, %s, %s, %s)
            """, (
            dane_sprz_z_hurt['id_klienta'].get(),
            dane_sprz_z_hurt['data sprzedazy'].get(),
            dane_sprz_z_hurt['status'].get(),
            dane_sprz_z_hurt['calkowita kwota'].get().replace(",", ".")
            ))
        connect.commit()

    tk.Button(root_otworz_DODANIE_sprzedaz, text='DODAJ', command=ZAPISZ_sprzedaz_z_hurtowni, width=20).place(x=300,y=250)
    
def otworz_DODAWANIE_szczegoly_sprzedazy_z_hurtowni(root_glowny,kursor,connect):
    root_otworz_DODANIE_szczegoly_sprzedaz = tk.Toplevel(root_glowny)
    root_otworz_DODANIE_szczegoly_sprzedaz.geometry('470x300')
    root_otworz_DODANIE_szczegoly_sprzedaz.title('DODAWANIE SZCZEGÓŁÓW SPRZEDAŻY Z HURTOWNI')

    dane_szcz_sprz_z_hurt = {
        'id_sz_sprz_zh': tk.StringVar(),
        'id_sprz_zh': tk.StringVar(),
        'id_produktu': tk.StringVar(),
        'ilosc': tk.StringVar(),
        'cena_suma': tk.StringVar()
    }
    
    # ID szczegółów sprzedaży (automatyczne)
    tk.Label(root_otworz_DODANIE_szczegoly_sprzedaz, text="id_sz_sprz_zh:").grid(row=0, column=0)
    tk.Label(root_otworz_DODANIE_szczegoly_sprzedaz, text="AUTOMATYCZNIE").grid(row=0, column=1, padx=5, pady=5)
    
    # ID sprzedaży
    tk.Label(root_otworz_DODANIE_szczegoly_sprzedaz, text="id_sprz_zh:").grid(row=1, column=0)
    tk.Entry(root_otworz_DODANIE_szczegoly_sprzedaz, textvariable=dane_szcz_sprz_z_hurt['id_sprz_zh']).grid(row=1, column=1, padx=5, pady=5)
    
    # ID produktu
    tk.Label(root_otworz_DODANIE_szczegoly_sprzedaz, text="id_produktu:").grid(row=2, column=0)
    tk.Entry(root_otworz_DODANIE_szczegoly_sprzedaz, textvariable=dane_szcz_sprz_z_hurt['id_produktu']).grid(row=2, column=1, padx=5, pady=5)
    
    # Ilość
    tk.Label(root_otworz_DODANIE_szczegoly_sprzedaz, text="ilość:").grid(row=3, column=0)
    tk.Entry(root_otworz_DODANIE_szczegoly_sprzedaz, textvariable=dane_szcz_sprz_z_hurt['ilosc']).grid(row=3, column=1, padx=5, pady=5)
    
    # Cena suma
    tk.Label(root_otworz_DODANIE_szczegoly_sprzedaz, text="cena_suma:").grid(row=4, column=0)
    tk.Entry(root_otworz_DODANIE_szczegoly_sprzedaz, textvariable=dane_szcz_sprz_z_hurt['cena_suma']).grid(row=4, column=1, padx=5, pady=5)

    def ZAPISZ_szcz_sprz_z_hurt():
        kursor.execute("""
            INSERT INTO szczegoly_sprz_z_hurtowni (id_sprz_zh, id_produktu, ilosc, cena_suma)
            VALUES (%s, %s, %s, %s)
            """, (
            dane_szcz_sprz_z_hurt['id_sprz_zh'].get(),
            dane_szcz_sprz_z_hurt['id_produktu'].get(),
            dane_szcz_sprz_z_hurt['ilosc'].get(),
            dane_szcz_sprz_z_hurt['cena_suma'].get().replace(",", ".")
            ))
        connect.commit()

    tk.Button(root_otworz_DODANIE_szczegoly_sprzedaz, text='DODAJ', command=ZAPISZ_szcz_sprz_z_hurt,width=20).place(x=300, y=250)
    