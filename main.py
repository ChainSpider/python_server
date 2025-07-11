from fastapi import FastAPI
from fastapi.responses import HTML_Response

app = FastAPI()

@app.get("/", read_class=HTML_Response)
async def read_alternative():
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Альтернативный метод</title>
        <head>
        <body>
            <h1>Some text</h1>
            <p>Another scenario</p>
        </body>
    </html>
    """
    return html_content