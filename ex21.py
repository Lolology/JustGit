def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} + {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} + {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let`s do some math with just functions")

age = add(30, 5)
print(">>>>  age=", age)
height =  subtract(78, 4)
print(">>>> height=", height)
weight = multiply(90, 2)
print(">>>> weight=", weight)
iq = divide(100, 2)
print(">>>> iq=", iq)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# a puzzle for extra credit, type it in any way.
print("vasya soset huy")

what =  add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can u do it by hand?")
