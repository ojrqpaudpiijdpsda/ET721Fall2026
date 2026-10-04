def addnumbers(a =0, b=0):
    return a +b

def subtractnumbers(a =0, b=0):
    return a - b

def multiplynumbers(a =1, b=1):
    return a *b


def dividenumbers(a , b):
    try:
        return a/b
    except ZeroDivisionError:
        print('Error!')
    except ValueError:
        print('Error!')
    except:
        print('ERROR!')