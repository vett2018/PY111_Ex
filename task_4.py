import heapq


"""
Навигатор на сетке.
Дана плоская квадратная двумерная сетка (массив), на которой определена стоимость захода в каждую ячейку
(все стоимости положительные). Необходимо найти путь минимальной стоимости из заданной ячейки
в заданную ячейку и вывести этот путь.
"""

def dijkstra(grid, start, end):
    m = len(grid)
    n = len(grid[0])

    # Инициализация стоимости и посещенных ячеек
    costs = [[float('inf')] * n for _ in range(m)]
    costs[start[0]][start[1]] = grid[start[0]][start[1]]
    visited = [[False] * n for _ in range(m)]

    # Инициализация пути
    paths = {(i, j): [] for j in range(n) for i in range(m)}
    paths[start] = [start]

    # Очередь с приоритетом для хранения ячеек
    q = []
    heapq.heappush(q, (costs[start[0]][start[1]], start))

    while q:
        # Извлечение ячейки с минимальной стоимостью
        _, curr = heapq.heappop(q)

        # Проверка, является ли ячейка конечной
        if curr == end:
            return paths[curr]

        # Перебор соседних ячеек
        row, col = curr
        for i, j in [(row-1,col), (row+1,col), (row,col-1), (row,col+1)]:
            if 0 <= i < m and 0 <= j < n and not visited[i][j]:
                # Обновление стоимости и пути
                new_cost = costs[row][col] + grid[i][j]
                if new_cost < costs[i][j]:
                    costs[i][j] = new_cost
                    paths[(i, j)] = paths[(row, col)] + [(i, j)]
                    heapq.heappush(q, (new_cost, (i, j)))

        # Пометка текущей ячейки как посещенной
        visited[row][col] = True

    # Если не найдено пути до конечной ячейки, вернуть None
    return None

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
start = (0, 0)
end = (2, 2)
path = dijkstra(grid, start, end)
print(path)
