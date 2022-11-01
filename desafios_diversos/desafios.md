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
      self.assertEqual(expression_matter(*test[i]), result[i])

def expression_matter(a, b, c):
  # Aqui vai seu código
  return  # aqui vai a resposta

unittest.main()
```

---

## Função de movimentação do jogo

### Tarefa

Neste jogo, o herói se move da esquerda para a direita. O jogador rola os dados e move o número de casas indicadas pelos dados duas vezes.

Crie uma função para o jogo terminal que tome a posição atual do herói e a rolagem (1-6) e retorne a nova posição.

#### Exemplo:
`move(3, 6) # deve ser igual a 15`

#### Codigo

```python
import unittest

class moveTestCase(unittest.TestCase):
  def test_move1(self):
    self.assertEqual(move(0, 4), 8)
  
  def test_move2(self):
    self.assertEqual(move(3, 6), 15)

  def test_move3(self):
    self.assertEqual(move(2, 5), 12)

def move(position, roll):
    # your code here
    return
    
unittest.main()
```

---

## Removendo elementos

### Tarefa

Pegue um array e remova cada segundo elemento do array. Sempre mantenha o primeiro elemento e comece a remover com o próximo elemento.

#### Exemplo:
`["Keep", "Remove", "Keep", "Remove", "Keep", ...] -> ["Keep", "Keep", "Keep", ...]`

> Nenhuma das matrizes estará vazia, então você não precisa se preocupar com isso!

#### Codigo

```python
import unittest

class removeTestCase(unittest.TestCase):
  def test_remove_string(self):
    self.assertEqual(remove_every_other(['Hello', 'Goodbye', 'Hello Again']), ['Hello', 'Hello Again'])
  
  def test_remove_numbers(self):
    self.assertEqual(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 3, 5, 7, 9])

  def test_not_remove(self):
    self.assertEqual(remove_every_other([[1, 2]]), [[1, 2]])

  def test_remove_dict(self):
    self.assertEqual(remove_every_other([['Goodbye'], {'Great': 'Job'}]), [['Goodbye']])

def remove_every_other(my_list):
    # Your code here!
    return

unittest.main()
```

---

## Calcular média

### Tarefa

Escreva uma função que calcule a média dos números em uma determinada lista. 
#### Nota 

 - Arrays vazios devem retornar 0.

#### Codigo

```python
import unittest

class find_averageTestCase(unittest.TestCase):
  def test_find_average_empyt(self):
    self.assertEqual(find_average([]), 0)

  def test_find_average_len_5(self):
    self.assertEqual(find_average([4, 10, 9, 67, 8]), 19.6)

def find_average(array):
  return 

unittest.main()
```

---

## n é divisível por x e y?

### Tarefa

Crie uma função que verifique se um número `n` é divisível por dois números `x` **E** `y`. Todas as entradas são números positivos e diferentes de zero.

#### Exemplo

> 1) `n =   3, x = 1, y = 3 =>  true` porque 3 é divisivel por 1 e 3
> 2) `n =  12, x = 2, y = 6 =>  true` porque  12 é divisivel por 2 e 6
> 3) `n = 100, x = 6, y = 3 => false` porque 100 não é divisivel por 6 e 3
> 4) `n =  12, x = 7, y = 5 => false` porque  12 não é divisivel por 7 e 5

#### Codigo

```python
import unittest

class isDivisibleTestCase(unittest.TestCase):
  
  self.assertFalse(is_divisible(3,2,2))
  self.assertTrue(is_divisible(3,3,1))
  self.assertTrue(is_divisible(12,3,4))
  self.assertFalse(is_divisible(8,3,4))

def is_divisible(n, x, y):
  return

unittest.main()
```

---
<!--
## Poço de Ideias - Versão Fácil

### Tarefa

Para cada boa ideia de **desafios**, parece haver algumas ruins!

Neste **desafio** você precisa verificar o array fornecido para boas ideias **'boas'** e ideias ruins **'ruins'**.

- Se houver uma ou duas boas ideias, retorne **'Publicar!'**,
- se houver mais de 2, retorne **'Sinto cheiro de série!'**.
- Se não houver boas ideias, como costuma acontecer, retorne **'Falha!'**.

#### Codigo

```python
import unittest

class wellTestCase(unittest.TestCase):
  def test_well_fail(self):
    self.assertEqual(well(['bad', 'bad', 'bad']), 'Falha!')
  
  def test_well_publish(self):
    self.assertEqual(well(['good', 'bad', 'bad', 'bad', 'bad']), 'Publicar!')

  def test_well_series(self):
    self.assertEqual(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']), 'Sinto cheiro de série!')

def well(array):
  return ''

unittest.main()
```

---
-->
