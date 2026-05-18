import os
import shutil
import re
import requests

# =====================================================
# MODULE 1 : JPG FILE ORGANIZATION
# =====================================================

# Define source and destination folders
source_folder = "Images"
destination_folder = "Moved_Images"

# Create destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)

# Scan source folder for JPG files
for file_name in os.listdir(source_folder):

    # Check for JPG image files
    if file_name.endswith(".jpg"):

        # Generate complete file paths
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)

        # Move JPG file
        shutil.move(source_path, destination_path)

print("All JPG files moved successfully.")


# =====================================================
# MODULE 2 : EMAIL ADDRESS EXTRACTION
# =====================================================

# Open and read input text document
with open("input.txt", "r") as file:
    data = file.read()

# Extract email addresses using Regular Expression
email_list = re.findall(
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    data
)

# Store extracted emails into output file
with open("emails.txt", "w") as output_file:
    for email in email_list:
        output_file.write(email + "\n")

print("Email extraction completed successfully.")


# =====================================================
# MODULE 3 : WEBPAGE TITLE SCRAPING
# =====================================================

# Fixed webpage URL
url = "https://example.com"

# Send request to webpage
response = requests.get(url)

# Store webpage HTML content
html_content = response.text

# Extract webpage title
title = re.search(
    r"<title>(.*?)</title>",
    html_content,
    re.IGNORECASE
)

# Save webpage title into output file
with open("webpage_title.txt", "w") as file:

    if title:
        file.write(title.group(1))
        print("Webpage title saved successfully.")
    else:
        file.write("Title not found.")
        print("Title not found.")
