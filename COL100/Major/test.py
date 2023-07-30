class BinaryMatrix(object):
    def __init__(self, mat) :
        self.mat = mat
    
    def __mul__(self, other):
        R = len(self.mat)
        C = len(self.mat[0])
        B = len(other.mat[0])
        m = [[0]*B for _ in range(R)]
        for i in range(R):
            for j in range(B):
                for k in range(C):
                    m[i][j] += self.mat[i][k]*other.mat[k][j]
                m[i][j] %= 2
        return BinaryMatrix(m)
    
class ColumnMajorSparseMatrix(BinaryMatrix):
    def __init__(self, sparse_mat, n, m):
        self.sparse_mat, self.n, self.m = sparse_mat, n, m

    def get_full_mat_from_sparse(self, sparse_matrix):
        matr = [[0]*sparse_matrix.m for _ in range(sparse_matrix.n)]
        for i in sparse_matrix.sparse_mat.keys():
            for j in sparse_matrix.sparse_mat[i]:
                matr[j][i] = 1

        return BinaryMatrix(matr)
    
    def get_sparse_repr_from_fullmat(self, bin_matrix):
        d = {}
        k = bin_matrix.mat
        R = len(k)
        C = len(k[0])

        for i in range(C):
            d[i] = []
            for j in range(R):
                if k[j][i] == 1:
                    d[i].append(j)
            if d[i] == []:
                del d[i]
        return ColumnMajorSparseMatrix(d,R,C)

    def __mul__(self, other):
        a = self.get_full_mat_from_sparse(self.sparse_mat)
        b = other.get_full_mat_from_sparse(other.sparse_mat)
        c = BinaryMatrix.__mul__(a,b)

        return c

mat1 = [[1,1],[0,0],[0,1]]
mat2 = [[1,1,0],[0,1,0]]

m1 = BinaryMatrix(mat1)
m2 = BinaryMatrix(mat2)
m3 = m1*m2

s1 = ColumnMajorSparseMatrix(m1, len(m1.mat), len(m1.mat[0]))
s2 = ColumnMajorSparseMatrix(m2, len(m2.mat), len(m2.mat[0]))

spa1 = (s1.get_sparse_repr_from_fullmat(m1))
spa2 = (s2.get_sparse_repr_from_fullmat(m2))

full1 = s1.get_full_mat_from_sparse(spa1)
full2 = s2.get_full_mat_from_sparse(spa2)

print(m1.mat)
print(spa1.sparse_mat)
print(full1.mat)
print()
print(m2.mat)
print(spa2.sparse_mat)
print(full2.mat)
print()
print(m3.mat)
print(s1.__mul__(s2))