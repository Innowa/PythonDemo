from src.LICENSE import orm
from src.LICENSE.Model import User, Blog, Comment
import asyncio

loop = asyncio.get_event_loop()


def test():
    yield from orm.create_pool(loop=loop, host='127.0.0.1', port=3306, user='root', password='123456', db='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank', id="123")

    yield from u.save()


for x in test():
    loop.run_until_complete(test())
