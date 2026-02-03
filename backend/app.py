from fastapi import FastAPI
from routes.authRoute import router as AuthRouter
app = FastAPI()

app.include_router(AuthRouter)
@app.get("/",tags=['health'])
def health():
    return {"msg":"i am fine"} 