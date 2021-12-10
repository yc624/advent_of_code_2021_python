import os

open_to_close_map = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

score_map = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def contain_syntax_error(line):
    stack = []
    for bracket in line:
        if (bracket in open_to_close_map):
            stack.append(bracket)
        else:
            pop = stack.pop()
            if (not bracket == open_to_close_map[pop]):
                return (True, bracket)  
    return (False, None) 


with open(os.path.join(os.getcwd(),"q10/input.txt"), "r") as f:
    inputs = [l[:-1]for l in f.readlines()]

score = 0

for line in inputs:
    result = contain_syntax_error(line)
    if (result[0] == True):
        score += score_map[result[1]]
        
print (score)