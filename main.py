from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
import random

app = FastAPI()

class Post(BaseModel):
    # pydantic classes are used for in-built auto validation of data
    title: str
    content: str
    published: bool = True #this is a default value if the user does not defien a value for us
    rating: Optional[int] = None

#We need to make our API CRUD compliant

@app.get('/') #this is a route or a path operation
#get - this is the type of request that will be sent as an HTTP method
#The '/' is an indication to thge usage pf the root path of the website or the api dependign on the user case
def root():
    
    return {"message": "Welcome to my API!!!"} # FastAPI automatically converts dictionary outputs to JSON

#Just testing the routing of FASTAPI with this function


#-----------------------------------------------------------
# @app.get('/posts')
# def get_posts():
#     #logic for retrieveing posts
#     return{"data": "this is your posts"}

#-----------------------------------------------------------

# to start the server weuse the uvicorn library

#NOTE: Fast API goes down the list of functions seuqentially, unless we specific asynchornicity, and refereneces teh first match

#NOTE: while running the server if we use:
#uvicorn main:app --reload
#the --reload is meant to run a live server - which keeps track of code changes continuously
#Do not use a --reload outside development environment

#-----------------------------------------------------------
#NOTE:first implementation of the create_posts function

# @app.post("/createposts")
# def create_posts(payload: dict = Body(...) ): #body returns a dict
#     #In postman, we send the data as part of the "body" of the request
#     print(payload)
#     return {"new_post": f"Title: {payload['title']} Content: {payload['content']}"}

# for a post we want:
#title: str, content: str ( category, published: Bool)

#-----------------------------------------------------------
#NOTE: second implementation of the create_posts function\


my_posts = [
    {"title": "Title1", "content": "Content1", "id": 1},
    {"title": "Title2", "content": "Content2", "id": 2},
    ]

@app.get('/posts')
def get_posts(): #based on the naming convention, posts means all posts
    return{"data": my_posts} # the good thing about fast api is that if we send data in the form of a list, it automatically serializes it for us in JSON

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"] = random.randrange(0,1000000)
    print(post_dict)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get('/posts/{id}') #technical term for the id feild is called a path parameter
def get_post(id): #the parameters of the function have access to the path parameters in the decorator above
    print(id)
    return {"post_detail" : f"Here is post {id}"}
