from fastapi import FastAPI
from fastapi.responses import FileResponse, StreamingResponse
from aigen import random_gen

some_file_path = "hello.mp4"
app = FastAPI()


@app.get("/")
async def main():
    return FileResponse("index.html")

@app.get("/generate")
def gen_page(): 
    # generate file
    random_gen('thing.mp4')
    def iterfile():  
        with open('thing.mp4', mode="rb") as file_like:  
            yield from file_like  
    return StreamingResponse(iterfile(), media_type="video/mp4")