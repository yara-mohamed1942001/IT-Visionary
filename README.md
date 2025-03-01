# 🚀 IT Visionary - Gemini LLM Chatbot

## Overview
This project is a chatbot application using Streamlit for the frontend and FastAPI for the backend. The backend serves as an API to generate responses using a language model, while the frontend provides an interactive user interface for users to interact with the chatbot.

## Tech Stack
- **Frontend:** Streamlit (Python)
- **Backend:** FastAPI (Python)
- **Containerization:** Docker, Docker Compose

## Setup Instructions

### 1. Clone the Repository
```sh
   git clone <your-repo-url>
   cd IT-Visionary
```

### 2. Set Up the Backend
1. Navigate to the backend directory:
   ```sh
   cd backend
   ```
2. Create a virtual environment and install dependencies:
   ```sh
   python -m venv venv
   source venv/bin/activate 
   pip install -r requirements.txt
   ```
3. Run the backend:
   ```sh
   uvicorn llm_api:app --host 0.0.0.0 --port 8000
   ```
   The API will be available at `http://127.0.0.1:8000`

### 3. Set Up the Frontend
1. Navigate to the frontend directory:
   ```sh
   cd frontend
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```
   The UI will be available at `http://127.0.0.1:8501`

### 4. Run with Docker Compose
1. Navigate to the root directory and build the services:
   ```sh
   docker-compose up --build
   ```
2. The backend will run on `http://localhost:8000` and the frontend on `http://localhost:8501`.

## Project Structure
```
IT-Visionary/
│── backend/
│   ├── llm_api.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── .env
│── frontend/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│── docker-compose.yml
│── README.md
```

## Challenges Faced & Solutions

### 1. **Backend Connection Error**
**Issue:** The frontend could not connect to the backend, showing `Connection Refused` errors.

**Solution:** Updated the API URL in the frontend from `http://127.0.0.1:8000/generate` to `http://backend:8000/generate` in `docker-compose.yml` to ensure proper networking between services.

### 2. **CORS Issues**
**Issue:** The frontend couldn't fetch responses from the backend due to CORS restrictions.

**Solution:** Enabled CORS in FastAPI by adding the following code:
```python
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 3. **Docker Network Issues**
**Issue:** The frontend was not able to resolve the backend hostname inside the Docker network.

**Solution:** Used Docker Compose to define networked services, allowing them to communicate using service names (`backend`, `frontend`) instead of `localhost`.

## Deliverables
- **Fully functional chatbot application**
- **GitHub repository with source code**
- **Documentation (this README.md)**
- **Challenges faced and solutions provided**

---
### Contributors
- **Yara Mousa**

### License
This project is open-source and available under the MIT License.
