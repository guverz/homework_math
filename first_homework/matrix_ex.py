def empty_matrix(a): #Создание пустой матрицы 
    end_f = []
    for _ in range(len(a)):
        end_f.append([])
    return end_f

def sum_matrix(a, b): #Сложение матриц
    end = empty_matrix(a)
    for j in range(len(a)):
        for i in range(len(a[0])):
            end[j].append(a[j][i] + b[j][i])
    return end

def sub_matrix(a, b): #Вычитание матриц
    end = []
    for _ in range(len(a)):
        end.append([])
    for j in range(len(a[0])):
        for i in range(len(b)):
            end[i].append(a[i][j] - b[i][j])
    return end

