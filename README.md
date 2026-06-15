# Topic Discovery on Cek Bansos Application Reviews using BERTopic

## Overview

This project was developed as part of the **NoLimit Indonesia Data Scientist Hiring Test**.

The objective of this project is to discover hidden discussion topics from user reviews of the **Cek Bansos** application available on Google Play Store using modern Natural Language Processing (NLP) techniques.

The project utilizes:

- Hugging Face Embedding Models
- UMAP Dimensionality Reduction
- HDBSCAN Clustering
- BERTopic Topic Modeling
- Streamlit Deployment

The resulting system can automatically identify discussion topics from user reviews and predict the most relevant topic for new incoming reviews.

---

## Business Problem

Government service applications receive thousands of user reviews every day.

Manually reading and categorizing these reviews is inefficient and time-consuming.

This project aims to:

- Identify major user concerns
- Discover hidden discussion themes
- Group similar reviews automatically
- Support data-driven decision making for application improvement

---

## Topic Selection

Before collecting data, trending topics were explored using Google Trends.

After analyzing publicly trending topics in Indonesia, the **Cek Bansos** application was selected due to:

- High public interest
- Large volume of user-generated reviews
- Social relevance
- Availability of public review data

---

## Dataset

### Source

Google Play Store Reviews

### Application

Cek Bansos

### Collection Method

Google Play Scraper

### Collected Attributes

| Attribute | Description |
|-----------|-------------|
| reviewId | Unique review identifier |
| content | User review text |
| score | User rating |
| at | Review date |

Dataset file:

```text
data/dataset_reviews_apk_cekbansos.csv
```

---

## Methodology

### End-to-End Pipeline

```text
Google Trends
      │
      ▼
Topic Selection
(Cek Bansos)
      │
      ▼
Google Play Review Scraping
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Text Preprocessing
      │
      ▼
Sentence Embedding
      │
      ▼
UMAP
      │
      ▼
HDBSCAN
      │
      ▼
BERTopic
      │
      ├── Topic Visualization
      ├── Topic Evaluation
      └── Topic Prediction
```

Flowchart image:

```text
flowchart/image.png
```

---

## Text Preprocessing

The following preprocessing techniques were applied:

- URL Removal
- Username Removal
- HTML Removal
- Emoji Removal
- Symbol Removal
- Number Removal
- Case Folding
- Tokenization
- Slang Normalization
- Stopword Removal

Additional resources:

- Indonesian Dictionary
- Indonesian Slang Dictionary
- Custom Stopword List

---

## Embedding Model

The project uses the following Hugging Face embedding model:

```python
LazarusNLP/all-indo-e5-small-v4
```

Reason:

- Optimized for Indonesian language
- Lightweight and efficient
- Strong semantic representation capability

---

## Topic Modeling Architecture

### Sentence Embedding

```text
Review Text
       │
       ▼
Sentence Transformer
```

### Dimensionality Reduction

```text
Sentence Embedding
       │
       ▼
UMAP
```

### Clustering

```text
Reduced Embedding
       │
       ▼
HDBSCAN
```

### Topic Discovery

```text
Clusters
       │
       ▼
BERTopic
```

---

## Model Components

| Component | Library |
|------------|---------|
| Embedding | Sentence Transformers |
| Reduction | UMAP |
| Clustering | HDBSCAN |
| Topic Modeling | BERTopic |
| Visualization | Plotly |
| Deployment | Streamlit |

---

## Topic Discovery Results

The model automatically groups reviews into multiple discussion topics.

Example discovered topics:

| Topic ID | Example Keywords |
|-----------|------------------|
| 0 | bansos, cek, aplikasi, ini, ada, dapat |
| 1 | koneksi, jaringan, wifi, masalah, bagus |
| 2 | data, nik, verifikasi |
| 3 | bansos, bantuan, penerima |
| 4 | update, versi, fitur |

Actual topic results can be explored through:

```python
topic_model.get_topic_info()
```

---

## Example Prediction

Input:

```text
Pemerintah membuat aplikasi yang sering error saat login
```

Output:

```json
{
  "topic_id": 1,
  "keywords": [
    "error",
    "login",
    "akun",
    "gagal"
  ],
  "confidence": 0.91
}
```

---

## Key Findings

Several dominant themes were identified from user reviews:

### Login Issues

Users frequently report authentication failures and account access problems.

### Application Errors

Many reviews mention crashes, bugs, and application instability.

### Data Verification

Users often discuss issues related to NIK validation and data synchronization.

### Social Assistance Information

Many users seek information regarding eligibility and social assistance status.

These findings can help prioritize future improvements of the application.

---

## Streamlit Application

A simple Streamlit application was developed to predict topics for new reviews.

Features:

- Review Input
- Topic Prediction
- Confidence Score
- Topic Keywords Display

Run locally:

```bash
streamlit run app.py
```

---

## Repository Structure

```text
.
.
├── app.py
├── requirements.txt
├── README.md
├── Topic_Discovery_Apk_CekBansos.ipynb
│
├── data/
├── models/
├── flowchart/
│
├── assets/
│   ├── streamlit_app.png
│   ├── topic_barchart.png
│   └── topic_hierarchy.png
│
├── outputs/
│   ├── topic_summary.csv
│   └── evaluation_results.csv
```

---

## Installation

Clone repository:

```bash
git clone https://github.com/AhmadMugiar/nolimit-ds-test-ahmadmugiarsujana.git
```

Move into project directory:

```bash
cd nolimit-ds-test-ahmadmugiarsujana
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running Notebook

Open:

```text
Topic_Discovery_Apk_CekBansos.ipynb
```

Run all cells sequentially.

---

## Running Streamlit

```bash
streamlit run app.py
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- NLTK
- BERTopic
- Sentence Transformers
- UMAP
- HDBSCAN
- Plotly
- WordCloud
- Streamlit
- Google Play Scraper

---

## Author

**Ahmad Mugiar Sujana**

Data Science & Machine Learning Enthusiast

GitHub:
https://github.com/AhmadMugiar

---

## Notes

This repository was developed for the NoLimit Indonesia Data Scientist Hiring Test and demonstrates an end-to-end NLP pipeline for topic discovery using transformer-based embeddings and BERTopic.
