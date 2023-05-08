#Check If It Is a Straight Line
def checkStraightLine(coordinates):
    sum_list = [abs(sum(item)) for item in coordinates]    
    difference_list = [sum_list[i+1] - sum_list[i] for i in range(len(sum_list)-1)]
    if len(set(difference_list)) > 1: return False
    else: return True

print(checkStraightLine([[0,0],[0,1],[0,-1]]))