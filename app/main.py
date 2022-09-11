import uvicorn
from fastapi import FastAPI

from server.api_v1.api import server_api_router
from config import DEBUG

app_server = FastAPI(title=f'TEST (Server API)', debug=DEBUG,)
app_server.include_router(server_api_router)

app = FastAPI()
app.mount('/api/v1', app_server)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)