# asyncio vs threads
This experiment compares the speed of threads vs async in Python.
  
Two workers are created, each represented by a thread or async task.
They will send a message back and forth via a queue.
They will reverse the message every time they receive it, to represent some work.
  
This experiment counts how many times the ball was played in 1 second.
  
Once with threads, and once with asyncio.
