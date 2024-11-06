---
title: Manipuler les tables dans un PDF existant
linktitle: Manipuler les tables
type: docs
weight: 40
url: fr/net/manipulate-tables-in-existing-pdf/
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipuler les tables dans un PDF existant",
    "alternativeHeadline": "Comment mettre à jour le contenu des tables dans un PDF existant",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de document PDF",
    "keywords": "pdf, c#, manipuler les tables",
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
    "url": "/net/manipulate-tables-in-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-tables-in-existing-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>
## Manipuler des tables dans des PDF existants

L'une des premières fonctionnalités prises en charge par Aspose.PDF pour .NET est ses capacités de travail avec les tables et il offre un excellent support pour l'ajout de tables dans des fichiers PDF générés à partir de zéro ou dans n'importe quel fichier PDF existant. Vous obtenez également la capacité d'intégrer une table avec une base de données (DOM) pour créer des tables dynamiques basées sur le contenu de la base de données. Dans cette nouvelle version, nous avons implémenté une nouvelle fonctionnalité de recherche et d'analyse de tables simples qui existent déjà sur la page du document PDF. Une nouvelle classe nommée **Aspose.PDF.Text.TableAbsorber** offre ces capacités. L'utilisation de TableAbsorber est très similaire à la classe TextFragmentAbsorber existante. Le code suivant montre les étapes pour mettre à jour le contenu dans une cellule de table particulière.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Charger un fichier PDF existant
Document pdfDocument = new Document(dataDir + "input.pdf");
// Créer un objet TableAbsorber pour trouver les tables
TableAbsorber absorber = new TableAbsorber();

// Visiter la première page avec l'absorbeur
absorber.Visit(pdfDocument.Pages[1]);

// Accéder à la première table de la page, leur première cellule et les fragments de texte à l'intérieur
TextFragment fragment = absorber.TableList[0].RowList[0].CellList[0].TextFragments[1];

// Changer le texte du premier fragment de texte dans la cellule
fragment.Text = "salut monde";
dataDir = dataDir + "ManipulateTable_out.pdf";
pdfDocument.Save(dataDir);
```
## Remplacer une ancienne table par une nouvelle dans un document PDF

Si vous avez besoin de trouver une table particulière et de la remplacer par celle souhaitée, vous pouvez utiliser la méthode Replace() de la classe [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) pour le faire. L'exemple suivant démontre la fonctionnalité pour remplacer la table à l'intérieur du document PDF :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Charger le document PDF existant
Document pdfDocument = new Document(dataDir + @"Table_input2.pdf");

// Créer un objet TableAbsorber pour trouver les tables
TableAbsorber absorber = new TableAbsorber();

// Visiter la première page avec l'absorbeur
absorber.Visit(pdfDocument.Pages[1]);

// Obtenir la première table de la page
AbsorbedTable table = absorber.TableList[0];

// Créer une nouvelle table
Table newTable = new Table();
newTable.ColumnWidths = "100 100 100";
newTable.DefaultCellBorder = new BorderInfo(BorderSide.All, 1F);

Row row = newTable.Rows.Add();
row.Cells.Add("Col 1");
row.Cells.Add("Col 2");
row.Cells.Add("Col 3");

// Remplacer la table par la nouvelle
absorber.Replace(pdfDocument.Pages[1], table, newTable);

// Enregistrer le document
pdfDocument.Save(dataDir + "TableReplaced_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF pour .NET Library",
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
```

