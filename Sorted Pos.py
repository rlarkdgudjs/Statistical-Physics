import networkx as nx
import matplotlib.pyplot as plt

# 그래프 생성
G = nx.DiGraph()

# 텍스트 파일에서 데이터 읽기 (경로, 가중치 정보)
file_path = 'C:\\2024_KEB_bootcamp_python\Statistical Physics\pathlist.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        if not line.strip():
            continue

        parts = line.strip().split(',')
        if len(parts) == 3 and all(part.isdigit() for part in parts):
            source, target, weight = map(int, parts)
            G.add_edge(source, target, weight=weight)

# 텍스트 파일에서 데이터 읽기 (노드 위치 정보)
pos_file_path = 'C:\\2024_KEB_bootcamp_python\Statistical Physics\poslist.txt'
pos_dict = {}
with open(pos_file_path, 'r') as pos_file:
    pos_lines = pos_file.readlines()
    for pos_line in pos_lines:
        if not pos_line.strip():
            continue

        node_id, x, y = map(float, pos_line.strip().split())
        pos_dict[node_id] = (x, y)

# 그래프 시각화
fig, ax = plt.subplots()
node_size = 100
edge_width = 1
font_size = 6
arrowsize = 6

nx.draw(G, pos=pos_dict, with_labels=True, font_size=font_size, node_size=node_size,
        node_color='lightgreen', font_color='black', arrowsize=arrowsize, width=edge_width, ax=ax, connectionstyle='arc3,rad=0.1')

labels = nx.get_edge_attributes(G, 'weight')

# 링크 라벨 위치 조정 및 투명도 조절
offset = 0.35

for (n1, n2), label in labels.items():
    x1, y1 = pos_dict[n1]
    x2, y2 = pos_dict[n2]

    # 라벨의 위치를 링크의 시작쪽에 가깝게 조정
    label_pos_x = x1 - offset * (x1 - x2)
    label_pos_y = y1 - offset * (y1 - y2)

    ax.text(label_pos_x, label_pos_y, label, color='red', ha='center', va='center', fontsize=6,
            bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.1', alpha=0.7))

plt.show()
