---
title: Suppression de pièce jointe d'un PDF à l'aide de Python
linktitle: Suppression de pièce jointe d'un PDF existant
type: docs
weight: 30
url: /python-net/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF peut supprimer les pièces jointes de vos documents PDF. Utilisez l'API PDF Python pour supprimer les pièces jointes dans les fichiers PDF à l'aide de la bibliothèque Aspose.PDF pour Python via .NET.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Suppression de pièce jointe d'un PDF",
    "alternativeHeadline": "Comment supprimer des pièces jointes d'un PDF avec Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, python, supprimer pièces jointes",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Équipe Doc Aspose.PDF",
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
                "contactType": "vente",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vente",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vente",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/removing-attachment-from-an-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/removing-attachment-from-an-existing-pdf/"
    },
    "dateModified": "2023-02-04",
    "description": "Aspose.PDF pour Python peut supprimer les pièces jointes de vos documents PDF. Utilisez l'API PDF Python pour supprimer les pièces jointes dans les fichiers PDF à l'aide de la bibliothèque Aspose.PDF."
}
</script>


Aspose.PDF pour Python peut supprimer des pièces jointes des fichiers PDF. Les pièces jointes d'un document PDF sont contenues dans la collection [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) de l'objet Document.

Pour supprimer toutes les pièces jointes associées à un fichier PDF :

1. Appelez la méthode [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) de la collection [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/).
2. Enregistrez le fichier mis à jour en utilisant la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) de l'objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Le code suivant montre comment supprimer des pièces jointes d'un document PDF.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)

    # Supprimer toutes les pièces jointes
    document.embedded_files.delete()

    # Enregistrer le fichier mis à jour
    document.save(output_pdf)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF pour Python Library",
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
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>