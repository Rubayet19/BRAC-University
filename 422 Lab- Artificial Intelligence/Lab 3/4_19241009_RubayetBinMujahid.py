import random
import math

infinity = math.inf
alpha = -infinity
beta = infinity
PrunedCount = 0
inputDepth = 0

def alphaBetaPrune(position, depth, alpha, beta, maximizingPlayer, leaves):
   global PrunedCount
   if depth == inputDepth:
       PrunedCount += 1
       return leaves[position]

   if maximizingPlayer:
       maxEval = -infinity
       for i in range(0, branches):
           eval = alphaBetaPrune(position * branches + i, depth + 1, alpha, beta, False, leaves)
           maxEval = max(maxEval, eval)
           alpha = max(alpha, maxEval)
           if beta <= alpha:
               break
       return maxEval

   else:
       minEval = infinity
       for i in range(0, branches):
           eval = alphaBetaPrune(position * branches + i, depth + 1, alpha, beta, True, leaves)
           minEval = min(beta, eval)
           beta = min(beta, minEval)
           if beta <= alpha:
               break
       return minEval


if __name__ == '__main__':
   n = input()
   digits = [int(x) for x in str(n)]
   turns = digits[0]
   branches = digits[2]
   rangeofvalues = input().split()
   rangeofvalues = list(map(int, rangeofvalues))
   lifeline = int(str(digits[-1]) + str(digits[-2]))

   inputDepth = 2 * turns
   totalLeafNodes = branches ** inputDepth


   randomGenleaf = random.sample(range(rangeofvalues[0], rangeofvalues[1]), totalLeafNodes)
   maximumAmount = alphaBetaPrune(0, 0, alpha, beta, True, randomGenleaf)

   print('Depth and Branches ratio is {}:{}'.format(inputDepth,branches))
   print("Terminal States (leaf node values) are:",*randomGenleaf, sep = ",")
   print("Left life(HP) of the defender after maximum damage caused by the attacker is", lifeline-maximumAmount)
   print("After Alpha-Beta Pruning Leaf Node Comparisons", PrunedCount)
