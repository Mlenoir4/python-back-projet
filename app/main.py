#System imports


# From Librairy import the class
from fastapi import FastAPI

# From Local import the class
from routers import userService, enterpriseService, activityService
import auth

app = FastAPI()


app.include_router(enterpriseService.router, tags=["enterprises"])
app.include_router(userService.router, tags=["users"])
app.include_router(activityService.router, tags=["planings"])
app.include_router(auth.router, tags=["auth"])


custom_responses = {
    204: {"description": "No content"},
    400: {"description": "Bad request"},
    401: {"description": "Unauthorized"},
    403: {"description": "Forbidden"},
    404: {"description": "Not found"},
    406: {"description": "Not acceptable"},
    500: {"description": "Internal server error"}
}

#Default route
@app.get("/")
async def root():
    return {"message": "Hello World"}

#Initialize database for User, Enterprise and Activity
@app.get("/initDatabase", tags=["initDatabase"])
async def initDatabase():
    userService.users = userService.initUsers()
    enterpriseService.enterprise = enterpriseService.initEnterprise()
    activityService.planings = activityService.initActivity()
    return {"message": "Database initialized"}
