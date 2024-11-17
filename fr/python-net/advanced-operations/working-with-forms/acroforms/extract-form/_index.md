---
title: Extraire AcroForm - Extraire les données de formulaire d'un PDF en Python
linktitle: Extraire AcroForm
type: docs
weight: 30
url: /fr/python-net/extract-form/
description: Extraire le formulaire de votre document PDF avec la bibliothèque Aspose.PDF pour Python. Obtenez la valeur d'un champ individuel du fichier PDF.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extraire AcroForm",
    "alternativeHeadline": "Comment extraire AcroForm d'un PDF en Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents pdf",
    "keywords": "pdf, python, extraire acroform",
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
            "https://www.youtube.com/@AsposePDF",
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
    "url": "/python-net/extract-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/extract-form/"
    },
    "dateModified": "2023-02-04",
    "description": "Extraire le formulaire de votre document PDF avec la bibliothèque Aspose.PDF pour Python. Obtenez la valeur d'un champ individuel du fichier PDF."
}
</script>


## Extraire des données du formulaire

### Obtenir les valeurs de tous les champs du document PDF

Pour obtenir les valeurs de tous les champs dans un document PDF, vous devez naviguer à travers tous les champs de formulaire et ensuite obtenir la valeur en utilisant la propriété Value. Obtenez chaque champ de la collection Form, dans le type de champ de base appelé [Field](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/) et accédez à sa propriété [value](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/#properties).

Les extraits de code Python suivants montrent comment obtenir les valeurs de tous les champs d'un document PDF.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    pdfDocument = ap.Document(input_file)

    # Obtenir les valeurs de tous les champs
    for formField in pdfDocument.form.fields:
        # Analyser les noms et les valeurs si nécessaire
        print("Nom du champ : " + formField.partial_name)
        print("Valeur : " + str(formField.value))