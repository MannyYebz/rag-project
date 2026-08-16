from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def get_answer(question):
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma(
        persist_directory="data/chroma_db",
        embedding_function=embeddings,
    )
    docs = vectorstore.similarity_search(question, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])

    llm = ChatOpenAI(model="gpt-4o-mini")
    prompt = f"Based on the following context, answer the question.\n\nContext:\n{context}\n\nQuestion: {question}"
    response = llm.invoke(prompt)
    return response.content

if __name__ == "__main__":
    question = "What is the Transformer architecture?"
    print(f"Q: {question}")
    print(f"A: {get_answer(question)}")