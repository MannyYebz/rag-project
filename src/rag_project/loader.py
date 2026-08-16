from langchain_community.document_loaders import PyPDFLoader
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


def load_documents():
    loader = PyPDFLoader("data/attention.pdf")
    documents = loader.load()
    return documents
