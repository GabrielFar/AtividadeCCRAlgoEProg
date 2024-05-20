# Atividade 10
def combinar(n, p):
  n_fator = fatorial(n)
  p_fator = fatorial(p)
  np_fator = fatorial(n - p)
  return n_fator/(p_fator*np_fator)

def fatorial(x):
  soma = 1
  for i in range(x, 1, -1):
    soma *= i
  return soma

n, p = map(int, input("Digite dois números: ").split())
print(f"{(combinar(n, p)):.2f}")