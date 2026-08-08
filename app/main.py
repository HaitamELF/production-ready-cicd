from fastapi import FastAPI

app = FastAPI(
    title="Production Ready CI/CD Demo",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Production Ready CI/CD",
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
