from pyecharts import Map

graph = {
    "德州市": ["聊城市", "济南市", "滨州市"],
    "滨州市": ["德州市", "济南市", "淄博市", "东营市"],
    "东营市": ["滨州市", "淄博市", "潍坊市"],
    "烟台市": ["威海市", "青岛市", "潍坊市"],
    "威海市": ["烟台市"],
    "聊城市": ["济南市", "德州市", "泰安市"],
    "济南市": ["滨州市", "淄博市", "莱芜市", "泰安市", "聊城市", "德州市"],
    "淄博市": ["滨州市", "东营市", "潍坊市", "莱芜市", "济南市", "临沂市", "泰安市"],
    "潍坊市": ["烟台市", "青岛市", "日照市", "临沂市", "淄博市", "东营市"],
    "青岛市": ["烟台市", "日照市", "潍坊市"],
    "莱芜市": ["淄博市", "泰安市", "济南市"],
    "泰安市": ["济南市", "莱芜市", "临沂市", "济宁市", "淄博市", "聊城市"],
    "菏泽市": ["济宁市"],
    "济宁市": ["泰安市", "临沂市", "枣庄市", "菏泽市"],
    "临沂市": ["淄博市", "潍坊市", "日照市", "枣庄市", "济宁市", "泰安市"],
    "日照市": ["临沂市", "青岛市", "潍坊市"],
    "枣庄市": ["临沂市", "济宁市"]

}

cities = {"滨州市": 0, "东营市": 0, "德州市": 0, "聊城市": 0, "烟台市": 0, "威海市": 0, "济南市": 0, "淄博市": 0,
          "潍坊市": 0, "青岛市": 0, "莱芜市": 0, "泰安市": 0, "菏泽市": 0, "济宁市": 0, "枣庄市": 0, "临沂市": 0,
          "日照市": 0}


def set_color(city):
    # 检查该节点准备要上的颜色是否与相邻的已访问的节点的颜色冲突
    # 一个存储四种颜色能否使用的列表（列表索引+1即为颜色），初始值全为True；
    # 对相邻节点使用的颜色进行遍历,若改颜色已经使用，则将改颜色的使用状态设置为False
    # 例如，1号颜色已经被使用，则colors = [False,True,True,True]
    colors = [True] * 4
    for node in graph[city]:
        num = cities[node] - 1
        if num == -1:
            continue
        else:
            colors[num] = False
    # .index()方法用于从列表中找出某个值第一个匹配项的索引位置
    # 当True不在列表中的时候会抛出异常，但实际上最多只需要四中颜色，所以这里不会出现全为false的情况
    cities[city] = colors.index(True) + 1

    # color = []
    # for node in graph[city]:
    #     color.append(cities[node])
    # # i从1-4（代表颜色），反复遍历color（内层循环），如果i与color里的值相等，就提前结束内层循环
    # # 如果是提前结束循环，则表示这种颜色没有被相邻的节点（已经遍历到的）用到，给该节点赋予一个颜色，结束外层循环
    # i = 1
    # while i < 5:
    #     n = 0
    #     for j in color:
    #         if i == j:
    #             break
    #         n = n + 1
    #     if n == len(color):
    #         cities[city] = i
    #         break
    #     i = i + 1


def get_color():
    for city in graph.keys():
        # 检查是否已上色,若没有上色则准备上色
        if cities[city] == 0:
            set_color(city)
        # 已经上色或者上色完毕,开始遍历与他相邻的节点
        for neighboringCity in graph[city]:
            if cities[neighboringCity] == 0:
                set_color(neighboringCity)


if __name__ == '__main__':
    get_color()
    for k in graph.keys():
        print(k + ":" + str(cities[k]))
    # 可视化输出
    city_list = list(cities.keys())
    values = list(cities.values())
    my_map = Map("山东地图示例", "地图着色", width=1000, height=600)
    my_map.add("山东", city_list, values,
               maptype="山东",
               visual_range=[1, 4],
               is_label_show=True,  # 地图上显示城市名
               label_text_size='18',  # 显示的字号
               is_visualmap=True,  # 开启后显示彩色
               pieces=[{"value": 1, "label": ' ', "color": "Beige"},
                       {"value": 2, "label": ' ', "color": "LavenderBlush"},
                       {"value": 3, "label": ' ', "color": "Lavender"},
                       {"value": 4, "label": ' ', "color": "LightCyan"}],  # 设置分段颜色
               is_piecewise=True)  # 开启分段显示

    my_map.render(path="地图着色.html")
