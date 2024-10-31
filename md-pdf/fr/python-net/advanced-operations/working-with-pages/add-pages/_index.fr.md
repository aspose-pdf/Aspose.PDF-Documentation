---
title: Ajouter des Pages dans un PDF avec Python
linktitle: Ajouter des Pages
type: docs
weight: 10
url: /python-net/add-pages/
description: Cet article explique comment insérer (ajouter) une page à l'emplacement souhaité dans un fichier PDF. Apprenez à déplacer, supprimer (effacer) des pages d'un fichier PDF en utilisant C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ajouter des Pages dans un PDF avec Python",
    "alternativeHeadline": "Comment ajouter des Pages dans un document PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de document pdf",
    "keywords": "pdf, python, ajouter page pdf, insérer page pdf",
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
    "url": "/python-net/add-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Cet article explique comment insérer (ajouter) une page à l'emplacement souhaité dans un fichier PDF. Apprenez à déplacer, supprimer (effacer) des pages d'un fichier PDF en utilisant Python."
}
</script>


Aspose.PDF pour Python via .NET API offre une flexibilité totale pour travailler avec les pages d'un document PDF en utilisant Python. Il maintient toutes les pages d'un document PDF dans [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) qui peut être utilisée pour travailler avec les pages PDF. Aspose.PDF pour Python via .NET vous permet d'insérer une page dans un document PDF à n'importe quel emplacement dans le fichier ainsi que d'ajouter des pages à la fin d'un fichier PDF. Cette section montre comment ajouter des pages à un PDF en utilisant Python.

## Ajouter ou Insérer une Page dans un Fichier PDF

Aspose.PDF pour Python via .NET vous permet d'insérer une page dans un document PDF à n'importe quel emplacement dans le fichier ainsi que d'ajouter des pages à la fin d'un fichier PDF.

### Insérer une Page Vide dans un Fichier PDF à l'Emplacement Désiré

Pour insérer une page vide dans un fichier PDF :

1. Créez un objet de classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) avec le fichier PDF d'entrée.

1. Appelez la méthode [insert](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection/methods/insert) de la collection [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) avec l'index spécifié.
1. Enregistrez le PDF de sortie en utilisant la méthode [save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Le snippet de code suivant vous montre comment insérer une page dans un fichier PDF.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)
    # Insérer une page vide dans un PDF
    document.pages.insert(2)
    # Enregistrer le fichier de sortie
    document.save(output_pdf)
```

### Ajouter une Page Vide à la Fin d'un Fichier PDF

Parfois, vous souhaitez vous assurer qu'un document se termine par une page vide. Ce sujet explique comment insérer une page vide à la fin du document PDF.

Pour insérer une page vide à la fin d'un fichier PDF :

1. Créez un objet de la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) avec le fichier PDF d'entrée.

1. Appelez la méthode [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) de la collection [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/), sans aucun paramètre.
1. Enregistrez le PDF de sortie en utilisant la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

L'extrait de code suivant vous montre comment insérer une page vide à la fin d'un fichier PDF.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)

    # Insérer une page vide à la fin d'un fichier PDF
    document.pages.add()

    # Enregistrer le fichier de sortie
    document.save(output_pdf)