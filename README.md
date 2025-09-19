# Sistema de Controle de Consumo de Insumos

## O Problema

Imagine que você trabalha em um laboratório de diagnóstico e precisa controlar o estoque de reagentes e materiais descartáveis. O problema é que o consumo diário desses insumos não está sendo registrado direito, o que complica muito a vida na hora de saber quando comprar mais material ou se vai faltar algo importante.

É exatamente isso que este projeto resolve: um sistema que simula o controle de consumo de insumos usando estruturas de dados e algoritmos clássicos da programação.

## Como Funciona

O sistema gera dados simulados de consumo diário (como se fossem registros reais de um laboratório) e depois aplica diferentes técnicas de programação para organizar e consultar essas informações de forma eficiente.

## As Estruturas e Algoritmos Usados

### 1. Fila (FIFO - First In, First Out)

**O que é:** Uma fila funciona como uma fila de banco - quem chega primeiro, é atendido primeiro.

**Por que usar aqui:** No controle de insumos, faz sentido processar os consumos na ordem cronológica que aconteceram. Assim você consegue ver o histórico completo do que foi usado dia após dia.

**Como funciona no código:** Cada registro de consumo é adicionado na fila conforme acontece. Quando você consulta, os dados saem na mesma ordem que entraram, mostrando a sequência temporal dos consumos.

### 2. Pilha (LIFO - Last In, First Out)

**O que é:** Uma pilha funciona como uma pilha de pratos - o último prato colocado é o primeiro a ser retirado.

**Por que usar aqui:** Às vezes você quer ver os consumos mais recentes primeiro, como quando precisa verificar o que foi usado hoje ou ontem rapidamente.

**Como funciona no código:** Os registros são empilhados, e quando você consulta, vê primeiro os consumos mais recentes, depois os mais antigos.

### 3. Busca Sequencial

**O que é:** É como procurar um nome na lista telefônica folheando página por página até encontrar.

**Por que usar aqui:** Quando você tem uma lista pequena de insumos e quer encontrar um específico, a busca sequencial é simples e direta.

**Como funciona no código:** O sistema percorre cada registro um por um até encontrar o insumo que você está procurando. É eficiente para listas pequenas, mas pode demorar em listas muito grandes.

### 4. Busca Binária

**O que é:** É como o jogo "maior ou menor" - você divide a lista pela metade e elimina metade das opções a cada tentativa.

**Por que usar aqui:** Quando você tem muitos registros e eles estão organizados em ordem alfabética, a busca binária é muito mais rápida.

**Como funciona no código:** O sistema pega a lista ordenada, olha o meio dela, e decide se o que você procura está na primeira ou segunda metade. Repete isso até encontrar. É muito mais eficiente que a busca sequencial.

### 5. Merge Sort

**O que é:** Um algoritmo que divide a lista em pedaços pequenos, ordena cada pedaço, e depois junta tudo de forma organizada.

**Por que usar aqui:** É perfeito para organizar os insumos por quantidade consumida. Assim você consegue ver rapidamente quais insumos são mais ou menos utilizados.

**Como funciona no código:** O sistema pega a lista de consumos, divide em duas partes, ordena cada parte separadamente, e depois combina tudo de forma que fique ordenado por quantidade.

### 6. Quick Sort

**O que é:** Um algoritmo que escolhe um "pivô" e separa os elementos em "menores que o pivô" e "maiores que o pivô".

**Por que usar aqui:** É ideal para organizar os insumos por data de validade. Assim você consegue ver quais insumos vencem primeiro e planejar melhor as compras.

**Como funciona no código:** O sistema escolhe um registro como referência (pivô) e separa os outros em dois grupos: os que vencem antes e os que vencem depois. Repete isso recursivamente até tudo ficar ordenado por validade.

## Por Que Cada Estrutura Faz Sentido

- **Fila:** Para manter o histórico cronológico dos consumos
- **Pilha:** Para acessar rapidamente os consumos mais recentes
- **Busca Sequencial:** Para encontrar insumos específicos em listas pequenas
- **Busca Binária:** Para encontrar insumos específicos em listas grandes e organizadas
- **Merge Sort:** Para organizar por quantidade (identificar padrões de uso)
- **Quick Sort:** Para organizar por validade (planejamento de compras)

## Resultado Prático

Com esse sistema, um laboratório consegue:

1. **Controlar o estoque** - saber exatamente o que foi consumido e quando
2. **Prever compras** - identificar quais insumos são mais usados
3. **Evitar desperdício** - organizar por validade para usar antes de vencer
4. **Consultar rapidamente** - encontrar informações específicas de forma eficiente

## Como Executar

Simplesmente execute o arquivo `sprint.py` e você verá todos os algoritmos funcionando com dados simulados de consumo de insumos.

O sistema mostra como cada estrutura de dados e algoritmo funciona na prática, demonstrando diferentes formas de organizar e consultar as informações de consumo.

---

## Integrantes:
# Silas Alves dos Santos: RM555020
# Guilherme Oliveira da Silva: RM558797
# Rafael Panhoca: RM555014
# Victor Rodrigues - RM559094
# Matheus Dantas - RM558804