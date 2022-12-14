import math
def sum_vector(v1, v2): #Сумма векторов
    end = []
    for i in range(len(v1)):
        b = int(v1[i]) + int(v2[i])
        end.append(b)
        b = 0
    return end

def sub_vector(v1, v2): #Разность векторов
    end = []
    for i in range(len(v1)):
        b = int(v1[i]) - int(v2[i])
        end.append(b)
        b = 0
    return end

def mult_scal_vector(v1, s): #Умножение вектора на скаляр
    end = []
    for i in range(len(v1)):
        b = int(v1[i]) * s
        end.append(b)
        b = 0
    return end

def div_scal_vector(v1, s): #Деление вектора на скаляр
    end = []
    for i in range(len(v1)):
        b = int(v1[i]) / s
        end.append(b)
        b = 0
    return end

def scal_prod_vectors(v1, v2): #Скалярное произведение векторов
    int_end = 0
    for i in range(len(v1)):        
        b = int(v1[i]) * int(v2[i])
        int_end += b
        b = 0
    return int_end

def vector_collin(v1, v2): #Коллинеарность векторов
    k = 1
    c = v1[0] / v2[0]
    for i in range(1, len(v1)):
        if v1[i] / v2[i] == c:
            k += 1
    if k == len(v1):
        return True
    else:
        return False

def codirect_vectors(v1, v2): #Сонаправленные вектора
    k = 1
    c = v1[0] / v2[0]
    if vector_collin(v1, v2) == True and c > 0:
        return True
    else:
        return False

def oppos_vectors(v1, v2): #Противоположнонаправленные вектора
    k = 1
    c = v1[0] / v2[0]
    if vector_collin(v1, v2) == True and c < 0:
        return True
    else:
        return False

def vectors_equality(v1, v2): #Равенство векторов
    k = 0 
    for i in range(len(v1)):
        if v1[i] == v2[i]:
            k += 1
    if k == len(v1):
        return True
    else:
        return False

def vectors_orthogon(v1, v2): #Ортогональность векторов
    if scal_prod_vectors(v1,v2) == 0:
        return True
    else:
        return False

def vector_length(v1): #Длина вектора
    int_end = 0
    for i in range(len(v1)):
        int_end += v1[i] ** 2
    return abs(math.sqrt(int_end))

def norm_vector(v1): #Нормировка вектора
    end = []
    for i in range(len(v1)):
        b = v1[i] / vector_length(v1)
        end.append(b)
        b = 0
    return end

def change_direct_vector(v1): #Изменение направления вектора на противоположный
    end = []
    for i in range(len(v1)):
        b = v1[i] * -1
        end.append(b)
        b = 0
    return end

def cos_between_vectors(v1, v2): #Косинус между векторами
    return scal_prod_vectors(v1, v2) / (vector_length(v1) * vector_length(v2))

def angle_between_vectors(v1, v2): #Угол между векторами
    return math.acos(cos_between_vectors(v1, v2))

def scal_projection_vectors(v1, v2): #Скалярная проекция вектора на вектор
    return scal_prod_vectors(v1, v2) / vector_length(v2)

def vector_projection_vectors(v1, v2): #Векторная проекция вектора на вектор    
    end = []
    for i in range(len(v2)):
        b = v2[i] * scal_projection_vectors(v1, v2) / vector_length(v2)
        end.append(b)
        b = 0
    return end







    
