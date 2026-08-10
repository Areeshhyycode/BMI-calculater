#BMI Calculator -project 1
#BMI - Weight (kg) / Height (m)^2 squared



print(" ====== BMI Calculator======")

name = input("Enter your name: ")
weight  =float (input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)
print()
print(F"Hello, {name}, Your BMI is:{bmi:.2f}")

print()
print(f"Hello {name}, aapka BMI hai: {bmi:.2f}")

if bmi < 18.5:
    print("Category: Underweight - thoda khana badhao!")
elif bmi < 25:
    print("Category: Normal - perfect, aise hi rakho!")
elif bmi < 30:
    print("Category: Overweight - thodi walk shuru karo.")
else:
    print("Category: Obese - doctor se baat karna zaroori hai.")
