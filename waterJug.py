def DFS(a, b, target):
    visited = {}
    stack = [(0, 0)]
    path = []

    while stack:
        current = stack.pop()

        if current in visited:
            continue

        visited[current] = True
        path.append(current)

        if current[0] == target or current[1] == target:
            if current[0] == target:
                final_state = (target, 0)
            else:
                final_state = (target,0)
            
            path.append(final_state)
            
            for state in path:
                print(f"({state[0]}, {state[1]})")
            return

        next_states = [
            (a, current[1]),  
            (current[0], b),  
            (0, current[1]),  
            (current[0], 0),  
            (max(current[0] - (b - current[1]), 0), min(current[1] + current[0], b)),  
            (min(current[0] + current[1], a), max(current[1] - (a - current[0]), 0))   
        ]

        for state in next_states:
            if state not in visited and 0 <= state[0] <= a and 0 <= state[1] <= b:
                stack.append(state)

    print("No solution")

Jug1=int(input("\nEnter the capacity of jug-1:"))
Jug2=int(input("\nEnter the capacity of jug-2:"))
target=int(input("\nEnter the target capicity:"))
print("Path from initial state to solution state ::")
DFS(Jug1, Jug2, target)
