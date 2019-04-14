num_entries = int(input())

backrowPrices = list(map(int ,input().split(" ")))
backrowHeights= list(map(int, input().split(" ")))

frontrowPrices = list(map(int, input().split(" ")))
frontrowHeights = list(map(int, input().split(" ")))

backrow = [(i+1, backrowPrices[i], backrowHeights[i]) for i in range(len(backrowPrices))]
frontrow = [(i+1, frontrowPrices[i], frontrowHeights[i]) for i in range(len(frontrowPrices))]

backrow = sorted(backrow, key = lambda x: x[2])
frontrow = sorted(frontrow, key = lambda x: x[2], reverse = True)

backrow = sorted(backrow, key = lambda x: x[1])
frontrow = sorted(frontrow, key = lambda x: x[1])

valid = True
for i in range(len(backrow)):
    if backrow[i][2] <= frontrow[i][2]:
        # print(backrow[i], frontrow[i])
        valid = False
        break;

if valid:

    for i in range(len(backrow)):
        print(backrow[i][0], end = " ")
    print()
    for i in range(len(frontrow)):
        print(frontrow[i][0], end = " ")

else:
    print("impossible")

# sol = []
# i = 0
# while i < len(backrow) - 1:
#
#     while backrow[i][0] == backrow[i+1][0] and i < (len(backrow)-1):
#         curr_group.append(backrow[i])
#
#     while backrow
