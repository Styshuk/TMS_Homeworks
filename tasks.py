from exceptions import TaskException


def task1(x: [float, int], y: [float, int]) -> [float, int]:
    """
    Даны действительные числа x и y.
    Вернуть (|x| − |y|) / (1+ |xy|)
    """
    return abs(x) - abs(y) / 1 + abs(x * y)


def task2(a: [float, int]) -> tuple[[float, int], [float, int]]:
    """
    Дана длина ребра куба.
    Вернуть кортеж с объемом куба и площадью его боковой поверхности.
    """
    return (a**3 , 6*a**2)

def task3(a: [float, int], b: [float, int]) -> [float, int]:
    """
    Даны два катета прямоугольного треугольника.
    Вернуть длину гипотенузы.
    """
    return c_squared = a**2 + b**2


def task4(string: str) -> str:
    """
    На вход подаётся строка.
    Вернуть строку равную предпоследнему символу введенной строки.
    """
    return str[-1]

def task5(string: str) -> str:
    """
    На вход подаётся строка.
    Вернуть строку равную первым пяти символам введенной строки.
    """
    return str[:5]

def task6(string: str) -> str:
    """
    На вход подаётся строка.
    Вернуть строку равную введенной строку без последних двух символов.
    """
    return str[:-2,]

def task7(string: str) -> str:
    """
    На вход подаётся строка.
    Вернуть строку равную всем элементам введенной строки с четными индексами.
    """
    return str [1::2]

def task8(string: str) -> str:
    """
    На вход подаётся строка.
    Вернуть строку равную третьему символу введенной строки.
    """
    return str[3]

def task9(string: str) -> str:
    """
    Дана строка. Если длина строки больше 10 символов, то вернуть новую строку
    с 3 восклицательными знаками в конце ('!!!') и вывести на экран.
    Если меньше 10, то вывести на экран второй символ строки
    """
    s = input('Введите строку: ')

    if len(s) > 10:
        print(s + '!!!')
    else:
        print(s[1])

def task10(string: str) -> tuple[str, [None, str]]:
    """
    Дана строка. Вернуть букву, которая находится в середине этой строки.
    Также, если эта центральная буква равна первой букве в строке, то вернуть часть строки между первым и
    последним символами исходной строки.
    (подсказка: для получения центральной буквы, найдите длину строки и разделите ее пополам.
    Для создания результирующий строки используйте срез)
    """


def task11(string: str) -> bool:
    """
    Напишите функцию которая проверяет является ли строка палиндромом.
    Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.
    """

    def is_palindrome(Jess):
        return Jess == Jess[::-1]

def task12(string: str, symbol: str) -> int:
    """
    Напишите функцию которая возвращает сколько раз символ встречается в строке
    """
    string = ""
    char = ""
    count = count_char_occurrences(string, char)
    print(f"Символ '{char}' встречается в строке '{string}' {count} раз(а)")

def task13(number: int) -> bool:
    """
    Дано число. Если это число делится на 1000 без остатка, то верните True иначе False
    """
    number = int(input("Введите число: "))
    if number % 1000 == 0:
        print(True)
    else:
        print(False)

def task14(guests_count: int) -> str:
    """
    В семье N свадьба. Они решили выбрать заведение, где будут праздновать в зависимости от количества гостей.
    Если их будет больше 50 - закажут ресторан, если от 20 до 50 - кафе, а если меньше 20 - отпразднуют дома.
    Вернуть "ресторан", "кафе", "дом" в зависимости от количества гостей.
    """
    def choose_place(num_guests):
        if num_guests > 50:
            return "ресторан"
        elif num_guests >= 20:
            return "кафе"
        else:
            return "дом"

def task15(number: int) -> tuple[int, int]:
    """
    Дано число. Найти сумму и произведение его цифр.
    """


def task16(start: int, end: int) -> list[int]:
    """
    Два натуральных числа называют дружественными, если каждое из них равно сумме всех делителей другого,
    кроме самого этого числа. Реализовать функцию для поиска всех пар дружественных чисел в заданном диапазоне
    """


def task17(n: int) -> float:
    """
    Для заданного числа N составьте программу вычисления суммы
    S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число
    """


