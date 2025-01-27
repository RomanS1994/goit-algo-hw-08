import heapq

def merge_k_lists(lists):
    """
    Зливає K відсортованих списків в один відсортований список.

    Аргументи:
        lists (list of lists): Список відсортованих списків, які потрібно злити.

    Повертає:
        list: Один відсортований список, що містить всі елементи з вхідних списків.
    
    """

    h = []
    
    # Додаємо всі елементи з вхідних списків до купи
    for el in lists:
        for value in el:
            heapq.heappush(h, value)

    # Витягуємо всі елементи з купи у відсортованому порядку
    return [heapq.heappop(h) for _ in range(len(h))]


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]


merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
