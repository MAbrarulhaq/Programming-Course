def no_factors(lockers , students):
    count = 0
    for i in range(1 , students + 1):
        if(lockers % i == 0):
            count += 1
    return count
    
def openLocks(lockers , students):
    count = 0
    for i in range(1 , lockers + 1):
        if(no_factors(i , students) % 2 != 0):
            count += 1
    return count
    
def mostTouchableLocker(lockers , students):
    cur_max = 1
    curr_pos = 1
    for i in range(1 , lockers + 1):
        temp = no_factors(i , students)
        if(temp >= cur_max):
            cur_max = temp
            curr_pos = i
    return curr_pos
    

