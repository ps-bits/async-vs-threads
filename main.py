import try_asyncio
import try_threading


if __name__ == "__main__":

    print("Async started!")

    try_asyncio.run()

    print("Async done! \n\nThreads started!")

    try_threading.run()

    print("Threads done!")
