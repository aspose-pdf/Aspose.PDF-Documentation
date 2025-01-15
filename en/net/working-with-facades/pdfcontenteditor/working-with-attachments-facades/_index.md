---
title: Working with Attachments - Facades
type: docs
weight: 50
url: /net/working-with-attachments-facades/
description: This section explains how to working with Attachments - Facades using PdfContentEditor Class.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Attachments - Facades",
    "alternativeHeadline": "Enhanced PDF Attachment Management",
    "abstract": "The Working with Attachments - Facades feature in Aspose.PDF for .NET enables users to easily manage file attachments within PDF documents. With functionalities for adding, retrieving, and removing various file types programmatically using the PdfContentEditor class, this feature streamlines the process of enhancing PDF interactivity by allowing attachments to be integrated seamlessly",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "589",
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
    "url": "/net/working-with-attachments-facades/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-attachments-facades/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

In this section, we will explain how to work with attachments in PDF using Aspose.PDF for .NET Facades. An attachment is an additional file that is attached to a parent document, it can be a variety of file types, such as pdf, word, image, or other files. You will learn how to add attachments to pdf, get the information of an attachment, and save it to file, delete the attachment from PDF programmatically with C#.

## Add Attachment from a File in an Existing PDF

You can add an attachment in an existing PDF file using [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class. The attachment can be added from a file on the disk using the file path. You can add attachment using [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) method. This method takes two arguments: file path and attachment description. First, you need to open the existing PDF file and add the attachement into it. Then you can save the output PDF file using [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) method of [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). 

The following code snippet shows you how to add attachment from a file. For example, let's add the MP3 file.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachment()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor =  new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf")))
    {
        editor.AddDocumentAttachment(dataDir + "Demo_MP3.mp3", "Demo MP3 file");

        // Save PDF document
        editor.Save(dataDir + "AddAttachment_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachment()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf"));
    editor.AddDocumentAttachment(dataDir + "Demo_MP3.mp3", "Demo MP3 file");

    // Save PDF document
    editor.Save(dataDir + "AddAttachment_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Add Attachment from a Stream in an Existing PDF

Attachment can be added in a PDF file from a stream – FileStream – using [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) method. This method takes three arguments: stream, attachment name, and attachment description. In order to add attachment, you need to create an object of [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class and bind the input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method. After that, you can call [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) method to add the attachment. Finally, you can call Save method to save the updated PDF file. The following code snippet shows you how to add attachment from a Stream.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachment()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf")))
    {
        var fileStream = File.OpenRead(dataDir + "Demo_MP3.mp3");
        editor.AddDocumentAttachment(fileStream, "Demo_MP3.mp3", "Demo MP3 file");

        // Save PDF document
        editor.Save(dataDir + "AddAttachment_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachment()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf"));

    var fileStream = File.OpenRead(dataDir + "Demo_MP3.mp3");
    editor.AddDocumentAttachment(fileStream, "Demo_MP3.mp3", "Demo MP3 file");

    // Save PDF document
    editor.Save(dataDir + "AddAttachment_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Delete All Attachments from an Existing PDF File

[DeleteAttachments](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments) method of [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class allows you to delete all the attachments from an existing PDF file. Call the [DeleteAttachments](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments) method. Finally, you have to call [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) method to save the updated PDF file. The following code snippet shows you how to delete all attachments from an existing PDF file.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteAllAttachments()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "DeleteAllAttachments.pdf")))
    {
        editor.DeleteAttachments();

        // Save PDF document
        editor.Save(dataDir + "DeleteAllAttachments_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteAllAttachments()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "DeleteAllAttachments.pdf"));
    editor.DeleteAttachments();

    // Save PDF document
    editor.Save(dataDir + "DeleteAllAttachments_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}
