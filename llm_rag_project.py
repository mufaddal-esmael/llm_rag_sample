# Import necessary libraries
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# Load environment variables
load_dotenv()

####################################################################
################ add tracing using langfuse ########################
from langfuse import Langfuse
from langfuse.llama_index import LlamaIndexInstrumentor

# Get your keys from the Langfuse project settings page and set them as environment variables
# or pass them as arguments when initializing the instrumentor
instrumentor = LlamaIndexInstrumentor()

# Automatically trace all LlamaIndex operations
instrumentor.start()
####################################################################

# Load documents from a directory (you can change this path as needed)
documents = SimpleDirectoryReader("data").load_data()

# Create an index from the documents
index = VectorStoreIndex.from_documents(documents)

# Create a query engine
query_engine = index.as_query_engine()

# Example query
# response = query_engine.query("What years does the strategic plan cover?")
# response = query_engine.query("What are the sources of revenue?")
# response = query_engine.query("Can you summarize this document?")
response = query_engine.query("How can I maximize my charge?")

print(response)

####################################################################
################ add tracing using langfuse ########################
# Flush events to langfuse
instrumentor.flush()