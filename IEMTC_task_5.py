
def create_dictionary(names, numbers):
    result_dict = {}
    for i in range(len(names)):
        result_dict[names[i]] = numbers[i]
    return result_dict


names = [input(f"Enter name {i + 1}: ") for i in range(5)]
numbers = [int(input(f"Enter number corresponding to {names[i]}: ")) for i in range(5)]


data_array = [names, numbers]


result_dict = create_dictionary(data_array[0], data_array[1])

sorted_array = sorted(data_array[0], key=lambda x: result_dict[x])


print("Sorted array based on values:")
for name in sorted_array:
    print(f"{name}: {result_dict[name]}")
