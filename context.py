#from pinecone.grpc import PineconeGRPC as Pinecone
from dotenv import load_dotenv
from extract import client
load_dotenv()

collection  = client.get_collection('mygita')
#pc = Pinecone(api_key=os.getenv('PINECONE_API'))
def context_retreival(query: str):
    results = collection.query(
        query_texts=[query],
        n_results=5
    )
    final_list=[]
    [documents] = results['documents']
    [metadatas] = results['metadatas']
    for i in range(len(documents)):
        final_list.append({f'document_{i}':
            {'document':documents[i],
            'metadata': metadatas[i]}
        })
    return str(final_list)


    
