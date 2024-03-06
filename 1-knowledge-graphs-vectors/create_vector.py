from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores.neo4j_vector import Neo4jVector
from langchain_openai import OpenAIEmbeddings

COURSES_PATH = "data/asciidoc"

# Load lesson documents
loader = DirectoryLoader(COURSES_PATH, glob="**/lesson.adoc")
docs = loader.load()

# Create a text splitter
# text_splitter =

# Split documents into chunks
# chunks =

# Create a Neo4j vector store
# neo4j_db =