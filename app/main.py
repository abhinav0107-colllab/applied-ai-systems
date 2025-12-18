from fastapi import FastAPI

app = FastAPI(title="Applied AI Systems")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"version": "0.1.0"}
@app.get("/hello")
def hello():
    return {"message": "hello i am abhinav"}
