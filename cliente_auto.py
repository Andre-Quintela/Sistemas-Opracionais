import os
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("operacao", choices=["soma", "sub", "mul", "div", "fat"])
args = parser.parse_args()

SERVER_FIFO = "/tmp/rpc_req_fifo"
CLIENT_FIFO = f"/tmp/rpc_resp_{os.getpid()}"

if not os.path.exists(CLIENT_FIFO):
    os.mkfifo(CLIENT_FIFO, 0o600)

if args.operacao == "fat":
    parametros = str(random.randint(1, 10))
else:
    a, b = random.randint(1, 100), random.randint(1, 100)
    parametros = f"{a},{b}"

mensagem = f"{CLIENT_FIFO}|{args.operacao}|{parametros}\n"

with open(SERVER_FIFO, "w") as server:
    server.write(mensagem)
    server.flush()

with open(CLIENT_FIFO, "r") as resposta:
    resultado = resposta.readline().strip()
    print(f"Resultado de {args.operacao}({parametros}) = {resultado}")

os.remove(CLIENT_FIFO)