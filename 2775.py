test_case = int(input())

floors = []
rooms = []

for _ in range(test_case):
    floors.append(int(input()))
    rooms.append(int(input()))

for i in range(test_case):
    floor = floors[i]
    room = rooms[i]
    
    if floor == 0:
        print(rooms[i])
    else:
        room = [(j + 1) for j in range(rooms[i])]
        for j in range(floors[i]):
            for p in range(1, rooms[i]):
                room[p] += room[p - 1]
    print(room[-1])