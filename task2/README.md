## Описание задачи
Необходимо написать программу, которая сможет, приняв на вход последовательность операндов и операций, вывести все возможные варианты результата и их вероятности.

Выражение на входе может содержать скобки, и следующие операторы в порядке уменьшения их приоритета:
* – умножение
+ и - – сложение и вычитание
> - левый операнд больше, чем правый. Результат равен 1, если истинно, и 0 - если ложно

## В качестве операндов могут выступать:
n - целые положительные числа, либо 0 (0≤n≤100 000)
dn - результат броска игральной кости, где n целое положительное число, количество граней (1≤n≤100). Результатом будет равномерное распределение вероятностей между всеми гранями (от 1 до n). Каждый такой операнд в выражении – это результат отдельного броска (например, d4+d4 – это сумма результатов двух разных бросков четырехгранной кости).


## Входные данные (поступают в стандартный поток ввода)
Одна строка без пробелов, содержащая выражение для вычисления. Выражение гарантировано вычисляемое и не содержит синтаксических ошибок. Максимальная длина строки 110 символов.


## Выходные данные (ожидаются в стандартном потоке вывода)
Одна или несколько строк, в каждой из которых есть два числа, разделенных пробелом:

1. целое – один из вариантов результата
2. вещественное - процент вероятности такого варианта с математическим округлением до 2 знаков и разделителем .
Строки на выходе должны быть отсортированы от меньшего результата к большему.

## Примечание к округлению
В связи с округлением вероятностей - суммарная вероятность всех исходов может быть не равна 100%, это нормально, компенсировать это в решении не нужно