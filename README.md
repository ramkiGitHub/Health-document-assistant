# Healthcare Document Assistant

## Overview

A professional, beginner-friendly GenAI MVP that helps users ask questions over synthetic healthcare documents and receive grounded answers with citations.

This project is designed to:
- Learn practical GenAI engineering skills required by the AI Engineer job description
- Build a portfolio project suitable for technical interviews
- Use only synthetic healthcare documents (no real patient data or PHI)
- Progress from basic RAG to agentic workflows with LangGraph

## Problem Statement

Healthcare organizations need better ways to answer patient and staff questions about policies, procedures, and guidelines while ensuring answers are grounded in official documents and easily auditable. This assistant provides:

- **Grounded Answers**: Only answers from provided documents, preventing hallucination
- **Citations**: Every answer includes source documents and chunk references
- **Safety Guardrails**: Refuses to provide medical advice or diagnose conditions
- **Agentic Routing**: Classifies questions and escalates uncertain responses for human review
- **Privacy**: Uses only synthetic data; production-ready to handle real healthcare data safely

## Architecture

```
User → FastAPI Backend → LangGraph Workflow → Question Classification
                              ↓
                        Document Retriever (FAISS)
                              ↓
                        Answer Generator (LLM)
                              ↓
                        Citation Verifier
                              ↓
                        Response with Citations or Escalation
```

## Tech Stack

- **Language**: Python
- **API Framework**: FastAPI
- **RAG Framework**: LangChain
- **Agent Orchestration**: LangGraph
- **Vector Database**: FAISS (local) / Azure AI Search (production)
- **LLM**: Azure OpenAI or OpenAI
- **Embeddings**: Azure OpenAI or OpenAI embeddings
- **Deployment**: Azure App Service (Phase 9)

## Project Structure

```
healthcare-rag-assistant/
├── app/
│   ├── main.py                 # FastAPI application
│   ├── config.py               # Configuration management
│   ├── schemas.py              # Pydantic models
│   ├── rag/                    # Document loading and retrieval
│   │   ├── loaders.py
│   │   ├── splitter.py
│   │   ├── embeddings.py
│   │   ├── vector_store.py
│   │   ├── retriever.py
│   │   ├── prompts.py
│   │   └── generator.py
│   ├── agents/                 # LangGraph workflows
│   │   ├── graph.py
│   │   ├── state.py
│   │   ├── tools.py
│   │   └── nodes.py
│   ├── services/               # Business logic
│   │   ├── document_service.py
│   │   ├── qa_service.py
│   │   └── evaluation_service.py
│   └── utils/                  # Helpers
│       ├── logging.py
│       └── text_cleaning.py
├── data/
│   ├── raw/                    # Synthetic healthcare documents
│   └── processed/              # Processed chunks
├── indexes/
│   └── faiss/                  # Local FAISS index
├── tests/                      # Unit and integration tests
├── evals/                      # Evaluation datasets and scripts
├── scripts/                    # Utility scripts
├── notebooks/                  # Jupyter notebooks for learning
├── docs/                       # Documentation
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── Dockerfile                 # Docker containerization
└── README.md                  # This file
```

## Getting Started

### Prerequisites
- Python 3.10+
- pip or conda
- API keys for OpenAI or Azure OpenAI

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/ramkiGitHub/Health-document-assistant.git
   cd health-document-assistant
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

5. **Run the application**
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Access the API**
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## Implementation Phases

This project is built in 10 learning phases:

### Phase 0: Setup and Mindset ✅
- Create project structure
- Set up synthetic healthcare documents
- Configure environment
- Write README with problem statement

### Phase 1: FastAPI Foundation
- Build API endpoints (/health, /ask, /documents, /documents/ingest)
- Create Pydantic request/response models
- Mock LLM responses with citations

### Phase 2: Document Ingestion
- Implement document loaders for .md and .txt
- Implement text chunking with metadata
- Test with synthetic documents

### Phase 3: Embeddings and FAISS
- Generate embeddings for all chunks
- Build and persist FAISS index
- Implement semantic search retriever

### Phase 4: Basic RAG Chain
- Implement grounded answer generation
- Add citation extraction from retrieved chunks
- Implement "I don't know" behavior for out-of-scope questions

### Phase 5: LangGraph Agentic Workflow
- Create agent state and nodes
- Implement question classification
- Implement answer verification and escalation logic

