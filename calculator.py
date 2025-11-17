def main():
    """
    Основная функция программы
    """
    print("=" * 40)
    print("       ДОБРО ПОЖАЛОВАТЬ В КАЛЬКУЛЯТОР")
    print("=" * 40)
    print("Программа запущена успешно!")

    # Точка входа в программу
if __name__ == "__main__":
    main()
def add(a, b):
    """
    Сложение двух чисел
    
    Аргументы:
        a (float): первое число
        b (float): второе число
    
    Возвращает:
        float: результат сложения
    """
    return a + b

    def main():
    """
    Основная функция программы
    """
import os

def clear_screen():
    """
    Очистка экрана консоли
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def show_operation_history(history):
    """
    Показывает историю операций
    
    Аргументы:
        history (list): список выполненных операций
    """
    if not history:
        print("История операций пуста.")
        return
    
    print("\n" + "=" * 40)
    print("         ИСТОРИЯ ОПЕРАЦИЙ")
    print("=" * 40)
    for i, operation in enumerate(history, 1):
        print(f"{i}. {operation}")