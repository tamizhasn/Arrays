def findMissingAndRepeatedValues(grid):
        l=len(grid)
        counts={}
        for row in grid:
            for num in row:
                counts[num] = counts.get(num, 0) + 1

        for num in range(1, l*l+1):
            if num not in counts:
                missing = num
            elif counts[num] == 2:
                repeat = num

        print([repeat, missing])

grid=[[3,2],[2,4]]
findMissingAndRepeatedValues(grid)
