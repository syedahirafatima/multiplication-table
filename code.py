# Multiplication Table Generator

# Input number from the user
num = int(input("Enter a number to generate its multiplication table: "))

# Input range up to which the table is required
limit = int(input("Enter the range (e.g., 10 for 1 to 10): "))

print(f"\nMultiplication Table for {num} up to {limit}:\n")

# Generate and display the table
for i in range(1, limit + 1):
    print(num, "x", i, "=", num * i)
