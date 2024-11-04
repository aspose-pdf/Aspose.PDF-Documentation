---
title: Obtenir, Mettre à Jour et Développer un Signet en utilisant Python
linktitle: Obtenir, Mettre à Jour et Développer un Signet
type: docs
weight: 20
url: /python-net/get-update-and-expand-bookmark/
description: Cet article décrit comment utiliser les signets dans un fichier PDF avec notre bibliothèque Aspose.PDF pour Python.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Obtenir, Mettre à Jour et Développer un Signet avec Python",
    "alternativeHeadline": "Comment obtenir des Signets à partir d'un fichier PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents pdf",
    "keywords": "pdf, python, obtenir des signets",
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
    "url": "/python-net/get-update-and-expand-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/get-update-and-expand-bookmark/"
    },
    "dateModified": "2023-02-04",
    "description": "Cet article décrit comment utiliser les signets dans un fichier PDF avec notre bibliothèque Aspose.PDF pour Python."
}
</script>


## Obtenez les Signets

La collection [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) de l'objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) contient tous les signets d'un fichier PDF. Cet article explique comment obtenir des signets à partir d'un fichier PDF et comment savoir sur quelle page se trouve un signet particulier.

Pour obtenir les signets, parcourez la collection [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) et obtenez chaque signet dans la OutlineItemCollection. La [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) permet d'accéder à tous les attributs du signet. Le snippet de code suivant vous montre comment obtenir des signets à partir du fichier PDF.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)

    # Parcourir tous les signets
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
```


## Obtenir le Numéro de Page d'un Signet

Une fois que vous avez ajouté un signet, vous pouvez savoir sur quelle page il se trouve en obtenant le numéro de page de destination associé à l'objet Signet.

```python

    import aspose.pdf as ap

    # Créer PdfBookmarkEditor
    bookmarkEditor = ap.facades.PdfBookmarkEditor()
    # Ouvrir le fichier PDF
    bookmarkEditor.bind_pdf(input_pdf)
    # Extraire les signets
    bookmarks = bookmarkEditor.extract_bookmarks()
    for bookmark in bookmarks:
        str_level_seprator = ""
        for i in range(bookmark.level):
            str_level_seprator += "----"

        print(str_level_seprator, "Titre :", bookmark.title)
        print(str_level_seprator, "Numéro de Page :", bookmark.page_number)
        print(str_level_seprator, "Action de Page :", bookmark.action)
```

## Obtenir les Signets Enfants d'un Document PDF

Les signets peuvent être organisés dans une structure hiérarchique, avec des parents et des enfants.
 Pour obtenir tous les signets, parcourez les collections Outlines de l'objet Document. Cependant, pour obtenir également les signets enfants, parcourez également tous les signets dans chaque objet [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) obtenu dans la première boucle. Les extraits de code suivants montrent comment obtenir les signets enfants d'un document PDF.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)

    # Parcourir tous les signets
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
        count = len(outline_item)
        if count > 0:
            print("Signets enfants")
            # Il y a des signets enfants, alors parcourez-les également
            for j in range(len(outline_item)):
                child_outline_item = outline_item[i + 1]
                print(child_outline_item.title)
                print(child_outline_item.italic)
                print(child_outline_item.bold)
                print(child_outline_item.color)
```

## Mettre à jour les signets dans un document PDF

Pour mettre à jour un signet dans un fichier PDF, d'abord, obtenez le signet particulier de la collection OutlineCollection de l'objet Document en spécifiant l'index du signet. Une fois que vous avez récupéré le signet dans l'objet [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), vous pouvez mettre à jour ses propriétés puis enregistrer le fichier PDF mis à jour en utilisant la méthode Save. Les extraits de code suivants montrent comment mettre à jour les signets dans un document PDF.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)

    # Obtenir un objet signet
    outline = document.outlines[1]

    # Obtenir l'objet signet enfant
    child_outline = outline[1]
    child_outline.title = "Outline mis à jour"
    child_outline.italic = True
    child_outline.bold = True

    # Enregistrer la sortie
    document.save(output_pdf)
```

## Signets développés lors de la visualisation du document

Les signets sont détenus dans la collection [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) de l'objet Document, elle-même dans la collection [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
 Cependant, nous pouvons avoir besoin que tous les signets soient développés lors de la visualisation du fichier PDF.

Afin de satisfaire cette exigence, nous pouvons définir le statut ouvert pour chaque élément de plan/signet comme Ouvert. Le snippet de code suivant vous montre comment définir le statut ouvert pour chaque signet comme développé dans un document PDF.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)

    # Définir le mode d'affichage de la page, c'est-à-dire afficher les miniatures, plein écran, afficher le panneau des pièces jointes
    document.page_mode = ap.PageMode.USE_OUTLINES
    # Parcourir chaque élément de plan dans la collection de plans du fichier PDF
    for i in range(len(document.outlines)):
        item = document.outlines[i + 1]
        # Définir le statut ouvert pour l'élément de plan
        item.open = True

    # Enregistrer la sortie
    document.save(output_pdf)
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
    "applicationCategory": "PDF Manipulation Library for Python",
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