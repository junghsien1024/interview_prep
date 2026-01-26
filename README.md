# Interview Preparation Project

A full-stack application for interview preparation with React (TypeScript) frontend and Python (FastAPI) backend.

## Project Structure

```
interviews/
├── frontend/          # React + TypeScript frontend
│   ├── src/
│   ├── package.json
│   └── vite.config.ts
├── backend/           # Python FastAPI backend
│   ├── main.py
│   └── requirements.txt
└── README.md
```

## Prerequisites

- Node.js (v18 or higher)
- Python (v3.9 or higher)
- npm or yarn

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the backend server:
   ```bash
   python main.py
   ```
   
   Or using uvicorn directly:
   ```bash
   uvicorn main:app --reload --port 8000
   ```

   The API will be available at `http://localhost:8000`
   API documentation (Swagger UI) will be available at `http://localhost:8000/docs`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the development server:
   ```bash
   npm run dev
   ```

   The frontend will be available at `http://localhost:3000`

## API Endpoints

- `GET /health` - Health check endpoint
- `GET /api/questions` - Get all interview questions
- `GET /api/questions/{id}` - Get a specific question
- `POST /api/questions` - Create a new question
- `PUT /api/questions/{id}` - Update a question
- `DELETE /api/questions/{id}` - Delete a question

## Development

- Frontend runs on port 3000 with hot-reload
- Backend runs on port 8000 with auto-reload
- Frontend is configured to proxy API requests to the backend

## Next Steps

- Add a database (SQLite, PostgreSQL, etc.)
- Implement authentication
- Add more features for interview preparation
- Add testing (Jest for frontend, pytest for backend)
