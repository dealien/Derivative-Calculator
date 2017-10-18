import re


def calculate(expression):
    if type(expression) is str:
        terms = exSplit(expression)
        # u = exSplit(expression)
        # terms = u[0::2]
    else:
        terms = [expression]
    r = []
    while terms.__len__() > 0:
        i = terms.pop(0)
        if i == "+":
            r.append(i)
        elif i == "-":
            r.append(i)
        elif i in trigoperations:
            l = terms.index(")")
            s = i
            for x in range(0, l):
                s += terms.pop(0)
            r.append(chainrule(s))
        elif i == ")":
            pass
        else:
            r.append(derivative(i))
    return "".join(r)


def exSplit(ex):
    delimiters = "+", "-", "*", "/", "(", ")"
    regex_pattern = '|'.join(map(re.escape, delimiters))
    iterms = re.split(regex_pattern, ex)
    operations = re.findall(regex_pattern, ex)
    split_ex = [None] * (len(operations) + len(iterms))
    split_ex[::2] = iterms
    split_ex[1::2] = operations
    split_ex = [x for x in split_ex if x]
    print("split_ex: ", split_ex)
    return split_ex


def expressionstring(val):
    return "+".join(val)


def derivative(term):
    if "x^" in term:
        coef = int(term.split("x^")[0])
        exp = int(term.split("x^")[1])
        print("")
        print("term: ", term)
        print("coef: ", coef)
        print("exp: ", exp)
        newcoef = coef * exp
        newexp = exp - 1
        if exp == 2:
            newterm = str(newcoef) + "x"
        else:
            newterm = str(newcoef) + "x^" + str(newexp)
        return str(newterm)
    elif "x" in term:
        coef = int(term.split("x")[0])
        newterm = coef
        return str(newterm)
    else:
        return "0"


def chainrule(term):
    print("")
    print("term: ", term)
    termsin = trigoperations
    termsout = ["cos(x)", "(-sin(x))", "sec(x)^2", "sec(x)*tan(x)", "(-csc(x)*cot(x))", "csc(x)^2"]
    outer = term.split("(")[0]
    inner = term.split("(")[1].split(")")[0]
    print("inner: ", inner)
    if outer in termsin:
        print("termout: ", termsout[termsin.index(outer)])
        newterm = termsout[termsin.index(outer)].replace("x", inner)
        newterm += "*(" + "".join(calculate(inner)) + ")"
        return newterm


trigoperations = ["sin", "cos", "tan", "sec", "csc", "cot"]
inputs = ["3x^5+7x^4-5x^3+2x^2+8x-6", "sec(3x^3+5x^2)", "cos(3x^3+5x^2)+cot(3x^3+5x^2)-9x^2+10x"]
# inputs = ["sec(3x^3+5x^2)"]
outputs = []
# fin = input("Equation to Compute: ")
# calculate(fin)
for i in range(0, inputs.__len__()):
    outputs.append((calculate(inputs[i])))

print("")
print("Outputs")
for i in range(0, outputs.__len__()):
    print("")
    print("input:  ", inputs[i])
    print("output: ", outputs[i])
