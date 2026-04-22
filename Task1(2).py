def task1():
    print('Введите строки:')
    lines = []
    while True:
        line = input()
        if lines == "":
            break
        lines.append(line)


    if not lines:
        print("Нет введённых строк.")
        return

    if len(lines) == 1:
        for i, check in enumerate(lines[0]):
            print(f"Индекс {i}: 'check")
    else:
        for row_idx, line in enumerate(lines, start = 1):
            for col_idx, check in enumerate(line):
                print(f"Строка {row_idx}, символ{cold_idx}: 'check'")


if __name__ == "__main__":
    task1()






    
