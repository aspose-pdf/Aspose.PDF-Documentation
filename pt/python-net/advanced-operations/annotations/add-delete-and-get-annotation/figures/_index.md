---
title: Adicionar Anotações de Figuras usando Python
linktitle: Anotações de Figuras
type: docs
weight: 30
url: /pt/python-net/figures-annotation/
description: Este artigo descreve como adicionar, obter e excluir anotações de figuras do seu documento PDF com Aspose.PDF para Python via .NET
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guia sobre como manipular anotações de Figuras em PDF
Abstract: Este artigo fornece um guia abrangente sobre como adicionar, recuperar e excluir anotações de quadrado, círculo, polígono e polilinha em documentos PDF usando Aspose.PDF para Python. As anotações de quadrado e círculo realçam visualmente áreas específicas em uma página PDF com formas retangulares e elípticas, respectivamente. O artigo inclui instruções passo a passo e trechos de código Python para criar essas anotações carregando um arquivo PDF, configurando propriedades da anotação como título, cor e opacidade, e adicionando-as às páginas do PDF. Além disso, o artigo detalha métodos para recuperar anotações por tipo, imprimindo suas dimensões retangulares, e excluí-las do documento PDF. Anotações de polígono e polilinha também são abordadas, onde polígonos são definidos por uma série de vértices conectados formando uma forma fechada, enquanto polilinhas conectam vértices de maneira aberta. O documento fornece exemplos de código para ilustrar os processos de adição dessas anotações a um PDF, bem como métodos para acessá‑las e removê‑las.

---

## Adicionar Anotações de Quadrado e Círculo

Em documentos PDF, uma anotação de quadrado refere‑se a um tipo específico de anotação representada por uma forma quadrada. As anotações de quadrado são usadas para destacar ou chamar a atenção para uma área ou seção específica dentro do documento.

[Quadrado](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation/) e [Círculo](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/circleannotation/) as anotações deverão exibir, respectivamente, um retângulo ou uma elipse na página.

Etapas para criar anotações de Quadrado ou Círculo:

1. Carregue o arquivo PDF - novo [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crie uma nova [SquareAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation) e defina os parâmetros (novo Rectangle, título, cor, interior_color, opacidade).
1. Em seguida, precisamos adicionar a anotação de Quadrado à página.

O trecho de código a seguir mostra como adicionar anotações de Quadrado em uma página PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    squareAnnotation = ap.annotations.SquareAnnotation(document.pages[1], ap.Rectangle(60, 600, 250, 450, True))
    squareAnnotation.title = "John Smith"
    squareAnnotation.color = ap.Color.blue
    squareAnnotation.interior_color = ap.Color.blue_violet
    squareAnnotation.opacity = 0.25

    document.pages[1].annotations.append(squareAnnotation)

    document.save(output_file)
```

O trecho de código a seguir mostra como adicionar anotações de Círculo em uma página PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    circleAnnotation = ap.annotations.CircleAnnotation(
        document.pages[1], ap.Rectangle(270, 160, 483, 383, True)
    )
    circleAnnotation.title = "John Smith"
    circleAnnotation.color = ap.Color.red
    circleAnnotation.interior_color = ap.Color.misty_rose
    circleAnnotation.opacity = 0.5
    circleAnnotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1], ap.Rectangle(842, 316, 1021, 459, True)
    )

    document.pages[1].annotations.append(circleAnnotation)
    document.save(output_file)
```

Como exemplo, veremos o seguinte resultado da adição de anotações de Quadrado e Círculo a um documento PDF:

![Demo de Anotações de Círculo e Quadrado](circle_demo.png)

### Obter Anotação de Círculo

Por favor, tente usar o trecho de código a seguir para obter a anotação de Círculo do documento PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    circleAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CIRCLE)
    ]

    for ca in circleAnnotations:
        print(ca.rect)
