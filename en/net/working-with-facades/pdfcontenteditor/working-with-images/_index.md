---
title: Work with Images using PdfContentEditor
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /net/working-with-images-in-pdf
description: This section explains how to add and delete Images with Aspose.PDF Facades using PdfContentEditor Class.
lastmod: "2021-06-24"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Work with Images using PdfContentEditor",
    "alternativeHeadline": "Enhance PDF Images with PdfContentEditor Features",
    "abstract": "Aspose.PDF for .NET now offers enhanced image management capabilities through the PdfContentEditor class, enabling users to easily delete specific images from designated pages or entirely remove all images from PDF files. Additionally, the feature allows for seamless image replacement, streamlining the editing process and improving document customization",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "415",
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
    "url": "/net/working-with-images-in-pdf",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-images-in-pdf"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Delete Images from a Particular Page of PDF (Facades)

In order to delete the images from a particular page, you need to call [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) method with pageNumber and index parameter. The index parameter represents an array of integers – the indexes of the images to be deleted. First of all, you need to create an object of [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class and then call the [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) method. After that, you can save the updated PDF file using [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) method.

The following code snippet shows you how to delete images from a particular page of PDF.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample.pdf")))
    {
        editor.DeleteImage(2, new[] { 2 });

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo10.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor Object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample.pdf"));

    editor.DeleteImage(2, new[] { 2 });

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo10.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Delete All the Images from a PDF File (Facades)

All the images can be deleted from a PDF file using [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) method of the [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). Call the [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) method – the overload without any parametes – to delete all the images, and then save the updated PDF file using [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) method.

The following code snippet shows you how to delete all the images from a PDF file.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample.pdf")))
    {
        editor.DeleteImage();

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo11.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample.pdf"));

    editor.DeleteImage();

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo11.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Replace Image in a PDF File (Facades)

the [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) allows you replace your image in a PDF file, call for this the [ReplaceImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replaceimage) method, and Save the result.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample_cats_dogs.pdf")))
    {
        editor.ReplaceImage(2, 4, dataDir + "Image.jpg");

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo12.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample_cats_dogs.pdf"));
    editor.ReplaceImage(2, 4, dataDir + "Image.jpg");

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo12.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}
