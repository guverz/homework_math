import math_ex as me
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
    end = empty_matrix(a)
    for j in range(len(a[0])):
        for i in range(len(b)):
            end[i].append(a[i][j] - b[i][j])
    return end

def matrix_trans(a): #Транспонирование матриц
    return [
        list(end)
        for end in zip(*a)
    ]

def mult_matrix_skal(a, s): #Умножение матриц на скаляр
    end = empty_matrix(a)
    for i in range(len(a)):
        #me.mult_scal_vector(a[i], s)
        for j in range(len((a)[i])):
            end[i].append(a[i][j] * s)
    return end

def get_row_i(a, n): #Получение строки по индексу
    return a[n]

def get_col_i(a, n): #Получение столбца по индексу
    return get_row_i(matrix_trans(a), n)

def row_replacement(a, n, n2): #Перестановка строк n - индекс 1-й строки для замены, n2 - индекс 2-й строки для замены
    end = empty_matrix(a)
    for k in range(len(get_row_i(a, n))):
        end[n2].append((get_row_i(a, n)[k]))
        end[n].append((get_row_i(a, n2)[k]))   
    for i in range(len(a)):
        if i != n2 and i != n:
            for j in range(len(a[i])):
                end[i].append((get_row_i(a, i)[j]))
    return end


def row_skal_mult(a, n, s): #Умножение строки матрицы на скаляр
    end = empty_matrix(a)
    for k in range(len(get_row_i(a, n))):
        end[n].append((me.mult_scal_vector(get_row_i(a, n), s)[k]))
    for i in range(len(a)):
        if i != n:
            for j in range(len(a[i])):
                end[i].append((get_row_i(a, i)[j]))
    return end

#def row_inserting(a, end, n):
#    for k in range(len(a[n])):
#        end[n].append((a[n][k]))
#    return end

#def wondering(a):
#    for n in range(len(a)):
#        end = row_inserting(a, end1, n)
#    return end

#a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
#end1 = empty_matrix(a)
#print(wondering)

def mult_of_sum_matrix(a, s, n, n1): #Сложение строк, умноженных на число (n - строка из которой вычитаем строку n1 * s)    
    end = empty_matrix(a)
    for k in range(len(get_row_i(a, n))):
        end[n].append((me.sum_vector(get_row_i(a, n), me.mult_scal_vector(get_row_i(a, n1), s))[k]))
    for i in range(len(a)):
        if i != n:
            for j in range(len(a[i])):
                end[i].append((get_row_i(a, i)[j]))
    return end

def mult_of_sub_matrix(a, s, n, n1): #Bычитание строк, умноженных на число (n - строка из которой вычитаем строку n1 * s)    
    end = empty_matrix(a)
    for k in range(len(get_row_i(a, n))):
        end[n].append((me.sub_vector(get_row_i(a, n), me.mult_scal_vector(get_row_i(a, n1), s))[k]))
    for i in range(len(a)):
        if i != n:
            for j in range(len(a[i])):
                end[i].append((get_row_i(a, i)[j]))
    return end

def empty_matrix_for_mult(a, b): #Создание пустой матрицы для умножения матриц
    m = len(a)                                                                                        
    k = len(b[0])
    return [[None for __ in range(k)] for __ in range(m)] 

def matrix_mult(a, b): #Умножение матриц
    end = empty_matrix_for_mult(a, b)
    print(end)
    for i in range(len(a)):
        for j in range(len(b[0])):       
            end[i][j] = sum(a[i][m] * b[m][j] for m in range(len(b)))
    return end
