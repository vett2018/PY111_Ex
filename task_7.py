import random


"""
Сорт
Дано: массив из 10**6 целых чисел, каждое из которых лежит на отрезке [13, 25].
Задача: отсортировать массив наиболее эффективным способом
"""

def quicksort(list_: list) -> list:
    """
    Для сортировки списка (массива) использую алгоритм быстрой сортировки
    :param list_: Не отсортированный список (массив)
    :return: Отсортированный список (массив)
    """
    if len(list_) <= 1:
        return list_
    else:
        pivot = random.choice(list_)
        left = []
        right = []
        equal = []
        for elem in list_:
            if elem < pivot:
                left.append(elem)
            elif elem > pivot:
                right.append(elem)
            else:
                equal.append(elem)
        return quicksort(left) + equal + quicksort(right)

if __name__ == "__main__":
    list_ = [random.randint(13, 25) for _ in range(10)]
    print(f'Неотсортированный список:\n{list_}')
    sort_list_ = quicksort(list_)
    print(f'Отсортированный список посредством быстрой сортировки:\n{sort_list_}')