---
title: Modifier la taille de la page PDF avec Python
linktitle: Modifier la taille de la page PDF
type: docs
weight: 60
url: fr/python-net/change-page-size/
description: Modifiez la taille des pages de votre document PDF à l'aide de la bibliothèque Aspose.PDF pour Python via .NET.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Modifier la taille de la page PDF avec Python",
    "alternativeHeadline": "Redimensionner la page PDF avec Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents pdf",
    "keywords": "pdf, python, changer taille pdf, redimensionner pdf",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Équipe de documentation Aspose.PDF",
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
    "url": "/python-net/change-page-size/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/change-page-size/"
    },
    "dateModified": "2023-04-04",
    "description": "Modifiez la taille des pages de votre document PDF à l'aide de la bibliothèque Aspose.PDF pour Python via .NET."
}
</script>


## Changer la Taille des Pages PDF

Aspose.PDF pour Python via .NET vous permet de changer la taille des pages PDF avec quelques lignes de code dans vos applications Python. Ce sujet explique comment mettre à jour/modifier les dimensions des pages (taille) d'un fichier PDF existant.

La classe [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) contient la méthode [set_page_size()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) qui vous permet de définir la taille de la page. L'extrait de code ci-dessous met à jour les dimensions de la page en quelques étapes simples :

1. Charger le fichier PDF source.
2. Obtenir les pages dans l'objet [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
3. Obtenir une page donnée.
4. Appeler la méthode set_page_size() pour mettre à jour ses dimensions.
5. Appeler la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) de la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) pour générer le fichier PDF avec les dimensions de page mises à jour.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)

    # Obtenir une page en particulier
    page = document.pages[1]

    # Définir la taille de la page en A4 (11,7 x 8,3 pouces) et dans Aspose.Pdf, 1 pouce = 72 points
    # Donc les dimensions A4 en points seront (842.4, 597.6)
    page.set_page_size(597.6, 842.4)

    # Enregistrer le document mis à jour
    document.save(output_pdf)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF pour .NET Library",
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
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>