def task18(number: [int, float], func_number: int) -> float:
    """
    Написать в отдельном файле 12 функций по переводу одних единиц измерения в другие.
    Импортировать написанные функции в данный файл и написать программу которая принимает на вход число и
    номер функции и возвращает результат
    1. Дюймы в сантиметры
    2. Сантиметры в дюймы
    3. Мили в километры
    4. Километры в мили
    5. Фунты в килограммы
    6. Килограммы в фунты
    7. Унции в граммы
    8. Граммы в унции
    9. Галлон в литры
    10. Литры в галлоны
    11. Пинты в литры
    12. Литры в пинты
    """


def micro_calc(a: [float, int], b: [float, int], sign: str) -> [float, int, str]:
    """
    Даны 2 действительных числа и строка с арифметическим знаком ('+', '-', ':', '*', '^')
    Необходимо вернуть результат арифметической операции
    В случае ошибки вычислений или неизвестного знака вернуть строку "error"
    """


def big_letters(phrase: str) -> str:
    """
    Напишите функцию, которая принимает строку, состоящую только из букв ASCII и пробелов, и возвращает
    эту строку печатными буквами шириной 5 символов и высотой 7 символов с одним пробелом между символами.
     - Заглавные буквы должны состоять из соответствующих заглавных букв.
     - Не имеет значения, состоит ли ввод из строчных или прописных букв.
     - Любые начальные и/или конечные пробелы во входных данных следует игнорировать.
     - Пустые строки или подобные строки, содержащие только пробелы, должны возвращать пустую строку.
     - Остальные пробелы (между буквами и/или словами) должны рассматриваться как любые другие символы.
       Это означает, что на входной пробел будет шесть пробелов в выводе или кратно шести,
       если пробелов было больше - плюс один от предыдущего символа!
     - Конечные пробелы должны быть удалены в результирующей строке.
     - Строка должна быть отформатирована таким образом, чтобы при передаче функции Python print()
       отображался желаемый результат (см., например, ниже)

      AAA  BBBB   CCC  DDDD  EEEEE FFFFF  GGG  H   H IIIII JJJJJ K   K L     M   M N   N  OOO  PPPP   QQQ  RRRR   SSS
     A   A B   B C   C D   D E     F     G   G H   H   I       J K  K  L     MM MM NN  N O   O P   P Q   Q R   R S   S
     A   A B   B C     D   D E     F     G     H   H   I       J K K   L     M M M N   N O   O P   P Q   Q R   R S
     AAAAA BBBB  C     D   D EEEEE FFFFF G GGG HHHHH   I       J KK    L     M   M N N N O   O PPPP  Q   Q RRRR   SSS
     A   A B   B C     D   D E     F     G   G H   H   I       J K K   L     M   M N   N O   O P     Q Q Q R R       S
     A   A B   B C   C D   D E     F     G   G H   H   I       J K  K  L     M   M N  NN O   O P     Q  QQ R  R  S   S
     A   A BBBB   CCC  DDDD  EEEEE F      GGG  H   H IIIII JJJJ  K   K LLLLL M   M N   N  OOO  P      QQQQ R   R  SSS

    TTTTT U   U V   V W   W X   X Y   Y ZZZZZ
      T   U   U V   V W   W X   X Y   Y     Z
      T   U   U V   V W   W X   X Y   Y     Z
      T   U   U V   V W   W  X X   Y Y     Z
      T   U   U V   V W W W   X     Y     Z
      T   U   U V   V W W W  X X    Y    Z
      T   U   U  V V  W W W X   X   Y   Z
      T    UUU    V    W W  X   X   Y   ZZZZZ
    """


def perfect_square(square: str) -> bool:
    """
    Напишите функцию, которая проверяет входную строку. Если строка представляет собой идеальный квадрат,
    верните true, в противном случае — false.
     - Символ '.' — правильный квадрат (1x1)
     - Правильные квадраты могут содержать только '.' и необязательно '\n' (перевод строки).
     - Идеальные квадраты должны иметь одинаковую ширину и высоту.
    """


def task_with_square_brackets(string_input: str) -> str:
    """
    Напишите программу которая принимает на вход строку вида 2[a]3[bc] или 2[a2[bc]]
    и возвращает строку сгененрированную по следующим правилам:
     - нужно повторить символы заключённые в квадратные скобки столько раз, какое число указано перед скобками
     - нужно соблюдать порядок действий как с обычными скобками (первым выполняются действия внутри скобок)
     - вложенность может быть любая
     - строка на входе в функцию всегда валидна
    """