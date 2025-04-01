from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime

class Admin(SQLModel, table=True):
    """Admin model with login credentials."""
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str  # Hashed password

    tournaments: List["Tournament"] = Relationship(back_populates="admin")
    players: List["Player"] = Relationship(back_populates="admin")


class Tournament(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    start_date: datetime
    admin_id: int = Field(foreign_key="admin.id")

    admin: Admin = Relationship(back_populates="tournaments")


class Player(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    admin_id: int = Field(foreign_key="admin.id")

    admin: Admin = Relationship(back_populates="players")
