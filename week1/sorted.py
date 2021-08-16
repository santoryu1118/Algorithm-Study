from typing import MutableSequence

# 삽입정렬 작은 수 앞 index에 넣어주고 뒤로 쭈르륵 밀어주는 정렬
def insertion_sort(a: MutableSequence, left : int, right:int)->None:
    print('삽입 정렬 시작')
    print(f'주어진 array : {a[left:right+1]}')
    for i in range(left +1, right+1):
        temp = a[i]
        j = i
        # 앞의 index원소 가져와서 temp랑 비교하는 식
        while a[j-1] > temp and j>left:
            a[j] = a[j-1]
            j -=1
        a[j] = temp
        if temp !=a[i]:
            print(f'a[{i}]원소 {temp}이 a[{j}]로 옮겨짐')       
    print(f'정렬 후 array : {a[left:right+1]}')
    print('삽입 정렬 끝')
    
# 퀵정렬 - pivot값을 기준으로 좌우 하고 stack이나 recursion사용하는 정렬
def quick_sort(a: MutableSequence, left : int, right:int, insertion_bool=0) ->None:

    # 리스트 원소가 insertion_bool 이하일 시, 삽입 정렬로 교체 
    if right-left < insertion_bool:
        insertion_sort(a, left, right)

    else:
        pl = left
        pr = right
        pivot = a[(left+right)//2]

        print(f'a[{left}] ~ a[{right}]: {a[left:right+1]}')

        while pl <=pr:
            while a[pl] < pivot:  # a[pl]값이 pivot값이랑 같거나 커지면 멈추고 next step해줌
                pl +=1
            while a[pr] > pivot:
                pr -=1
            if pl <=pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl +=1
                pr -=1
        # if left < pr은 원소가 하나밖에 없는거 방지
        if left <pr: quick_sort(a, left, pr)
        if pl <right: quick_sort(a, pl, right)


# 합병정렬 - 원소를 한개될때까지 리커젼으로 나누고 두개의 나눠진 리스트에서 하나씩 추가해주는 정렬
def merge_sort(a: MutableSequence)->None:
    if len(a)>1:
        mid = len(a)//2
        # L = a 이런식으로 하면 a원소 바뀌면 L도 바뀌는데 L = a[:mid] 이런식으로 하면 안바뀜.
        L = a[:mid]
        R = a[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                a[k] = L[i]
                i +=1
                k +=1
            else :
                a[k] = R[j]
                j +=1
                k +=1
        while i < len(L):
            a[k] = L[i]
            i +=1
            k +=1
        while j < len(R):
            a[k] = R[j]
            j +=1
            k +=1

# 힙 정렬
# 완전 이진 트리 안에 조그만한 트리들 heapify시켜줄 수 있게 함수 지정
def heapify(a: MutableSequence, left: int, right: int)->None:
    ''' 
               0
        1             2
     3     4       5     6
    7 8   9 10   11 12  13 14
    '''
    temp = a[left]
    parent = left
    while parent < (right+1)//2:  # parent node는 (child node-1)//2 임
        # left child 는 parent index*2 +1, +2
        lc = parent*2 +1
        rc = parent*2 +2
        child_to_choose = rc if rc <= right and a[lc] < a[rc]  else lc

        if temp < a[child_to_choose]:
            a[parent] = a[child_to_choose]  # parent index에 더 큰 값 넣어주기
            parent = child_to_choose
        else: 
            break

    a[parent] = temp
    
def heap_sort(a:MutableSequence)->None:
    n = len(a)-1

    # 트리(배열)를 완전히 heapify 해주는 과정
    # 최대값이 0번 index에 들어가게됨
    for i in range(n//2, -1, -1):
        heapify(a, i, n)
    
    # 최대값이랑 맨 마지막 index값이랑 switch 해주면서 뒤에서부터 큰 순으로 정렬
    for i in range(n, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, 0, i-1)


if __name__ == '__main__':
    # numbers =[]
    # for i in range(int(input())):
    #     numbers.append(int(input()))
    # insertion_sort(numbers,0,len(numbers)-1)
    a = [1,6,5,3,7,9,8,10]
    # quick_sort(a, 0, len(a)-1)
    # insertion_sort(a)
    heap_sort(a)
    print(a)


