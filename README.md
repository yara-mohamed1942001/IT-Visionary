# 🚀 IT Visionary - Gemini LLM Chatbot

A full-stack AI-powered chatbot using **FastAPI (backend) and Streamlit (frontend)**, deployed with **Docker & Docker Compose**.

---

## 📌 **Deliverables**
### 📜 **Submission Requirements**
- ✅ **GitHub Repository** containing the full implementation and documentation.
- ✅ **Short Write-up** on app structure and challenges faced.

---

## 📦 **Project Structure**
The project follows a **modular architecture** for scalability:



---

## 🏗 **Short Write-up on App Structure**
The project consists of two main components:

### 🛠 **1. Backend (FastAPI)**
- Acts as an **API server** to process user queries.
- Provides an endpoint `/generate` for processing inputs and returning responses.
- Uses **Uvicorn** for efficient ASGI server deployment.

### 🎨 **2. Frontend (Streamlit)**
- Simple **chat interface** for user interaction.
- Sends user queries to the backend API and displays responses.
- Uses **requests** to communicate with the FastAPI backend.

### 🐳 **3. Deployment with Docker & Docker Compose**
- **Backend and Frontend** are containerized for **easy deployment**.
- **Docker Compose** manages both services in a single command.

---

## 🚀 **Setup & Run**
### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/YOUR_USERNAME/IT-Visionary.git
cd IT-Visionary

