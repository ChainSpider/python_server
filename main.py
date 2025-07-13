from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

def generate_html_response():
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Альтернативный метод</title>
        </head>
        <body>
            <h1>Some text</h1>
            <p>Another scenario</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/items/", response_class=HTMLResponse)
async def read_items():
    return generate_html_response()