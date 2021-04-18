"""
Problem statement :
Number of ways two students can sit next to each other in a class room where 
there are N number of desks arranged in two lines and some seats are already occupied.
First line numbering 1, 3, 5, etc and Second line numbering 2, 4, 6, ... N.
Input format: [N, occuped_desk_number, occuped_desk_number, ...]
Ex: i/p : [8, 1, 8] => there are 8 desks and out of which 1, 8 are  occupied. Out put should be 6
Possible seating : [2,4], [3, 4], [3,5], [4,6], [5, 6], [5,7] total 6 ways
"""

arr = [8, 1, 8]

def SeatingStudents(arr):
    
    num_desks = arr[0] # seating capacity
    occupied = arr[1:] #Occupied seats
    num_pairs = 0
    for pos in range(1, num_desks):
        #Ignore 
        if pos in occupied:
            continue
        #Available Bottom left desk
        if pos == num_desks - 1:
            #Check for right desk availability
            if pos+1 not in occupied:
                num_pairs += 1   
        #Available Left desks
        elif pos % 2 != 0:
            #Check for right desk availability
            if pos+1 not in occupied:
                num_pairs += 1
            #check for below desk availability
            if pos+2 not in occupied:
                num_pairs += 1 
        #Available Right desks
        elif pos % 2 == 0:
            #check for below desk availability
            if pos+2 not in occupied:
                num_pairs += 1 
        arr = num_pairs 
    return arr

print (SeatingStudents(arr))
