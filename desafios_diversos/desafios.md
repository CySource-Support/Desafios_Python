# Bem vido aos desafios Diversos

## Expressions Matter

dificuldade | fundamental
---:|:---

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

dificuldade | fundamental
---:|:---

### Tarefa

Neste jogo, o herói se move da esquerda para a direita. O jogador rola os dados e move o número de casas indicadas pelos dados duas vezes.

Crie uma função para o jogo terminal que tome a posição atual do herói e a rolagem (1-6) e retorne a nova posição.

#### Exemplo

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

dificuldade | fundamental
---:|:---

### Tarefa

Pegue um array e remova cada segundo elemento do array. Sempre mantenha o primeiro elemento e comece a remover com o próximo elemento.

#### Exemplo

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

dificuldade | fundamental
---:|:---

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

dificuldade | fundamental
---:|:---

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
  def test_is_divisible(self):
      self.assertTrue(is_divisible(3,3,1))
      self.assertTrue(is_divisible(12,3,4))
      
  def test_not_divisible(self)
      self.assertFalse(is_divisible(8,3,4))
      self.assertFalse(is_divisible(3,2,2))

def is_divisible(n, x, y):
  return

unittest.main()
```

---

## Poço de Ideias - Versão Fácil

dificuldade | fundamental
---:|:---

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
  return 

unittest.main()
```

---

## Terceiro ângulo de um triângulo

dificuldade | fundamental
---:|:---

### Tarefa

Você recebe dois ângulos internos (em graus) de um triângulo.

Escreva uma função para retornar o 3º ângulo.

Nota: apenas números inteiros positivos serão testados.

[Mais dicas](https://en.wikipedia.org/wiki/Triangle)

#### Codigo

```Python
import unittest

class angleTestCase(unittest.TestCase):
  def test_angle_90(self):
    self.assertEqual(other_angle(30, 60), 90)
  
  def test_angle_60(self):
    self.assertEqual(other_angle(60, 60), 60)

  def test_angle_59(self):
    self.assertEqual(other_angle(43, 78), 59)

  def test_angle_150(self):
    self.assertEqual(other_angle(10, 20), 150)

def other_angle(a, b):
    pass

unittest.main()
```

---

## Calcular IMC

dificuldade | fundamental
---:|:---

### Tarefa

Escreva a função imc que calcula o índice de massa corporal (imc = peso/altura2 ).

se `imc <= 18,5` retornar `"Abaixo do peso"`

se `imc <= 25,0` retorna `"Normal"`

se `imc <= 30,0` retornar `"Excesso de peso"`

se `imc > 30` retorna `"Obeso"`

#### codigo

```python
import unittest

class imcTestCase(unitest.TestCase):
  def test_bmi_Underweight(self):
    test.assert_equals(bmi(50, 1.80), "Underweight")
  
  def test_bmi_Normal(self):
    test.assertEqual(bmi(80, 1.80), "Normal")
    test.assertEqual(bmi(50, 1.50), "Normal")
  
  def test_bmi_Overweight(self):
    test.assertEqual(bmi(90, 1.80), "Overweight")

  def test_bmi_Obese(self):
    test.assertEqual(bmi(110, 1.80), "Obese")

def bmi(weight, height):
    #your code here

unittest.main()
  
```

---

## Elementos maiores

### Tarefa

Escreva um programa que produza os `n` maiores elementos de uma lista.

**Exemplo:**

```python
largest(2, [7,6,5,4,3,2,1])
# => [6,7]
```

#### codigo

```python
import unittest

class largestTestCase(unittest.TestCase):
  def test_largest_two_number(self):
    self.assertEqual(largest(2,[10,9,8,7,6,5,4,3,2,1]),[9,10])
  
  def test_largest_trhee_number(self):
    self.assertEqual(largest(3,[5,1,5,2,3,1,2,3,5]),[5,5,5])
  
  def test_largest_seven_number(self):
    self.assertEqual(largest(7,[9,1,50,22,3,13,2,63,5]),[3, 5, 9, 13, 22, 50, 63])

def largest(n, xs):
  """Find the n highest elements in a list"""


unittest.mmain()
```

---

## Safen User Input Parte I - htmlspecialchars

### Descrição

Você é um(a) desenvolvedor(a) da Web iniciante/médio/experiente/profissional/mundialmente famoso (escolha um) que possui um site simples/limpo/slick/bonito/complicado/profissional/de negócios (escolha um ou mais) que contém campos de formulário para que os visitantes possam enviar e-mails ou deixar um comentário em seu site com facilidade. No entanto, com facilidade vem o perigo . De vez em quando, um hacker visita seu site e tenta comprometê-lo através do uso de XSS (Cross Site Scripting). Isso é feito injetando script tags no site por meio de campos de formulário que podem conter código malicioso (por exemplo, um redirecionamento para um site malicioso que rouba informações pessoais).

### Tarefa

Sua missão é implementar uma função que converta os seguintes caracteres potencialmente prejudiciais:

 < | \&lt;
:---:|:---:
\> | \&gt;
" | \&quot;
& | \&amp;

#### codigo

```python
import unittest

class html_charTestCase(unittest.TestCase):
  def test_html_char(self):
    self.assertEqual(html_special_chars("<h2>Hello World</h2>"), "&lt;h2&gt;Hello World&lt;/h2&gt;")
  
  def test_html_char_1(self):
    self.assertEqual(html_special_chars("Hello, how would you & I fare?"), "Hello, how would you &amp; I fare?")

  def test_html_char_2(self):
    self.assertEqual(html_special_chars('How was "The Matrix"?  Did you like it?'), 'How was &quot;The Matrix&quot;?  Did you like it?')

  def test_html_char_3(self):
    self.assertEqual(html_special_chars("<script>alert('Website Hacked!');</script>"), "&lt;script&gt;alert('Website Hacked!');&lt;/script&gt;")

def html_special_chars(data): 
    # your code here
    pass

unittest.main()

```

---
