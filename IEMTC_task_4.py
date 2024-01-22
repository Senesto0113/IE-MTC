def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))


if start >= end:
    print("Invalid input. Starting number should be less than the ending number.")
else:
   
    print(f"Prime numbers between {start} and {end}:")
    for number in range(start, end + 1):
        if is_prime(number):
            print(number)
