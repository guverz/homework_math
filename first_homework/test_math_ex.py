import math_ex as me
def test_sum_vector():
    v1 = [5, 7, 3]
    v2 = [3, 1, 2]
    exp = [8, 8, 5]
    res = me.sum_vector(v1,v2)
    assert res == exp

def test_sub_vector():
    v1 = [5, 7, 3]
    v2 = [3, 1, 2]
    exp = [2, 6, 1]
    res = me.sub_vector(v1,v2)
    assert res == exp

def test_mult_scal_vector():
    v1 = [5, 7, 3]
    s = 2
    exp = [10, 14, 6]
    res = me.mult_scal_vector(v1,s)
    assert res == exp

def test_div_scal_vector():
    v1 = [5, 7, 3]
    s = 2
    exp = [2.5, 3.5, 1.5]
    res = me.div_scal_vector(v1,s)
    assert res == exp

def test_scal_prod_vectors():
    v1 = [5, 7, 3]
    v2 = [3, 1, 2]
    exp = 28
    res = me.scal_prod_vectors(v1,v2)
    assert res == exp

def test_vector_collin():
    v1 = [2, 4, 6, 8]
    v2 = [4, 8, 12, 16]
    exp = True
    res = me.vector_collin(v1,v2)
    assert res == exp

def test_codirect_vectors():
    v1 = [2, 4, 6, 8]
    v2 = [4, 8, 12, 16]
    exp = True
    res = me.codirect_vectors(v1,v2)
    assert res == exp

def test_codirect_almost_vectors():
    v1 = [2, 4, 6, 8.2]
    v2 = [4, 8, 12, 16]
    e = 0.0001
    exp = True
    res = me.codirect_almost_vectors(v1, v2, e)
    assert res == exp 


def test_oppos_vectors():
    v1 = [2, 4, 6, 8]
    v2 = [-4, -8, -12, -16]
    exp = True
    res = me.oppos_vectors(v1,v2)
    assert res == exp

def test_oppos_almost_vectors():
    v1 = [-2, -4, -6, -8.2]
    v2 = [4, 8, 12, 16]
    e = 0.0001
    exp = True
    res = me.oppos_almost_vectors(v1, v2, e)
    assert res == exp 

def test_vectors_equality():
    v1 = [2, 4, 6, 8]
    v2 = [2, 4, 6, 8]
    exp = True
    res = me.vectors_equality(v1,v2)
    assert res == exp

def test_vectors_orthogon():
    v1 = [1, 2, 0]
    v2 = [2, -1, 10]
    exp = True
    res = me.vectors_orthogon(v1,v2)
    assert res == exp

def test_vector_length():
    v1 = [2, 4, -4, 0]
    exp = 6
    res = me.vector_length(v1)
    assert res == exp

def test_norm_vector():
    v1 = [0, 2]
    exp = [0, 1]
    res = me.norm_vector(v1)
    assert res == exp

def test_change_direct_vector():
    v1 = [6, 3, 1, -2]
    exp = [-6, -3, -1, 2]
    res = me.change_direct_vector(v1)
    assert res == exp

def test_angle_between_vectors():
    v1 = [5, 2, 6]
    v2 = [4, 3, 0]
    exp = 0.8697984039061518
    res = me.angle_between_vectors(v1,v2)
    assert res == exp

def test_cos_between_vectors():
    v1 = [5, 2, 6]
    v2 = [4, 3, 0]
    exp = 0.644980619863884
    res = me.cos_between_vectors(v1,v2)
    assert res == exp

def test_scal_projection_vectors():
    v1 = [5, 7, 3]
    v2 = [3, 1, 2]
    exp = 7.483314773547883
    res = me.scal_projection_vectors(v1, v2)
    assert res == exp

def test_vector_projection_vectors():
    v1 = [4, 5]
    v2 = [6, 0]
    exp = [4, 0]
    res = me.vector_projection_vectors(v1,v2)
    assert res == exp

def test_vector_almost_equality():
    v1 = [2.1, 0.9]
    v2 = [2.3, 0.9]
    e = 0.2
    exp = True
    res = me.vector_almost_equality(v1, v2, e)
    assert res == exp