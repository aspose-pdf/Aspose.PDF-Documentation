---
title: Ajouter des tampons d'image dans un PDF en utilisant Python
linktitle: Tampons d'image dans un fichier PDF
type: docs
weight: 10
url: fr/python-net/image-stamps-in-pdf-page/
description: Ajoutez le tampon d'image dans votre document PDF en utilisant la classe ImageStamp avec la bibliothèque Aspose.PDF pour Python.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ajouter des tampons d'image dans un PDF en utilisant Python",
    "alternativeHeadline": "Ajouter des tampons d'image dans un PDF en utilisant Python",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "génération de documents pdf",
    "keywords": "pdf, python, génération de documents",
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
    "url": "/python-net/image-stamps-in-pdf-page/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/image-stamps-in-pdf-page/"
    },
    "dateModified": "2023-04-04",
    "description": "Ajoutez le tampon d'image dans votre document PDF en utilisant la classe ImageStamp avec la bibliothèque Aspose.PDF pour Python."
}
</script>


## Ajouter un Tampon d'Image dans un Fichier PDF

Vous pouvez utiliser la classe [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) pour ajouter un tampon d'image à un fichier PDF. La classe [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) fournit les propriétés nécessaires pour créer un tampon basé sur une image, telles que la hauteur, la largeur, l'opacité, etc.

Pour ajouter un tampon d'image :

1. Créez un objet Document et un objet ImageStamp en utilisant les propriétés requises.
1. Appelez la méthode [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) de la classe [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) pour ajouter le tampon au PDF.

Le code suivant montre comment ajouter un tampon d'image dans le fichier PDF.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)

    # Créer un tampon d'image
    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.background = True
    image_stamp.x_indent = 100
    image_stamp.y_indent = 100
    image_stamp.height = 300
    image_stamp.width = 300
    image_stamp.rotate = ap.Rotation.ON270
    image_stamp.opacity = 0.5
    # Ajouter le tampon à une page particulière
    document.pages[1].add_stamp(image_stamp)

    # Enregistrer le document de sortie
    document.save(output_pdf)
```


## Contrôler la Qualité de l'Image lors de l'Ajout d'un Tampon

Lors de l'ajout d'une image en tant qu'objet tampon, vous pouvez contrôler la qualité de l'image. La propriété [quality](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) de la classe [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) est utilisée à cet effet. Elle indique la qualité de l'image en pourcentage (les valeurs valides sont 0..100).

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)

    # Créer un tampon d'image
    image_stamp = ap.ImageStamp(input_jpg)
    image_stamp.quality = 10
    # Ajouter le tampon à une page particulière
    document.pages[1].add_stamp(image_stamp)

    # Enregistrer le document de sortie
    document.save(output_pdf)
```

## Tampon d'Image en tant qu'Arrière-plan dans une Boîte Flottante

L'API Aspose.PDF pour Python vous permet d'ajouter un tampon d'image en tant qu'arrière-plan dans une boîte flottante.
 Le [propriété de fond](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) de la classe [FloatingBox](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) peut être utilisée pour définir le tampon d'image de fond pour une boîte flottante comme indiqué dans l'exemple de code suivant.

```python

    import aspose.pdf as ap

    # Instancier l'objet Document
    document = ap.Document()
    # Ajouter une page au document PDF
    page = document.pages.add()
    # Créer un objet FloatingBox
    box = ap.FloatingBox(200.0, 100.0)
    # Définir la position gauche pour FloatingBox
    box.left = 40
    # Définir la position supérieure pour FloatingBox
    box.top = 80
    # Définir l'alignement horizontal pour FloatingBox
    box.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Ajouter un fragment de texte à la collection de paragraphes de FloatingBox
    box.paragraphs.add(ap.text.TextFragment("texte principal"))
    # Définir la bordure pour FloatingBox
    box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    img = ap.Image()
    img.file = input_image_file
    # Ajouter une image de fond
    box.background_image = img
    # Définir la couleur de fond pour FloatingBox
    box.background_color = ap.Color.yellow
    # Ajouter FloatingBox à la collection de paragraphes de l'objet page
    page.paragraphs.add(box)
    # Enregistrer le document PDF
    document.save(output_pdf)
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
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>