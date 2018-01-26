
def karatsuba(x,y):
    if x < 10 or y < 10:
        return x*y
    sx = str(x)
    sy = str(y)
    nx = len(sx)
    ny = len(sy)
    n = round(max(nx,ny)/2)*2 #it goes to first even number > max(nx,ny)
    
    sx = '0'*(n-nx) + sx #pad 0s to n
    sy = '0'*(n-ny) + sy
    
    #split
    a = int(sx[0:n//2])
    b = int(sx[n//2:])
    c = int(sy[0:n//2])
    d = int(sy[n//2:])
    
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    abcd = karatsuba(a+b, c+d)
    adbc = abcd - ac - bd
    return 10**n * ac + 10**(n//2) *adbc + bd