from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

if __name__ == '__main__':
    # 从自定义的工具文件中读取中国地图的信息
    from 数据结构.实训.tool import get_adjacency
    from 数据结构.实训.tool import get_position

    position = get_position()
    adjacency = get_adjacency()
    province = list(position.keys())
    G = nx.Graph()
    G.add_nodes_from(province)
    G.add_edges_from(adjacency)
    note_labels = dict()
    for p in province:
        note_labels[p] = p
    fig = plt.figure()
    plt.ion()
    all_colors = ['r', 'g', 'b', 'y', 'c', 'm', 'k']
    colors = dict()
    province = list(G.nodes)
    for p in province:
        colors[p] = 'w'
    start = province[0]
    other_nodes = list()
    other_nodes.append(start)
    while other_nodes:
        p = other_nodes.pop(0)
        color_list = deepcopy(all_colors)
        # 给p上一种邻接点没有用过的颜色
        for n in G[p]:
            # 将邻接点加入上色目标
            if colors[n] == 'w' and n not in other_nodes:
                other_nodes.append(n)
            elif colors[n] in color_list:
                color_list.remove(colors[n])
        colors[p] = color_list[0]
        plt.clf()
        values = [colors.get(node) for node in G.nodes()]
        nx.draw_networkx_nodes(G, pos=position, node_color=values, node_size=300, alpha=0.6)
        nx.draw_networkx_edges(G, pos=position)
        nx.draw_networkx_labels(G, position, labels=note_labels, font_size=8)
        plt.pause(0.02)
    # 检查一共用了多少颜色
    s = set()
    for c in colors.values():
        s.add(c)
    print(len(s), s)
    plt.ioff()
    plt.show()