```

### Obter Anotação de Quadrado

Por favor, tente usar o trecho de código a seguir para obter a anotação de Quadrado do documento PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squareAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUARE)
    ]

    for pa in squareAnnotations:
        print(pa.rect)
```


### Excluir Anotação de Círculo

O trecho de código a seguir mostra como excluir a anotação de Círculo de um arquivo PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    circleAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CIRCLE)
    ]

    for ca in circleAnnotations:
        document.pages[1].annotations.delete(ca)

    document.save(output_file)
```

### Excluir Anotação de Quadrado

O trecho de código a seguir mostra como excluir a anotação de Quadrado de um arquivo PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squareAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUARE)
    ]

    for pa in squareAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

## Adicionar Anotações de Polígono e Polilinha

A ferramenta Polilinha permite criar formas e contornos com um número arbitrário de lados no documento.

[Anotações de Polígono](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation/) representam polígonos em uma página. Elas podem ter qualquer número de vértices conectados por linhas retas.

[Anotações de Polilinha](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) são também semelhantes a polígonos, a única diferença é que o primeiro e o último vértice não são conectados implicitamente.

Etapas com as quais criamos anotações de Polígono:

1. Carregue o arquivo PDF - novo [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crie uma nova [Polygon Annotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation) e defina os parâmetros do Polígono (novo Rectangle, novos Points, título, cor, interior_color e opacidade).
1. Em seguida, podemos adicionar as anotações à página.

O trecho de código a seguir mostra como adicionar Anotações de Polígono a um arquivo PDF:

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    polygonAnnotation = ap.annotations.PolygonAnnotation(
        document.pages[1],
        ap.Rectangle(200, 300, 400, 400, True),
        [
            ap.Point(200, 300),
            ap.Point(220, 300),
            ap.Point(250, 330),
            ap.Point(300, 304),
            ap.Point(300, 400),
        ],
    )
    polygonAnnotation.title = "John Smith"
    polygonAnnotation.color = ap.Color.blue
    polygonAnnotation.interior_color = ap.Color.blue_violet
    polygonAnnotation.opacity = 0.25

    document.pages[1].annotations.append(polygonAnnotation)
    document.save(output_file)
```

O trecho de código a seguir mostra como adicionar Anotações de Polilinha a um arquivo PDF:

1. Carregue o arquivo PDF - novo [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crie novas [Anotações de Polilinha](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) e defina os parâmetros do Polígono (novo Rectangle, novos Points, título, cor, interior_color e opacidade).
1. Em seguida, podemos adicionar as anotações à página.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    polylineAnnotation = ap.annotations.PolylineAnnotation(
        document.pages[1],
        ap.Rectangle(270, 193, 571, 383, True),
        [
            ap.Point(545, 150),
            ap.Point(545, 190),
            ap.Point(667, 190),
            ap.Point(667, 110),
            ap.Point(626, 111),
        ],
    )
    polylineAnnotation.title = "John Smith"
    polylineAnnotation.color = ap.Color.red
    polylineAnnotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1], ap.Rectangle(842, 196, 1021, 338, True)
    )

    document.pages[1].annotations.append(polylineAnnotation)
    document.save(output_file)
```

### Obter Anotações de Polígono e Polilinha

Por favor, tente usar o trecho de código a seguir para obter Anotações de Polígono em um documento PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polygonAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLYGON)
    ]

    for pa in polygonAnnotations:
        print(pa.rect)
```

Por favor, tente usar o trecho de código a seguir para obter Anotações de Polilinha em um documento PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polylineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLY_LINE)
    ]

    for pa in polylineAnnotations:
        print(pa.rect)
```

### Excluir Anotações de Polígono e Polilinha

O trecho de código a seguir mostra como excluir Anotações de Polígono de um arquivo PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polygonAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLYGON)
    ]

    for pa in polygonAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

O trecho de código a seguir mostra como excluir anotações de polilinha de um arquivo PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polylineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLY_LINE)
    ]

    for pa in polylineAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```


