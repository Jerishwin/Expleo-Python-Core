def salary(oldSalary,hike):
    total = oldSalary+(oldSalary*hike/100)
    return total

a=int(input("Enter Old Salary: "))
b=int(input("Enter The hike"))

print("Ne Salary: ",salary(a,b))