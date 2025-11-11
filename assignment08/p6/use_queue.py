# CTMS-14
# a8 p6.py
# Ahmed Abasimel
# aabasimel@constructor.university


import module_queue

queue=[]

module_queue.enqueue(queue, 10)
module_queue.enqueue(queue, 20)
module_queue.enqueue(queue, 30)
module_queue.printq(queue)        # Should print [20, 30]

module_queue.enqueue(queue, 40)
module_queue.printq(queue)        # Should print [20, 30, 40]

module_queue.dequeue(queue)       # Removes 20
module_queue.dequeue(queue)       # Removes 30
module_queue.dequeue(queue) 
module_queue.printq(queue)        
module_queue.dequeue(queue)  
    
module_queue.dequeue(queue)  # Queue is empt