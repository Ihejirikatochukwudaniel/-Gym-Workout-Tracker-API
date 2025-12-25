Gym Workout Tracker API
A production-grade FastAPI backend for comprehensive workout tracking, exercise management, progress analytics, and goal setting. Built with clean architecture principles and enterprise-level code quality.
Show Image
Show Image
Show Image
Show Image

🎯 Project Overview
This API provides a complete backend solution for fitness enthusiasts and personal trainers to track workouts, monitor progress, set goals, and analyze performance over time. The system supports multiple users, customizable exercise libraries, workout templates, and detailed analytics.
Key Features

🔐 Authentication & Authorization: JWT-based secure authentication with refresh tokens
💪 Workout Management: Create, update, and delete workout sessions with detailed tracking
📚 Exercise Library: Comprehensive exercise database with muscle groups and categories
📊 Progress Tracking: Automatic PR (Personal Record) detection and historical tracking
🎯 Goal Setting: Set and monitor strength targets and consistency goals
📈 Analytics Dashboard: Weekly, monthly, and custom-range performance insights
📝 Workout Templates: Save and reuse favorite workout routines
🔍 Advanced Filtering: Search and filter across all entities with pagination
⚡ Performance Optimized: Efficient queries with eager loading and indexing


🏗️ Architecture
Clean Architecture Layers
┌─────────────────────────────────────────┐
│           API Layer (Routes)            │  ← HTTP endpoints, request/response
├─────────────────────────────────────────┤
│         Service Layer (Business)        │  ← Business logic, orchestration
├─────────────────────────────────────────┤
│       Repository Layer (Data Access)    │  ← Database operations, queries
├─────────────────────────────────────────┤
│         Models Layer (Domain)           │  ← SQLAlchemy models, relationships
├─────────────────────────────────────────┤
│          Database Layer (SQLite)        │  ← Persistence, transactions
└─────────────────────────────────────────┘
Design Principles

Separation of Concerns: Each layer has a single, well-defined responsibility
Dependency Injection: Services and repositories injected via FastAPI dependencies
Repository Pattern: Abstracts data access logic from business logic
Service Pattern: Encapsulates complex business operations
DTO Pattern: Pydantic schemas for request/response validation
Database Migrations: Version-controlled schema changes with Alembic


