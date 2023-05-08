#Distance Between Bus Stops
def distanceBetweenBusStops(distance, start, destination):
    '''
    (0)-------1---------(1)
    |                    |
    |                    |
    4                    2
    |                    |
    |                    |
    (3)---------3--------(2)       
    '''
    clock_distance = anti_clock_distance = i = 0
    while i != destination:
        clock_distance += distance[i] 
        i+=1
    i = len(distance)
    while i != destination:
        anti_clock_distance += distance[i-1]
        i-=1
    if clock_distance < anti_clock_distance: return clock_distance
    else: return anti_clock_distance

print("Enter boarding and destination points:")
board = int(input())#0
depart = int(input())#3
print(distanceBetweenBusStops([1,2,3,4], board,depart))