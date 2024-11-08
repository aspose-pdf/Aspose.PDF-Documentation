---
title: Ajouter un en-tête et un pied de page au PDF en utilisant Python
linktitle: Ajouter un en-tête et un pied de page au PDF
type: docs
weight: 50
url: /fr/python-net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF pour Python via .NET vous permet d'ajouter des en-têtes et des pieds de page à votre fichier PDF en utilisant la classe TextStamp.
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ajouter un en-tête et un pied de page au PDF en utilisant Python",
    "alternativeHeadline": "Comment ajouter un en-tête et un pied de page à un fichier PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents pdf",
    "keywords": "pdf, python, ajouter en-tête, ajouter pied de page dans pdf",
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
    "url": "/python-net/add-headers-and-footers-of-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-headers-and-footers-of-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF pour Python via .NET vous permet d'ajouter des en-têtes et des pieds de page à votre fichier PDF en utilisant la classe TextStamp."
}
</script>


**Aspose.PDF pour Python via .NET** vous permet d'ajouter un en-tête et un pied de page dans votre fichier PDF existant. Vous pouvez ajouter des images ou du texte à un document PDF. Essayez également d'ajouter différents en-têtes dans un fichier PDF avec Python.

## Ajouter du texte dans l'en-tête du fichier PDF

Vous pouvez utiliser la classe [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) pour ajouter du texte dans l'en-tête d'un fichier PDF. La classe TextStamp fournit les propriétés nécessaires pour créer un tampon basé sur du texte comme la taille de police, le style de police et la couleur de police, etc. Afin d'ajouter du texte dans l'en-tête, vous devez créer un objet Document et un objet TextStamp en utilisant les propriétés requises. Après cela, vous pouvez appeler la méthode 'add_stamp' de la Page pour ajouter le texte dans l'en-tête du PDF.

Vous devez définir la propriété [top_margin](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) de manière à ajuster le texte dans la zone de l'en-tête de votre PDF. Vous devez également définir 'horizontal_alignment' sur Center et 'vertical_alignment' sur Top.

Le snippet de code suivant vous montre comment ajouter du texte dans l'en-tête d'un fichier PDF avec Python :

```python
import aspose.pdf as pdf

# Créer un objet Document
document = pdf.Document("input.pdf")

# Créer un objet TextStamp
text_stamp = pdf.TextStamp("This is a header text")
text_stamp.top_margin = 10
text_stamp.horizontal_alignment = pdf.HorizontalAlignment.Center
text_stamp.vertical_alignment = pdf.VerticalAlignment.Top

# Ajouter le TextStamp à la première page du document PDF
document.pages[1].add_stamp(text_stamp)

# Enregistrer le document mis à jour
document.save("output.pdf")


```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)

    # Créer un en-tête
    textStamp = ap.TextStamp("Texte de l'en-tête")
    # Définir les propriétés du tampon
    textStamp.top_margin = 10
    textStamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    textStamp.vertical_alignment = ap.VerticalAlignment.TOP
    # Ajouter un en-tête sur toutes les pages
    for page in document.pages:
        page.add_stamp(textStamp)

    # Enregistrer le document mis à jour
    document.save(output_pdf)
```

## Ajout de texte dans le pied de page d'un fichier PDF

Vous pouvez utiliser la classe [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) pour ajouter du texte dans le pied de page d'un fichier PDF.
 class TextStamp fournit les propriétés nécessaires pour créer un tampon basé sur du texte comme la taille de la police, le style de la police et la couleur de la police, etc. Pour ajouter du texte dans le pied de page, vous devez créer un objet Document et un objet TextStamp en utilisant les propriétés requises. Après cela, vous pouvez appeler la méthode 'add_stamp' de la Page pour ajouter le texte dans le pied de page du PDF.

Le code suivant vous montre comment ajouter du texte dans le pied de page d'un fichier PDF avec Python :

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)
    # Créer le pied de page
    textStamp = ap.TextStamp("Texte du pied de page")
    # Définir les propriétés du tampon
    textStamp.bottom_margin = 10
    textStamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    textStamp.vertical_alignment = ap.VerticalAlignment.BOTTOM
    # Ajouter le pied de page sur toutes les pages
    for page in document.pages:
        page.add_stamp(textStamp)

    # Enregistrer le fichier PDF mis à jour
    document.save(output_pdf)
```

## Ajouter une image dans l'en-tête d'un fichier PDF

Vous pouvez utiliser la classe [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) pour ajouter une image dans l'en-tête d'un fichier PDF. Image Stamp class fournit les propriétés nécessaires pour créer un tampon basé sur une image, comme la taille de la police, le style de la police et la couleur de la police, etc. Afin d'ajouter une image dans l'en-tête, vous devez créer un objet Document et un objet Image Stamp en utilisant les propriétés requises. Après cela, vous pouvez appeler la méthode 'add_stamp' de la Page pour ajouter l'image dans l'en-tête du PDF.

