#!/bin/python3

#import math
#import os
#import random
#import re
#import sys



#
# Complete the 'gridGame' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY grid
#  2. INTEGER k
#  3. STRING_ARRAY rules
#
def check_upper_left(grid, i, j):
    if(i>0) and (j>0):
        if grid[i-1][j-1]==1:
            return 1
        else:
            return 0 
    else:
        return 0
    
def check_upper(grid, i, j):
    if(i>0):
        if grid[i-1][j]==1:
            return 1
        else:
            return 0     
    else:
        return 0
    
def check_upper_right(grid, i, j):
    if(i>0) and (j<len(grid[0])-1):
        if grid[i-1][j+1]==1:
            return 1
        else:
            return 0 
    else:
        return 0
    
def check_left(grid, i, j):
    if (j>0):
        if grid[i][j-1]==1:
            return 1
        else:
            return 0 
    else:
        return 0
    
def check_right(grid, i, j):
    if (j<len(grid[0])-1):
        if grid[i][j+1]==1:
            return 1
        else:
            return 0
    else:
        return 0
    
def check_down_left(grid, i, j):
    if (i<len(grid)-1) and (j>0):
        if grid[i+1][j-1]==1:
            return 1
        else:
            return 0
    else:
        return 0
    
def check_down(grid, i, j):
    if (i<len(grid)-1) :
        if grid[i+1][j]==1:
            return 1
        else:
            return 0
    else:
        return 0

def check_down_right(grid, i, j):    
    if (i<len(grid)-1) and (j<len(grid[0])-1):
        if grid[i+1][j+1]==1:
            return 1
        else:
            return 0
    else:
        return 0

def check_neigbours(grid):
    tab=[[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    al_neigb=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            al_neigb+=check_upper_left(grid,i,j)
            al_neigb+=check_upper(grid,i,j)
            al_neigb+=check_upper_right(grid,i,j)
            al_neigb+=check_left(grid,i,j)
            al_neigb+=check_right(grid,i,j)
            al_neigb+=check_down_left(grid,i,j)
            al_neigb+=check_down_right(grid,i,j)
            al_neigb+=check_down(grid,i,j)
            tab[i][j]=al_neigb
            al_neigb=0
    return tab            

def gridGame(grid, k, rules):
    for moves in range(k):  
        tab=check_neigbours(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if rules[tab[i][j]]=='dead':
                    grid[i][j]=0
                else:
                    grid[i][j]=1
    return grid                

if __name__ == '__main__':

    grid=[[0,1,0,1,1,1],[0,0,1,0,1,1]]
    k=2000
    rules=['dead','alive','dead','dead','dead','dead','dead','dead','dead']
    for line in gridGame(grid,k,rules):
        print(*line)
        
