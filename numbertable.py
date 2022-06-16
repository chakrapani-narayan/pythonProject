# This is my first ever Python code to generate a number table

num = int(input("Type the number you want the table for "))
print("Ok here is table of " + str(num))

# Print the table of num
mx = [(x+1) * num for x in range(10)]
print(mx)

# Print the table of num in a better format '1 x num = result'
mx1 = [f'{num} x {(x+1)} = {num * (x+1)}' for x in range(10)]
print(mx1)
