---
title: Manipular Propiedades de Página
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /es/net/manipulate-page-properties/
description: Esta sección explica cómo manipular las Propiedades de Página con Aspose.PDF Facades utilizando la Clase PdfPageEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipulate Page Properties",
    "alternativeHeadline": "Enhance PDF Page Control with PdfPageEditor Features",
    "abstract": "Presentando la clase PdfPageEditor, una herramienta poderosa para gestionar las propiedades de página PDF con Aspose.PDF for .NET Facades. Esta función permite a los desarrolladores recuperar y modificar atributos esenciales de la página como rotación, niveles de zoom y dimensiones de la página, proporcionando un control preciso sobre la presentación del contenido PDF. Con métodos sencillos para obtener y establecer propiedades, incluyendo la capacidad de redimensionar contenidos de páginas específicas, mejorar documentos PDF nunca ha sido tan fácil.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "483",
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
    "url": "/net/manipulate-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-page-properties/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también hacer frente a objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Obtener Propiedades de Página PDF de un Archivo PDF Existente

[PdfPageEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfpageeditor) te permite trabajar con páginas individuales del archivo PDF. Te ayuda a obtener las propiedades de la página individual como diferentes tamaños de caja de página, rotación de página, zoom de página, etc. Para obtener esas propiedades, necesitas crear un objeto [PdfPageEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfpageeditor) y vincular el archivo PDF de entrada utilizando el método [BindPdf](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.facade/bindpdf/methods/3). Después de eso, puedes usar diferentes métodos para obtener las propiedades de la página como [GetPageRotation](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfpageeditor/methods/getpagerotation), [GetPages](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfpageeditor/methods/getpages), [GetPageBoxSize](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfpageeditor/methods/getpageboxsize), etc.

El siguiente fragmento de código te muestra cómo obtener las propiedades de página PDF de un archivo PDF existente.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPdfPageProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var pageEditor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        pageEditor.BindPdf(dataDir + "input.pdf");

        // Get page properties and print them to the console
        Console.WriteLine($"Page 1 Rotation: {pageEditor.GetPageRotation(1)}");
        Console.WriteLine($"Total Pages: {pageEditor.GetPages()}");
        Console.WriteLine($"Trim Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "trim")}");
        Console.WriteLine($"Art Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "art")}");
        Console.WriteLine($"Bleed Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "bleed")}");
        Console.WriteLine($"Crop Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "crop")}");
        Console.WriteLine($"Media Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "media")}");
    }
}
```

## Establecer Propiedades de Página PDF en un Archivo PDF Existente

Para establecer propiedades de página como rotación de página, zoom o punto de origen, necesitas usar la clase [PdfPageEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfpageeditor). Esta clase proporciona diferentes métodos y propiedades para establecer estas propiedades de página. Primero que todo, necesitas crear un objeto de la clase [PdfPageEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfpageeditor) y vincular el archivo PDF de entrada utilizando el método [BindPdf](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.facade/bindpdf/methods/3). Después de eso, puedes usar estos métodos y propiedades para establecer las propiedades de la página. Finalmente, guarda el archivo PDF actualizado utilizando el método [Save](https://reference.aspose.com/pdf/es/net/aspose.pdf/document/methods/save).

El siguiente fragmento de código te muestra cómo establecer las propiedades de página PDF en un archivo PDF existente.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPdfPageProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var pageEditor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        pageEditor.BindPdf(dataDir + "input.pdf");

        // Set page properties
        // Move origin from (0,0)
        pageEditor.MovePosition(100, 100);

        // Set page rotations
        var pageRotations = new System.Collections.Hashtable
        {
            { 1, 90 },
            { 2, 180 },
            { 3, 270 }
        };

        // Set zoom where 1.0f = 100% zoom
        pageEditor.Zoom = 2.0f;

        // Save PDF document
        pageEditor.Save(dataDir + "SetPageProperties_out.pdf");
    }
}
```

## Redimensionar Contenidos de Página de Páginas Específicas en un Archivo PDF

El método ResizeContents de la clase [PdfPageEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfpageeditor) te permite redimensionar los contenidos de la página en un archivo PDF. La clase [ContentsResizeParameters](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.pdffileeditor/contentsresizeparameters) se utiliza para especificar los parámetros que se utilizarán para redimensionar la(s) página(s), por ejemplo, márgenes en porcentaje o unidades, etc. Puedes redimensionar todas las páginas o especificar un arreglo de páginas a redimensionar utilizando el método ResizeContents.

El siguiente fragmento de código muestra cómo redimensionar los contenidos de algunas páginas específicas del archivo PDF.

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ResizePdfPageContents()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create PdfFileEditor Object
     var fileEditor = new Aspose.Pdf.Facades.PdfFileEditor();

     // Open PDF Document
     using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
     {
         // Specify Parameters to be used for resizing
         var parameters = new Aspose.Pdf.Facades.PdfFileEditor.ContentsResizeParameters(
             // Left margin = 10% of page width
             PdfFileEditor.ContentsResizeValue.Percents(10),
             // New contents width calculated automatically as width - left margin - right margin (100% - 10% - 10% = 80%)
             null,
             // Right margin is 10% of page
             PdfFileEditor.ContentsResizeValue.Percents(10),
             // Top margin = 10% of height
             PdfFileEditor.ContentsResizeValue.Percents(10),
             // New contents height is calculated automatically (similar to width)
             null,
             // Bottom margin is 10%
             PdfFileEditor.ContentsResizeValue.Percents(10)
         );

         // Resize Page Contents
         fileEditor.ResizeContents(document, new[] { 1, 2 }, parameters);

         // Save PDF document
         document.Save(dataDir + "ResizePageContents_out.pdf");
     }
 }
```