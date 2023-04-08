# asyncio vs threads
This experiment compares Python's threads with Python's asyncio. 
  
It creates two tests. One for threads, one for asyncio.  

In each test, two worker tasks are created.  
The workers then send a message back and forth via a queue.  
They will also do some work on that message.  
  
The experiment then counts how many times the message was sent within 1 second.
