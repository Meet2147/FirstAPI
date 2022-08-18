
from fastapi import FastAPI
from fastapi.responses import FileResponse
import instaloader
from glob import glob
import os
from PIL import Image
from starlette.responses import StreamingResponse
from starlette.requests import Request

path = os.getcwd()


app = FastAPI()


@app.get("/")
def root():
  return {"Welcome": "Hello, World"}

@app.get("/path")
def path():
    return os.getcwd()

@app.get("/profile/")
def profile(username: str):
    obj = instaloader.Instaloader()
    obj.download_profile(username, profile_pic_only=True)
    
    file_path = glob(os.path.join(f"{username}",'*.jpg'))
    print(file_path)
    for i in file_path:
        return FileResponse(i)
    return {"error":"file not found"}
   
    
        #return FileResponse(filename)
    
    # if ext.lower() not in valid_images:
    #     return{"error":"Image not found"}
    # image_list.append(Image.open(os.path.join(path,file_path)))
    
   
    # for f in os.listdir():
        
    
    # path = f"/Users/meetjethwa/Developer/Projects/Insta_API/{username}"
    # file_path = os.path.join(path, '/*.jpg')
    # if os.path.exists(file_path):
