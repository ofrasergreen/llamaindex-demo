import os

from llama_index import download_loader
from llama_index.node_parser import SimpleNodeParser
from llama_index import GPTVectorStoreIndex

import logging
import sys

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

download_loader("GithubRepositoryReader")

from llama_index.readers.llamahub_modules.github_repo import (
    GithubRepositoryReader,
    GithubClient,
)

# Initialize the GithubRepositoryReader
github_client = GithubClient(os.getenv("GITHUB_TOKEN"))
loader = GithubRepositoryReader(
    github_client,
    owner="jerryjliu",
    repo="llama_index",
    filter_directories=(
        ["llama_index", "docs"],
        GithubRepositoryReader.FilterType.INCLUDE,
    ),
    filter_file_extensions=([".py"], GithubRepositoryReader.FilterType.INCLUDE),
    verbose=True,
    concurrent_requests=10,
)

# 1. Load the documents
docs = loader.load_data(branch="main")

# 2. Parse the docs into nodes
parser = SimpleNodeParser()
nodes = parser.get_nodes_from_documents(docs)

# 3. Build an index
# You can customize the LLM. By default it uses `text-embedding-ada-002`
index = GPTVectorStoreIndex(nodes)

# 4. Persist the index
index.storage_context.persist(persist_dir="index")
