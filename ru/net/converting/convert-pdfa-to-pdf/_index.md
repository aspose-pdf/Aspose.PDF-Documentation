---
title: Конвертация PDF/A в формат PDF
linktitle: Конвертация PDF/A в формат PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 110
url: /ru/net/convert-pdfa-to-pdf/
lastmod: "2021-11-01"
description: Эта тема показывает, как Aspose.PDF позволяет конвертировать файл PDF/A в документ PDF с помощью библиотеки .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF/A to PDF format",
    "alternativeHeadline": "Remove PDF/A Compliance for Enhanced Document Flexibility in C#",
    "abstract": "Aspose.PDF теперь предоставляет возможность бесшовно конвертировать файлы PDF/A в стандартные PDF-документы с использованием своей библиотеки .NET. Эта функция позволяет пользователям удалять ограничения соответствия PDF/A, что упрощает редактирование и модификацию содержимого PDF без ограничений, налагаемых стандартами PDF/A.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "259",
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
    "url": "/net/convert-pdfa-to-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdfa-to-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Конвертация документа PDF/A в PDF

Конвертация документа PDF/A в PDF означает удаление <abbr title="Portable Document Format Archive">PDF/A</abbr> ограничения из оригинального документа. 
Класс [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) имеет метод [RemovePdfaCompliance(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/removepdfacompliance) для удаления информации о соответствии PDF из входного/исходного файла.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFAtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFAToPDF.pdf"))
    {
        // Remove PDF/A compliance information
        document.RemovePdfaCompliance();
    
        // Save PDF document
        document.Save(dataDir + "PDFAToPDF_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFAtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "PDFAToPDF.pdf");

    // Remove PDF/A compliance information
    document.RemovePdfaCompliance();
    
    // Save PDF document
    document.Save(dataDir + "PDFAToPDF_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

Соответствие PDF/A также может быть удалено, если вы вносите какие-либо изменения в документ (например, добавляете страницы). В следующем примере выходной документ теряет соответствие PDF/A после добавления новой страницы.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFAtoPDFAdvanced()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFAToPDF.pdf"))
    {
        // Adding a new (empty) page removes PDF/A compliance information.
        document.Pages.Add();

        // Save PDF document
        document.Save(dataDir + "PDFAToPDF_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFAtoPDFAdvanced()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "PDFAToPDF.pdf");

    // Adding a new (empty) page removes PDF/A compliance information.
    document.Pages.Add();

    // Save PDF document
    document.Save(dataDir + "PDFAToPDF_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}