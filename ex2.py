import random

random_num = random.randint(1,5)


while True:
    num = int(input("Introduce un numero del 1 - 5 :  "))
    if random_num == num:
        print("well done")
        break
    else:
        print("mal")











