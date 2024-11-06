---
title: Pesquisar e Obter Texto das Páginas de um Documento PDF
linktitle: Pesquisar e Obter Texto
type: docs
weight: 60
url: pt/java/search-and-get-text-from-pdf/
description: Este artigo explica como usar várias ferramentas para pesquisar e obter texto de documentos PDF. Podemos pesquisar com expressão regular em páginas específicas ou em todo o documento.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Pesquisar e Obter Texto de Todas as Páginas de um Documento PDF

TextFragmentAbsorber permite que você encontre texto, correspondendo a uma frase específica, de todas as páginas de um documento PDF.

Para pesquisar texto em todo o documento, chame o método accept() da coleção [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
 O método [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) aceita um objeto TextFragmentAbsorber como parâmetro, que retorna uma coleção de objetos TextFragment. Percorra todos os fragmentos para obter suas propriedades, por exemplo, Texto, Posição, XIndent, YIndent, FontName, FontSize, IsAccessible, IsEmbedded, IsSubset, ForegroundColor etc.

O trecho de código a seguir mostra como pesquisar em todo o documento e exibir todas as correspondências em um console.

```java
// Abrir documento
Document pdfDocument = new Document("input.pdf");

// Criar objeto TextAbsorber para encontrar todas as instâncias da frase de busca de entrada
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("sample");

// Aceitar o absorvedor para todas as páginas
pdfDocument.getPages().accept(textFragmentAbsorber);

// Obter os fragmentos de texto extraídos em uma coleção
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// Percorrer os fragmentos
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    System.out.println("Texto :- " + textFragment.getText());
    System.out.println("Posição :- " + textFragment.getPosition());
    System.out.println("XIndent :- " + textFragment.getPosition().getXIndent());
    System.out.println("YIndent :- " + textFragment.getPosition().getYIndent());
    System.out.println("Fonte - Nome :- " + textFragment.getTextState().getFont().getFontName());
    System.out.println("Fonte - É Acessível :- " + textFragment.getTextState().getFont().isAccessible());
    System.out.println("Fonte - Está Incorporada - " + textFragment.getTextState().getFont().isEmbedded());
    System.out.println("Fonte - É Subconjunto :- " + textFragment.getTextState().getFont().isSubset());
    System.out.println("Tamanho da Fonte :- " + textFragment.getTextState().getFontSize());
    System.out.println("Cor de Primeiro Plano :- " + textFragment.getTextState().getForegroundColor());
}
```

Para pesquisar texto em uma página específica e obter propriedades associadas a ele, forneça o índice da página:

```java
// Aceitar o absorvedor para a primeira página do documento
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);
```

## Pesquisar e Obter Segmentos de Texto das Páginas do PDF

Para pesquisar segmentos de texto em todas as páginas de um documento, obtenha objetos TextFragment de um documento.

TextFragmentAbsorber permite encontrar texto que corresponde a uma frase específica em todas as páginas de um documento PDF. Para pesquisar texto em todo o documento, chame o método [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) da coleção [Pages](https://reference.aspose.com/pdf//java/com.aspose.pdf/pagecollection). O método [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) leva um objeto TextFragmentAbsorber como parâmetro, que retorna uma coleção de objetos TextFragment.

{{% alert color="primary" %}}

Quando a coleção TextFragmentCollection foi extraída do documento, faça um loop através dela para obter a coleção TextSegmentCollection de cada objeto TextFragment.
 Após isso, você pode obter as propriedades individuais do objeto TextSegment.

{{% /alert %}}

O trecho de código a seguir mostra como pesquisar segmentos de texto em todas as páginas.

```java
// Abrir documento
Document pdfDocument = new Document("input.pdf");

// Criar objeto TextAbsorber para encontrar todas as instâncias da frase de busca de entrada
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("sample");

// Aceitar o absorvedor para a primeira página do documento
pdfDocument.getPages().accept(textFragmentAbsorber);

// Obter os fragmentos de texto extraídos em uma coleção
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// Percorrer os fragmentos de texto
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    // Iterar através dos segmentos de texto
    for (TextSegment textSegment : (Iterable<TextSegment>) textFragment.getSegments()) {
        System.out.println("Texto :- " + textSegment.getText());
        System.out.println("Posição :- " + textSegment.getPosition());
        System.out.println("XIndent :- " + textSegment.getPosition().getXIndent());
        System.out.println("YIndent :- " + textSegment.getPosition().getYIndent());
        System.out.println("Fonte - Nome :- " + textSegment.getTextState().getFont().getFontName());
        System.out.println("Fonte - É Acessível :- " + textSegment.getTextState().getFont().isAccessible());
        System.out.println("Fonte - Está Incorporada - " + textSegment.getTextState().getFont().isEmbedded());
        System.out.println("Fonte - É Subconjunto :- " + textSegment.getTextState().getFont().isSubset());
        System.out.println("Tamanho da Fonte :- " + textSegment.getTextState().getFontSize());
        System.out.println("Cor de Primeiro Plano :- " + textSegment.getTextState().getForegroundColor());
    }
}
```

Para buscar um segmento de texto específico e obter as propriedades associadas, especifique o índice da página para a página que você deseja buscar:

```java
// Aceitar o absorvedor para a primeira página do documento.
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);
```

## Buscar e Obter Texto das páginas usando Expressão Regular

TextFragmentAbsorber ajuda você a buscar e recuperar texto de todas as páginas de um documento, com base em uma expressão regular.

Para buscar e obter texto de um documento:

1. Passe o termo de busca como uma expressão regular para o construtor do TextFragmentAbsorber.
1. Defina a propriedade TextSearchOptions do objeto TextFragmentAbsorber.
   Esta propriedade requer um objeto TextSearchOptions: passe true para seu construtor ao criar um novo objeto.
1. Para recuperar o texto correspondente de todas as páginas, chame o método [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) da coleção [Pages](https://reference.aspose.com/pdf//java/com.aspose.pdf/pagecollection).

   TextFragmentAbsorber retorna um TextFragmentCollection contendo todos os fragmentos que correspondem aos critérios especificados pela expressão regular.

O trecho de código a seguir mostra como pesquisar todas as páginas de um documento e obter texto com base em uma expressão regular.

```java
// Abrir um documento
Document pdfDocument = new Document("source.pdf");

// Criar objeto TextAbsorber para encontrar todas as instâncias da frase de pesquisa de entrada
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // como 1999-2000

// Definir a opção de pesquisa de texto para especificar o uso de expressão regular
TextSearchOptions textSearchOptions = new TextSearchOptions(true);
textFragmentAbsorber.setTextSearchOptions(textSearchOptions);

// Aceitar o absorvedor para a primeira página do documento
pdfDocument.getPages().accept(textFragmentAbsorber);

// Obter os fragmentos de texto extraídos na coleção
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// Percorrer os fragmentos
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    System.out.println("Texto :- " + textFragment.getText());
    System.out.println("Posição :- " + textFragment.getPosition());
    System.out.println("XIndent :- " + textFragment.getPosition().getXIndent());
    System.out.println("YIndent :- " + textFragment.getPosition().getYIndent());
    System.out.println("Fonte - Nome :- " + textFragment.getTextState().getFont().getFontName());
    System.out.println("Fonte - É Acessível :- " + textFragment.getTextState().getFont().isAccessible());
    System.out.println("Fonte - Está Incorporada - " + textFragment.getTextState().getFont().isEmbedded());
    System.out.println("Fonte - É Subconjunto :- " + textFragment.getTextState().getFont().isSubset());
    System.out.println("Tamanho da Fonte :- " + textFragment.getTextState().getFontSize());
    System.out.println("Cor do Primeiro Plano :- " + textFragment.getTextState().getForegroundColor());
}
```


Para buscar texto em uma página específica e obter suas propriedades, especifique o índice da página:

```java
// Aceite o absorvedor para a primeira página do documento.
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber)
```

Para buscar uma string em maiúsculas ou minúsculas, você pode considerar usar expressão regular.

```java
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("(?i)Line", new TextSearchOptions(true));
```

Exemplo:

```java
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[\\S]+");
```