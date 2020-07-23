
__author__ = "Guilherme Dias"
__version__ = "Python 3.7"

class Machine:
    number = 0
    number2 = 0
    operator = ''

    @classmethod
    def operation(cls):

        if cls.operator == 'more':
                cls.number2 = cls.number2 + cls.number
                cls.number = 0

        elif cls.operator == 'less':
                cls.number2 = cls.number2 - cls.number
                cls.number = 0

        elif cls.operator == 'times':
                cls.number2 *= cls.number
                cls.number = 0

        elif cls.operator == 'division':
                if cls.number != 0:
                    cls.number2 = cls.number2 / cls.number
                    cls.number = 0
                else:
                    pass

        elif cls.operator == 'pow':
                aux = (cls.number2 ** cls.number)
                cls.number2 = aux
                cls.number = 0

        elif cls.operator == 'square':
                if cls.number != 0:
                    aux = cls.number2 ** (1/cls.number)
                    cls.number2 = aux
                    cls.number = 0

        elif cls.operator == 'clear':
            cls.number = 0
            cls.number2 = 0

        cls.operator = ''
