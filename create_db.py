import chromadb
from langchain_google_genai import  GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from dotenv import load_dotenv



load_dotenv()
GOOGLE_API_KEY=os.getenv('google_api_key')
embeddings=GoogleGenerativeAIEmbeddings(google_api_key=GOOGLE_API_KEY,model="models/text-embedding-004")


text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

from langchain.document_loaders.csv_loader import CSVLoader
loader=CSVLoader("/utils/dataset_after_scrapping.csv")
documents=loader.load()

splits=text_splitter.split_documents(documents) 


persist_client=chromadb.PersistentClient(path="./services_db")
collection=persist_client.get_or_create_collection(name='online_service_22_02_2025')
collection.add(documents=[d.page_content for d in splits],
               ids=[str(i) for i in range(len(splits))],
               embeddings=embeddings.embed_documents([d.page_content for d in splits])
               )