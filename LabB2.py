#!/usr/bin/python3

#Jake Le
#4/19/2017


""" Demonstrate using a stack to find a solution to a maze. """

import Maze

class Stack:
  """ An implemtation of a stack. """
  def __init__(self):
    "Initialize an empty stack"
    self.data=[]
  def isEmpty(self):
    "Return true if the stack is empty"
    return self.data==[]
  def push(self,item):
    "Push item on top of the stack"
    self.data.append(item)
  def pop(self):
    "Pop the last item in the stack and return it"
    return self.data.pop()
  def peek(self):
    "Return the last item in the stack"
    return self.data[len(self.data)-1]
  def size(self):
    "Return the size of the stack"
    return len(self.data)

def solve(screen, maze):
  """ Return a list containing the path through the maze that solves the
      maze. If screen is not None, show the progress to solution on the
      screen. Return None if no solution path is found. 
  """
  maze.startCurses(screen)
  path=[maze.location()]
  solution=Stack()
  solution.push(path)
  visited=[]
  while solution.size()>=1:
    last=solution.pop()
    move=last[-1]
    visited.append(move)
    try:
      maze.tryMove(move,".")
    except Maze.MazeDone:
      path=list(last)
      break
    moves=maze.moves(last)
    for i in moves:
      if i not in visited:
        copy=list(last)
        copy.append(i)
        solution.push(copy)
  if len(path)<=1:
    return None
  return path

  # Create a stack.
  # Push the initial path onto the stack.
  # Until the stack is empty or a solution is found,
    # Pop a path off the stack.
    # Get the last move from the path.
    # Use maze.tryMove(move, ".") to test if the path is a solution.
    # Use maze.moves(path) to get a list of legal moves.
    # For each legal move:
      # Make a copy of path and append the legal move to the copy.
      # Push the new copy of the path onto the stack.

if __name__ == "__main__":
  import curses
  maze=( "+----+@+---+", \
         "|    | |   |", \
         "| +--+ | | |", \
         "| |    | | |", \
         "| | ---+ +-+", \
         "| |      | |", \
         "| | +--+-+ |", \
         "| | |  |   |", \
         "| |      +-+", \
         "| +-+ -+ | |", \
         "|   |  |   |", \
         "+---+--+!--+" )
  mazeController=Maze.Maze(maze,)
  print("PATH:")
  print(curses.wrapper(solve, mazeController))

  f=open("nomaze.txt","r")
  maze=Maze.Maze([line for line in f],0.1)
  f.close()
  print(curses.wrapper(solve,maze))

  # Example of reading a maze from a file:
  #f=open("nomaze.txt", "r")
  #mazeController=Maze.Maze([line for line in f],0)
  #f.close()
  #print(curses.wrapper(solve, mazeController))
