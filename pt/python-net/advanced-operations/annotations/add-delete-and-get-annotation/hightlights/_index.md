---
title: Anotação de Destaques em PDF usando Python
linktitle: Anotação de Destaques
type: docs
weight: 20
url: /pt/python-net/highlights-annotation/
description: Aprenda como adicionar anotações de destaques a arquivos PDF em Python usando Aspose.PDF para ênfase de texto.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guia sobre como manipular anotações de Destaques em PDF
Abstract: O artigo fornece um guia abrangente sobre como usar anotações de marcação de texto em documentos PDF, focando nas funcionalidades fornecidas pela biblioteca Aspose.PDF em Python. Ele explica o propósito e o uso de diferentes tipos de anotações, incluindo anotações de destaque, sublinhado, tachado e ondulado, cada uma projetada para enfatizar ou modificar o texto de várias maneiras. O documento descreve as etapas necessárias para adicionar essas anotações a um PDF, incluindo o carregamento do documento, a criação das anotações com parâmetros específicos como título e cor, e a inserção delas na página desejada. Além disso, o artigo inclui trechos de código para recuperar anotações de um PDF, permitindo que os usuários filtrem e imprimam detalhes das anotações com base no tipo. Por fim, detalha o processo de exclusão de anotações, fornecendo exemplos de código para remover cada tipo de anotação de marcação de texto do documento. Este guia serve como um recurso prático para desenvolvedores que desejam manipular anotações de texto em arquivos PDF programaticamente usando Python.
---

As anotações de marcação de texto em PDF são usadas para destacar, sublinhar, rasurar ou adicionar notas ao texto no documento. Essas anotações têm o objetivo de realçar ou chamar a atenção para partes específicas do texto. Tais anotações permitem que os usuários marquem visualmente ou modifiquem o conteúdo de um arquivo PDF.

A anotação de destaque é usada para marcar o texto com um fundo colorido, geralmente amarelo, para indicar sua importância ou relevância.

A anotação de sublinhado é uma linha colocada sob o texto selecionado para indicar relevância, ênfase ou sugerir edições.

A anotação de tachado inclui riscar ou atravessar um determinado texto para mostrar que ele foi deletado, substituído ou não é mais válido.

A linha ondulada é usada para sublinhar o texto a fim de indicar um tipo diferente de destaque, como erros ortográficos, problemas potenciais ou alterações propostas.

## Adicionar Anotação de Marcação de Texto

Para adicionar uma Anotação de Marcação de Texto ao documento PDF, precisamos executar as seguintes ações:

1. Carregar o arquivo PDF - novo objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .
1. Criar anotações:
- [HighlightAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation/) e definir parâmetros (título, cor).
- [StrikeOutAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/strikeoutannotation/) e definir parâmetros (título, cor).
- [SquigglyAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squigglyannotation/) e definir parâmetros (título, cor).
- [UnderlineAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/underlineannotation/) e definir parâmetros (título, cor).
1. Em seguida, devemos adicionar todas as anotações à página.

### Adicionar Anotação de Destaque

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    # Create Circle Annotation
    highlightAnnotation = ap.annotations.HighlightAnnotation(
        document.pages[1], ap.Rectangle(300, 750, 320, 770, True)
    )
    document.pages[1].annotations.append(highlightAnnotation)
    document.save(output_file)
```

### Adicionar Anotação de Tachado

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

### Adicionar Anotação Ondulada

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    page = document.pages[1]
    squigglyAnnotation = ap.annotations.SquigglyAnnotation(page, ap.Rectangle(67, 317, 261, 459, True))
    squigglyAnnotation.title = "John Smith"
    squigglyAnnotation.color = ap.Color.blue

    page.annotations.append(squigglyAnnotation)

    document.save(output_file)
```

### Adicionar Anotação de Sublinhado

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    underlineAnnotation = ap.annotations.UnderlineAnnotation(
        document.pages[1], ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    underlineAnnotation.title = "Aspose User"
    underlineAnnotation.subject = "Inserted Underline 1"
    underlineAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    underlineAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(underlineAnnotation)
    document.save(output_file)
```

## Obter Anotação de Marcação de Texto

Por favor, tente usar o seguinte trecho de código para Obter Anotação de Marcação de Texto do documento PDF.

### Obter Anotação de Destaque

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT)
    ]

    for ha in highlightAnnotations:
        print(ha.rect)
```

### Obter Anotação de Tachado

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


### Obter Anotação Ondulada

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squigglyAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUIGGLY)
    ]

    for pa in squigglyAnnotations:
        print(pa.rect)
```

### Obter Anotação de Sublinhado

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    UnderlineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.UNDERLINE)
    ]

    for ta in UnderlineAnnotations:
        print(ta.rect)
```

## Excluir Anotação de Marcação de Texto

O trecho de código a seguir mostra como Excluir Anotação de Marcação de Texto de um arquivo PDF.

### Excluir Anotação de Destaque

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(output_file)
```

### Excluir Anotação de Tachado

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

### Excluir Anotação Ondulada

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squigglyAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUIGGLY)
    ]

    for pa in squigglyAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

### Excluir Anotação de Sublinhado

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    underlineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.UNDERLINE)
    ]

    for ta in underlineAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```



