class CircularQueue:
    def __init__(self, size):
        self.front = -1
        self.rear = -1
        self.size = size
        self.queue_list = [None] * size

    def isFull(self):
        # Queue is full when the next position of rear is front
        return (self.rear + 1) % self.size == self.front

    def isEmpty(self):
        # Queue is empty when front and rear are -1
        return self.front == -1

    def Enqueue(self, val):
        if self.isFull():
            print("QUEUE is full")
        else:
            if self.front == -1:  # First element to be inserted
                self.front = 0
            # Move rear circularly
            self.rear = (self.rear + 1) % self.size
            self.queue_list[self.rear] = val

    def Dequeue(self):
        if self.isEmpty():
            print("QUEUE has no Element")
            return None
        else:
            rem = self.queue_list[self.front]
            self.queue_list[self.front] = None
            if self.front == self.rear:  # Queue has become empty after dequeue
                self.front = -1
                self.rear = -1
            else:
                # Move front circularly
                self.front = (self.front + 1) % self.size
            return rem

    def Peak(self):
        if self.isEmpty():
            print("QUEUE has no Element")
            return None
        else:
            return self.queue_list[self.front]

# Usage
que = CircularQueue(int(input("Enter the size of queue: ")))
print("1-Enqueue, 2-Dequeue, 3-Peak, 4-Empty, 5-Full, 6-Exit")

while True:
    cas = int(input())

    match cas:
        case 1:
            que.Enqueue(int(input("Enter the enqueue element: ")))
            print(que.queue_list)
        case 2:
            print("Dequeued Element:", que.Dequeue())
            print(que.queue_list)
        case 3:
            print("Peak of Queue:", que.Peak())
        case 4:
            print("Queue is Empty:", que.isEmpty())
        case 5:
            print("Queue is Full:", que.isFull())
        case 6:
            break
