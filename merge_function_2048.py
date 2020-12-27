"""
Merge function for 2048 game.

http://www.codeskulptor.org/#user47_LdpzTlalqn_1.py

"""
def move(line):
    """
    Function to segregate the 0 and non zero entries
    """
    results = [0]*len(line)
    index = 0
    for item in line:
        if item!=0:
            results[index] = item
            index+=1
    return results

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code
    results = [0]*len(line)
    line_1 = move(line)
    line_2 = list(line_1)
    flag = True
    for num in range(len(line_1)-1):
        if line_1[num] == line_1 [num+1] and flag:
            line_2[num] = 2*line_1[num]
            line_2[num+1] = 0
            flag = False
        else:
            flag = True
    results = move(line_2)
    return results

print merge([2,0,2,2])
