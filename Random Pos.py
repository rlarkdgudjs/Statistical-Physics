import networkx as nx
import matplotlib.pyplot as plt

# 그래프 생성
G = nx.DiGraph()

# 텍스트 파일에서 데이터 읽기
file_path = 'C:\\2024_KEB_bootcamp_python\Statistical Physics\pathlist.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        # 공백이나 빈 줄은 건너뜀
        if not line.strip():
            continue

        # 쉼표로 데이터를 나누고 정수로 변환
        parts = line.strip().split(',')
        if len(parts) == 3 and all(part.isdigit() for part in parts):
            source, target, weight = map(int, parts)
            G.add_edge(source, target, weight=weight)

# 레이아웃 조정
pos = nx.spring_layout(G)

# 그래프 시각화
node_size = 100
edge_width = 1.0
font_size = 8
arrowsize = 10

nx.draw(G, pos, with_labels=True, font_size=font_size,
        node_size=node_size, node_color='skyblue',
        font_color='black', arrowsize=arrowsize,
        width=edge_width)

# 엣지에 가중치 표시
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red')

plt.show()