📁 Project Structure
gym-workout-tracker/
├── app/
│   ├── __init__.py
│   ├── main.py                      # FastAPI application factory
│   ├── config.py                    # Configuration management
│   │
│   ├── api/                         # API Layer
│   │   ├── __init__.py
│   │   ├── deps.py                  # Dependency injection functions
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── auth.py              # Authentication endpoints
│   │       ├── users.py             # User management endpoints
│   │       ├── workouts.py          # Workout CRUD endpoints
│   │       ├── exercises.py         # Exercise library endpoints
│   │       ├── templates.py         # Workout template endpoints
│   │       ├── progress.py          # Progress tracking endpoints
│   │       ├── goals.py             # Goal management endpoints
│   │       └── analytics.py         # Analytics and insights endpoints
│   │
│   ├── services/                    # Business Logic Layer
│   │   ├── __init__.py
│   │   ├── auth_service.py          # Authentication logic
│   │   ├── user_service.py          # User operations
│   │   ├── workout_service.py       # Workout business logic
│   │   ├── exercise_service.py      # Exercise management
│   │   ├── template_service.py      # Template operations
│   │   ├── progress_service.py      # Progress calculations
│   │   ├── goal_service.py          # Goal tracking logic
│   │   └── analytics_service.py     # Analytics computations
│   │
│   ├── repositories/                # Data Access Layer
│   │   ├── __init__.py
│   │   ├── base.py                  # Base repository with common CRUD
│   │   ├── user_repository.py
│   │   ├── workout_repository.py
│   │   ├── exercise_repository.py
│   │   ├── template_repository.py
│   │   ├── progress_repository.py
│   │   └── goal_repository.py
│   │
│   ├── models/                      # Database Models
│   │   ├── __init__.py
│   │   ├── user.py                  # User model
│   │   ├── workout.py               # Workout session model
│   │   ├── exercise.py              # Exercise definition model
│   │   ├── workout_exercise.py      # Workout-Exercise junction
│   │   ├── set.py                   # Individual set tracking
│   │   ├── template.py              # Workout template models
│   │   ├── progress.py              # Personal records model
│   │   └── goal.py                  # User goals model
│   │
│   ├── schemas/                     # Pydantic Schemas (DTOs)
│   │   ├── __init__.py
│   │   ├── user.py                  # User request/response schemas
│   │   ├── auth.py                  # Auth request/response schemas
│   │   ├── workout.py               # Workout DTOs
│   │   ├── exercise.py              # Exercise DTOs
│   │   ├── template.py              # Template DTOs
│   │   ├── progress.py              # Progress DTOs
│   │   ├── goal.py                  # Goal DTOs
│   │   └── common.py                # Shared schemas (pagination, etc.)
│   │
│   ├── core/                        # Core Utilities
│   │   ├── __init__.py
│   │   ├── security.py              # Password hashing, JWT utilities
│   │   ├── exceptions.py            # Custom exception classes
│   │   └── constants.py             # Application constants
│   │
│   └── db/                          # Database Configuration
│       ├── __init__.py
│       ├── base.py                  # Base model and metadata
│       ├── session.py               # Database session management
│       └── seed.py                  # Database seeding script
│
├── alembic/                         # Database Migrations
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── tests/                           # Test Suite
│   ├── __init__.py
│   ├── conftest.py                  # Pytest fixtures
│   ├── test_auth.py
│   ├── test_workouts.py
│   ├── test_exercises.py
│   ├── test_progress.py
│   ├── test_goals.py
│   └── test_analytics.py
│
├── scripts/                         # Utility Scripts
│   ├── seed_exercises.py            # Populate exercise library
│   └── create_admin.py              # Create admin user
│
├── .env.example                     # Environment variables template
├── .gitignore
├── alembic.ini                      # Alembic configuration
├── requirements.txt                 # Python dependencies
├── requirements-dev.txt             # Development dependencies
├── pyproject.toml                   # Project metadata
├── README.md                        # This file
└── LICENSE

🗄️ Database Schema
Entity Relationship Diagram
┌──────────────┐         ┌──────────────────┐         ┌──────────────┐
│    User      │────────<│     Workout      │>────────│   Exercise   │
│              │         │                  │         │              │
│ - id         │         │ - id             │         │ - id         │
│ - email      │         │ - user_id (FK)   │         │ - name       │
│ - password   │         │ - date           │         │ - category   │
│ - name       │         │ - duration       │         │ - muscle_grp │
└──────┬───────┘         │ - notes          │         └──────┬───────┘
       │                 └────────┬─────────┘                │
       │                          │                          │
       │                          │                          │
       │                 ┌────────▼─────────┐                │
       │                 │ WorkoutExercise  │◄───────────────┘
       │                 │                  │
       │                 │ - id             │
       │                 │ - workout_id(FK) │
       │                 │ - exercise_id(FK)│
       │                 │ - order          │
       │                 └────────┬─────────┘
       │                          │
       │                          │
       │                 ┌────────▼─────────┐
       │                 │       Set        │
       │                 │                  │
       │                 │ - id             │
       │                 │ - workout_ex(FK) │
       │                 │ - reps           │
       │                 │ - weight         │
       │                 │ - rest_seconds   │
       │                 └──────────────────┘
       │
       ├──────────────>  ┌──────────────────┐
       │                 │   Progress       │
       │                 │                  │
       │                 │ - id             │
       │                 │ - user_id (FK)   │
       │                 │ - exercise_id(FK)│
       │                 │ - pr_weight      │
       │                 │ - pr_reps        │
       │                 │ - achieved_date  │
       │                 └──────────────────┘
       │
       ├──────────────>  ┌──────────────────┐
       │                 │      Goal        │
       │                 │                  │
       │                 │ - id             │
       │                 │ - user_id (FK)   │
       │                 │ - type           │
       │                 │ - target_value   │
       │                 │ - deadline       │
       │                 │ - status         │
       │                 └──────────────────┘
       │
       └──────────────>  ┌──────────────────┐
                         │    Template      │
                         │                  │
                         │ - id             │
                         │ - user_id (FK)   │
                         │ - name           │
                         │ - description    │
                         │ - exercises_json │
                         └──────────────────┘
