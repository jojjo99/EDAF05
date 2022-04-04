"""

Wordladder solution breadth first search (BFS)

"""
import sys
# Prev is a list of nodes pointing to current
class Node:
    def __init__(self, word):
        self.word = word
        self.visited = False
        self.connections = list()
        self.came_from = None
"""
Method create list of nodes and make connections.
"""
def main():
    create_nodes()

def create_nodes():
    inputs = list(sys.stdin.read().replace('\n', ' ').split(' '))
    nbrWords = int(inputs[0])
    nbrQueries = int(inputs[1])
    node_list = list()
    wordToNodeMap = dict()

    for i in range(2,nbrWords+2):
        word = inputs[i]
        node = Node(word)
        node_list.append(node)
        wordToNodeMap[word]=node
    node_list=create_node_connections(node_list)

    start_index = 2+nbrWords
    for i in range(0,nbrQueries):
        start_word = inputs[start_index+2*i]
        stop_word = inputs[start_index+1+2*i]
        start_node = wordToNodeMap[start_word]
        print(BFS(start_node,stop_word))
        restoreNodes(node_list)



"""
Method creates connection between nodes
"""
def create_node_connections(node_list):
    # Loop through list with nodes
    for i in range(len(node_list)):
        current_node = node_list[i]
        current_word = current_node.word
        current_chars = list(current_word)
        # Compare current word with all other nodes
        for j in range(len(node_list)):
            connected = None
            if i!=j:
                compared_node = node_list[j]
                compared_word = compared_node.word
                compared_chars = list(compared_word)
                for k in range(4):
                    letter=current_chars[len(current_chars)-k-1]
                    if letter in compared_chars:
                        index=compared_chars.index(letter) # Remove first occurence
                        compared_chars.pop(index)
                    else: # If not present, they are not connected
                        connected = False
                if connected is not False:
                    connected=True
                    current_node.connections.append(compared_node)
    return node_list

"""
Breadth first search.
1) Define starting and target node
2) 
"""

def BFS(node,word):
    # Keep track of how far away current node is
    steps=0
    layers = list()
    layers.insert(steps,list())

    node.visited = True
    layers[steps].append(node)

    if node.word == word: #If node.word is word -> return 0
        return steps
    while True: #Create a set with every step, if node.word == word, return step
        steps+=1
        layers.insert(steps,list())
        for n in layers[steps-1]: #for every node in prev layer-> add their neighbours to this layer
            for neigbour in n.connections:
                if neigbour.word == word:
                    return steps
                if not neigbour.visited:
                    layers[steps].append(neigbour)
                    neigbour.visited =True
        if not layers[steps]:
            return "Impossible"

def restoreNodes(nodeList):
    for node in nodeList:
        node.visited = False




        

main()
#node_list=[Node("where"), Node("there"), Node("shere")]
#create_node_connections(node_list)



