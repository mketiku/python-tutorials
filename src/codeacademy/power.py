def differentiate(expression):
    # uses the formula x^n ==> nx^n-1
    negdel = expression.split("+")
    retval = ""
    for i in [0, eval((negdel.__sizeof__)/4)]:
        numbers = ""
        variable = ""
        for n in (0, i[length]):
            if (isdigit(n)):
                numbers += n
            else:
                variable += n
        return numbers + variable


expression = input("Type in your expression: ")
if (expression):
    print("Result of evaluation = " + differentiate(expression))
else:
    print("Cannot evaluate.")
