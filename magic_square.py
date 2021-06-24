def square(n):
    if n%2 == 1:
        return odd_square(n)
    if n%4 == 0:
        return doubly_even_square(n)
    return singly_even_square(n)

# Siamese method
def odd_square(n):
    m = [[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            m[i][j] = (i+j-n//2)%n*n + (i+2*j+1)%n
    return m

def doubly_even_square(n):
    m = [[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            m[i][j] = i*n+j
            if (a := i%4) == (b := j%4) or a+b == 3:
                m[i][j] = n*n-m[i][j]-1
    return m

# Strachey method
def singly_even_square(n):
    m = [[None]*n for _ in range(n)]
    h = n//2
    r = odd_square(h)
    s = h*h
    for i in range(h):
        for j in range(h):
            m[i][j] = r[i][j]
            m[i][j+h] = r[i][j]+s*2
            m[i+h][j] = r[i][j]+s*3
            m[i+h][j+h] = r[i][j]+s
    q = h//2
    if q > 1:
        for i in range(h):
            m[i][-q+1:], m[i+h][-q+1:] = m[i+h][-q+1:], m[i][-q+1:]
    for i in range(h):
        m[i][:q], m[i+h][:q] = m[i+h][:q], m[i][:q]
    m[q][0], m[q+h][0] = m[q+h][0], m[q][0]
    m[q][q], m[q+h][q] = m[q+h][q], m[q][q]
    return m

print(square(3))
print(square(4))
print(square(5))
print(square(6))
