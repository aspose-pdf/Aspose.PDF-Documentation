---
title: Ajouter une pièce jointe à un document PDF en utilisant Python
linktitle: Ajouter une pièce jointe à un document PDF
type: docs
weight: 10
url: /fr/python-net/add-attachment-to-pdf-document/
description: Cette page décrit comment ajouter une pièce jointe à un fichier PDF avec Aspose.PDF pour Python via la bibliothèque .NET.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ajouter une pièce jointe à un document PDF via Python",
    "alternativeHeadline": "Comment ajouter des pièces jointes à un PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents pdf",
    "keywords": "pdf, python, pièces jointes dans pdf",
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
    "url": "/python-net/add-attachment-to-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-attachment-to-pdf-document/"
    },
    "dateModified": "2023-02-04",
    "description": "Cette page décrit comment ajouter une pièce jointe à un fichier PDF avec Aspose.PDF pour Python via la bibliothèque .NET"
}
</script>


Attachments peuvent contenir une grande variété d'informations et peuvent être de différents types de fichiers. Cet article explique comment ajouter une pièce jointe à un fichier PDF.

1. Créez un nouveau projet Python.
1. Importez le package Aspose.PDF
1. Créez un objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Créez un objet [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) avec le fichier que vous ajoutez, et la description du fichier.
1. Ajoutez l'objet [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) à la collection [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) de l'objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), avec la méthode [add](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods).

La collection [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) contient toutes les pièces jointes dans le fichier PDF.
 Le code suivant vous montre comment ajouter une pièce jointe dans un document PDF.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)

    # Configurer le nouveau fichier à ajouter en tant que pièce jointe
    fileSpecification = ap.FileSpecification(attachment_file, "Fichier texte d'exemple")

    # Ajouter la pièce jointe à la collection de pièces jointes du document
    document.embedded_files.append(fileSpecification)

    # Enregistrer la nouvelle sortie
    document.save(output_pdf)
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
        "@type": "Offre",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Bibliothèque de manipulation PDF pour Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "ÉvaluationAgrégée",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>