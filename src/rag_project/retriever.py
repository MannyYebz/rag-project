from langchain_openai import ChatOpenAI
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

load_dotenv()

def get_answer(question):
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma(
        persist_directory="data/chroma_db",
        embedding_function=embeddings,
    )
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    llm = ChatOpenAI(model="gpt-4o-mini")
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
    )
    result = chain.invoke({"query": question})
    return result["result"]


if __name__ == "__main__":
    question = "What is the Transformer architecture?"
    answer = get_answer(question)
    print(f"Q: {question}")
    print(f"A: {answer}")