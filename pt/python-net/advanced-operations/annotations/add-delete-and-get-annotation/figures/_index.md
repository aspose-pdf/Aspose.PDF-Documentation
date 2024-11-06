---
title: Adicionar Anotações de Figuras usando Python
linktitle: Anotações de Figuras
type: docs
weight: 30
url: pt/python-net/figures-annotation/
description: Este artigo descreve como adicionar, obter e excluir anotações de figuras do seu documento PDF com Aspose.PDF para Python via .NET
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adicionar Anotações de Figuras usando Python",
    "alternativeHeadline": "Como adicionar Anotações de Figuras em PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos pdf",
    "keywords": "pdf, python, anotações de figuras, anotação de polígono, anotação de linha, anotação de quadrado, anotação de círculo",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/figures-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/figures-annotation/"
    },
    "dateModified": "2023-02-04",
    "description": "Este artigo descreve como adicionar, obter e excluir anotações de figuras do seu documento PDF com Aspose.PDF para Python"
}
</script>


## Adicionar Anotações de Quadrado e Círculo

Em documentos PDF, uma anotação de quadrado refere-se a um tipo específico de anotação que é representada por uma forma quadrada. As anotações de quadrado são usadas para destacar ou chamar a atenção para uma área ou seção específica dentro do documento.

As anotações [Quadrado](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation/) e [Círculo](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/circleannotation/) devem exibir, respectivamente, um retângulo ou uma elipse na página.

Passos para criar Anotações de Quadrado ou Círculo:

1. Carregar o arquivo PDF - novo [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. Criar nova [SquareAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation) e definir parâmetros (novo Retângulo, título, cor, cor_interior, opacidade).
3. Depois precisamos Adicionar a Anotação de Quadrado à página.

O trecho de código a seguir mostra como adicionar Anotações de Quadrado em uma página PDF.

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

O seguinte trecho de código mostra como adicionar Anotações de Círculo em uma página PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
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


Como exemplo, veremos o seguinte resultado de adicionar anotações de Quadrado e Círculo a um documento PDF:

![Demonstração de Anotação de Círculo e Quadrado](circle_demo.png)

### Obter Anotação de Círculo

Por favor, tente usar o seguinte trecho de código para Obter Anotação de Círculo do documento PDF.

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

Por favor, tente usar o seguinte trecho de código para Obter Anotação de Quadrado do documento PDF.

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

O trecho de código a seguir mostra como excluir a anotação de círculo de um arquivo PDF.

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

O trecho de código a seguir mostra como excluir a anotação de quadrado de um arquivo PDF.

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

[Anotações de Polígono](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation/) representam polígonos em uma página. Eles podem ter qualquer número de vértices conectados por linhas retas.

[Anotações de Polilinha](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) também são semelhantes a polígonos, a única diferença é que o primeiro e o último vértices não são implicitamente conectados.

Passos com os quais criamos anotações de Polígono:

1. Carregar o arquivo PDF - novo [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Criar nova [Anotação de Polígono](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation) e definir parâmetros do Polígono (novo Retângulo, novos Pontos, título, cor, cor_interior e opacidade).
1. Depois podemos adicionar anotações à página.

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

1. Carregar o arquivo PDF - novo [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Criar novas [Polyline Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) e definir parâmetros do Polígono (novo Retângulo, novos Pontos, título, cor, cor_interior e opacidade).
1. Depois podemos Adicionar anotações à página.

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

Por favor, tente usar o seguinte trecho de código para Obter Anotações de Polígono em documento PDF.

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

Por favor, tente usar o seguinte trecho de código para Obter Anotações de Polilinha em documento PDF.

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

O seguinte trecho de código mostra como Excluir Anotações de Polígono de um arquivo PDF.

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


O seguinte trecho de código mostra como excluir anotações de polilinha de um arquivo PDF.

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

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Biblioteca de Manipulação de PDF para Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>