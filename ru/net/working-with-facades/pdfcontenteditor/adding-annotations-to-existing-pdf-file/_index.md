---
title: Добавление аннотаций в существующий PDF файл
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ru/net/adding-annotations-to-existing-pdf-file/
description: Узнайте, как добавлять аннотации, такие как комментарии или выделения, в существующие PDF документы в .NET с использованием Aspose.PDF.
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
    "abstract": "Улучшите ваши PDF документы с помощью нашей новой функции аннотирования, позволяющей пользователям добавлять различные типы аннотаций, включая свободный текст, текст и аннотации линий, без проблем. Используя PdfContentEditor, вы можете легко связать существующие PDF файлы и указать области аннотаций, улучшая интерактивность и ясность документа всего лишь несколькими строками кода. Оптимизируйте свой рабочий процесс, интегрируя богатые аннотации непосредственно в ваши PDF, повышая вовлеченность пользователей и понимание",
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
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Добавление аннотации свободного текста в существующий PDF файл (facades)

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) позволяет добавлять аннотации различных типов в существующий PDF файл. Вы можете использовать соответствующий метод для добавления конкретной аннотации. Например, в следующем фрагменте кода мы использовали метод [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) для добавления аннотации типа [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation).

Любой тип аннотаций можно добавить в PDF файл тем же способом. Прежде всего, вам нужно создать объект типа [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) и связать входной PDF файл с помощью метода [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Во-вторых, вам нужно создать объект Rectangle, чтобы указать область аннотации.

После этого вы можете вызвать метод [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) для добавления аннотации [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation), а затем использовать метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) для сохранения обновленного PDF файла.

Следующий фрагмент кода показывает, как добавить аннотацию свободного текста в PDF файл.

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

## Добавление текстовой аннотации в существующий PDF файл (facades)

В этом примере также необходимо создать объект типа [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) и связать входной PDF файл с помощью метода [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Во-вторых, вам нужно создать объект Rectangle, чтобы указать область аннотации. После этого вы можете вызвать метод [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) для добавления аннотации FreeText, создать заголовок ваших аннотаций и номер страницы, на которой находится аннотация.

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

## Добавление аннотации линии в существующий PDF файл (facades)

Мы также указываем Rectangle, координаты начала и конца линии, номер страницы, толщину, стиль и цвет рамки аннотации, тип штриха линии, тип начала и конца линии.

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