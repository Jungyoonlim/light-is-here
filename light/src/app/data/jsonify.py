import re
import os
import json

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Read the content of part1_modified.txt
file_path = os.path.join(script_dir, "modified_text", "part1_modified.txt")
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

# Extract the table of contents
toc_match = re.search(r"(1\.\s+[^.]+(?:\n(?:\d+\.\s+[^.]+|\s+[^.]+))*)", content, re.MULTILINE)
if toc_match:
    toc = toc_match.group(1)
    # Remove the table of contents from the content
    content = content.replace(toc, "").strip()
else:
    print("Table of contents not found.")
    exit(1)

# Split the table of contents into titles
titles = re.findall(r"(\d+(?:\.\s*\d+)?\.\s+[^.]+)", toc)

# Create a dictionary to store the chapters
chapter_dict = {}

# Iterate over the titles and extract the corresponding chapters
for i, title in enumerate(titles):
    chapter_number = re.findall(r"^\d+(?:\.\s*\d+)?", title)[0].strip()
    chapter_title = re.sub(r"^\d+(?:\.\s*\d+)?\.\s+", "", title).strip()

    # Find the start of the chapter content
    chapter_start = content.find(chapter_number + ".")
    if chapter_start != -1:
        # Find the end of the chapter content
        if i < len(titles) - 1:
            next_title = titles[i + 1]
            next_chapter_number = re.findall(r"^\d+(?:\.\s*\d+)?", next_title)[0].strip()
            chapter_end = content.find(next_chapter_number + ".", chapter_start)
        else:
            chapter_end = len(content)

        # Extract the chapter content
        chapter_content = content[chapter_start + len(chapter_number) + 1:chapter_end].strip()
        chapter_dict[chapter_number] = {"title": chapter_title, "content": chapter_content}
    else:
        print(f"Chapter content not found for: {title}")

# Write the chapter dictionary to a JSON file
json_filename = "chapters.json"
with open(json_filename, "w", encoding="utf-8") as json_file:
    json.dump(chapter_dict, json_file, ensure_ascii=False, indent=4)

print("Chapters converted to JSON successfully.")