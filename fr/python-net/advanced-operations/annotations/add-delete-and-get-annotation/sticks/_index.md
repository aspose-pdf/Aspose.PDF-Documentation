---
title: Annotations autocollantes PDF avec Python
linktitle: Annotation autocollante
type: docs
weight: 50
url: /fr/python-net/sticky-annotations/
description: Découvrez comment ajouter des annotations autocollantes dans les documents PDF en utilisant Aspose.PDF avec Python via .NET pour les commentaires et les retours.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guide sur la façon de manipuler les annotations autocollantes dans un PDF
Abstract: Cet article fournit un guide détaillé sur la façon de gérer les annotations filigrane dans les documents PDF en utilisant la bibliothèque Aspose.PDF pour Python. Il explique le processus d'ajout, de récupération et de suppression des annotations filigrane afin d'assurer l'authenticité et le branding du document. L'annotation filigrane peut être utilisée pour intégrer des graphiques, tels que des logos, à une taille et une position fixes sur une page. Le guide comprend des extraits de code montrant comment ajouter une annotation filigrane à une position spécifique avec une opacité réglable, ainsi que comment récupérer et supprimer les annotations filigrane existantes. Les exemples de code illustrent l'utilisation de la bibliothèque Aspose.PDF pour manipuler les documents PDF de manière programmatique, offrant une approche pratique aux développeurs pour intégrer les fonctionnalités de filigrane dans leurs applications.
---

## Ajouter une annotation filigrane

L'annotation filigrane est la plus visible et la plus facile à visualiser et à transmettre. C'est le meilleur moyen de placer dans votre document PDF un logo ou tout autre signe qui confirme son originalité.

Une annotation filigrane doit être utilisée pour représenter des graphiques qui seront imprimés à une taille et à une position fixes sur une page, indépendamment des dimensions de la page imprimée.

Vous pouvez ajouter du texte filigrane en utilisant [WatermarkAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/watermarkannotation/) à une position spécifique de la page PDF. L'opacité du filigrane peut également être contrôlée en utilisant la propriété [opacity](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/watermarkannotation/#properties).

Veuillez consulter l'extrait de code suivant pour ajouter WatermarkAnnotation.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # Create Annotation
    # Load Page object to add Annotation
    page = document.pages[1]

    # Create Annotation
    wa = ap.annotations.WatermarkAnnotation(page, ap.Rectangle(100, 0, 400, 100, True))

    # Add annotaiton into Annotation collection of Page
    page.annotations.append(wa)

    # Create TextState for Font settings
    ts = ap.text.TextState()
    ts.foreground_color = ap.Color.blue
    ts.font_size = 25
    ts.font = ap.text.FontRepository.find_font("Arial");

    # Set opacity level of Annotaiton Text
    wa.opacity = 0.5

    # Add Text in Annotation
    wa.set_text_and_state([ "HELLO", "Line 1", "Line 2" ], ts)

    document.save(output_file)
```

## Récupérer l'annotation filigrane

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    watermarkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.WATERMARK)
    ]

    for ta in watermarkAnnotations:
        print(ta.rect)
```

## Supprimer l'annotation filigrane

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    watermarkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.WATERMARK)
    ]

    for ta in watermarkAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```


