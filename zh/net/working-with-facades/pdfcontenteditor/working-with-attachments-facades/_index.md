---
title: 使用附件 - 外观
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /zh/net/working-with-attachments-facades/
description: 本节解释如何使用 PdfContentEditor 类处理附件 - 外观。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Attachments - Facades",
    "alternativeHeadline": "Enhanced PDF Attachment Management",
    "abstract": "Aspose.PDF for .NET 中的使用附件 - 外观功能使用户能够轻松管理 PDF 文档中的文件附件。通过使用 PdfContentEditor 类以编程方式添加、检索和删除各种文件类型的功能，该功能通过允许无缝集成附件来简化增强 PDF 交互性的过程。",
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
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一节以获取高级用户和开发人员的信息。"
}
</script>

在本节中，我们将解释如何使用 Aspose.PDF for .NET 外观处理 PDF 中的附件。附件是附加到父文档的附加文件，可以是多种文件类型，例如 pdf、word、图像或其他文件。您将学习如何将附件添加到 pdf、获取附件的信息并将其保存到文件中，以及使用 C# 从 PDF 中以编程方式删除附件。

## 从现有 PDF 文件中添加附件

您可以使用 [PdfContentEditor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfcontenteditor) 类在现有 PDF 文件中添加附件。附件可以通过文件路径从磁盘上的文件添加。您可以使用 [AddDocumentAttachment](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) 方法添加附件。该方法接受两个参数：文件路径和附件描述。首先，您需要打开现有的 PDF 文件并将附件添加到其中。然后，您可以使用 [PdfContentEditor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfcontenteditor) 的 [Save](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document/methods/save/index) 方法保存输出 PDF 文件。

以下代码片段演示了如何从文件中添加附件。例如，让我们添加 MP3 文件。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

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
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf"));
    editor.AddDocumentAttachment(dataDir + "Demo_MP3.mp3", "Demo MP3 file");

    // Save PDF document
    editor.Save(dataDir + "AddAttachment_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## 从现有 PDF 文件中的流添加附件

可以使用 [AddDocumentAttachment](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) 方法从流 - FileStream - 在 PDF 文件中添加附件。该方法接受三个参数：流、附件名称和附件描述。为了添加附件，您需要创建 [PdfContentEditor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfcontenteditor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/facade/methods/bindpdf/index) 方法绑定输入 PDF 文件。之后，您可以调用 [AddDocumentAttachment](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) 方法来添加附件。最后，您可以调用 Save 方法来保存更新后的 PDF 文件。以下代码片段演示了如何从流中添加附件。

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

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
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

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

## 从现有 PDF 文件中删除所有附件

[DeleteAttachments](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments) 方法允许您从现有 PDF 文件中删除所有附件。调用 [DeleteAttachments](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments) 方法。最后，您必须调用 [Save](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document/methods/save/index) 方法以保存更新后的 PDF 文件。以下代码片段演示了如何从现有 PDF 文件中删除所有附件。

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteAllAttachments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

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
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "DeleteAllAttachments.pdf"));
    editor.DeleteAttachments();

    // Save PDF document
    editor.Save(dataDir + "DeleteAllAttachments_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}