age = int(input("Enter your age: "))

if age >= 17:
 print("you are now signed up!")
elif age < 0:
 print("You havent born yet!")
else:
 print("you must be 18+ to sign up")



 response = input("would u like food?: ")

 if response == "y":
  print("have some food")
 else:
  print("i dont want")




#simple calculator programs
operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
 result = num1  + num2
 print(result)

elif operator == "-":
 result = num1 - num2
 print(result)

elif operator == "*":
 result = num1 * num2
 print(result)

elif operator == "/":
 result = num1 / num2
 print(result)

else:
 print(f"{operator}is not valid")

 #temperature conversion
 unit = input("Is this temperature in celsius or fahrenheit (c/f): ")
 temp = float(input("Enter the temperature: "))

if unit == "c":
  temp = round(9 * temp) / 5 + 32, 1)
  print(f"The temp  in fahrenheit is: {temp}degree F")

elif unit == "f":
 pass
else:
 print(f"{unit}is invalid")
