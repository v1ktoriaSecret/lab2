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

        def main():
    """
    Основная функция программы с интерактивным меню и историей операций
    """
    operation_history = []
    
    while True:
        clear_screen()
        print("=" * 40)
        print("       ДОБРО ПОЖАЛОВАТЬ В КАЛЬКУЛЯТОР")
        print("=" * 40)
        
        print("\n" + "=" * 30)
        print("         ГЛАВНОЕ МЕНЮ")
        print("=" * 30)
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. История операций")
        print("6. Выход из программы")
        print("=" * 30)
        
        choice = input("Выберите операцию (1-6): ").strip()
        
        # Показ истории операций
        if choice == '5':
            show_operation_history(operation_history)
            input("\nНажмите Enter для продолжения...")
            continue
        
        # Выход из программы
        if choice == '6':
            print("\nСпасибо за использование калькулятора! До свидания!")
            break
        
        # Проверка корректности выбора операции
        if choice not in ['1', '2', '3', '4']:
            print("Ошибка: выберите операцию от 1 до 6!")
            input("Нажмите Enter для продолжения...")
            continue
        
        # Ввод чисел
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: пожалуйста, введите корректные числа!")
            input("Нажмите Enter для продолжения...")
            continue
        
        # Выполнение операции и сохранение в историю
        operation_text = ""
        if choice == '1':
            result = add(num1, num2)
            operation_text = f"{num1} + {num2} = {result}"
        elif choice == '2':
            result = subtract(num1, num2)
            operation_text = f"{num1} - {num2} = {result}"
        elif choice == '3':
            result = multiply(num1, num2)
            operation_text = f"{num1} * {num2} = {result}"
        elif choice == '4':
            result = divide(num1, num2)
            operation_text = f"{num1} / {num2} = {result}"
        
        print(f"\nРезультат: {operation_text}")
        operation_history.append(operation_text)
        input("\nНажмите Enter для продолжения...")
