number = int(input('Please enter a number : '))
if number % 2 != 0 and number % 3 != 0 and number > 1:
  print(number, "is a prime number")
else:
  print(number, "is not a prime number")