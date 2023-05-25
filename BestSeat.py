# BestSeat.py
import math
def bestSeat(seats):

    occupied = []
    i = 0
    while i < len(seats):
        if seats[i] == 1:
            occupied.append(i)
        i += 1
    print("occupied = ", occupied)
    # to find max contiguous empty seats and positions of the occupied seats at the ends
    maxContEmptySeats = 0
    bestSeat = -1
    emptySeats = 0
    for i in range(1, len(occupied)):

        emptySeats = occupied[i] - occupied[i - 1] - 1 # seats in between the two occupied seats.
        print("i = ", i, "emptySeats = ", emptySeats, "occupied[i] = ", occupied[i], "occupied[i - 1] = ", occupied[i -1])
        if emptySeats > maxContEmptySeats:
            maxContEmptySeats = emptySeats
            bestSeat = (occupied[i-1] + occupied[i])//2

    return bestSeat



def main():
    seats = [1, 0, 1, 0, 0, 0, 1]
    print("seats = ", seats)
    result = bestSeat(seats)
    print("result = ", result)
    print("---------------------------------")
    seats = [1, 0, 0, 1]
    print("seats = ", seats)
    result = bestSeat(seats)
    print("result = ", result)
    print("---------------------------------")
    seats = [1, 0, 0, 0, 1, 0, 0, 0, 0, 1]
    print("seats = ", seats)
    result = bestSeat(seats)
    print("result = ", result)
    print("---------------------------------")

if __name__=='__main__':
    main()