### Phase 6: Prompt Engineering and Safety
- Add safety rules to prevent diagnosis advice
- Test prompt injection resistance
- Implement responsible AI guardrails

### Phase 7: Evaluation
- Create golden question dataset
- Implement metrics: retrieval hit rate, citation accuracy, groundedness
- Build evaluation script

### Phase 8: UI or API Demo
- Option A: Use FastAPI Swagger (default)
- Option B: Build Streamlit UI
- Option C: Build React frontend

### Phase 9: Azure Deployment
- Containerize with Docker
- Deploy to Azure App Service
- Set up Azure AI Search (optional upgrade)

### Phase 10: Interview Preparation
- Document architecture and decisions
- Practice explaining the project
- Prepare answers to common interview questions

## API Endpoints (Phase 1+)

### Health Check
```
GET /health
```

### Ask a Question
```
POST /ask
{
  "question": "What documents are needed for an insurance claim?",
  "top_k": 4
}
```

**Response:**
```json
{
  "answer": "The following documents are required for insurance claims: policy number, date of service, provider invoice, diagnosis code, and discharge summary when applicable.",
  "citations": [
    {
      "document": "insurance_claims.md",
      "section": "Required Documents",
      "chunk_id": "insurance_claims_003"
    }
  ],
  "confidence": "high",
  "escalation_note": null
}
```

### List Documents
```
GET /documents
```

### Ingest Documents
```
POST /documents/ingest
```

## Learning Outcomes

By completing this project, you will understand:

1. **LLM Fundamentals**: Tokens, embeddings, context windows, prompt engineering
2. **RAG Architecture**: Why and how to use retrieval to ground LLM responses
3. **Vector Databases**: Semantic search using embeddings and similarity
4. **LangChain**: Document loaders, splitters, retrievers, and chains
5. **LangGraph**: State management, nodes, edges, and agentic workflows
6. **FastAPI**: Building async APIs, Pydantic models, request/response validation
7. **Responsible AI**: Hallucination prevention, safety guardrails, privacy considerations
8. **Evaluation**: Measuring retrieval quality, answer groundedness, and citations
9. **Azure Deployment**: Containerization, cloud deployment, environment management
10. **Interview Skills**: Articulating technical decisions and system design

## Interview Talking Points

### What This Project Demonstrates
- Hands-on RAG implementation (not just theory)
- LangChain and LangGraph expertise
- Agentic AI workflow design
- Responsible AI and safety considerations
- Professional code structure and testing
- Deployment-ready architecture
- Understanding of evaluation metrics

### Key Questions You Should Be Able To Answer
1. Why is retrieval necessary instead of sending all documents to the LLM?
2. How do embeddings enable semantic search?
3. What is the difference between retrieval and generation?
4. How do you prevent hallucination in RAG systems?
5. Why use LangGraph instead of simple chains?
6. How would you scale this to millions of documents?
7. How would you handle real patient data securely?
8. How do you evaluate whether answers are grounded?
9. What are the tradeoffs between local FAISS and Azure AI Search?
10. How would you implement multi-turn conversation?

## Data

All documents in `data/raw/` are **synthetic** and for educational purposes only:
- No real patient information
- No real medical records
- No PHI (Protected Health Information)
- Suitable for portfolio demonstration
- Can be safely shared in interviews

## Development Rules

- **One phase at a time**: Complete a phase before moving to the next
- **Write comments**: Explain complex logic for beginners
- **Add tests**: Write tests for important functions
- **Update README**: Document changes and how to run code
- **Commit often**: Push to GitHub after each phase
- **No over-engineering**: Keep code simple and understandable

## Resources

- [Azure AI Search RAG Overview](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview)
- [LangChain RAG Tutorial](https://docs.langchain.com/)
- [LangGraph Overview](https://langchain-ai.github.io/langgraph/)
- [FAISS Documentation](https://faiss.ai/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Azure App Service Python Quickstart](https://learn.microsoft.com/en-us/azure/app-service/quickstart-python)

## Next Steps

1. Review the implementation plan in `docs/Implementation plan.md`
2. Create a `.env` file from `.env.example` with your API keys
3. Run `uvicorn app.main:app --reload` to start the development server
4. View the API documentation at `http://localhost:8000/docs`
5. Begin Phase 1: Implement FastAPI endpoints

## License

This project is for educational purposes. Use synthetically generated healthcare documents only.

## Author

Built as an AI Engineer interview preparation project.
