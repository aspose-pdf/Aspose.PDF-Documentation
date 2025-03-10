---
title: Remplacer du texte - Façades
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /fr/net/replace-text-facades/
description: Cette section explique comment travailler avec Text - Façades en utilisant la classe PdfContentEditor.
lastmod: "2021-06-24"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Replace Text - Facades",
    "alternativeHeadline": "Effortless Text Replacement in PDF Files",
    "abstract": "La fonctionnalité Remplacer du texte dans la classe PdfContentEditor permet aux utilisateurs de modifier efficacement le contenu textuel au sein de documents PDF existants. En utilisant des méthodes simples comme BindPdf et ReplaceText, les utilisateurs peuvent mettre à jour le texte, ajuster les tailles de police et personnaliser le formatage du texte, y compris le gras et la couleur, tout en maintenant l'intégrité du document original. Cette fonctionnalité améliore les capacités d'édition PDF, facilitant la gestion dynamique du contenu.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "550",
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
    "url": "/net/replace-text-facades/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/replace-text-facades/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Remplacer du texte dans un fichier PDF existant

Pour remplacer du texte dans un fichier PDF existant, vous devez créer un objet de la classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) et lier un fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Après cela, vous devez appeler la méthode [ReplaceText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replacetext/index). Vous devez enregistrer le fichier PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) de la classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). Le code suivant vous montre comment remplacer du texte dans un fichier PDF existant.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "sample.pdf");
        editor.ReplaceText("Value", "Label");

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo01_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor Object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    editor.BindPdf(dataDir + "sample.pdf");
    editor.ReplaceText("Value", "Label");

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo01_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

Vérifiez à quoi cela ressemble dans le document original :

![Remplacer du texte](replace_text1.png)

Et vérifiez le résultat après avoir remplacé le texte :

![Résultat du remplacement de texte](replace_text2.png)

Dans le deuxième exemple, vous verrez comment, en plus de remplacer le texte, vous pouvez également augmenter ou diminuer la taille de la police :

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "sample.pdf");
        editor.ReplaceText("Value", "Label", 12);

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo02_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    editor.BindPdf(dataDir + "sample.pdf");
    editor.ReplaceText("Value", "Label", 12);

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo02_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

Pour des possibilités plus avancées de travail avec notre texte, nous utiliserons la méthode [TextState](https://reference.aspose.com/pdf/net/aspose.pdf.text/textstate). Avec cette méthode, nous pouvons rendre le texte gras, italique, coloré, etc.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText03()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "sample.pdf");

        var textState = new Aspose.Pdf.Text.TextState
        {
            ForegroundColor = Aspose.Pdf.Color.Red,
            FontSize = 12,
        };

        editor.ReplaceText("Value", "Label", textState);

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo03_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText03()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    editor.BindPdf(dataDir + "sample.pdf");

    var textState = new Aspose.Pdf.Text.TextState
    {
        ForegroundColor = Aspose.Pdf.Color.Red,
        FontSize = 12,
    };

    editor.ReplaceText("Value", "Label", textState);

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo03_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

Dans le cas où vous devez remplacer tout le texte spécifié dans le document, utilisez le code suivant. C'est-à-dire que le remplacement du texte aura lieu partout où le texte spécifié pour le remplacement sera rencontré, et il comptera également le nombre de tels remplacements.

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText04()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "sample.pdf");
        int count = 0;

        while (editor.ReplaceText("Value", "Label"))
        {
            count++;
        }

        Console.WriteLine($"{count} occurrences have been replaced.");

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo04_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText04()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    editor.BindPdf(dataDir + "sample.pdf");
    int count = 0;

    while (editor.ReplaceText("Value", "Label"))
    {
        count++;
    }

    Console.WriteLine($"{count} occurrences have been replaced.");

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo04_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

![Remplacer tout le texte](replace_text3.png)

Le code suivant montre comment effectuer tous les remplacements de texte mais sur une page spécifique de votre document.

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText05()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "sample.pdf");
        int count = 0;

        while (editor.ReplaceText("9999", 2, "ABCDE"))
        {
            count++;
        }

        Console.WriteLine($"{count} occurrences have been replaced.");

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo05_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText05()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    editor.BindPdf(dataDir + "sample.pdf");
    int count = 0;

    while (editor.ReplaceText("9999", 2, "ABCDE"))
    {
        count++;
    }

    Console.WriteLine($"{count} occurrences have been replaced.");

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo05_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

Dans le prochain extrait de code, nous montrerons comment remplacer, par exemple, un nombre donné par les lettres dont nous avons besoin.

{{< tabs tabID="6" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText06()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor
           {
               ReplaceTextStrategy = new Aspose.Pdf.Facades.ReplaceTextStrategy
               {
                   IsRegularExpressionUsed = true,
                   ReplaceScope = Aspose.Pdf.Facades.ReplaceTextStrategy.Scope.ReplaceAll
               }
           })
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "sample.pdf");
        editor.ReplaceText("\\d{4}", "ABCDE");

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo06_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText06()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor
    {
        ReplaceTextStrategy = new Aspose.Pdf.Facades.ReplaceTextStrategy
        {
            IsRegularExpressionUsed = true,
            ReplaceScope = Aspose.Pdf.Facades.ReplaceTextStrategy.Scope.ReplaceAll
        }
    };

    // Bind PDF document
    editor.BindPdf(dataDir + "sample.pdf");
    editor.ReplaceText("\\d{4}", "ABCDE");

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo06_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}