from fastapi import FastAPI
from fastapi.responses import FileResponse, StreamingResponse
from aigen import random_gen
import gdown
import os

some_file_path = "hello.mp4"
app = FastAPI()


@app.get("/")
async def main():
    return FileResponse("index.html")

@app.get("/generate")
def gen_page():
    # download model
    if not os.path.exists('smaller_trained_model'):
        os.mkdir('smaller_trained_model')
    if not os.path.exists("smaller_trained_model/config.json"):
        gdown.download(
            "https://drive.google.com/uc?id=1JkPZqaAuoX7eh4IuDQMVYpyu2IciQ-73", "smaller_trained_model/config.json", quiet=False
        )
    if not os.path.exists("smaller_trained_model/pytorch_model.bin"):
        gdown.download(
            "https://drive.google.com/uc?id=1OfAAfPNxorF-_hy7k1fysLBc6JJc7X41", "smaller_trained_model/pytorch_model.bin", quiet=False
        )
    # generate file
    random_gen('thing.mp4')
    def iterfile():  
        with open('thing.mp4', mode="rb") as file_like:  
            yield from file_like  
    return StreamingResponse(iterfile(), media_type="video/mp4")