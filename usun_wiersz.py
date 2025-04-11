import mysql.connector as sql
import tkinter as tk
from tkinter import ttk
from tkinter import *

# ---------- DEF NA USUWANIE "➖" ---------- #

def usuwanie_wierszy(root_glowny,kursor,connect):
    def usun_rekord():
        tabela = tabela_var.get()
        rekord_id = id_var.get()

        if rekord_id == "":
            return

        klucz_glowny = {
            "dostawcy": "id_dostawcy",
            "produkty": "id_produktu",
            "klienci": "id_klienta",
            "faktury": "id_faktury",
            "zam_do_hurtowni": "id_zdh",
            "szczegoly_zam_do_hurtowni": "id_sz_zdh",
            "sprzedaz_z_hurtowni": "id_sprz_zh",
            "szczegoly_sprz_z_hurtowni": "id_sz_sprz_zh"
        }

        kolumna_id = klucz_glowny.get(tabela)

        if not kolumna_id:
            return

        try:
            kursor.execute(f"DELETE FROM {tabela} WHERE {kolumna_id} = %s", (rekord_id,))
            connect.commit()
        except Exception as e:
            print(f"Nie udało się usunąć rekordu: {e}")

    root_usuwanie_wierszy = tk.Toplevel(root_glowny)
    root_usuwanie_wierszy.geometry("350x350")
    root_usuwanie_wierszy.title("Usuwanie wiersza")

    opcje_wybor_tabeli = ["dostawcy", "klienci", "faktury", "produkty", "sprzedaz_z_hurtowni", 
                          "szczegoly_sprz_z_hurtowni", "szczegoly_zam_do_hurtowni", "zam_do_hurtowni"]

    tabela_var = tk.StringVar()
    tabela_var.set(opcje_wybor_tabeli[0])

    id_var = tk.StringVar()

    tabela_menu = tk.OptionMenu(root_usuwanie_wierszy, tabela_var, *opcje_wybor_tabeli)
    tabela_menu.pack(pady=10)

    id_label = tk.Label(root_usuwanie_wierszy, text="Podaj ID rekordu do usunięcia:")
    id_label.pack(pady=5)

    id_entry = tk.Entry(root_usuwanie_wierszy, textvariable=id_var)
    id_entry.pack(pady=5)

    usun_button = tk.Button(root_usuwanie_wierszy, text="Usuń rekord", command=usun_rekord)
    usun_button.pack(pady=20)
