len = 10
count = 0
kol = 4


def battle(mas, sign):
    for lvl in range(3, 0, -1):
        for i in range(len):  # закрывает по горизонтали справа
            for j in range(len):
                if mas[i][j] == 'x':
                    count += 1
                    if count >= lvl and (j + 1) < len and mas[i][j + 1] == 0:
                        mas[i][j + 1] = sign
                        return mas[i][j + 1]
                else:
                    count = 0

        for i in range(len):  # закрывает по горизонтали слева
            for j in range(len):
                if mas[i][j] == 'x':
                    count += 1
                    if count >= lvl and (j - count) >= 0 and mas[i][j - count] == 0:
                        mas[i][j - count] = sign
                        return mas[i][j - count]
                else:
                    count = 0

        for i in range(len):  # закрывает по вертикали снизу
            for j in range(len):
                if mas[j][i] == 'x':
                    count += 1
                    if count >= lvl and (j + 1) < len and mas[j + 1][i] == 0:
                        mas[j + 1][i] = sign
                        return mas[j + 1][i]
                else:
                    count = 0

        for i in range(len):  # закрывает по вертикали сверху
            for j in range(len):
                if mas[j][i] == 'x':
                    count += 1
                    if count >= lvl and (j - count) >= 0 and mas[j - count][i] == 0:
                        mas[j - count][i] = sign
                        return mas[j - count][i]
                else:
                    count = 0

        for i in range(len):  # низ главной диагонали снизу
            for j in range(len - i):
                if mas[j + i][j] == 'x':
                    count += 1
                    if count >= lvl and (j + i + 1) < len and (j + 1) < len and mas[j + i + 1][j + 1] == 0:
                        mas[j + i + 1][j + 1] = sign
                        return mas[j + i + 1][j + 1]
                else:
                    count = 0

        for i in range(len):  # низ главной диагонали свверху
            for j in range(len - i):
                if mas[j + i][j] == 'x':
                    count += 1
                    if count >= lvl and (j + i - count) >= 0 and (j - count) >= 0 and mas[j + i - count][
                        j - count] == 0:
                        mas[j + i - count][j - count] = sign
                        return mas[j + i - count][j - count]
                else:
                    count = 0

        for i in range(len):  # сверху главной диагонали сверху
            for j in range(len - i):
                if mas[j][i + j] == 'x':
                    count += 1
                    if count >= lvl and (j + i + 1) < len and (j + 1) < len and mas[j + 1][j + i + 1] == 0:
                        mas[j + 1][j + i + 1] = sign
                        return mas[j + 1][j + i + 1]
                else:
                    count = 0

        for i in range(len):  # сверху главной диагонали снизу
            for j in range(len - i):
                if mas[j][i + j] == 'x':
                    count += 1
                    if count >= lvl and (j + i - count) >= 0 and (j - count) >= 0 and mas[j - count][
                        j + i - count] == 0:
                        mas[j - count][j + i - count] = sign
                        return mas[j - count][j + i - count]
                else:
                    count = 0

        for n in range(len - 1, 8, -1):
            count = 0  # побочная диагональ снизу
            for i in range(len):
                if mas[i][n - i] == 'x':
                    count += 1
                    if count >= lvl and (i + 1) < len and (n - i - 1) < len and mas[i + 1][n - i - 1] == 0:
                        mas[i + 1][n - i - 1] = sign
                        return mas[i + 1][n - i - 1]
                else:
                    count = 0

        for n in range(len - 1, 8, -1):
            count = 0  # побочная диагональ сверху
            for i in range(len):
                if mas[i][n - i] == 'x':
                    count += 1
                    if count >= lvl and (i - count) >= 0 and (n - i + count) < len and mas[i - count][
                        n - i + count] == 0:
                        mas[i - count][n - i + count] = sign
                        return mas[i - count][n - i + count]
                else:
                    count = 0

        for n in range(1, len, 1):  # побочная диагональ под снизу
            for i in range(len - n):
                if mas[i + n][len - 1 - i] == 'x':
                    count += 1
                    if count >= lvl and (i + n + 1) < len and (len - 2 - i) < len and mas[i + n + 1][len - 2 - i] == 0:
                        mas[i + n + 1][len - 2 - i] = sign
                        return mas[i + n + 1][len - 2 - i]
                else:
                    count = 0

        for n in range(1, len, 1):  # побочная диагональ под сверху
            for i in range(len - n):
                if mas[i + n][len - 1 - i] == 'x':
                    count += 1
                    if count >= lvl and (i + n - count) >= 0 and (len - 1 - i + count) < len and \
                            mas[i + n - count][len - 1 - i + count] == 0:
                        mas[i + n - count][len - 1 - i + count] = sign
                        return mas[i + n - count][len - 1 - i + count]
                else:
                    count = 0

        for n in range(len - 1, 1, -1):  # побочная диагональ над снизу
            for i in range(n):
                if mas[i][n - 1 - i] == 'x':
                    count += 1
                    if count >= lvl and (i + 1) >= 0 and (n - 2 - i) >= 0 and mas[i + 1][n - 2 - i] == 0:
                        mas[i + 1][n - 2 - i] = sign
                        return mas[i + 1][n - 2 - i]
                else:
                    count = 0

        for n in range(len - 1, 1, -1):  # побочная диагональ над сверху
            for i in range(n):
                if mas[i][n - 1 - i] == 'x':
                    count += 1
                    if count >= lvl and (i - count) >= 0 and (n - 1 - i + count) < (len - 1) and mas[i - count][
                        n - 1 - i + count] == 0:
                        mas[i - count][n - 1 - i + count] = sign
                        return mas[i - count][n - 1 - i + count]
                else:
                    count = 0


