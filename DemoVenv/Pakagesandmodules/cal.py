from Calculator.addition import add
from Calculator.subraction import sub
from Calculator.multiplication import mul
from Calculator.division import div

a=int(input("Enter a: "))
b=int(input("Enter b: "))

print("Addition: ",add(a,b))
print("Subraction: ",sub(a,b))
print("Multiplication: ",mul(a,b))
print("Division: ",div(a,b))