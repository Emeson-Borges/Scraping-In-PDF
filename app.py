import PyPDF2


def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def save_text_to_txt(text, txt_path):
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(text)

def main():
    pdf_path = "exemplo.pdf"  # Substitua "exemplo.pdf" pelo caminho do seu arquivo PDF
    text = extract_text_from_pdf(pdf_path)
    print("Texto extraído do PDF:")
   #print(text)
    
    txt_path = "texto_extraido.txt"
    save_text_to_txt(text, txt_path)
    print(f"Texto salvo em '{txt_path}'.")

if __name__ == "__main__":
    main()

    
    
    