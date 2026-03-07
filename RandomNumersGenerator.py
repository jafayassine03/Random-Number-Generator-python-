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

        print("\n Generated Numbers:")
        for i in range(count):
            print(random.randint(a, b))

        again = input("\nDo you want to generate again? (y/n): ").lower()
        if again != "y":
            print("👋 Goodbye!")
            break

    except ValueError:
        print(" Please enter valid numbers only.\n")