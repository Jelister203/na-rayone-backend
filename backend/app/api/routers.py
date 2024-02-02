from . import models, schemas, db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(db.get_db)],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def create_user(user: schemas.UserCreate, db: Session = Depends(db.get_db)):
    db_user = models.User(**user.model_dump())
    if db.query(models.User).filter(models.User.email == db_user.email).first():
        raise HTTPException(status_code=409, detail="User with such email already exists.")
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/{user_id}")
async def read_user(user_id: int, db: Session = Depends(db.get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found.")
    return db_user
