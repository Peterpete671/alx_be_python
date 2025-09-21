#Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

#Initialize row counter for the while loop
row = 0

#Use a while loop for rows
while row < size:
	# Use a loop for columns
	for col in range(size):
		print("*", end="")
	print()
	row += 1
