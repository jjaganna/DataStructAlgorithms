# SpiralTraverse.py

def spiralTraverse(array):
    n = len(array[0])  # Number of columns
    m = len(array)  # Number of rows
    if m == 1:
        return array[0]
    if n == 1:
        result = []
        for row in range(m):
            result.append(array[row][0])

        return result

    startCol = 0
    startRow = 0
    endCol = n - 1
    endRow = m - 1
    result = []
    curRow = 0
    curCol = 0
    while startCol < endCol and startRow < endRow:
        # go right
        while curCol <= endCol:
            result.append(array[curRow][curCol])
            curCol += 1
        curRow += 1
        curCol = endCol
        print("line 20: result = ", result, "curRow = ", curRow, "curCol = ", curCol)
        while curRow <= endRow:
            result.append(array[curRow][curCol])
            curRow += 1
        curCol -= 1
        curRow = endRow
        print("line 26: result = ", result, "curRow = ", curRow, "curCol = ", curCol)
        while curCol >= startCol:
            result.append(array[curRow][curCol])
            curCol -= 1
        curRow -= 1
        curCol = startCol
        print("line 32: result = ", result, "curRow = ", curRow, "curCol = ", curCol)
        while curRow > startRow:
            result.append(array[curRow][curCol])
            curRow -= 1
        print("line 36: result = ", result, "curRow = ", curRow, "curCol = ", curCol)
        curRow += 1
        curCol += 1
        print("line 39: result = ", result, "curRow = ", curRow, "curCol = ", curCol)
        startRow += 1
        startCol += 1
        endRow -= 1
        endCol -= 1
        print("result = ", result)
    print("out of while loop -- result = ", result)
    print("Edge cases")
    if  startRow == endRow:
        if startCol == endCol:
            result.append(array[startRow][startCol])
            return result
        elif curCol == startCol and startCol != endCol:
            while curCol <= endCol:
                result.append(array[curRow][curCol])
                curCol += 1
        elif curCol == endCol:
            while curCol >= startCol:
                result.append(array[curRow][curCol])
                curCol -= 1
    if startCol == endCol:
        if curRow == startRow and startRow != endRow:
            while curRow <= endRow:
                result.append(array[curRow][curCol])
                curRow += 1
        elif curRow == endRow:
            while curRow >= startRow:
                result.append(array[curRow][curCol])
                curRow -= 1

    print("out of while loop -- final result = ", result)
    return result

def main():
    array = [[1,2,3,4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
    print("array = ", array)
    result = spiralTraverse(array)
    print("result = ", result)
    print("--------------------------------------------------------")
    array = [[1, 2, 3, 4, 5], [12, 13, 14, 15, 6], [11, 10, 9, 8, 7]]
    print("array = ", array)
    result = spiralTraverse(array)
    print("result = ", result)
    print("--------------------------------------------------------")
    array = [[1]]
    print("array = ", array)
    result = spiralTraverse(array)
    print("result = ", result)
    print("--------------------------------------------------------")
    array = [[1, 2], [4, 3]]
    print("array = ", array)
    result = spiralTraverse(array)
    print("result = ", result)
    print("--------------------------------------------------------")
    array = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    print("array = ", array)
    result = spiralTraverse(array)
    print("result = ", result)
    print("--------------------------------------------------------")
    array = [
        [19, 32, 33, 34, 25, 8],
        [16, 15, 14, 13, 12, 11],
        [18, 31, 36, 35, 26, 9],
        [1, 2, 3, 4, 5, 6],
        [20, 21, 22, 23, 24, 7],
        [17, 30, 29, 28, 27, 10]
    ]
    print("array = ", array)
    result = spiralTraverse(array)
    print("result = ", result)
    print("--------------------------------------------------------")
    array = [
       [1,2,3],[8,9,4], [7,6,5]
    ]
    print("array = ", array)
    result = spiralTraverse(array)
    print("result = ", result)
    print("--------------------------------------------------------")
if __name__=='__main__':
    main()