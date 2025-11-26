# 📘 **n8n + Git Versioning + FastAPI Project Template**

This project provides a clean and reproducible setup for working with **n8n**, **FastAPI**, and **Python scripts** in a shared Git environment.  
It is designed for students who collaborate on automation workflows and backend scripts while using Docker as the underlying infrastructure.

The goal is simple:

> **Clone → Configure → Start Containers → Import/Export Workflows → Run Python API**

Everything in this project is fully reproducible and works on **Windows**, **macOS**, and **Linux**.

---

# 📂 **Project Structure**

```
.
├── app/
│   ├── main.py
│   ├── requirements.txt
│   └── .gitkeep
├── workflows/
│   └── (exported n8n workflows as JSON files)
├── docker-compose.yml
├── .env.example
├── .gitignore
├── export_workflows.bat / export_workflows.sh
├── import_workflows.bat / import_workflows.sh
└── README.md
```

### **Directory Explanation**

| Folder / File | Purpose |
|---------------|---------|
| **app/** | Contains Python scripts. Students place their FastAPI code or other Python files here. |
| **app/main.py** | A minimal FastAPI REST API example. |
| **app/requirements.txt** | Python dependencies for the API. Students install these locally via `pip install -r app/requirements.txt`. |
| **workflows/** | Contains exported n8n workflow JSON files. These *are versioned* in Git for collaboration. |
| **docker-compose.yml** | Defines and starts the entire infrastructure (n8n + PostgreSQL). |
| **.env.example** | Template for environment variables. Students copy it to `.env`. |
| **export_workflows / import_workflows scripts** | Convenience scripts to export/import workflows to/from `workflows/`. |
| **.gitignore** | Ensures local caches, env files, and temporary directories are not committed. |

---

# 🚀 **How to Start (Step-by-Step for Students)**

This is the recommended order for running the project.

---

## **1️⃣ Clone the repository**

```bash
git clone <YOUR_REPO_URL>
cd <THE_PROJECT_FOLDER>
```

---

## **2️⃣ Create your `.env` file**

Copy the template:

```bash
cp .env.example .env
```

*(Windows PowerShell)*

```powershell
Copy-Item .env.example .env
```

Inside `.env`, set your encryption key and DB credentials if necessary.

---

## **3️⃣ Start the infrastructure (n8n + PostgreSQL)**

Make sure Docker Desktop (Windows/macOS) or Docker Engine (Linux) is running.

Then:

```bash
docker compose up -d
```

After a few seconds, n8n is available at:

👉 **http://localhost:5678**

---

## **4️⃣ Install Python dependencies (for the FastAPI service)**

Inside the project root:

```bash
pip install -r app/requirements.txt
```

This installs:

- FastAPI  
- Uvicorn  

Both are needed to run the example API.

---

## **5️⃣ Start the FastAPI server**

```bash
uvicorn app.main:app --reload --port 8000
```

The API is now available at:

- Swagger UI → **http://localhost:8000/docs**
- OpenAPI JSON → **http://localhost:8000/openapi.json**
- Example request → **http://localhost:8000/hello?name=Student**

---

## **6️⃣ Export n8n Workflows (into Git)**

Whenever you have created or updated workflows in n8n, run:

### Windows
```bat
export_workflows.bat
```

### macOS / Linux
```bash
./export_workflows.sh
```

This writes all workflow JSON files into:

```
workflows/
```

These files **are versioned in Git** → perfect for team collaboration.

---

## **7️⃣ Import Workflows (from Git into n8n)**

If you clone the project or switch machines:

### Windows
```bat
import_workflows.bat
```

### macOS / Linux
```bash
./import_workflows.sh
```

This loads all workflow JSON files into your n8n instance.

---

# 🧠 **Typical Student Workflow**

1. Start Docker containers  
2. Start FastAPI server  
3. Work in n8n UI  
4. Export workflows using the provided script  
5. Commit & push the `workflows/` folder  
6. Pull updates from teammates  
7. Import workflows when needed

This ensures **everyone stays in sync** without overwriting each other's work.

---

# 🛠️ **Troubleshooting**

### ❗ n8n says database connection failed

Run:

```bash
docker compose logs postgres
```

Make sure `.env` matches the values in `docker-compose.yml`.

---

### ❗ FastAPI won't start

Run:

```bash
pip install -r app/requirements.txt
```

Or check if Python is installed correctly (`python --version`).

---

### ❗ Workflow import/export fails

Make sure the n8n container is running:

```bash
docker ps
```

Look for a container named `n8n`.

---

# 🎉 **You’re Ready to Go!**

This project gives students a **clean, professional, and reproducible development workflow**, combining:

- Docker  
- n8n  
- Python  
- FastAPI  
- Git version control  

