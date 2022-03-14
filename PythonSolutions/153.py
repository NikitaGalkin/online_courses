class Buffer:
    def __init__(self):
        self.current_numbers = []

    def add(self, *a):
        for i in range(0, len(a)):
            self.current_numbers.append(a[i])
            if (len(self.current_numbers) == 5):
                sum = 0

                for j in range(0, len(self.current_numbers)):
                    sum += self.current_numbers[j]

                print(sum)
                self.current_numbers = []

    def get_current_part(self):
        return self.current_numbers



buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]