
import fitz  # PyMuPDF

def extract_title_and_headings(pdf_path):
    doc = fitz.open(pdf_path)
    headings = []
    title = ""

    font_sizes = {}
    all_text = []

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    line_text = ""
                    max_font = 0
                    for span in line["spans"]:
                        line_text += span["text"].strip() + " "
                        font_size = round(span["size"])
                        max_font = max(max_font, font_size)
                        font_sizes[font_size] = font_sizes.get(font_size, 0) + 1
                    line_text = line_text.strip()
                    if line_text:
                        all_text.append((line_text, max_font, page_num))

    sorted_fonts = sorted(font_sizes.items(), key=lambda x: -x[0])
    top_fonts = [font[0] for font in sorted_fonts[:4]]

    for text, size, page in all_text:
        if size == top_fonts[0] and not title:
            title = text
        elif size == top_fonts[1]:
            headings.append({"level": "H1", "text": text, "page": page})
        elif len(top_fonts) > 2 and size == top_fonts[2]:
            headings.append({"level": "H2", "text": text, "page": page})
        elif len(top_fonts) > 3 and size == top_fonts[3]:
            headings.append({"level": "H3", "text": text, "page": page})

    return title, headings
