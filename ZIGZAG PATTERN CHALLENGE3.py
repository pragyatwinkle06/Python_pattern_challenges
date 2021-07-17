# Python3 ZIGZAG PATTERN CHALLENGE3

# Function to print any string
# in zigzag fashion
def zigzag(s, rows):
	
	# Store the gap between the major columns
	interval = 2 * rows - 2

	# Traverse through rows
	for i in range(rows):
		
		# Store the step value for each row
		step = interval - 2 * i

		# Iterate in the range [1, N-1]
		for j in range(i, len(s), interval):
			
			# Print the character
			print(s[j], end = "")
			
			if (step > 0 and step < interval and
						step + j < len(s)):

				# Print the spaces before character
				# s[j+step]
				for k in range((interval - rows - i)):
					print(end = " ")

				# Print the character
				print(s[j + step], end = "")

				# Print the spaces after character
				# after s[j+step]
				for k in range(i - 1):
					print(end = " ")
			else:

				# Print the spaces for first and
				# last rows
				for k in range(interval - rows):
					print(end = " ")
					
		print()


if __name__ == '__main__':
	
	# Given Input
	s = input("enter string: ")
	rows=int(input("enter a no"))

	# Function Call
	zigzag(s, rows)

# enter no. of rows u want
