# Problem 1
def safe_divide(a,b):
    try:
        divide = a / b
        return divide
    except ZeroDivisionError:
        return "Division not by zero"
print(safe_divide(10,0))
print(safe_divide(10,2))
    
# Problem 2

while True:
    try:
        num = int(input("Enter a number: "))
        print("Thank you")
        break
    except ValueError:
        print("Invalid input! Try again.")
    
# Problem 3
try:
    with  open("data.txt","r") as f:
        file = f.read()
        print(file)
except FileNotFoundError:
    print("File not found!")
finally:
    print("Operation complete")
    
# Problem 4
def check_positive(num):
    try:
        if num < 0:
            return num
    except ValueError:
        print("Number must be positive")
print(check_positive(10))
print(check_positive(-5))

# Problem 5
try:
    text = input("Enter some text:")
    with open("data.txt","w") as f:
        file = f.write(text)
    with open("data.txt","r") as f:
        file = f.read()
    print(file)
except IOError:
    print("Could not write to file!")
finally:
    print("Writing complete")

# Problem 6
try:
    with open("log.txt","a") as d:
        file = d.write("Hye!")
        print(file)
except FileNotFoundError:
    print("File not found. Creating new file...")
finally:
    print("Operation done")

# Problem 7
def multiply_list(list):
        result = 0
        print(f"result = {result}")
        for num in list:
                print(f"num = {num}")
                result *= num # Here is a bug.
                print(f"result = {result}")
        return result
print(multiply_list([1, 2, 3, 4]))

# Problem 8
try:
    num = int((input("Enter a number:")))
    divide = num / 100
    print(divide)
except ValueError:
    print("Not a number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Swapping
li = [2,10]
li[0],li[1] = li[1],li[0]
print(li)

# Find largest and second largest number
list = [23,10,7,34,98]
maxi_num = 0
for i in list:
    if i > maxi_num:
        maxi_num = i
print(maxi_num)

