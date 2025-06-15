from langchain.chains import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph
from langchain_community.llms import Ollama  # Or use OpenAI
import os

llm = Ollama(model="llama3")  # or use ChatOpenAI(model="gpt-4")
graph = Neo4jGraph(
    url=os.getenv("NEO4J_URI"),
    username=os.getenv("NEO4J_USERNAME"),
    password=os.getenv("NEO4J_PASSWORD")
)

chain = GraphCypherQAChain.from_llm(llm, graph=graph, verbose=True)

def run_finance_chatbot(question):
    return chain.run(question)
