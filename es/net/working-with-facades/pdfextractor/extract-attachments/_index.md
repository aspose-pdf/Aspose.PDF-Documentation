---
title: Extraer Archivos Adjuntos de un Archivo PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/extract-attachments/
description: Descubre cómo extraer y gestionar archivos adjuntos en documentos PDF en .NET utilizando Aspose.PDF para un mejor manejo de documentos.
lastmod: "2021-06-05"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Attachments from PDF File",
    "alternativeHeadline": "Effortlessly Extract and Manage PDF Attachments",
    "abstract": "La nueva funcionalidad de extracción de archivos adjuntos en Aspose.PDF for .NET permite a los desarrolladores recuperar y gestionar fácilmente archivos adjuntos dentro de documentos PDF. Al utilizar la clase PdfExtractor, los usuarios pueden extraer archivos adjuntos y obtener información esencial, como nombres y detalles de los archivos adjuntos, mejorando las capacidades de procesamiento de documentos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "208",
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
    "url": "/net/extract-attachments/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-attachments/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

Una de las principales categorías bajo las capacidades de extracción del [espacio de nombres Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) es la extracción de archivos adjuntos. Esta categoría proporciona un conjunto de métodos, que no solo ayudan a extraer los archivos adjuntos, sino que también ofrecen métodos que pueden proporcionarte información relacionada con los archivos adjuntos, es decir, los métodos [GetAttachmentInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachmentinfo) y [GetAttachName](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachnames) proporcionan información sobre los archivos adjuntos y el nombre del archivo adjunto, respectivamente. Para extraer y luego obtener archivos adjuntos, utilizamos los métodos [ExtractAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractattachment) y [GetAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachment).

El siguiente fragmento de código te muestra cómo utilizar los métodos de PdfExtractor:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractAttachments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Create the extractor
    using (var pdfExtractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        pdfExtractor.BindPdf(dataDir + "GetAlltheAttachments.pdf");

        // Extract attachments
        pdfExtractor.ExtractAttachment();

        // Get attachment names
        if (pdfExtractor.GetAttachNames().Count > 0)
        {
            Console.WriteLine("Extracting and storing...");

            // Get extracted attachments
            pdfExtractor.GetAttachment(dataDir + "GetAlltheAttachments_out.pdf");
        }
    }
}
```