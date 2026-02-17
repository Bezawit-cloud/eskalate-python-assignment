# Eskalate AI Python Assignment

This repository contains the solution for the Eskalate AI Training Software Engineer (Python) assignment.  
It includes the core application logic, a comprehensive test suite, Docker configuration, and setup instructions.

---

##  Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.11+
- `pip` or `conda` (for dependency management)
- Docker Desktop (optional, for containerized testing)

---

##  Running Tests Locally

Follow these steps to execute the test suite on your local machine:

1. **Activate your environment**:

```bash
conda activate eskalate-assignment
```
2. **Install dependencies** :

```
pip install -r requirements.txt
```

3. **Run the test suite**:
```
pytest -v
```

**Example of successful local test run:**

![Local Test Results](screenshots/pytest_local.png)


Note: Ensure all tests show a green PASSED status before committing changes.

---
## Running Tests via Docker

To ensure environment parity, you can run the entire suite within a Docker container:

1. **Build the Docker image**:
```
docker build -t eskalate-assignment .
```
2. **Run the container**:
```
docker run --rm eskalate-assignment
```

**Example of successful Docker test run:**

![Docker Test Results](screenshots/pytest_docker.png)

--- 

##  Repository Structure
.
├── app/                 # Application source code
├── tests/               # Unit and integration tests
├── Dockerfile           # Containerization setup
├── requirements.txt     # Pinned Python dependencies
├── README.md            # Project instructions
└── Explanation.md       # Detailed bug analysis and fix documentation



---
##  Project Notes

- **Automation:** The Dockerfile runs `pytest -v` automatically when executed.
- **Reproducibility:** Dependencies are pinned in `requirements.txt` to avoid "works on my machine" issues.
- **Precision:** Bug fixes were minimal and targeted, ensuring tests pass without side effects.
- **Verification:** Screenshots (if added) provide visual confirmation of successful runs locally and in Docker.