Key Relationships

User → Workouts: One-to-Many (A user has multiple workouts)
Workout → WorkoutExercises: One-to-Many (A workout contains multiple exercises)
Exercise → WorkoutExercises: One-to-Many (An exercise appears in multiple workouts)
WorkoutExercise → Sets: One-to-Many (Each exercise in a workout has multiple sets)
User → Progress: One-to-Many (User has PRs for different exercises)
User → Goals: One-to-Many (User can set multiple goals)
User → Templates: One-to-Many (User creates multiple templates)


🚀 Getting Started
Prerequisites

Python: 3.11 or higher
pip: Latest version
Virtual Environment: venv or virtualenv
Git: For version control

Installation

Clone the repository

bashgit clone https://github.com/yourusername/gym-workout-tracker.git
cd gym-workout-tracker

Create and activate virtual environment

Windows (PowerShell):
powershellpython -m venv .venv
.\.venv\Scripts\Activate.ps1
macOS/Linux:
bashpython -m venv .venv
source .venv/bin/activate

Install dependencies

bashpip install --upgrade pip
pip install -r requirements.txt
For development (includes testing and linting tools):
bashpip install -r requirements-dev.txt

Configure environment variables

bashcp .env.example .env
Edit .env with your configuration:
env# Application
APP_NAME=Gym Workout Tracker
DEBUG=True
API_V1_PREFIX=/api/v1

# Database
DATABASE_URL=sqlite:///./gym_tracker.db
# For PostgreSQL: postgresql://user:password@localhost/gym_tracker

# Security
SECRET_KEY=your-secret-key-here-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# CORS
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000

# Pagination
DEFAULT_PAGE_SIZE=20
MAX_PAGE_SIZE=100

Initialize the database

bash# Run migrations
alembic upgrade head

# Seed default exercises
python -m app.db.seed

Start the development server

bashuvicorn app.main:app --reload --host 0.0.0.0 --port 8000
The API will be available at: http://localhost:8000
Interactive API documentation: http://localhost:8000/docs

📚 API Documentation
Authentication Endpoints
MethodEndpointDescriptionAuth RequiredPOST/api/v1/auth/registerRegister new userNoPOST/api/v1/auth/loginLogin and get tokensNoPOST/api/v1/auth/refreshRefresh access tokenYesPOST/api/v1/auth/logoutLogout userYesGET/api/v1/auth/meGet current userYes
User Endpoints
MethodEndpointDescriptionAuth RequiredGET/api/v1/users/profileGet user profileYesPUT/api/v1/users/profileUpdate profileYesPUT/api/v1/users/passwordChange passwordYesDELETE/api/v1/users/accountDelete accountYes
Workout Endpoints
MethodEndpointDescriptionAuth RequiredGET/api/v1/workoutsList workouts (paginated)YesPOST/api/v1/workoutsCreate workoutYesGET/api/v1/workouts/{id}Get workout detailsYesPUT/api/v1/workouts/{id}Update workoutYesDELETE/api/v1/workouts/{id}Delete workoutYesPOST/api/v1/workouts/{id}/exercisesAdd exercise to workoutYesPOST/api/v1/workouts/{id}/exercises/{ex_id}/setsAdd set to exerciseYes
Exercise Endpoints
MethodEndpointDescriptionAuth RequiredGET/api/v1/exercisesList exercises (filterable)YesPOST/api/v1/exercisesCreate custom exerciseYesGET/api/v1/exercises/{id}Get exercise detailsYesPUT/api/v1/exercises/{id}Update exerciseYesDELETE/api/v1/exercises/{id}Delete exerciseYesGET/api/v1/exercises/categoriesGet exercise categoriesYesGET/api/v1/exercises/muscle-groupsGet muscle groupsYes
Template Endpoints
MethodEndpointDescriptionAuth RequiredGET/api/v1/templatesList user templatesYesPOST/api/v1/templatesCreate templateYesGET/api/v1/templates/{id}Get template detailsYesPUT/api/v1/templates/{id}Update templateYesDELETE/api/v1/templates/{id}Delete templateYesPOST/api/v1/templates/{id}/useCreate workout from templateYes
Progress Endpoints
MethodEndpointDescriptionAuth RequiredGET/api/v1/progress/prsGet personal recordsYesGET/api/v1/progress/exercise/{id}Get progress for exerciseYesGET/api/v1/progress/historyGet workout historyYesGET/api/v1/progress/volumeGet volume trendsYes
Goal Endpoints
MethodEndpointDescriptionAuth RequiredGET/api/v1/goalsList user goalsYesPOST/api/v1/goalsCreate goalYesGET/api/v1/goals/{id}Get goal detailsYesPUT/api/v1/goals/{id}Update goalYesDELETE/api/v1/goals/{id}Delete goalYesGET/api/v1/goals/{id}/progressGet goal progressYes
Analytics Endpoints
MethodEndpointDescriptionAuth RequiredGET/api/v1/analytics/summaryWeekly/monthly summaryYesGET/api/v1/analytics/trendsPerformance trendsYesGET/api/v1/analytics/muscle-groupsMuscle group distributionYesGET/api/v1/analytics/frequencyWorkout frequency statsYes

