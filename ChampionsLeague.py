points = {}
goals = {}
for i in range(12):
    arr = input().split()

    team1 = arr[0]
    team2 = arr[4]
    score1 = int(arr[1])
    score2 = int(arr[3])

    if team1 in goals:
        goals[team1] += score1
    else:
        goals[team1] = score1

    if team2 in goals:
        goals[team2] += score2
    else:
        goals[team2] = score2

    if team1 in points and team2 in points:
        # print('p1')
        if score1 > score2:
            points[team1] += 3
        elif score1 < score2:
            points[team2] += 3
        else:
            points[team1] += 1
            points[team2] += 1
    elif team1 not in points and team2 not in points:
        # print('p1')
        if score1 > score2:
            points[team1] = 3
            points[team2] = 0
        elif score1 < score2:
            points[team2] = 3
            points[team1] = 0
        else:
            points[team1] = 1
            points[team2] = 1
    elif team1 in points and team2 not in points:
        if score1 > score2:
            points[team1] += 3
            points[team2] = 0
        elif score1 < score2:
            points[team2] = 3
        else:
            points[team1] += 1
            points[team2] = 1
    elif team1 not in points and team2 in points:
        if score1 > score2:
            points[team1] = 3
        elif score1 < score2:
            points[team1] = 0
            points[team2] += 3
        else:
            points[team1] = 1
            points[team2] += 1

    print('points', points)
    print('goals', goals)

points = {'manutd': 6, 'arsenal': 0, 'lyon': 1, 'fcbarca': 4}
goals = {'manutd': 10, 'arsenal': 3, 'lyon': 1, 'fcbarca': 5}
points_arr = sorted(points.values())
print(points_arr.pop())
print(points_arr)
