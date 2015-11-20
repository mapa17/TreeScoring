# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys

#SCORE = 0
CNT = 0
LEFT = 1
RIGHT = 2

def main(argv):
    #N = int(input())
    if len(argv) > 1:
        scores = [ int(x) for x in argv[1:]]
    else:
        scores = [4, 2, 5, 5, 6, 1 , 4]
        scores = [4, 2, 5, 5, 6, 1, 4, 0]
    
    res = gatherScores(scores)
    print(res)
    
def  gatherScores(scores):
    ser = ''
    try:
        root = scores.pop(0)
        S = {}
        S[root] = (1, None, None)
        for element in scores:
            #print('Processing %d' % element)
            S = addScore(S, root, element)
        
        print('Finished!')
        print(S)
        
        treeStr = printTree(S, root)
        print('Tree format:', treeStr)
        #print(S)
    except Exception as e:
        print(e)
    
    return ser
    
def addScore(S, root, score):
    if score in S:
        S[score] = (S[score][CNT] + 1, S[score][LEFT], S[score][RIGHT])
    else:
        S = addChild(S, root, score)
    
    return S

def addChild(S, element, score):
    #print('Try to add %d, to %d' % (score, element) )
    if element > score:
        if S[element][LEFT] is None:
            #print('New Left')
            S[element] = (S[element][CNT], score, S[element][RIGHT])
            S[score] = (1, None, None)
            return S
        else:
            #print('Go Left')
            return addChild(S, S[element][LEFT], score)    
    elif element < score:
        if S[element][RIGHT] is None:
            #print('New Right')
            S[element] = (S[element][CNT], S[element][LEFT], score)
            S[score] = (1, None, None)
            return S
        else:
            #print('Go right')
            return addChild(S, S[element][RIGHT], score)
    else:
        S[score] = (S[score][CNT] + 1, S[score][LEFT], S[score][RIGHT])
        return S

def printTree(S, element):
    center = format('%d:%d' % (element, S[element][CNT]))
    
    if (S[element][LEFT] is None) and (S[element][RIGHT] is None):
        return center
    
    if S[element][LEFT] is None:
        left = ','
    else:
        left = printTree(S, S[element][LEFT]) + ','
        
    if S[element][RIGHT] is None:
        right = ','
    else:
        right = ',' + printTree(S, S[element][RIGHT])
        
    return left + center + right
            
if __name__ == "__main__":
    main(sys.argv)