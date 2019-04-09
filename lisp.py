
class LispObject():
    def eval(self):
        pass

    @staticmethod
    def parse(str):
        pass


class Integer(LispObject):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

    @staticmethod
    def parse(str):
        i = 0
        while i < len(str) and (str[i] >= '0' and str[i] <= '9' or str[i] == '-'):
            i += 1
        return i, Integer(int(str[0:i]))


class List(LispObject):
    def __init__(self, lst):
        self.list = lst

    @staticmethod
    def parse(str):
        list = []
        i = 1
        while i < len(str):
            if str[i] == ')':
                break
            elif str[i] == ' ':
                i += 1
            else:
                pos, obj = parse(str[i:])
                list.append(obj)
                i += pos
        return i+1, List(list)

    def eval(self):
        return list


def parse(str):
    i = 0
    while i < len(str) and str[i] == ' ':
        i += 1
    if str[i] >= '0' and str[i] <= '9':
        return Integer.parse(str[i:])
    elif len(str) > i+1 and str[i] == '-' and str[i+1] >= '0' and str[i+1] <= '9':
        return Integer.parse(str[i:])
    elif str[i] == '(':
        return List.parse(str[i:])
    else:
        print('parse fail', str, i)
        pass


def eval(obj):
    return obj.eval()
