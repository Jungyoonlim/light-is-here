import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Construct the paths to the text files relative to the script directory -- automated for part 2,3,4! 
text_paths = [os.path.join(script_dir, "text_file", f"part{i}.txt") for i in range(2, 5)]

# Construct the output directory path
output_dir = os.path.join(script_dir, "modified_text")

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Loop through each text file path
for text_path in text_paths:
    # Read the contents of the text file
    with open(text_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Replace the "BOH with a red icon" with an empty string
    modified_text = text.replace('', ' ')

    # Extract the part number from the file name
    part_number = os.path.basename(text_path).split('.')[0].split('part')[1]

    # Construct the output file path
    output_path = os.path.join(output_dir, f"part{part_number}_modified.txt")

    # Write the modified text back to the file
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(modified_text)
