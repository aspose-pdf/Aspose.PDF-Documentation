---
title: Déterminer le Saut de Ligne
linktitle: Déterminer le Saut de Ligne
type: docs
weight: 70
url: fr/python-net/determine-line-break/
description: Apprenez-en plus sur comment déterminer un saut de ligne d'un TextFragment multi-lignes en utilisant Python
lastmod: "2024-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Déterminer le Saut de Ligne",
    "alternativeHeadline": "Comment déterminer le saut de ligne d'un TextFragment",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents pdf",
    "keywords": "pdf, python, déterminer le saut de ligne",
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
    "url": "/python-net/determine-line-break/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/determine-line-break/"
    },
    "dateModified": "2024-02-04",
    "description": "Apprenez-en plus sur comment déterminer un saut de ligne d'un TextFragment multi-lignes en utilisant Python"
}
</script>


## Suivi de la Césure de Texte Multi-Lignes

Le snippet de code suivant montre comment suivre le comportement de la césure d'un TextFragment multi-lignes dans un document PDF.

La fonction track_line_breaking() est définie pour démontrer cette fonctionnalité. Elle commence par spécifier les chemins des fichiers de sortie pour le document PDF généré et un fichier texte correspondant qui contiendra des informations sur la césure.

Au sein de la fonction, un nouvel objet document PDF est créé, et une nouvelle page y est ajoutée. Par la suite, une boucle est utilisée pour générer quatre instances d'un TextFragment contenant un texte avec des sauts de ligne ("\r\n") insérés dans la chaîne pour simuler un texte multi-lignes.

Chaque TextFragment est configuré avec une taille de police de 20 points avant d'être ajouté aux paragraphes de la page.

Après que tous les TextFragments ont été ajoutés, le document est sauvegardé.

La fonction procède ensuite à extraire des notifications sur la césure de la deuxième page du document PDF généré en utilisant la méthode get_notifications().
 Ces notifications sont écrites dans un fichier texte spécifié précédemment.

Cet extrait de code illustre comment créer un document PDF contenant du texte sur plusieurs lignes, puis extraire des informations concernant le comportement de saut de ligne, fournissant des insights sur la disposition du texte dans le document.

```python

    import aspose.pdf as ap

    def track_line_breaking():
        """Suivre le découpage de ligne de TextFragment multi-ligne"""
        output_pdf = DIR_OUTPUT_TEXTS + "track_line_breaking.pdf"
        output_txt = DIR_OUTPUT_TEXTS + "track_line_breaking.txt"

        # Créer un nouvel objet document
        document = ap.Document()
        page = document.pages.add()

        for i in range(4):
            text = ap.text.TextFragment(
                "Lorem ipsum \r\ndolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
            )
            text.text_state.font_size = 20
            page.paragraphs.add(text)
        document.save(output_pdf)

        notifications = document.pages[1].get_notifications()
        with open(output_txt, "w") as f:
            f.write(notifications)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF pour la bibliothèque .NET",
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
    "applicationCategory": "Bibliothèque de manipulation PDF pour .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>