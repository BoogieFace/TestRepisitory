import numpy as np


def quickly_predict(number: int = 1) -> int:
    """Функция быстрого угадывания

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0  # счётчик попыток
    predict_number = 50  # первая попытка в центр интервала

    while True:
        count += 1
        if number == predict_number:
            break  # выход из цикла если угадали
        elif number > predict_number:
            predict_number = round(predict_number + 50 * 2 ** (-count))  # вдвое сокращаем интервал с повышением
        else:
            predict_number = round(predict_number - 50 * 2 ** (-count))  # вдвое сокращаем итервал с уменьшением

    return count


def score_game(quickly_predict) -> int:
    """Функция сбора статистики

    Args:
        quickly_predict ([type]): функция быстрого угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    random_array = np.random.randint(1, 101, size=1000)  # загадали список чисел

    for number in random_array:
        count_ls.append(quickly_predict(number))

    score = int(np.mean(count_ls))
    print(f"Алгоритм угадывает число в среднем за {score} попыток.")
    print(f"Максимальное число попыток: {max(count_ls)}.")
    return score


if __name__ == "__main__":
    # RUN
    score_game(quickly_predict)
