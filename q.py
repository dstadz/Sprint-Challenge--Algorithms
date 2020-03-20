def bunnyEars(bunnies):
  if bunnies == 0:
    return 0
  print(bunnies)
  return 2 + bunnyEars(bunnies-1)

print(bunnyEars(100))