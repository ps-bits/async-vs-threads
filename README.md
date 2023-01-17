# treads vs asyncio
This experiment compares the speed of threads and async in Python.
  
Two ping pong players are created, each represented by a thread or async task.
They will send a "ball" back and forth via a queue.
(The ball is actually a text string)
  
This experiment counts how many times the ball was played in 1 second.
  
Once with threads, and once with asyncio.
  
## Result
Asyncio is faster in this comparison.