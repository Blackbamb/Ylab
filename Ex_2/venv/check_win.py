def check_win(mas, sign):
    count=0
    len=10
    for i in range(len): #горизонталь
        for j in range(len):
            if mas[i][j] == sign:
                count += 1
                if count == 5:
                    return sign
            else:
                count = 0

    for i in range(len): #вертикаль
        for j in range(len):
            if mas[j][i] == sign:
                count += 1
                if count == 5:
                    return sign
            else:
                count = 0

    for i in range(len): #низ главной диагонали
        for j in range(len-i):
            if mas[j + i][j] == sign:
                count += 1
                if count == 5:
                    return sign
            else:
                count=0

    for i in range(len): #сверху главной диагонали
        for j in range(len-i):
            if mas[j][i+j] == sign:
                count += 1
                if count == 5:
                    return sign
            else:
                count=0

    for n in range(len - 1, 8, -1):
        count=0 # побочная диагональ
        for i in range(len):
            if mas[i][n - i] == sign:
                count += 1
                if count == 5:
                    return sign
            else:
                count = 0

    for n in range(1,len,1): #побочная диагональ снизу
        for i in range(len - n):
            if mas[i + n][len - 1 - i] == sign:
                count += 1
                if count == 5:
                    return sign
            else:
                count = 0

    for n in range(len-1, 1, -1):  # побочная диагональ сверху
        for i in range(n):
            if mas[i][n-1 - i] == sign:
                count += 1
                if count == 5:
                    return sign
            else:
                count = 0
    for i in range(len): #ничья
        for j in range(len):
            if mas[i][j] !=0:
                count += 1
        if count == 99:
            return 'Ничья'