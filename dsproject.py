import string
import random
import time
from collections import *
from final import *
"""def load_dictionary(path = '/usr/share/dict/words'):
  dictionary = set()
  with open('/usr/share/dict/words', 'r') as f:
    for line in f:
      dictionary.add(line.strip().lower())
  return dictionary"""


def makeGraph(dictionary): #takes 
 graph=defaultdict(list) #used defaultdict so if any key that is called does not have any value then it returns a type list
 alphabets="abcdefghijklmnopqrstuvwxyz" #assigns lower case alphabets to alphabets
 for word in dictionary: #deleting, followed by replacement and finally adding (this can be modified to whatever order)
  for i in range(len(word)):
   #delete 1 character from the front of the word
   delete=word[:i]+word[i+1:] #performs concatenation
   if delete in dictionary:
    graph[word].append(delete) #appending the word to the value list of the key
   #change 1 character
   for char in alphabets:
    rep=word[:i]+char+word[i+1:]
    if rep in dictionary and rep!=word:
     graph[word].append(rep)
     #add 1 character in each position
 for i in range(len(word)+1):
  for char in alphabets:
   add=word[:i]+char+word[i:] 
   if add in dictionary:
    graph[word].append(add)
 return graph



def bfs(graph, start, end):
 paths=deque([ [start] ]) #used deque since it is convenienient to add and delete from both ends                                                    
 visited=set() #set to maintain all the words visited so we don't revisit them
 #Breadth First Search
 while len(paths)!=0: #it breaks out of the while loop when there are no elements in paths
  currPath=paths.popleft() #gets the first path in the deque
  #print currPath (using pop would return the longest path instead of shortest)
  currWord=currPath[-1] #gets the last node in the path 
  if currWord==end:
   return currPath
  elif currWord in visited: #already visited this word 
   continue
  visited.add(currWord) 
  transforms=graph[currWord]
  for word in transforms:
   if(word==end):
    return currPath+[word]
   if(word not in currPath):
    paths.append(currPath +[word])
  #if transformation not possible
 return

def shortestDist(graph,sw,ew):
 if(bfs(graph,sw,ew)):
  edit=0
  sol=bfs(graph,sw,ew)
  for w in sol:
   edit=edit+1
  return edit
 return 0




def randGame(graph,dct,en,ed,soln):
 trans=input('Enter transform word starting from the start word or to view solution enter \'s\': ')
 lst=[]
 for word in soln:
  while(trans not in dct and trans!='s'):
   trans=input('Invalid word! Enter valid transform word:')
  while(trans!=word and trans!='s'):
   trans=input('Keep trying! If you want to view the solution enter \'s\' else if you want to view a word enter\'w\':\n')
   if(trans=='s'):
    print(soln)
    return
   if(trans=='w'):
    print('This is the next word: ',word)
    trans=word
    #lst.append(trans)
    break
  if(word == trans and word!=en):
   print('Good job!')
   lst.append(trans)
  if(word==en):
   print('You made it!!!')
   lst.append(trans)
   print(lst)
   return
  if(trans=='s'):
   print(soln)
   return

#dcty=load_dictionary();
print('Hey there! Constructing the graph...')
t0 = time.time()
graph1=makeGraph(dcty)
t1 = time.time()
total = t1-t0
print('Time taken to contruct graph (in seconds):',total)
print('~~~~~~~~~~~~~~~~~~~~~~~WELCOME~~~~~~~~~~~~~~~~~~~~~~~~')
x=input('\nTo check word transformation enter \'c\', to play the game enter \'g\' or to end enter \'e\':\n')
while(x=='c' or x=='g'):
 if(x=='c'):
  sw=input('Enter start word:')
  while sw not in dcty:
   print('Enter valid start word')
   sw=input('Enter start word:')
  ew=input('Enter end word:')
  while ew not in dcty:
   print('Enter valid end word')
   ew=input('Enter end word:')
  print('Solution:')
  print(bfs(graph1,sw,ew))
 if(x=='g'):
  lev=input('Enter \'ez\' for level 1, \'med\' for level 2 or \'dif\' for level 3: ')
  print('Finding two words which can be transformed might take a while...')
  t2=time.time()
  flag=0 
  while(flag==0):
   dt=list(dcty)
   s1=random.choice(dt)
   e1=random.choice(dt)
   edis=shortestDist(graph1,s1,e1)
   if(lev=='ez'):
    if(edis>=3 and edis<=5):
     flag=1
     t3=time.time()
   if(lev=='med'):
    if(edis>=6 and edis<=7):
     flag=1
     t3=time.time()
   if(lev=='dif'):
    if(edis>=8):
     flag=1
     t3=time.time()
  tot=t3-t2
  print('Time taken to find the words (in seconds): ',tot)
  print('Here is your start word: ',s1)
  print('Here is your end word: ',e1)
  soln=bfs(graph1,s1,e1)
  print('Shortest distance: ',edis)
  randGame(graph1,dcty,e1,edis,soln)
 x=input('To check word transformation enter \'c\', to play the game enter \'g\' or to end enter \'e\':\n')
print('THE END!')





 


