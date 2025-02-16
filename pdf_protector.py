import PyPDF2
import sys

import PyPDF2.errors

def protection(input_pdf, output_pdf, password):
    try:
        with open(input_pdf, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            pdf_writer = PyPDF2.PdfWriter()

            for page_num in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page_num])

            pdf_writer.encrypt(password)

            with open(output_pdf, 'wb') as file:
                pdf_writer.write(output_pdf)

            print(f"Protected PDF {output_pdf} is created!")
    
    except FileNotFoundError:
        print(f"There is no such file in the folder as {input_pdf}")
    except PyPDF2.errors.PdfReadError:
        print(f"{input_pdf} is not a pdf file")
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 script.py <input_pdf> <output_pdf> <password>")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    password = sys.argv[3]
    protection(input_pdf, output_pdf, password)

if __name__ == "__main__":
    main()