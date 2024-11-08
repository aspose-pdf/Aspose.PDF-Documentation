---
title: Ajouter une image à un PDF en utilisant Python
linktitle: Ajouter une image
type: docs
weight: 10
url: /fr/python-net/add-image-to-existing-pdf-file/
description: Cette section décrit comment ajouter une image à un fichier PDF existant en utilisant une bibliothèque Python.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ajouter une image à un PDF en utilisant Python",
    "alternativeHeadline": "Comment ajouter une image à un PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents pdf",
    "keywords": "pdf, python, ajouter une image au pdf",
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
    "url": "/python-net/add-image-to-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-image-to-existing-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Cette section décrit comment ajouter une image à un fichier PDF existant en utilisant une bibliothèque Python."
}
</script>


## Ajouter une Image dans un Fichier PDF Existant

Le code suivant montre comment ajouter une image dans le fichier PDF.

1. Chargez le fichier PDF d'entrée.
1. Spécifiez le numéro de page sur lequel l'image sera placée.
1. Pour définir la position de l'image sur la page, appelez la méthode [add_image](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) de la classe [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Appelez la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) de la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_file)

    document.pages[1].add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))

    document.save(output_pdf)
```

## Ajouter une Image dans un Fichier PDF Existant (Facades)

Il existe également une méthode alternative, plus simple pour ajouter une image à un fichier PDF.
 Vous pouvez utiliser la méthode [AddImage](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilemend/methods/addimage/index) de la classe [PdfFileMend](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilemend/). La méthode [add_image()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilemend/#methods) nécessite l'image à ajouter, le numéro de page auquel l'image doit être ajoutée et les informations de coordonnées. Après cela, enregistrez le fichier PDF mis à jour et fermez l'objet PdfFileMend en utilisant la méthode [close()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilemend/#methods). Le code suivant vous montre comment ajouter une image dans un fichier PDF existant.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    mender = ap.facades.PdfFileMend()

    # Créer un objet PdfFileMend pour ajouter du texte
    mender.bind_pdf(input_file)

    # Ajouter une image dans le fichier PDF
    mender.add_image(image_file, 1, 100.0, 600.0, 200.0, 700.0)

    # Enregistrer les modifications
    mender.save(output_pdf)

    # Fermer l'objet PdfFileMend
    mender.close()

```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF pour Python via .NET Library",
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