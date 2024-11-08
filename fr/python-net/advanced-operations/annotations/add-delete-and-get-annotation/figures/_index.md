---
title: Ajouter des Annotations de Figures en utilisant Python
linktitle: Annotations de Figures
type: docs
weight: 30
url: /fr/python-net/figures-annotation/
description: Cet article décrit comment ajouter, obtenir et supprimer des annotations de figures de votre document PDF avec Aspose.PDF pour Python via .NET
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ajouter des Annotations de Figures en utilisant Python",
    "alternativeHeadline": "Comment ajouter des Annotations de Figures dans un PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de document pdf",
    "keywords": "pdf, python, annotations de figures, annotation de polygone, annotation de ligne, annotation de carré, annotation de cercle",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
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
    "url": "/python-net/figures-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/figures-annotation/"
    },
    "dateModified": "2023-02-04",
    "description": "Cet article décrit comment ajouter, obtenir et supprimer des annotations de figures de votre document PDF avec Aspose.PDF pour Python"
}
</script>


## Ajouter des annotations carrées et circulaires

Dans les documents PDF, une annotation carrée se réfère à un type spécifique d'annotation représentée par une forme carrée. Les annotations carrées sont utilisées pour mettre en évidence ou attirer l'attention sur une zone ou une section spécifique du document.

Les annotations [Carré](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation/) et [Cercle](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/circleannotation/) doivent afficher, respectivement, un rectangle ou une ellipse sur la page.

Étapes pour créer des annotations carrées ou circulaires :

1. Charger le fichier PDF - nouveau [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. Créer une nouvelle [SquareAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation) et définir les paramètres (nouveau Rectangle, titre, couleur, couleur intérieure, opacité).
3. Ensuite, nous devons ajouter l'annotation carrée à la page.

Le code suivant vous montre comment ajouter des annotations carrées dans une page PDF.

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

Le code suivant vous montre comment ajouter des annotations de cercle dans une page PDF.

```python

    import aspose.pdf as ap

    # Ouvrir le document
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


En tant qu'exemple, nous verrons le résultat suivant de l'ajout d'annotations Carré et Cercle à un document PDF :

![Démonstration d'annotation Cercle et Carré](circle_demo.png)

### Obtenir l'annotation Cercle

Veuillez essayer d'utiliser l'extrait de code suivant pour obtenir l'annotation Cercle à partir d'un document PDF.

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

### Obtenir l'annotation Carré

Veuillez essayer d'utiliser l'extrait de code suivant pour obtenir l'annotation Carré à partir d'un document PDF.

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



### Supprimer l'annotation Cercle

Le extrait de code suivant montre comment supprimer une annotation de cercle d'un fichier PDF.

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

### Supprimer une Annotation Carrée

Le extrait de code suivant montre comment supprimer une annotation carrée d'un fichier PDF.

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

## Ajouter des Annotations Polygone et Polyligne

L'outil Polyligne vous permet de créer des formes et des contours avec un nombre arbitraire de côtés sur le document.

[Annotations de Polygone](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation/) représentent des polygones sur une page. Ils peuvent avoir n'importe quel nombre de sommets connectés par des lignes droites.

[Annotations de Polyline](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) sont également similaires aux polygones, la seule différence est que les premiers et derniers sommets ne sont pas implicitement connectés.

Étapes avec lesquelles nous créons des annotations de polygone :

1. Charger le fichier PDF - nouveau [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Créer une nouvelle [Annotation de Polygone](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation) et définir les paramètres du polygone (nouveau Rectangle, nouveaux Points, titre, couleur, couleur intérieure et opacité).
1. Après, nous pouvons ajouter des annotations à la page.

Le fragment de code suivant montre comment ajouter des annotations de polygone à un fichier PDF :

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


The following code snippet shows how to add Polyline Annotations to a PDF file:

1. Charger le fichier PDF - nouveau [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Créer de nouvelles [Annotations de polyligne](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) et définir les paramètres du polygone (nouveau Rectangle, nouveaux Points, titre, couleur, couleur intérieure et opacité).
1. Ensuite, nous pouvons ajouter des annotations à la page.

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


### Obtenir des annotations de polygone et de polyligne

Veuillez essayer d'utiliser le code suivant pour obtenir des annotations de polygone dans un document PDF.

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

Veuillez essayer d'utiliser le code suivant pour obtenir des annotations de polyligne dans un document PDF.

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

### Supprimer les annotations de polygone et de polyligne

Le code suivant montre comment supprimer des annotations de polygone d'un fichier PDF.

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


Le fragment de code suivant montre comment supprimer des annotations de polyligne d'un fichier PDF.

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
    "name": "Aspose.PDF pour la bibliothèque Python",
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
                "contactType": "ventes",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventes",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventes",
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
    "applicationCategory": "Bibliothèque de manipulation PDF pour Python",
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