---
title: Annotations supplémentaires en utilisant Python
linktitle: Annotations supplémentaires
type: docs
weight: 60
url: fr/python-net/extra-annotations/
description: Cette section décrit comment ajouter, obtenir et supprimer des types supplémentaires d'annotations de votre document PDF.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Annotations supplémentaires en utilisant Python",
    "alternativeHeadline": "Comment ajouter des annotations supplémentaires dans un PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents pdf",
    "keywords": "pdf, python, annotation de lien, annotation de caret",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Équipe Aspose.PDF Doc",
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
    "url": "/python-net/extra-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/extra-annotations/"
    },
    "dateModified": "2023-02-04",
    "description": "Cette section décrit comment ajouter, obtenir et supprimer des types supplémentaires d'annotations de votre document PDF avec Python."
}
</script>


## Comment ajouter une annotation de type Caret dans un fichier PDF existant via Python

Une annotation de type Caret est un symbole qui indique l'édition de texte. L'annotation Caret est également une annotation de balisage, donc la classe Caret dérive de la classe Markup et fournit également des fonctions pour obtenir ou définir les propriétés de l'annotation Caret et réinitialiser le flux de l'apparence de l'annotation Caret. Les annotations Caret sont souvent utilisées pour suggérer des modifications, des ajouts ou des changements au texte.

Étapes avec lesquelles nous créons une annotation Caret :

1. Charger le fichier PDF - nouveau [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. Créer une nouvelle [CaretAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/caretannotation/) et définir les paramètres du Caret (nouveau Rectangle, titre, sujet, drapeaux, couleur). Cette annotation est utilisée pour indiquer l'insertion de texte.
3. Une fois que nous sommes en mesure d'ajouter des annotations à la page.

Le fragment de code suivant montre comment ajouter une annotation Caret à un fichier PDF :

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_file)

    caretAnnotation1 = ap.annotations.CaretAnnotation(
        document.pages[1], ap.Rectangle(200, 700.664, 308.708, 740.769, True)
    )
    caretAnnotation1.title = "Utilisateur Aspose"
    caretAnnotation1.subject = "Texte inséré 1"
    caretAnnotation1.flags = ap.annotations.AnnotationFlags.PRINT
    caretAnnotation1.color = ap.Color.blue

    document.pages[1].annotations.append(caretAnnotation1)
    document.save(output_file)
```


### Obtenir l'Annotation Caret

Veuillez essayer d'utiliser l'extrait de code suivant pour obtenir l'annotation Caret dans le document PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    caretAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CARET)
    ]

    for ca in caretAnnotations:
        print(ca.rect)
```

### Supprimer l'Annotation Caret

L'extrait de code suivant montre comment supprimer l'annotation Caret d'un fichier PDF en utilisant Python.

```python

    import aspose.pdf as ap

    # Charger le fichier PDF
    document = ap.Document(input_file)
    caretAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CARET)
    ]

    for ca in caretAnnotations:
        document.pages[1].annotations.delete(ca)

    document.save(output_file)
```

## Ajouter une Annotation de Lien

[Les liens](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/) sont des annotations qui ouvrent des URL ou se déplacent vers certaines positions à l'intérieur du même document ou d'un document externe lorsque vous cliquez.

A Link Annotations est une zone rectangulaire qui peut être placée n'importe où sur la page. Chaque lien a une action PDF correspondante qui lui est associée. Cette action est effectuée lorsque l'utilisateur clique dans la zone de ce lien.

Le code suivant montre comment ajouter une Annotation de Lien à un fichier PDF en utilisant un exemple de numéro de téléphone :

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # Créer un objet TextFragmentAbsorber pour trouver un numéro de téléphone
    textFragmentAbsorber = ap.text.TextFragmentAbsorber("file")

    # Accepter l'absorbeur uniquement pour la 1ère page
    document.pages[1].accept(textFragmentAbsorber)

    phoneNumberFragment = textFragmentAbsorber.text_fragments[1]

    # Créer une Annotation de Lien et définir l'action pour appeler un numéro de téléphone
    linkAnnotation = ap.annotations.LinkAnnotation(document.pages[1], phoneNumberFragment.rectangle)
    linkAnnotation.action = ap.annotations.GoToURIAction("www.aspose.com")

    # Ajouter l'annotation à la page
    document.pages[1].annotations.append(linkAnnotation)
    document.save(output_file)
```


### Obtenir l'Annotation de Lien

Veuillez essayer d'utiliser l'extrait de code suivant pour obtenir [LinkAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/) à partir d'un document PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    linkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in linkAnnotations:
        print(la.rect)
```

### Supprimer l'Annotation de Lien

L'extrait de code suivant montre comment supprimer l'annotation de lien d'un fichier PDF. Pour cela, nous devons trouver et supprimer toutes les annotations de lien sur la première page. Après cela, nous enregistrerons le document avec l'annotation supprimée.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(output_file)
```


## Rédiger une certaine région de page avec l'annotation de rédaction en utilisant Aspose.PDF pour Python

Aspose.PDF pour Python via .NET prend en charge la fonctionnalité d'ajout ainsi que la manipulation des annotations dans un fichier PDF existant. Les annotations de rédaction dans les documents PDF servent à supprimer ou masquer de manière permanente des informations confidentielles du document. Le processus d'édition des informations implique de couvrir ou d'assombrir un contenu spécifique, tel que du texte, des images ou des graphiques, de manière à restreindre sa visibilité et son accessibilité par d'autres. Cela garantit que les informations sensibles restent cachées et protégées au sein du document. Afin de répondre à cette exigence, une classe nommée [RedactionAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/redactionannotation/) est fournie, qui peut être utilisée pour rédiger certaines régions de page ou elle peut être utilisée pour manipuler des RedactionAnnotations existantes et les rédiger (c'est-à-dire aplatir l'annotation et supprimer le texte en dessous).

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    page = document.pages[1]
    redactionAnnotation = ap.annotations.RedactionAnnotation(page, ap.Rectangle(270, 190, 371, 250, True))
    redactionAnnotation.title = "John Smith"
    redactionAnnotation.fill_color = ap.Color.light_gray
    redactionAnnotation.color = ap.Color.red
    redactionAnnotation.redact()

    page.annotations.append(redactionAnnotation)
    document.save(output_file)
```


### Obtenir l'annotation de rédaction

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    redactionAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.REDACTION)
    ]

    for pa in redactionAnnotations:
        print(pa.rect)
```    

### Supprimer l'annotation de rédaction

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    redactionAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.REDACTION)
    ]

    for pa in redactionAnnotations:
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