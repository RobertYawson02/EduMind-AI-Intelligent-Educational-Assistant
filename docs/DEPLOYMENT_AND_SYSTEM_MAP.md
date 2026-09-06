# Deployment and System Map

## What the system does

EduMind AI is a Flask web application for educational question answering. A user can ask an academic question, ask follow-up questions, search for supporting web evidence, inspect conversation context, and request Akan/Twi-aware responses from a browser or mobile device.

## Request flow

```text
Browser or mobile device
        |
        v
Flask routes in app.py
        |
        +--> /ask --------------> model/qa_engine.py
        +--> /chat --------------> model/enhanced_conversation_engine.py
        +--> /search ------------> model/web_engine.py
        +--> /semantic-analysis -> model/semantic_engine.py
        |
        v
Intent and language detection
        |
        v
Router and retrieval engines
        +--> controlled educational knowledge
        +--> Akan/Twi lexical knowledge
        +--> optional Ghana-QA CSV
        +--> optional educational web evidence
        |
        v
Ranking, synthesis, confidence, sources
        |
        v
JSON response rendered by templates/index.html
```

## File map

- `app.py`: Flask application, browser route, API routes, health check, and production WSGI object named `app`.
- `model/`: runtime intelligence. `router_engine.py` chooses retrieval paths; `knowledge_engine.py`, `akan_engine*.py`, `ghana_qa_engine.py`, and `web_engine.py` retrieve evidence; ranking and synthesis modules form the response.
- `data/`: runtime knowledge and conversation data. `data/educational_knowledge.json` is the controlled academic base; `data/akan/` contains expanded Akan resources.
- `data/datasets/`: optional external datasets and the offline Ghanaian sample. The full `ghana_qa.csv` is not required for startup.
- `templates/index.html`: responsive single-page chat interface and client-side API integration.
- `static/`: static assets available to the web interface.
- `scripts/`: dataset construction, scaling, and runtime validation utilities.
- `tests/`: unit and integration checks for engines, routes, datasets, and the final system.
- `render.yaml`: one-click Render Blueprint configuration.
- `Dockerfile`: portable container deployment for any Docker-compatible host.
- `requirements.txt`: pinned Python runtime dependencies, including Gunicorn for hosted deployment.

## Hosting and sharing

Render is the recommended first deployment because it can build directly from GitHub and supplies HTTPS. After deployment, share the generated service URL. A supervisor can use the same URL from a laptop, tablet, or phone without installing Python or copying the dataset.

Other suitable hosts are Railway, Fly.io, Google Cloud Run, Azure App Service, and an institutional VM. They all need the same production command:

```text
gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 4 --timeout 120 app:app
```

Conversation history is keyed by an opaque signed browser session ID and stored in SQLite locally or PostgreSQL when `DATABASE_URL` is configured. This prevents users from seeing one another's follow-up context and allows multiple hosted workers to share history. The current interface does not provide accounts or identity verification, so anonymous browser sessions are not an access-control boundary for confidential information.

## Production checklist

- Push the project to a private GitHub repository if the knowledge files are not intended to be public.
- Keep `SECRET_KEY` private and stable across deployments so signed sessions remain valid.
- Configure PostgreSQL through `DATABASE_URL` for multiple workers and reliable restarts; local SQLite is intended for development and single-instance use.
- Set `AUTH_ENABLED=1`, `APP_USERNAME`, and `APP_PASSWORD_HASH` to require supervisor sign-in before sharing the URL.
- Add a full account system with authorization roles if the project grows beyond one supervisor account.
- Add a retention policy and a way for users to delete stored conversation data.
- Keep the full Ghana-QA download outside Git history when licensing or repository size requires it.
- Configure rate limiting, request logging, error monitoring, and a custom domain for supervisor-facing use.
- Add automated tests for mobile layout, source attribution, malformed requests, and cold-start behavior.
- Report measured accuracy, retrieval precision, latency, and language coverage; confidence is not the same as accuracy.

## Health check

`GET /health` returns the service status, loaded knowledge-record count, and declared capabilities. Use it as the hosting platform's health check and as the first test after deployment.