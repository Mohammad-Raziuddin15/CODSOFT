print("===== SIMPLE CALCULATOR =====")

while True:

   num1 = float(input("Enter a first number:-"))
   num2 = float(input("Enter a second number:-"))

   print("\nChoose Operation")
   print("1. Addition")
   print("2. Substraction")
   print("3. Multiplication")
   print("4. Division")

   choice = input("Enter your choice (1/2/3/4):-")

   if choice == '1':
      result = num1 + num2
      print("Result =", result)

   elif choice == '2':
      result = num1 - num2
      print("Result =", result)

   elif choice == '3':
      result = num1 * num2
      print("Result =", result)

   elif choice == '4':
      if num2 != 0:
          result = num1 / num2
          print("Result =", result)
      else:
         print("Division by zero is not allowed")

   else :
      print("Invalid input")

   again = input("\nDo you want to continue? (yes/no):-")

   if again.lower() != "yes":
      print("\nCalculator closed")
      break
   


