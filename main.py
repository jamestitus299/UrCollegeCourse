from fastapi import FastAPI
from api import users, sections, courses

# API
app = FastAPI()

@app.get("/")
async def home():
    return "Hello World"

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)

