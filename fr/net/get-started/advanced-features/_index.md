---
title: Fonctionnalités Avancées
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 140
url: /fr/net/advanced-features/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Advanced Features",
    "alternativeHeadline": "Streamlined PDF Handling and Mathematical Expression Support in C#",
    "abstract": "Découvrez la dernière amélioration dans Aspose.PDF for .NET qui permet l'envoi sans faille de documents PDF vers des navigateurs web pour un téléchargement direct sans besoin de stockage physique. Cette fonctionnalité simplifie non seulement la livraison de fichiers, mais inclut également des capacités avancées pour extraire des fichiers intégrés et incorporer des expressions mathématiques complexes en utilisant LaTeX, en faisant un outil essentiel pour les développeurs travaillant avec des formats PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "386",
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
    "url": "/net/advanced-features/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/advanced-features/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés."
}
</script>

## Envoi de PDF au navigateur pour téléchargement

Parfois, lorsque vous développez une application ASP.NET, vous devez envoyer des fichiers PDF vers des navigateurs web pour téléchargement sans les enregistrer physiquement. Pour y parvenir, vous pouvez enregistrer le document PDF dans un objet MemoryStream après l'avoir généré et passer les octets de ce MemoryStream à l'objet Response. Cela fera en sorte que le navigateur télécharge le document PDF généré.

Le code suivant illustre cette fonctionnalité :
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private void Page_Load(object sender, EventArgs e)
{
    // Clear the response before writing to it
    Response.Clear();
    // Set content type for PDF
    Response.ContentType = "application/pdf";
    // Set the response header for file download
    Response.AddHeader("content-disposition", "attachment; filename=TestDocument.pdf");

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add Page in Pages Collection
        var page = document.Pages.Add();
        var textFragment = new Aspose.Pdf.Text.TextFragment("Hello World");
        page.Paragraphs.Add(textFragment);
        
        // Save PDF document to a MemoryStream
        using (var ms = new MemoryStream())
        {
            document.Save(ms);
             // Reset the stream position to the beginning
            ms.Position = 0;

            // Write the MemoryStream to the response
            ms.CopyTo(Response.OutputStream);
            Response.AddHeader("content-length", ms.Length.ToString());
            Response.Flush();
            // Suppress the remaining content
            Response.SuppressContent = true; 
        }
    }
    // End the response to prevent further processing
    Response.End(); 
}
```

## Utilisation de script LaTeX pour ajouter des expressions mathématiques

Avec Aspose.PDF, vous pouvez ajouter des expressions/formules mathématiques à l'intérieur d'un document PDF en utilisant un script LaTeX. Les exemples suivants montrent comment cette fonctionnalité peut être utilisée de deux manières différentes, afin d'ajouter une formule mathématique à l'intérieur d'une cellule de tableau :

### Sans préambule et environnement de document

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET      
private static void LatexWithoutPreambleAndDocEnvironment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = doc.Pages.Add();
        // Create a Table
        var table = new Aspose.Pdf.Table();
        // Add a row into Table
        var row = table.Rows.Add();
        // Add Cell with Latex Script to add methematical expressions/formulae
        var latexText1 = "$123456789+\\sqrt{1}+\\int_a^b f(x)dx$";
        var cell = row.Cells.Add();
        cell.Margin = new MarginInfo { Left = 20, Right = 20, Top = 20, Bottom = 20 };
        // Second TeXFragment constructor bool parameter provides LaTeX paragraph indents elimination
        var ltext1 = new Aspose.Pdf.TeXFragment(latexText1, true);
        cell.Paragraphs.Add(ltext1);
        // Add table inside page
        page.Paragraphs.Add(table);
        // Save PDF document
        document.Save(dataDir + "LatextScriptInPdf_out.pdf");
    }
}
```

### Avec préambule et environnement de document

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void LatexWithPreambleAndDocEnvironment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = doc.Pages.Add();
        // Create a Table
        var table = new Aspose.Pdf.Table();
        // Add a row into Table
        var row = table.Rows.Add();
       // Add Cell with Latex Script to add methematical expressions/formulae
        var latexText2 = @"\documentclass{article}
                            \begin{document}
                            Latex and the document class will normally take care of page layout issues for you. For submission to an academic publication, this entire topic will be out
                            \end{document}";
        var cell = row.Cells.Add();
        cell.Margin = new Aspose.Pdf.MarginInfo { Left = 20, Right = 20, Top = 20, Bottom = 20 };
        var text2 = new Aspose.Pdf.HtmlFragment(latexText2);
        cell.Paragraphs.Add(text2);
        // Add table inside page
        page.Paragraphs.Add(table);
        // Save PDF document
        document.Save(dataDir + "LatextScriptInPdf2_out.pdf");
    }
}
```

### Support pour les balises LaTeX

L'environnement align est défini dans le package amsmath, et l'environnement proof est défini dans le package amsthm. Ainsi, vous devez spécifier ces packages en utilisant la commande \usepackage dans le préambule du document. Cela signifie que vous devez enfermer le texte LaTeX dans un environnement de document comme montré dans l'exemple de code suivant.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void LatexTagsSupport()
{
    var s = @"
    \usepackage{amsmath,amsthm}
    \begin{document}
    \begin{proof} The proof is a follows: 
    \begin{align}
    (x+y)^3&=(x+y)(x+y)^2
    (x+y)(x^2+2xy+y^2)\\
    &=x^3+3x^2y+3xy^3+x^3.\qedhere
    \end{align}
    \end{proof}
    \end{document}";

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var latex = new Aspose.Pdf.TeXFragment(s);
        page.Paragraphs.Add(latex);
        // Save PDF document
        document.Save(dataDir + "Script_out.pdf");
    }
}
```