from fastapi import Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from models import Admin, Player, Tournament

def get_current_admin(session: Session = Depends(get_session), admin_id: int = 1):
    admin = session.exec(select(Admin).where(Admin.id == admin_id)).first()
    if not admin:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return admin

def get_players(session: Session = Depends(get_session), admin: Admin = Depends(get_current_admin)):
    return session.exec(select(Player).where(Player.admin_id == admin.id)).all()
