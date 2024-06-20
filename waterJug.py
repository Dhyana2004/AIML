class WaterJugState:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

    def __eq__(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2

def dfs(current_state, visited, jug1_capacity, jug2_capacity, target_volume):
    if current_state.jug1 == target_volume or current_state.jug2 == target_volume:
        if current_state.jug1 == target_volume:
            print("Jug 1 now has", target_volume, "liters.")
        else:
            print("Jug 2 now has", target_volume, "liters.")
        return True
    
    visited.append((current_state.jug1, current_state.jug2))

    operations = [
        ('Fill Jug 1', jug1_capacity, current_state.jug2),
        ('Fill Jug 2', current_state.jug1, jug2_capacity),
        ('Empty Jug 1', 0, current_state.jug2),
        ('Empty Jug 2', current_state.jug1, 0),
        ('Pour Jug 1 to Jug 2', 
            max(0, current_state.jug1 + current_state.jug2 - jug2_capacity), 
            min(jug2_capacity, current_state.jug1 + current_state.jug2)),
        ('Pour Jug 2 to Jug 1', 
            min(jug1_capacity, current_state.jug1 + current_state.jug2), 
            max(0, current_state.jug1 + current_state.jug2 - jug1_capacity))
    ]

    for operation in operations:
        action, new_jug1, new_jug2 = operation
        new_state = WaterJugState(new_jug1, new_jug2)

        if (new_state.jug1, new_state.jug2) not in visited:
            print(f"Trying: {action} => ({new_jug1}, {new_jug2})")
            if dfs(new_state, visited, jug1_capacity, jug2_capacity, target_volume):
                return True

    return False

def solve_water_jug_problem(jug1_capacity, jug2_capacity, target_volume):
    initial_state = WaterJugState(0, 0)
    visited = []
    
    if dfs(initial_state, visited, jug1_capacity, jug2_capacity, target_volume):
        print("Solution found!")
    else:
        print("Solution not possible.")

jug1_capacity = int(input("Enter Jug 1 capacity: "))
jug2_capacity = int(input("Enter Jug 2 capacity: "))
target_volume = int(input("Enter Target Volume: "))

print(f"Solving Water Jug Problem with capacities ({jug1_capacity}, {jug2_capacity}) to measure {target_volume} liters.")
solve_water_jug_problem(jug1_capacity, jug2_capacity, target_volume)
