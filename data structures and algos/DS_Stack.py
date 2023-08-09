push - add to top
pop - remove from top
peek
empty
search

stack(string) stack = new(stack)

stack.push("phillip")
stack.push("matthew")
stack.push("andrew")

print(stack) - shows whole stack

stack.pop() # you dont need to add a parameter since it can ONLY remove the top anyways
            # if you pop too many things it returns an error

stack.peek() # shows the top most item in the data structure

stack.search() #

stacks can run out of memory

for (i=0 in; i<1000; 1+=):

uses of stacks are good for undo/redo in text editors move back or forward by one
browser back and forward
backtracking in file directoriies
calling functions aka call stacks