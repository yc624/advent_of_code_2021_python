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

autocomplete_score_map = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
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

def process(line): 
    stack = []
    for bracket in line:
        if (bracket in open_to_close_map):
            stack.append(bracket)
        else:
            pop = stack.pop()
            if (not bracket == open_to_close_map[pop]):
                return {
                    "syntax_error": True
                }

    autocomplete_score = 0

    while (not len(stack) == 0):
        pop = stack.pop()
        autocomplete_score = autocomplete_score * 5 + autocomplete_score_map[open_to_close_map[pop]]
    return {
        "syntax_error": False,
        "autocomplete_score": autocomplete_score
    }



with open(os.path.join(os.getcwd(),"q10/input.txt"), "r") as f:
    inputs = [l[:-1]for l in f.readlines()]


autocomplete_scores = []

for line in inputs:
    result = process(line)
    if (result["syntax_error"] == False):
        autocomplete_scores.append(result["autocomplete_score"])

autocomplete_scores.sort()

print(autocomplete_scores[int(len(autocomplete_scores)/2)])

        