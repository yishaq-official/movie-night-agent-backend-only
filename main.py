from fastapi import FastAPI
from app.core.database import engine
from app.models import tables
from fastapi.middleware.cors import CORSMiddleware

# Import all routers
from app.api import sessions, users, movies

tables.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Movie Night Agent API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)


app.include_router(sessions.router)
app.include_router(users.router)
app.include_router(movies.router) 

@app.get("/")
def read_root():
    return {"message": "Movie Night Agent API is running."}

@app.get("/health")
def health_check():
    return {"status": "Database connected and Agent is online."}

