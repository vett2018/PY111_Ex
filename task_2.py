"""
    Дано N человек, считалка из K слогов. Считалка начинает считать с первого человека. Когда считалка досчитывает до k-го слога, человек,
    на котором она остановилась, вылетает. Игра происходит до тех пор, пока не останется последний человек.
    Для данных N и К дать номер последнего оставшегося человека
"""

def last_name(n_people: int, k_number: int) -> int:
    """
    :param n_people: Список из людей
    :param k_number: Считалка из слогов
    :return: Вывод последнего человека
    """
    if n_people == 1:
        return people_list[0]
    else:
        people_list.pop(k_number % n_people - 1) # удаляем выбывшего "-1" так как список начинается с 0-индекса, а порядковый номер с 1
    return last_name(n_people - 1, k_number)

if __name__ == "__main__":
    people_list = ["Коля", "Света", "Ольга", "Саша", "Витя"]
    people_list_copy = people_list.copy() #копия списка создана для того что бы узнать порядковый номер человека
    print(f'Список людей: {" ".join(people_list)}')
    slog = int(input(f'Укажите кол-во слогов: '))
    people = last_name(len(people_list), slog)
    print(f'Остался: {people}')
    print(f'Порядковый номер человека = {people_list_copy.index(people) + 1}')