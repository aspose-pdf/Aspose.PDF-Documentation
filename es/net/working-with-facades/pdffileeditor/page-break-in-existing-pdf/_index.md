---
title: Salto de página en PDF existente
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /es/net/page-break-in-existing-pdf/
description: Descubre cómo insertar saltos de página en un archivo PDF existente en .NET utilizando Aspose.PDF para una mejor gestión de páginas.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Page Break in existing PDF",
    "alternativeHeadline": "Insert Custom Page Breaks in PDF Files",
    "abstract": "Presentando la funcionalidad de salto de página en la clase PdfFileEditor, que permite a los usuarios controlar el diseño de documentos PDF existentes con precisión. Esta característica permite la inserción de saltos de página en ubicaciones específicas dentro del documento, mejorando la personalización y la presentación general del contenido. Con llamadas a métodos simples, los usuarios pueden modificar fácilmente sus PDFs para cumplir con requisitos de formato específicos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "369",
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
    "url": "/net/page-break-in-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/page-break-in-existing-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

Como diseño predeterminado, los contenidos dentro de los archivos PDF se añaden en un diseño de arriba a la izquierda a abajo a la derecha. Una vez que los contenidos superan el margen inferior de la página, ocurre el salto de página. Sin embargo, puede que te encuentres con la necesidad de insertar un salto de página dependiendo del requerimiento. Se ha añadido un método llamado AddPageBreak(...) en la clase [PdfFileEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffileeditor) para cumplir con este requisito.

1. [public void AddPageBreak(Document src, Document dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.pdffileeditor/addpagebreak/methods/1).
1. [public void AddPageBreak(string src, string dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.pdffileeditor/addpagebreak/methods/2).
1. [public void AddPageBreak(Stream src, Stream dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffileeditor/methods/addpagebreak).

- src es el documento de origen/ruta al documento/flujo con el documento de origen.
- dest es el documento de destino/ruta donde se guardará el documento/flujo donde se guardará el documento.
- PageBreak es un arreglo de objetos de salto de página. Tiene dos propiedades: el índice de la página donde debe colocarse el salto de página y la posición vertical del salto de página en la página.

## Ejemplo 1 (Agregar salto de página)

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PageBrakeExample01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_PageBreak();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PageBreak.pdf"))
    {
        // Create PDF document
        using (var dest = new Aspose.Pdf.Document())
        {
            // Create PdfFileEditor object
            var fileEditor = new Aspose.Pdf.Facades.PdfFileEditor();
            fileEditor.AddPageBreak(document, dest, new Aspose.Pdf.Facades.PdfFileEditor.PageBreak[]
            {
                new Aspose.Pdf.Facades.PdfFileEditor.PageBreak(1, 450)
            });
            // Save PDF document
            dest.Save(dataDir + "PageBreak_out.pdf");
        }
    }
}
```

## Ejemplo 2

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PageBrakeExample02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_PageBreak();

    // Create PdfFileEditor object
    var fileEditor = new Aspose.Pdf.Facades.PdfFileEditor();

    fileEditor.AddPageBreak(dataDir + "PageBreak.pdf",
        dataDir + "PageBreakWithDestPath_out.pdf",
        new Aspose.Pdf.Facades.PdfFileEditor.PageBreak[]
        {
            new Aspose.Pdf.Facades.PdfFileEditor.PageBreak(1, 450)
        });
}
```

## Ejemplo 3

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PageBrakeExample03()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_PageBreak();

    using (var src = new FileStream(dataDir + "PageBreak.pdf", FileMode.Open, FileAccess.Read))
    {
        using (var dest = new FileStream(dataDir + "PageBreakWithStream_out.pdf", FileMode.Create, FileAccess.ReadWrite))
        {
            // Create PdfFileEditor object
            var fileEditor = new Aspose.Pdf.Facades.PdfFileEditor();

            // Add page break
            fileEditor.AddPageBreak(src, dest,
                new[]
                {
                    new Aspose.Pdf.Facades.PdfFileEditor.PageBreak(1, 450)
                });
        }
    }
}
```