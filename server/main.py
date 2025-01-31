import langchain
from fastapi import FastAPI
from chat.routes import router as chat_router
from fastapi.middleware.cors import CORSMiddleware

# Set LangChain runtime configurations
langchain.debug = True

# Instantiate FastAPI application
app = FastAPI(
    title="StationMaster",
    description="StationMaster - Chat with Railway Schedule",
)

# Setup routers
app.include_router(chat_router)

# Define allowed origins for CORS
origins = [
    "*",
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:4000",
]

# Setup CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Root route (to test service health)
@app.get("/", tags=["Internals"])
async def root():
    return {
        "message": "StationMaster is up and running.",
    }
