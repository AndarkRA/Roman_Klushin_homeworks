class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self._name = name
        self._surname = surname
        self._position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self._name} {self._surname}'

    def position(self):
        return f'{self._position}'  # на всякий случай должность тоже ввел

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]



if __name__ == '__main__':
    user = Position(name='Ivan', surname='Ivanov', position='Lawyer', wage=100, bonus=70)
    print(user.get_full_name())
    print(user.position())
    print(user.get_total_income())
