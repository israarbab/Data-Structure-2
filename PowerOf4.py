def power4(number):
  if number <= 0:
      return False
  if number == 1:
      return True
  if number % 4 != 0:
      return False
  return power4(number // 4)

n = int(input("Enter a number: "))
if power4(n):
    print("\nThe number is a power of 4")
else:
    print("\nThe number is not a power of 4")
