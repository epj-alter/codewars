operation = "2 + 3 * 4 / 3 - 6 / 3 * 3 + 8"
# not the best, gotta refactor!


class Calculator(object):
    @staticmethod
    def evaluate(string):
        opr = string.split()

        try:
            while len(opr) > 1:
                while '/' in opr:
                    i = opr.index('/')
                    div = float(opr[i - 1]) / float(opr[i + 1])
                    opr.pop(i + 1)
                    opr[i] = div
                    opr.pop(i - 1)

                while '*' in opr:
                    i = opr.index('*')
                    mul = float(opr[i - 1]) * float(opr[i + 1])
                    opr.pop(i + 1)
                    opr[i] = mul
                    opr.pop(i - 1)

                while '-' in opr:
                    i = opr.index('-')
                    sum = float(opr[i - 1]) - float(opr[i + 1])
                    opr.pop(i + 1)
                    opr[i] = sum
                    opr.pop(i - 1)

                while '+' in opr:
                    i = opr.index('+')
                    sum = float(opr[i - 1]) + float(opr[i + 1])
                    opr.pop(i + 1)
                    opr[i] = sum
                    opr.pop(i - 1)
        except:
            pass

        return float(opr[0])


print(Calculator.evaluate(operation))
