"""Authentication endpoints: register, login, profile."""
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserRead, Token
from app.services.auth_service import get_auth_service, AuthService
from app.db.session import get_db
from app.core import config, security
from app.repositories.user_repo import UserRepository

router = APIRouter()


@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register(user_in: UserCreate, db: Session = Depends(get_db), svc: AuthService = Depends(get_auth_service)):
    """Register a new user. Returns created user (without password)."""
    user = svc.register(user_in=user_in)
    return user


@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Obtain JWT token using email (username field) and password."""
    svc = AuthService(db)
    user = svc.authenticate(email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token = svc.create_token(user_id=user.id, expires_delta=config.get_access_token_expires())
    return token


def _get_current_user(db: Session = Depends(get_db), token: str = Depends(security.create_access_token)):
    # This function is intentionally simple; proper dependency below.
    ...


from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

oauth2_scheme = HTTPBearer()


@router.get("/me", response_model=UserRead)
def me(credentials: HTTPAuthorizationCredentials = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """Get current user profile from JWT token."""
    token = credentials.credentials
    try:
        payload = security.decode_access_token(token)
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload")

    repo = UserRepository(db)
    user = repo.get_by_id(int(user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user
