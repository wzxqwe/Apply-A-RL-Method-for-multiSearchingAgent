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
from util import*
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
        print('Successors')
        util.raiseNotDefined()
        print('Successors')

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
    """

    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())

    # stack_dfs: ((x,y),[path]) #
    "*** YOUR CODE HERE ***"
    stack_dfs = Stack()

    explored_set = [] # explored_set states
    path = [] # Every state keeps it's path from the starting state
    finished_state = 0
    # Check if initial state is goal state #
    if problem.isGoalState(problem.getStartState()):
        return []

    # Start from the beginning and find a solution, path is an empty list #
    stack_dfs.push((problem.getStartState(),[]))

    while finished_state == 0:
        pos,path = stack_dfs.pop()
        explored_set.append(pos)

        # check terminate
        if problem.isGoalState(pos):
            print("dfs end")
            finished_state = 1
            return path
        else:
            # Get succor
            succor = problem.getSuccessors(pos)

            # Add new states
            if succor:
                for ele in succor:
                    if ele[0] not in explored_set:
                        updated_path = path + [ele[1]] 
                        stack_dfs.push((ele[0],updated_path))
                else:
                    pass
            #no solution
            if stack_dfs.isEmpty():
                finished_state = 1
                return []
        if stack_dfs.isEmpty():
            finished_state =1 
            return []
    if finished_state == 1:
        print('ok')
    else:
        print('go back check dfs')



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    #BFS USE QUEUE STORE FRONTIER AND GO WITH LAYER
    "*** YOUR CODE HERE ***"

    
    queue_bfs = Queue()
    explored_set = [] 
    path = [] 
    f_state = 0

    # Check INIT
    if problem.isGoalState(problem.getStartState()):
        f_state = 1
        return []
    #else:
    #	print('bfs state not ok yet')

    # Start 
    start_state = problem.getStartState()
    queue_bfs.push(( start_state, [] ))

    while(f_state==0):

        if queue_bfs.isEmpty():
            f_state = 1
            return []

        pos,path = queue_bfs.pop() 
        explored_set.append(pos)

        if problem.isGoalState(pos):
            f_state =1
            return path

        # loop frontier
        succors = problem.getSuccessors(pos)
        if succors:
            for ele in succors:
                if ele[0] not in explored_set:
                    if ele[0] not in (state[0] for state in queue_bfs.list):
                        updated_path = path + [ele[1]] # Calculate new path
                        queue_bfs.push((ele[0],updated_path))

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    # UFS basiclyy we just change bfs queue to a priority queue, measured by cost
    "*** YOUR CODE HERE ***"

    queue_bfs = PriorityQueue()

    explored_set = [] 
    path = [] 
    f_state = 0

    # init state
    if problem.isGoalState(problem.getStartState()):
        f_state =1
        return []

	# loop ft
    queue_bfs.push((problem.getStartState(),[]),0)

    while(f_state ==0):
        if queue_bfs.isEmpty():
            f_state =1
            return []


        pos,path = queue_bfs.pop() 
        explored_set.append(pos)

        if problem.isGoalState(pos):
            f_state = 1
            print('ufs state ' + str(f_state))
            return path


        succor = problem.getSuccessors(pos)

        # succssors
        if succor:
            for ele in succor:
                if ele[0] not in explored_set:
                	# check if succor == goal
                    if (ele[0] not in (state[-1][0] for state in queue_bfs.heap)):

                        updated_path = path + [ele[1]]
                        priority = problem.getCostOfActions(updated_path)
                        queue_bfs.push((ele[0],updated_path),priority)

                	# update priority queue by cost
                    elif ele[0] not in [x for x in explored_set]:
                        if (ele[0] in (state[-1][0] for state in queue_bfs.heap)):
                            for state in [x for x in queue_bfs.heap]:
                                if state[-1][0] == ele[0]:
                                    old_prioirity = problem.getCostOfActions(state[-1][1])
                            new_prioirity = problem.getCostOfActions(path + [ele[1]])

                      # State is cheaper with his hew father -> update and fix parent #
                        if old_prioirity > new_prioirity:
                            updated_path = path + [ele[1]]
                            queue_bfs.update((ele[0],updated_path),new_prioirity)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    # if this is a constant basically we are not having any heuris
    return 666


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    pri_queue = util.PriorityQueue()
    start_state = problem.getStartState()
    startNode = (start_state, [], 0)
    pri_queue.push(startNode, 0)
    explored_set = []
    f_state = 0
    while f_state== 0:
        # loop priori que by cost+heu
        path = pri_queue.pop()
        if problem.isGoalState(path[0]):
            f_state =1
            return path[1]
        if path[0] not in [x for x in explored_set]:
            explored_set.append(path[0])
            for successor in problem.getSuccessors(path[0]):
                if successor[0] in explored_set:
                    continue
                else:
                	# priori que measure by cost + heuristic val
                    cost = path[-1] + successor[-1]
                    totalCost = cost + heuristic(successor[0], problem)
                    temp_path = path[1] + [successor[1]]
                    pri_queue.push((successor[0], temp_path, cost), totalCost)

    print( 'A* Finished' + str(f_state) )


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch