# Bem vido aos desafios de Algoritimos

## Busca Linear em uma Lista não Ordenada

> A busca linear é um algoritmo simples, que percorre um array de elementos não ordenados e compara cada um deles com o elemento procurado, até que encontre e retorne a sua posição.
> Essa abordagem é conhecida como busca por força bruta.
> No pior caso, o elemento não será encontrado mesmo depois de percorrer todas as posições do array, até a última.

###### Problema proposto

- Crie um programa que recebe uma lista de inteiros e um valor que deve ser buscado. O programa deve retornar o índice onde o valor foi encontrado, ou -1, caso não encontre o valor.

---

## Busca Binária em uma Lista de Números Aleatórios
> A busca binária procura um valor em uma lista ordenada, comparando o valor buscado com o valor do meio da lista.
>
> Se o valor buscado for maior que o elemento existente no meio da lista, a busca continua de forma recursiva na metade superior da lista.
>
> Mas se o valor buscado for menor que o elemento existente no meio da lista, a busca continua de forma recursiva na metade inferior da lista.

###### Problema proposto

- Escreva um programa que cria uma lista de 100 números aleatórios inteiros ordenados e solicita um número para o usuário. Use a busca binária para encontrar a posição do número fornecido na lista, ou retorne -1 se ele não for encontrado.

---
<!--
## Algoritmo que Verifica se um Texto é um Palíndromo

>De acordo com o dicionário da língua portuguesa, um palíndromo é uma palavra ou frase escrita da mesma forma da esquerda para a direita ou da direita para a esquerda.
>
> Por exemplo, “Ana”, “arara” e “Socorram-me, subi no ônibus em Marrocos” são palíndromos.

###### Problema proposto

- Crie um programa que verifica se uma string é um palíndromo e retorna True ou False.

---

## Números de Armstrong

> Um número de Armstrong é um número de N dígitos onde a soma de cada dígito, elevado a N, é igual ao próprio número.
Veja um exemplo com um número de 3 dígitos em base 10:
>
> `153 = 13 + 53 + 33 =  1 + 125 + 27 = 153`

###### Problema proposto

- Escreva um programa que imprima todos os números de Armstrong em base 10 que tenham até 6 dígitos.

---

## Programa para Imprimir Tabelas Verdade a Partir de Expressões

> Esse é um ótimo exercício para entender como funcionam os operadores lógicos e como fazer laços de repetição aninhados.

###### Problema proposto

- Crie um programa que receba uma expressão booleana qualquer com duas variáveis, x e y, e imprima a tabela verdade para cada valor de x e y em (True, False).

    Você pode começar atribuindo cada expressão booleana que será testada a uma variável dentro do seu programa (hardcoded).

    Depois, você pode evoluir o seu código, criando uma função que imprime a tabela verdade e passando uma função lambda contendo a expressão, semelhante a esse exemplo:

    ```python
    def tabelaVerdade(expr):
        #  Imprimir a tabela

    #  Teste
    nor = (lambda x, y: not (x or y))
    tabelaVerdade(nor)
    ```

    Ou então, passe só a string contendo a expressão e use a função eval() para executar o código

> Embora o uso da função `eval()` facilite a construção desse exemplo, eu sugiro que você evite usar essa função em seus programas, já que ela executa qualquer código que recebe.
>
> Em um programa real, isso pode ser uma porta de entrada para um código malicioso.

---

-->
