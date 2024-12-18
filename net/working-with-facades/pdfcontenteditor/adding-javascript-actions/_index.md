---
title: Adding Javascript actions PDF 
type: docs
weight: 10
url: /net/adding-javascript-actions/
description: Discover how to add JavaScript actions, such as button clicks or form submissions, to PDFs in .NET using Aspose.PDF.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding Javascript actions PDF",
    "alternativeHeadline": "Enhance PDF with Interactive JavaScript Actions",
    "abstract": "Enhance your PDF by integrating interactive Javascript actions with Aspose.PDF for .NET PdfContentEditor class. This feature allows users to create dynamic links and execute specific menu item actions, enriching the document experience with custom interactive elements. Streamline your workflow by adding event-based actions that respond to user interactions effortlessly",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "216",
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
    "url": "/net/adding-javascript-actions/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/adding-javascript-actions/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

The [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/PdfContentEditor) class present underAspose.Pdf.Facades package provides the flexibility to add Javascript actions to a PDF file. You can create a link with the serial actions corresponding to execute a menu item in the PDF viewer. This class also provides the feature to create additional actions for document events. 

First of all, an object is drawn in the [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document), in our example a [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle). And set the action [createJavaScriptLink](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createjavascriptlink) to the Rectangle. After you may save your document.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

public static void AddJavascriptAction()
{
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        editor.BindPdf(dataDir + "sample.pdf");

        // create Javascript link
        var rect = new System.Drawing.Rectangle(50, 750, 50, 50);

        var code = "app.alert('Welcome to Aspose!');";
        editor.CreateJavaScriptLink(code, rect, 1, System.Drawing.Color.Green);

        // save the output file
        editor.Save(dataDir + "JavaScriptAdded_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

public static void AddJavascriptAction()
{
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    using var editor = new Aspose.Pdf.Facades.PdfContentEditor();
    editor.BindPdf(dataDir + "sample.pdf");

    // create Javascript link
    var rect = new System.Drawing.Rectangle(50, 750, 50, 50);

    var code = "app.alert('Welcome to Aspose!');";
    editor.CreateJavaScriptLink(code, rect, 1, System.Drawing.Color.Green);

    // save the output file
    editor.Save(dataDir + "JavaScriptAdded_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}
