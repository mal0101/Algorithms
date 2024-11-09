def binary_search(sequence, target):
    begin_indx = 0
    end_indx = len(sequence) - 1
    
    while begin_indx <= end_indx:
        midpoint = begin_indx + (end_indx - begin_indx) // 2
        mid_value = sequence[midpoint]
        
        if mid_value == target:
            return midpoint
        
        elif target < mid_value:
            end_indx = midpoint - 1
        
        else:
            begin_indx = midpoint + 1
            
    return None


# test case:
sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 4
print(binary_search(sequence, target))  # 3
