from fastapi import FastAPI, HTTPException

app = FastAPI()

text_post = {1: {"title": "New Post", "content": "cool test post"}}

@app.get("/post")
def get_all_posts(limit: int = None):
    if limit:
        return  list(text_post.values())[:limit]
    return text_post

@app.post("/post/{id}")
def get_post(id: int):
    if id not in text_post:
         raise HTTPException(status_code=404, detail="Not found")
    return text_post.get(id)