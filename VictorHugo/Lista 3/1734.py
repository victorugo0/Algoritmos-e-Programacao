# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734

N = int(input())
valorN = N
fatorial = N


if N == 0:
    fatorial = 1
while N > 1:
    fatorial = fatorial * (N - 1)

    N = N - 1

print("%i! = %i" % (valorN, fatorial))