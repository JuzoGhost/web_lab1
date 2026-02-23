import requests
import urllib.parse


def solve_math_expression():
    print("--- Калькулятор через Math.js API ---")

    # 1. Введення даних користувачем
    # Приклад для вашого варіанту: 2*sqrt(4)
    user_input = input("Введіть математичний вираз (наприклад, 2*sqrt(4)): ")

    # 2. Підготовка URL (кодування спецсимволів, як-от '+', '/', '*')
    encoded_expr = urllib.parse.quote(user_input)
    url = f"https://api.mathjs.org/v4/?expr={encoded_expr}"

    try:
        # 3. Відправка GET-запиту
        response = requests.get(url)

        # Перевірка на успішність запиту (код 200)
        if response.status_code == 200:
            # 4. Обробка та виведення результату
            result = response.text
            print(f"\nРезультат від API: {result}")
        else:
            print(f"\nПомилка API: Статус {response.status_code}")
            print(f"Повідомлення: {response.text}")

    except Exception as e:
        print(f"\nВиникла помилка при підключенні: {e}")


if __name__ == "__main__":
    solve_math_expression()