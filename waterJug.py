jug1_store = int(input("Enter the quantity of jug 1: "))
jug2_store = int(input("Enter the quantity of jug 2: "))
target = int(input("Enter the target value: "))
jug1 = int(input("Enter the initial value of jug 1: "))
jug2 = int(input("Enter the initial value of jug 2: "))

if jug1 == target or jug2 == target:
    print("The target is already achieved.")
    exit()

while True:
    jug1 = jug1_store
    while jug1 != 0 and jug2 != jug2_store:
        pour_water = min(jug1, jug2_store - jug2)
        jug1 -= pour_water
        jug2 += pour_water

    if jug1 == target or jug2 == target:
        print("The target is achieved.")
        break

    if jug1 == 0:
        jug1 = jug1_store
    else:
        jug2 = 0
