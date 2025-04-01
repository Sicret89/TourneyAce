from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from database import get_session
from models import Player

router = APIRouter()

@router.post("/")
def add_player(player: Player, session: Session = Depends(get_session)):
    session.add(player)
    session.commit()
    session.refresh(player)
    return player

@router.get("/")
def get_players(session: Session = Depends(get_session)):
    return session.exec(select(Player)).all()
