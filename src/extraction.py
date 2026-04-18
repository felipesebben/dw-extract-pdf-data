import os
from dotenv import load_dotenv
from img2table.document import PDF
from img2table.ocr import TesseractOCR
import pandas as pd

# Load environment variables
load_dotenv()

# Setup OCR engine
tesseract_path = os.getenv("TESSERACT_PATH")
if tesseract_path:
    tesseract_dir = os.path.dirname(tesseract_path)
    os.environ["PATH"] = tesseract_dir + os.pathsep + os.environ.get("PATH", "")
ocr_engine = TesseractOCR(
                n_threads=1,
                lang="por",
                tessdata_dir=os.path.join(tesseract_dir, "tessdata")
                )

# Load sample PDF
sample_pdf = PDF("data/raw/sample_data.pdf")

# Extract Tables
extracted_tables = sample_pdf.extract_tables(ocr=ocr_engine, 
                                             implicit_rows=True, 
                                             borderless_tables=True,
                                             implicit_columns=True, 
                                             min_confidence=90)

# print(extracted_tables)

# 1. Access the single table found on page 2
page_2_table = extracted_tables[1][0]

# 2. Convert ExtractedTable to DataFrame
df = page_2_table.df
print(df.head(15))