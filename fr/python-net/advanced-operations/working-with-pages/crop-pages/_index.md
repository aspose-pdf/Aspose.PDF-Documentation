---
title: Rogner les pages PDF par programmation en Python
linktitle: Rogner les pages
type: docs
weight: 70
url: fr/python-net/crop-pages/
description: Vous pouvez obtenir les propriétés des pages, telles que la largeur, la hauteur, bleed-, crop- et trimbox en utilisant Aspose.PDF pour Python via .NET.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Rogner les pages PDF par programmation en Python",
    "alternativeHeadline": "Comment rogner les pages PDF en Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de document pdf",
    "keywords": "pdf, python, rogner les pages pdf",
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
    "url": "/python-net/crop-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/crop-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Vous pouvez obtenir les propriétés des pages, telles que la largeur, la hauteur, bleed-, crop- et trimbox en utilisant Aspose.PDF pour Python via .NET."
}
</script>


## Obtenir les Propriétés de la Page

Chaque page d'un fichier PDF possède un certain nombre de propriétés, telles que la largeur, la hauteur, le bleed-, le crop- et le trimbox. Aspose.PDF pour Python vous permet d'accéder à ces propriétés.

- **media_box**: La media box est la plus grande boîte de page. Elle correspond à la taille de la page (par exemple A4, A5, US Letter, etc.) sélectionnée lorsque le document a été imprimé en PostScript ou PDF. En d'autres termes, la media box détermine la taille physique du support sur lequel le document PDF est affiché ou imprimé.
- **bleed_box**: Si le document a un bleed, le PDF aura également une bleed box. Le bleed est la quantité de couleur (ou d'œuvre) qui dépasse le bord d'une page. Il est utilisé pour s'assurer que lorsque le document est imprimé et coupé à la taille ("découpé"), l'encre ira jusqu'au bord de la page. Même si la page est mal découpée - coupée légèrement en dehors des marques de coupe - aucun bord blanc n'apparaîtra sur la page.
- **trim_box**: La trim box indique la taille finale d'un document après impression et découpe.
- **art_box**: La art box est la boîte dessinée autour du contenu réel des pages dans vos documents.
 Cette boîte de page est utilisée lors de l'importation de documents PDF dans d'autres applications.
- **crop_box**: La boîte de recadrage est la taille de "page" à laquelle votre document PDF est affiché dans Adobe Acrobat. En vue normale, seuls les contenus de la boîte de recadrage sont affichés dans Adobe Acrobat. Pour des descriptions détaillées de ces propriétés, lisez la spécification Adobe.Pdf, en particulier 10.10.1 Page Boundaries.

L'extrait ci-dessous montre comment recadrer la page :

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)

    # Créer un nouveau Rectangle Box
    new_box = ap.Rectangle(200, 220, 2170, 1520, True)
    document.pages[1].crop_box = new_box
    document.pages[1].trim_box = new_box
    document.pages[1].art_box = new_box
    document.pages[1].bleed_box = new_box

    document.save(output_pdf)
```

Dans cet exemple, nous avons utilisé un fichier d'exemple [ici](crop_page.pdf). Initialement, notre page ressemble à ce qui est montré sur la Figure 1.
![Figure 1. Page Recadrée](crop_page.png)

Après la modification, la page ressemblera à la Figure 2.
![Figure 2. Page rognée](crop_page2.png)

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
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>