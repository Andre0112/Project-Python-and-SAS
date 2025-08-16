
#2.1
lista_1 = ["Damian Elena", "Grigorescu Marius", "OfficePro SRL", "Ciobanu Andreea", "Stanciu Vlad",
          "ProSolutions SRL", "SmartPrint SRL", "Universitatea Alexandru Ioan Cuza", "Cabinet Medical DentCare",
          "Dumitrescu Ioana"]
lista_2 = ["TechCorp SRL", "Popa Cristian", "MegaOffice SRL", "BrightTech SRL", "FlexiOffice SRL"]

print("Prima lista are urmatoarele elemente: \n", lista_1)
print("A doua lista are urmatoarele elemente: \n", lista_2)

lista_1.extend(lista_2)

print("Lista completa cu clientii fideli este: \n", lista_1)

lista_1.sort(reverse=True)

print("Lista sortata crescator cu clientii fideli este: \n", lista_1)

lista_1.append("Avramescu Andrei")

print("Lista cu 16 clienti fideli este: \n",lista_1)

lista_1.sort()

print("Lista finala a clientilor fideli este: \n", lista_1)

chei = {"Pix cu gel", "Marker permanent"}
valoare = "Pilot"

produse = dict.fromkeys(chei, valoare)
print("Dicționarul cu cele 2 produse este:\n", produse)

produse.update({"Biblioraft albastru": "Leitz"})
print("Dicționarul cu cele 3 produse este:\n", produse)

produse.update({"Set markere colorate": "Stabilo"})
print("Dicționarul cu cele 4 produse este:\n", produse)


#2.2.
#seturi
setPF = {'Pilot', 'Staedtler', 'Faber-Castell', 'Koh-I-Noor', 'Schneider'}
print("Setul corespunzator Brandurilor PF este: \n", setPF)
print(" ")

setPJ = {'Esselte', 'Navigator', 'Herlitz', 'Stabilo','Pilot', 'Faber-Castell', 'Mondi', 'Schneider'}
print("Setul corespunzator Brandurilor PJ este: \n", setPJ)
print(" ")

setComun = setPF.intersection(setPJ)
print("Brandurile comune din acele doua categorii sunt: \n", setComun)
print(" ")

setPJ.discard('Esselte')
setPJ.discard('Navigator')
print("Setul corespunzator Brandurilor PJ dupa eliminare: \n", setPJ)
print(" ")


setPF.add('Herlitz')
print("Setul corespunzator Brandurilor PF dupa adaugare: \n", setPF)
print(" ")

setComun_nou = setPF.intersection(setPJ)
print("Brandurile comune din cele doua categorii nou: \n", setComun_nou)
print(" ")

#tupluri
tupluIS = ('Liner cu varf de fibra', 'Marker tabla', 'Set pixuri', 'Set carioci', 'Marker permanent',
           'Carioci cu varf de pensula', 'Ascutitoare cu radiera', 'Creion mecanic', 'Marker tabla')
print("Stocul initial: \n", tupluIS)
print(" ")


tupluIS = tupluIS + ('Marker permanent', 'Pix cu gel', 'Marker tabla')
print("Stocul nou: \n", tupluIS)
print(" ")

print("Numarul de markere permanente este: \n", tupluIS.count('Marker permanent'))
print(" ")

print("Pozitia in care se afla Pixul cu gel este: \n", tupluIS.index('Pix cu gel'))
print(" ")
#2.3 definirea si apelarea unor functii

categorie = input("Introduceți categoria produsului: ")

