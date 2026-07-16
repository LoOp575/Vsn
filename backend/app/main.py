from fastapi import FastAPI

app = FastAPI(
    title="VSN Formula Brain",
    version="0.1.0",
    description="Quantitative crypto analysis framework for MEXC"
)

@app.get("/")
def root():
    return {
        "project": "VSN Formula Brain",
        "status": "running",
        "version": "0.1.0"
    }

@app.get("/health")
def health():
    return {"status": "ok"}
