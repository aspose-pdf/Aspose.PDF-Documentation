---
title: Supprimer les tables d'un PDF existant
linktitle: Supprimer les tables
type: docs
weight: 50
url: fr/net/remove-tables-from-existing-pdf/
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Supprimer les tables d'un PDF existant",
    "alternativeHeadline": "Comment supprimer les tables d'un PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, supprimer table, supprimer tables",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Équipe de documentation Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "url": "/net/remove-tables-from-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/remove-tables-from-existing-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>
{{% alert color="primary" %}}

Aspose.PDF pour NET offre la capacité d'insérer/créer une table dans un document PDF lorsqu'il est généré à partir de zéro ou vous pouvez également ajouter l'objet table dans un document PDF existant. Cependant, vous pouvez avoir besoin de [Manipuler les tables dans un PDF existant](https://docs.aspose.com/pdf/net/manipulate-tables-in-existing-pdf/) où vous pouvez mettre à jour le contenu dans les cellules de table existantes. Vous pourriez également rencontrer le besoin de supprimer des objets table d'un document PDF existant.

{{% /alert %}}

Pour supprimer les tables, nous devons utiliser la classe [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) pour saisir les tables dans un PDF existant, puis appeler [Remove](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber/methods/remove).

Le fragment de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Supprimer une table d'un document PDF

Nous avons ajouté une nouvelle fonction, c'est-à-dire
Nous avons ajouté une nouvelle fonction, c'est-à-dire

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Charger un document PDF existant
Document pdfDocument = new Document(dataDir + "Table_input.pdf");

// Créer un objet TableAbsorber pour trouver les tables
TableAbsorber absorber = new TableAbsorber();

// Visiter la première page avec l'absorbeur
absorber.Visit(pdfDocument.Pages[1]);

// Obtenir la première table de la page
AbsorbedTable table = absorber.TableList[0];

// Supprimer la table
absorber.Remove(table);

// Sauvegarder le PDF
pdfDocument.Save(dataDir + "Table_out.pdf");
```

## Supprimer plusieurs tables d'un document PDF

Parfois, un document PDF peut contenir plus d'une table et vous pourriez avoir besoin de supprimer plusieurs tables de celui-ci. Pour supprimer plusieurs tables d'un document PDF, veuillez utiliser le fragment de code suivant :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Charger un document PDF existant
Document pdfDocument = new Document(dataDir + "Table_input2.pdf");

// Créer un objet TableAbsorber pour trouver les tables
TableAbsorber absorber = new TableAbsorber();

// Visiter la deuxième page avec l'absorbeur
absorber.Visit(pdfDocument.Pages[1]);

// Obtenir une copie de la collection de tables
AbsorbedTable[] tables = new AbsorbedTable[absorber.TableList.Count];
absorber.TableList.CopyTo(tables, 0);

// Parcourir la copie de la collection et supprimer les tables
foreach (AbsorbedTable table in tables)
    absorber.Remove(table);

// Sauvegarder le document
pdfDocument.Save(dataDir + "Table2_out.pdf");
```
{{% alert color="primary" %}}

Veuillez prendre en compte que la suppression ou le remplacement d'une table modifie la collection TableList. Par conséquent, dans le cas de la suppression ou du remplacement des tables dans une boucle, la copie de la collection TableList est essentielle.

{{% /alert %}}

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "applicationCategory": "Bibliothèque de manipulation de PDF pour .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>


