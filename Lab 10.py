# -*- coding: utf-8 -*-
"""Lab 10

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e2pGRP3sxDai_AjxTD0zq91S3WbRJUGI

#**Lab 10 - Networks and eigenvector centrality**

Enter your code in the spaces provided. Do not change any of the variable names or function names that are already provided for you. In places where we specify the name of the return value, make sure that your code produces the a value with the correct name.
"""

# Do not edit this cell.

LabID="Lab10"

try:
  from graderHelp import ISGRADEPLOT
except ImportError:
  ISGRADEPLOT = True

"""**Enter your name, section number, and BYU NetID**"""

# Enter your first and last names in between the quotation marks.

first_name="Dallin"

last_name="Henderson"

# Enter your Math 215 section number in between the quotation marks. 

section_number="1"  

# Enter your BYU NetID in between the quotation marks.  NOT YOUR BYU ID NUMBER! 

BYUNetID="henderda"

"""**Import and visualize the data**

The simplest way to load the data into Colab is to first download it as a .csv file to your local computer by clicking the link

https://drive.google.com/uc?export=download&id=1J8IirxuOT0vLp2jl-yIitFCqVX71XzsN

This will allow you to download the data as a .csv file.  In the top left corner of this screen you should see a little file folder icon.   Selecting it opens a new window to the left of the notebook with three tabs: "Upload", "Refresh", and "Mount Drive". Select "Upload".  This should bring up a window that allows you to select the file "Lab10webpagedata.csv" from your local machine, which will upload the file to your notebook.  You will need to do this again if you decide to close your notebook and reopen it at a later time.

Once you've uploaded your file, convert it to a NumPy array called "webpage_data" by executing the following cell.
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Lab10webpagedata.csv')
webpagedata=df.values
webpage_data=np.array(webpagedata)

"""Execute the following cell to visualize the network."""

import networkx as nx
edges=[(i[0],i[1]) for i in webpagedata]
G=nx.from_edgelist(edges)
nx.draw(G,node_size=75)

"""**Problem 1**"""

def adj_matrix(n,edge_list): 
  adj=np.zeros((n,n))
  for i in range(0,edge_list.shape[0]):
    adj[edge_list[i][0]][edge_list[i][1]] += 1
  return adj

# Use E1 to test your function.

E1=np.array([[0,1],[1,4],[0,2],[0,4],[1,3],[2,0],[2,4],[3,4],[3,2],[3,2]])
adj_matrix(5,E1)

"""**Problem 2**"""

def degree_cent(n,edge_list):
  new=adj_matrix(n,edge_list)
  deg=np.zeros(n)
  for i in range(0,n):
    deg[i]=np.sum(new[:,i])
  return deg

degree_cent(5,E1)

"""**Problem 3**"""

# Save the value you obtain in Problem 3 as the variable top_indegree.

top_indegree=np.flip(degree_cent(webpage_data.shape[0],webpage_data).argsort(),0)[0] 
top_indegree

"""**Problem 4**"""

def stoch_mat(A):
  t=np.transpose(A)
  new=np.copy(t)
  sums=np.zeros(t.shape[1])
  for i in range(0,t.shape[1]):
    sums[i]=np.sum(t[:,i])
  for i in range(0,t.shape[1]): # i shifts right
    for j in range(0,t.shape[0]): # j shfifts down
      new[j][i]= t[j][i] / sums[i]
  return new

# Use A2 to test your function. 

A2= np.array([[0.,1.,0.,0.,0.,0.,0.,0.],
 [0.,0.,1.,0.,0.,0.,0.,0.],
 [1.,0.,0.,1.,0.,1.,1.,0.],
 [0.,0.,0.,0.,1.,1.,0.,0.],
 [1.,0.,1.,0.,0.,0.,0.,0.],
 [1.,0.,0.,0.,0.,0.,0.,0.],
 [0.,0.,0.,0.,0.,1.,0.,1.],
 [1.,0.,0.,0.,0.,0.,0.,0.]])
stoch_mat(A2)

"""**Problem 5**"""

def stoch_eig(P,k):
  x_0=np.zeros(P.shape[0])
  x_0[:]=1.0 / P.shape[0]
  for i in range(0,k):
    x_0=P@x_0
  return x_0

P=np.array([[0,0,0.25,0,0.5,1.,0,1.],
           [1,0,0,0,0,0,0,0],
           [0,1,0,0,0.5,0,0,0],
           [0,0,0.25,0,0,0,0,0],
           [0,0,0,0.5,0,0,0,0],
           [0,0,0.25,0.5,0,0,0.5,0],
           [0,0,0.25,0,0,0,0,0],
           [0,0,0,0,0,0,0.5,0]])

stoch_eig(P,100)

"""**Problem 6**"""

def PageRank_cent(n,edge_list,k):
  adj=adj_matrix(n,edge_list)
  P=stoch_mat(adj)
  x=stoch_eig(P,k)
  return x

E2=np.array([[0,1],[1,2],[2,0],[2,3],[2,5],[2,6],[3,5],[3,4],[4,2],[4,0],[5,0],[6,5],[6,7],[7,0]])

PageRank_cent(8,E2,100)

"""**Problem 7**"""

# Save the value you obtain in Problem 7 as the variable top_PageRank.

top_PageRank=np.flip(PageRank_cent(499,webpage_data,100).argsort(),0)[0] 
top_PageRank

"""**STOP!  BEFORE YOU SUBMIT THIS LAB:**  Go to the "Runtime" menu at the top of this page, and select "Restart and run all".  If any of the cells produce error messages, you will either need to fix the error(s) or delete the code that is causing the error(s).  Then use "Restart and run all" again to see if there are any new errors.  Repeat this until no new error messages show up.

**You are not ready to submit until you are able to select "Restart and run all" without any new error messages showing up.  Your code will not be able to be graded if there are any error messages.**

To submit your lab for grading you must first download it to your compute as .py file. In the "File" menu select "Download .py". The resulting file can then be uploaded to http://www.math.byu.edu:30000 for grading.
"""