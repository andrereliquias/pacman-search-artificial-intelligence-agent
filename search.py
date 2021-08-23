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

    from util import Stack
            
    def andre():
        stack = Stack()
        accessed = []

        aux = []
        aux.append(problem.getStartState())
        aux.append('nil')
        aux.append('nil')
        stack.push(aux) # aux => [(5, 5), 'nil', 'nil']
        mappedArray = [] # mappedArray => Array mapeado com pai e filhos

        while not stack.isEmpty():
            currentNode = stack.pop() # armazena o no como atual
            if not currentNode in accessed: # se esse no nao foi acessado
                accessed.append(currentNode) # seta ele como acessado
                print "Estou acessando o no: ", currentNode[0]

                if problem.isGoalState(currentNode[0]): # caso seja o no objetivo
                    print "Chegou ao Final"
                    print "No que encontrou o objetivo: ", accessed[-2]
                    stack.push(currentNode)
                    break
                else: # caso nao seja o objetivo
                    for info in problem.getSuccessors(currentNode[0]): # pega os sucessores dele
                        tupleAux = None
                        if not info in accessed: # caso o sucessor analisado ainda nao foi acessado
                            print "Vou colocar na pilha: ", info
                            tupleAux = info
                            tupleAux += (currentNode, )
                            mappedArray.append(tupleAux) # armazena em um array o mapeamento pai -> filho
                            stack.push(info)
        
        accessed.pop(0)
        print "\nCaminho percorrido pelo algoritmo de busca: ", accessed
        print "\nArray mapeado cru: ", mappedArray

        moveTo = []    
        currentFather = [x for x in mappedArray if problem.isGoalState(x[0])] # pega as informacoes do no objetivo
        moveTo.append(currentFather[0][3][1]) # pega o passo do pai do no objetivo
        currentCoordinate = currentFather[0][3][0] # seta a coordenada atual de verificacao como sendo a coordenada do pai

        print "Realizando o mapeamento: "
        while True:
            # vai interar pelo mapeamento navegando pelo pai de cada filho ate chegar no problema inicial
            print "No atual: ", currentCoordinate
            currentFather = [x for x in mappedArray if x[0] == currentCoordinate]
            moveTo.append(currentFather[0][3][1])
            currentCoordinate = currentFather[0][3][0]
            print "Encontrado por: ", currentCoordinate
            # caso encontre o inicio do problema
            if currentCoordinate == problem.getStartState():
                moveTo.remove('nil') # remover lixo
                currentFather = [x for x in mappedArray if x[0] == (1, 1)] # procura o primeiro movimento realizado e insere no comeco do array  
                moveTo.insert(0, currentFather[0][1])
                print "Custo atual para ", currentFather[0][1], problem.getCostOfActions(moveTo[::-1]) 
                break
        
        print "\nMovimentos necessarios para vencer: ", moveTo[::-1]
        print "Tamanho: ", len(moveTo), "\n"

        return moveTo[::-1]

    return andre()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    
    def andre():
        from util import Queue  
        queue = Queue()
        accessed = []

        aux = []
        aux.append(problem.getStartState())
        aux.append('nil')
        aux.append('nil')
        queue.push(aux) # aux => [(5, 5), 'nil', 'nil']
        mappedArray = [] # mappedArray => Array mapeado com pai e filhos

        while not queue.isEmpty():
            currentNode = queue.pop() # armazena o no como acessado
            if not currentNode in accessed: # se esse no nao foi acessado
                accessed.append(currentNode) # seta ele como acessado
                print "Estou acessando o no: ", currentNode[0]

                if problem.isGoalState(currentNode[0]): # caso seja o no objetivo
                    print "Chegou ao Final"
                    print "No que encontrou o objetivo: ", accessed[-2]
                    queue.push(currentNode)
                    break
                else: # caso nao seja o objetivo
                    for info in problem.getSuccessors(currentNode[0]): # pega os sucessores dele
                        tupleAux = None
                        if not info in accessed: # caso o sucessor analisado ainda nao foi acessado
                            print "Vou colocar na fila: ", info
                            tupleAux = info
                            tupleAux += (currentNode, )
                            mappedArray.append(tupleAux) # armazena em um array o mapeamento pai -> filho
                            queue.push(info)
        
        accessed.pop(0)
        print "\nCaminho percorrido pelo algoritmo de busca: ", accessed
        print "\nArray mapeado cru: ", mappedArray
        
        moveTo = []    
        currentFather = [x for x in mappedArray if problem.isGoalState(x[0])] # pega as informacoes do no objetivo

        moveTo.append(currentFather[0][3][1]) # pega o passo do pai do no objetivo
        currentCoordinate = currentFather[0][3][0] # seta a coordenada atual de verificacao como sendo a coordenada do pai

        print "Realizando o mapeamento: "
        while True:
            # vai interar pelo mapeamento navegando pelo pai de cada filho ate chegar no problema inicial
            print "No atual: ", currentCoordinate
            currentFather = [x for x in mappedArray if x[0] == currentCoordinate]
            moveTo.append(currentFather[0][3][1])
            currentCoordinate = currentFather[0][3][0]
            print "Encontrado por: ", currentCoordinate
            # caso encontre o inicio do problema
            if currentCoordinate == problem.getStartState():
                moveTo.remove('nil') # remover lixo
                currentFather = [x for x in mappedArray if problem.isGoalState(x[0])] # procura o primeiro movimento realizado e insere no comeco do array  
                moveTo.insert(0, currentFather[0][1])
                print "Custo atual para ", currentFather[0][1], problem.getCostOfActions(moveTo[::-1]) 
                break
        
        print "\nMovimentos necessarios para vencer: ", moveTo[::-1]
        print "Tamanho: ", len(moveTo), "\n"

        return moveTo[::-1]
        
    return andre()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    def andre():
        from util import PriorityQueue
        pQueue = PriorityQueue()
        accessed = []

        aux = []
        aux.append(problem.getStartState())
        aux.append('nil')
        aux.append('nil')
        pQueue.push(aux, 0) # ex aux => [(5, 5), 'nil', 'nil']
        mappedArray = [] # mappedArray => Array mapeado com pai e filhos
        while not pQueue.isEmpty():
            currentNode = pQueue.pop()
            if not currentNode in accessed:
                accessed.append(currentNode)
                print "Estou acessando o no:", currentNode[0]
                
                if problem.isGoalState(currentNode[0]):
                    print "Chegou ao Final"
                    print "No que encontrou o objetivo: ", accessed[-2]
                    pQueue.push(currentNode, currentNode[2])
                    break
                else: # caso nao seja o objetivo
                    for info in problem.getSuccessors(currentNode[0]): # pega os sucessores dele
                        tupleAux = None
                        if not info in accessed: # caso o sucessor analisado ainda nao foi acessado
                            print "Vou colocar na fila de prioridade: ", info
                            tupleAux = info
                            tupleAux += (currentNode, )
                            mappedArray.append(tupleAux) # armazena em um array o mapeamento pai -> filho
                            pQueue.push(info, info[2])
        accessed.pop(0)
        print "\nCaminho percorrido pelo algoritmo de busca: ", accessed
        print "\nArray mapeado cru: ", mappedArray

        moveTo = []    
        currentFather = [x for x in mappedArray if problem.isGoalState(x[0])] # pega as informacoes do no objetivo
        moveTo.append(currentFather[0][3][1]) # pega o passo do pai do no objetivo
        currentCoordinate = currentFather[0][3][0] # seta a coordenada atual de verificacao como sendo a coordenada do pai

        print "Realizando o mapeamento: "
        while True:
            # vai interar pelo mapeamento navegando pelo pai de cada filho ate chegar no problema inicial
            print "No atual: ", currentCoordinate
            currentFather = [x for x in mappedArray if x[0] == currentCoordinate]
            moveTo.append(currentFather[0][3][1])
            currentCoordinate = currentFather[0][3][0]
            print "Encontrado por: ", currentCoordinate
            # caso encontre o inicio do problema
            if currentCoordinate == problem.getStartState():
                moveTo.remove('nil') # remover lixo
                currentFather = [x for x in mappedArray if problem.isGoalState(x[0])] # procura o primeiro movimento realizado e insere no comeco do array  
                print currentFather
                moveTo.insert(0, currentFather[0][1])
                print "Custo atual para ", currentFather[0][1], problem.getCostOfActions(moveTo[::-1]) 
                break
        
        print "\nMovimentos necessarios para vencer: ", moveTo[::-1]
        print "Tamanho: ", len(moveTo), "\n"

        return moveTo[::-1]

    return andre()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    def andre():
        print "Start:", problem.getStartState()
        print "Is the start a goal?", problem.isGoalState(problem.getStartState())
        print "Start's successors:", problem.getSuccessors(problem.getStartState())
        print "heuristic", heuristic((1, 1), problem)
        from util import PriorityQueue
        pQueue = PriorityQueue()
        accessed = []
        # return [1]
        aux = []
        aux.append(problem.getStartState())
        aux.append('nil')
        aux.append('nil')
        pQueue.push(aux, 0) # ex aux => [(5, 5), 'nil', 'nil']
        mappedArray = [] # mappedArray => Array mapeado com pai e filhos
        while not pQueue.isEmpty():
            currentNode = pQueue.pop()
            if not currentNode in accessed:
                accessed.append(currentNode)
                print "Estou acessando o no:", currentNode[0]
                
                if problem.isGoalState(currentNode[0]):
                    print "Chegou ao Final"
                    print "No que encontrou o objetivo: ", accessed[-2]
                    pQueue.push(currentNode, heuristic(currentNode[0], problem))
                    break
                else: # caso nao seja o objetivo
                    for info in problem.getSuccessors(currentNode[0]): # pega os sucessores dele
                        tupleAux = None
                        if not info in accessed: # caso o sucessor analisado ainda nao foi acessado
                            print "Vou colocar na fila de prioridade: ", info
                            tupleAux = info
                            tupleAux += (currentNode, )
                            mappedArray.append(tupleAux) # armazena em um array o mapeamento pai -> filho
                            pQueue.push(info, heuristic(info[0], problem))
        accessed.pop(0)
        print "\nCaminho percorrido pelo algoritmo de busca: ", accessed
        print "\nArray mapeado cru: ", mappedArray

        moveTo = []

        currentFather = [x for x in mappedArray if problem.isGoalState(x[0])] # pega as informacoes do no objetivo
        moveTo.append(currentFather[0][3][1]) # pega o passo do pai do no objetivo
        currentCoordinate = currentFather[0][3][0] # seta a coordenada atual de verificacao como sendo a coordenada do pai
        print "Realizando o mapeamento: "
        while True:
        # vai interar pelo mapeamento navegando pelo pai de cada filho ate chegar no problema inicial
            print "No atual: ", currentCoordinate
            currentFather = [x for x in mappedArray if x[0] == currentCoordinate]
            moveTo.append(currentFather[0][3][1])
            currentCoordinate = currentFather[0][3][0]
            print "Encontrado por: ", currentCoordinate
            # caso encontre o inicio do problema
            if currentCoordinate == problem.getStartState():
                moveTo.remove('nil') # remover lixo
                currentFather = [x for x in mappedArray if problem.isGoalState(x[0])] # procura o primeiro movimento realizado e insere no comeco do array  
                print currentFather
                moveTo.insert(0, currentFather[0][1])
                print "Custo atual para ", currentFather[0][1], problem.getCostOfActions(moveTo[::-1]) 
                break
        
        print "\nMovimentos necessarios para vencer: ", moveTo[::-1]
        print "Tamanho: ", len(moveTo), "\n"

        return moveTo[::-1]
    return andre()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
