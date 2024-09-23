# Initialize the category counter dictionary
category_counts = {
    'TV': 0,
    'ONA': 0,
    'OVA': 0,
    'Movie': 0,
    'Special': 0
}

# Open the CSV file
with open(r'C:\Projects\toprankedanime.csv', 'r') as file:
    print("File opened successfully!") # Confirm that the file was opened

    # Since 'type' is the second column, we set type_index to 1
    type_index = 1

    # Read each subsequent line in the file
    for line in file:
        # Split the line into columns
        columns = line.strip().split(',')

        # Strip extra whitespace from the type column
        type_value = columns[type_index].strip()

        # Check if the type column matches any of the specified types
        if type_value in category_counts:
            # Increment the corresponding category counter
            category_counts[type_value] += 1

# Print the counts for each category
for category, count in category_counts.items():
    print(f'{category}: {count}')