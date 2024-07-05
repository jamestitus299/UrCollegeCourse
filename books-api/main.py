from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "Welcome to The Books API"
