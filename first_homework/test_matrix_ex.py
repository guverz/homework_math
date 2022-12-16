import matrix_ex as mxe
def test_sum_matrix():
    a = [[1, 2, 3],[3, 2, 1]]
    b = [[3, 2, 1],[1, 2, 5]]
    exp = [[4, 4, 4], [4, 4, 6]]
    res = mxe.sum_matrix(a,b)
    assert res == exp

def test_sub_matrix():
    a = [[1, 2, 3],[3, 2, 1]]
    b = [[3, 2, 1],[1, 2, 5]]
    exp = [[-2, 0, 2], [2, 0, -4]]
    res = mxe.sub_matrix(a,b)
    assert res == exp