import xml.etree.ElementTree as ET
import re
import csv

# Function to extract media links from content
def extract_media_links(content):
    if content is None:
        return []
    # Regex to find URLs
    url_regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    return re.findall(url_regex, content)


def extract_data_from_xml(file_path):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Namespace dictionary for finding tags
    namespaces = {
        'content': 'http://purl.org/rss/1.0/modules/content/',
        'dc': 'http://purl.org/dc/elements/1.1/',
        'wp': 'http://wordpress.org/export/1.2/'
    }

    # List to hold all post data
    posts_data = []

    # Iterate over each post item
    for post in root.iter('item'):
        # Extract categories and tags
        categories_tags = [cat.text for cat in post.findall('category')]

        post_data = {
            'title': post.find('title').text or '',
            'link': post.find('link').text or '',
            'author': post.find('dc:creator', namespaces).text or '',
            'content': post.find('content:encoded', namespaces).text or '',
            'date': post.find('pubDate').text or '',
            'media_links': ', '.join(extract_media_links(post.find('content:encoded', namespaces).text)),
            'categories_tags': ', '.join(categories_tags)
        }
        posts_data.append(post_data)

    return posts_data

def save_to_csv(data, csv_file_path):
    # Define the header
    header = ['title', 'link', 'author', 'content', 'date', 'media_links', 'categories_tags']

    # Write to CSV
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=header)

        # Write the header
        writer.writeheader()

        # Write the rows
        for row in data:
            writer.writerow(row)

# Path to your XML file
file_path = './wp_exports/POSTSgamacidado.WordPress.2024-01-17.xml'

# Extracting data
extracted_data = extract_data_from_xml(file_path)

# You can now work with `extracted_data`, which is a list of dictionaries containing each post's data

# Path for the CSV file
csv_file_path = './extracted/extracted_data.csv'

# Save data to CSV
save_to_csv(extracted_data, csv_file_path)
