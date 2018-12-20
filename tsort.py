from sys import argv
from stack_array import *

class VertexValue:
    def __init__(self): 
        self.in_deg = 0
        self.adj_list = []
        
    def get_inDegree(self):
        return self.in_deg
        
    def get_adjList(self):
        return self.adj_list
    
    def set_list(self, value):
        self.adj_list.append(value)
        
    def add_degree(self):
        self.in_deg += 1
        
    def __str__(self):
        return '(' + str(self.get_inDegree()) + ',' + str(self.get_adjList()) + ')'

def tsort(vertices):
    '''
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * identically to the Unix utility {@code tsort}.  That is, one vertex per
    * line in topologically sorted order.
    *
    * Raises a ValueError if:
    *   - vertices is emtpy with the message "input contains no edges"
    *   - vertices has an odd number of vertices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message 
    *     "input contains a cycle"'''
    if len(vertices) == 0:
        raise ValueError('input contains no edges')
    elif len(vertices) % 2 != 0:
        raise ValueError('input contains an odd number of tokens')
    # elif: #the graph is cyclical
        # raise ValueError('input contains a cylce')
    
    vertex_dict = {}
    key_list = {}
        
    for v in range(1, len(vertices), 2):
        # print(v)
        right_key = str(vertices[v])
        left_key = str(vertices[v-1])

        if not left_key in key_list:
            key_list[left_key] = 1
            vertex_dict[left_key] = VertexValue()
            
        if not right_key in key_list:
            key_list[right_key] = 1
            vertex_dict[right_key] = VertexValue()
        
        # print('left key', left_key)
        # print('right key', right_key)
        
        vertex_dict[left_key].set_list(right_key)
        vertex_dict[right_key].add_degree()
    
    
    # for (key, value) in vertex_dict.items():
        # print(key, value)
        
    stack = Stack(len(key_list))
    count = len(vertex_dict)
    
    for key in key_list.keys(): 
        if vertex_dict[key].get_inDegree() == 0:
            stack.push(key)
            count -= 1
            
    
    outstring = ''        
    while not stack.is_empty():
        key = stack.peek()
        
        outstring += str(stack.pop()) + '\n'
        for v in vertex_dict[key].get_adjList():
            vertex_dict[v].in_deg -= 1
            if vertex_dict[v].get_inDegree() == 0:
                stack.push(v)
                count -= 1
                 
    if count != 0:
        raise ValueError('input contains a cycle')            
    return outstring
    
def main():
    '''Entry point for the tsort utility allowing the user to specify
       a file containing the edge of the DAG'''
    if len(argv) != 2:
        print("Usage: python3 tsort.py <filename>")
        exit()
    try:
        f = open(argv[1], 'r')
    except FileNotFoundError as e:
        print(argv[1], 'could not be found or opened')
        exit()
    
    vertices = []
    for line in f:
        vertices += line.split()
       
    try:
        result = tsort(vertices)
        print(result)
    except Exception as e:
        print(e)
    
if __name__ == '__main__': 
    main()
    input = ['1', '2', '1', '9', '1', '8', '9', '8', '9', '10', '8', '11', '10', '11', '2', '3', '3', '11', '3', '4', '4', '7', '4', '5', '7', '5', '7', '13', '7', '6', '6', '14', '6', '12']
    expect = "1\n9\n10\n8\n2\n3\n4\n7\n6\n12\n14\n13\n5\n11"
    actual = tsort(input)
    print(actual)
    print('got here')
