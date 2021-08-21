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
        teste = []
        teste2 = []

        stack = Stack()
        accessed = []

        aux = []
        aux.append(problem.getStartState())
        aux.append('nil')
        aux.append('nil')
        # aux => [(5, 5), 'nil', 'nil']
        stack.push(aux)
        before_goal = 0
        mappedArray = []
        # mappedArray => Array mapeado com pai e filhos
        while not stack.isEmpty():
            # armazena o no como acessado
            currentNode = stack.pop()
            # se esse no nao foi acessado
            if not currentNode in accessed:
                # seta ele como acessado
                accessed.append(currentNode)
                print "Estou acessando o no: ", currentNode[0]
                
                # caso seja o no objetivo
                if problem.isGoalState(currentNode[0]):
                    print "Chegou ao Final"
                    before_goal = accessed[-2]
                    print accessed[-2]
                    # input()
                    stack.push(currentNode)
                    break
                else:
                    # caso nao seja o objetivo pega os sucessores dele
                    for info in problem.getSuccessors(currentNode[0]):
                        # caso o sucessor analisado ainda nao foi acessado
                        tupleAux = None
                        if not info in accessed:
                            print "Vou colocar na pilha: ", info
                            tupleAux = info
                            tupleAux += (currentNode, )
                            # teste2.append(currentNode)
                            # teste2.append(info)
                            # teste = teste2
                            # mappedArray.append(teste)
                            mappedArray.append(tupleAux)
                            stack.push(info)
        
        accessed.pop(0)
        # for x in mappedArray:
        #     print x
        #     print "-----"

        # print "Start:", problem.getStartState()
        # currentFather = [x for x in mappedArray if x[0] == (35, 1)] #(35, 1)
        # print "PAPAPAPPAPAPAPAPAPPA"
        # for x in currentFather:
        #     print x
        #     print "-----"
        # print "PAPAPAPPAPAPAPAPAPPA"
        # input()
        print "\nCaminho percorrido pelo algoritmo de busca: ", accessed

        print "\nArray mapeado cru: ", mappedArray

        moveTo = []    
        
        # pega as informacoes do no objetivo
        print "No objetivo: ", (1, 1)
        currentFather = [x for x in mappedArray if x[0] == (1, 1)]
        moveTo.append(currentFather[0][3][1])
        currentCoordinate = currentFather[0][3][0]

        print "Realizando o mapeamento: "
        while True:
            print "No atual: ", currentCoordinate
            currentFather = [x for x in mappedArray if x[0] == currentCoordinate]
            moveTo.append(currentFather[0][3][1])
            currentCoordinate = currentFather[0][3][0]
            print "Encontrado por: ", currentCoordinate
            # caso encontre o inicio do problema
            if currentCoordinate == problem.getStartState():
                # procura o primeiro movimento realizado e insere no comeco do array  
                # currentFather = [x for x in mappedArray if x[0] == currentCoordinate]
                # moveTo.insert(0, currentFather[0][3][1])
                # # moveTo.insert(0, 'South') # Descomente isso para fazer o bigMaze rodar :)
                # print "----------------- Primeiro mapeamento", currentFather
                moveTo.remove('nil')
                # moveTo.insert(0, before_goal[1])
                print before_goal
                currentFather = [x for x in mappedArray if x[0] == (1, 1)]
                print currentFather
                print "PAPAPAPPAPAPAPAPAPPA"
                for x in currentFather:
                    moveTo.insert(0, x[1])
                    print "Custo atual para ", x[1], problem.getCostOfActions(moveTo) 
                    if problem.getCostOfActions(moveTo[::-1]) < 999999:
                        print "vou dar bom"
                        break
                    else:
                        moveTo.pop(0)
                    print x
                    print "-----"
                print "PAPAPAPPAPAPAPAPAPPA"
                # input()
                break
        
        # moveTo.pop()
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
        # aux => [(5, 5), 'nil', 'nil']
        queue.push(aux)
        before_goal = 0
        mappedArray = []

        # mappedArray => Array mapeado com pai e filhos
        while not queue.isEmpty():
            # armazena o no como acessado
            currentNode = queue.pop()
            # se esse no nao foi acessado
            if not currentNode in accessed:
                # seta ele como acessado
                accessed.append(currentNode)
                print "Estou acessando o no: ", currentNode[0]
                
                # caso seja o no objetivo
                if problem.isGoalState(currentNode[0]):
                    print "Chegou ao Final"
                    before_goal = accessed[-2]
                    print accessed[-2]
                    # input()
                    queue.push(currentNode)
                    break
                else:
                    # caso nao seja o objetivo pega os sucessores dele
                    for info in problem.getSuccessors(currentNode[0]):
                        # caso o sucessor analisado ainda nao foi acessado
                        tupleAux = None
                        if not info in accessed:
                            print "Vou colocar na fila: ", info
                            tupleAux = info
                            tupleAux += (currentNode, )
                            # print type(info)
                            # print info[0]
                            # break
                            mappedArray.append(tupleAux)
                            queue.push(info)
        
        accessed.pop(0)

        # print "\nCaminho percorrido pelo algoritmo de busca: ", accessed

        print "\nArray mapeado cru: ", mappedArray

        moveTo = []    
        
        # def findGoal():
        #     for x in mappedArray:
        #         if x[0].isGoal():
        #             return x
        # print mappedArray[0][0]
        # print mappedArray[0][0]
        # print mappedArray[0][0]
        # print type(mappedArray[0][0])
        # print type(mappedArray[0][0])
        # print type(mappedArray[0][0])
        # print type(mappedArray[0][0])

        if not type(mappedArray[0][0]) == type(tuple()):
            return [0]
            # currentFather = findGoal()
            # # print currentFather[0]
            # # print currentFather[1]
            # # print currentFather[2]
            # # print currentFather[3]
            # moveTo.append(currentFather[1])
            # print "PAI ATUAL !!!", currentFather[3]
            # print "COORDENADA ATUAL!@!!!", currentFather[0]
            # currentCoordinate = currentFather[0]
            # # print currentCoordinate
            # # print currentCoordinate
            # # print currentCoordinate
            # # print currentCoordinate
            # print "Realizando o mapeamento: "
            # while True:
            #     print "\n\n\n"
            #     print "No atual: ", currentCoordinate
            #     print "ANTES DE QUEBRAR INFORERNO DEBUGGG", mappedArray[0][0]
            #     print "\n\n\n\n\n\n"
            #     currentFather = [x for x in mappedArray if x[0] is currentCoordinate]
            #     print "currentFather", currentFather
            #     print "paipaipaipaipaia", currentFather
            #     print "paipaipaipaipaia", currentFather[0]
            #     print "paipaipaipaipaia", currentFather[0][1]
            #     moveTo.append(currentFather[0][1])

            #     currentCoordinate = currentFather[0][0]
            #     print "Encontrado por: ", currentCoordinate
            #     # caso encontre o inicio do problema

            #     print problem.getStartState()
            #     if currentCoordinate is problem.getStartState():
            #         moveTo.remove('nil')
            #         print before_goal
            #         currentFather = findGoal()
            #         print currentFather
            #         print "PAPAPAPPAPAPAPAPAPPA"
            #         for x in currentFather:
            #             moveTo.insert(0, x[0])
            #             print "Custo atual para ", x[1], problem.getCostOfActions(moveTo) 
            #             if problem.getCostOfActions(moveTo[::-1]) < 999999:
            #                 print "vou dar bom"
            #                 break
            #             else:
            #                 moveTo.pop(0)
            #             print x
            #             print "-----"
            #         print "PAPAPAPPAPAPAPAPAPPA"
            #         # input()
            #         break
            
            # # moveTo.pop()
            # print "\nMovimentos necessarios para vencer: ", moveTo[::-1]
            # print "Tamanho: ", len(moveTo), "\n"

            # return moveTo[::-1]
        else:
            currentFather = [x for x in mappedArray if x[0] == (1, 1)]
        # return
        # pega as informacoes do no objetivo
        moveTo.append(currentFather[0][3][1])
        currentCoordinate = currentFather[0][3][0]

        print "Realizando o mapeamento: "
        while True:
            print "No atual: ", currentCoordinate
            currentFather = [x for x in mappedArray if x[0] == currentCoordinate]
            moveTo.append(currentFather[0][3][1])
            currentCoordinate = currentFather[0][3][0]
            print "Encontrado por: ", currentCoordinate
            # caso encontre o inicio do problema

            if currentCoordinate == problem.getStartState():
                moveTo.remove('nil')
                print before_goal
                currentFather = [x for x in mappedArray if x[0] == (1, 1)]
                print currentFather
                print "PAPAPAPPAPAPAPAPAPPA"
                for x in currentFather:
                    moveTo.insert(0, x[1])
                    print "Custo atual para ", x[1], problem.getCostOfActions(moveTo) 
                    if problem.getCostOfActions(moveTo[::-1]) < 999999:
                        print "vou dar bom"
                        break
                    else:
                        moveTo.pop(0)
                    print x
                    print "-----"
                print "PAPAPAPPAPAPAPAPAPPA"
                # input()
                break
        
        # moveTo.pop()
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
    """
    def vini():
        acao = []
        acao.append('South')
        acao.append('South')
        acao.append('West')
        acao.append('West')
        acao.append('West')
        print "seila:", problem.getCostOfActions(acao)
        return acao


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
