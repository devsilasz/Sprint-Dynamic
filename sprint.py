import random
from datetime import datetime, timedelta

nomes_insumos = ["Reagente A", "Reagente B", "Descartável X", "Descartável Y", "Kit Z"]

consumos = []
data_base = datetime.today()

for i in range(10):
    insumo = random.choice(nomes_insumos)
    quantidade = random.randint(1, 20)
    validade = data_base + timedelta(days=random.randint(5, 30))
    consumos.append({"data": data_base + timedelta(days=i),
                     "insumo": insumo,
                     "quantidade": quantidade,
                     "validade": validade})

# FILA
class Fila:
    def __init__(self):
        self.itens = []

    def adicionar(self, dado):
        self.itens.append(dado)

    def retirar(self):
        if not self.vazia():
            return self.itens.pop(0)

    def vazia(self):
        return len(self.itens) == 0

# PILHA
class Pilha:
    def __init__(self):
        self.itens = []

    def adicionar(self, dado):
        self.itens.append(dado)

    def retirar(self):
        if not self.vazia():
            return self.itens.pop()

    def vazia(self):
        return len(self.itens) == 0

# BUSCA SEQUENCIAL
def busca_sequencial(lista, alvo):
    for item in lista:
        
        if item["insumo"] == alvo:
            return item
    return None

# BUSCA BINÁRIA (lista ordenada)
def busca_binaria(lista, alvo):
    inicio, fim = 0, len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio]["insumo"] == alvo:
            return lista[meio]
        elif lista[meio]["insumo"] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return None

# MERGE SORT
def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista)//2
        esquerda = lista[:meio]
        direita = lista[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i]["quantidade"] < direita[j]["quantidade"]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

# QUICK SORT
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[0]
        menores = [x for x in lista[1:] if x["validade"] <= pivo["validade"]]
        maiores = [x for x in lista[1:] if x["validade"] > pivo["validade"]]
        return quick_sort(menores) + [pivo] + quick_sort(maiores)

# RESULTADOS
print("\n--- FILA ---")
fila = Fila()
for c in consumos:
    fila.adicionar(c)

while not fila.vazia():
    item = fila.retirar()
    print(f"Data: {item['data'].strftime('%d/%m/%Y')} | "
          f"Insumo: {item['insumo']} | "
          f"Quantidade: {item['quantidade']} | "
          f"Validade: {item['validade'].strftime('%d/%m/%Y')}")

print("\n--- PILHA ---")
pilha = Pilha()
for c in consumos:
    pilha.adicionar(c)

while not pilha.vazia():
    item = pilha.retirar()
    print(f"Data: {item['data'].strftime('%d/%m/%Y')} | "
          f"Insumo: {item['insumo']} | "
          f"Quantidade: {item['quantidade']} | "
          f"Validade: {item['validade'].strftime('%d/%m/%Y')}")

print("\n--- BUSCA SEQUENCIAL ---")
item = busca_sequencial(consumos, "Reagente A")
if item:
    print(f"Data: {item['data'].strftime('%d/%m/%Y')} | "
          f"Insumo: {item['insumo']} | "
          f"Quantidade: {item['quantidade']} | "
          f"Validade: {item['validade'].strftime('%d/%m/%Y')}")
else:
    print("Insumo não encontrado.")

print("\n--- BUSCA BINÁRIA ---")
ordenada_por_nome = sorted(consumos, key=lambda x: x["insumo"])
item = busca_binaria(ordenada_por_nome, "Kit Z")
if item:
    print(f"Data: {item['data'].strftime('%d/%m/%Y')} | "
          f"Insumo: {item['insumo']} | "
          f"Quantidade: {item['quantidade']} | "
          f"Validade: {item['validade'].strftime('%d/%m/%Y')}")
else:
    print("Insumo não encontrado.")

print("\n--- MERGE SORT ---")
merge_sort(consumos)
for c in consumos:
    print(f"Data: {c['data'].strftime('%d/%m/%Y')} | "
          f"Insumo: {c['insumo']} | "
          f"Quantidade: {c['quantidade']} | "
          f"Validade: {c['validade'].strftime('%d/%m/%Y')}")

print("\n--- QUICK SORT ---")
ordenados_validade = quick_sort(consumos)
for c in ordenados_validade:
    print(f"Data: {c['data'].strftime('%d/%m/%Y')} | "
          f"Insumo: {c['insumo']} | "
          f"Quantidade: {c['quantidade']} | "
          f"Validade: {c['validade'].strftime('%d/%m/%Y')}")
