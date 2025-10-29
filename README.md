🧠 Generative AI for Data Documentation (Prototype)
🚀 Automating Metadata Documentation and Schema Summarization with AI

This project is a Generative AI-powered assistant that automates the process of writing data documentation, metadata tagging, and schema summarization. It helps data teams reduce manual effort in understanding datasets, generating summaries, and creating structured documentation — all powered by LLMs (Large Language Models).

🏗️ Project Overview

Traditional data documentation is time-consuming and error-prone.
This GenAI assistant leverages OpenAI GPT models integrated with LangChain and Flask to automatically generate comprehensive and human-readable documentation for database schemas, datasets, and CSV files.

✨ Key Idea:
Feed your data → The AI analyzes schema → Generates clean, descriptive documentation in seconds.

⚙️ Features

✅ Automatic Metadata Extraction — Reads tables, columns, and datatypes from structured sources like CSV, JSON, or SQL.
✅ AI-Based Schema Summarization — Uses an LLM to generate short and long descriptions of each field.
✅ Smart Data Insights — Produces contextual explanations, example values, and relationships between tables.
✅ Documentation Generator — Converts analysis into Markdown, JSON, or HTML reports.
✅ Web Interface (Flask) — Simple frontend for uploading data and viewing generated documentation.
✅ Customizable Prompts — Modify AI behavior using prompt templates in LangChain.

🧩 Tech Stack
Component	Technology Used
Frontend	HTML, CSS, JavaScript
Backend	Python Flask
AI Framework	LangChain, OpenAI API
Data Handling	Pandas
Documentation Output	Markdown / JSON / HTML
Storage	Local / SQLite (optional)
🧠 How It Works

Upload Dataset / Connect DB

Upload a .csv, .json, or database schema file.

Data Profiling

The system analyzes columns, data types, and sample records.

Prompt Engineering

A structured prompt is created describing the schema and context.

AI Summarization

The LLM (via OpenAI API) generates detailed documentation and insights.

Documentation Output

View or download the final output in Markdown, JSON, or HTML format.
