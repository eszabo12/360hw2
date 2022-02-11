# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from multiprocessing import parent_process
from turtle import position
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


class Info:
    def __init__(self, position, parent, direction):
        self.position = position
        self.parent = parent
        self.direction = direction
        
def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # visited = set()
    stack = []
    #the state, the path, and the current visited list
    stack.append(((problem.getStartState(), None, None), [], set()))
    sols = []
    while stack:
        state = stack.pop() #last element on stack
        position = state[0][0]
        direction = state[0][1]
        path = state[1]
        visited = state[2]
        if position in visited:
            # print("visited")
            continue
        visited.add(position)
        if problem.isGoalState(position):
            sol = path + [direction]
            sol.pop(0)
            sols.append(sol)
            return sol
        children = problem.getSuccessors(position)
        for child in children:
            stack.append((child, path + [direction], visited))
    return sols[0]

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    visited = set()
    stack = []
    #the state, the path, and the current visited list
    stack.append(((problem.getStartState(), None, None), []))
    while stack:
        state = stack.pop(0) #last element on stack
        position = state[0][0]
        direction = state[0][1]
        path = state[1]
        if position in visited:
            # print("visited")
            continue
        visited.add(position)
        if problem.isGoalState(position):
            sol = path + [direction]
            sol.pop(0)
            return sol
        children = problem.getSuccessors(position)
        for child in children:
            stack.append((child, path + [direction]))
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # visited = set()
    stack = util.PriorityQueue()
    #the state, the path, and the current visited list
    stack.push(((problem.getStartState(), None, 0), [], 0, set()), 0)
    sols = []
    while not stack.isEmpty():
        deq = stack.pop()
        info, path, totalCost, visited = deq[0] #priority queue whatever
        print("priority: " + str(deq[1]))
        position, direction, currentCost = info
        if position in visited:
            # print("visited")
            continue
        visited.add(position)
        if problem.isGoalState(position):
            sol = path + [direction]
            sol.pop(0)
            sols.append(sol)
        children = problem.getSuccessors(position)
        for child in children:
            childCost = child[2]
            stack.push((child, path + [direction], totalCost + childCost, visited), totalCost + childCost)
    # return min(sols, key=len)
    print(len(sols))
    return sols[0]


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