def reduceripromo(produs_categorie):
    if produs_categorie == "Ambalare":
        y = 15
        print("Produsul beneficiaza de o reducere de ", y, "%")
    elif produs_categorie == "Articole generale de birou":
        y = 10
        print("Produsul beneficiaza de o reducere de ", y, "%")
    elif produs_categorie == "Organizare":
        y = 25
        print("Produsul beneficiaza de o reducere de ", y, "%")
    elif produs_categorie == "Rechizite scolare":
        y = 40
        print("Produsul beneficiaza de o reducere de ", y, "%")
    elif produs_categorie == "Accesorii de birou":
        y = 25
        print("Produsul beneficiaza de o reducere de ", y, "%")
    else:
        print("Produsul nu beneficiaza de reducere.")

reduceripromo(categorie)  # Apelăm funcția cu 'categorie' ca parametru


# 2.4
comanda = int(input("Introduceti numarul de produse comandate: "))

if comanda >= 2 and comanda <= 8:
    print("Comanda mica.")
elif comanda >= 12 and comanda <= 35:
    print("Comanda medie.")
elif comanda>40:
    print("Comanda mare.")
else:
    print("Numarul de produse este invalid. Introduceti un alt numar!")

print(" ")

#2.5

listaMF = ["penar", "creion", "stilou", "rucsac", "toc hartie", "biblioraft", "dosar plastic",
           "mapa", "acuarele", "agrafe de birou"]
listaCS = ["biblioraft", "agrafe de birou", "laminator", "pix", "radiera", "stilou", "toc hartie",
           "agenda", "capsator", "mapa"]

for x in listaMF:
    for y in listaCS:
        if x == y:  # Dacă produsul este în ambele liste
            print("Produsul", x, "este achiziționat de către Filimon Mihnea și Campta SRL.")



#2.6
import pandas as pd

# Calea fișierului CSV (folosește 'r' pentru a evita problemele cu caracterele de escape)
file_path = r"C:\Users\burca\Desktop\proiect phyton\date.csv"

# Citirea fișierului CSV
df = pd.read_csv(file_path, delimiter=";")

# Setarea opțiunilor pentru a vizualiza toate coloanele și toate liniile
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Afișarea DataFrame-ului
print(df)

#2.7
import pandas as pd

file_path = r"C:\Users\burca\Desktop\proiect phyton\dateclean.csv"

df = pd.read_csv(file_path, delimiter=",")

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print("Numele clientilor de pe randurile 4, 7, 23 și 36 respectiv fisierului .csv \n",
      "si valorile comenzilor inregistrate de acestia sunt: \n",
      df.iloc[[3, 6, 22, 35], [0, 9]])

# capul de tabel nu este luat in considerare ca linie, iar numerotarea in Python incepe
# de la 0, astfel scadem 2 din fiecare valoare
print("Codurile clientilor, denumirile produselor si preturile unitare aferente produselor \n",
      "din categoria 'Organizare' al ceror venit total depaseste 300 lei sunt: \n",
      df.loc[(df['Categorie'] == "Organizare") & (df['Total comandă'] > 300),
      ['Cod client', 'Denumire produs', 'Preț unitar']])

#2.8
import pandas as pd
file_path = r"C:\Users\burca\Desktop\proiect phyton\dateclean.csv"
df = pd.read_csv(file_path, delimiter=",")

print(df)
print(" ")

df_copy = df.copy()

# Afișarea produselor și procentului de reducere pentru categoria "Informatică și accesorii"
print("Procentul de reducere initial din categoria 'Informatică și accesorii':\n",
      df.loc[(df["Categorie"] == "Informatică și accesorii"), ["Denumire produs", "Procent de reducere"]])
print(" ")

# Modificarea procentului de reducere de la 25% la 20% pentru categoria "Informatică și accesorii"
df.loc[(df["Categorie"] == "Informatică și accesorii"), "Procent de reducere"] = 0.20

# Afișarea noii valori pentru procentul de reducere din aceleași produse
print("Procentul de reducere modificat din categoria 'Informatică și accesorii':\n",
      df.loc[(df["Categorie"] == "Informatică și accesorii"), ["Denumire produs", "Procent de reducere"]])
print(" ")


