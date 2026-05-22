# 💼 Income Predictor AI

An end-to-end Machine Learning web application that predicts whether a person's income exceeds **50K/year** using demographic and employment-related attributes.

The project uses a deployed ML model with a modern full-stack deployment workflow:

- ⚡ FastAPI backend
- 🎨 Streamlit frontend
- 🤖 Scikit-learn ML pipeline
- ☁️ Hugging Face Spaces deployment
- 🚀 Streamlit Community Cloud deployment

---

# 🌐 Live Deployment

## Backend API
🔗 https://fede8rma-income-predict.hf.space/

### Swagger Docs
🔗 https://fede8rma-income-predict.hf.space/docs

---

## Frontend App
🔗 https://income-predictor-whx2blyfel8wzghpbshyue.streamlit.app/

---

# 🧠 Features

- Income prediction using ML
- FastAPI REST API
- Interactive Streamlit UI
- Real-time predictions
- Prediction confidence score
- Dockerized backend deployment
- Cloud-hosted frontend + backend

---

# 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Machine Learning | Scikit-learn |
| Backend API | FastAPI |
| Frontend | Streamlit |
| Model Serialization | Pickle |
| Deployment | Hugging Face Spaces |
| Frontend Hosting | Streamlit Community Cloud |
| Language | Python |

---

# 📂 Project Structure

```bash
income-predictor/
│
├── backend/
│   ├── main.py
│   ├── model.pkl
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
└── README.md
```

---

# ⚙️ Deployment Plan

## Stack

| Layer | Platform | Why |
|---|---|---|
| Backend | Hugging Face Spaces | Free, supports FastAPI via Docker |
| Frontend | Streamlit Community Cloud | Free, native Streamlit deployment |

---

# 🚀 Backend — Hugging Face Spaces (Docker)

Hugging Face Spaces supports Docker, allowing FastAPI to run directly inside a containerized environment.

## Backend Files

Inside `backend/`:

- `main.py`
- `model.pkl`
- `requirements.txt`
- `Dockerfile`

---

## Backend Deployment Steps

1. Create a new Docker Space on Hugging Face
2. Upload backend files
3. Hugging Face automatically builds the Docker image
4. Public API URL becomes available

Example:

```bash
https://fede8rma-income-predict.hf.space
```

---

# 🎨 Frontend — Streamlit Community Cloud

The frontend UI is built using Streamlit and connected to the deployed FastAPI backend.

## Frontend Files

Inside `frontend/`:

- `app.py`
- `requirements.txt`

---

## Frontend Deployment Steps

1. Push project to GitHub
2. Connect repository to Streamlit Cloud
3. Set main file path:

```bash
frontend/app.py
```

4. Deploy publicly

---

# 🔗 API Connection

Inside `frontend/app.py`:

```python
API_URL = "https://fede8rma-income-predict.hf.space/predict"
```

The frontend sends user input to the FastAPI backend and receives prediction results in real time.

---

# 🐳 Docker Configuration

## Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7860

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
```

---

# 📦 Backend Requirements

```txt
fastapi
uvicorn
pandas
numpy
scikit-learn==1.6.1
python-multipart
```

---

# 📦 Frontend Requirements

```txt
streamlit
requests
```

---

# ▶️ Clone and Run Locally

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

---

## 2️⃣ Move Into Project Folder

```bash
cd income-predictor
```

---

# ⚡ Backend Setup

## Move to backend folder

```bash
cd backend
```

---

## Create virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run FastAPI server

```bash
uvicorn main:app --reload
```

Backend runs on:

```bash
http://127.0.0.1:8000
```

Swagger docs:

```bash
http://127.0.0.1:8000/docs
```

---

# 🎨 Frontend Setup

## Open new terminal

Move to frontend folder:

```bash
cd frontend
```

---

## Create virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run Streamlit app

```bash
streamlit run app.py
```

Frontend runs on:

```bash
http://localhost:8501
```

---

# 🔮 Future Improvements

- SHAP explainability
- Authentication system
- Prediction history
- Dashboard analytics
- Dark/light mode
- Database integration
- CI/CD pipeline
- Kubernetes deployment
- Mobile-responsive UI

---

# 👨‍💻 Author

Built by Fahad Pervez 🚀

---