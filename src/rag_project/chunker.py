from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    return splitter.split_documents(documents)





if __name__ == "__main__":
    from loader import load_documents
    documents = load_documents()
    chunks = chunk_documents(documents)
    print(f"Split {len(documents)} pages into {len(chunks)} chunks")
    print(f"\nFirst chunk:\n{chunks[0].page_content}")