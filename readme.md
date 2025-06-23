# GenAI Stack (Customized for Financial Q&A in Thai & English)
The GenAI Stack is a modular, Docker-based platform for building and deploying financial question-answering applications powered by large language models (LLMs), knowledge graphs, and relational databases.

This customized fork focuses on the Thai stock market (SET50) and supports querying financial metrics and stock data using either Neo4j (as a knowledge graph) or MySQL (as structured tables). It includes multiple chatbot services, data loaders, and RAG-enhanced interfaces.

**Installation Instructions**

1.Clone the Repository
```
git clone https://github.com/naphattha/genai-stack -b naphattha
cd genai-stack
```

2.Insert Financial Data

Before launching the stack, place your JSON data files in the correct directories:

| File          | Destination Directory                     | Purpose                                                             |
|------------------------|------------------------------------|-------------------------------------------------------------------------|
|FilteredEODData.json	|src/mysql/ and src/neo4j/	|Contains daily stock price data (EOD)|
|FilteredFinancialData.json	|src/mysql/ and src/neo4j/	|Contains financial statement metrics|

Quick Start
Ensure Docker is installed and running
Download: https://www.docker.com/products/docker-desktop/

**Start the application**
```
docker compose up --build
```
This will:

Load your Filtered*.json data into Neo4j and MySQL

Start the front-end bots (Thai and English)

Start Neo4j browser and vector index

Activate Ollama or OpenAI model endpoint

**Watch Mode for Development**
```
docker compose watch
```

**Shutdown**
If health check fails or containers don't start up as expected, shutdown
completely to start up again.
```
docker compose down
```


## Applications

| Name               | Main files                              | Compose name   | URLs                    | Description |
|--------------------|------------------------------------------|----------------|--------------------------|-------------|
| Thai Chatbot       | `Dockerfile.thai`                        | `thai`         | http://localhost:8502    | LLM-powered chatbot (Thai), answers financial queries via MySQL + Neo4j |
| English Chatbot    | `Dockerfile.eng`                         | `eng` *(commented)* | http://localhost:8501    | *(Optional)* English version chatbot using similar architecture |
| MySQL Loader       | `src/mysql/`, `Dockerfile.mysql`         | `mysql-loader` | —                        | Loads EOD and financial data into MySQL from `FilteredEODData.json` and `FilteredFinancialData.json` |
| Neo4j Loader       | `src/neo4j/`, `Dockerfile.neo4jloader`   | `neo4j-loader` | —                        | Loads EOD and financial data into Neo4j as a knowledge graph |
| Neo4j Browser      | —                                        | `neo4j`        | http://localhost:7474    | Visualize and query the financial knowledge graph |
| Ollama LLM Server  | —                                        | `ollama`       | http://localhost:11434   | Local LLM backend supporting models like Gemma, LLaMA, and Mistral |

## English Chatbot Notice
 
The English Chatbot service (eng) is currently commented out in the docker-compose.yml file to reduce resource usage during development or when only Thai support is required.

To enable the English chatbot:

Open docker-compose.yml.

Scroll to the section starting with # eng: and uncomment the lines related to this service.

Start the service with:
```
docker compose up --build eng
```
Once enabled, it will be accessible at: http://localhost:8501
