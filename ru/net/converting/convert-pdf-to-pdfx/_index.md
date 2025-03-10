---
title: Преобразование PDF в формат обмена PDF/X
linktitle: Преобразование PDF в формат обмена PDF/X
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 120
url: /ru/net/convert-pdf-to-pdfx/
lastmod: "2025-01-16"
description: Узнайте, как преобразовать файл PDF в формат PDF/X для обмена графикой и печати с помощью Aspose.PDF for .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to PDF/X exchange format",
    "alternativeHeadline": "Effortless PDF to PDF/X Conversion in C#",
    "abstract": "Поддержка PDF/X в Aspose.PDF для .NET позволяет легко преобразовывать стандартные PDF-файлы в различные форматы, совместимые с PDF/X. Эта функция не только обеспечивает соответствие стандартам PDF/X за счёт комплексной проверки, но и позволяет использовать пользовательский ICC-профиль для обеспечения корректного обмена графикой в любой среде. Изучите надёжные возможности Aspose.PDF для эффективного и надёжного преобразования PDF/X",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1064",
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
    "url": "/net/convert-pdf-to-pdfx/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-pdfx/"
    },
    "dateModified": "2025-01-16",
    "description": "Aspose.PDF может выполнять не только простые и лёгкие задачи, но и справляться с более сложными целями. Ознакомьтесь со следующим разделом для опытных пользователей и разработчиков."
}
</script>

**Aspose.PDF for .NET** позволяет преобразовать PDF-файл в PDF-файл, совместимый с форматом обмена **PDF/X**. В этой статье объясняется, как это сделать.

Следующие фрагменты кода также работают с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Поддерживаемые стандарты
**Aspose.PDF for .NET** поддерживает следующие стандарты: PDF/X-1a:2001, PDF/X-1a:2003, PDF/X-3:2003, PDF/X-4.

## Преобразование PDF-файла в PDF/X-4 с использованием внешнего профиля ICC

Следующий фрагмент кода показывает, как преобразовывать PDF-файлы в совместимые с PDF/X-4 PDF-файлы и предоставлять внешний профиль ICC для обеспечения правильного воспроизведения цветов.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfToPdfX()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFX.pdf"))
    {
        // Set up the desired PDF/X format with PdfFormatConversionOptions
        Aspose.Pdf.PdfFormatConversionOptions options = new Aspose.Pdf.PdfFormatConversionOptions(Aspose.Pdf.PdfFormat.PDF_X_4, Aspose.Pdf.ConvertErrorAction.Delete);

        // Provide the name of the external ICC profile file (optional)
        options.IccProfileFileName = dataDir + "ISOcoated_v2_eci.icc";

        // Provide an output condition identifier and other necessary OutputIntent properties (optional)
        options.OutputIntent = new Aspose.Pdf.OutputIntent("FOGRA39");

        // Convert to PDF/X compliant document
        document.Convert(options);
        
        // Save PDF document
        document.Save(dataDir + "PDFToPDFX4_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfToPdfA()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFX.pdf");

    // Set up the desired PDF/X format with PdfFormatConversionOptions
    Aspose.Pdf.PdfFormatConversionOptions options = new Aspose.Pdf.PdfFormatConversionOptions(Aspose.Pdf.PdfFormat.PDF_X_4, Aspose.Pdf.ConvertErrorAction.Delete);

    // Provide the name of the external ICC profile file (optional)
    options.IccProfileFileName = dataDir + "ISOcoated_v2_eci.icc";

    // Provide an output condition identifier and other necessary OutputIntent properties (optional)
    options.OutputIntent = new Aspose.Pdf.OutputIntent("FOGRA39");

    // Convert to PDF/X compliant document
    document.Convert(options);
    
    // Save PDF document
    document.Save(dataDir + "PDFToPDFX4_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}