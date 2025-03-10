---
title: Работа с вложениями — фасады
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ru/net/working-with-attachments-facades/
description: В этом разделе объясняется, как работать со вложениями с помощью фасадов с использованием класса PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Attachments - Facades",
    "alternativeHeadline": "Enhanced PDF Attachment Management",
    "abstract": "Функция «Работа с вложениями — фасады» в Aspose.PDF для .NET позволяет пользователям легко управлять файловыми вложениями в PDF-документах. Благодаря функциям добавления, извлечения и удаления различных типов файлов программным способом с использованием класса PdfContentEditor эта функция упрощает процесс повышения интерактивности PDF, позволяя легко интегрировать вложения",
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
    "description": "Aspose.PDF может выполнять не только простые и лёгкие задачи, но и справляться с более сложными целями. Ознакомьтесь со следующим разделом для опытных пользователей и разработчиков."
}
</script>

В этом разделе мы объясним, как работать с вложениями в формате PDF с помощью фасадов Aspose.PDF for .NET. Вложение — это дополнительный файл, прикреплённый к родительскому документу, оно может быть разных типов, таких как PDF, Word, изображение или другие файлы. Вы узнаете, как добавлять вложения в PDF, получать информацию о вложении и сохранять её в файл, удалять вложение из PDF программно с помощью C#.

## Добавление вложения из файла в существующий PDF

Вы можете добавить вложение в существующий файл PDF с помощью класса [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). Вложение можно добавить из файла на диске, используя путь к файлу. Вы можете добавить вложение с помощью метода [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment). Этот метод принимает два аргумента: путь к файлу и описание вложения. Сначала вам нужно открыть существующий файл PDF и добавить в него вложение. Затем вы можете сохранить выходной файл PDF с помощью метода [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) класса [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor).

Следующий фрагмент кода показывает, как добавить вложение из файла. Например, давайте добавим файл MP3.

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

## Добавление вложения из потока в существующий PDF

Вложение можно добавить в файл PDF из потока — FileStream — с помощью метода [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment). Этот метод принимает три аргумента: поток, имя вложения и описание вложения. Чтобы добавить вложение, вам нужно создать объект класса [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) и связать входной файл PDF с помощью метода [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). После этого вы можете вызвать метод [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment), чтобы добавить вложение. Наконец, вы можете вызвать метод Save, чтобы сохранить обновлённый файл PDF. Следующий фрагмент кода показывает, как добавить вложение из потока.

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

## Удаление всех вложений из существующего файла PDF

Метод [DeleteAttachments](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments) класса [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) позволяет удалить все вложения из существующего файла PDF. Вызовите метод [DeleteAttachments](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments). Наконец, необходимо вызвать метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index), чтобы сохранить обновлённый файл PDF. Следующий фрагмент кода показывает, как удалить все вложения из существующего файла PDF.

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