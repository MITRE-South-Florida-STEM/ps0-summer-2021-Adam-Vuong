import math
# 1. Ask the user to enter a number "x"
x = float(input("Enter a number. "))

# 2. Ask the user to enter a number "y"
y = float(input("Enter a second number. "))

# 3. Prints out the number "x" raised to the power "y"
z = x**y
print("x raised to the power y is: " + str(z))

# 4. Prints out the log (base 2) of "x"
t = math.log2(x)
print("Log base 2 of x is: " + str(t))