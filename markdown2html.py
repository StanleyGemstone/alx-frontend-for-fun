#!/usr/bin/python3

"""
markdown2html.py: A script to convert Markdown files to HTML.
"""

import sys
import os
from typing import List

# Function to parse Markdown paragraphs and generate HTML
def parse_paragraphs(markdown_content: List[str]) -> List[str]:
    """Parse Markdown paragraphs and generate HTML."""
    html_content = []
    in_paragraph = False
    for line in markdown_content:
        if line.strip():  # Check if the line is not empty
            if not in_paragraph:
                html_content.append('<p>\n')
                in_paragraph = True
            html_content.append(f'    {line.strip()}\n')
        else:
            if in_paragraph:
                html_content.append('</p>\n')
                in_paragraph = False
            html_content.append('\n')  # Add an empty line for readability
    
    # Close the paragraph if it's still open
    if in_paragraph:
        html_content.append('</p>\n')
    
    return html_content

# Function to convert Markdown headings to HTML
def parse_headings(markdown_content: List[str]) -> List[str]:
    """Parse Markdown headings and generate HTML."""
    html_content = []
    heading_mapping = {
        '#': 'h1',
        '##': 'h2',
        '###': 'h3',
        '####': 'h4',
        '#####': 'h5',
        '######': 'h6'
    }
    for line in markdown_content:
        if line.startswith('#'):
            heading_level, heading_text = line.strip().split(maxsplit=1)
            html_tag = heading_mapping.get(heading_level, 'h1')
            html_content.append(f'<{html_tag}>{heading_text}</{html_tag}>\n')
    return html_content

# Function to parse Markdown unordered and ordered lists and generate HTML
def parse_lists(markdown_content: List[str]) -> List[str]:
    """Parse Markdown lists and generate HTML."""
    html_content = []
    in_list = False
    in_ordered_list = False
    for line in markdown_content:
        if line.startswith('* '):
            if not in_list:
                html_content.append('<ol>\n')
                in_list = True
            html_content.append(f'    <li>{line.strip("* ").strip()}</li>\n')
        elif line.startswith('- '):
            if not in_ordered_list:
                html_content.append('<ul>\n')
                in_ordered_list = True
            html_content.append(f'    <li>{line.strip("- ").strip()}</li>\n')
        else:
            if in_list:
                html_content.append('</ol>\n')
                in_list = False
            elif in_ordered_list:
                html_content.append('</ul>\n')
                in_ordered_list = False
    if in_list:
        html_content.append('</ol>\n')
    elif in_ordered_list:
        html_content.append('</ul>\n')
    return html_content

# Function to convert Markdown file to HTML
def convert_markdown_to_html(markdown_file: str, output_file: str) -> None:
    """Converts Markdown file to HTML."""
    # Check if the Markdown file exists
    if not os.path.exists(markdown_file):
        sys.stderr.write(f"Missing {markdown_file}\n")
        sys.exit(1)
    
    # Perform Markdown to HTML conversion
    with open(markdown_file, 'r') as md:
        markdown_content = md.readlines()

    # Parse Markdown headings, lists, and paragraphs
    html_content = []
    html_content.extend(parse_headings(markdown_content))
    html_content.extend(parse_lists(markdown_content))
    html_content.extend(parse_paragraphs(markdown_content))
    
    # Write HTML content to the output file
    with open(output_file, 'w') as html:
        html.write(''.join(html_content))
    
    sys.exit(0)

# Main function
def main() -> None:
    """Main function."""
    # Check if correct number of arguments is provided
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(markdown_file, output_file)

if __name__ == "__main__":
    main()
