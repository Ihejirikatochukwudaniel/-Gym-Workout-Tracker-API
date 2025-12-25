# 🏋️ Gym Workout Tracker API

<div align="center">

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-red.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

**A production-grade FastAPI backend for comprehensive workout tracking, exercise management, progress analytics, and goal setting.**

Built with clean architecture principles and enterprise-level code quality.

[Features](#-key-features) • [Quick Start](#-quick-start) • [Documentation](#-api-documentation) • [Architecture](#️-architecture)

</div>

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Architecture](#️-architecture)
- [Project Structure](#-project-structure)
- [Database Schema](#️-database-schema)
- [Quick Start](#-quick-start)
- [API Documentation](#-api-documentation)
- [Authentication](#-authentication-flow)
- [Usage Examples](#-usage-examples)
- [Testing](#-testing)
- [Database Migrations](#-database-migrations)
- [Production Deployment](#-production-deployment)
- [Performance](#-performance-considerations)
- [Security](#️-security-best-practices)
- [Contributing](#-contributing)
- [Roadmap](#️-roadmap)
- [License](#-license)

---

## 🎯 Project Overview

This API provides a complete backend solution for fitness enthusiasts and personal trainers to track workouts, monitor progress, set goals, and analyze performance over time. The system supports multiple users, customizable exercise libraries, workout templates, and detailed analytics.

### 💡 Key Features

<table>
<tr>
<td width="50%">

#### Core Functionality
- 🔐 **JWT Authentication** - Secure auth with refresh tokens
- 💪 **Workout Management** - Full CRUD operations
- 📚 **Exercise Library** - Comprehensive database
- 📊 **Progress Tracking** - Automatic PR detection

</td>
<td width="50%">

#### Advanced Features
- 🎯 **Goal Setting** - Track strength & consistency
- 📈 **Analytics Dashboard** - Performance insights
- 📝 **Workout Templates** - Save favorite routines
- 🔍 **Advanced Filtering** - Search with pagination

</td>
</tr>
</table>

---

## 🏗️ Architecture

### Clean Architecture Layers

```
┌─────────────────────────────────────────┐
│        API Layer (Routes)               │  ← HTTP endpoints
├─────────────────────────────────────────┤
│        Service Layer (Business)         │  ← Business logic
├─────────────────────────────────────────┤
│        Repository Layer (Data)          │  ← Database operations
├─────────────────────────────────────────┤
│        Models Layer (Domain)            │  ← SQLAlchemy models
├─────────────────────────────────────────┤
│        Database Layer (SQLite)          │  ← Persistence
└─────────────────────────────────────────┘
```

### 🎨 Design Principles

| Principle | Implementation |
|-----------|----------------|
| **Separation of Concerns** | Each layer has single responsibility |
| **Dependency Injection** | FastAPI dependencies for services |
| **Repository Pattern** | Abstracted data access layer |
| **Service Pattern** | Encapsulated business logic |
| **DTO Pattern** | Pydantic schemas for validation |
| **Database Migrations** | Alembic version control |

---

## 📁 Project Structure

<details>
<summary><b>Click to expand full project structure</b></summary>

```
gym-workout-tracker/
├── 📁 app/
│   ├── main.py                          # FastAPI application factory
│   ├── config.py                        # Configuration management
│   │
│   ├── 📁 api/                          # API Layer
│   │   ├── deps.py                      # Dependency injection
│   │   └── 📁 v1/
│   │       ├── auth.py                  # Authentication endpoints
│   │       ├── users.py                 # User management
│   │       ├── workouts.py              # Workout CRUD
│   │       ├── exercises.py             # Exercise library
│   │       ├── templates.py             # Workout templates
│   │       ├── progress.py              # Progress tracking
│   │       ├── goals.py                 # Goal management
│   │       └── analytics.py             # Analytics endpoints
│   │
│   ├── 📁 services/                     # Business Logic Layer
│   │   ├── auth_service.py
│   │   ├── user_service.py
│   │   ├── workout_service.py
│   │   ├── exercise_service.py
│   │   ├── template_service.py
│   │   ├── progress_service.py
│   │   ├── goal_service.py
│   │   └── analytics_service.py
│   │
│   ├── 📁 repositories/                 # Data Access Layer
│   │   ├── base.py                      # Base repository
│   │   ├── user_repository.py
│   │   ├── workout_repository.py
│   │   ├── exercise_repository.py
│   │   ├── template_repository.py
│   │   ├── progress_repository.py
│   │   └── goal_repository.py
│   │
│   ├── 📁 models/                       # Database Models
│   │   ├── user.py
│   │   ├── workout.py
│   │   ├── exercise.py
│   │   ├── workout_exercise.py
│   │   ├── set.py
│   │   ├── template.py
│   │   ├── progress.py
│   │   └── goal.py
│   │
│   ├── 📁 schemas/                      # Pydantic Schemas (DTOs)
│   │   ├── user.py
│   │   ├── auth.py
│   │   ├── workout.py
│   │   ├── exercise.py
│   │   ├── template.py
│   │   ├── progress.py
│   │   ├── goal.py
│   │   └── common.py
│   │
│   ├── 📁 core/                         # Core Utilities
│   │   ├── security.py                  # JWT & password hashing
│   │   ├── exceptions.py                # Custom exceptions
│   │   └── constants.py                 # App constants
│   │
│   └── 📁 db/                           # Database Configuration
│       ├── base.py                      # Base model
│       ├── session.py                   # Session management
│       └── seed.py                      # Seeding script
│
├── 📁 alembic/                          # Database Migrations
│   └── 📁 versions/
│
├── 📁 tests/                            # Test Suite
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_workouts.py
│   ├── test_exercises.py
│   ├── test_progress.py
│   └── test_analytics.py
│
├── 📁 scripts/                          # Utility Scripts
│   ├── seed_exercises.py
│   └── create_admin.py
│
├── .env.example
├── requirements.txt
├── requirements-dev.txt
├── alembic.ini
└── README.md
```

</details>

---

## 🗄️ Database Schema

### Entity Relationship Diagram

```
┌──────────────┐         ┌──────────────────┐         ┌──────────────┐
│    User      │────────<│     Workout      │>────────│   Exercise   │
│              │         │                  │         │              │
│ • id         │         │ • id             │         │ • id         │
│ • email      │         │ • user_id (FK)   │         │ • name       │
│ • password   │         │ • date           │         │ • category   │
│ • name       │         │ • duration       │         │ • muscle_grp │
└──────┬───────┘         │ • notes          │         └──────┬───────┘
       │                 └────────┬─────────┘                │
       │                          │                          │
       │                 ┌────────▼─────────┐                │
       │                 │ WorkoutExercise  │◄───────────────┘
       │                 │ • id             │
       │                 │ • workout_id(FK) │
       │                 │ • exercise_id(FK)│
       │                 │ • order          │
       │                 └────────┬─────────┘
       │                          │
       │                 ┌────────▼─────────┐
       │                 │       Set        │
       │                 │ • id             │
       │                 │ • workout_ex(FK) │
       │                 │ • reps           │
       │                 │ • weight         │
       │                 │ • rest_seconds   │
       │                 └──────────────────┘
       │
       ├──>  ┌──────────────────┐
       │     │   Progress       │
       │     │ • id             │
       │     │ • user_id (FK)   │
       │     │ • exercise_id(FK)│
       │     │ • pr_weight      │
       │     │ • achieved_date  │
       │     └──────────────────┘
       │
       ├──>  ┌──────────────────┐
       │     │      Goal        │
       │     │ • id             │
       │     │ • user_id (FK)   │
       │     │ • type           │
       │     │ • target_value   │
       │     │ • deadline       │
       │     └──────────────────┘
       │
       └──>  ┌──────────────────┐
             │    Template      │
             │ • id             │
             │ • user_id (FK)   │
             │ • name           │
             │ • exercises_json │
             └──────────────────┘
```

<details>
<summary><b>View relationship details</b></summary>

| Relationship | Type | Description |
|--------------|------|-------------|
| User → Workouts | One-to-Many | A user has multiple workouts |
| Workout → WorkoutExercises | One-to-Many | A workout contains multiple exercises |
| Exercise → WorkoutExercises | One-to-Many | An exercise appears in multiple workouts |
| WorkoutExercise → Sets | One-to-Many | Each exercise has multiple sets |
| User → Progress | One-to-Many | User has PRs for different exercises |
| User → Goals | One-to-Many | User can set multiple goals |
| User → Templates | One-to-Many | User creates multiple templates |

</details>

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- pip (latest)
- Git

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/yourusername/gym-workout-tracker.git
cd gym-workout-tracker
```

**2. Create virtual environment**

<table>
<tr>
<td width="50%">

**Windows (PowerShell)**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

</td>
<td width="50%">

**macOS/Linux**
```bash
python -m venv .venv
source .venv/bin/activate
```

</td>
</tr>
</table>

**3. Install dependencies**

```bash
pip install --upgrade pip
pip install -r requirements.txt

# For development
pip install -r requirements-dev.txt
```

**4. Configure environment**

```bash
cp .env.example .env
```

Edit `.env`:

```env
# Application
APP_NAME=Gym Workout Tracker
DEBUG=True
API_V1_PREFIX=/api/v1

# Database
DATABASE_URL=sqlite:///./gym_tracker.db

# Security
SECRET_KEY=your-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# CORS
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000

# Pagination
DEFAULT_PAGE_SIZE=20
MAX_PAGE_SIZE=100
```

**5. Initialize database**

```bash
alembic upgrade head
python -m app.db.seed
```

**6. Start server**

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

> 🎉 **Success!** API running at `http://localhost:8000`
> 
> 📖 **API Docs:** `http://localhost:8000/docs`

---

## 📚 API Documentation

### 🔐 Authentication Endpoints

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| `POST` | `/api/v1/auth/register` | Register new user | ❌ |
| `POST` | `/api/v1/auth/login` | Login and get tokens | ❌ |
| `POST` | `/api/v1/auth/refresh` | Refresh access token | ✅ |
| `POST` | `/api/v1/auth/logout` | Logout user | ✅ |
| `GET` | `/api/v1/auth/me` | Get current user | ✅ |

### 👤 User Endpoints

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| `GET` | `/api/v1/users/profile` | Get user profile | ✅ |
| `PUT` | `/api/v1/users/profile` | Update profile | ✅ |
| `PUT` | `/api/v1/users/password` | Change password | ✅ |
| `DELETE` | `/api/v1/users/account` | Delete account | ✅ |

### 💪 Workout Endpoints

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| `GET` | `/api/v1/workouts` | List workouts (paginated) | ✅ |
| `POST` | `/api/v1/workouts` | Create workout | ✅ |
| `GET` | `/api/v1/workouts/{id}` | Get workout details | ✅ |
| `PUT` | `/api/v1/workouts/{id}` | Update workout | ✅ |
| `DELETE` | `/api/v1/workouts/{id}` | Delete workout | ✅ |
| `POST` | `/api/v1/workouts/{id}/exercises` | Add exercise to workout | ✅ |
| `POST` | `/api/v1/workouts/{id}/exercises/{ex_id}/sets` | Add sets | ✅ |

### 🏃 Exercise Endpoints

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| `GET` | `/api/v1/exercises` | List exercises (filterable) | ✅ |
| `POST` | `/api/v1/exercises` | Create custom exercise | ✅ |
| `GET` | `/api/v1/exercises/{id}` | Get exercise details | ✅ |
| `PUT` | `/api/v1/exercises/{id}` | Update exercise | ✅ |
| `DELETE` | `/api/v1/exercises/{id}` | Delete exercise | ✅ |
| `GET` | `/api/v1/exercises/categories` | Get categories | ✅ |
| `GET` | `/api/v1/exercises/muscle-groups` | Get muscle groups | ✅ |

### 📝 Template Endpoints

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| `GET` | `/api/v1/templates` | List user templates | ✅ |
| `POST` | `/api/v1/templates` | Create template | ✅ |
| `GET` | `/api/v1/templates/{id}` | Get template details | ✅ |
| `PUT` | `/api/v1/templates/{id}` | Update template | ✅ |
| `DELETE` | `/api/v1/templates/{id}` | Delete template | ✅ |
| `POST` | `/api/v1/templates/{id}/use` | Create workout from template | ✅ |

### 📊 Progress Endpoints

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| `GET` | `/api/v1/progress/prs` | Get personal records | ✅ |
| `GET` | `/api/v1/progress/exercise/{id}` | Exercise progress | ✅ |
| `GET` | `/api/v1/progress/history` | Workout history | ✅ |
| `GET` | `/api/v1/progress/volume` | Volume trends | ✅ |

### 🎯 Goal Endpoints

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| `GET` | `/api/v1/goals` | List user goals | ✅ |
| `POST` | `/api/v1/goals` | Create goal | ✅ |
| `GET` | `/api/v1/goals/{id}` | Get goal details | ✅ |
| `PUT` | `/api/v1/goals/{id}` | Update goal | ✅ |
| `DELETE` | `/api/v1/goals/{id}` | Delete goal | ✅ |
| `GET` | `/api/v1/goals/{id}/progress` | Get goal progress | ✅ |

### 📈 Analytics Endpoints

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| `GET` | `/api/v1/analytics/summary` | Weekly/monthly summary | ✅ |
| `GET` | `/api/v1/analytics/trends` | Performance trends | ✅ |
| `GET` | `/api/v1/analytics/muscle-groups` | Muscle distribution | ✅ |
| `GET` | `/api/v1/analytics/frequency` | Workout frequency | ✅ |

---

## 🔒 Authentication Flow

### Registration & Login Process

```
┌────────┐                    ┌─────────┐                    ┌──────────┐
│ Client │                    │   API   │                    │ Database │
└───┬────┘                    └────┬────┘                    └────┬─────┘
    │                              │                              │
    │ POST /auth/register          │                              │
    │─────────────────────────────>│                              │
    │                              │  Save user                   │
    │                              │─────────────────────────────>│
    │                              │                              │
    │                              │  User created                │
    │                              │<─────────────────────────────│
    │  201 Created                 │                              │
    │<─────────────────────────────│                              │
    │                              │                              │
    │ POST /auth/login             │                              │
    │─────────────────────────────>│                              │
    │                              │  Query user                  │
    │                              │─────────────────────────────>│
    │                              │                              │
    │                              │  User data                   │
    │                              │<─────────────────────────────│
    │                              │                              │
    │                              │  Verify password             │
    │                              │  Generate JWT tokens         │
    │                              │                              │
    │  200 OK + tokens             │                              │
    │<─────────────────────────────│                              │
```

### Token-Based Request Flow

```
┌────────┐         ┌─────────┐         ┌──────────────┐         ┌─────────┐
│ Client │         │   API   │         │ Auth Midware │         │ Service │
└───┬────┘         └────┬────┘         └──────┬───────┘         └────┬────┘
    │                   │                     │                      │
    │ GET /workouts     │                     │                      │
    │ Bearer: token     │                     │                      │
    │──────────────────>│                     │                      │
    │                   │  Verify JWT         │                      │
    │                   │────────────────────>│                      │
    │                   │                     │  Decode & validate   │
    │                   │                     │                      │
    │                   │  User context       │                      │
    │                   │<────────────────────│                      │
    │                   │                                            │
    │                   │  Get workouts with user context            │
    │                   │───────────────────────────────────────────>│
    │                   │                                            │
    │                   │  Workout data                              │
    │                   │<───────────────────────────────────────────│
    │                   │                                            │
    │  200 OK + data    │                                            │
    │<──────────────────│                                            │
```

---

## 🎯 Usage Examples

### Register and Login

```bash
# Register new user
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
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```

### Create Workout Session

```bash
# Create workout
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

# Add sets
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
```

### Query Progress

```bash
# Get personal records
curl -X GET http://localhost:8000/api/v1/progress/prs \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

# Get progress for specific exercise
curl -X GET http://localhost:8000/api/v1/progress/exercise/5 \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

# Get analytics summary
curl -X GET "http://localhost:8000/api/v1/analytics/summary?period=monthly" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

## 🧪 Testing

### Run Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_auth.py

# Run with verbose output
pytest -v

# Run specific test
pytest tests/test_workouts.py::test_create_workout
```

### Test Structure Example

```python
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
```

---

## 🔧 Database Migrations

### Create Migration

```bash
# Auto-generate from model changes
alembic revision --autogenerate -m "Add workout templates table"

# Create empty migration
alembic revision -m "Add indexes to workout table"
```

### Apply Migrations

```bash
# Upgrade to latest
alembic upgrade head

# Upgrade one version
alembic upgrade +1

# Downgrade one version
alembic downgrade -1

# View history
alembic history

# Check current version
alembic current
```

---

## 🏭 Production Deployment

### Environment Configuration

```env
DEBUG=False
DATABASE_URL=postgresql://user:password@db_host:5432/gym_tracker
SECRET_KEY=generate-a-strong-random-secret-key
ALLOWED_ORIGINS=https://yourdomain.com
```

### Docker Setup

**Dockerfile**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**docker-compose.yml**
```yaml
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
```

**Deploy**
```bash
docker-compose up -d
docker-compose exec api alembic upgrade head
docker-compose exec api python -m app.db.seed
```

---

## 📊 Performance Considerations

### Database Optimization

✅ **Indexes** - Applied on foreign keys, user_id, date fields  
✅ **Eager Loading** - Use `joinedload()` for related entities  
✅ **Query Optimization** - Select only needed columns  
✅ **Connection Pooling** - Configured in database session  

### Caching Strategies

Consider implementing **Redis** for:
- User sessions and JWT token blacklisting
- Frequently accessed exercise library
- Analytics computation caching
- Rate limiting

### Pagination

All list endpoints support pagination:

```bash
GET /api/v1/workouts?page=1&page_size=20
```

---

## 🛡️ Security Best Practices

### Implemented Security Measures

<table>
<tr>
<td width="50%">

#### Password Security
✅ Bcrypt hashing with salt  
✅ Password strength validation  
✅ Secure reset flow  

#### JWT Security
✅ Short-lived access tokens (30min)  
✅ Refresh token rotation  
✅ Token signature verification  
✅ Secure secret management  

</td>
<td width="50%">

#### Input Validation
✅ Pydantic schema validation  
✅ SQL injection prevention  
✅ XSS protection  

#### API Security
✅ CORS configuration  
✅ Rate limiting ready  
✅ HTTPS enforcement (prod)  
✅ Error handling  

</td>
</tr>
</table>

#### Data Privacy
✅ User data isolation (queries filtered by user_id)  
✅ Soft deletes for audit trails  
✅ No sensitive data in logs  

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/AmazingFeature`
3. **Commit** your changes with clear messages
4. **Add tests** for new functionality
5. **Run linting**: `black app/ && isort app/ && flake8 app/`
6. **Submit** a pull request

### Code Style Guidelines

- Follow **PEP 8** conventions
- Use **type hints** for function signatures
- Write **descriptive docstrings**
- Keep functions **focused** and under 50 lines
- Use **meaningful variable names**

---

## 🗺️ Roadmap

### Version 1.0 (Current)
- ✅ Core workout tracking
- ✅ Exercise library
- ✅ Progress monitoring
- ✅ Basic analytics

### Version 1.1 (Planned)
- [ ] Social features (share workouts)
- [ ] Workout recommendations
- [ ] Mobile app companion
- [ ] Advanced analytics (charts, trends)

### Version 2.0 (Future)
- [ ] Real-time workout tracking
- [ ] Video exercise demonstrations
- [ ] AI-powered form analysis
- [ ] Nutrition tracking integration

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Tochukwu Ihejirika Daniel**

[![GitHub](https://img.shields.io/badge/GitHub-ihejirikatochukwudaniel-black?style=flat&logo=github)](https://github.com/ihejirikatochukwudaniel)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat&logo=linkedin)](https://linkedin.com/in/tochukwu-ihejirika-daniel-902a51203/)
[![Email](https://img.shields.io/badge/Email-tochukwuihejirika3@gmail.com-red?style=flat&logo=gmail)](mailto:tochukwuihejirika3@gmail.com)

---

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - The incredible web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - Robust ORM
- [Pydantic](https://docs.pydantic.dev/) - Data validation
