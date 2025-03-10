---
title: Convertir PDF al formato de intercambio PDF/X
linktitle: Convertir PDF al formato de intercambio PDF/X
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 120
url: /es/net/convert-pdf-to-pdfx/
lastmod: "2025-01-16"
description: Aprenda cómo convertir un archivo PDF al formato PDF/X para intercambio gráfico e impresión utilizando Aspose.PDF for .NET.
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
    "abstract": "El soporte de PDF/X en Aspose.PDF for .NET permite la conversión fácil de archivos PDF estándar a varios formatos compatibles con PDF/X. Esta función no solo garantiza el cumplimiento de los estándares PDF/X a través de una validación exhaustiva, sino que también permite emplear un perfil ICC personalizado para asegurar un intercambio gráfico adecuado en cada entorno. Explore las robustas capacidades de Aspose.PDF para una conversión PDF/X eficiente y confiable.",
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
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulte la siguiente sección para usuarios avanzados y desarrolladores."
}
</script>

**Aspose.PDF for .NET** le permite convertir un archivo PDF a un archivo PDF compatible con <abbr title="Portable Document Format eXchange">PDF/X</abbr>. Este artículo explica cómo.

Los siguientes fragmentos de código también funcionan con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Estándares soportados
**Aspose.PDF for .NET** soporta los siguientes estándares: PDF/X-1a:2001, PDF/X-1a:2003, PDF/X-3:2003, PDF/X-4.

## Convertir archivo PDF a PDF/X-4 con perfil ICC externo

El siguiente fragmento de código muestra cómo convertir archivos PDF a PDF/X-4 compatibles y proporcionar un perfil ICC externo para asegurar la correcta representación del color.

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