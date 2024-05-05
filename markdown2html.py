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
    
    # Dictionary mapping Markdown heading levels to HTML tags
    heading_mapping = {
        '#': 'h1',
        '##': 'h2',
        '###': 'h3',
        '####': 'h4',
        '#####': 'h5',
        '######': 'h6'
    }

    # Perform Markdown to HTML conversion
    with open(markdown_file, 'r') as md:
        markdown_content = md.readlines()

    html_content = []
    in_list = False
    in_ordered_list = False
    for line in markdown_content:
        if line.startswith('#'):
            # Extract the heading level and text
            heading_level, heading_text = line.strip().split(maxsplit=1)
            # Get the HTML tag for the corresponding heading level
            html_tag = heading_mapping.get(heading_level, 'h1')
            # Generate HTML tag with text on separate lines
            html_content.append(f'<{html_tag}>{heading_text}</{html_tag}>\n')
        elif line.startswith('* '):
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
            html_content.append(line)

    # Close the list if it's still open
    if in_list:
        html_content.append('</ol>\n')
    elif in_ordered_list:
        html_content.append('</ul>\n')

    # Write HTML content to the output file
    with open(output_file, 'w') as html:
        html.write(''.join(html_content))
    
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
