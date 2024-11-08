---
title: Ajouter un Numéro de Page au PDF avec Python
linktitle: Ajouter un Numéro de Page
type: docs
weight: 30
url: /fr/python-net/add-page-number/
description: Aspose.PDF pour Python via .NET vous permet d'ajouter un tampon de numéro de page à votre fichier PDF en utilisant la classe PageNumberStamp.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ajouter un Numéro de Page au PDF avec Python",
    "alternativeHeadline": "Comment ajouter un tampon de numéro de page au PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents pdf",
    "keywords": "pdf, python, tampon de numéro de page",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Équipe de Documentation Aspose.PDF",
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
    "url": "/python-net/add-page-number/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-page-number/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF pour Python via .NET vous permet d'ajouter un tampon de numéro de page à votre fichier PDF en utilisant la classe PageNumberStamp."
}
</script>


All the documents must have page numbers in it. The page number makes it easier for the reader to locate different parts of the document.  
**Aspose.PDF pour Python via .NET** vous permet d'ajouter des numéros de page avec [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/).

Vous pouvez utiliser la classe [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) pour ajouter un tampon de numéro de page dans un fichier PDF.
 [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) classe fournit les propriétés nécessaires pour créer un tampon basé sur le numéro de page comme le format, les marges, les alignements, le numéro de départ, etc. Afin d'ajouter un tampon de numéro de page, vous devez créer un objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) et un objet [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) en utilisant les propriétés requises. Après cela, vous pouvez appeler la méthode [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) de la [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) pour ajouter le tampon dans le PDF. Vous pouvez également définir les attributs de police du tampon de numéro de page. Le snippet de code suivant vous montre comment ajouter des numéros de page dans un fichier PDF.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)

    # Créer un tampon de numéro de page
    page_number_stamp = ap.PageNumberStamp()
    # Si le tampon est en arrière-plan
    page_number_stamp.background = False
    page_number_stamp.format = "Page # de " + str(len(document.pages))
    page_number_stamp.bottom_margin = 10
    page_number_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    page_number_stamp.starting_number = 1
    # Définir les propriétés du texte
    page_number_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    page_number_stamp.text_state.font_size = 14.0
    page_number_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    page_number_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    page_number_stamp.text_state.foreground_color = ap.Color.aqua

    # Ajouter le tampon à une page particulière
    document.pages[1].add_stamp(page_number_stamp)

    # Enregistrer le document de sortie
    document.save(output_pdf)
```

## Exemple en Direct

[Ajouter des numéros de page au PDF](https://products.aspose.app/pdf/page-number) est une application web gratuite en ligne qui vous permet d'examiner comment fonctionne l'ajout de numéros de page.

[![Comment ajouter un numéro de page dans un PDF en utilisant Python](page_number.png)](https://products.aspose.app/pdf/page-number)

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