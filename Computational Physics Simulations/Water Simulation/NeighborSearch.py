#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import random
import math

h = 2  # kernel range
N = 2000    # total number of particles
p = [[  ] for _ in range(N)]   # create empty list to store positions of N particles
neighbor = [[  ] for _ in range(N)]    # create empty list to store neighbors of N particles
side_length = 100    #side length of the map

# define function to calculate distance between particle i and j
def distance(i,j,p):
    return math.sqrt((p[i][0] - p[j][0])**2 + (p[i][1] - p[j][1])**2)

# assign position values for N particles
for i in range(N):
    p[i] = [random.randint(0,side_length - 1),random.randint(0,side_length - 1)]

# record start time for conventional method
start_time = time.time()

# conventional method
for i in range(N):
    for j in range(N):
        if distance(i,j,p) < h:
            neighbor[i].append(j)

# record end time for conventional method
end_time = time.time()


# now for grid-based method

# create empty list to store neighbors of N particles
neighbor_grid_based = [[  ] for _ in range(N)]

# number of grids should be n * n
n = 25

# create empty list to store particles in grids
grids = [[[  ] for _ in range(n)] for _ in range(n)]

# length of square is side length of map over number of grids
length_of_grid = side_length / n
    
    
# record start time for grid-based method
start_time2 = time.time()    

# now we put all particles into their belonging grid
for i in range(N):
    x_grid = int(p[i][0]/length_of_grid) 
    y_grid = int(p[i][1]/length_of_grid) 
    grids[x_grid][y_grid].append(i)


for i in range(N):
    # now we are trying to find all neighboring grids for particle i
    x_grid = int(p[i][0]/length_of_grid) 
    y_grid = int(p[i][1]/length_of_grid)
    if x_grid == 24:
        x_grid = 23
    if y_grid == 24:
        y_grid = 23    
    possible_neighbors = grids[x_grid][y_grid+1] + grids[x_grid][y_grid] + grids[x_grid][y_grid-1]
    possible_neighbors += grids[x_grid+1][y_grid+1] + grids[x_grid+1][y_grid] + grids[x_grid+1][y_grid-1] 
    possible_neighbors += grids[x_grid-1][y_grid+1] + grids[x_grid-1][y_grid] + grids[x_grid-1][y_grid-1] 
    # now we are trying to find all neighboring grids for particle i
    
    
    # put your codes here    
    # your codes should determine neighboring particles in possible_neighbors and store them into list neighbor_grid_based
    # put your codes here

# record end time for grid-based method
end_time2 = time.time()

print('now we check the correctness of grid-based method by randomly choosing neighbors of particle 3 4 and 90')
print('\nfor conventional method, particle 3 has neighbors:',neighbor[3],'particle 4 has neighbors:',neighbor[4],'particle 90 has neighbors:',neighbor[90])
print('for grid-based method, particle 3 has neighbors:',neighbor_grid_based[3],'particle 4 has neighbors:',neighbor_grid_based[4],'particle 90 has neighbors:',neighbor_grid_based[90])
print('\nsearch time for conventional method:',end_time - start_time,'s') 
print('search time for Grid-based method:',end_time2 - start_time2,'s')
print('it is',int((end_time - start_time)/(end_time2 - start_time2)),'times faster')

