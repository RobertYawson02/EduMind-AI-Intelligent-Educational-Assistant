# Intelligent Educational Assistant

A Flask-based educational question-answering assistant that combines controlled educational knowledge, Akan/Twi lexical support, optional Ghanaian QA data, TF-IDF/cosine retrieval and ranking, web retrieval, answer synthesis, and conversation context.

## Architecture

`User → Flask API → Intent/Topic → Conversation Context → Router → Local/Akan/Ghana-QA/Web Retrieval → TF-IDF Ranking → Answer Synthesis → JSON/UI`

## Run locally

```powershell
cd "D:\Robert Gaisie Yawson\Eric-Amponsah-Project-final\project\intelligent-qa-chatbot-final"
.\venv\Scripts\Activate.ps1
python scripts/runtime_validation.py
python -m unittest discover -s tests -p "test*.py" -v
python app.py
```

Open `http://127.0.0.1:5000` in a browser. The development server is for local work only.

## Host it and share a link

The repository includes `render.yaml`, so the simplest public deployment is Render:

1. Push this folder to a GitHub repository.
2. In Render, choose **New > Blueprint**, connect the repository, and select `render.yaml`.
3. Deploy the service. Render provides an HTTPS URL such as `https://edumind-ai.onrender.com`.
4. Share that HTTPS URL with your supervisor. The `/health` endpoint is the deployment check.

For a portable self-hosted deployment, use the included Docker image:

```powershell
docker build -t edumind-ai .
docker run --rm -p 5000:5000 edumind-ai
```

The Render Blueprint is configured for the free web service and free PostgreSQL plans. The free web service sleeps after inactivity and may take about a minute to wake up. Free PostgreSQL is limited to 1 GB and expires after 30 days, so export or upgrade the database before that deadline if you need to retain conversation history.

### Supervisor access

Set these Render environment variables before sharing the URL:

```text
AUTH_ENABLED=1
APP_USERNAME=supervisor
APP_PASSWORD_HASH=<generated password hash>
```

Generate a password hash locally without putting the password in source control:

```powershell
python -c "from werkzeug.security import generate_password_hash; print(generate_password_hash('replace-this-password'))"
```

Use the generated output as `APP_PASSWORD_HASH`. Keep `SECRET_KEY`, the password, and the hash private.

See [docs/DEPLOYMENT_AND_SYSTEM_MAP.md](docs/DEPLOYMENT_AND_SYSTEM_MAP.md) for the complete file map, request flow, security controls, deployment options, and production-readiness notes.

## Data

- `data/educational_knowledge.json` — controlled educational knowledge base (108 curated records in this project version).
- `data/akan_lexical_knowledge_base.json` — Akan/Twi lexical knowledge.
- `data/datasets/ghana_qa_sample.csv` — small offline Ghanaian QA sample for demonstration.
- `data/datasets/ghana_qa.csv` — optional full Ghana-QA dataset; if present it is preferred automatically.

## Validation

The runtime validation checks dependencies, knowledge retrieval, Akan translation, TF-IDF ranking, QA coordination, `/health`, and `/ask` API contracts. The confidence value is a system confidence indicator; project evaluation should report measured accuracy and retrieval metrics rather than claiming absolute 100% correctness.
