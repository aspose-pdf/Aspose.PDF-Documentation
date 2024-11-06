---
title: Travailler avec un Portfolio en PDF en utilisant Python
linktitle: Portfolio
type: docs
weight: 20
url: fr/python-net/portfolio/
description: Comment créer un portfolio PDF avec Python. Vous devez utiliser un fichier Microsoft Excel, un document Word et un fichier image pour créer un portfolio PDF.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Travailler avec un Portfolio en PDF en utilisant Python",
    "alternativeHeadline": "Créer un Portfolio dans un document PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de document pdf en pdf",
    "keywords": "pdf, python, portfolio",
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
    "url": "/python-net/portfolio/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/portfolio/"
    },
    "dateModified": "2023-02-04",
    "description": "Comment créer un portfolio PDF avec Python. Vous devez utiliser un fichier Microsoft Excel, un document Word et un fichier image pour créer un portfolio PDF."
}
</script>


Créer un portfolio PDF permet de consolider et d'archiver différents types de fichiers en un seul document cohérent. Un tel document pourrait inclure des fichiers texte, des images, des feuilles de calcul, des présentations et d'autres matériaux, et garantir que tous les éléments pertinents sont stockés et organisés au même endroit.

Le portfolio PDF vous aidera à présenter votre travail de manière haute qualité, où que vous l'utilisiez. En général, créer un portfolio PDF est une tâche très actuelle et moderne.

## Comment Créer un Portfolio PDF

Aspose.PDF pour Python via .NET permet de créer des documents de Portfolio PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Ajoutez un fichier dans un objet document.collection après l'avoir obtenu avec la classe [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/). Une fois les fichiers ajoutés, utilisez la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) de la classe Document pour enregistrer le document de portfolio.

L'exemple suivant utilise un fichier Microsoft Excel, un document Word et un fichier image pour créer un Portfolio PDF.

Le code ci-dessous donne le résultat suivant pour le portfolio.

### Un portfolio PDF créé avec Aspose.PDF pour Python

![Un portfolio PDF créé avec Aspose.PDF pour Python](working-with-pdf-portfolio_1.jpg)

```python

    import aspose.pdf as ap

    # Instancier l'objet Document
    document = ap.Document()

    # Instancier l'objet Collection de document
    document.collection = ap.Collection()

    # Obtenir les fichiers à ajouter au portfolio
    excel = ap.FileSpecification(input_excel)
    word = ap.FileSpecification(input_doc)
    image = ap.FileSpecification(input_jpg)

    # Fournir la description des fichiers
    excel.description = "Fichier Excel"
    word.description = "Fichier Word"
    image.description = "Fichier Image"

    # Ajouter des fichiers à la collection de documents
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # Enregistrer le document de portfolio
    document.save(output_pdf)
```

## Supprimer des fichiers du portfolio PDF

Pour supprimer/enlever des fichiers du portfolio PDF, essayez d'utiliser les lignes de code suivantes.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)
    document.collection.delete()

    # Enregistrer le fichier mis à jour
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