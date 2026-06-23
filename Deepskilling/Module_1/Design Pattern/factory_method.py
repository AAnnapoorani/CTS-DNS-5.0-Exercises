class WordDocument:
    def open(self):
        print("Word Document Opened")

class PdfDocument:
    def open(self):
        print("PDF Document Opened")

class ExcelDocument:
    def open(self):
        print("Excel Document Opened")

class DocumentFactory:
    def create_document(self, doc_type):
        if doc_type == "word":
            return WordDocument()
        elif doc_type == "pdf":
            return PdfDocument()
        elif doc_type == "excel":
            return ExcelDocument()
        else:
            print("Invalid Document Type")
            return None

factory = DocumentFactory()
doc = factory.create_document("pdf")
if doc:
    doc.open()