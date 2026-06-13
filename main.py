
def main():
    while True:
        print("1. Celsius to Kelvin")
        print("2. Celsius to Fahrenheit")

choice = input("Enter your choice:")

if choice == "1.":
  Cel = float(input("Enter the temperature in celsius"))
  Kel = Cel + 273.15
  print("The temperature in Kelvin is:", Kel)

elif choice == "2.":
  Fa = float(input("Enter the temperature in celsius"))
  F = (Fa * 9/5) + 32
  print("The temperature in Fahrenheit is:", F)

else:
    print("Enter a valid temperature")

again = input("Do you want to convert again? y/n:")
if again == "y":
    if choice == "1.":
        C = Kel - 273.15
        print("The temperature back to celsius is:", C)
    elif choice == "2.":
        F1 = (F - 32) * 5/9
        print("The converted temperature back to celsius is:", F1)
elif again == "n":
    print("Converter finished")
else:
    print("Invalid value")

