🔒 Authentication Flow
Registration & Login
mermaidsequenceDiagram
    participant Client
    participant API
    participant Auth Service
    participant Database

    Client->>API: POST /auth/register
    API->>Auth Service: Create user
    Auth Service->>Database: Save user
    Database-->>Auth Service: User created
    Auth Service-->>API: Success
    API-->>Client: 201 Created

    Client->>API: POST /auth/login
    API->>Auth Service: Validate credentials
    Auth Service->>Database: Query user
    Database-->>Auth Service: User data
    Auth Service->>Auth Service: Verify password
    Auth Service->>Auth Service: Generate tokens
    Auth Service-->>API: Access + Refresh tokens
    API-->>Client: 200 OK + tokens
Token-Based Requests
mermaidsequenceDiagram
    participant Client
    participant API
    participant Auth Middleware
    participant Service Layer

    Client->>API: GET /workouts (Bearer token)
    API->>Auth Middleware: Verify token
    Auth Middleware->>Auth Middleware: Decode JWT
    Auth Middleware->>Service Layer: Request with user context
    Service Layer-->>API: Response data
    API-->>Client: 200 OK + data

🧪 Testing
Run Tests
bash# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_auth.py

# Run with verbose output
pytest -v

# Run specific test
pytest tests/test_workouts.py::test_create_workout
Test Structure
python# Example test
def test_create_workout(client, auth_headers):
    """Test creating a new workout session."""
    payload = {
        "date": "2025-01-15",
        "duration_minutes": 60,
        "notes": "Chest day"
    }
    
    response = client.post(
        "/api/v1/workouts",
        json=payload,
        headers=auth_headers
    )
    
    assert response.status_code == 201
    data = response.json()
    assert data["duration_minutes"] == 60
    assert "id" in data

🔧 Database Migrations
Create Migration
bash# Auto-generate migration from model changes
alembic revision --autogenerate -m "Add workout templates table"

# Create empty migration
alembic revision -m "Add indexes to workout table"
Apply Migrations
bash# Upgrade to latest version
alembic upgrade head

# Upgrade by one version
alembic upgrade +1

# Downgrade by one version
alembic downgrade -1

# View migration history
alembic history

# View current version
alembic current

🎯 Usage Examples
Register and Login
bash# Register
curl -X POST http://localhost:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "SecurePass123!",
    "full_name": "John Doe"
  }'

# Login
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "SecurePass123!"
  }'

# Response:
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
Create Workout
bash# Create workout session
curl -X POST http://localhost:8000/api/v1/workouts \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2025-01-15",
    "duration_minutes": 60,
    "notes": "Push day - feeling strong"
  }'

