---
title: Adding Annotations to existing PDF file
type: docs
weight: 80
url: /net/adding-annotations-to-existing-pdf-file/
description: Explore how to add annotations like comments or highlights to existing PDF documents in .NET using Aspose.PDF.
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
    "abstract": "Enhance your PDF documents with our new annotation feature, allowing users to add various types of annotations including free text, text, and line annotations seamlessly. By utilizing the PdfContentEditor, you can easily bind existing PDF files and specify annotation areas, improving document interactivity and clarity with just a few lines of code. Optimize your workflow by integrating rich annotations directly into your PDFs, elevating user engagement and comprehension",
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
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Add Free Text Annotation in an Existing PDF File (facades)

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) allows you to add annotations of different types in an existing PDF file. You can use the respective method to add a particular annotation. For example, in the following code snippet, we have used [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) method add [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) type annotation. 

Any type of annotations can be added to the PDF file in the same way. First of all, you need to create an object of type [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor)  and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. Secondly, you have to create a Rectangle object to specify the area of the annotatation. 

After that, you can call [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) method to add [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) annotation, and then use [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method to save the updated PDF file.


The following code snippet shows you how to add free text annotation in a PDF file.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFreeTextAnnotation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

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
    string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

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

## Add Text Annotation in an Existing PDF File (facades)

In this example also, you need to create an object of type [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. Secondly, you have to create a Rectangle object to specify the area of the annotation. After that, you can call [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) method to add FreeText annotation, create title of your annotations, and the page number on which the annotation is located.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextAnnotation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

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
    string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

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

## Add Line Annotation in an Existing PDF File (facades)

We also specify the Rectangle, coordinates of the beginning and end of the line, page number, thickness, style and color of the annotation frame, type of line dash, type of start and end of the line.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLineAnnotation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

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
    string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

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
