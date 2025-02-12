# Dynamic Practice Test Question Generation Agent

A microservice-based application that dynamically generates practice test questions for pesticide industry certification exams, using LangGraph, Gemini AI, and Neo4j.

## Features
- Adaptive testing using LangGraph and Gemini AI
- Knowledge graph-based question generation using Neo4j
- Real-time feedback and explanations
- Multiple question types support (Multiple Choice, True/False, Math)
- Session-based progress tracking

## Setup

1. Clone the repository

```bash
git clone https://github.com/chai-dev682/dynamic-practice-test.git
cd dynamic-practice-test
```

2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Set up environment variables

```bash
cp .env.example .env
# Edit .env with your Neo4j credentials
```

5. Run the application

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## Environment Variables

```env
NEO4J_URI=your_neo4j_uri
NEO4J_USERNAME=your_neo4j_username
NEO4J_PASSWORD=your_neo4j_password
```
