from fastapi import FastAPI

app = FastAPI()

@app.get('/') #this is a route or a path operation
async def root():
    return {"message": "Hello World"}

# to start the server weuse the uvicorn library
