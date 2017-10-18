import re


def calculate(expression):
    if type(expression) is str:
        terms = exSplit(expression)
    else:
        terms = [expression]
    r = []
    for x in range(0, terms.__len__()):
        r.append(derivative(terms[x]))
    return r


def exSplit(ex):
    delimiters = "+", "-", "*", "/"
    regex_pattern = '|'.join(map(re.escape, delimiters))
    split_ex = re.split(regex_pattern, ex)
    print("split_ex: ", split_ex)
    return split_ex


def expressionString(val):
    return " + ".join(val)


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


def chainRule(term):
    print("")
    print("term: ", term)
    termsin = trigoperations
    termsout = ["cos(x)", "(-sin(x))", "sec(x)^2", "sec(x) * tan(x)", "(-csc(x) * cot(x))", "csc(x)^2"]
    ex = term.split("(")[0]
    inner = term.split("(")[1].split(")")[0]
    print("inner: ", inner)
    if ex in termsin:
        print("termout: ", termsout[termsin.index(ex)])
        newterm = termsout[termsin.index(ex)].replace("x", inner)
        newterm += " * (" + " + ".join(calculate(inner)) + ")"
        return newterm


trigoperations = ["sin", "cos", "tan", "sec", "csc", "cot"]
inputs = ["3x^5+7x^4-5x^3*2x^2/8x+6", "sec(3x^3 + 5x^2)"]
outputs = []
# fin = input("Equation to Compute: ")
# calculate(fin)
for i in range(0, inputs.__len__()):
    outputs.append(calculate(inputs[i]))

print("")
print("Outputs")
for i in range(0, outputs.__len__()):
    print("")
    print("input:  ", inputs[i])
    print("output: ", outputs[i])
