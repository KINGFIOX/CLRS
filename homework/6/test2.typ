== (1) 定义

设root节点为出发的节点, 可以是任意的节点;

n表示除了root节点以外的任一节点

g(n)表示: 从root节点到n节点的实际代价

h\*(n)表示: 从n, 沿着路径path_rest(v)到root节点的代价, 其中path_rest(v)表示: 假设path(v)表示从root-->n,
已经经过的点, 而path_rest(v)表示, 还没有经过的点