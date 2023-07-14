

prim = int(input("Primeiro termo: "))
raz = int(input("Razão da PA: "))

dec = (prim + (10 - 1) * raz)  

counter = prim
while counter <= dec:
    print("{}".format(counter))
    counter += raz