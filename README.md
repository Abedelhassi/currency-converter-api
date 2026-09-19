
# 💱 Currency Converter API

![CI/CD Pipeline](https://github.com/Abedelhassi/currency-converter-api/actions/workflows/ci-cd.yml/badge.svg)

A production-ready REST API that converts amounts between currencies, stores conversion history in PostgreSQL, and is automatically deployed to AWS via a full CI/CD pipeline.

**Live Demo:** http://13.60.79.6/docs

---

## 🚀 Features

- **Convert currencies** between USD, EUR, DZD, GBP, and AED.
- **Persist conversion history** in PostgreSQL.
- **Interactive web UI** served at `/` (HTML + JavaScript).
- **Interactive API docs** at `/docs` (Swagger UI).
- **Input validation** with Pydantic.
- **Automated CI/CD** with GitHub Actions.
- **Security scanning** with Trivy (0 HIGH/CRITICAL vulnerabilities).
- **Secrets management** with AWS Secrets Manager.
- **Containerized** with Docker & Docker Compose.

---

## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| Backend | Python, FastAPI, SQLAlchemy (async) |
| Database | PostgreSQL 15 |
| Frontend | HTML, CSS, JavaScript |
| Containerization | Docker, Docker Compose |
| Cloud | AWS (EC2, ECR, IAM, Secrets Manager) |
| CI/CD | GitHub Actions |
| Security | Trivy, OWASP best practices |

---

## 🏗️ Architecture

```
┌─────────────┐      ┌──────────────┐      ┌──────────────┐
│  Browser    │─────▶│  FastAPI     │─────▶│ PostgreSQL   │
│  (HTML/JS)  │◀─────│  (Docker)    │◀─────│  (Docker)    │
└─────────────┘      └──────────────┘      └──────────────┘
                            ▲
                            │
                     ┌──────┴───────┐
                     │  AWS ECR     │
                     │  (Docker     │
                     │   Registry)  │
                     └──────────────┘
                            ▲
                            │
                     ┌──────┴───────┐
                     │ GitHub       │
                     │ Actions      │
                     │ (CI/CD)      │
                     └──────────────┘
```

---

## ⚙️ Run Locally

### Prerequisites
- Docker
- Docker Compose

### Steps

```bash
git clone https://github.com/Abedelhassi/currency-converter-api.git
cd currency-converter-api
docker compose up -d --build
```

Then open:
- Web UI: http://localhost:8000
- API Docs: http://localhost:8000/docs

---

## ☁️ Deployment (AWS)

This project uses a **fully automated CI/CD pipeline**:

1. Push code to the `main` branch.
2. GitHub Actions builds a Docker image.
3. Trivy scans the image for vulnerabilities.
4. The image is pushed to **Amazon ECR**.
5. GitHub Actions SSHes into **EC2** and redeploys the container.
6. Database credentials are fetched from **AWS Secrets Manager**.

---

## 🔐 Security

- ✅ **No hardcoded secrets** — all credentials live in AWS Secrets Manager.
- ✅ **Least-privilege IAM** — dedicated roles for GitHub Actions and EC2.
- ✅ **Container scanning** — Trivy blocks any CRITICAL/HIGH vulnerability.
- ✅ **Input validation** — Pydantic models enforce strict schemas.
- ✅ **Isolated network** — PostgreSQL is not exposed to the internet.

---

## 📌 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| POST | `/convert` | Convert an amount between two currencies. |
| GET | `/health` | Health check endpoint. |

**Example Request:**

```bash
curl -X POST http://13.60.79.6/convert \
  -H "Content-Type: application/json" \
  -d '{"amount": 100, "from_currency": "USD", "to_currency": "DZD"}'
```

**Example Response:**

```json
{
  "amount": 100,
  "from_currency": "USD",
  "to_currency": "DZD",
  "converted_amount": 13400.0,
  "rate": 134.0
}
```

---

## 🔮 Future Improvements

- [ ] Add HTTPS with CloudFront and a custom domain.
- [ ] Add JWT authentication for protected endpoints.
- [ ] Add unit tests with pytest.
- [ ] Add rate limiting.
- [ ] Migrate to AWS ECS Fargate for better scalability.

---

## 👤 Author

**Abdelhassib Lakhdari**
- GitHub: [@Abedelhassi](https://github.com/Abedelhassi)
- Email: a.lakhdari@univ-eltarf.dz

---

## 📄 License

This project is open-source and available for educational purposes.
