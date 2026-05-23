from fastapi import FastAPI
import platform
import datetime

app=FastAPI()

@app.get("/")
def root():
    return {"msg":"TFS DevOps API is running"}

@app.get("/health")
def health_check():
    return{
        "status":"healthy",
        "timestamp":datetime.datetime.utcnow().isoformat(),
        "python_version":platform.python_version(),
        "system":platform.system()

    }


@app.get("/info")
def info():
    return{
        "app":"TFS DevOps Project",
        "version":"1.0.0",
        "environment":"local"
    }