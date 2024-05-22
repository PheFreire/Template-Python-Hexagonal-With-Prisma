from fastapi import FastAPI
from pydantic import BaseModel

from entrypoints.controllers import (
    get_dependency_injections_controller,
    start_database_controller,
)
from entrypoints.routes import *

# origins = [
#     "http://localhost:3000",
#     "http://ip:port",
#     os.getenv("FRONTEND_API_HOST")
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.include_router()
app = FastAPI()

class Test(BaseModel):
    data: str


@app.post("/get_users_by_company")
async def test(test: Test):
    dependency_injections = get_dependency_injections_controller()
    database_executor_provider = await start_database_controller(
        dependency_injections
    )
    
    return 200