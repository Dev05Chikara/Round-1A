
import os
import json
from utils import extract_title_and_headings

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for file in os.listdir(INPUT_DIR):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(INPUT_DIR, file)
            title, outline = extract_title_and_headings(pdf_path)
            json_data = {
                "title": title,
                "outline": outline
            }
            out_file = os.path.join(OUTPUT_DIR, f"{os.path.splitext(file)[0]}.json")
            with open(out_file, "w", encoding="utf-8") as f:
                json.dump(json_data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()
