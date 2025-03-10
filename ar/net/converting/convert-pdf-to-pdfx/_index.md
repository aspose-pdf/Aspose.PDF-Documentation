---
title: تحويل ملف PDF إلى تنسيق PDF/X
linktitle: تحويل ملف PDF إلى تنسيق PDF/X
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 120
url: /ar/net/convert-pdf-to-pdfx/
lastmod: "2025-01-16"
description: تعلم كيفية تحويل ملف PDF إلى تنسيق PDF/X لأغراض تبادل الرسومات والطباعة باستخدام Aspose.PDF for .NET.
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
    "abstract": "يدعم Aspose.PDF for .NET تحويل ملفات PDF القياسية إلى تنسيقات متوافقة مع PDF/X بسهولة. هذه الميزة لا تضمن الامتثال لمعايير PDF/X من خلال التحقق الشامل فحسب، بل تسمح أيضًا باستخدام ملف ICC مخصص لضمان تبادل الرسومات بشكل صحيح في كل بيئة. استكشف القدرات القوية لـ Aspose.PDF لتحويل PDF/X بكفاءة وموثوقية",
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
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

**Aspose.PDF for .NET** يتيح لك تحويل ملف PDF إلى ملف PDF متوافق مع <abbr title="Portable Document Format eXchange">PDF/X</abbr>. يشرح هذا المقال كيفية القيام بذلك.

تعمل مقتطفات الكود التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

## المعايير المدعومة
**Aspose.PDF for .NET** يدعم المعايير التالية: PDF/X-1a:2001، PDF/X-1a:2003، PDF/X-3:2003، PDF/X-4.

## تحويل ملف PDF إلى PDF/X-4 مع ملف ICC خارجي

تظهر مقتطفات الكود التالية كيفية تحويل ملفات PDF إلى PDF متوافقة مع PDF/X-4 وتوفير ملف ICC خارجي لضمان تقديم الألوان بشكل صحيح.

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