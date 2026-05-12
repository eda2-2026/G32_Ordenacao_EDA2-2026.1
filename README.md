# Trabalho 2 de EDA 2 - Ordenação

[Vídeo explicando sobre o trabalho](https://youtu.be/--cAIG70X8Q)

O trabalho 2 é uma continuação direta do trabalho 1 realizado em EDA 2 sobre Busca. No trabalho 1, era garantido que as questões estariam agrupadas por categoria no CSV. No trabalho 2, não há mais essa garantia: o CSV pode estar desorganizado por padrão. O desafio foi utilizar algorítimos de ordenação eficientes que ordenassem as questões em uma ordem que pudesse ser utilizada pelos algorítmos de busca implementados anteriormente.

Os algorítmos utilizados foram o **Radix Sort LSD** e o **Counting Sort**. Ambos foram utilizados para ordenar respectivamente as questões por categoria e ano de lançamento.

A utilização de estruturas prontas do Python3 foi limitada ao máximo para construir algorítmos com as estruturas simples e manuais, similares ao que foi apresentado nas aulas. **NÃO FORAM UTILIZADAS bibliotecas como o Pandas, para facilidades com tabelas, ou funções como o `collections.Counter`, para facilidades na criação de histogramas (utilizados no Counting Sort e Radix Sort)**.

A ordenação pelo ano de lançamento é descendente e a ordenação pela categoria é descendente, mas tanto o Radix quanto o Counting Sort foram implementados para ordenarem ascendentemente e descendentemente se assim for desejado.

Algorítmo do Counting Sort:

* Extrair o mínimo e o máximo da coluna desejada da tabela original.
    * Caracteres foram traduzidas via função `ord` para números.
* Criar histograma de frequência
    * Utilizar mínimo e máximo para implementar um histograma de frequência como um vetor. Considere o index 0 o valor mínimo e o último index o valor máximo, ou seja, utilize *offsets*.
* Transformar histograma de frequência em *vetor de último index*.
    * Realizar isso *inplace*, sem copiar o histograma inteiro.
    * A troca entre ascendente e descendente é feita aqui. Se for ascendente (asc = 1), percorra comumente (passsada 1) o histograma para construir o vetor. Caso seja descendente (asc = 0), percorra o histograma de trás para frente (passada -1). Ou seja: passada = `-1 + asc*2`. 
* Posicionar o os registros da tabela nos índices do *vetor de último index*.
    * É essencial posicionar de trás para frente os registros para manter estabilidade do algorítmo e, posteriormente no Radix Sort, a ordem em strings.
    * Ajustar índice do vetor após posicionamento de cada registro (posicionei `'a'` no índice 3, o próximo `'a'` será no índice 2.).


Algorítmo do Radix Sort LSD:

* Preencher cada string da coluna referência de ordenação com `'\0'` para evitar `IndexError` e manter a ordem. Preencher até o tamanho da maior string.
* Para cada caractere da coluna:
    * Realizar o counting sort nos caracteres naquela posição da coluna. É do caractere menos significativo ao mais significativo (LSD), ou seja, de trás para frente ou direita para esquerda.
* Remover o preenchimento das strings.

O counting sort nos anos de lançamento é realizado primeiro do que o radix sort devido ao mesmo efeito do LSD nos caracteres: em caso de empate, a ordem anterior é mantida. Nesse caso, em toda categoria, as primeiras questões a aparecer são as dos anos mais recentes respectivamente.

## Trabalho 1 de EDA 2 - Busca


[Vídeo explicando sobre o trabalho](https://youtu.be/BkVsTYFPsbs?si=xylZH6ynKZAGbuUL)

Coloco algumas anotações minhas de estudo em um [MkDocs público](https://github.com/Raphides/cybersecurity) e tenho a vontade de adicionar perguntas e respostas (QAs) de concursos. Julguei esta como uma ótima oportunidade de aplicar um algorítmo de busca. A ideia é buscar e extrair, para cada página, QAs armazenadas no respositório e por fim imprimí-las nas páginas.

Esse projeto portanto serve como uma Prova de Conceito (PoC). A ideia não é encher de páginas reais, inserir uma impressão satisfatória na página e nem lotar a coleção de QAs. A intenção é só uma:

* Buscar QAs para cada página.

É garantido que todas as questões de uma mesma categoria estarão agrupadas no CSV.

Para isso, utiliza-se a seguinte estratégia:

1. Leitura do CSV.
2. Criação de uma tabela de índices por categorias
3. Para cada página (correspondente a uma categoria):
    1. Busca categoria na tabela de índice.
    2. Acessa a lista resultante do CSV pela tabela de índice.
    3. Inserir todas as questões da categoria até achar uma questão que não seja da categoria ou o EOF.

Logo, utiliza-se a estratégia de **Busca Sequencial Indexada** para fazer um filtro mais veloz.

Esperam-se uma quantidade considerável de categorias, logo, dentro da tabela de índices, utiliza-se a **Busca Sequencial com Sentinela com "Mover para Frente" invertido**. O "Mover Para Frente" invertido, nomeado por mim como "Mover Para Trás", é possível porque espera-se uma página por categoria, logo, após essa categoria ser acessada, as chances dela serem chamadas novamente são extremamente baixas. Dessa forma, podemos trocar uma categoria acessada com o último elemento. Mais uma adaptação em que se troca sempre pelo último que já não foi trocado, até chegar ao início da lista, onde volta para o final da lista. Exemplo

* 1ª busca por uma categoria: troca com o 3º (último).
* 2ª busca por uma categoria: troca com o 2º.
* 3ª busca por uma categoria: troca com o 1º.
* 4ª busca por uma categoria: troca com o 3º (último).
* 5ª busca por uma categoria: troca com o 2º.
* 6ª busca por uma categoria: troca com o 1º.

...


## Como rodar localmente

* Clone o projeto localmente
* Instale Python3 e Mkdocs
* Instale as bibliotecas do `requirements.txt`
* Execute na pasta raiz do projeto:

```bash
mkdocs serve
```

## Autor

|Autor|Matrícula|Github|
|---|---|---|
|Raphael Mendes da Silva|211039690|[Raphides](https://github.com/Raphides)|