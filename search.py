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
    # Busca em profundidade

    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

    # como deveria ser a resposta para o tinyMaze
    # ['South', 'South', 'West', 'South', 'West', 'West', 'South', 'West']

    from util import Stack

    

    def testeVini(): #python2 pacman.py -l tinyMaze -p SearchAgent
        accessed = []
        moveOrder = []
        steps = []
        inicial = []
        inicial.append(problem.getStartState())
        inicial.append('null')
        inicial.append('null')
        #accessed.append(inicial)

        def procura(atual):
            if atual in accessed:
                print "atual nos acessados"
                return False
            else:
                accessed.append(atual[0])
                steps.append(atual)
                print "acessou e andou para:", atual

            if problem.isGoalState(atual[0]):
                return True
            filhos = problem.getSuccessors(atual[0])
            print "filhos do atual", filhos
            if filhos:
                for filho in filhos:
                    print "acessando filho: ", filho
                    if not filho[0] in accessed:
                        if procura(filho):
                            return True
                        else:
                            temp = steps.pop()
                            print "passo pra tras, tirando:", temp[0]
                            return False
                    else:
                        print "filho ja acessado"
            else:
                return False

        if problem.isGoalState(inicial[0]):
            return []
        else:
            state = procura(inicial)
            print "estado do search: ", state
            for passo in steps:
                moveOrder.append(passo[1])
            print "ordem de movimentos:", moveOrder
            if moveOrder:
                return moveOrder
            else:
                return []
            


    def andre():
        accessed = []
        moveTo = []
        stack = Stack()
        aux = []
        aux.append(problem.getStartState())
        aux.append('nil')
        aux.append('nil')
        print aux
        stack.push(aux)
        lista = []
        while not stack.isEmpty():
            # armazena o no como acessado
            currentNode = stack.pop()
            # se esse no nao foi acessado
            if not currentNode in accessed:
                # seta ele como acessado
                accessed.append(currentNode)
                # lista.append(currentNode)
                print "Estou acessando o no: ", currentNode[0]
                if problem.isGoalState(currentNode[0]):
                    print "Chegou ao Final"

                    stack.push(currentNode)

                    # aux2.append(currentNode)
                    # dictionary[accessed[-2][0]] = aux2
                    break
                else:
                    for info in problem.getSuccessors(currentNode[0]):
                        if not info in accessed:
                            print "Vou colocar na pilha: ", info
                            t = info
                            t += (currentNode, )
                            lista.append(t)
                            # info += (currentNode, )
                            # print "infoooooooooooo:", info 
                            # break
                            # info.append(currentNode[0])
                            stack.push(info)
                            # aux2.append(info)
                    # dictionary[currentNode[0]] = aux2
        

        print accessed
        accessed.pop(0)
        print '----------- Lista com pai e filho em baixo'
        print lista

        go_to = []    

        auxiliar = [x for x in lista if x[0] == (1, 1)]
        go_to.append(auxiliar[0][3][1])
        aux2 = auxiliar[0][3][0]
        print aux2
        print aux2
        print aux2

        i = True
        while i:
            print "COMECO: ", aux2

            auxiliar = [x for x in lista if x[0] == aux2]
            print "auxiliar:  ", auxiliar
            go_to.append(auxiliar[0][3][1])
            aux2 = auxiliar[0][3][0]
            print "FINAL: ", aux2
            if aux2 == problem.getStartState():
                auxiliar = [x for x in lista if x[0] == aux2]
                go_to.insert(0, auxiliar[0][3][1])
                go_to.remove('nil')
                print go_to
                i = False
        print len(go_to)
        print len(go_to)
        print len(go_to)
        print len(go_to)
        print len(go_to)
        print go_to[::-1]
        return go_to[::-1]

        for element in lista:
            print "--Elemento--"
            print element
            print "--Elemento--"
    
        for element in accessed:
            moveTo.append(element[1])
        
        print len(moveTo)
        print len(moveTo)

        print moveTo
        print "Caminhos para mover acima ---------"
        return moveTo

        # from util import Stack
        # accessed = []
        # moveTo = []
        # stack = Stack()
        # stack.push(problem.getStartState())
        
        # while not stack.isEmpty():
        #     # Armazena o no como acessado
        #     currentNode = stack.pop()

        #     # Se esse no nao foi acessado
        #     if not currentNode in accessed:

        #         accessed.append(currentNode)
        #         print "Estou acessando o ", currentNode
        #         if problem.isGoalState(currentNode):
        #             print "Chegou ao Final, oq fazer?"
        #         else:
        #             for info in problem.getSuccessors(currentNode):
        #                 print "Vou colocar na pilha: ", info[0]
        #                 stack.push(info[0])
        # print accessed
        # util.raiseNotDefined()

    return testeVini()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

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
