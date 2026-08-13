# from langchain_community.document_loaders import PyPDFLoader

# loader = PyPDFLoader("data/attention.pdf")
# documents = loader.load()

# # for doc in documents:
# #     print("there were " +int((len(doc.page_content))) + "documents loaded")
# print(documents)

from pypdf import PdfReader

reader = PdfReader("data/attention.pdf")
for page in reader.pages:
    print(page.extract_text()[:500])
    print("---")

