import requests

spzky = set()

soubor = open('spztky.txt', encoding='utf-8')
for spzka in soubor:
    spzky.add(spzka.strip())
soubor.close()

while True:
    vidim = input("Vidíš nějakou SPZku? ").strip()
    print("Takže ty tvrdíš, že vidíš:", vidim)
    
    if vidim in spzky:
        print("SPZka je zaplacena!")
    else:
        odpoved = requests.get("http://spz.anilinux.org/kontrola", params={'spz': vidim})
        data = odpoved.json()
        
        if "error" in data:
            print("Něco se pokazilo.")
        elif data["kontrola"] == "platna":
            print("Vypadalo to, že je neplatná, ale prý mezi tím zaplatil.")
        else:
            print("Chytili jsme neplatiče.")
