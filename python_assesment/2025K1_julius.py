import random

name: str = str(input("hallo, wat is jouw naam? "))
age: int = int(input(f"Oke {name} hoe oud ben jij? "))

birth_date: int = 2025 - age 
changed_birth_date: int = birth_date - 1


print(f"Welkom {name}, jij bent waarschijnlijk in {birth_date} geboren.")

answer_options: tuple = ("j", "n")

dot: str = '.' 

guess: int = 1

def ask():
    return input("is dit juist (j/n): ")

while True:
    answer = ask()

    if answer == "j":  
        print("Goed van mij he?!")
        break 
    else:
        guess += 1 
        print(f"Ah, sorry {name}, dat moet natuurlijk dan {changed_birth_date} zijn.")
        answer = ask()

        if answer == "j":
                print(f"Niet slecht, in {guess} keer geraden!")
                break

        while answer == "n":
            # update guess count
            guess += 1  

            # change your birth date guess
            new_birth_date = changed_birth_date - (guess - 1)  

            print(f"Oh ehhh{dot} is het dan {new_birth_date}?")
            dot += "."

            answer = ask()
        
        if answer == "j":
            print(f"Niet slecht, in {guess} keer geraden!")
            break

print("_" * 40)

full_name: str = input("wat is jouw volledige naam?: ")

split_full_name = full_name.split()
first_name = split_full_name[0]
last_name = split_full_name[-1]

print(f"Hoi {first_name}, een leuke fantasienaam voor jou is {last_name[::-1]}.")

color = [
    "rood",
    "blauw",
    "groen",
    "geel",
    "oranje",
    "paars",
    "roze",
    "bruin",
    "grijs",
    "turquoise"
]

print("_" * 40)

# ask the user for input (1-10)
while True:
    try:
        num = int(input("Voer een getal in tussen 1-10: "))
        if 0 <= num < 11:
            break
        else:
            print("Het getal moet tussen 0 en 10 liggen.")
    except ValueError:
        print("Voer een geldig getal in.")

# takes the color posistion in de list
chosen_color = color[num-1]  # -1 because the list starts with 0
print(f"Verrassing {first_name}! De {num}e kleur is {chosen_color}! Mooi he?")


def make_dict(num):
    geselecteerde_kleuren = random.sample(color, num)

    mine_dict = {}
    for colors in geselecteerde_kleuren:
        # genereer een willekeurig getal met 1 decimaal
        waarde = round(random.uniform(0, 10), 1)
            # vervang punt door komma
        waarde_str = str(waarde).replace(".", ",")
        # genereer willekeurig getal met komma
        mine_dict[colors] = waarde_str
    return mine_dict            


resultaat = make_dict(num)
print(resultaat)