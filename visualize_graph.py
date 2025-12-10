import networkx as nx
import matplotlib.pyplot as plt


nodes = [
    {"id": "start", "type": "start", "next": "review"},
    {"id": "review", "type": "code_review", "next": "end"},
    {"id": "end", "type": "end", "next": None}
]


G = nx.DiGraph()

for node in nodes:
    G.add_node(node["id"], type=node["type"])
    if node["next"]:
        G.add_edge(node["id"], node["next"])

pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, arrowsize=20)
nx.draw_networkx_edge_labels(G, pos)
plt.show()
