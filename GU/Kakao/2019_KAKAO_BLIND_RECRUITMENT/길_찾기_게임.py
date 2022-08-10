import sys
sys.setrecursionlimit(10**6)

class tree_node:
    def __init__(self, num, x, y):
        self.x = x
        self.y = y
        self.num = num
        self.left = None
        self.right = None

class bin_tree:
    def __init__(self):
        self.root = None
    
    def add(self, node):
        if self.root == None:
            self.root = node
        else:
            traveler = self.root
            while True :
                # node의 x 값이 pointer가 가리키는 x보다 작을 때
                if traveler.x > node.x:
                    # 자리가 비었다면 그 자리에 대입
                    if traveler.left == None:
                        traveler.left = node
                        break
                    # 비지 않았다면 포인터 이동
                    else:
                        traveler = traveler.left
                else:
                    if traveler.right == None:
                        traveler.right = node
                        break
                    else:
                        traveler = traveler.right
    # 전위 순회-> 중간, 왼쪽, 오른쪽
    def pre_order(self, node, print_list):
        walker = node
        print_list.append(node.num)
        if node.left != None:
            self.pre_order(node.left, print_list)
        if node.right != None:
            self.pre_order(node.right, print_list)
        return print_list
    
    # 후위 순회 -> 왼쪽, 오른쪽, 중간
    def post_order(self, node, print_list):
        walker = node
        if node.left != None:
            self.post_order(node.left, print_list)
        if node.right != None:
            self.post_order(node.right, print_list)
        print_list.append(node.num)
        return print_list
    
def solution(nodeinfo):
    answer = [[]]
    # tree 선언
    tree = bin_tree()
    # nodeinfo에 번호 설정
    for idx, (x, y) in enumerate(nodeinfo):
        nodeinfo[idx] = [x,y,idx+1]
    # tree에 node를 넣을 때, y값이 높은 것을 먼저 넣어야하므로
    # y값이 높은 순서대로, x값이 낮은 순서대로 정렬.
    nodeinfo = sorted(nodeinfo, key = lambda x: (-x[1], x[0]))
    # node를 만들고 tree에 넣기
    for (x, y, num) in nodeinfo:
        node = tree_node(num, x, y)
        tree.add(node)
    pre = tree.pre_order(tree.root, [])
    post = tree.post_order(tree.root, [])
    answer = [pre, post]
    return answer