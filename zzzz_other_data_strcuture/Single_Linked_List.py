##원문은 이곳에.##
#https://underflow101.tistory.com/3


#  1.시간복잡도
#
# Single Linked List
#    	최선	  최악
# 삽입	O(1)	O(1)
# 삭제	O(1)	O(1)
# 탐색	O(k)	O(N)

# 2. 장점
#
# 삽입과 삭제가 O(1)에 이루어진다.
# 삽입과 삭제를 할 때마다 동적으로 링크드 리스트의 크기가 결정되므로 전통적인 배열(Array)에 비해 처음부터 큰 공간을 할당할 필요가 없어진다.
# 메모리 관리가 용이하다. (사실상 이게 가장 큰 이유이다.)
# 3. 단점
#
# Random Access, 즉 배열처럼 index를 통해 탐색이 불가능하다.
# 탐색이 O(N)이 걸린다. (Head부터 Tail까지 모두 탐색 시)
# 사실상 삽입과 삭제가 왼쪽에서(Head에서) 이루어지지 않을 경우, 결국 탐색을 먼저 해야 하기 때문에 삽입과 삭제 모두 적게는 O(k)부터 최악의 경우 O(N)까지 걸릴 가능성이 있다. 이게 뭔 개소리야
# 파이썬에서 링크드 리스트는 의미가 크게 없는 게, 그냥 리스트 쓰면 된다. C++의 STL vector보다도 훨씬 쓰기 간편하며, 어떠한 타입의 데이터도(심지어 튜플이나 리스트마저) 넣을 수 있고 동적으로 메모리 관리가 되기 때문에, 링크드 리스트의 의미가 크게 퇴색된다.
# 4. 결론
#
# 파이썬의 리스트를 사용하자.


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SList(object):
    def __init__(self):
        self.head = Node(None)
        self.size = 0

    def listSize(self):
        return self.size

    def is_empty(self):
        if self.size != 0:
            return False
        else:
            return True

    def selectNode(self, idx):
        if idx >= self.size:
            print("Index Error")
            return None
        if idx == 0:
            return self.head
        else:
            target = self.head
            for cnt in range(idx):
                target = target.next
            return target

    def appendleft(self, value):
        if self.is_empty():
            self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        self.size += 1

    def append(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.size += 1
        else:
            target = self.head
            while target.next != None:
                target = target.next
            newtail = Node(value)
            target.next = newtail
            self.size += 1

    def insert(self, value, idx):
        if self.is_empty():
            self.head = Node(value)
            self.size += 1
        elif idx == 0:
            self.head = Node(value, self.head)
            self.size += 1
        else:
            target = self.selectNode(idx - 1)
            if target == None:
                return
            newNode = Node(value)
            tmp = target.next
            target.next = newNode
            newNode.next = tmp
            self.size += 1

    def delete(self, idx):
        if self.is_empty():
            print('Underflow: Empty Linked List Error')
            return
        elif idx >= self.size:
            print('Overflow: Index Error')
            return
        elif idx == 0:
            target = self.head
            self.head = target.next
            del (target)
            self.size -= 1
        else:
            target = self.selectNode(idx - 1)
            deltarget = target.next
            target.next = target.next.next
            del (deltarget)
            self.size -= 1

    def printlist(self):
        target = self.head
        while target:
            if target.next != None:
                print(target.data, '-> ', end='')
                target = target.next
            else:
                print(target.data)
                target = target.next





mylist = SList()
mylist.append('A')
mylist.printlist()
mylist.append('B')
mylist.printlist()
mylist.append('C')
mylist.printlist()
mylist.insert('D', 1)
mylist.printlist()
mylist.appendleft('E')
mylist.printlist()
print(mylist.listSize())
mylist.delete(0)
mylist.printlist()
mylist.delete(3)
mylist.printlist()
mylist.delete(0)
mylist.printlist()
mylist.appendleft('A')
mylist.printlist()