def computer_win(mas, sign, signx):
    for i in range(len):
        for j in range(len):
            if mas[i][j] == signx:
                count += 1
                if count == kol and (j + 1) < len and mas[i][j + 1] == 0:
                    mas[i][j + 1] = 'o'
                    return mas[i][j + 1]
            else:
                count = 0

    for i in range(len):
        for j in range(len):
            if mas[i][j] == signx:
                count += 1
                if count == kol and (j - count) >= 0 and mas[i][j - count] == 0:
                    mas[i][j - count] = 'o'
                    return mas[i][j - count]
            else:
                count = 0

    for i in range(len):
        for j in range(len):
            if mas[j][i] == signx:
                count += 1
                if count == kol and (j + 1) < len and mas[j + 1][i] == 0:
                    mas[j + 1][i] = 'o'
                    return mas[j + 1][i]
            else:
                count = 0

    for i in range(len):
        for j in range(len):
            if mas[j][i] == signx:
                count += 1
                if count == kol and (j - count) >= 0 and mas[j - count][i] == 0:
                    mas[j - count][i] = 'o'
                    return mas[j - count][i]
            else:
                count = 0

    for i in range(len):  # низ главной диагонали
        for j in range(len - i):
            if mas[j + i][j] == signx:
                count += 1
                if count >= kol and (j + i + 1) < len and (j + 1) < len and mas[j + i + 1][j + 1] == 0:
                    mas[j + i + 1][j + 1] = 'o'
                    return mas[j + i + 1][j + 1]
            else:
                count = 0

    for i in range(len):  # низ главной диагонали
        for j in range(len - i):
            if mas[j + i][j] == signx:
                count += 1
                if count >= kol and (j + i - count) >= 0 and (j - count) >= 0 and mas[j + i - count][
                    j - count] == 0:
                    mas[j + i - count][j - count] = 'o'
                    return mas[j + i - count][j - count]
            else:
                count = 0

    for i in range(len):  # сверху главной диагонали
        for j in range(len - i):
            if mas[j][i + j] == signx:
                count += 1
                if count == kol and (j + i + 1) < len and (j + 1) < len and mas[j + 1][j + i + 1] == 0:
                    mas[j + 1][j + i + 1] = 'o'
                    return mas[j + 1][j + i + 1]
            else:
                count = 0

    for i in range(len):  # сверху главной диагонали
        for j in range(len - i):
            if mas[j][i + j] == signx:
                count += 1
                if count == kol and (j + i - count) >= 0 and (j - count) >= 0 and mas[j - count][
                    j + i - count] == 0:
                    mas[j - count][j + i - count] = 'o'
                    return mas[j - count][j + i - count]
            else:
                count = 0

    for n in range(len - 1, 8, -1):
        count = 0  # побочная диагональ
        for i in range(len):
            if mas[i][n - i] == signx:
                count += 1
                if count == kol and (i + 1) < len and (n - i - 1) < len and mas[i + 1][n - i - 1] == 0:
                    mas[i + 1][n - i - 1] = 'o'
                    return mas[i + 1][n - i - 1]
            else:
                count = 0

    for n in range(len - 1, 8, -1):
        count = 0  # побочная диагональ
        for i in range(len):
            if mas[i][n - i] == signx:
                count += 1
                if count == kol and (i - count) >= 0 and (n - i + count) < len and mas[i - count][
                    n - i + count] == 0:
                    mas[i - count][n - i + count] = 'o'
                    return mas[i - count][n - i + count]
            else:
                count = 0

    for n in range(1, len, 1):  # побочная диагональ снизу
        for i in range(len - n):
            if mas[i + n][len - 1 - i] == signx:
                count += 1
                if count == kol and (i + n + 1) < len and (len - 2 - i) < len and mas[i + n + 1][len - 2 - i] == 0:
                    mas[i + n + 1][len - 2 - i] = 'o'
                    return mas[i + n + 1][len - 2 - i]
            else:
                count = 0

    for n in range(1, len, 1):  # побочная диагональ снизу
        for i in range(len - n):
            if mas[i + n][len - 1 - i] == signx:
                count += 1
                if count == kol and (i + n - count) >= 0 and (len - 1 - i + count) < len and mas[i + n - count][
                    len - 1 - i + count] == 0:
                    mas[i + n - count][len - 1 - i + count] = 'o'
                    return mas[i + n - count][len - 1 - i + count]
            else:
                count = 0

    for n in range(len - 1, 1, -1):  # побочная диагональ сверху
        for i in range(n):
            if mas[i][n - 1 - i] == signx:
                count += 1
                if count == kol and (i + 1) >= 0 and (n - 2 - i) >= 0 and mas[i + 1][n - 2 - i] == 0:
                    mas[i + 1][n - 2 - i] = 'o'
                    return mas[i + 1][n - 2 - i]
            else:
                count = 0

    for n in range(len - 1, 1, -1):  # побочная диагональ сверху
        for i in range(n):
            if mas[i][n - 1 - i] == signx:
                count += 1
                if count == kol and (i - count) >= 0 and (n - 1 - i + count) < (len - 1) and mas[i - count][
                    n - 1 - i + count] == 0:
                    mas[i - count][n - 1 - i + count] = 'o'
                    return mas[i - count][n - 1 - i + count]
            else:
                count = 0

    for i in range(len):
        for j in range(len):
            if mas[i][j] == sign:
                count += 1
                if count >= 3 and (j + 1) < len and mas[i][j + 1] == 0:
                    mas[i][j + 1] = sign
                    return mas[i][j + 1]
            else:
                count = 0

    for i in range(len):
        for j in range(len):
            if mas[i][j] == sign:
                count += 1
                if count >= 3 and (j - count) >= 0 and mas[i][j - count] == 0:
                    mas[i][j - count] = sign
                    return mas[i][j - count]
            else:
                count = 0

    for i in range(len):
        for j in range(len):
            if mas[j][i] == sign:
                count += 1
                if count >= 3 and (j + 1) < len and mas[j + 1][i] == 0:
                    mas[j + 1][i] = sign
                    return mas[j][i + 1]
            else:
                count = 0

    for i in range(len):
        for j in range(len):
            if mas[j][i] == sign:
                count += 1
                if count >= 3 and (j - count) >= 0 and mas[j - count][i] == 0:
                    mas[j - count][i] = sign
                    return mas[j - count][i]
            else:
                count = 0

    for i in range(len):  # низ главной диагонали
        for j in range(len - i):
            if mas[j + i][j] == sign:
                count += 1
                if count >= 3 and (j + i + 1) < len and (j + 1) < len and mas[j + i + 1][j + 1] == 0:
                    mas[j + i + 1][j + 1] = sign
                    return mas[j + i + 1][j + 1]
            else:
                count = 0

    for i in range(len):  # низ главной диагонали
        for j in range(len - i):
            if mas[j + i][j] == sign:
                count += 1
                if count >= 3 and (j + i - count) >= 0 and (j - count) >= 0 and mas[j + i - count][j - count] == 0:
                    mas[j + i - count][j - count] = sign
                    return mas[j + i - count][j - count]
            else:
                count = 0

    for i in range(len):  # сверху главной диагонали
        for j in range(len - i):
            if mas[j][i + j] == sign:
                count += 1
                if count >= 3 and (j + i + 1) < len and (j + 1) < len and mas[j + 1][j + i + 1] == 0:
                    mas[j + 1][j + i + 1] = sign
                    return mas[j + 1][j + i + 1]
            else:
                count = 0

    for i in range(len):  # сверху главной диагонали
        for j in range(len - i):
            if mas[j][i + j] == sign:
                count += 1
                if count >= 3 and (j + i - count) >= 0 and (j - count) >= 0 and mas[j - count][j + i - count] == 0:
                    mas[j - count][j + i - count] = sign
                    return mas[j - count][j + i - count]
            else:
                count = 0

    for n in range(len - 1, 8, -1):
        count = 0  # побочная диагональ
        for i in range(len):
            if mas[i][n - i] == sign:
                count += 1
                if count >= 3 and (i + 1) < len and (n - i - 1) < len and mas[i + 1][n - i - 1] == 0:
                    mas[i + 1][n - i - 1] = sign
                    return mas[i + 1][n - i - 1]
            else:
                count = 0

    for n in range(len - 1, 8, -1):
        count = 0  # побочная диагональ
        for i in range(len):
            if mas[i][n - i] == sign:
                count += 1
                if count >= 3 and (i - count) >= 0 and (n - i + count) < len and mas[i - count][n - i + count] == 0:
                    mas[i - count][n - i + count] = sign
                    return mas[i - count][n - i + count]
            else:
                count = 0

    for n in range(1, len, 1):  # побочная диагональ снизу
        for i in range(len - n):
            if mas[i + n][len - 1 - i] == sign:
                count += 1
                if count >= 3 and (i + n + 1) < len and (len - 2 - i) < len and mas[i + n + 1][len - 2 - i] == 0:
                    mas[i + n + 1][len - 2 - i] = sign
                    return mas[i + n + 1][len - 2 - i]
            else:
                count = 0

    for n in range(1, len, 1):  # побочная диагональ снизу
        for i in range(len - n):
            if mas[i + n][len - 1 - i] == sign:
                count += 1
                if count >= 3 and (i + n - count) >= 0 and (len - 1 - i + count) < len and mas[i + n - count][
                    len - 1 - i + count] == 0:
                    mas[i + n - count][len - 1 - i + count] = sign
                    return mas[i + n - count][len - 1 - i + count]
            else:
                count = 0

    for n in range(len - 1, 1, -1):  # побочная диагональ сверху
        for i in range(n):
            if mas[i][n - 1 - i] == sign:
                count += 1
                if count >= 3 and (i + 1) >= 0 and (n - 2 - i) >= 0 and mas[i + 1][n - 2 - i] == 0:
                    mas[i + 1][n - 2 - i] = sign
                    return mas[i + 1][n - 2 - i]
            else:
                count = 0

    for n in range(len - 1, 1, -1):  # побочная диагональ сверху
        for i in range(n):
            if mas[i][n - 1 - i] == sign:
                count += 1
                if count >= 3 and (i - count) >= 0 and (n - 1 - i + count) < (len - 1) and mas[i - count][
                    n - 1 - i + count] == 0:
                    mas[i - count][n - 1 - i + count] = sign
                    return mas[i - count][n - 1 - i + count]
            else:
                count = 0
    battle(mas, 'o')
