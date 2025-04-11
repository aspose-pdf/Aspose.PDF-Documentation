---
title: Convertir PDF a formatos PDF/A
linktitle: Convertir PDF a formatos PDF/A
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 100
url: /es/net/convert-pdf-to-pdfa/
lastmod: "2021-11-01"
description: Aprenda cómo convertir un archivo PDF a formato PDF/A para fines de archivo utilizando Aspose.PDF en .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to PDF/A formats",
    "alternativeHeadline": "Effortless PDF to PDF/A Conversion with Validation in C#",
    "abstract": "La función en Aspose.PDF for .NET permite la conversión sin problemas de archivos PDF estándar a varios formatos compatibles con PDF/A, incluyendo PDF/A-1b, PDF/A-2u y PDF/A-3a. Esta función no solo asegura el cumplimiento de los estándares PDF/A a través de una validación exhaustiva, sino que también permite la adjunción de archivos adicionales y la sustitución de fuentes faltantes, mejorando la integridad y accesibilidad del documento. Explore las robustas capacidades de Aspose.PDF para conversiones PDF/A eficientes y confiables.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1885",
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
    "url": "/net/convert-pdf-to-pdfa/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-pdfa/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulte la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

**Aspose.PDF for .NET** le permite convertir un archivo PDF a un archivo PDF compatible con <abbr title="Portable Document Format / A">PDF/A</abbr>. Antes de hacerlo, el archivo debe ser validado. Este tema explica cómo.

