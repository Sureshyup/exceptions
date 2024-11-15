try:
    a=int(input("enter the dividend"))
    b=int(input("Enter the divisior"))
    result=a/b
except ZeroDivisionError:
    print("Error : cannot divide by zero")
except ValueError:
    print("Error: please enter a valid numbers")
else:
    print("the result of division is",result)
finally:
    print("this message always print after the try ")
