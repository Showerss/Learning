FIFO (first in first out like a line of people approaching a register)
    linear data structure
        head .......... to tail

enqueue is to add to the queue
dequeue is to remove from the queue


queue(string) queue = new LinkedList(string)

    enqueue is offer()
    dequeue is poll()

    queue.offer("phillip")
    queue.offer("matthew")
    queue.offer("andrew")

    print(queue.peek) #displays the first in the queue
    queue.poll() #removes phillip
    queue.pol() #now removes matthew since he moved to the head

    print(queue.size()) #prints how many things are in the queue
    print(queue.contains()) #is something inside the list

used in keyboard buffers like how a keyboard sends input
printer queues, print jobs or etc
used in linked lists, priority queues, etc
