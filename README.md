# Trabalho 2 de EDA 2 - Busca

<!-- [Vídeo explicando sobre o trabalho](https://youtu.be/BkVsTYFPsbs?si=xylZH6ynKZAGbuUL)

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

Logo, utiliza-se a estratégia de **Busca Sequencial Indexada** para fazer um filtro mais veloz. -->

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