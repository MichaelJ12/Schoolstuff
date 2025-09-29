import random

print("hi welkom")
naam = input("wat is je naam: ")
getal = input("kies een getal tussen 5 en 10: ")

print(f"OK {naam}, jij hebt gekozen voor: {getal} ")

answer = input("is dit juist (j/n): ")

if answer == "j":
   nieuwe_getal = int(input(f"neem nu een nieuwe getal in je hoofd tussen 0 en 10: "))
else:
    nieuwe_getal = int(input(f"We gaan toch beginnen. Neem een nieuw getal in je hoofd tussen 0 en 10: "))


random_start_num = random.randint(1, 10)

gokken = []
count = 1 
even_count = 0 

print(f"Is het soms: {random_start_num}?")

answer = input("is dit juist (j/n): ")
gokken.append(random_start_num)
juist_getal = gokken[-1]

while answer == "n":
   random_num = random.randint(1, 10)
   gokken.append(random_num)
   juist_getal = gokken[-1]
   count += 1 
   answer = input(f"Oh ehhh… is het dan: {random_num}? ")
   if random_num % 2 == 0:
       even_count += 1
       
   if answer == "j":
        print(f"Niet slecht, in {count} keer geraden!")
        

print(
    f"Ik heb het volgende gegokt: {'-'.join(str(g) for g in gokken)}. "
    f"En het was {juist_getal}! "
    f"Ik heb {even_count} keer een even getal gegokt."
)

import random

# Lijst met 20 namen (hard-coded)
namen = ["Lucas", "Emma", "Saar", "Milan", "Noah", "Lotte", "Finn", "Tess", 
         "Sam", "Liam", "Eva", "Jesse", "Nina", "Max", "Anna", "Daan", "Bo", 
         "Levi", "Fien", "Olaf"]

def maak_omgekeerde_dict(getal):
    # Kies 'getal' unieke namen willekeurig uit de lijst
    gekozen_namen = random.sample(namen, getal)
    
    # Maak dictionary met omgekeerde waarden
    omgekeerde_dict = {naam: naam[::-1] for naam in gekozen_namen}
    
    return omgekeerde_dict

# Gebruiker invoer
while True:
    try:
        getal = int(input("Voer een getal in onder de 20: "))
        if 0 <= getal < 20:
            break
        else:
            print("Het getal moet tussen 0 en 19 liggen.")
    except ValueError:
        print("Voer een geldig getal in.")

# Verrassingstekst
gekozen_naam = namen[getal-1]  # pak de naam op die positie
print(f"Verrassing!{naam} De {getal}e naam is {gekozen_naam}!!")

# Dictionary maken en tonen
resultaat = maak_omgekeerde_dict(getal)
print("De dictionary is:", resultaat)
