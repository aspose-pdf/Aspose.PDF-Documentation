---
title: Création d'un PDF complexe
linktitle: Création d'un PDF complexe
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /fr/net/complex-pdf-example/
description: Aspose.PDF pour NET vous permet de créer des documents plus complexes contenant des images, des fragments de texte et des tableaux dans un seul document.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Creating a complex PDF",
    "alternativeHeadline": "Create Complex PDFs with Images, Text, and Tables in C#",
    "abstract": "Aspose.PDF for .NET introduit une fonctionnalité puissante pour créer des PDFs complexes, permettant aux développeurs d'intégrer facilement des images, des fragments de texte et des tableaux dans un seul document. Cette fonctionnalité utilise une approche basée sur le DOM, permettant une personnalisation détaillée et un contrôle de mise en page dans la génération de PDF, ce qui la rend idéale pour créer des documents de qualité professionnelle de manière efficace.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "632",
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
    "url": "/net/complex-pdf-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/complex-pdf-example/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés."
}
</script>

L'exemple [Hello, World](/pdf/fr/net/hello-world-example/) a montré des étapes simples pour créer un document PDF en utilisant C# et Aspose.PDF. Dans cet article, nous allons examiner la création d'un document plus complexe avec C# et Aspose.PDF for .NET. Comme exemple, nous prendrons un document d'une entreprise fictive qui opère des services de ferry pour passagers. Notre document contiendra une image, deux fragments de texte (en-tête et paragraphe), et un tableau. Pour construire un tel document, nous utiliserons une approche basée sur le DOM. Vous pouvez en lire plus dans la section [Bases de l'API DOM](/pdf/fr/net/basics-of-dom-api/).

Si nous créons un document à partir de zéro, nous devons suivre certaines étapes :

1. Instancier un objet [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document). À cette étape, nous créerons un document PDF vide avec quelques métadonnées mais sans pages.
1. Ajouter une [Page](https://reference.aspose.com/pdf/fr/net/aspose.pdf/page) à l'objet document. Ainsi, notre document aura maintenant une page.
1. Ajouter une [Image](https://reference.aspose.com/pdf/fr/net/aspose.pdf/image/methods/index) à la Page.
1. Créer un [TextFragment](https://reference.aspose.com/pdf/fr/net/aspose.pdf.text/textfragment) pour l'en-tête. Pour l'en-tête, nous utiliserons la police Arial avec une taille de police de 24pt et un alignement centré.
1. Ajouter l'en-tête aux [Paragraphes](https://reference.aspose.com/pdf/fr/net/aspose.pdf/page/properties/paragraphs) de la page.
1. Créer un [TextFragment](https://reference.aspose.com/pdf/fr/net/aspose.pdf.text/textfragment) pour la description. Pour la description, nous utiliserons la police Arial avec une taille de police de 24pt et un alignement centré.
1. Ajouter (description) aux Paragraphes de la page.
1. Créer un tableau, ajouter des propriétés au tableau.
1. Ajouter (tableau) aux [Paragraphes](https://reference.aspose.com/pdf/fr/net/aspose.pdf/page/properties/paragraphs) de la page.
1. Enregistrer un document "Complex.pdf".

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreatingComplexPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Add image
        page.AddImage(dataDir + "logo.png", new Aspose.Pdf.Rectangle(20, 730, 120, 830));

        // Add Header
        var header = new Aspose.Pdf.Text.TextFragment("New ferry routes in Fall 2020");
        header.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        header.TextState.FontSize = 24;
        header.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        header.Position = new Aspose.Pdf.Text.Position(130, 720);
        page.Paragraphs.Add(header);

        // Add description
        var descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. Ferry service is operating at half capacity and on a reduced schedule. Expect lineups.";
        var description = new Aspose.Pdf.Text.TextFragment(descriptionText);
        description.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Times New Roman");
        description.TextState.FontSize = 14;
        description.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Left;
        page.Paragraphs.Add(description);

        // Add table
        var table = new Aspose.Pdf.Table
        {
            ColumnWidths = "200",
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1f, Aspose.Pdf.Color.DarkSlateGray),
            DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 0.5f, Aspose.Pdf.Color.Black),
            DefaultCellPadding = new Aspose.Pdf.MarginInfo(4.5, 4.5, 4.5, 4.5),
            Margin =
            {
                Bottom = 10
            },
            DefaultCellTextState =
            {
                Font =  Aspose.Pdf.Text.FontRepository.FindFont("Helvetica")
            }
        };

        var headerRow = table.Rows.Add();
        headerRow.Cells.Add("Departs City");
        headerRow.Cells.Add("Departs Island");
        foreach (Aspose.Pdf.Cell headerRowCell in headerRow.Cells)
        {
            headerRowCell.BackgroundColor = Aspose.Pdf.Color.Gray;
            headerRowCell.DefaultCellTextState.ForegroundColor = Aspose.Pdf.Color.WhiteSmoke;
        }

        var time = new TimeSpan(6, 0, 0);
        var incTime = new TimeSpan(0, 30, 0);
        for (int i = 0; i < 10; i++)
        {
            var dataRow = table.Rows.Add();
            dataRow.Cells.Add(time.ToString(@"hh\:mm"));
            time = time.Add(incTime);
            dataRow.Cells.Add(time.ToString(@"hh\:mm"));
        }

        page.Paragraphs.Add(table);
        // Save PDF document
        document.Save(dataDir + "Complex_out.pdf");
    }
}
```