#약 55분
n = int(input())
drg_cuv = [[]for _ in range(n)]
dxs, dys = [0,-1,0,1],[1,0,-1,0]
        
def findIndex(dx, dy):
    for i in range(4):
        if dxs[i] == dx and dys[i] == dy:
            return i
for i in range(n):
    y, x, d, g = map(int,input().split())
    #index에 1씩 더해가면서 접근하면 될듯 
    # 0세대 입력
    drg_cuv[i].append([x,y])
    drg_cuv[i].append([x+dxs[d], y+dys[d]])
    # 세대 만큼 반복
    for _ in range(g):
        #뒤에서 앞으로 오면서 덧붙히기
        end_point = drg_cuv[i][-1]
        for k in range(len(drg_cuv[i])-1, 0, -1):
            #끝점
            dx, dy = drg_cuv[i][k][0] - drg_cuv[i][k-1][0], drg_cuv[i][k][1] - drg_cuv[i][k-1][1]
            index = findIndex(dx, dy)
            # 다음 방향
            index = (index+1)%4
            end_point = [end_point[0]+dxs[index],end_point[1]+dys[index]]
            drg_cuv[i].append(end_point)

total_point = []
for cuv in drg_cuv:
    for point in cuv:
        if point not in total_point:
            total_point.append(point)
answer = 0

for i in range(100):
    for j in range(100):
        FIND = True
        for k in range(i,i+2):
            for p in range(j,j+2):
                if [k,p] not in total_point:
                    FIND = False
                    break
        if FIND == True:
            answer+=1
print(answer)