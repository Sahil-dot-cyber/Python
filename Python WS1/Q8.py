a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Swap
a, b = b, a

# Increment one variable (let's increment 'a')
a += 1

print("After swapping and incrementing:")
print("First number:", a)
print("Second number:", b)