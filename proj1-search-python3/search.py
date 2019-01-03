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

import util


def generic_search_dfs_bfs(fringe_type, problem):
    """
    A generic search function implementation. DFS, BFS both
    in the same way except for the node structuring mechanism. This generic 
    search will take problem and popping mechanism and will return the expected
    actions. 
    """
    closed = set()
    fringe = fringe_type()

    if problem.isGoalState(problem.getStartState()):
        return []

    # Adding initial successors to the stack
    for successor in problem.getSuccessors(problem.getStartState()):
        fringe.push((successor, [successor[1]]))

    while not fringe.isEmpty():
        node, path = fringe.pop()
        state, _, _ = node
        if problem.isGoalState(state):
            return path

        if state not in closed:
            closed.add(state)
            for child_node in problem.getSuccessors(state):
                fringe.push((child_node, path+[child_node[1]]))
        else:
            print(f'Node {state} already expanded.')
    return None




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
    return generic_search_dfs_bfs(util.Stack, problem)
 

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    return generic_search_dfs_bfs(util.Queue, problem)



def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    closed = set()
    fringe = util.PriorityQueue()

    if problem.isGoalState(problem.getStartState()):
        return []
    
    for (successor_state, successor_action, successor_cost) in problem.getSuccessors(problem.getStartState()):
        fringe.push((successor_state, [successor_action]), successor_cost)

    while not fringe.isEmpty():
        state, path = fringe.pop()

        if problem.isGoalState(state):
            return path

        if state not in closed:
            closed.add(state)
            for (successor_state, successor_action, successor_cost) in problem.getSuccessors(state):
                fringe.push((successor_state, path + [successor_action]), successor_cost)
        else:
            print(f'Node {state} already expanded!')
    
    return None
        


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarPriorityGenerator(item):
    """
    A priority generator function that will generate priority value for aStar search
    problem. Assuming data is stored in queue as (state, cost, heuristic_val, path). 
    """
    _, cost, heuristic_val, _ = item
    return cost + heuristic_val


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    closed = set()
    fringe = util.PriorityQueueWithFunction(aStarPriorityGenerator)

    if problem.isGoalState(problem.getStartState()):
        return []

    for (successor_state, successor_action, successor_cost) in problem.getSuccessors(problem.getStartState()):
        fringe.push((successor_state, successor_cost, heuristic(successor_state, problem), [successor_action]))

    while not fringe.isEmpty():
        state, _, _, path = fringe.pop()

        if problem.isGoalState(state):
            return path
        
        if state not in closed:
            closed.add(state)
            for (successor_state, successor_action, successor_cost) in problem.getSuccessors(state):
                fringe.push((successor_state, successor_cost, heuristic(successor_state, problem), path + [successor_action]))
        else:
            print(f'Node {state} already expanded!')
    
    return None
        


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
