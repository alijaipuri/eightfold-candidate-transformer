# 🚀 Multi-Source Candidate Data Transformer

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge\&logo=python)
![Pydantic](https://img.shields.io/badge/Pydantic-v2-red?style=for-the-badge\&logo=pydantic)
![Pytest](https://img.shields.io/badge/Pytest-Tested-green?style=for-the-badge\&logo=pytest)
![Architecture](https://img.shields.io/badge/Architecture-Modular-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Production%20Inspired-success?style=for-the-badge)

### Building trustworthy candidate profiles from fragmented and conflicting data sources.

*A robust data transformation pipeline for candidate intelligence systems inspired by real-world talent platforms.*

</div>

---

# 📖 Overview

Recruitment systems receive candidate information from multiple independent sources:

* Applicant Tracking Systems (ATS)
* Recruiter Notes
* LinkedIn Profiles
* GitHub Profiles
* Resumes
* Internal Databases

These sources frequently contain:

* inconsistent names
* conflicting job titles
* duplicate records
* missing information
* noisy unstructured text

This project transforms heterogeneous candidate data into a single canonical candidate profile while preserving explainability, confidence scores, and provenance metadata.

---

# 🎯 Problem Statement

Given multiple noisy candidate representations:

| Source          | Example           |
| --------------- | ----------------- |
| ATS             | Ali A. Jaipuri    |
| LinkedIn        | Ali Asgar Jaipuri |
| GitHub          | Ali Asgar Jaipuri |
| Recruiter Notes | Ali Jaipuri       |

Determine:

* Are these records referring to the same candidate?
* Which value should be trusted?
* Why was a value selected?
* How confident are we in the decision?

---

# ✨ Features

## Multi-Source Ingestion

Supports ingestion from:

* ATS JSON exports
* Recruiter CSV records
* LinkedIn profile exports
* GitHub profile exports
* Resume text documents
* Recruiter notes

---

## Schema Normalization

Normalizes:

* Names
* Emails
* Phone Numbers
* Skills

Examples:

```text
ALI@EXAMPLE.COM
↓
ali@example.com
```

```text
9876543210
↓
+919876543210
```

---

## Entity Resolution

Detects whether multiple records belong to the same candidate using:

* Email similarity
* Phone similarity
* Name similarity

---

## Conflict Resolution

Resolves conflicting values using source confidence weighting.

Example:

| Source    | Company         |
| --------- | --------------- |
| ATS       | OpenAI          |
| Resume    | OpenAI Research |
| Recruiter | OpenAI          |

Result:

```json
{
  "value": "OpenAI",
  "selected_source": "recruiter_csv",
  "confidence": 1.0
}
```

---

## Confidence Scoring

Each canonical field includes:

* confidence score
* supporting evidence
* source attribution

Example:

```json
{
  "value": "Ali Asgar Jaipuri",
  "confidence": 1.0,
  "supporting_sources": [
    "recruiter_csv",
    "linkedin_profile",
    "github_profile"
  ]
}
```

---

## Provenance Tracking

Every decision made by the system is explainable.

Example:

```json
{
  "selected_source": "recruiter_csv",
  "alternatives": [
    "Ali A. Jaipuri"
  ],
  "resolution_strategy": "highest_source_confidence"
}
```

---

## Skill Aggregation

Combines skills across multiple independent sources.

Example:

```json
{
  "skill_name": "Python",
  "confidence": 0.94,
  "occurrence_count": 3
}
```

---

## Projection Engine

Supports generation of consumer-specific candidate views.

Examples:

* recruiter dashboard view
* search index view
* CRM export view
* matching engine view

---

## Automated Testing

Includes unit tests for:

* email normalization
* phone normalization
* field resolution
* skill aggregation
* canonical candidate generation

```text
10 tests passing
```

---

# 🏗️ System Architecture

```text
┌────────────────────────────┐
│     Recruiter CSV          │
├────────────────────────────┤
│        ATS JSON            │
├────────────────────────────┤
│     GitHub Profile         │
├────────────────────────────┤
│    LinkedIn Profile        │
├────────────────────────────┤
│        Resume              │
├────────────────────────────┤
│    Recruiter Notes         │
└─────────────┬──────────────┘
              │
              ▼
┌────────────────────────────┐
│      Ingestion Layer       │
└─────────────┬──────────────┘
              ▼
┌────────────────────────────┐
│    Normalization Layer     │
└─────────────┬──────────────┘
              ▼
┌────────────────────────────┐
│     Matching Engine        │
└─────────────┬──────────────┘
              ▼
┌────────────────────────────┐
│    Conflict Resolution     │
└─────────────┬──────────────┘
              ▼
┌────────────────────────────┐
│    Confidence Engine       │
└─────────────┬──────────────┘
              ▼
┌────────────────────────────┐
│   Canonical Builder        │
└─────────────┬──────────────┘
              ▼
┌────────────────────────────┐
│  Provenance Generator      │
└─────────────┬──────────────┘
              ▼
┌────────────────────────────┐
│ Canonical Candidate Model  │
└────────────────────────────┘
```

---

# 📂 Project Structure

```text
eightfold-candidate-transformer/
│
├── src/
│   ├── cli/
│   ├── core/
│   ├── ingestion/
│   ├── normalization/
│   ├── matching/
│   ├── merge/
│   ├── projection/
│   ├── validation/
│   └── models/
│
├── sample_data/
│
├── tests/
│
├── README.md
├── requirements.txt
└── pytest.ini
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/alijaipuri/eightfold-candidate-transformer.git
cd eightfold-candidate-transformer
```

## Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Pipeline

```bash
python -m src.cli.main \
--recruiter sample_data/recruiter/recruiter.csv \
--ats sample_data/ats/ats.json \
--github sample_data/github/github.json \
--linkedin sample_data/linkedin/linkedin.json \
--resume sample_data/resume/resume.txt \
--notes sample_data/notes/notes.txt
```

---

# 🧪 Running Tests

```bash
./venv/bin/python -m pytest -v
```

Example:

```text
==========================
10 tests passed
==========================
```

---

# 📊 Example Output

```json
{
  "full_name": {
    "value": "Ali Asgar Jaipuri",
    "confidence": 1.0
  },
  "primary_email": {
    "value": "ali@example.com",
    "confidence": 1.0
  },
  "current_company": {
    "value": "OpenAI",
    "confidence": 1.0
  }
}
```

---

# 🧠 Design Decisions

## Why Source Confidence Weighting?

Not all sources are equally reliable.

Priority:

1. Recruiter CSV
2. ATS Exports
3. LinkedIn Profiles
4. GitHub Profiles
5. Resumes
6. Recruiter Notes

This approach provides explainability and deterministic conflict resolution.

---

## Why Provenance Tracking?

Recruitment systems require transparency.

Every field should answer:

* Why was this value selected?
* Which sources supported it?
* Which alternatives existed?

---

## Why Canonical Profiles?

Downstream consumers should not need to understand individual source schemas.

The canonical model acts as a contract between producers and consumers.

---

# 🔮 Future Improvements

* Embedding-based entity matching
* LLM-assisted resume parsing
* Streaming ingestion pipelines
* Real-time source synchronization
* Graph-based candidate identity resolution
* Vector search integration
* Distributed processing support

---

# 👨‍💻 Author

**Ali Asgar Jaipuri**

B.E. Artificial Intelligence and Machine Learning
BMS College of Engineering, Bengaluru

---

<div align="center">

### Built for the Eightfold Internship Assignment 2026

*"Transforming fragmented candidate information into explainable intelligence."*

</div>
