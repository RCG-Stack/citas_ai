from fastapi import FastAPI

app = FastAPI(
    title="Citas AI",
    description="Backend para la gestión automatizada de citas con IA",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "Bienvenido a Citas AI 🚀"}

