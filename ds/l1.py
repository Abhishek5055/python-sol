def enqueue(Q):
    item = int(input("Enter an item to enqueue: "))
    Q.append(item)

def dequeue(Q):
    if len(Q) == 0:
        print("Queue Underflow")
    else:
        dequeued_item = Q.pop(0)
        print("Dequeued item:", dequeued_item)

def QFront(Q):
    if len(Q) == 0:
        print("Queue is empty")
    else:
        return Q[0]

def QRear(Q):
    if len(Q) == 0:
        print("Queue is empty")
    else:
        return Q[-1]

def disp(Q):
    if len(Q) == 0:
        print("Queue is Empty")
    else:
        print("The list is:")
        for item in Q:
            print(item, end=' ')
        print()  # Print a newline after displaying the queue

def main():
    Q = []
    while True:
        print("1.Enqueue 2.Dequeue 3.Disp 4.QFront 5.QRear 6.Exit")
        opt = int(input("Enter your option: "))
        if opt == 1:
            enqueue(Q)
        elif opt == 2:
            dequeue(Q)
        elif opt == 3:
            disp(Q)
        elif opt == 4:
            front_item = QFront(Q)
            if front_item is not None:
                print("Front item:", front_item)
        elif opt == 5:
            rear_item = QRear(Q)
            if rear_item is not None:
                print("Rear item:", rear_item)
        elif opt == 6:
            break
        else:
            print("Incorrect Choice")

if __name__ == "__main__":
    main()
