import os

SERVER_FIFO = "/tmp/rpc_req_fifo"
CLIENT_FIFO = f"/tmp/rpc_resp_{os.getpid()}"

if not os.path.exists(CLIENT_FIFO):
    os.mkfifo(CLIENT_FIFO, 0o600)

entrada = input("Digite a operação e os parâmetros (ex: soma 3 5): ")
partes = entrada.split()
operacao = partes[0]
parametros = ",".join(partes[1:])

mensagem = f"{CLIENT_FIFO}|{operacao}|{parametros}\n"

with open(SERVER_FIFO, "w") as server:
    server.write(mensagem)
    server.flush()

with open(CLIENT_FIFO, "r") as resp:
    resultado = resp.readline().strip()
    print("Resultado:", resultado)

os.remove(CLIENT_FIFO)