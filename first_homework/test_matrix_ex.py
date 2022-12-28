import matrix_ex as mxe
def test_sum_matrix():
    a = [[1, 2, 3], [3, 2, 1]]
    b = [[3, 2, 1], [1, 2, 5]]
    exp = [[4, 4, 4], [4, 4, 6]]
    res = mxe.sum_matrix(a,b)
    assert res == exp

def test_sub_matrix():
    a = [[1, 2, 3], [3, 2, 1]]
    b = [[3, 2, 1], [1, 2, 5]]
    exp = [[-2, 0, 2], [2, 0, -4]]
    res = mxe.sub_matrix(a,b)
    assert res == exp

def test_matrix_trans():
    a = [[1, 2, 3], [3, 4, 5]]
    exp = [[1, 3], [2, 4], [3, 5]]
    res = mxe.matrix_trans(a)
    assert res == exp

def test_mult_matrix_skal():
    a = [[1, 2, 3], [3, 4, 5]]
    s = 2
    exp = [[2, 4, 6], [6, 8, 10]]
    res = mxe.mult_matrix_skal(a, s)
    assert res == exp

def test_get_row_i():
    a = [[1, 2, 3], [3, 4, 5]]
    n = 1
    exp = [3, 4, 5]
    res = mxe.get_row_i(a, n)
    assert res == exp

def test_get_col_i():
    a = [[1, 2, 3], [3, 4, 5]]
    n = 1
    exp = [2, 4]
    res = mxe.get_col_i(a, n)
    assert res == exp

def test_row_replacement():
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    n = 0
    n2 = 2
    exp = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [10, 11, 12]]
    res = mxe.row_replacement(a, n, n2)
    assert res == exp

def test_row_skal_mult():
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    n = 0
    s = 4
    exp = [[4, 8, 12], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    res = mxe.row_skal_mult(a, n, s)
    assert res == exp

def test_row_inserting():
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    n = 0
    end = mxe.empty_matrix(a)
    exp = [[1, 2, 3], [], [], []]
    res = mxe.row_inserting(a, end, n)
    assert res == exp

def test_mult_of_sum_matrix():
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    n1 = 0
    n = 2
    s = 2
    exp = [[1, 2, 3], [4, 5, 6], [9, 12, 15], [10, 11, 12]]
    res = mxe.mult_of_sum_matrix(a, s, n, n1)
    assert res == exp

def test_mult_of_sub_matrix():
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    n1 = 0
    n = 2
    s = 2
    exp = [[1, 2, 3], [4, 5, 6], [5, 4, 3], [10, 11, 12]]
    res = mxe.mult_of_sub_matrix(a, s, n, n1)
    assert res == exp

def test_matrix_mult():
    a = [[1], [2], [3]]
    b = [[2, 4]]
    exp = [[2, 4], [4, 8], [6, 12]]
    res = mxe.matrix_mult(a, b)
    assert res == exp