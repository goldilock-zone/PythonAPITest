# Day 1

1. Get used to making get and post requests on postman
2. We use FASTAPI
3. @app.get(), is the decorator we use to make paths in our app
4. Always use a virtual enviorment while developing apps
5. app=FastAPI() is the way you intialize apps on FastAPI
6. Uvicorn main:app --reload is the way that we run the app in dev mode, where we dont have to restart the server everytime we make a change to our code
7. Here the doc link for fast api: https://fastapi.tiangolo.com/

# Day 2

1. It is important to make a schema for the data that we use as a back and forth data format between the backend and the front end
2. Use pydantic to make schemas. Here's the doc link to pydantic's website: https://docs.pydantic.dev/
3. pydantic gives a lot of inbuilt data validation for the JSON going back abnd forth between the front end and the back end of the system. To do so we create a pydantic model class that extends the BASeModel class of pydantic
4. We need to make CRUD compliant app: Create (POST), Read (GET) (either something specific, or all the data which is a non-specific request)), Update(PUT - pass every feild/PATCH - pass only the feild that needs to be changed) and Delete (DELETE)
5. Try exploring the typing library of python
6. The good thing about fast api is that if we send data in the form of a list, it automatically serializes it for us in JSON (JSON also has the concept of an array)
7. Realize: whatever your function returns is the  data that you send back to the user
8. Naming convention for functions that are GET requests: use plural for requests that involve retrieving all objects from an object type, and use singular when we reference the id to get a specific object (eg: get_posts() for all posts, vs get_post for a single post)
9. The path parameter that is passed in the api query is normally to refernce a particular object from the database (example, the id for a post)

# Day 3
