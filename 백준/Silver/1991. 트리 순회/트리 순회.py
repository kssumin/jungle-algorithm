class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def preorder(result, key):
    current_node = tree[key]
    result.append(current_node.value)

    if current_node.left != ".":
        preorder(result, current_node.left)
    if current_node.right != ".":
        preorder(result, current_node.right)

    return result


def midorder(result, key):
    current_node = tree[key]

    # 왼쪽이 있다면 왼쪽으로 간다.
    if current_node.left != ".":
        midorder(result, current_node.left)

    # 왼쪽이 없다는 소리니깐 본인을 출력
    result.append(current_node.value)

    # 오른쪽이 있다면 오른쪽으로 간다
    if current_node.right != ".":
        midorder(result, current_node.right)

    return result


def postorder(result, key):
    current_node = tree[key]

    # 왼쪽이 있다면 왼쪽으로 간다.
    if current_node.left != ".":
        postorder(result, current_node.left)

    # 오른쪽이 있다면 오른쪽으로 간다
    if current_node.right != ".":
        postorder(result, current_node.right)

    result.append(current_node.value)
    return result


if __name__ == "__main__":
    n = int(input())

    tree = {}
    for _ in range(n):
        value, left, right = input().split()
        node = Node(value, left, right)
        tree[value] = node

    print("".join(preorder([], "A")))
    print("".join(midorder([], "A")))
    print("".join(postorder([], "A")))