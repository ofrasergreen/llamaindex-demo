from llama_index import StorageContext, load_index_from_storage
from dotenv import load_dotenv
import logging
import sys

load_dotenv()

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

storage_context = StorageContext.from_defaults(persist_dir="index")

index = load_index_from_storage(storage_context)
query_engine = index.as_query_engine()
response = query_engine.query(
    "What does load_index_from_storage do and how does it work?"
)
print(response)
