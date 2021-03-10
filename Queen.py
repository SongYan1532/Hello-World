import matplotlib.pyplot as plt

result_set = []
an = [0] * 8


def is_legal(n):
    for i in range(n):
        if an[i] == an[n] or abs(n - i) == abs(an[n] - an[i]):
            return False
    return True


def put(n):
    if n == 8:
        result_set.append(an[:])
        return
    for i in range(8):
        an[n] = i
        if is_legal(n):
            put(n + 1)


def show():
    put(0)
    color1 = (0, 0, 0)
    color2 = (255, 255, 255)
    color3 = (255, 0, 0)
    num = 0
    for rs in result_set:
        chessboard = []
        for i in range(8):
            line = []
            for j in range(8):
                if rs[i] == j:
                    line.append(color3)
                elif (i + j) % 2 == 0:
                    line.append(color1)
                else:
                    line.append(color2)
            chessboard.append(line[:])
        num = num + 1
        plt.title("Answer" + str(num))
        plt.imshow(chessboard)
        plt.savefig("E:\\学习\\python\\数据结构\\实训\\结果\\四皇后Answer" + str(num) + ".png")


if __name__ == '__main__':
    show()
    print("运行完成")
