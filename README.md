# Mini-RPC com FIFOs em Python

Este projeto implementa um sistema simples de RPC (Request–Reply) usando pipes nomeados (FIFOs) no Linux.

## 📁 Arquivos

- `servidor.py`: Servidor que recebe requisições e envia respostas.
- `cliente.py`: Cliente com entrada manual pelo teclado.
- `cliente_auto.py`: Cliente automático que envia operações com números aleatórios.

## 🚀 Como Executar

### 1. Extraia os arquivos
```bash
unzip lab_mini_rpc_com_readme.zip
cd lab_mini_rpc_com_readme
```

### 2. Execute o servidor
Em um terminal:
```bash
python3 servidor.py
```

### 3. Execute um cliente manual
Em outro terminal:
```bash
python3 cliente.py
```
Digite, por exemplo: `soma 4 9`

### 4. Execute um cliente automático
Em outro terminal:
```bash
python3 cliente_auto.py soma
python3 cliente_auto.py sub
python3 cliente_auto.py fat
```

### 🧹 Limpando FIFOs
Caso os FIFOs já existam ou ocorra erro de permissão, remova com:
```bash
rm /tmp/rpc_req_fifo /tmp/rpc_resp_*
```

---

Desenvolvido para fins didáticos.