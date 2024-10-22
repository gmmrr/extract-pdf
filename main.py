import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io


def pdf_to_text(pdf_path, txt_output_path):
    pdf_document = fitz.open(pdf_path)
    extracted_text = ""

    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        text = pytesseract.image_to_string(img, lang="chi_tra")
        extracted_text += text

    with open(txt_output_path, "w", encoding="utf-8") as text_file:
        text_file.write(extracted_text)

    print(f"Extracting Finished. Save in {txt_output_path}")

pdf_path = "input.pdf"
txt_output_path = "output.txt"
pdf_to_text(pdf_path, txt_output_path)