Le snippet de code suivant vous montre comment ajouter une image dans l'en-tête d'un fichier PDF avec Python :

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)

    # Créer l'en-tête
    image_stamp = ap.ImageStamp(input_image)
    # Définir les propriétés du tampon
    image_stamp.top_margin = 10
    image_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    image_stamp.vertical_alignment = ap.VerticalAlignment.TOP
    # Ajouter l'en-tête sur toutes les pages
    for page in document.pages:
        page.add_stamp(image_stamp)

    # Enregistrer le document mis à jour
    document.save(output_pdf)
```

## Ajouter une image dans le pied de page d'un fichier PDF

Vous pouvez utiliser la classe [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) pour ajouter une image dans le pied de page d'un fichier PDF. [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) classe fournit les propriétés nécessaires pour créer un tampon basé sur une image comme la taille de la police, le style de la police et la couleur de la police, etc. Afin d'ajouter une image dans le pied de page, vous devez créer un objet Document et un objet Image Stamp en utilisant les propriétés requises. Après cela, vous pouvez appeler la méthode 'add_stamp' de la Page pour ajouter l'image dans le pied de page du PDF.

Le code suivant vous montre comment ajouter une image dans le pied de page d'un fichier PDF avec Python :

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)
    # Créer le pied de page
    image_stamp = ap.ImageStamp(input_image)
    # Définir les propriétés du tampon
    image_stamp.bottom_margin = 10
    image_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    image_stamp.vertical_alignment = ap.VerticalAlignment.BOTTOM
    # Ajouter le pied de page sur toutes les pages
    for page in document.pages:
        page.add_stamp(image_stamp)

    # Enregistrer le fichier PDF mis à jour
    document.save(output_pdf)
```

## Ajout de différents en-têtes dans un fichier PDF

Nous savons que nous pouvons ajouter un TextStamp dans la section En-tête/Pied de page du document en utilisant les propriétés [top_margin](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) ou [bottom_margin](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties), mais parfois, nous pouvons avoir besoin d'ajouter plusieurs en-têtes/pieds de page dans un seul document PDF. **Aspose.PDF pour Python via .NET** explique comment faire cela.

Pour répondre à cette exigence, nous créerons des objets TextStamp individuels (le nombre d'objets dépend du nombre d'en-têtes/pieds de page nécessaires) et nous les ajouterons au document PDF.
 Nous pouvons également spécifier des informations de formatage différentes pour chaque objet de tampon individuel. Dans l'exemple suivant, nous avons créé un objet Document et trois objets TextStamp, puis nous avons utilisé la méthode 'add_stamp' de la Page pour ajouter le texte dans la section d'en-tête du PDF. Le fragment de code suivant vous montre comment ajouter une image dans le pied de page d'un fichier PDF avec Aspose.PDF pour Python :

```python

    import aspose.pdf as ap

    # Créer trois tampons
    stamp1 = ap.TextStamp("En-tête 1")
    stamp2 = ap.TextStamp("En-tête 2")
    stamp3 = ap.TextStamp("En-tête 3")

    # Définir l'alignement du tampon (placer le tampon en haut de la page, centré horizontalement)
    stamp1.vertical_alignment = ap.VerticalAlignment.TOP
    stamp1.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Spécifier le style de police comme Gras
    stamp1.text_state.font_style = ap.text.FontStyles.BOLD
    # Définir la couleur du texte en avant-plan comme rouge
    stamp1.text_state.foreground_color = ap.Color.red
    # Spécifier la taille de la police comme 14
    stamp1.text_state.font_size = 14

    # Maintenant, nous devons définir l'alignement vertical du deuxième objet tampon comme Haut
    stamp2.vertical_alignment = ap.VerticalAlignment.TOP
    # Définir les informations d'alignement horizontal pour le tampon comme centré
    stamp2.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Définir le facteur de zoom pour l'objet tampon
    stamp2.zoom = 10

    # Définir le formatage du troisième objet tampon
    # Spécifier les informations d'alignement vertical pour l'objet tampon comme HAUT
    stamp3.vertical_alignment = ap.VerticalAlignment.TOP
    # Définir les informations d'alignement horizontal pour l'objet tampon comme centré
    stamp3.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Définir l'angle de rotation pour l'objet tampon
    stamp3.rotate_angle = 35
    # Définir le rose comme couleur de fond pour le tampon
    stamp3.text_state.background_color = ap.Color.pink
    # Changer les informations de la police pour le tampon en Verdana
    stamp3.text_state.font = ap.text.FontRepository.find_font("Verdana")
    # Le premier tampon est ajouté sur la première page;
    document.pages[1].add_stamp(stamp1)
    # Le deuxième tampon est ajouté sur la deuxième page;
    document.pages[2].add_stamp(stamp2)
    # Le troisième tampon est ajouté sur la troisième page.
    document.pages[3].add_stamp(stamp3)

    # Enregistrer le document mis à jour
    document.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF pour Python via la bibliothèque .NET",
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