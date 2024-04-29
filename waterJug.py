def pour_water(jug1, jug2, capacity1, capacity2):
    # Pour water from jug1 to jug2
    pour_amount = min(jug1, capacity2 - jug2)
    jug1 -= pour_amount
    jug2 += pour_amount
    return jug1, jug2

def water_jug_solution(jug1_store, jug2_store, target):
    jug1 = 0
    jug2 = 0
    #steps = 0

    while True:
        # Check if the target is already achieved
        if jug1 == target or jug2 == target:
            print("The target is already achieved.")
            break

        # Fill jug1 if it's empty
        if jug1 == 0:
            jug1 = jug1_store
        # Empty jug2 if it's full
        elif jug2 == jug2_store:
            jug2 = 0
        # Pour water from jug1 to jug2
        else:
            jug1, jug2 = pour_water(jug1, jug2, jug1_store, jug2_store)

       # //steps += 1

   # //print(f"Steps taken: {steps}")

# Example usage
jug1_store = int(input("Enter the quantity of jug 1: "))
jug2_store = int(input("Enter the quantity of jug 2: "))
target = int(input("Enter the target value: "))

water_jug_solution(jug1_store, jug2_store, target)
