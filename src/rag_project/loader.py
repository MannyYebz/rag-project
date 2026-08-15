from langchain_community.document_loaders import PyPDFLoader
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

loader = PyPDFLoader("data/attention.pdf")
documents = loader.load()


for i,doc in enumerate(documents, start=1):
    print(f" Page {i} has {len(doc.page_content)} characters")
print(f'The document has {len(documents)} pages')
#print(documents)

# from pypdf import PdfReader

# reader = PdfReader("data/attention.pdf")
# for page in reader.pages:
#     print(page.extract_text()[:500])
#     print("---")

