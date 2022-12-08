from random import choices, randint
from numpy.random import rand

transac=[]
Genome=[]
global pop
fit=[]

def genome(length):
    result = choices([0, 1], k=length)
    while all(element == 0 for element in result):
        result = choices([0, 1], k=length)
    return result

def individualfitness (genome):
    value=0
    for i,val in enumerate(transac):
        if genome[i]==1:
            value+=transac[i]
    if all(element == 0 for element in genome):
        value=10005
        return value
    return abs(value)

def fitness(population):
    for i in range(len(population)):
        fit.append(individualfitness(population[i]))
    return fit

def select(fit): #taking fit list
    min_index=fit.index(min(fit))
    fit[min_index]=100005
    return pop[min_index]

def crossover(p1, p2):
    c1, c2 = p1.copy(), p2.copy()
    pt = randint(1, len(p1)-2)
    c1 = p1[:pt] + p2[pt:]
    c2 = p2[:pt] + p1[pt:]
    return [c1, c2]

def mutation(bitstring, r_mut):
    for i in range(len(bitstring)):
        if rand() < r_mut:
            bitstring[i] = 1 - bitstring[i]

def population(genome_length):
    global pop
    pop= [genome(genome_length) for _ in range(6)]

def check_goal(children):
    for i in children:
        if individualfitness(i)==0:
            for j in i:
                print(j,end='')
            return True
    return False


def GA():
    n=int(input("Enter number of daily transactions "))
    for i in range(n):
        x,y=[v for v in input().split()]
        if x=='l' or x=='L':
            transac.append(-abs(int(y)))
        else:
            transac.append(int(y))
    r_mut = 1.0 / float(n)
    population(n)
    for gen in range(10000):
        global pop
        fitness(pop)
        selected = [select(fit) for _ in range(4)]
        # create the next generation
        children = list()
        for i in range(0, 4, 2):
            # get selected parents in pairs
            p1, p2 = selected[i], selected[i + 1]
            # crossover and mutation
            for c in crossover(p1, p2):
                # mutation
                mutation(c, r_mut)
                # store for next generation
                children.append(c)
        # replace population
        if check_goal(children)==True:
            return
        fit.clear()
        pop = children
    print("-1")

GA()