#2.9
import pandas as pd
file_path = r"C:\Users\burca\Desktop\proiect phyton\dateclean.csv"
df = pd.read_csv(file_path, delimiter=",")

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
SumaComenzi = df["Total comandă"].sum()
CantitateTotala = df["Cantitate comandată"].sum()
ProcentMediuReducere = df["Procent de reducere"].mean()
print("Suma totală a veniturilor comenzilor este: ", SumaComenzi)
print("Numărul total de produse comandate este: ", CantitateTotala)
print("Valoarea medie a procentului reducerilor este: ", ProcentMediuReducere, "%")


#2.10
import pandas as pd
dateLipsa = r"C:\Users\burca\Desktop\proiect phyton\dateclean1.csv"
df = pd.read_csv(dateLipsa)
print(df)
print(df['Preț unitar'])

# Afișarea doar a valorilor lipsă din coloana "Pret unitar"
print("Date lipsă în coloana 'Preț unitar':\n", df[df['Preț unitar'].isnull()])

# Înlocuirea valorilor lipsă din "Pret unitar" cu mesajul "Este gol"
df['Preț unitar'] = df['Preț unitar'].fillna("Este gol")

# Afișarea coloanei "Pret unitar" după înlocuirea valorilor lipsă
print("Coloana 'Preț unitar' după înlocuirea valorilor lipsă:\n", df['Preț unitar'])

# Salvarea datelor într-un fișier Excel
output_path = r"C:\Users\burca\Desktop\proiect phyton\date_curatate.xlsx"
df.to_excel(output_path, index=False)

print(f"Fișierul Excel a fost salvat la: {output_path}")


#2.11
import pandas as pd
df = pd.read_csv( r"C:\Users\burca\Desktop\proiect phyton\dateclean.csv", delimiter=",")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

coloane = ["Cod client", "Procent de reducere"]
df1 = df.drop(coloane, axis=1)
print("Dupa eliminarea coloanelor 'Cod client' si 'Procent de reducere', coloanele ramase sunt: \n", df1)

df3 = df.drop(df.index[10:36], axis=0)
print(" \n Dupa eliminarea randurilor de la 10 la 35, primele 5 randuri sunt: \n", df3)

#2.12
import pandas as pd
dateFolder = pd.read_csv(r"C:\Users\burca\Desktop\proiect phyton\dateclean.csv", delimiter=",")

print(dateFolder)
df = dateFolder.copy()

# Gruparea după coloanele "Categorie" și "Brand" și calcularea sumelor pentru "Total comanda" și minimului pentru "Pret unitar"
df1 = df.groupby(["Categorie", "Brand"]).agg({'Total comandă': "sum", 'Preț unitar': 'min'})

# Afișarea rezultatelor
print(df1)


#2.13

df = pd.read_csv(r"C:\Users\burca\Desktop\proiect phyton\dateclean.csv", delimiter=",")

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df1 = pd.read_csv(r"C:\Users\burca\Desktop\proiect phyton\comenzi1.csv", delimiter=",")

# Realizarea merge-ului pe baza coloanei "Cod client" cu opțiunea 'outer'
result = pd.merge(df, df1, on="Cod client", how="outer")

print(result)



# 2.14

df2 = dateFolder.copy()

#am dorit sa creez un plot in care sa se afiseze din coloana Categorie doar Instrumentele de scris
plot = df2[df2["Categorie"] == "Instrumente de scris"]

#am creat dupa acel plot, alaturi de functia .groupby() in care sa afiseze suma comenzilor utilizand functia .sum()
#dupa Brand si Total comanda
plot = plot.groupby("Brand")["Total comandă"].sum()

#am sortat valorile din acel grafic folosind functia .sort_values().plot() in care am specificat ca graficul sa fie
#de tip pie
plot.sort_values().plot(kind="pie")

#am folosit pachetul matplotlib pentru a putea afisa graficul folosind functia .show()
mplib.show()
