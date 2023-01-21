import threading
import queue
import time


def run(message, work):

    ping_q = queue.Queue()
    pong_q = queue.Queue()

    ping_q.put("start")

    ping_thread = threading.Thread(
        target=ping_pong_player,
        args=["Mr Ping", ping_q, pong_q, message, work],
        daemon=True,
    )
    pong_thread = threading.Thread(
        target=ping_pong_player,
        args=["Mr Pong", pong_q, ping_q, message, work],
        daemon=True,
    )

    ping_thread.start()
    pong_thread.start()

    time.sleep(1)

    ping_q.put("stop")
    pong_q.put("stop")

    ping_thread.join()
    pong_thread.join()


def ping_pong_player(name, own_q, other_q, message, work):
    start = time.time()
    counter = 0
    max_duration = 1

    while True:
        now = time.time()
        dif = now - start
        if dif > max_duration:
            break

        item = own_q.get()

        if item == "stop":
            break

        counter += 1

        message = work(message)

        other_q.put(message)

        own_q.task_done()

    print(f"{name} done. Received {counter} balls.")
