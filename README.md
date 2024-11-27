# Python_AL

11-20 AL

# Div(Binary) ALG
  1. 자료가 크기순으로 정렬되어 있을 것. (Reverse 상관 X)
  2. List를 반으로 쪼갬 있을법한 곳을 
  3. 대충 속도가 매우 빠르다 콘
  4. log(2)100

# 원리
  1. List를 반으로 쪼개(중앙기준으로)
  2. 원하는 값이 있는 범위로 접근 = 해당 안되는 범위를 제외해버림(빠름)

그러면 list를 len 해서 값을 //2 하고나서 그 값으로 셀을 선택해버리기? = 중간값 (이분)
그리고 나눠진 list len //2 반복해  = 범위가 계속 좁혀짐
값이 더 크다면 오른쪽으로 작다면 왼쪽으로 범위를 좁혀가는 과정. 뛸떄마다 거리는 //2가 됨

# FIFO / LIFO 회문 
  1.qu/st 의 방식을 정리한다
  2.어떤 문장이 있을떄 앞과 뒤 서로 대체하여도 값이 같은 경우에 사용한다
  3.Qu/ST에서 FIFO/LIFO의 개념 그대로 서칭을 한다 만약 이게 꺼낸 순서와 역순이 일치한다면 회문임이 증명된다
  
여기서 Qu = append/pop()지정 안해주면 제일 마지막놈 / 아니면 너가 대상위치를 지정하던가 0 or -1 등등.. // 
stack은 pop써야만 한다! ()은 qu에서 꼭 지정해줘야해 까먹기금지

elif문을 통한 다가가는 내용이 같지 않다면 이게 메인 
// 한글자라도 틀리면 바로 False // 좌-우 에서 확인해보고 // 서로 교차될때까지 진행한다면 True값을 줌 

# 동명의인찿기
dict['',1] 쓰는거 기억하지 / 얜 STR값이랑 INT값을 매칭시켜둚 // Hash Slot

d[] 안에 같은사람의 이름이 있다면 for 문 써서  if in 해서 있ㅇ으면 +=1 해서 증가시키기 없으면 초기화
그리고나서 값이 증가한걸 return res로 뺴내주면 됨

dict 쓰면 아무튼 빠름 // 메모리많이씀 O(n)
list 약간느림 // 멤적게씀 O(n2)

  
# Dict 로 대상 찿아보기  / 11-27 AL
그냥 해당 dict내에서 뭐 있나 찍어서 찿아보기 list할때랑 비슷한 맛임
그냥 딕셔너리를 만들때부터 데이터를 넣어서 바로 색인하기  =  O(1) //한번에 찿을수있는 "정렬되어 있다면"

  1.친구찿기 알고리즘
    대충 서로 일촌관계/이촌관계/3촌관계/4촌관계 등등으로 정리가 되잖아 
    이거 DS Tree 그거 아님? 순회형으로 어디서 많이 본,,,, Graph잔아?
    Ex. 싸이월드같은 촌수개념에 + 친밀도로 보자면 1:1로 알면 친밀도가 1 (이걸 촌수로 보면 된다) 건너 2/ 건너건너면 3 

    vertex to edge // nord to edge

    그러니까 그래프 그리는거도 하자 쉽잔아... <--시험문제일수도있어 응애
    
