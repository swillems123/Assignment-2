# Initialize the category variable
category = None

# Open the CSV file
with open(r'C:\Projects\toprankedanime.csv', 'r') as file:

	# Since 'type' is the second column, we set type_index to 1
	type_index = 1

	# Read each subsequent line in the file
	for line in file:
		# Split the line into columns
		columns = line.strip().split(',')

		# Strip extra whitespace from the type column
		type_value = columns[type_index].strip()

		# Check if the type column matches any of the specified types
		if type_value in ['TV', 'ONA', 'OVA', 'Movie', 'Special']:
			# Set the category variable
			category = type_value
			print(f'Category: {category}')