---
title: Ajouter des annotations à un fichier PDF existant
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /fr/net/adding-annotations-to-existing-pdf-file/
description: Découvrez comment ajouter des annotations telles que des commentaires ou des surlignages à des documents PDF existants en .NET en utilisant Aspose.PDF.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding Annotations to existing PDF file",
    "alternativeHeadline": "Enhance PDF with Dynamic Annotation Capabilities",
    "abstract": "Améliorez vos documents PDF avec notre nouvelle fonctionnalité d'annotation, permettant aux utilisateurs d'ajouter divers types d'annotations, y compris du texte libre, du texte et des annotations de ligne de manière transparente. En utilisant le PdfContentEditor, vous pouvez facilement lier des fichiers PDF existants et spécifier des zones d'annotation, améliorant ainsi l'interactivité et la clarté du document avec seulement quelques lignes de code. Optimisez votre flux de travail en intégrant des annotations riches directement dans vos PDF, élevant l'engagement et la compréhension des utilisateurs.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "621",
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
    "url": "/net/adding-annotations-to-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/adding-annotations-to-existing-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés."
}
</script>

## Ajouter une annotation de texte libre dans un fichier PDF existant (facades)

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) vous permet d'ajouter des annotations de différents types dans un fichier PDF existant. Vous pouvez utiliser la méthode respective pour ajouter une annotation particulière. Par exemple, dans l'extrait de code suivant, nous avons utilisé la méthode [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) pour ajouter une annotation de type [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation).

Tout type d'annotations peut être ajouté au fichier PDF de la même manière. Tout d'abord, vous devez créer un objet de type [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) et lier le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Deuxièmement, vous devez créer un objet Rectangle pour spécifier la zone de l'annotation.

Après cela, vous pouvez appeler la méthode [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) pour ajouter l'annotation [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation), puis utiliser la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) pour enregistrer le fichier PDF mis à jour.

L'extrait de code suivant vous montre comment ajouter une annotation de texte libre dans un fichier PDF.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFreeTextAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate PdfContentEditor object
        var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

        var tfa = new Aspose.Pdf.Text.TextFragmentAbsorber("PDF");
        tfa.Visit(document.Pages[1]);

        var rect = new System.Drawing.Rectangle
        {
            X = (int)tfa.TextFragments[1].Rectangle.LLX,
            Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
            Height = 18,
            Width = 100
        };

        // Add annotation
        editor.CreateFreeText(rect, "Free Text Demo", 1); // last param is a page number

        // Save PDF document
        editor.Save(dataDir + "AddFreeTextAnnotation_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFreeTextAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Instantiate PdfContentEditor object
    var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

    var tfa = new Aspose.Pdf.Text.TextFragmentAbsorber("PDF");
    tfa.Visit(document.Pages[1]);

    var rect = new System.Drawing.Rectangle
    {
        X = (int)tfa.TextFragments[1].Rectangle.LLX,
        Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
        Height = 18,
        Width = 100
    };

    // Add annotation
    editor.CreateFreeText(rect, "Free Text Demo", 1); // last param is a page number

    // Save PDF document
    editor.Save(dataDir + "AddFreeTextAnnotation_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Ajouter une annotation de texte dans un fichier PDF existant (facades)

Dans cet exemple également, vous devez créer un objet de type [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) et lier le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Deuxièmement, vous devez créer un objet Rectangle pour spécifier la zone de l'annotation. Après cela, vous pouvez appeler la méthode [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) pour ajouter l'annotation FreeText, créer le titre de vos annotations et le numéro de page sur lequel l'annotation est située.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate PdfContentEditor object
        var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

        var tfa = new Aspose.Pdf.Text.TextFragmentAbsorber("PDF");
        tfa.Visit(document.Pages[1]);

        var rect = new System.Drawing.Rectangle
        {
            X = (int)tfa.TextFragments[1].Rectangle.LLX,
            Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
            Height = 18,
            Width = 100
        };

        // Add annotation
        editor.CreateText(rect, "Aspose User", "PDF is a better format for modern documents", false, "Key", 1);

        // Save PDF document
        editor.Save(dataDir + "AddTextAnnotation_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Instantiate PdfContentEditor object
    var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

    var tfa = new Aspose.Pdf.Text.TextFragmentAbsorber("PDF");
    tfa.Visit(document.Pages[1]);

    var rect = new System.Drawing.Rectangle
    {
        X = (int)tfa.TextFragments[1].Rectangle.LLX,
        Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
        Height = 18,
        Width = 100
    };

    // Add annotation
    editor.CreateText(rect, "Aspose User", "PDF is a better format for modern documents", false, "Key", 1);

    // Save PDF document
    editor.Save(dataDir + "AddTextAnnotation_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Ajouter une annotation de ligne dans un fichier PDF existant (facades)

Nous spécifions également le Rectangle, les coordonnées du début et de la fin de la ligne, le numéro de page, l'épaisseur, le style et la couleur du cadre de l'annotation, le type de tiret de ligne, le type de début et de fin de la ligne.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLineAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate PdfContentEditor object
        var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

        // Create Line Annotation
        editor.CreateLine(
            new System.Drawing.Rectangle(550, 93, 562, 439),
            "Test",
            556, 99, 556, 443, 1, 2,
            System.Drawing.Color.Red,
            "dash",
            new int[] { 1, 0, 3 },
            new[] { "Open", "Open" });

        // Save PDF document
        editor.Save(dataDir + "AddLineAnnotation_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLineAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Instantiate PdfContentEditor object
    var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

    // Create Line Annotation
    editor.CreateLine(
        new System.Drawing.Rectangle(550, 93, 562, 439),
        "Test",
        556, 99, 556, 443, 1, 2,
        System.Drawing.Color.Red,
        "dash",
        new int[] { 1, 0, 3 },
        new[] { "Open", "Open" });

    // Save PDF document
    editor.Save(dataDir + "AddLineAnnotation_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}