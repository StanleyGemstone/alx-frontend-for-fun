#!/usr/bin/python3

"""
markdown2html.py: A script to convert Markdown files to HTML.
"""

import sys
import os

def convert_markdown_to_html(markdown_file: str, output_file: str) -> None:
    """Converts Markdown file to HTML."""
    # Check if the Markdown file exists
    if not os.path.exists(markdown_file):
        sys.stderr.write(f"Missing {markdown_file}\n")
        sys.exit(1)
    
    # Perform Markdown to HTML conversion here
    # For demonstration purposes, let's assume a simple conversion
    with open(markdown_file, 'r') as md:
        markdown_content = md.read()
    # For simplicity, just write the Markdown content to the output file
    with open(output_file, 'w') as html:
        html.write(markdown_content)
    
    sys.exit(0)

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
