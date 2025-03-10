---
title: Convertir PDF/A a formato PDF
linktitle: Convertir PDF/A a formato PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 110
url: /es/net/convert-pdfa-to-pdf/
lastmod: "2021-11-01"
description: Este tema te muestra cómo Aspose.PDF permite convertir un archivo PDF/A a un documento PDF con la biblioteca .NET.
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
    "abstract": "Aspose.PDF ahora proporciona una función para convertir sin problemas archivos PDF/A a documentos PDF estándar utilizando su biblioteca .NET. Esta funcionalidad permite a los usuarios eliminar las restricciones de conformidad con PDF/A, lo que facilita la edición y modificación del contenido PDF sin las limitaciones impuestas por los estándares PDF/A.",
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
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Convertir documento PDF/A a PDF

Convertir un documento PDF/A a PDF significa eliminar la <abbr title="Portable Document Format Archive">conformidad PDF/A</abbr> del documento original. 
La clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) tiene el método [RemovePdfaCompliance(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/removepdfacompliance) para eliminar la información de conformidad PDF del archivo de entrada/origen.

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

La conformidad con PDF/A también puede ser eliminada si realizas algún cambio en el documento (por ejemplo, agregar páginas). En el siguiente ejemplo, el documento de salida pierde la conformidad PDF/A después de que se agrega una nueva página.

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