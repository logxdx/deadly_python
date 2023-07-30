a=float(input())
b=float(input())

print("Addition: ",a+b)
print("Subtraction: ",a-b)
print("Multiplication: ",a*b)

if b==0:
    print("Division: Cannot be divided")
else:
    print("Division: ",a/b)

print("Exponentiation: ",a**b)
print("L2-norm: ",(a**2 + b**2)**(0.5))