# dict / list 로 표현해보자
  1. dict에 key(vertex) 부분에 먼저 정해야하겠지 value(연결된 사람들을 넣으면 된다.)
  2. 그러면 즉 서로 접점이 있는 (대응하는) 값으로 넣어주어야만 한다 이거야 // dict안에 list도 들어가니까...

  fr_info ={
    'Summer':['Jhon',Justin','Mike'] // 이런식으로 관계를 서로 찎어서 연결되었다는걸 기록 // 순서는 상관없다
    'XI_JIN_Phuuu' :[''] // 이런식으로 나가는거거든~
  }

그러면 이제 친구 불러오기를 해보자 
  1. 자기 자신을 출력함
  2. 그러고 옆에 붙은 친구들이 딸려오겠네?
  3. 그놈을 다시 출력시키면?
  4. 다른친구가 또 나온다는거야
 ! 주의사항 친구 리스트에 서로 겹치는 부분이 있다면 재방문하는 사소한 찐빠가 일어남 ==  그러면 그걸 처리해줘야겠지?
  1. 외부로 데이터를 빼두면서 스캔 
  2. 거기서 중복이 보이면 그걸 삭제 // 삭제는 이미 스캔이 완료되어서 추가적으로 더 들어오는 데이터 값에만 POP이 해당함.
  3. PROFIT!!!
! 이걸 안해주면 무한반복이 걸려버리는 이상한 상황이 생김

# 코드로 생각해보기
#친구 리스트에서 자신의 모든 친구를 찾는 알고리즘
#입력: 친구 관계 그래프 g, 모든 친구를 찾을 자신 start
#출력: 모든 친구의 이름
def print_all_friends(g, start):
    qu = []       # 기억 장소1: 앞으로 처리해야 할 사람들을 큐에 저장
    done = set()  # 기억 장소2: 이미 큐에 추가한 사람들을 집합에 기록(중복 방지)
    qu.append(start)  # 자신을 큐에 넣고 시작
    done.add(start)   # 집합에도 추가

    
    #코드의 핵심내용
    while qu:           # 큐에 처리할 사람이 남아 있는 동안
        p = qu.pop(0)   # 큐에서 처리 대상을 한 명 꺼내 // POP(0) <---이새기 중요
        print(p,d)        # 이름을 출력하고
        for x in g[p]:  # 그의 친구들 중에
            if x not in done:  # 아직 큐에 추가된 적이 없는 사람을
                qu.append(x)   # 큐에 추가하고
                done.add(x)    # 집합에도 추가
                
#친구 관계 리스트
#A와 B가 친구이면
#A의 친구 리스트에도 B가 나오고, B의 친구 리스트에도 A가 나옴

fr_info = {​​​​​
    'Summer': ['John', 'Justin', 'Mike'],
    'John': ['Summer', 'Justin'],
    'Justin': ['John', 'Summer', 'Mike', 'May'],
    'Mike': ['Summer', 'Justin'],
    'May': ['Justin', 'Kim'],
    'Kim': ['May'],
    'Tom': ['Jerry'],
    'Jerry': ['Tom']
}​​​​​
print_all_friends(fr_info, 'Summer')
print()
print_all_friends(fr_info, 'Jerry')

해석: 즉 찿으면 리스트에 넣고 다른 리스트에도 넣어두고 하나하나 빼면서 서로 비교해보는거임~
즉 방문했으면 다시 재방문하지 않는것이 핵심인거지
qu 랑 list집합을 활용하여 for 문 뻉뻉이 돌리면서 추가 pop 반복을 하게 된다 이거징

=  그래프 탐색 알고리즘 콘

촌수 계산 넣어보기?

n+1 로 1:1 = 1 / 1:2 = 2 이런식으로 늘려주면 되겠네?

# 친구관계 + 친밀도 계산 해보기
def print_all_friends(g, start):
    qu = []
    done = set()
    
    qu.append((start,0)) #튜플 형태로 저장했으니까
    
    done.add(start)
    while qu:
        (p,d) = qu.pop(0)
        print(p,d)
        for x in [p]:
            if x not in done:
            
                qu.append((x, d+1)) #중요함 // Summer의 친밀도 0 즉 그 친구들은 +=1 되는거지 (직접적으로 이어진 1:1 이니까)
                
                done.add(x)


fr_info ={
'Summer': ['John', 'Justin', 'Mike'],
'John': ['Summer', 'Justin'],
'Justin': ['John', 'Summer', 'Mike', 'May'],
'Mike': ['Summer', 'Justin'],
'May': ['Justin', 'Kim'],
'Kim': ['May'],
'Tom': ['Jerry'],
'Jerry': ['Tom']
}
print_all_friends(fr_info, 'Summer')
print()
print_all_friends(fr_info, 'Jerry')    

#응용한다면?
    while qu:
        (p,d) = qu.pop(0)
        
        if d<2:
            print(p,d)
            
        for x in [p]:
            if x not in done:
                qu.append((x, d+1))
                done.add(x)

// 이렇게 출력 범위를 지정해버릴수도있음

#정리
  1. 일단 Tuple을 사용했음 / 값을 서로 대응시켰으니 말이야
  2. 대충 DBMS배울적에 나온 그 맛임....
  3. 셀 번호를 지정하여 해당 튜플에서 값을 추출이 가능함 extract
  4. 튜플을 (()) 하는 이유는 append할때 이미 (start,0) 를 제공했으니 한번 더 덮어버리는 것
  5. (p,d) = qu.pop(0) <--0 지정 까먹지말기 + 이건 값을 나눠서 각각 저장한다는 뜻임

# 연습문제 div_to_2_TREE // 너비 우선 탐색 BFS
#그래프 탐색: 너비 우선 탐색
#입력: 그래프 g, 탐색 시작점 start
#출력: start에서 출발해 연결된 꼭짓점들을 출력
def bfs(g, start):
    qu = []# 기억 장소 1: 앞으로 처리해야 할 꼭짓점을 큐에 저장
    done = set()# 기억 장소 2: 이미 큐에 추가한 꼭짓점들을 집합에 기록(중복 방지)

    qu.append(start) # 시작점을 큐에 넣고 시작
    done.add(start) # 집합에도 추가
    while qu: # 큐에 처리할 꼭짓점이 남아있으면
      p = qu.pop(0) # 큐에서 처리 대상을 꺼내어
      print(p)  # 꼭짓점 이름을 출력하고
    for x in g[p]:  # 대상 꼭짓점에 연결된 꼭짓점들 중에
            if x not in done: # 아직 큐에 추가된 적이 없는 꼭짓점들을
                qu.append(x)  # 큐에 추가하고
                done.add(x) # 집합에도 추가
#그래프 정보
g = {
1: [2, 3],
2: [1, 4, 5],
3: [1],
 4: [2],
5: [2]
}
bfs(g, 1)

# 에서 WWE 하면
#그래프 탐색: 너비 우선 탐색
#입력: 그래프 g, 탐색 시작점 start
#출력: start에서 출발해 연결된 꼭짓점들을 출력
def bfs(g, start):
    qu = []# 기억 장소 1: 앞으로 처리해야 할 꼭짓점을 큐에 저장
    done = set()# 기억 장소 2: 이미 큐에 추가한 꼭짓점들을 집합에 기록(중복 방지)

    qu.append((start,0)) # 시작점을 큐에 넣고 시작
    done.add(start) # 집합에도 추가
    while qu: # 큐에 처리할 꼭짓점이 남아있으면
      (p,d) = qu.pop(0) # 큐에서 처리 대상을 꺼내어
      print(p,d)  # 꼭짓점 이름을 출력하고
    for x in g[p]:  # 대상 꼭짓점에 연결된 꼭짓점들 중에
            if x not in done: # 아직 큐에 추가된 적이 없는 꼭짓점들을
                qu.append(x)  # 큐에 추가하고
                done.add(x) # 집합에도 추가
#그래프 정보
g = {
1: [2, 3],
2: [1, 4, 5],
3: [1],
 4: [2],
5: [2]
}
bfs(g, 1)

얘도 마찬가지로 친밀도가 추가된 버전임 // tuple (()) 절대 까먹지 말자.

# DFS // 깊이 우선 탐색.
    






































    



  

