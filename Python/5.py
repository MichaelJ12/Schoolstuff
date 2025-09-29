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


random_num = random.randint(1, 10)

count = 0 
count += 1 
print(f"Is het soms: {random_num}?")

answer = input("is dit juist (j/n): ")

while answer == "n":
   count += 1 
   answer = input(f"Oh ehhh… is het dan: {random.randint(1, 10)}? ")
   if answer == "j":
        input(f"Niet slecht, in {count} keer geraden!")