---
title: Ajouter des tampons texte dans un PDF via Python
linktitle: Tampons texte dans un fichier PDF
type: docs
weight: 20
url: /fr/python-net/text-stamps-in-the-pdf-file/
description: Ajouter un tampon texte à un document PDF en utilisant la classe TextStamp avec la bibliothèque Aspose.PDF pour Python.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ajouter des tampons texte dans un PDF Python",
    "alternativeHeadline": "Ajouter des tampons texte dans un PDF Python",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "génération de document pdf",
    "keywords": "pdf, python, génération de document",
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
    "url": "/python-net/text-stamps-in-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/text-stamps-in-the-pdf-file/"
    },
    "dateModified": "2023-04-04",
    "description": "Ajouter un tampon texte à un document PDF en utilisant la classe TextStamp avec la bibliothèque Aspose.PDF pour Python."
}
</script>


## Ajouter un tampon de texte avec Python

Vous pouvez utiliser la classe [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) pour ajouter un tampon de texte dans un fichier PDF. La classe [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) fournit les propriétés nécessaires pour créer un tampon basé sur du texte comme la taille de la police, le style de la police, la couleur de la police, etc. Pour ajouter un tampon de texte, vous devez créer un objet Document et un objet TextStamp en utilisant les propriétés requises. Après cela, vous pouvez appeler la méthode [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) de la Page pour ajouter le tampon dans le PDF. Le code suivant vous montre comment ajouter un tampon de texte dans le fichier PDF.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)

    # Créer un tampon de texte
    text_stamp = ap.TextStamp("Sample Stamp")
    # Définir si le tampon est en arrière-plan
    text_stamp.background = True
    # Définir l'origine
    text_stamp.x_indent = 100
    text_stamp.y_indent = 100
    # Faire pivoter le tampon
    text_stamp.rotate = ap.Rotation.ON90
    # Définir les propriétés du texte
    text_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_stamp.text_state.font_size = 14.0
    text_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    text_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    text_stamp.text_state.foreground_color = ap.Color.aqua
    # Ajouter le tampon à une page particulière
    document.pages[1].add_stamp(text_stamp)

    # Enregistrer le document de sortie
    document.save(output_pdf)
```


## Définir l'alignement pour l'objet TextStamp

Ajouter des filigranes aux documents PDF est l'une des fonctionnalités fréquemment demandées et Aspose.PDF pour Python est entièrement capable d'ajouter des filigranes d'image ainsi que de texte. Nous avons une classe nommée [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) qui fournit la fonctionnalité d'ajouter des tampons de texte sur le fichier PDF. Récemment, il a été nécessaire de prendre en charge la fonctionnalité de spécifier l'alignement du texte lors de l'utilisation de l'objet TextStamp. Donc, afin de répondre à cette exigence, nous avons introduit la propriété [text_alignment](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) dans la classe [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/). En utilisant cette propriété, nous pouvons spécifier l'alignement du texte [horizontal_alignment](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties).

Les exemples de code suivants montrent comment charger un document PDF existant et y ajouter un TextStamp.

```python

    import aspose.pdf as ap

    # Instancier l'objet Document avec le fichier d'entrée
    doc = ap.Document(input_pdf)
    # Instancier l'objet FormattedText avec une chaîne d'exemple
    text = ap.facades.FormattedText("This")
    # Ajouter une nouvelle ligne de texte à FormattedText
    text.add_new_line_text("is sample")
    text.add_new_line_text("Center Aligned")
    text.add_new_line_text("TextStamp")
    text.add_new_line_text("Object")
    # Créer un objet TextStamp en utilisant FormattedText
    stamp = ap.TextStamp(text)
    # Spécifier l'alignement horizontal du tampon de texte comme centré
    stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Spécifier l'alignement vertical du tampon de texte comme centré
    stamp.vertical_alignment = ap.VerticalAlignment.CENTER
    # Spécifier l'alignement horizontal du texte de TextStamp comme centré
    stamp.text_alignment = ap.HorizontalAlignment.CENTER
    # Définir la marge supérieure pour l'objet tampon
    stamp.top_margin = 20
    # Ajouter l'objet tampon sur la première page du document
    doc.pages[1].add_stamp(stamp)

    # Enregistrer le document mis à jour
    doc.save(output_pdf)
```


## Remplir le Texte de Contour comme un Tampon dans un Fichier PDF

Nous avons implémenté le paramétrage du mode de rendu pour les scénarios d'ajout et d'édition de texte. Pour rendre le texte en contour, veuillez créer un objet TextState pour transférer des propriétés avancées. Définissez la couleur pour le contour. Ensuite, définissez le mode de rendu du texte. L'étape suivante est de lier TextState et d'ajouter le tampon.

Le snippet de code suivant démontre l'ajout de texte de contour rempli :

```python

    import aspose.pdf as ap

    # Créez un objet TextState pour transférer des propriétés avancées
    ts = ap.text.TextState()
    # Définissez la couleur pour le contour
    ts.stroking_color = ap.Color.gray
    # Définissez le mode de rendu du texte
    ts.rendering_mode = ap.text.TextRenderingMode.STROKE_TEXT
    # Chargez un document PDF d'entrée
    file_stamp = ap.facades.PdfFileStamp(ap.Document(input_pdf))

    stamp = ap.facades.Stamp()
    stamp.bind_logo(
        ap.facades.FormattedText(
            "PAID IN FULL",
            ap.facades.FontColor(100, 100, 100),
            ap.facades.FontStyle.TIMES_ROMAN,
            ap.facades.EncodingType.WINANSI,
            True,
            78.0,
        )
    )

    # Liez TextState
    stamp.bind_text_state(ts)
    # Définissez l'origine X,Y
    stamp.set_origin(100, 100)
    stamp.opacity = 5
    stamp.blending_space = ap.facades.BlendingColorSpace.DEVICE_RGB
    stamp.rotation = 45.0
    stamp.is_background = False
    # Ajoutez le tampon
    file_stamp.add_stamp(stamp)
    file_stamp.save(output_pdf)
    file_stamp.close()
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