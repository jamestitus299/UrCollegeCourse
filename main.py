from fastapi import FastAPI
from api import users, sections, courses

from db.dbsetup import engine
from db.models import users, courses

users.Base.metadata.create_all(bind=engine)
courses.Base.metadata.create_all(bind=engine)

# API
app = FastAPI()

@app.get("/")
async def home():
    return "Hello World"

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)

