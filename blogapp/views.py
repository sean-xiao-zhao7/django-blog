from django.shortcuts import render
from datetime import date

postsData = [{
    "slug": 'hiking',
    'image': 'mountains.jpg',
    'author': 'Pico',
    'date': date(2021, 7, 10),
    'title': 'Hiking',
    'content': 'Aliquam minus officia suscipit fuga impedit perferendis, repellat cumque debitis voluptatum natus veniam sit culpa enim, repellendus quos tempore cumque exercitationem tenetur est aliquid et, magnam ipsa voluptate veritatis dolores iure quia eius possimus quibusdam? Laborum aut voluptatum neque cum totam quam fugiat odio veritatis dignissimos porro, sint inventore commodi facere quasi facilis aliquam mollitia quia temporibus unde vero, voluptatum ducimus libero, cum consectetur doloribus asperiores qui enim adipisci aliquid. Doloribus impedit reprehenderit soluta consequatur vero est quia ipsa consectetur eaque. Unde excepturi cupiditate consequuntur aliquam ratione quia nulla ab distinctio praesentium, ipsum inventore rerum quibusdam eligendi veniam odit, earum aliquid fugit unde perferendis reiciendis repudiandae commodi, asperiores possimus aperiam expedita facilis labore nihil?',
    'excerpt': 'In rerum ut, incidunt error nulla dignissimos officiis nisi omnis unde laborum voluptatum facere autem? Laborum deleniti quo, vitae obcaecati facere porro quidem facilis?',
}, {
    "slug": 'pua',
    'image': 'mountains.jpg',
    'author': 'PUA',
    'date': date(2021, 7, 11),
    'title': 'PUA',
    'content': 'Aliquam minus officia suscipit fuga impedit perferendis, repellat cumque debitis voluptatum natus veniam sit culpa enim, repellendus quos tempore cumque exercitationem tenetur est aliquid et, magnam ipsa voluptate veritatis dolores iure quia eius possimus quibusdam? Laborum aut voluptatum neque cum totam quam fugiat odio veritatis dignissimos porro, sint inventore commodi facere quasi facilis aliquam mollitia quia temporibus unde vero, voluptatum ducimus libero, cum consectetur doloribus asperiores qui enim adipisci aliquid. Doloribus impedit reprehenderit soluta consequatur vero est quia ipsa consectetur eaque. Unde excepturi cupiditate consequuntur aliquam ratione quia nulla ab distinctio praesentium, ipsum inventore rerum quibusdam eligendi veniam odit, earum aliquid fugit unde perferendis reiciendis repudiandae commodi, asperiores possimus aperiam expedita facilis labore nihil?',
    'excerpt': 'In rerum ut, incidunt error nulla dignissimos officiis nisi omnis unde laborum voluptatum facere autem? Laborum deleniti quo, vitae obcaecati facere porro quidem facilis?',
},
    {
    "slug": 'alphamale',
    'image': 'mountains.jpg',
    'author': 'Alpha',
    'date': date(2021, 7, 12),
    'title': 'Alpha',
    'content': 'Aliquam minus officia suscipit fuga impedit perferendis, repellat cumque debitis voluptatum natus veniam sit culpa enim, repellendus quos tempore cumque exercitationem tenetur est aliquid et, magnam ipsa voluptate veritatis dolores iure quia eius possimus quibusdam? Laborum aut voluptatum neque cum totam quam fugiat odio veritatis dignissimos porro, sint inventore commodi facere quasi facilis aliquam mollitia quia temporibus unde vero, voluptatum ducimus libero, cum consectetur doloribus asperiores qui enim adipisci aliquid. Doloribus impedit reprehenderit soluta consequatur vero est quia ipsa consectetur eaque. Unde excepturi cupiditate consequuntur aliquam ratione quia nulla ab distinctio praesentium, ipsum inventore rerum quibusdam eligendi veniam odit, earum aliquid fugit unde perferendis reiciendis repudiandae commodi, asperiores possimus aperiam expedita facilis labore nihil?',
    'excerpt': 'In rerum ut, incidunt error nulla dignissimos officiis nisi omnis unde laborum voluptatum facere autem? Laborum deleniti quo, vitae obcaecati facere porro quidem facilis?',
}]


def get_date(post):
    return post['date']


def starting(req):
    temp = sorted(postsData, key=get_date)
    final = temp[-3:]
    return render(req, "blog/index.html", {"newests": final})


def posts(req):
    return render(req, 'blog/posts.html', {"postsData": postsData})


def post_details(req, slug):
    post = next(post for post in postsData if post['slug'] == slug)
    return render(req, 'blog/post.html', {"post": post})
