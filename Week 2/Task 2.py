s1 = input("Enter a string: ")

digits = []

for char in s1:
    if char.isdigit():
        digits.append(int(char))

total = sum(digits)
average = total / len(digits)

print("digits: ", digits)
print("Sum:", total)
print("Average:", average)
