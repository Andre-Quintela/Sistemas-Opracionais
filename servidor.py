import os
import math

SERVER_FIFO = "/tmp/rpc_req_fifo"

def soma(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Divisão por zero"
def fat(a): return math.factorial(a)

OPERACOES = {
    "soma": soma,
    "sub": sub,
    "mul": mul,
    "div": div,
    "fat": fat,
}

if not os.path.exists(SERVER_FIFO):
    os.mkfifo(SERVER_FIFO, 0o600)

print("Servidor ativo...")

while True:
    with open(SERVER_FIFO, "r") as fifo:
        linha = fifo.readline().strip()
        if not linha:
            continue

        try:
            resp_fifo, operacao, parametros = linha.split("|")
            args = list(map(int, parametros.split(",")))

            if operacao in OPERACOES:
                resultado = OPERACOES[operacao](*args)
            else:
                resultado = "Operação inválida"

            with open(resp_fifo, "w") as cliente:
                cliente.write(str(resultado) + "\n")
                cliente.flush()
        except Exception as e:
            print("Erro:", e)