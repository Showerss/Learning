linked list

# better than an array in some ways... arrays are great at storing memory but lacks
# when setting in new elements, espiceally in larger lists
# linked list chains nodes into 2 parts, data and pointers
# non contigious data set
# tail of the data set will return null as a pointer
# bad at searching however, because you must work the list always, because theres only pointers going forward
# double linked list uses even more memory because theres pointers at both ends

linkedlist() = new LinkedList
linkedlist.push("phillip")
linkedlist.push("matthew")
linkedlist.push("andrew")
linkedlist.pop()


linkedlist.offer("phillip")
linkedlist.poll()

# linked list can be used as a stack or queue ^

linkedlist.add(4, "e") #add e to position 4
linkedlist.remove("e") #remove "e"

print(linkedlist.indexOf"e") #search linkedlist for "e"

print(linkedlist.peekFirst())
print(linkedlist.peekLast())

linkedlist.addFirst("0")
linkedlist.addLast("G")

