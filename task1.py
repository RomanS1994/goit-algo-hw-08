import heapq


# ==============================================================
# min_cost_to_connect_cables
# ==============================================================

def min_cost_to_connect_cables(cable_lengths: list) -> int:
    """
    Обчислює мінімальну вартість для з'єднання всіх кабелів в один, 
    де вартість об'єднання двох кабелів дорівнює їхній сумарній довжині.
    
    Аргументи:
        cable_lengths (list): Список довжин кабелів.
    
    Повертає:
        int: Мінімальна комулятивна вартість об'єднання кабелів.
    """
    # Якщо список кабелів порожній, повертаємо 0
    if not cable_lengths:
        return 0
    

    heapq.heapify(cable_lengths)
    print(f'Довжини кабелів до обʼєднань - {cable_lengths}')
    
    total_lengths = 0  # Загальна вартість об'єднання кабелів
    count = 0  # Лічильник кількості об'єднань

    while len(cable_lengths) > 1:
        count += 1
        

        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)


        length = first + second
        total_lengths += length

        # Додаємо новий об'єднаний кабель назад у купу
        heapq.heappush(cable_lengths, length)
        print(f'Довжини кабелів після {count}-го обʼєднання - {cable_lengths}')

    return total_lengths


cables = [45, 2, 12, 5, 9, 23, 3, 8]
cables2 = [1, 1, 9, 2, 1, 2]

# Виклик функції та виведення результату
res = min_cost_to_connect_cables(cables)
print(f'Мінімальна Комулятивна сума = {res}')






# ==============================================================
# max_cost_to_connect_cables
# ==============================================================


def min_cost_to_connect_cables(cable_lengths: list) -> int:

    if not cable_lengths:
        return 0
    
    cable_lengths = [-el for el in cable_lengths]
    heapq.heapify(cable_lengths)
    print(f'Довжини кабелів до обʼєднань - {[-el for el in cable_lengths]}')
    
    total_lengths = 0  # Загальна вартість об'єднання кабелів
    count = 0  # Лічильник кількості об'єднань

    while len(cable_lengths) > 1:
        count += 1
        

        first = -heapq.heappop(cable_lengths)
        second = -heapq.heappop(cable_lengths)


        length = first + second
        total_lengths += length

        # Додаємо новий об'єднаний кабель назад у купу
        heapq.heappush(cable_lengths, -length)
        print(f'Довжини кабелів після {count}-го обʼєднання - {[-el for el in cable_lengths]}')

    return total_lengths


cables = [45, 2, 12, 5, 9, 23, 3, 8]

# Виклик функції та виведення результату
res = min_cost_to_connect_cables(cables)
print(f'Максимальна Комулятивна сума = {res}')
