---
title: Manipuler des tableaux dans un PDF existant
linktitle: Manipuler des tableaux
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /fr/net/manipulate-tables-in-existing-pdf/
description: Apprenez à travailler avec des tableaux dans des PDF existants en utilisant Aspose.PDF for .NET, offrant une flexibilité dans la modification des documents.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipulate Tables in existing PDF",
    "alternativeHeadline": "Enhance Table Editing in Existing PDF Documents",
    "abstract": "Aspose.PDF for .NET introduit une fonctionnalité puissante pour manipuler des tableaux PDF existants, permettant aux utilisateurs de rechercher, analyser et modifier le contenu des tableaux avec facilité. La nouvelle classe TableAbsorber permet des mises à jour et des remplacements dynamiques de tableaux directement dans les documents PDF, rationalisant le processus de gestion des données tabulaires dans les PDF pour une fonctionnalité améliorée. Explorez cette capacité innovante pour optimiser vos tâches d'édition PDF et d'intégration de données.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "url": "/net/manipulate-tables-in-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-tables-in-existing-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Manipuler des tableaux dans un PDF existant

L'une des premières fonctionnalités prises en charge par Aspose.PDF for .NET est ses capacités de travail avec des tableaux et elle offre un excellent support pour ajouter des tableaux dans des fichiers PDF générés à partir de zéro ou de tout fichier PDF existant. Vous obtenez également la capacité d'intégrer un tableau avec une base de données (DOM) pour créer des tableaux dynamiques basés sur le contenu de la base de données. Dans cette nouvelle version, nous avons mis en œuvre une nouvelle fonctionnalité de recherche et d'analyse de tableaux simples qui existent déjà sur la page du document PDF. Une nouvelle classe nommée **Aspose.PDF.Text.TableAbsorber** fournit ces capacités. L'utilisation de TableAbsorber est très similaire à celle de la classe TextFragmentAbsorber existante. L'extrait de code suivant montre les étapes pour mettre à jour le contenu d'une cellule de tableau particulière.

L'extrait de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ManipulateTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create TableAbsorber object to find tables
        var absorber = new Aspose.Pdf.Text.TableAbsorber();

        // Visit first page with absorber
        absorber.Visit(document.Pages[1]);

        // Get access to first table on page, their first cell and text fragments in it
        Aspose.Pdf.Text.TextFragment fragment = absorber.TableList[0].RowList[0].CellList[0].TextFragments[1];

        // Change text of the first text fragment in the cell
        fragment.Text = "hi world";

        // Save PDF document
        document.Save(dataDir + "ManipulateTable_out.pdf");
    }
}
```

## Remplacer un ancien tableau par un nouveau dans un document PDF

Dans le cas où vous devez trouver un tableau particulier et le remplacer par celui souhaité, vous pouvez utiliser la méthode Replace() de la classe [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) pour ce faire. L'exemple suivant démontre la fonctionnalité de remplacement du tableau à l'intérieur du document PDF :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Table_input2.pdf"))
    {
        // Create TableAbsorber object to find tables
        var absorber = new Aspose.Pdf.Text.TableAbsorber();

        // Visit first page with absorber
        absorber.Visit(document.Pages[1]);

        // Get first table on the page
        Aspose.Pdf.Text.AbsorbedTable table = absorber.TableList[0];

        // Create new table
        var newTable = new Aspose.Pdf.Table();
        newTable.ColumnWidths = "100 100 100";
        newTable.DefaultCellBorder = new Aspose.Pdf.BorderInfo(BorderSide.All, 1F);

        Row row = newTable.Rows.Add();
        row.Cells.Add("Col 1");
        row.Cells.Add("Col 2");
        row.Cells.Add("Col 3");

        // Replace the table with new one
        absorber.Replace(document.Pages[1], table, newTable);

        // Save PDF document
        document.Save(dataDir + "ReplaceTable_out.pdf");
    }
}
```

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
    "applicationCategory": "PDF Manipulation Library for .NET",
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