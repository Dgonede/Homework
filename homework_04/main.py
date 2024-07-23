import asyncio
from collections.abc import Sequence
from sqlalchemy import desc
from sqlalchemy import func
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.orm import joinedload
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
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
    
async def create_user(
    session: AsyncSession,
    username: str,
    email: str | None = None,
) -> User:
    user = User(username=username, email=email)
    session.add(user)

    await session.commit()

    print("user created:", user)
    return user


async def create_post(
    session: AsyncSession,
    title: str,
    user_id: int,
) -> Post:
    post = Post(title=title, user_id=user_id)
    session.add(post)
    await session.commit()
    print("post created:", post)
    return post

async def create_users(
    session: AsyncSession,
    *usernames: str,
) -> Sequence[User]:
    users = [
        User(username=username)
        for username in usernames
    ]
    session.add_all(users)
    print("prepared users:", users)

    

    print("saved users:", users)
    return users


async def create_posts(
    session: AsyncSession,
    *titles: str,
    user_id: int,
) -> Sequence[Post]:
    posts = [
        Post(title=title, user_id=user_id)
        for title in titles
    ]
    session.add_all(posts)
    print("prepared posts:", posts)
    
    print("saved posts:", posts)
    return posts


async def fetch_all_users(session: AsyncSession) -> Sequence[User]:
    stmt = select(User).order_by(desc(User.username))
    result = await session.scalars(stmt)
    users = result.all()
    print("users:", users)
    return users


async def fetch_users_with_posts(
    session: AsyncSession,
) -> Sequence[User]:
    stmt = (
        select(User)
        .options(
            # joinedload(User.posts),
            selectinload(User.posts),
        )
        .order_by(User.username)
    )

    print("load users w/ posts:")
    result = await session.scalars(stmt)
    users = result.all()
    for user in users:
        print("+", user)
        for post in user.posts:
            print("  -", post)

    return users


async def fetch_all_posts(session: AsyncSession) -> Sequence[Post]:
    stmt = select(Post).order_by(Post.id)
    result = await session.scalars(stmt)
    posts = result.all()
    print("posts:", posts)
    return posts


async def fetch_all_posts_with_authors(
    session: AsyncSession,
) -> Sequence[Post]:
    stmt = (
        select(Post)
        .options(
            joinedload(Post.user),
        )
        .order_by(Post.id)
    )
    result = await session.scalars(stmt)
    posts = result.all()
    print("posts:", posts)

    for post in posts:
        print("+", post)
        print("= user:", post.user)

    return posts


async def set_body_for_null_post_table(
    session: AsyncSession,
    title_size_limit: int,
    
):
    """

    :param session:
    :param username_size_limit:
    :param domain: example: '@ya.ru'
    :return:
    """

    new_body = (
        func.concat(
            func.upper(Post.title),
            Post.body == Post.title,
        )
    )
    stmt = (
        update(Post)
        .where(
            
            Post.body.is_(None),
            
            func.length(Post.title) < title_size_limit,
        )
        .values(
            {
                Post.body: new_body,
            }
        )
    )

    await session.execute(stmt)
    await session.commit()


async def async_main():
    await create_tables()
    async with Session() as session:
        await session.create_user(username="lone", email="lone@admin.com")
        gane: User = await session.create_user(session, username="gane", email=None)
        post_pg: Post = await create_post(
            session=session,
            title="Reander post",
            user_id=gane.id,
           
        )
        print("post pg:", post_pg)
        await create_users(session, "nick", "bob", "alice")
        sam: User = await session.create_user(session, username="sam", email=None)
        await create_posts(
            session,
            "MySQL Intro",
            "MariaDB Lesson",
            user_id=sam.id,
            
        )

        await fetch_all_posts_with_authors(session)
        await fetch_all_users(session)
        await fetch_users_with_posts(session)

        await fetch_all_posts(session)
       
def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()