from fastapi import FastAPI, HTTPException
from src.schemas import PostCreate, PostResponse
from src.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

text_post = {1: {"title": "New Post", "content": "cool test post"}}

@app.get("/post")
def get_all_posts(limit: int = None):
    if limit:
        return  list(text_post.values())[:limit]
    return text_post

@app.get("/post/{id}")
def get_post(id: int):
    if id not in text_post:
         raise HTTPException(status_code=404, detail="Not found")
    return text_post.get(id)

@app.post("/post")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {"title": post.title, "content": post.content}
    text_post[max(text_post.keys())+1] = new_post
    return new_post