__all__ = ("app", "Container",)

from app import app
import uvicorn




if __name__=="__main__":
    uvicorn.run("main:app", reload=True)

