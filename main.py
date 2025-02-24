import tkinter
from tkinter import ttk
import math

def calculate_bearing():
    miesto1 = (miesto1_entry.get()).split(",")
    miesto2 = (miesto2_entry.get()).split(",")

    if (miesto1_entry.get() != "" and miesto2_entry.get() != "") and (len(miesto1) == 2 and len(miesto2) == 2):
        lat1, lon1, lat2, lon2 = miesto1[0], miesto1[1], miesto2[0], miesto2[1]
        lat1, lon1, lat2, lon2 = float(lat1), float(lon1), float(lat2), float(lon2)  

        # Convert degrees to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        
        # Compute differences
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        # Compute initial bearing
        x = math.sin(dlon) * math.cos(lat2)
        y = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)
        
        initial_bearing = math.atan2(x, y)
        
        # Convert radians to degrees
        initial_bearing = math.degrees(initial_bearing)
        
        # Normalize to 0–360 degrees
        compass_bearing = round((initial_bearing + 360) % 360, 2)

        # Radius of Earth in km (use 3958.8 for miles)
        R = 6371  

        # Haversine formula
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        # Compute distance
        distance = round(R * c, 2)
        
        #vysledky smeru a vzdialenosti
        vysledok_label_smer.config(text=f"{compass_bearing}")
        vysledok_label_vzdialenost.config(text=f"{distance}")
        
        text1.delete(1.0, tkinter.END)
        text2.delete(1.0, tkinter.END)

        text1.insert(1.0, f"{miesto1[0]}, {miesto1[1]}")
        text2.insert(1.0, f"{miesto2[0]}, {miesto2[1]}")
        
        #vymazanie entry polí 
        miesto1_entry.delete(0, tkinter.END)
        miesto2_entry.delete(0, tkinter.END)

    else:
        #ERROR okno
        error_window = tkinter.Tk()
        error_window.title("Chyba")
        error_frame = tkinter.Frame(error_window)
        error_frame.pack()

        #hláška o zlom vyplnení
        chyba_hlaska = tkinter.Label(error_frame, text="Zle vyplnené údaje miest.", font=("Arial", 15, "bold"))
        chyba_hlaska.grid(column=0, row=0, padx=5, pady=5)

        #informácie o správnom formáte údajov
        spravny_format = tkinter.Label(error_frame, text="Príklad správneho formátu údajov:\n\n48.729637979744375, 19.136377993823103\n\n")
        spravny_format.grid(column=0, row=1, padx=5, pady=5)

        #tlačidlo na zatvorenie chybovej hlášky
        tlacidlo_error = tkinter.Button(error_frame, text="OK", command=error_window.destroy) 
        tlacidlo_error.grid(column=0, row=2, sticky="nesw", padx=30, pady=20)

#okno
window = tkinter.Tk()
window.title("Kompas")

#frame okna
frame = tkinter.Frame(window)
frame.pack()

#udaje o miestach
udaje_miesta = tkinter.LabelFrame(frame, text="Zadajte súradnice prvého a druhého miesta")
udaje_miesta.grid(column=0, row=0, padx=10, pady=10)

miesto1_label = tkinter.Label(udaje_miesta, text="Prvé miesto", width=11, anchor="w")   
miesto1_label.grid(column=0, row=0)

miesto2_label = tkinter.Label(udaje_miesta, text="Druhé miesto", width=11, anchor="w")    
miesto2_label.grid(column=0, row=1)

miesto1_entry = tkinter.Entry(udaje_miesta, width=40)
miesto1_entry.grid(column=1, row=0)

miesto2_entry = tkinter.Entry(udaje_miesta, width=40)
miesto2_entry.grid(column=1, row=1)

for widget in udaje_miesta.winfo_children():
    widget.grid(padx=5, pady=5)

# tlacidlo na vypocet
button = tkinter.Button(frame, text="Vypočítať", command=calculate_bearing)
button.grid(column=0, row=1, sticky="nesw", padx=10, pady=10)

#zadane hodnoty
zadane_hodnoty = tkinter.LabelFrame(frame, text="Zadané hodnoty")
zadane_hodnoty.grid(column=0, row=2, sticky="news", padx=10, pady=10)

miesto1_label_zadane = tkinter.Label(zadane_hodnoty, text="Prvé miesto:", width=11, anchor="w")
miesto1_label_zadane.grid(column=0, row=0)

miesto2_label_zadane = tkinter.Label(zadane_hodnoty, text="Druhé miesto:", width=11, anchor="w")
miesto2_label_zadane.grid(column=0, row=1)

#text zadanych suradnic
text1 = tkinter.Text(zadane_hodnoty, wrap="word", height=1, font=("Arial", 8))
text2 = tkinter.Text(zadane_hodnoty, wrap="word", height=1, font=("Arial", 8))
text2.grid(column=1, row=1)
text1.grid(column=1, row=0)
text1.config(width=40)
text2.config(width=40)

# vysledok
vysledok = tkinter.LabelFrame(frame, text="Výsledok")
vysledok.grid(column=0, row=3, sticky="news", padx=10, pady=10)

smer_frame = tkinter.LabelFrame(vysledok, text="Smer")
smer_frame.grid(column=0, row=0,padx=5, pady=5)   

vzdialenost_frame = tkinter.LabelFrame(vysledok, text="Vzdialenosť")
vzdialenost_frame.grid(column=1, row=0,padx=5, pady=5)

vysledok_label_smer = tkinter.Label(smer_frame, text="0",width=15, font=("Helvetica", 16))
vysledok_label_smer.grid(column=0, row=0)

vysledok_label_vzdialenost = tkinter.Label(vzdialenost_frame, text="0",width=15, font=("Helvetica", 16))
vysledok_label_vzdialenost.grid(column=0, row=0)

window.mainloop()