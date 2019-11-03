'''
first version of factory pattern
'''


def createCal(calName):
    if calName =="+":
        return add

    elif calName == "*":
        return multiple


def add(x,y):
    return x+y


def multiple(x,y):
    return x*y


def getResult(x,y,cal):
    return cal(x,y)



if __name__ == "__main__":
    inputs = input("input the calculation in following  format: 'number1 operator number2'\n ")
    x,oper,y = inputs.split()
    _x ,_y = float(x),float(y)
    cal = createCal(oper)
    res =  getResult(_x,_y,cal)

    print("{} {} {} = {}".format(x,oper,y,res))