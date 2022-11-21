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

    Você pode começar atribuindo cada expressão booleana que será testada a uma variável dentro do seu programa.

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

## Lei dos Grandes Números (Law of Large Numbers)
> A Lei dos Grandes Números tem origem na teoria da probabilidade.
> 
> Para entender o que ela significa, sugiro que você leia esse artigo na [Wikipedia](https://pt.wikipedia.org/wiki/Lei_dos_grandes_n%C3%BAmeros).
>
> Em resumo, na Lei dos Grandes Números, “a média aritmética dos resultados da realização da mesma experiência repetidas vezes tende a se aproximar do valor esperado à medida que mais tentativas se sucederem”.
>
> É fácil de entender o que isso significa…
> Imagine um dado com 6 lados.
>
> A probabilidade de sair cada um dos 6 lados é de `1/6`.
>
> Então, se você jogar o dado milhares de vezes, cada resultado possível saíra em `1/6` das vezes.
>
> A média aritmética desses resultados possíveis, `(1 + 2 + 3 + 4 + 5 + 6)/6`, é igual a `3,5`.
>
> Perceba que `3,5` é a média dos resultados ao longo de muitos lançamentos, não a probabilidade de sair um resultado e nem o valor de um lado do dado.

###### Problema proposto:

- Crie um programa que simule N lançamentos de um dado de 6 lados e imprima a média aritmética dos resultados. Verifique se a média se aproxima de `3,5` à medida que o valor de `N` aumenta.

---

## Automatize Tarefas Repetitivas
> Uma tarefa importante para administradores de sistemas é gerenciar arquivos nos diretórios sem precisar ficar movendo ícones em uma interface gráfica ou rodando dezenas de comandos em um terminal.
>
> Portanto, um script que manipula arquivos pode ser adaptado para várias finalidades, dependendo da necessidade.

###### Problema proposto:

- Escreva um programa que crie `100 arquivos` texto de `4KB` com nomes e conteúdo aleatórios.

> Em seguida, o programa deve renomear os arquivos em sequência, com um prefixo de `001` a `100`.
> 
- Depois disso, o programa deve criar arquivos `.zip` com `10 arquivos texto` em cada e salvar os arquivos `.zip` gerados a cada execução em um diretório com a estrutura `ano/mês/dia/hora/minuto`.

  Por fim, o programa deve apagar os `arquivos texto originais` , caso o processamento termine **sem erros.**
  
---

## Envie E-mails
> Uma das tarefas mais comuns realizadas por um programa, seja um script de gerenciamento de arquivos de backup ou um sistema Web como o WordPress, é enviar e-mails.

###### Problema proposto:

- Crie um programa que envia um e-mail para os endereços cadastrados, contendo o resultado da execução do programa do desafio anterior.

---

## Acesse um Conjuntos de Dados Online
> Alguns programadores se organizam em comunidades para desenvolver softwares com o objetivo de fiscalizar a Administração Pública nas esferas municipal, estadual e federal.
>
> Uma dessas iniciativas é a [Operação Serenata de Amor](https://serenata.ai/).
>
> Em geral, as soluções desenvolvidas por esses grupos são baseadas nos dados disponibilizados pelos órgãos públicos, conhecidos como [Dados Abertos](http://dados.gov.br/).
>
> Esses dados são disponibilizados via Internet em formatos comuns, como `JSON`, `XML` ou `CSV`.
>
> Outra fonte de dados bastante utilizada por programadores é o [Kaggle](http://kaggle.com/), uma plataforma online com mais de 50.000 conjuntos de dados, que vão desde levantamentos de doenças no mundo todo até opiniões sobre sopa de macarrão japonesa.

###### Problema proposto:

- Crie um programa que acessa um conjunto de dados na Internet, baixa os arquivos e monta uma tabela com as colunas do arquivo utilizado. Em seguida, salve a tabela em um banco de dados SQLite.

---

## Gere Visualizações de Dados Interessantes
> Uma vez que você tenha entendido como recuperar e processar conjuntos de dados, chegou a hora de criar visualizações sobre esses dados.
>
> Essa é uma competência fundamental para quem quer seguir a carreira de cientista de dados.
>
> As bibliotecas Matplotlib e Seaborn permitem construir gráficos avançados usando a linguagem Python.

###### Problema proposto:

- Usando a lógica do problema anterior, baixe o conjunto de dados de estatísticas da NBA desde 1950 e crie gráficos que demonstrem:

1. A quantidade total de pontos dos 10 maiores pontuadores de cada temporada, ao longo dos anos, comparada com o percentual de jogos em que eles jogaram por temporada (gráfico de linhas).

2. A distribuição da quantidade de bloqueios por altura do jogador, em intervalos de 10 cm de diferença (histograma).

3. A relação entre o número de faltas cometidas e o percentual de lances livres convertidos por jogador, separando por posições (scatter plot).
---
