import random

print(" Random Number Generator")
print("The computer will generate random numbers between the min and max you choose.\n")

while True:
    try:
        a = int(input("Enter the minimum number: "))
        b = int(input("Enter the maximum number: "))

        if b <= a:
            print(" The maximum number must be greater than the minimum number.\n")
            continue

        count = int(input("How many random numbers do you want to generate? "))

        unique = input("Do you want the numbers to be unique? (y/n): ").lower()

        if unique == "y":
            if count > (b - a + 1):
                print(" Not enough numbers in the range to generate unique values.\n")
                continue

            numbers = random.sample(range(a, b + 1), count)

        else:
            numbers = [random.randint(a, b) for _ in range(count)]

        print("\n Generated Numbers:")
        for num in numbers:
            print(num)

        again = input("\nDo you want to generate again? (y/n): ").lower()
        if again != "y":
            print("👋 Goodbye!")
            break

    except ValueError:
        print(" Please enter valid numbers only.\n")