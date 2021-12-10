import os

    # step 1
def solve_letter_of_seg_h_up(processed_entry):
    pattern_of_1 = processed_entry['number_to_pattern'][1]
    pattern_of_7 = processed_entry['number_to_pattern'][7]

    for letter in pattern_of_7:
        if (not letter in pattern_of_1):
            processed_entry['segment_to_letter']['h_up'] = letter

    # step 2
def solve_pattern_of_6(processed_entry):
    patterns_of_len_6 = processed_entry['length_to_patterns'][6]
    pattern_of_1 = processed_entry['number_to_pattern'][1]

    index_to_remove = None
    for i,p in enumerate(patterns_of_len_6):
        for letter_of_pattern_of_1 in pattern_of_1:
            if (not letter_of_pattern_of_1 in p):
                processed_entry['number_to_pattern'][6] = p 
                index_to_remove = i
    patterns_of_len_6.pop(index_to_remove)

    # step 3 & 4
def solve_letter_of_seg_up_r_and_down_r(processed_entry):
    pattern_of_6 = processed_entry['number_to_pattern'][6]
    pattern_of_1 = processed_entry['number_to_pattern'][1]

    for letter in pattern_of_1:
        if (not letter in pattern_of_6):
            processed_entry['segment_to_letter']['up_r'] = letter
        else:
            processed_entry['segment_to_letter']['down_r'] = letter

def doesPatternAcontainsPatternB(pa, pb):
    for letter in pb:
        if (not letter in pa):
            return False
    return True 

    # step 5 & 6
def solve_pattern_of_9_and_0(processed_entry):
    patterns_of_len_6 = processed_entry['length_to_patterns'][6]
    pattern_of_4 = processed_entry['number_to_pattern'][4]
    index_to_remove = None
    for i,p in enumerate(patterns_of_len_6):
        if(doesPatternAcontainsPatternB(p, pattern_of_4)):
            processed_entry['number_to_pattern'][9] = p
            index_to_remove = i
    # remove p from patterns_of_len_6
    patterns_of_len_6.pop(index_to_remove)

    processed_entry['number_to_pattern'][0] = patterns_of_len_6[0]
    patterns_of_len_6.pop(0)

    # step 7
def solve_pattern_of_3(processed_entry):
    patterns_of_len_5 = processed_entry['length_to_patterns'][5]
    pattern_of_1 = processed_entry['number_to_pattern'][1]

    index_to_remove = None
    for i,p in enumerate(patterns_of_len_5):
        if(doesPatternAcontainsPatternB(p, pattern_of_1)):
            processed_entry['number_to_pattern'][3] = p
            index_to_remove = i
    # remove p from patterns_of_len_6
    patterns_of_len_5.pop(index_to_remove)

    # step 8 & 9 
def solve_pattern_of_2_and_5(processed_entry):
    up_r_letter = processed_entry['segment_to_letter']['up_r']
    down_r_letter = processed_entry['segment_to_letter']['down_r']

    patterns_of_len_5 = processed_entry['length_to_patterns'][5]

    i_of_2 = None
    i_of_5 = None 
    for i,p in enumerate(patterns_of_len_5):
        if (up_r_letter in p):
            processed_entry['number_to_pattern'][2] = p
            i_of_2 = i

        elif (down_r_letter in p):
            processed_entry['number_to_pattern'][5] = p
            i_of_5 = i 
        else:
            print ("ERROR shouldn't happen")

def get_pattern_to_number_map(number_to_pattern_map):
    print (number_to_pattern_map)
    reverse_map = {}
    for k,v in number_to_pattern_map.items():
        reverse_map[v] = k
    return reverse_map
    
# read input into a list of numbers
with open(os.path.join(os.getcwd(),"q8/input.txt"), "r") as f:
    inputs = [ l[:-1].split("|") for l in f.readlines()]

print (inputs)

all_entries = []

sum = 0 

for entry in inputs:
    patterns = [''.join(sorted(pattern)) for pattern in entry[0].strip().split(" ")]
    output = [''.join(sorted(digit)) for digit in entry[1].strip().split(" ")]
    processed_entry = {
        'patterns': patterns,
        'output': output,
        'number_to_pattern': {},
        'segment_to_letter': {},
        'length_to_patterns': {
            5: [],
            6: []
        }
    }
    for p in patterns:
        if (len(p) == 2):
            processed_entry['number_to_pattern'][1] = p
        elif (len(p) == 4):
            processed_entry['number_to_pattern'][4] = p
        elif (len(p) == 3): 
            processed_entry['number_to_pattern'][7] = p
        elif (len(p) == 7):
            processed_entry['number_to_pattern'][8] = p
        elif (len(p) == 5 or len(p) == 6):
            processed_entry['length_to_patterns'][len(p)].append(p)
        else:
            print ("ERROR unknown length", len(p))
    # step 1
    solve_letter_of_seg_h_up(processed_entry)

    # step 2
    solve_pattern_of_6(processed_entry)

    # step 3 & 4
    solve_letter_of_seg_up_r_and_down_r(processed_entry)

    # step 5 & 6
    solve_pattern_of_9_and_0(processed_entry)

    # step 7
    solve_pattern_of_3(processed_entry)

    # step 8
    solve_pattern_of_2_and_5(processed_entry)

    pattern_to_number = get_pattern_to_number_map(processed_entry["number_to_pattern"])
    print (pattern_to_number)
    output_number_list = [str(pattern_to_number[pattern]) for pattern in output]

    final_number = int("".join(output_number_list))
    print (final_number)

    sum += final_number
    all_entries.append(processed_entry)

print (sum)
"""
output_digits = [ row[1].strip().split(" ") for row in inputs]

print (output_digits)

unique_num_segment_dict = {
# num_of_segment: digit_represented
    2: 1,
    4: 4,
    3: 7,
    7: 8
}


count = 0

for entry in output_digits:
    for digit in entry:
        if (len(digit) in unique_num_segment_dict):
            print (digit)
            count += 1

print(count)
"""