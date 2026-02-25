---
title: Usando Anotação de Texto para PDF via Python
linktitle: Anotação de Texto
type: docs
weight: 10
url: /pt/python-net/text-annotation/
description: Aspose.PDF para Python permite que você Adicione, Recupere e Exclua Anotações de Texto do seu documento PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Guia sobre como manipular anotações de texto em PDF
Abstract: Este artigo oferece um guia abrangente sobre como manipular anotações de texto em arquivos PDF usando a biblioteca Aspose.PDF para Python. Ele cobre a adição, recuperação e exclusão de vários tipos de anotação, incluindo Texto, Texto Livre e Anotações de Tachado. Anotações de Texto são notas anexadas a um local específico dentro de um PDF, exibidas como ícones que revelam texto em um pop-up quando abertas. Anotações de Texto Livre exibem texto diretamente na página, enquanto Anotações de Tachado marcam o texto com uma linha para indicar remoção ou desconsideração. O processo envolve adicionar anotações à coleção Annotations de uma página usando o método `add()`, e exemplos são fornecidos para cada tipo de anotação. Trechos de código ilustram como implementar essas tarefas, incluindo a criação de anotações com propriedades específicas como título, assunto, cor e flags, bem como a recuperação e exclusão de anotações de páginas PDF. Este guia serve como um recurso prático para desenvolvedores que desejam aprimorar documentos PDF por meio da manipulação de anotações usando Aspose.PDF.
---

## Como adicionar Anotação de Texto em arquivo PDF existente

Uma Anotação de Texto é uma anotação anexada a um local específico em um documento PDF. Quando fechada, a anotação é exibida como um ícone; quando aberta, deve exibir uma janela pop-up contendo o texto da nota na fonte e tamanho escolhidos pelo leitor.

Anotações são contidas pela coleção [Anotações](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/) de uma página específica. Esta coleção contém as anotações apenas para essa página individual; cada página tem sua própria coleção de Anotações.

Para adicionar uma anotação a uma página específica, adicione-a à coleção Anotações dessa página usando o método [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/#methods).

1. Primeiro, crie uma anotação que você deseja adicionar ao PDF.
1. Em seguida, abra o PDF de entrada.
1. Adicione a anotação à coleção [Anotações](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/) do objeto 'page'.

O trecho de código a seguir mostra como adicionar uma anotação em uma página PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    textAnnotation = ap.annotations.TextAnnotation(
        document.pages[1], ap.Rectangle(300, 700.664, 320, 720.769, True)
    )
    textAnnotation.title = "Aspose User"
    textAnnotation.subject = "Inserted text 1"
    textAnnotation.contents = "qwerty"
    textAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    textAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(textAnnotation)
    document.save(output_file)
```

## Obter Anotação de Texto de um arquivo PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    textAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.TEXT)
    ]

    for ta in textAnnotations:
        print(ta.rect)
```

## Excluir Anotação de Texto de um arquivo PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    textAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.TEXT)
    ]

    for ta in textAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```


## Como adicionar (ou Criar) nova Anotação de Texto Livre

Uma anotação de texto livre exibe texto diretamente na página. A classe [FreeTextAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/freetextannotation/) permite criar esse tipo de anotação. No trecho a seguir, adicionamos uma anotação de texto livre acima da primeira ocorrência da string.

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)

    freeTextAnnotation = ap.annotations.FreeTextAnnotation(
        document.pages[1], ap.Rectangle(299, 713, 308, 720, True), ap.annotations.DefaultAppearance()
    )
    freeTextAnnotation.title = "Aspose User"
    freeTextAnnotation.color = ap.Color.light_green

    document.pages[1].annotations.append(freeTextAnnotation)
    document.save(output_file)
```

## Obter Anotação de Texto Livre de um arquivo PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    freeTextAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.FREE_TEXT)
    ]

    for fa in freeTextAnnotations:
        print(fa.rect)
```

## Excluir Anotação de Texto Livre de um arquivo PDF

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)
    freeTextAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.FREE_TEXT)
    ]

    for fa in freeTextAnnotations:
        document.pages[1].annotations.delete(fa)

    document.save(output_file)
```


### Rabiscar Palavras usando StrikeOutAnnotation

Aspose.PDF para Python permite que você adicione, exclua e atualize anotações em documentos PDF. Uma das classes também permite riscar anotações. Quando uma StrikeOutAnnotation é aplicada a um PDF, uma linha é desenhada através do texto especificado, indicando que ele deve ser removido ou ignorado.

O trecho de código a seguir mostra como adicionar uma [StrikeOutAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/strikeoutannotation/) ao PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    strikeoutAnnotation = ap.annotations.StrikeOutAnnotation(
        document.pages[1], ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    strikeoutAnnotation.title = "Aspose User"
    strikeoutAnnotation.subject = "Inserted text 1"
    strikeoutAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    strikeoutAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(strikeoutAnnotation)
    document.save(output_file)
```


## Obter StrikeOutAnnotation de PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    StrikeoutAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT)
    ]

    for pa in StrikeoutAnnotations:
        print(pa.rect)
```

## Excluir StrikeOutAnnotation de PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    StrikeoutAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT)
    ]

    for pa in StrikeoutAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```



