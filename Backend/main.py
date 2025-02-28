import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.Routes import home_route
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(home_route.router,prefix="/home",tags=["Upload"])

if __name__ =="__main__":
    uvicorn.run(app,host="127.0.0.1",port=4000)