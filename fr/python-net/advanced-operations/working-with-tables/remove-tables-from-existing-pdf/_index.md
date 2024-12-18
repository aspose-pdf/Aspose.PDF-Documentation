---
title: Supprimer les tableaux d'un PDF existant
linktitle: Supprimer les tableaux
type: docs
weight: 50
url: /fr/python-net/remove-tables-from-existing-pdf/
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Supprimer les tableaux d'un PDF existant",
    "alternativeHeadline": "Comment supprimer les tableaux d'un PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents pdf",
    "keywords": "pdf, python, supprimer tableau, supprimer tableaux",
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
    "url": "/python-net/remove-tables-from-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/remove-tables-from-existing-pdf/"
    },
    "dateModified": "2023-02-04",
    "description": ""
}
</script>


{{% alert color="primary" %}}

Aspose.PDF pour Python via .NET offre les capacités d'insérer/créer une table à l'intérieur d'un document PDF pendant sa génération à partir de zéro, ou vous pouvez également ajouter l'objet table dans un document PDF existant. Cependant, vous pouvez avoir besoin de [Manipuler les tables dans un PDF existant](https://docs.aspose.com/pdf/python-net/manipulate-tables-in-existing-pdf/) où vous pouvez mettre à jour le contenu des cellules de table existantes. Cependant, vous pouvez rencontrer une exigence de suppression d'objets table d'un document PDF existant.

{{% /alert %}}

Pour supprimer les tables, nous devons utiliser la classe [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) pour obtenir les tables dans le PDF existant, puis appeler [remove()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods).

## Supprimer une table d'un document PDF

Nous avons ajouté une nouvelle fonction, c'est-à-dire.
 [remove()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods) à la classe existante [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) afin de supprimer une table d'un document PDF. Une fois que l'absorbeur trouve avec succès des tables sur la page, il devient capable de les supprimer. Veuillez vérifier l'extrait de code suivant montrant comment supprimer une table d'un document PDF :

```python

    import aspose.pdf as ap

    # Charger un document PDF existant
    pdf_document = ap.Document(input_file)
    # Créer un objet TableAbsorber pour trouver des tables
    absorber = ap.text.TableAbsorber()
    # Visiter la première page avec l'absorbeur
    absorber.visit(pdf_document.pages[1])
    # Obtenir la première table de la page
    table = absorber.table_list[0]
    # Supprimer la table
    absorber.remove(table)
    # Enregistrer le PDF
    pdf_document.save(output_file)
```

## Supprimer plusieurs tables d'un document PDF

Parfois, un document PDF peut contenir plus d'une table et vous pouvez avoir besoin de supprimer plusieurs tables de celui-ci. Afin de supprimer plusieurs tables d'un document PDF, veuillez utiliser l'extrait de code suivant :

```python

    import aspose.pdf as ap

    # Charger un document PDF existant
    pdf_document = ap.Document(input_file)
    # Créer un objet TableAbsorber pour trouver les tables
    absorber = ap.text.TableAbsorber()
    # Visiter la deuxième page avec l'absorbeur
    absorber.visit(pdf_document.pages[1])
    # Obtenir une copie de la collection de tables
    tables = absorber.table_list
    # Parcourir la copie de la collection et supprimer les tables
    for table in tables:
        absorber.remove(table)
    # Enregistrer le document
    pdf_document.save(output_file)
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
    "applicationCategory": "PDF Manipulation Library for Python via .NET",
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