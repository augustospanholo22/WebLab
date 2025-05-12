ossos = str(input("Vertebrado ou invertebrado? ")).upper()
classe = str(input("Classe: ")).upper()
tipos = str(input("Tipo de animal: ")).upper()

if ossos == "VERTEBRADO":
    if classe == "AVE":
        if tipos == "CARNIVORO":
            print("Águia")
        if tipos == "ONIVORO":
            print("Pomba")

    if classe == "MAMIFERO":
        if tipos == "ONIVORO":
            print("Homem")
        if tipos == "HERBIVORO":
            print("Vaca")

if ossos == "INVERTEBRADO":
    if classe == "INSETO":
        if tipos == "HEMATOFAGO":
            print("Pulga")
        if tipos == "HERBIVORO":
            print("Lagarta")
    if classe == "ANELIDEO":
        if tipos == "HEMATOFAGO":
            print("Sanguessuga")
        if tipos == "ONIVORO":
            print("Minhoca")
