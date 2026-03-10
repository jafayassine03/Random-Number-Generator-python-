import random

print("🎲 Random Number Generator")
print("The computer will generate random numbers between the min and max you choose.\n")

while True:
    try:
        a = int(input("Enter the minimum number: "))
        b = int(input("Enter the maximum number: "))

        if b <= a:
            print("❌ The maximum number must be greater than the minimum number.\n")
            continue

        count = int(input("How many random numbers do you want to generate? "))

        unique = input("Do you want the numbers to be unique? (y/n): ").lower()

        if unique == "y":
            if count > (b - a + 1):
                print("❌ Not enough numbers in the range to generate unique values.\n")
                continue
            numbers = random.sample(range(a, b + 1), count)
        else:
            numbers = [random.randint(a, b) for _ in range(count)]

        sort_option = input("Sort numbers? (asc/desc/no): ").lower()

        if sort_option == "asc":
            numbers.sort()
        elif sort_option == "desc":
            numbers.sort(reverse=True)

        print("\n🎯 Generated Numbers:")
        for num in numbers:
            print(num)

        show_stats = input("\nShow statistics? (y/n): ").lower()

        if show_stats == "y":
            total = sum(numbers)
            average = total / len(numbers)
            print("\n📊 Statistics")
            print("Total numbers:", len(numbers))
            print("Minimum:", min(numbers))
            print("Maximum:", max(numbers))
            print("Sum:", total)
            print("Average:", round(average, 2))

        again = input("\nDo you want to generate again? (y/n): ").lower()
        if again != "y":
            print("👋 Goodbye!")
            break

    except ValueError:
        print("❌ Please enter valid numbers only.\n")