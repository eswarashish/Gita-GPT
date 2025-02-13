from PyPDF2 import PdfReader
# from pinecone.grpc import PineconeGRPC as Pinecone
# from pinecone  import  ServerlessSpec
# Changing from pinecone to ChromaDB
import chromadb
from chromadb.config import Settings
import json
import os,time
from dotenv import load_dotenv

#env intialization
pages= []
data=[]
ids = []
load_dotenv()
#ChromDB Client intialization
client = chromadb.PersistentClient(path='data')

# reader = PdfReader("Bhagavad-gita_ english.pdf")

# def extract_raw_text():
#     for i in range(42,1030):
#         page = reader.pages[i]#now lets break down each page to five chunks with a window size
#         pages.append({  
#             'pno': i,
#         })
#         data.append(page.extract_text())
#         ids.append(f'pg-{i}')
# extract_raw_text()

# if len(data)!= 0:
#         collection.add(
#         documents=data,
#         metadatas=pages,
#         ids = ids
#     )




    



        
    
