
# Adobe Hackathon - PDF Outline Extractor

## Description
This project extracts the title and structured outline (H1, H2, H3) from PDF files based on font size analysis using PyMuPDF.

## Instructions

### Build the Docker image:

```bash
docker build -t pdf_outline_extractor:latest .
```

### Run the Docker container:

```bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none pdf_outline_extractor:latest
```

## Dependencies
- Python 3.10
- PyMuPDF (fitz)
