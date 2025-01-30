from langchain_community.embeddings import FastEmbedEmbeddings
from langchain_chroma import Chroma
import os
from constants import DOCS_INDEX_NAME

def check_docs():
    persist_directory = os.path.join(os.path.dirname(__file__), "chroma_db")
    # Check if directory exists
    if not os.path.exists(persist_directory):
        print("Database directory not found!")
        return
    # Check directory size
    dir_size = sum(os.path.getsize(os.path.join(persist_directory, f))
                  for f in os.listdir(persist_directory)
                  if os.path.isfile(os.path.join(persist_directory, f)))
    print(f"Database size: {dir_size/1024/1024:.2f} MB")
    # Check document count
    embedding = FastEmbedEmbeddings()
    db = Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding,
        collection_name=DOCS_INDEX_NAME
    )
    count = db._collection.count()
    print(f"Number of documents: {count}")

if __name__ == "__main__":
    check_docs()
