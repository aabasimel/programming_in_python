# CTMS-14
# a8 p5.py
# Ahmed Abasimel

# aabasimel@constructor.university

# Queue implementation using a Python list

# Initialize an empty queue
queue = []

# Function to add an element at the end
def enqueue(q, item):
    q.append(item)
    print(f"Enqueued: {item}")

# Function to remove an element from the front
def dequeue(q):
    if not q:
        print("Queue is empty. Cannot dequeue.")
        return None
    item = q.pop(0)
    print(f"Dequeued: {item}")
    return item

# Function to print the queue
def printq(q):
    print("Queue content:", q)

# Example usage
enqueue(queue, 10)
enqueue(queue, 20)
enqueue(queue, 30)
printq(queue)        # Should print [20, 30]

enqueue(queue, 40)
printq(queue)        # Should print [20, 30, 40]

dequeue(queue)       # Removes 20
dequeue(queue)       # Removes 30
dequeue(queue)       # Removes 40
dequeue(queue)       # Queue is empty