---
title: Comment Fusionner des PDF en utilisant Python
linktitle: Fusionner des fichiers PDF
type: docs
weight: 50
url: fr/python-net/merge-pdf-documents/
keywords: "fusionner plusieurs pdf en un seul pdf python, combiner plusieurs pdf en un seul python, fusionner plusieurs pdf en un seul python"
description: Cette page explique comment fusionner des documents PDF en un seul fichier PDF avec Python.
lastmod: "2023-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Comment Fusionner des PDF en utilisant Python",
    "alternativeHeadline": "Combiner des documents PDF via Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "manipulation de documents pdf",
    "keywords": "pdf, python, fusionner pdf, concaténer, combiner pdf",
    "wordcount": "212",
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
    "url": "https://docs.aspose.com/pdf/python-net/merge-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://docs.aspose.com/pdf/python-net/merge-pdf-documents/"
    },
    "dateModified": "2023-04-14",
    "description": "Cette page explique comment fusionner des documents PDF en un seul fichier PDF avec Python via .NET."
}
</script>


## Fusionner ou combiner plusieurs PDF en un seul PDF en Python

Combiner des fichiers PDF est une requête très populaire parmi les utilisateurs. Cela peut être utile lorsque vous avez plusieurs fichiers PDF que vous souhaitez partager ou stocker ensemble en tant qu'un seul document.

Fusionner des fichiers PDF peut vous aider à organiser vos documents, à libérer de l'espace de stockage sur votre PC et à partager plusieurs fichiers PDF avec d'autres en les combinant en un seul document.

Fusionner des PDF en Python via .NET n'est pas une tâche simple sans utiliser une bibliothèque tierce. Cet article montre comment fusionner plusieurs fichiers PDF en un seul document PDF en utilisant Aspose.PDF pour Python via .NET.

## Fusionner des fichiers PDF en utilisant Python et DOM

Pour concaténer deux fichiers PDF :

1. Créez deux objets [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), chacun contenant l'un des fichiers PDF d'entrée.

1. Ensuite, appelez la méthode [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) de la collection [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) pour l'objet Document auquel vous souhaitez ajouter l'autre fichier PDF.
1. Passez la collection PageCollection du deuxième objet Document à la méthode [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) de la première collection PageCollection.
1. Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

Le snippet de code suivant montre comment concaténer des fichiers PDF.

```python

    import aspose.pdf as ap

    # Ouvrir le premier document
    document1 = ap.Document(input_pdf_1)
    # Ouvrir le deuxième document
    document2 = ap.Document(input_pdf_2)

    # Ajouter les pages du deuxième document au premier
    document1.pages.add(document2.pages)

    # Enregistrer le fichier de sortie concaténé
    document1.save(output_pdf)
```

## Exemple en direct

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) est une application web gratuite en ligne qui vous permet d'explorer comment fonctionne la fonctionnalité de fusion de présentations.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
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
    "applicationCategory": "Bibliothèque de manipulation de PDF pour Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>