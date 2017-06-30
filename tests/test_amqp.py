from aioworkers_amqp import AmqpQueue


class MockedAsynqp:
    AMQPError = RuntimeError

    class Message:
        def __init__(self, *args):
            self.a, = args

    def __getattr__(self, item):
        return self

    def __call__(self, *args, **kwargs):
        return self

    def __await__(self):
        async def coro():
            return self
        return coro().__await__()


async def test_queue(loop, mocker):
    mocker.patch('aioworkers_amqp.sync.asynqp', MockedAsynqp())
    config = mocker.Mock(format='json')
    config.connection.auth = {}
    config.connection.host = 'localhost'
    config.connection.port = 5672
    config.wait = 0
    context = mocker.Mock()
    q = AmqpQueue(config, context=context, loop=loop)

    c = True
    async def mocked_get():
        nonlocal c
        if c:
            c = False
            raise RuntimeError
        else:
            return q

    await q.init()
    async with q:
        await q.put('3')
        await q.get()

        q.queue.get = mocked_get
        await q.put('4')
        await q.get()
    assert {'reconnect': 1} == await q.status()
