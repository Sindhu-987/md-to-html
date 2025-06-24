#!/usr/bin/env python3
"""
Markdown to HTML Converter CLI
"""

import argparse
from pathlib import Path
import markdown

def convert_markdown_to_html(input_file, output_file):
    input_path = Path(input_file)
    output_path = Path(output_file)

    if not input_path.is_file():
        print(f"Error: '{input_file}' does not exist.")
        return

    # Read markdown content
    with open(input_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Convert to HTML
    html = markdown.markdown(md_text, extensions=['fenced_code', 'tables'])

    # Write to output file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✅ Converted '{input_file}' → '{output_file}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Markdown to HTML")
    parser.add_argument("input", help="Path to the input .md file")
    parser.add_argument("output", help="Path to the output .html file")
    args = parser.parse_args()

    convert_markdown_to_html(args.input, args.output)
