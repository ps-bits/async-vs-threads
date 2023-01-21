import asyncio


def run(message, work):
    asyncio.run(main(message, work))


async def main(message, work):

    ping_q = asyncio.Queue()
    pong_q = asyncio.Queue()

    ping_task = asyncio.create_task(
        ping_pong_player("Mr Ping", ping_q, pong_q, message, work)
    )
    pong_task = asyncio.create_task(
        ping_pong_player("Mr Pong", pong_q, ping_q, message, work)
    )

    ping_q.put_nowait("start")

    await asyncio.sleep(1)

    ping_q.put_nowait("stop")
    pong_q.put_nowait("stop")

    # wait for the tasks to finish
    await ping_task
    await pong_task

    # tasks can also be stopped from the outside:
    # ping_task.cancel()
    # pong_task.cancel()


async def ping_pong_player(name, own_q, other_q, message, work):
    counter = 0
    while True:

        item = await own_q.get()

        if item == "stop":
            break

        counter += 1

        message = work(message)

        other_q.put_nowait(message)

    print(f"{name} done. Received {counter} balls.")
