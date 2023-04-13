from PyPDF4 import PdfFileReader
import pyttsx3

speak = pyttsx3.init()

def read_pdf(path):
    with open(path, 'rb') as f:
        pdf_read = PdfFileReader(f)
        for x in range(pdf_read.getNumPages()):
            page = pdf_read.getPage(x)
            page_content = page.extractText()
            #print(page_content)
            speak.save_to_file(page_content, 'c:\support\story.mp3')
            speak.runAndWait()
            speak.stop()
            



__name__ == "main.py"
read_pdf('test.pdf')