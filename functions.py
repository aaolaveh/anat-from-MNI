#Original matlab code from Xu Cui ( https://alivelearn.net/?p=1456)
# author: Astrid Olave 

import sys
import scipy.io
import warnings
import numpy as np

#----------------------------  find_structure ---------------------------
#Converts MNI coordinate to a description of brain structure in aal
#Input: - mni : the coordinates (MNI) of some points, in mm.  It is Mx3 matrix
#        where each row is the coordinate for one point.
#        -DB (optional): The database. If is omit, make sure TDdatabase.mat is in the 
#        same folder
#Output: -one_line_result: A list of M elements, each describing each point.
#        -table_result:  A  MxN matrix being N the size of the database (DB)
#

def find_structure(mni,DB=None):
    #Copy from cuixuFindStructure.m
    
    #Vectorize this functions
    vstr=np.vectorize(str)
    vround = np.vectorize(my_round)
    vint=np.vectorize(int)
    
    if DB == None:
        mat=scipy.io.loadmat('TDdatabase.mat')  
            
    mni=np.array(mni)        
    M=len(mni)
    
    #round coordinates
    mni=vround(mni/2)*2 
    
    T=np.array([[2 ,0 ,0 ,-92],[0,2,0,-128],
                    [0,0,2,-74],[0,0,0,1]])
    
    index=mni2cor(mni,T)
    
    #-1 by python indexation
    index=vint(index) - 1 
    
    N=np.shape(mat['DB'])[1]
    table_result=np.zeros((M,N))
    table_result=table_result.tolist() #instead of [i,j] use [i][j]
    
    one_line_result=[""] * M
    
    for i in range(M):
        for j in range(N):
            #mat['DB'][0,j][0,0][0] is the j-th 3D-matrix 
            graylevel=mat['DB'][0,j][0,0][0][index[i,0],index[i,1],index[i,2]] 
            if graylevel == 0:
                 label = 'undefined'
            else:
                if j < (N-1):
                    tmp = ''
                else:
                    tmp =' (aal)' 
                    
                #mat['DB'][0,j][0,0][1]  is the list with regions
                label=mat['DB'][0,j][0,0][1][0,(graylevel-1)][0] + tmp
            
            table_result[i][j]=label
            one_line_result[i] = one_line_result[i] + ' // ' + label
    return(one_line_result,table_result)
    
#---------------------------- mni2cor --------------------------------
# convert mni coordinate to matrix coordinate
#Input: - mni : the coordinates (MNI) of some points, in mm.  It is Mx3 matrix
#        where each row is the coordinate for one point.
#        -T (optional): transform matrix coordinate is the returned coordinate in matrix.
#Output: -coords : Coordinate matrix
#
def mni2cor(mni,T=np.array([[-4 ,0 ,0 ,84],[0,4,0,-116],
                    [0,0,4,-56],[0,0,0,1]])):
    
    mni=np.array(mni)
    
    if len(np.shape(mni))==1:
        mni=mni.reshape((1, len(mni)))
    
    if np.shape(mni)[1] != 3:
        warnings.warn('are not 3-length coordinates')
        return(np.array([]))
        
    a=np.hstack((mni,np.ones((np.shape(mni)[0],1))))
    b=np.transpose(np.linalg.inv(T))
    coords=a.dot(b)
    coords=coords[:,0:3]
        
    vround = np.vectorize(my_round)
    coords = vround(coords)
    return(coords)
    
#-------------------------- my_round ------------------------------
# round function to integer to match with round in MATLAB
# Input: -x: value to be rounded
# Output: rounded x
def my_round(x):
    r=x-np.floor(x)
    if(r == 0.5):
        if x<0: return(x-0.5)
        else: return(x+0.5)
    else:
        return(round(x))
    
  
 
