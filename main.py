from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/items/", response_class=StaticFiles)
async def read_items():
    return app.mount("/", StaticFiles(directory="static", html = True), name="static")