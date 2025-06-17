# Invertendo uma Árvore Binária

Significa trocar os filhos esquerdo e direito de todos os nós da árvore. Esse
é um problema clássico e muito comum em entrevistas de emprego.

# Teoria

Dada uma árvore binária, inverta-a trocando o filho esquerdo com o direito
de cada nó recursivamente.

Ex:

```bash
Antes:               Depois:
    1                   1
   / \                 / \
  2   3      -->      3   2
 / \ / \             / \ / \
4  5 6  7           7  6 5  4
```

## Como inverter?

**Estratégias possíveis**:

1. Recursiva (DFS - Depth First Search)
    Para cada nó:  
        - inverta a subárvore da esquerda  
        - inverta a subárvore da direita  
        - troque os ponteiros  

2. Iterativa (usando fila - BFS - Breath First Search)
    - use uma fila (ou pilha)
    - visite cada nó e troque seus filhos
    - adicione os filhos à fila para continuar o processo

## Complexidade

- **Tempo:** O(n) onde `n` é o número de nós  
- **Espaço:**  
    - Recursivo: O(h) onde `h` é a altura da árove (por conta da stack)  
    - Iterativo: O(n) no pior caso se usar fila
