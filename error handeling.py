on = True
def divide (a,b):
    try:
        c= int(a) / int(b)
        return c
    except ZeroDivisionError:
        return "you can't divide by zero"
    except ValueError:
        return "you can only divide numbers"

while on:
    first = input ("first number")
    print("divided by:")
    second = input ("second number:")
    print(divide(first,second))
    