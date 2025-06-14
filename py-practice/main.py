from fastapi import FastAPI
import uvicorn

app = FastAPI()

def main():
    print("Hello from py-practice!")
    uvicorn.run(app , host = "0.0.0.0",  port=8000 )

@app.get("/")
async def root():
    return {
        "message":"Hello from fast-api"
    }

if __name__ == "__main__":
    main()
