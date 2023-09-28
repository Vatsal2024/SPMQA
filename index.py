# Print a pyramid pattern
rows = 5

# Outer loop iterates over the rows
for i in range(1, rows + 1):
  # Inner loop iterates over the columns
  for j in range(1, i + 1):
    print("*", end='')
  print()
