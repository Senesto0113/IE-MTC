def find_solutions():
    solutions = []

    for x in range(11):
        for y in range(11 - x):
            z = 10 - x - y
            if 0 <= z <= 10:
                solutions.append((x, y, z))

    return solutions

all_solutions = find_solutions()
for solution in all_solutions:
    print(f"x = {solution[0]}, y = {solution[1]}, z = {solution[2]}")
