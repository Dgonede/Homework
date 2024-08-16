import asyncio
from jsonplaceholder_requests import (
    fetch_posts_data, 
    fetch_users_data,
    )
from .models import (
    Session,
    async_engine, 
    Base, 
    User, 
    Post, 
    )


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
async def add_users(session, users_data):
    users = [User(name=user["name"], username=user["username"], email=user["email"]) for user in users_data]
    session.add_all(users)
    

async def add_posts(session, posts_data):
    posts = [Post(user_id=post["userId"], title=post["title"], body=post["body"]) for post in posts_data]
    session.add_all(posts)    
       
async def async_main():
    async with Session() as session:
        await create_tables()
        users_data, posts_data = await asyncio.gather(
            fetch_users_data(),
            fetch_posts_data(),
        )
        await add_users(session, users_data)
        await add_posts(session, posts_data)
        await session.commit()
        await session.close()


if __name__ == "__main__":
    asyncio.run(async_main())