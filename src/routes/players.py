from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from database import get_session
from auth.dependencies import get_current_admin
from models import Player, Admin

router = APIRouter(prefix="/players", tags=["Players"])

@router.post("/")
def add_player(player: Player, session: Session = Depends(get_session), admin: Admin = Depends(get_current_admin)):
    """Create a player under the logged-in admin."""
    player.admin_id = admin.id  # Assign player to the current admin
    session.add(player)
    session.commit()
    session.refresh(player)
    return player

@router.get("/")
def get_players(session: Session = Depends(get_session), admin: Admin = Depends(get_current_admin)):
    """Retrieve only the players associated with the logged-in admin."""
    return session.exec(select(Player).where(Player.admin_id == admin.id)).all()
