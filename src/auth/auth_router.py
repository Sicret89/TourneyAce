from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from auth.security import hash_password, verify_password, create_access_token, get_current_admin
from database import get_session
from models import Admin
from datetime import timedelta

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register")
def register_admin(username: str, email: str, password: str, session: Session = Depends(get_session)):
    """Register a new admin user."""
    existing_admin = session.exec(select(Admin).where(Admin.email == email)).first()
    if existing_admin:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(password)
    new_admin = Admin(username=username, email=email, password=hashed_password)
    session.add(new_admin)
    session.commit()
    session.refresh(new_admin)
    return {"message": "Admin registered successfully"}

@router.post("/login")
def login_admin(email: str, password: str, session: Session = Depends(get_session)):
    """Authenticate an admin and return a JWT token."""
    admin = session.exec(select(Admin).where(Admin.email == email)).first()
    if not admin or not verify_password(password, admin.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": str(admin.id)}, expires_delta=timedelta(hours=1))
    return {"access_token": access_token, "token_type": "bearer"}
