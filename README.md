# Smart QA chatbot  

## Overview

A FastAPI-base RAG system for querying PDF documents using local LLMs.

## Architechture

## Features

- Semantic search with FAISS
- Answer questions using local LLM (Ollama)
- REST API built with FastAPI

## Tech Stack 

- Python 3.11
- FastAPI
- LangChain
- FAISS
- Sentence Transformer
- Docker
- Ollama

## Project strure


```
├── app
│   ├── api
│   │   └── main.py
│   ├── db
│   │   └── vector_store.py
│   ├── ingestion
│   │   ├── __init__.py
│   │   ├── pdf_loader.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-311.pyc
│   │   │   ├── pdf_loader.cpython-311.pyc
│   │   │   └── text_cleaner.cpython-311.pyc
│   │   └── text_cleaner.py
│   └── rag
│       ├── chunking.py
│       ├── context_builder.py
│       ├── embeddings.py
│       ├── generator.py
│       ├── ollama_client.py
│       ├── promps.py
│       ├── retriever.py
│       ├── schema.py
│       └── section_parser.py
├── data
│   ├── processed
│   ├── processed.index
│   ├── processed.pkl
│   └── raw_pdfs
│       └── attention_is_all_you_need.pdf
├── Dockerfile
├── README.md
└── requirements.txt
```

## Installation
Clone project from github
```
git clone https://github.com/cuong111103hd/smartQAchatbot.git
cd smartQAchatbot
```

Docker setup

```
docker compose up --build
```

Example: 

```
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"question": "What is RAG?"}'

```



## Usage

## API docs

## Roadmap

