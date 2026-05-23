from langchain.tools import tool
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings

DB_PATH = "vectordb"

embeddings = OllamaEmbeddings(model="llama3.2")

vectordb = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embeddings
)

def search_by_corpus(question: str, corpus_name: str) -> str:
    docs = vectordb.similarity_search(
        question,
        k=2,
        filter={"source_folder": corpus_name}
    )

    results = []

    for doc in docs:
        source = doc.metadata.get("source_folder", "unknown")
        content = doc.page_content
        results.append(f"[Corpus: {source}]\n{content}")

    return "\n\n".join(results)


@tool
def search_telework_policy(question: str) -> str:
    """Recherche uniquement dans la politique RH de télétravail."""
    return search_by_corpus(question, "telework")


@tool
def search_leave_policy(question: str) -> str:
    """Recherche uniquement dans la politique RH de congés et absences."""
    return search_by_corpus(question, "leave")


@tool
def search_training_policy(question: str) -> str:
    """Recherche uniquement dans la politique RH de formation."""
    return search_by_corpus(question, "training")


@tool
def search_mobility_policy(question: str) -> str:
    """Recherche uniquement dans la politique RH de mobilité interne."""
    return search_by_corpus(question, "mobility")