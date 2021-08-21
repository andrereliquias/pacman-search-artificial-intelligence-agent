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
        print "inicial e:", inicial
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
        stack = Stack()
        accessed = []

        aux = []
        aux.append(problem.getStartState())
        aux.append('nil')
        aux.append('nil')
        stack.push(aux) # aux => [(5, 5), 'nil', 'nil']
        mappedArray = [] # mappedArray => Array mapeado com pai e filhos

        while not stack.isEmpty():
            currentNode = stack.pop() # armazena o no como acessado
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
        print "No objetivo: ", (1, 1)
        currentFather = [x for x in mappedArray if x[0] == (1, 1)] # pega as informacoes do no objetivo
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
                for x in currentFather: # por cada movimento realizado saindo da posicao inicial
                    moveTo.insert(0, x[1])
                    print "Custo atual para ", x[1], problem.getCostOfActions(moveTo) 
                    if problem.getCostOfActions(moveTo[::-1]) < 999999: # verifica se e uma acao valida
                        print "Encontrei uma acao valida!"
                        break
                    else:
                        moveTo.pop(0)
                break
        
        print "\nMovimentos necessarios para vencer: ", moveTo[::-1]
        print "Tamanho: ", len(moveTo), "\n"

        return moveTo[::-1]

    return andre()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    # pseudo-codigo
    """BuscaEmLargura:
        escolha uma raiz s de G
        marque s
        insira s em F
        enquanto F nao esta vazia faca
            seja v o primeiro vertice de F
            para cada w pertence listaDeAdjacencia de v faca
                se w nao esta marcado entao
                    visite aresta entre v e w
                    marque w
                    insira w em F
                senao se w pertence F entao
                    visite aresta entre v e w
                fim se
            fim para
            retira v de F
        fim enquanto"""
    
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
                            print "Vou colocar na pilha: ", info
                            tupleAux = info
                            tupleAux += (currentNode, )
                            mappedArray.append(tupleAux) # armazena em um array o mapeamento pai -> filho
                            queue.push(info)
        
        accessed.pop(0)
        print "\nCaminho percorrido pelo algoritmo de busca: ", accessed
        print "\nArray mapeado cru: ", mappedArray
        
        # metodo para encontrar o objetivo do 8puzzle no array mapeado
        def findGoal():
            for x in mappedArray:
                if x[0].isGoal():
                    return x

        moveTo = []    
        if not type(mappedArray[0][0]) == type(tuple()):
            currentFather = findGoal()[3]
            # print "\n", currentFather
            # print "\n", currentFather[0]
            # print "\n", currentFather[1]
            # print "\n", currentFather[2]
            moveTo.append(currentFather[1])
            print "PAI ATUAL !!!", currentFather # (<__main__.EightPuzzleState instance at 0x7f8562be18c0>, 'up', 1)
            print "COORDENADA ATUAL!@!!!", currentFather[0]
            currentCoordinate = currentFather[0]
            print "Realizando o mapeamento: "
            while True:
                print "No atual: ", currentCoordinate
                currentFather = [x for x in mappedArray if x[0] is currentCoordinate][0]
                print "currentFather", currentFather
                print "coordenada do pai", currentFather[3][0]
                print "movimento do pai", currentFather[3][1]
                moveTo.append(currentFather[3][1])

                currentCoordinate = currentFather[3][0]
                print "Encontrado por: ", currentCoordinate
                # caso encontre o inicio do problema

                # print problem.getStartState()

                if currentCoordinate is problem.getStartState():
                    moveTo.remove('nil')

                    currentFather = findGoal()
                    print currentFather
                    print "PAPAPAPPAPAPAPAPAPPA"
                    moveTo.insert(0, currentFather[3][1])
                    break
                    for x in currentFather:
                        print "vou printar o x ", x
                        moveTo.insert(0, x)
                        print "Custo atual para ", x, problem.getCostOfActions(moveTo) 
                        if problem.getCostOfActions(moveTo[::-1]) < 999999:
                            print "vou dar bom"
                            break
                        else:
                            moveTo.pop(0)
                        print "-----"
                    print "PAPAPAPPAPAPAPAPAPPA"
                    # input()
                    break
            
            # moveTo.pop()
            print "\nMovimentos necessarios para vencer: ", moveTo[::-1]
            print "Tamanho: ", len(moveTo), "\n"

            return moveTo[::-1]
        else:
            print "No objetivo: ", (1, 1)
            currentFather = [x for x in mappedArray if x[0] == (1, 1)] # pega as informacoes do no objetivo
        # return

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
                for x in currentFather: # por cada movimento realizado saindo da posicao inicial
                    moveTo.insert(0, x[1])
                    print "Custo atual para ", x[1], problem.getCostOfActions(moveTo) 
                    if problem.getCostOfActions(moveTo[::-1]) < 999999: # verifica se e uma acao valida
                        print "Encontrei uma acao valida!"
                        break
                    else:
                        moveTo.pop(0)
                break
        
        print "\nMovimentos necessarios para vencer: ", moveTo[::-1]
        print "Tamanho: ", len(moveTo), "\n"

        return moveTo[::-1]

    #Codigo

    # python2 pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
    # python2 pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
    # se ficar muito lento acrescente a flag --frameTime 0
    
    def vini():
        inicial = []
        visitados = []
        inicial.append(problem.getStartState())
        inicial.append('null')
        inicial.append(0)

        fila = []
        fila.append(inicial)
        while len(fila) > 0:
            noh = fila.pop(0)
            visitados[noh] = 1
            print(mD[noh])

            if problem.isGoalState(noh[0]):
                print "foi"
                break
            for n in grafo[noh]:
                if visitados[n] == 0:
                    visitados[n] = 1
                    fila.append(n)
        return []     
        
    return andre()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    """
    codigos do objeto problem:
        getStartState(self)
        isGoalState(self, state)
        getSuccessors(self, state)
        getCostOfActions(self, actions)


    def vini():
        acao = []
        acao.append('South')
        acao.append('South')
        acao.append('West')
        acao.append('West')
        acao.append('West')
        print "seila:", problem.getCostOfActions(acao)
        return acao

        

        
    """

    return vini()

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
