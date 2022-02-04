import re

#сбор входного выражения и преобразование в строку значений и строку вероятностей
stroka = re.findall(r"\w+|[()+>\-*]", str(input()))
values = []
chance = []
operators = '()*-+>'
for i in range(len(stroka)):
    if stroka[i].isdigit():
        s1 = [int(stroka[i])]
        e1 = [1]
    elif stroka[i] in operators:
        s1 = stroka[i]
        e1 = stroka[i]
    else:
        num = int(stroka[i][1:])
        s1 = [i + 1 for i in range(num)]
        e1 = [1 / num for i in range(num)]
    values.append(s1)
    chance.append(e1)

#вывод ответа
def output(a, b):
    a, b = (list(t) for t in zip(*sorted(zip(a, b))))
    for i in range(len(a)):
        print(a[i], f'{round(b[i] * 100, 2):.2f}', sep=' ')

#функция суммы
def summa(a1, b1, a2, b2, c):
    g = []
    g1 = []
    t = 0
    for i in range(len(a1)):
        for q in range(len((a2))):
            if c == '+':
                t = a1[i] + a2[q]
            elif c == '*':
                t = a1[i] * a2[q]
            elif c == '-':
                t = a1[i] - a2[q]
            elif c == '>':
                if a1[i] > a2[q]:
                    t = 1
                else:
                    t = 0
            if t in g:
                j = g.index(t)
                t = 0
                t = b1[i] * b2[q] + g1[j]
                g1[j] = t
                continue
            else:
                g.append(t)
                t = 0
                t = b1[i] * b2[q]
                g1.append(t)
                t = 0
    return(g, g1)

def mainfun(v, c):
    while len(v) != 1:
        if '(' in v:
            i1 = -1 - v[-1::-1].index('(')
            i2 = v[i1::1].index(')')
            a, b = i1, i2
            b = a + b
            i2 = i1 + i2
            i1 = i1 + 1
            v[a], c[a] = mainfun(v[i1:i2], c[i1:i2])
            del v[(a + 1):b]
            del v[b]
            del c[(a+1):b]
            del c[b]
        else:
            i1, i2, i3 = 0, 0, 0
            if '*' in v:
                i3 = v.index('*')
            elif '+' in v and '-' in v:
                if v.index('+') < v.index('-'):
                    i3 = v.index('+')
                else:
                    i3 = v.index('-')
            elif '+' in v:
                i3 = v.index('+')
            elif '-' in v:
                i3 = v.index('-')
            elif '>' in v:
                i3 = v.index('>')
            i1 = i3 - 1
            i2 = i3 + 1
            v[i1], c[i1] = summa(v[i1], c[i1], v[i2], c[i2], v[i3])
            del v[i3:(i2 + 1)]
            del c[i3:(i2 + 1)]
        mainfun(v, c)
    return(*v, *c)

values, chance = mainfun(values, chance)

output(values, chance)
