# Bem vido aos desafios de Diversos

## Expressions Matter

### Tarefa

Dados três inteiros `a` ,`b`,`c`, retorne o maior número obtido após inserir os seguintes operadores e colchetes:`+`,`*`,`()`.
Em outras palavras, tente todas as combinações de `a`,`b`,`c` com `[* + ()]` e retorne o Máximo Obtido [(Leia as notas para mais detalhes sobre isso)](./Desafio.md#notas) e para o codigo, [clique aqui](./desafios.md#codigo).

#### Exemplo

Com os números 1, 2 e 3 , aqui estão algumas maneiras de colocar sinais e colchetes :

```python
1 * (2 + 3) = 5
1 * 2 * 3 = 6
1 + 2 * 3 = 7
(1 + 2) * 3 = 9
```

Portanto, o valor máximo que você pode obter é **9** .

#### Notas

- Os números são sempre positivos.
- Os números estão no intervalo `(1 ≤ a, b, c ≤ 10)`.
- Você pode usar a mesma operação mais de uma vez.
- Não é necessário colocar todos os sinais e colchetes.
- Pode ocorrer repetição de números.
- Você não pode trocar os operandos. Por exemplo, no exemplo dado, você não pode obter expression `(1 + 3) * 2 = 8`.
- Entrada >> Exemplos de Saída:
`expressionsMatter(1,2,3)`  ==>  `return 9`

##### Codigo

```python
import unittest

class matterTestCase(unittest.TestCase):
  def test_basic_expression_matter(self):
    test = [[2, 1, 2], [2, 1, 1], [2, 2, 4], [3, 3, 3], \
            [1, 1, 1], [1, 2, 3], [1, 3, 1], [2, 2, 2], \
            [5, 1, 3], [3, 5, 7], [5, 6, 1], [1, 6, 1], \
            [2, 6, 1], [6, 7, 1], [2, 10, 3], [1, 8, 3], \
            [9, 7, 2], [1, 1, 10], [9, 1, 1], [10, 5, 6], \
            [1, 10, 1]]
    result = [6,4,16,27,3,9,5,8,20,105,35,8,14,48,60,27,126,20,18,300,12]
    for i in range(len(test)):
      self.assertEquals(expression_matter(*test[i]), result[i])

def expression_matter(a, b, c):
  # Aqui vai seu código
  return  # aqui vai a resposta

unittest.main()
```

---
