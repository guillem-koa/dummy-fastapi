from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

# redirect
@app.get("/", include_in_schema=False)
async def redirect():
    return RedirectResponse("/docs")

@app.get('/health_check')
def health_check():
    return('Everything OK!')
