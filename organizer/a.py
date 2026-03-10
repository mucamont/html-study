from datetime import datetime
name = input("Hallo, wie heisst du? ")

jetzt = datetime.now().hour

if jetzt < 11.59:
    print(f"Guten Morgan Herr {name}")
elif jetzt >= 12 & jetzt < 18:
    print(f"Guten Tag {name}")
else:
    print(f"Good Nacht Herr {name}")