# Add exercise to workout
curl -X POST http://localhost:8000/api/v1/workouts/1/exercises \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "exercise_id": 5,
    "order": 1
  }'

# Add sets to exercise
curl -X POST http://localhost:8000/api/v1/workouts/1/exercises/1/sets \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "sets": [
      {"reps": 8, "weight": 100, "rest_seconds": 90},
      {"reps": 8, "weight": 100, "rest_seconds": 90},
      {"reps": 6, "weight": 110, "rest_seconds": 120}
    ]
  }'
Query Progress
bash# Get personal records
curl -X GET http://localhost:8000/api/v1/progress/prs \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

# Get progress for specific exercise
curl -X GET http://localhost:8000/api/v1/progress/exercise/5 \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

# Get analytics summary
curl -X GET "http://localhost:8000/api/v1/analytics/summary?period=monthly" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

🏭 Production Deployment
Environment Configuration
For production, update your .env:
envDEBUG=False
DATABASE_URL=postgresql://user:password@db_host:5432/gym_tracker
SECRET_KEY=generate-a-strong-random-secret-key
ALLOWED_ORIGINS=https://yourdomain.com
Docker Deployment
dockerfile# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
yaml# docker-compose.yml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/gym_tracker
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=gym_tracker
      - POSTGRES_PASSWORD=password
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
Run with Docker
bashdocker-compose up -d
docker-compose exec api alembic upgrade head
docker-compose exec api python -m app.db.seed

📊 Performance Considerations
Database Optimization

Indexes: Applied on foreign keys, user_id, date fields
Eager Loading: Use joinedload() for related entities
Query Optimization: Select only needed columns
Connection Pooling: Configured in database session

Caching Strategies
Consider implementing Redis for:

User sessions and JWT token blacklisting
Frequently accessed exercise library
Analytics computation caching
Rate limiting

Pagination
All list endpoints support pagination:
bashGET /api/v1/workouts?page=1&page_size=20

🛡️ Security Best Practices
Implemented Security Measures
✅ Password Security

Bcrypt hashing with automatic salt
Minimum password strength validation
Secure password reset flow

✅ JWT Security

Short-lived access tokens (30 min)
Refresh token rotation
Token signature verification
Secure secret key management

✅ Input Validation

Pydantic schema validation
SQL injection prevention (SQLAlchemy ORM)
XSS protection through input sanitization

✅ API Security

CORS configuration
Rate limiting (recommended: add middleware)
HTTPS enforcement (production)
Comprehensive error handling without information leakage

✅ Data Privacy

User data isolation (queries filtered by user_id)
Soft deletes for audit trails
No sensitive data in logs


🤝 Contributing
Contributions are welcome! Please follow these guidelines:

Fork the repository
Create a feature branch: git checkout -b feature/AmazingFeature
Make your changes with clear commit messages
Add tests for new functionality
Run linting: black app/ && isort app/ && flake8 app/
Submit a pull request

Code Style

Follow PEP 8 conventions
Use type hints for function signatures
Write descriptive docstrings
Keep functions focused and under 50 lines
Use meaningful variable names


📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

👨‍💻 Author
Tochukwu Ihejirika

GitHub: @ihejirikatochukwudaniel
LinkedIn: https://www.linkedin.com/in/tochukwu-ihejirika-daniel-902a51203/
Email: tochukwuihejirka3@gmail.com


🙏 Acknowledgments

FastAPI for the incredible web framework
SQLAlchemy team for the robust ORM
Pydantic for data validation
The Python community


📮 Support
If you have questions or need help:

Check the API Documentation
Review existing issues
Create a new issue with detailed information
Reach out via email


🗺️ Roadmap
Version 1.0 (Current)

✅ Core workout tracking
✅ Exercise library
✅ Progress monitoring
✅ Basic analytics

Version 1.1 (Planned)

 Social features (share workouts)
 Workout recommendations
 Mobile app companion
 Advanced analytics (charts, trends)

Version 2.0 (Future)

 Real-time workout tracking
 Video exercise demonstrations
 AI-powered form analysis
 Nutrition tracking integration


Built for fitness enthusiasts and developers