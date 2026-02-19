# Empta

Mercis is a production-style ecommerce platform built with React and FastAPI.  
This project was developed as a learning initiative to gain hands-on experience with PostgreSQL ORM design, relational data modeling, and modern full-stack architecture.

## Tech Stack
- **Frontend:** React
- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Auth:** JWT-based authentication
- **API:** REST

## Core Features
- User authentication and authorization
- Product and category management
- Shopping cart and order processing
- Relational data modeling using PostgreSQL ORM
- RESTful API design with FastAPI

## Project Goals
- Learn and apply PostgreSQL ORM patterns
- Design normalized relational schemas
- Implement scalable backend architecture with FastAPI
- Build a modern full-stack ecommerce application

## Status
🚧 In active development

## Getting Started

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
