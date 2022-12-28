import matrix_ex as mxe
def first_stuff(a, n):
    for i in range(len(a)):
        for j in range((len(mxe.get_col_i(a, i)))):
            if mxe.get_col_i(a, i)[j] > 0:

            
