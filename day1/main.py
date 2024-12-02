totalSumPart1 = 0
totalSumPart2 = 0
left = []
right = []

with open('input.txt') as file:
    for line in file:
        lists = line.strip().split()
        num1 = lists[0]
        num2 = lists[1]

        left.append(int(num1))
        right.append(int(num2))


for i in range(len(left)):
    num1 = sorted(left)[i]
    num2 = sorted(right)[i]
    totalSumPart1 += abs(int(num1) - int(num2))
    totalSumPart2 += num1 * right.count(num1)



print(totalSumPart1, totalSumPart2)