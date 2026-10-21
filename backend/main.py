from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Study Sathi Backend is running!"}