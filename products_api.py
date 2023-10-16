import fastapi
import uvicorn

api = fastapi.FastAPI()

@api.get('/products/all')
def dict_request():
    return api
