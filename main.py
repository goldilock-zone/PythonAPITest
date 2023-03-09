from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get('/') #this is a route or a path operation
#get - this is the type of request that will be sent as an HTTP method
#The '/' is an indication to thge usage pf the root path of the website or the api dependign on the user case
def root():
    
    return {"message": "Welcome to my API!!!"} # FastAPI automatically converts dictionary outputs to JSON

@app.get('/posts')
def get_posts():
    #logic for retrieveing posts
    return{"data": "this is your posts"}

# to start the server weuse the uvicorn library

#NOTE: Fast API goes down the list of functions seuqentially, unless we specific asynchornicity, and refereneces teh first match

#NOTE: while running the server if we use:
#uvicorn main:app --reload
#the --reload is meant to run a live server - which keeps track of code changes continuously
#Do not use a --reload outside development environment

@app.post("/createposts")
def create_posts(payload: dict = Body(...) ): #body returns a dict
    #In postman, we send the data as part of the "body" of the request
    print(payload)
    return {"new_post": f"Title: {payload['title']} Content: {payload['content']}"}

