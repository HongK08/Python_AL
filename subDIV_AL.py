def Binary_Serch(a,x):
    start = 0 # 시작지점의 지정
    end = len(a) -1 #끝인데 왜 -1? 배열의 index가 0부터 시작하니까 (이부분 시험? Blank)

    while start <= end: # 얘가 이진탐색을 시작함 Start가 End보다 커지면 멈춰버림
        mid = (start+end)//2 # 이건 누가봐도 중간값 구하기지? //기억
        if x == a[mid]:
            return mid
        elif x>a[mid]:
            start = mid +1
        else:
            end = mid -1
    return -1 

d = [1,4,9,16,25,36,49,64,81]
print(Binary_Serch(d,36))
print(Binary_Serch(d,50))
