import try_asyncio
import try_threading


def work(s: str) -> str:
    # Reverses a string. Used by the workers to do some random work.
    return s[::-1]


if __name__ == "__main__":

    message = "ball"

    print("Async started!")

    try_asyncio.run(message, work)

    print("Async done! \n\nThreads started!")

    try_threading.run(message, work)

    print("Threads done!")
