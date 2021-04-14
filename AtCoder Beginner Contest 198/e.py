class Node:
    def __init__(self, id_num, color):
        self.id_num = id_num
        self.color = color
        self.children = []

    def add_child(self, child):
        self.children.append(child)


n = int(input())
v = list(map(int, input().split()))

# 木構造を作成
tree = [Node(i+1, v[i]) for i in range(n)]
tree.insert(0, Node(0, 0))

edges = [list(map(int, input().split())) for _ in range(n-1)]

seen_nodes = [1]
remain_nodes = []
while(len(edges) != 0 ):
    for i in range(len(edges)):
        if edges[i][0] in seen_nodes:
            tree[edges[i][0]].add_child(edges[i][1])
            seen_nodes.append(edges[i][1])
        elif edges[i][1] in seen_nodes:
            tree[edges[i][1]].add_child(edges[i][0])
            seen_nodes.append(edges[i][0])
        else:
            remain_nodes.append(edges[i])
            continue
    edges = remain_nodes
# print(n, v)
# print(xy)
# for node in tree:
#     print("node:", node.id_num, "color:", node.color, "children:", node.children)

# 出力
output = ["1"]
complete_node = [1]

nodes = [1]
colors = {1:[v[0]]}

for depth in range(1, n + 1):
    next_nodes = []
    for i in nodes:
        next_nodes += tree[i].children

        for child in tree[i].children:
            if not tree[child].color in colors[i]:
                output.append(f"{child}")
            colors[child] = colors[i] + list([tree[child].color])
            complete_node.append(child)

    # 全てのノードを確認
    if len(complete_node) == n:
        break

    nodes = next_nodes

# 出力
# for color in sorted(colors.items()):
#     print(color)
print("\n".join(sorted(output)))
