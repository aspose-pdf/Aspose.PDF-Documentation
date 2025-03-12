---
title: Извлечение изображения и изменение позиции штампа
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ru/net/extract-image-and-change-position-of-a-stamp/
description: Этот раздел объясняет, как извлечь изображение и изменить позицию штампа с помощью Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract image and change stamp position",
    "alternativeHeadline": "Extract Images and Adjust Stamp Positions in PDF",
    "abstract": "Функция в Aspose.PDF for .NET позволяет пользователям эффективно извлекать изображения из PDF-штампов и точно изменять их положение. Используя класс PdfContentEditor, разработчики могут легко управлять и манипулировать изображениями штампов, улучшая свои возможности редактирования PDF и улучшая общее представление документа",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "393",
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
    "url": "/net/extract-image-and-change-position-of-a-stamp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-image-and-change-position-of-a-stamp/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Извлечение изображения из штампа изображения

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) класс позволяет вам извлекать изображения из штампа в PDF-файле. Сначала вам нужно создать объект класса [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) и связать входной PDF-файл с помощью метода [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). После этого вызовите метод [GetStamps](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/getstamps), чтобы получить массив объектов StampInfo с определенной страницы PDF-файла. Затем вы можете получить изображение из StampInfo, используя свойство StampInfo.Image. Как только вы получите изображение, вы можете сохранить его или работать с различными свойствами изображения. Следующий фрагмент кода показывает, как извлечь изображение из штампа изображения.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImageFromStamp()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_StampsWatermarks();

    // Instantiate PdfContentEditor object
    using (var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        pdfContentEditor.BindPdf(dataDir + "ExtractImage-ImageStamp.pdf");

        // Get Stamp info for the first stamp
        var infos = pdfContentEditor.GetStamps(1);

        // Get the image from Stamp Info
        var image = infos[0].Image;

        // Save the extracted image
        image.Save(dataDir + "image_out.jpg");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImageFromStamp()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_StampsWatermarks();

    // Instantiate PdfContentEditor object
    using var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    pdfContentEditor.BindPdf(dataDir + "ExtractImage-ImageStamp.pdf");

    // Get Stamp info for the first stamp
    var infos = pdfContentEditor.GetStamps(1);

    // Get the image from Stamp Info
    var image = infos[0].Image;

    // Save the extracted image
    image.Save(dataDir + "image_out.jpg");
}
```
{{< /tab >}}
{{< /tabs >}}

## Изменение позиции штампа в PDF-файле

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) класс позволяет вам изменить позицию штампа в PDF-файле. Сначала вам нужно создать объект класса [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) и связать входной PDF-файл с помощью метода [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). После этого вызовите метод [MoveStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/movestamp) с индексом штампа и новой позицией на определенной странице PDF-файла. Затем вы можете сохранить обновленный файл, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Следующий фрагмент кода показывает, как переместить штамп на определенной странице.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangeStampPosition()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_StampsWatermarks();

    // Instantiate PdfContentEditor object
    using (var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        pdfContentEditor.BindPdf(dataDir + "ChangeStampPosition.pdf");

        int pageId = 1;
        int stampIndex = 1;
        double x = 200;
        double y = 200;

        // Change the position of the stamp to new x and y position
        pdfContentEditor.MoveStamp(pageId, stampIndex, x, y);

        // Save PDF document
        pdfContentEditor.Save(dataDir + "ChangeStampPosition_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangeStampPosition()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_StampsWatermarks();

    // Instantiate PdfContentEditor object
    using var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    pdfContentEditor.BindPdf(dataDir + "ChangeStampPosition.pdf");

    int pageId = 1;
    int stampIndex = 1;
    double x = 200;
    double y = 200;

    // Change the position of the stamp to new x and y position
    pdfContentEditor.MoveStamp(pageId, stampIndex, x, y);

    // Save PDF document
    pdfContentEditor.Save(dataDir + "ChangeStampPosition_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

Кроме того, вы можете использовать метод [MoveStampById](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/movestampbyid), чтобы переместить конкретный штамп, используя StampId.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MoveStampById()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_StampsWatermarks();

    // Instantiate PdfContentEditor Object
    using (var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        pdfContentEditor.BindPdf(dataDir + "ChangeStampPosition.pdf");

        int pageId = 1;
        int stampId = 1;
        double x = 200;
        double y = 200;

        // Change the position of the stamp to new x and y position
        pdfContentEditor.MoveStamp(pageId, stampId, x, y);

        // Save PDF document
        pdfContentEditor.Save(dataDir + "ChangeStampPositionByID_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MoveStampById()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_StampsWatermarks();

    // Instantiate PdfContentEditor Object
    using var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    pdfContentEditor.BindPdf(dataDir + "ChangeStampPosition.pdf");

    int pageId = 1;
    int stampId = 1;
    double x = 200;
    double y = 200;

    // Change the position of the stamp to new x and y position
    pdfContentEditor.MoveStamp(pageId, stampId, x, y);

    // Save PDF document
    pdfContentEditor.Save(dataDir + "ChangeStampPositionByID_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}