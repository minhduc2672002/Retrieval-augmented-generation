# 🔍 Retrieval-Augmented Generation for Large Language Models (LLM)

**Demo:** [📺 Watch on YouTube](https://www.youtube.com/watch?v=HJTrIfLI8Ow)

This project demonstrates how to use Retrieval-Augmented Generation (RAG) to combine the generative power of Large Language Models (LLMs) with the retrieval capabilities of a vector database for question-answering and knowledge-based systems.

---

## 📑 Table of Contents

- [📌 Introduction](#-introduction)
- [🏗️ Architecture](#️-architecture)
- [🔁 Flow](#-flow)
- [🖥️ User Interface](#-user-interface)
- [🔗 References](#-references)

---

## 📌 Introduction

**Retrieval-Augmented Generation (RAG)** is a technique that enhances the performance of LLMs in question-answering tasks by retrieving relevant context from an external knowledge base.

It works by:
- Retrieving relevant documents using a vector search engine.
- Feeding these documents into an LLM (e.g. LLaMA 3) along with the user query.
- Letting the LLM generate accurate, grounded answers based on real data.

---

## 🏗️ Architecture

![Architecture Diagram](https://github.com/user-attachments/assets/a24441c9-ed95-46a1-951b-27f6352ce21d)

Key components:
- **Text Preprocessing & Chunking**
- **Embedding using Language Models**
- **Vector Storage (ChromaDB)**
- **Retriever + LLM via Langchain Pipeline**

---

## 🔁 Flow

![Flow Diagram](https://github.com/user-attachments/assets/19ba9d7c-903d-49d5-bde9-703162f04c79)

### 🔍 Description:

- 📄 Raw data is in **text format** and split into chunks of **512 tokens**.
- 🔢 Each chunk is embedded into a **768-dimensional vector** using an embedding model.
- 🧠 Vectors are stored in a **vector database** (Chroma), and optionally indexed via **BM25** for hybrid retrieval.
- 🧩 Using **Langchain**, a retrieval pipeline is built combining:
  - Vector Search
  - LLM Query Processing (e.g. **LLaMA 3**)
- 🤖 The model returns relevant, context-aware answers based on embedded knowledge.

---

## 🖥️ User Interface

The application provides a clean interface to test query-answering on your custom document set.

### Chat Screen

![Chat Screenshot](https://github.com/user-attachments/assets/5cdeebd3-049a-4980-bf94-7edf916835ed)

### Document Upload and History

![Upload Screenshot](https://github.com/user-attachments/assets/a6d330b5-86c9-4b71-8b7a-0e23ec09dc80)

---

## 🔗 References

- [Langchain Documentation]()
