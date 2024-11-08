---
title: Déplacer des pages PDF par programmation via Python
linktitle: Déplacer des pages PDF
type: docs
weight: 100
url: /fr/python-net/move-pages/
description: Essayez de déplacer des pages à l'emplacement souhaité ou à la fin d'un fichier PDF à l'aide de Aspose.PDF pour Python via .NET.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Déplacer des pages PDF par programmation Python",
    "alternativeHeadline": "Comment déplacer des pages PDF avec Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents pdf",
    "keywords": "pdf, python, déplacer page pdf",
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
    "url": "/python-net/move-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/move-pages/"
    },
    "dateModified": "2023-04-04",
    "description": "Essayez de déplacer des pages à l'emplacement souhaité ou à la fin d'un fichier PDF à l'aide de Aspose.PDF pour Python via .NET."
}
</script>


## Déplacer une page d'un document PDF à un autre

Ce sujet explique comment déplacer une page d'un document PDF vers la fin d'un autre document en utilisant Python.
Pour déplacer une page, nous devons :

1. Créer un objet de classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) avec le fichier PDF source.
1. Créer un objet de classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) avec le fichier PDF de destination.
1. Obtenir la page de la collection de [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) page au document de destination.
1. Sauvegarder le PDF de sortie en utilisant la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).
1. [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) page dans le document source.

1. Enregistrez le PDF source en utilisant la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

Le code suivant vous montre comment déplacer une page.

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(src_file_name)
    dstDocument = ap.Document(dst_File_name)
    page = srcDocument.pages[2]
    dstDocument.pages.add(page)
    # Enregistrer le fichier de sortie
    dstDocument.save(dst_File_name_new)
    srcDocument.pages.delete(2)
    srcDocument.save(src_file_name_new)
```

## Déplacement d'un ensemble de pages d'un document PDF à un autre

1. Créez un objet de classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) avec le fichier PDF source.
1. Créez un objet de classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) avec le fichier PDF de destination.
1. Définissez un tableau avec les numéros de pages à déplacer.
1. Exécutez une boucle à travers le tableau :

1. Obtenez la page de la collection [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) page au document de destination.
1. Enregistrez le PDF de sortie en utilisant la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).
1. [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) page dans le document source en utilisant un tableau.
1. Enregistrez le PDF source en utilisant la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

L'extrait de code suivant vous montre comment insérer une page vide à la fin d'un fichier PDF.

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(input_pdf)
    dstDocument = ap.Document()
    pages = [1, 3]
    for page_index in pages:
        page = srcDocument.pages[page_index]
        dstDocument.pages.add(page)
    # Enregistrez les fichiers de sortie
    dstDocument.save(output_pdf_1)
    srcDocument.pages.delete(pages)
    srcDocument.save(output_pdf_2)
```


## Déplacer une Page à un nouvel emplacement dans le document PDF actuel

1. Créez un objet de classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) avec le fichier PDF source.
1. Obtenez la Page de la collection [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Ajoutez la page avec la méthode [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) au nouvel emplacement (par exemple à la fin).
1. Supprimez la page à l'emplacement précédent avec la méthode [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods).
1. Enregistrez le fichier PDF de sortie à l'aide de la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(input_pdf)

    page = srcDocument.pages[2]
    srcDocument.pages.add(page)
    srcDocument.pages.delete(2)

    # Enregistrer le fichier de sortie
    srcDocument.save(output_pdf)
```

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
    "applicationCategory": "PDF Manipulation Library for Python",
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