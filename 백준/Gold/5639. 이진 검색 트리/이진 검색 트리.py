import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, value):
        self.value = value
        # 왼쪽 노드를 가리킨다
        self.left = None
        # 오른쪽 노드를 가리킨다
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, insert_node):
        # root 가 없다면 insert하는 node가 root이다
        if self.root is None:
            self.root = insert_node
            return

        # 현재 위치한 노드
        current_node = self.root

        while True:
            # root보다 insert하는 node의 값이 더 작다면 왼쪽 트리에 있다.
            if current_node.value > insert_node.value:
                # 트리에 왼쪽 값이 없으면 노드를 넣는다.
                if current_node.left is None:
                    current_node.left = insert_node
                    break

                else:
                    # 트리의 왼쪽에 값이 있으면 다시 반복문을 돈다
                    current_node = current_node.left

            # root보다 insert하는 노드의 값이 더 크다면 오른쪽 트리에 있다.
            else:
                # 트리에 오른쪽 값이 없으면 노드를 넣는다.
                if current_node.right is None:
                    current_node.right = insert_node
                    break
                else:
                    # 트리의 왼쪽에 값이 있으면 다시 반복문을 돈다
                    current_node = current_node.right
    def get_root_node(self):
        return self.root


def post_search(current_node):
    # 왼쪽 노드가 존재한다면
    if current_node.left is not None:
        post_search(current_node.left)

    # 오른쪽 노드가 존재한다면
    if current_node.right is not None:
        post_search(current_node.right)

    # 왼쪽 오른쪽 노드 모두가 존재하지 않는다면
    result.append(current_node.value)


if __name__ == "__main__":
    # 이진 트리 생성
    tree = BinaryTree()
    while True:
        try:
            a = int(input())
            node = Node(a)
            tree.insert(node)
        except:
            break

    # 후위 탐색 시작
    result = []

    post_search(tree.get_root_node())
    for node in result:
        print(node)