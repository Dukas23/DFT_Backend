

def ordenar(lista):
    izquierda = []
    derecha = []
    for num in lista:
        if num is not None:
            if num % 2 == 0:
                izquierda.append(num)
            else:
                derecha.append(num)
    return izquierda + derecha


def factorial(n):
    if (n == 0 or n == 1):
        return 1
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


def taylor_seno(x, n):
    sen = 0
    for i in range(0, n):
        sen += ((-1)**i * x**(2*i+1)) / factorial(2*i+1)
    return sen


def taylor_coseno(x, n):
    cos = 0
    for i in range(0, n):
        cos += ((-1)**i * x**(2*i)) / factorial(2*i)
    return cos


def dft(lista):

    n = len(lista)
    vect = [0] * n

    if n == 1:
        vect[0] = lista[0]
        return vect

    par = []
    impar = []

    for i in range(n):
        if i % 2 == 0:
            par.append(lista[i])
        else:
            impar.append(lista[i])

    par_dft = dft(par)
    impar_dft = dft(impar)
    pi = 3.1415926535897932384
    for m in range(n // 2):
        theta = 2 * pi * m / n
        w_re = taylor_coseno(theta, n)
        w_im = -taylor_seno(theta, n)

        z_re = w_re * impar_dft[m].real - w_im * impar_dft[m].imag
        z_im = w_re * impar_dft[m].imag + w_im * impar_dft[m].real

        vect[m] = par_dft[m] + complex(z_re, z_im)
        vect[m + n // 2] = par_dft[m] - complex(z_re, z_im)

    return vect
