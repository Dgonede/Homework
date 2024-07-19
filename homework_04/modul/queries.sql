-- Active: 1720691113704@@127.0.0.1@5432@blog
SELECT users.username
, users.email
, users.id
, post_1.user_id
, post_1.title
, post_1.published_at
, post_1.id AS id_1    
FROM users 
    LEFT OUTER JOIN post AS post_1 
        ON users.id = post_1.user_id 
ORDER BY users.id;

--

SELECT users.username
, users.email
, users.id
FROM users ORDER BY users.id;

SELECT post.user_id AS post_user_id
, post.title AS post_title
, post.published_at AS post_published_at
, post.id AS post_id
FROM post
WHERE post.user_id IN (1, 2, 5);


SELECT post.user_id
, post.title
, users_1.username
, users_1.id AS id_1      
FROM post 
    LEFT OUTER JOIN users AS users_1 
    ON users_1.id = post.user_id 
ORDER BY post.id;

