# Deployment Plan

## Stack

| Layer    | Platform              | Why                                              |
|----------|-----------------------|--------------------------------------------------|
| Backend  | Hugging Face Spaces   | Free, supports FastAPI via Docker, handles model.pkl easily |
| Frontend | Streamlit Community Cloud | Free, native Streamlit support, connects to any URL |

---

## Backend — Hugging Face Spaces (Docker)

Hugging Face Spaces supports Docker, so we can run FastAPI directly.

### Files needed inside `backend/`
- `main.py` — already done
- `model.pkl` — already exists
- `requirements.txt` — list of pip packages
- `Dockerfile` — tells HF how to build and run the app

### Steps
1. Create a new Space on huggingface.co → choose **Docker** template
2. Push `backend/` contents to that Space repo
3. HF builds the Docker image and exposes a public URL like:
   `https://<username>-<space-name>.hf.space`

---

## Frontend — Streamlit Community Cloud

### Files needed inside `frontend/`
- `app.py` — already done
- `requirements.txt` — streamlit, requests
- Update the API URL in `app.py` from `http://127.0.0.1:8000` to the HF Space URL

### Steps
1. Push the full project to a GitHub repo
2. Go to share.streamlit.io → connect GitHub repo → set main file to `frontend/app.py`
3. Deploy — Streamlit gives a public URL like:
   `https://<username>-<appname>.streamlit.app`

---

## Files to Create

- `backend/Dockerfile`
- `backend/requirements.txt`
- `frontend/requirements.txt`
- Update API URL in `frontend/app.py`

---

## Order of Steps

1. Create backend files (Dockerfile + requirements.txt)
2. Deploy backend to Hugging Face → get public URL
3. Update frontend API URL with HF URL
4. Push to GitHub
5. Deploy frontend to Streamlit Cloud
