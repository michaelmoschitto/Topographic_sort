import random
def main():
    '''Entry point for the tsort utility allowing the user to specify
       a file containing the edge of the DAG'''
    out_file = open('vertices.txt', 'w')
    outstring = ''
    
    for i in range(1000000):
        int1 = random.randint(0,401)
        int2 = random.randint(0, 401)
        outstring += str(int1) + ' ' + str(int2) + '\n'
        
    out_file.write(outstring)
    # print(outstring[:-1])
    
if __name__ == '__main__': 
    main()
#     this is a test change