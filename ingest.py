import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings

DATA_PATH = "data"
DB_PATH = "vectordb"

documents = []

# Parcourir les dossiers RH
for root, dirs, files in os.walk(DATA_PATH):

    for file in files:

        if file.endswith(".pdf"):

            file_path = os.path.join(root, file)

            print(f"Chargement : {file_path}")

            loader = PyPDFLoader(file_path)

            docs = loader.load()

            # Ajouter metadata
            for doc in docs:
                doc.metadata["source_folder"] = os.path.basename(root)

            documents.extend(docs)

print(f"\nDocuments chargés : {len(documents)}")

# Découpage
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)

if len(chunks) == 0:
    print("\nAucun document PDF trouvé.")
    print("Ajoute au moins un fichier PDF dans un de ces dossiers :")
    print("- data/telework")
    print("- data/leave")
    print("- data/training")
    print("- data/mobility")
    exit()

# Embeddings Ollama
embeddings = OllamaEmbeddings(
    model="llama3.2"
)

# Base vectorielle
vectordb = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=DB_PATH
)

print("\nBase vectorielle créée avec succès")