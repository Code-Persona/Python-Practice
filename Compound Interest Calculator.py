# A = P(1+r/n)^t

# A = the future value of the investment/loan, including interest

principle = 0
rate = 0
time = 0

while True:
  principle = float(input("Enter the principle amount: "))
  if principle < 0:
    print("Please enter a positive number for the principle amount.")
  else:
    break

while True:
  rate = float(input("Enter the rate amount: "))
  if rate < 0:
    print("Please enter a positive number for the rate amount.")
  else:
    break

while True:
  time = int(input("Enter the time amount: "))
  if time < 0:
    print("Please enter a positive number for the time amount.")
  else:
    break


total = principle * pow((1 + rate / 100) ,time)
print(f"Balance after {time} years is: ${total:.2f}")