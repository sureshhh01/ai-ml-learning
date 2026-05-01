# Exception Handling Example

try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid input")

else:
    print("No errors occurred")

finally:
    print("Execution finished")