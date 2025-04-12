x = float(input("X: "))
y = float(input("Y: "))

if x == 0 and y == 0:
    print("Origem")

elif x == 0:
    print("Eixo X")

elif y ==0:
    print("Eixo Y")

else:
    if x > 0 and y > 0:
        print("Q1")

    elif x > 0 and y < 0:
        print("Q4")

    elif x < 0 and y > 0:
        print("Q2")

    elif x < 0 and y < 0:
        print("Q3")



