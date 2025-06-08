from fastapi import FastAPI

app = FastAPI(title="Veterinaria API", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "🏥 API Veterinaria funcionando!"}

@app.get("/health")
async def health():
    return {"status": "healthy"}