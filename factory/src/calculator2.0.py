'''
second version of factory pattern
OOP
'''

class calculation():
    def __init__(self):
        self._x = None
        self._y = None

    def operation(self):
         pass

    def getResult(self):
        return self.operation()


class Addition(calculation):
    def __init__(self):
        super(Addition,self).__init__()

    def operation(self):
        return self._x + self._y


class Multiple(calculation):
    def __init__(self):
        super(Multiple, self).__init__()

    def operation(self):
        return self._x * self._y


def createCal(calName):
    if calName =="+":
        return Addition()

    elif calName == "*":
        return Multiple()



if __name__ == "__main__":
    inputs = input("input the calculation in following  format: 'number1 operator number2'\n ")
    x,oper,y = inputs.split()
    cal = createCal(oper)
    cal._x ,cal._y = float(x),float(y)
    res =  cal.getResult()
    print("{} {} {} = {}".format(x,oper,y,res))