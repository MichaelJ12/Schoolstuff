import random
  
while True:
    name: str = input("hallo, wat is jouw naam? ")
    if name.isalpha():
        break
    else:
        print("voer letters in!")

while True:
    try: 
        age: int = int(input(f"Oke {name} hoe oud ben jij? "))
        if type(age) == int:
            break
    except ValueError:
        print("voer een nummer in!")

birth_date: int = 2025 - age 
changed_birth_date: int = birth_date - 1

print(f"Welkom {name}, jij bent waarschijnlijk in {birth_date} geboren.")

# funcion to make sure the input is always j/n
dot = "."
guess = 0

def ask():
    while True:
        answer = input("is dit juist (j/n): ").lower()
        if answer in ("j", "n"):
            return answer
        print("vul (j/n) in")

answer = ask()
if answer == "j":
    print("Goed van mij he?!")
else:
    guess += 1
    print(f"Ah, sorry {name}, dat moet natuurlijk dan {changed_birth_date} zijn.")

    while True:
        answer = ask()
        if answer == "j":
            print(f"Niet slecht, in {guess} keer geraden!")
            break

        guess += 1
        new_birth_date = changed_birth_date - (guess - 1)
        print(f"Oh ehhh{dot} is het dan {new_birth_date}?")
        dot += "."

print("_" * 40)
 
while True:
    try:
        full_name: str = input("wat is jouw volledige naam?: ")
        while True:
            if type(full_name) == str:
                break
            else:
                print("voer letters in!")

        split_full_name = full_name.split()
        first_name = split_full_name[0]
        last_name = split_full_name[-1]
        if len(split_full_name) <= 1:
            print("vul jouw volledige naam in!")
        else:
            break
    except IndexError:
        print("vul jouw volledige naam in!")

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
        if 1 <= num < 11:
            break
        else:
            print("Het getal moet tussen 1 en 10 liggen.")
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