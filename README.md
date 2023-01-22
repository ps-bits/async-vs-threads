# asyncio vs threads
This experiment compares the speed of threads vs async in Python.
  
It creates two tests. One for threads, one for asyncio.  
In each test, two workers are created, each represented by threads or async tasks.  
  
They workers will send a message back and forth via a queue.  
They will also do some work on that message.  
  
This experiment then counts how many times the message was sent in 1 second.

## variations
To modify the experiment, you could alter the size of the message being sent, as well as the amount of work being done.  
That could lead to different results.
