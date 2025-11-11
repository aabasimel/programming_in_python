# CTMS-14
# a8 p6.py
# Ahmed Abasimel
# aabasimel@constructor.university

def enqueue(q, item):
    q.append(item)
    print(f"Enqueued: {item}")

def dequeue(q):
    if not q:
        print("Queue is empty, cannot dequeue")
        return
    item = q.pop(0)
    print(f"Dequeued: {item}")
    return item

def printq(q):
    print("Queue content:", q)
