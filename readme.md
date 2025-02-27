# Documentation Chatbot

A simple Flask-based chatbot that answers "how-to" questions by scraping and retrieving relevant documentation from the official documentation of four Customer Data Platforms (CDPs): **Segment**, **mParticle**, **Lytics**, and **Zeotap**. The chatbot uses web scraping to find relevant answers and display them to the user in a conversational interface.

## Features
- Fetches relevant documentation based on the user's query.
- Scrapes content from multiple platforms’ documentation (Segment, mParticle, Lytics, Zeotap).
- Displays answers or documentation snippets in a chat interface.
- Supports dynamic URL matching based on the user’s query.
- Provides a clean, simple web-based interface for querying.

## Platforms Supported
- **Segment**
- **mParticle**
- **Lytics**
- **Zeotap**

## Technologies Used
- **Flask**: Web framework for handling the backend.
- **BeautifulSoup4**: Library for web scraping and parsing HTML content.
- **Requests**: For making HTTP requests to the documentation URLs.
- **HTML/CSS/JavaScript**: For creating the frontend user interface.
- **Python**: Core programming language for backend logic.

## Setup Instructions

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.6 or higher
- Pip (Python package manager)



/documentation-chatbot
│
├── app.py                 # Flask application logic
├── requirements.txt       # List of dependencies
├── templates/             # Folder for HTML files
│   └── chatbot.html       # Frontend UI for the chatbot
└── static/                # Folder for static files (CSS/JS)
    └── style.css          # Styles for the chatbot UI
