from typing import List, Tuple


def guess_number(target: int, numbers: List[int]) -> Tuple[int, int]:
    '''
    Алгоритм перебирает список по одному элементу, пока не встретит загаданное число.
    target (int): Число, которое нужно угадать.
    numbers (List[int]): Список чисел для поиска.
    Tuple[int, int]: Кортеж из двух значений:
            1. Угаданное число.
            2. Количество шагов (попыток), которые потребовались для поиска.
    '''
    attempts = 0  # Счётчик попыток
    for num in numbers:
        attempts += 1
        if num == target:
            return num, attempts
def get_range_from_input() -> List[int]:
    '''
    Вспомогательная функция для создания списка чисел.

    Пользователь вводит начало и конец диапазона,
    а функция возвращает список чисел.
        List[int]: Список чисел от start до end включительно.
    '''
    start = int(input("Начало диапазона: "))
    end = int(input("Конец диапазона: "))
    return list(range(start, end + 1))