- [Convertir PDF a PDF/A-1b](#csharp-convert-pdf-to-a1b)
- [Convertir PDF a PDF/A-3b](#csharp-convert-pdf-to-a3b)
- [Convertir PDF a PDF/A-4](#csharp-convert-pdf-to-a4)

{{% alert color="primary" %}}

Tenga en cuenta que seguimos Adobe Preflight y veraPDF para validar la conformidad con PDF/A. Todas las herramientas en el mercado tienen su propia “representación” de la conformidad con PDF/A. Consulte este artículo sobre herramientas de validación de PDF/A para referencia. Elegimos productos de Adobe para verificar cómo Aspose.PDF produce archivos PDF porque Adobe está en el centro de todo lo relacionado con PDF.

{{% /alert %}}

Convierta el archivo utilizando el método Convert de la clase Document. Antes de convertir el PDF a un archivo compatible con PDF/A, valide el PDF utilizando el método Validate. El resultado de la validación se almacena en un archivo XML y luego este resultado también se pasa al método Convert. También puede especificar la acción para los elementos que no se pueden convertir utilizando la enumeración ConvertErrorAction.

{{% alert color="success" %}}
**Intente convertir PDF a PDF/A en línea**

Aspose.PDF for .NET le presenta una aplicación gratuita en línea ["PDF a PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de PDF a PDF/A con aplicación gratuita](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

## Estándares soportados
Soportamos los siguientes estándares: PDF/A-1b, PDF/A-1a, PDF/A-2b, PDF/A-2u, PDF/A-2a, PDF/A-3b, PDF/A-3u, PDF/A-3a, PDF/A-4, PDF/A-4e, PDF/A-4f.

## Convertir archivo PDF a PDF/A-1b

<a name="csharp-convert-pdf-to-a1b" id="csharp-convert-pdf-to-a1b"><strong>Convertir PDF a PDF/A-1b</strong></a>

El siguiente fragmento de código muestra cómo convertir archivos PDF a PDF compatibles con PDF/A-1b.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfToPdfA()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf"))
    {
        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        document.Convert(dataDir + "PDFA1bConversionLog.xml", Aspose.Pdf.PdfFormat.PDF_A_1B, Aspose.Pdf.ConvertErrorAction.Delete);
        
        // Save PDF document
        document.Save(dataDir + "PDFToPDFA_out.pdf");
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
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf");

    // Convert to PDF/A compliant document
    // During conversion process, the validation is also performed
    document.Convert(dataDir + "PDFA1bConversionLog.xml", Aspose.Pdf.PdfFormat.PDF_A_1B, Aspose.Pdf.ConvertErrorAction.Delete);
    
    // Save PDF document
    document.Save(dataDir + "PDFToPDFA_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

Para realizar solo la validación, use la siguiente línea de código:

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ValidatePdfAStandard()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ValidatePDFAStandard.pdf"))
    {
        // Validate PDF for PDF/A-1a
        document.Validate(dataDir + "ValidationResultA1b.xml", Aspose.Pdf.PdfFormat.PDF_A_1B);
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ValidatePdfAStandard()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "ValidatePDFAStandard.pdf");

    // Validate PDF for PDF/A-1a
    document.Validate(dataDir + "ValidationResultA1b.xml", Aspose.Pdf.PdfFormat.PDF_A_1B);
}
```
{{< /tab >}}
{{< /tabs >}}

## Convertir archivo PDF a PDF/A-3b

<a name="csharp-convert-pdf-to-a3b" id="csharp-convert-pdf-to-a3b"><strong>Convertir PDF a PDF/A-3b</strong></a>

Aspose.PDF for .NET también admite la función de convertir un archivo PDF al formato PDF/A-3b.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfToPdfA3b()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf"))
    {
        // Convert to PDF/A compliant document, log file is omitted
        document.Convert(Stream.Null, Aspose.Pdf.PdfFormat.PDF_A_3B, Aspose.Pdf.ConvertErrorAction.Delete);
        
        // Save PDF document
        document.Save(dataDir + "PDFToPDFA3b_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfToPdfA3b()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf");

    // Convert to PDF/A compliant document, log file is omitted
    document.Convert(Stream.Null, Aspose.Pdf.PdfFormat.PDF_A_3B, Aspose.Pdf.ConvertErrorAction.Delete);

    // Save PDF document
    document.Save(dataDir + "PDFToPDFA3b_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Convertir archivo PDF a PDF/A-4

<a name="csharp-convert-pdf-to-a4" id="csharp-convert-pdf-to-a4"><strong>Convertir PDF a PDF/A-4</strong></a>

Aspose.PDF for .NET también admite la función de convertir un archivo PDF al formato PDF/A-4.

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfToPdfA4()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf"))
    {
        // If the document version is less than PDF-2.0, it must be converted to PDF-2.0
        document.Convert(Stream.Null, Aspose.Pdf.PdfFormat.v_2_0, Aspose.Pdf.ConvertErrorAction.Delete);
    
        // Convert to the PDF/A-4 format
        document.Convert(dataDir + "PDFA4ConversionLog.xml", Aspose.Pdf.PdfFormat.PDF_A_4, Aspose.Pdf.ConvertErrorAction.Delete);

        // Save PDF document
        document.Save(dataDir + "PDFToPDFA4_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfToPdfA4()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf");

    // If the document version is less than PDF-2.0, it must be converted to PDF-2.0
    document.Convert(Stream.Null, Aspose.Pdf.PdfFormat.v_2_0, Aspose.Pdf.ConvertErrorAction.Delete);

    // Convert to the PDF/A-4 format
    document.Convert(dataDir + "PDFA4ConversionLog.xml", Aspose.Pdf.PdfFormat.PDF_A_4, Aspose.Pdf.ConvertErrorAction.Delete);

    // Save PDF document
    document.Save(dataDir + "PDFToPDFA4_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Agregar archivo adjunto a archivo PDF/A

En caso de que tenga un requisito para adjuntar archivos a un documento compatible con PDF/A, le recomendamos usar un valor PDF_A_3A de la enumeración Aspose.PDF.PdfFormat.
PDF/A-3a es el formato que proporciona la función para adjuntar cualquier formato de archivo como un archivo adjunto a un archivo compatible con PDF/A.

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachmentToPdfA()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf"))
    {
        // Setup new file to be added as attachment
        using (var fileSpecification = new Aspose.Pdf.FileSpecification(dataDir + "aspose-logo.jpg", "Large Image file"))
        {
            // Add attachment to document's attachment collection
            document.EmbeddedFiles.Add(fileSpecification);

            // Perform conversion to PDF/A-3a, so that the attachment is included in the resultant file
            document.Convert(dataDir + "PDFA3aConversionLog.xml", Aspose.Pdf.PdfFormat.PDF_A_3A, Aspose.Pdf.ConvertErrorAction.Delete);

            // Save PDF document
            document.Save(dataDir + "AddAttachmentToPDFA_out.pdf");
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachmentToPdfA()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf");

    // Setup new file to be added as attachment
    using var fileSpecification = new Aspose.Pdf.FileSpecification(dataDir + "aspose-logo.jpg", "Large Image file");

    // Add attachment to document's attachment collection
    document.EmbeddedFiles.Add(fileSpecification);

    // Perform conversion to PDF/A-3a, so that the attachment is included in the resultant file
    document.Convert(dataDir + "PDFA3aConversionLog.xml", Aspose.Pdf.PdfFormat.PDF_A_3A, Aspose.Pdf.ConvertErrorAction.Delete);

    // Save PDF document
    document.Save(dataDir + "AddAttachmentToPDFA_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Reemplazar fuentes faltantes con fuentes alternativas

Según los estándares PDF/A, las fuentes deben estar incrustadas en un documento PDF/A. Sin embargo, si las fuentes no están incrustadas en el documento fuente y no existen en la máquina, la conversión a PDF/A falla. En este caso, es necesario sustituir las fuentes faltantes por algunas fuentes alternativas que existan en la máquina. Las fuentes faltantes se pueden sustituir utilizando la clase SimpleFontSubsitution durante la conversión de PDF a PDF/A.

{{< tabs tabID="6" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceMissingFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    try
    {
        // Check whether a font, used in the source document, is installed in the system
        Aspose.Pdf.Text.FontRepository.FindFont("AgencyFB");
    }
    catch (Aspose.Pdf.FontNotFoundException)
    {
        // Font is missing on the destination machine. Replace it with the Arial font installed in the system
        var fontSubstitution = new Aspose.Pdf.Text.SimpleFontSubstitution("AgencyFB", "Arial");
        Aspose.Pdf.Text.FontRepository.Substitutions.Add(fontSubstitution);
    }

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf"))
    {
        // During the conversion, the missing font will be replaced with the substitution one
        document.Convert(dataDir + "ReplaceMissingFonts.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

        // Save PDF document
        document.Save(dataDir + "ReplaceMissingFonts_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceMissingFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    try
    {
        // Check whether a font, used in the source document, is installed in the system
        Aspose.Pdf.Text.FontRepository.FindFont("AgencyFB");
    }
    catch (Aspose.Pdf.FontNotFoundException)
    {
        // Font is missing on the destination machine. Replace it with the Arial font installed in the system
        var fontSubstitution = new Aspose.Pdf.Text.SimpleFontSubstitution("AgencyFB", "Arial");
        Aspose.Pdf.Text.FontRepository.Substitutions.Add(fontSubstitution);
    }

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf");

    // During the conversion, the missing font will be replaced with the substitution one
    document.Convert(dataDir + "ReplaceMissingFonts.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

    // Save PDF document
    document.Save(dataDir + "ReplaceMissingFonts_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}