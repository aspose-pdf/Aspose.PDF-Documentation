---
title: Guardar documento PDF programáticamente
linktitle: Guardar PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /es/net/save-pdf-document/
description: Aprenda cómo guardar archivos PDF en la biblioteca PDF Aspose.PDF for .NET en C#. Guarde documentos PDF en el sistema de archivos, en flujos y en aplicaciones web.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Save PDF document programmatically",
    "alternativeHeadline": "Programmatic PDF Saving with C#",
    "abstract": "Descubra cómo los desarrolladores guardan documentos PDF programáticamente con facilidad utilizando Aspose.PDF for .NET. Esta función admite el guardado de PDFs en el sistema de archivos, flujos y directamente dentro de aplicaciones web, acomodando diversos casos de uso mientras asegura el cumplimiento de los estándares PDF/A y PDF/X para archivo a largo plazo e intercambio gráfico. Optimice sus capacidades de manejo de PDF con este robusto mecanismo de guardado",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "471",
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
    "url": "/net/save-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/save-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también hacer frente a objetivos más complejos. Consulte la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

El siguiente fragmento de código también funciona con la biblioteca [Aspose.Drawing](/pdf/es/net/drawing/).

## Guardar documento PDF en el sistema de archivos

Puede guardar el documento PDF creado o manipulado en el sistema de archivos utilizando el método `Save` de la clase `Document`.
Cuando no proporciona el tipo de formato (opciones), el documento se guarda en el formato Aspose.PDF v.1.7 (*.pdf).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Make some manipation, i.g add new empty page
        document.Pages.Add();
        // Save PDF document
        document.Save(dataDir + "SimpleResume_out.pdf");
    }
}
```

## Guardar documento PDF en un flujo

También puede guardar el documento PDF creado o manipulado en un flujo utilizando sobrecargas de los métodos `Save`.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveDocumentStream()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Make some manipation, i.g add new empty page
        document.Pages.Add();
        // Save PDF document
        document.Save(dataDir + "SimpleResume_out.pdf");
    }
}
```

Para una explicación más detallada, consulte la sección [Showcase](/pdf/es/net/showcases/).

## Guardar formato PDF/A o PDF/X

PDF/A es una versión estandarizada por ISO del Formato de Documento Portátil (PDF) para su uso en archivo y preservación a largo plazo de documentos electrónicos.
PDF/A se diferencia de PDF en que prohíbe características no adecuadas para el archivo a largo plazo, como el enlace de fuentes (en lugar de la incrustación de fuentes) y la encriptación. Los requisitos de ISO para los visores PDF/A incluyen pautas de gestión del color, soporte de fuentes incrustadas y una interfaz de usuario para leer anotaciones incrustadas.

PDF/X es un subconjunto del estándar ISO PDF. El propósito de PDF/X es facilitar el intercambio gráfico, y por lo tanto tiene una serie de requisitos relacionados con la impresión que no se aplican a los archivos PDF estándar.

En ambos casos, se utiliza el método `Save` para almacenar los documentos, mientras que los documentos deben ser preparados utilizando el método `Convert`.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveDocumentAsPDFx()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Add page
        document.Pages.Add();
        // Convert a document to a PDF/X-3 format
        document.Convert(new Aspose.Pdf.PdfFormatConversionOptions(Aspose.Pdf.PdfFormat.PDF_X_3));
        // Save PDF document
        document.Save(dataDir + "SimpleResume_X3.pdf");
    }
}
```