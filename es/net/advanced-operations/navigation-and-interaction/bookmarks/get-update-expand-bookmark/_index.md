---
title: Obtener, Actualizar y Expandir un Marcador
linktitle: Obtener, Actualizar y Expandir un Marcador
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /es/net/get-update-and-expand-bookmark/
description: Este artículo describe cómo usar marcadores en un archivo PDF con nuestra biblioteca Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get, Update and Expand a Bookmark",
    "alternativeHeadline": "Effortlessly Manage PDF Bookmarks",
    "abstract": "La nueva función Obtener, Actualizar y Expandir un Marcador mejora la biblioteca Aspose.PDF for .NET al proporcionar a los usuarios la capacidad de recuperar, modificar y expandir visualmente los marcadores dentro de los documentos PDF. Esta funcionalidad permite una navegación y organización eficientes del contenido PDF, facilitando la gestión de documentos complejos con estructuras de marcadores jerárquicas.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "get bookmarks, update bookmarks, expand bookmarks, PDF bookmarks, Aspose.PDF for .NET, OutlineCollection, OutlineItemCollection, child bookmarks",
    "wordcount": "1050",
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
    "url": "/net/get-update-and-expand-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-update-and-expand-bookmark/"
    },
    "dateModified": "2024-11-25",
    "description": "Este artículo describe cómo usar marcadores en un archivo PDF con nuestra biblioteca Aspose.PDF for .NET."
}
</script>

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

## Obtener Marcadores

La colección [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) del objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) contiene todos los marcadores de un archivo PDF. Este artículo explica cómo obtener marcadores de un archivo PDF y cómo saber en qué página se encuentra un marcador en particular.

Para obtener los marcadores, recorre la colección [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) y obtén cada marcador en la OutlineItemCollection. La OutlineItemCollection proporciona acceso a todos los atributos del marcador. El siguiente fragmento de código te muestra cómo obtener marcadores del archivo PDF.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetBookmarks.pdf"))
    {
        // Loop through all the bookmarks
        foreach (var outlineItem in document.Outlines)
        {
            Console.WriteLine(outlineItem.Title);
            Console.WriteLine(outlineItem.Italic);
            Console.WriteLine(outlineItem.Bold);
            Console.WriteLine(outlineItem.Color);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "GetBookmarks.pdf");

    // Loop through all the bookmarks
    foreach (var outlineItem in document.Outlines)
    {
        Console.WriteLine(outlineItem.Title);
        Console.WriteLine(outlineItem.Italic);
        Console.WriteLine(outlineItem.Bold);
        Console.WriteLine(outlineItem.Color);
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Obtener el Número de Página de un Marcador

Una vez que has añadido un marcador, puedes averiguar en qué página se encuentra obteniendo el número de página de destino asociado con el objeto Bookmark.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetBookmarkPageNumber()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Create PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "GetBookmarks.pdf");

        // Extract bookmarks
        Aspose.Pdf.Facades.Bookmarks bookmarks = bookmarkEditor.ExtractBookmarks();

        foreach (var bookmark in bookmarks)
        {
            string strLevelSeparator = string.Empty;

            for (int i = 1; i < bookmark.Level; i++)
            {
                strLevelSeparator += "----";
            }

            Console.WriteLine("{0}Title: {1}", strLevelSeparator, bookmark.Title);
            Console.WriteLine("{0}Page Number: {1}", strLevelSeparator, bookmark.PageNumber);
            Console.WriteLine("{0}Page Action: {1}", strLevelSeparator, bookmark.Action);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetBookmarkPageNumber()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Create PdfBookmarkEditor
    using var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor();

    // Bind PDF document
    bookmarkEditor.BindPdf(dataDir + "GetBookmarks.pdf");

    // Extract bookmarks
    Aspose.Pdf.Facades.Bookmarks bookmarks = bookmarkEditor.ExtractBookmarks();

    foreach (var bookmark in bookmarks)
    {
        string strLevelSeparator = string.Empty;

        for (int i = 1; i < bookmark.Level; i++)
        {
            strLevelSeparator += "----";
        }

        Console.WriteLine("{0}Title: {1}", strLevelSeparator, bookmark.Title);
        Console.WriteLine("{0}Page Number: {1}", strLevelSeparator, bookmark.PageNumber);
        Console.WriteLine("{0}Page Action: {1}", strLevelSeparator, bookmark.Action);
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Obtener Marcadores Hijos de un Documento PDF

Los marcadores pueden organizarse en una estructura jerárquica, con padres e hijos. Para obtener todos los marcadores, recorre las colecciones Outlines del objeto Document. Sin embargo, para obtener también los marcadores hijos, recorre todos los marcadores en cada objeto [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) obtenido en el primer bucle. Los siguientes fragmentos de código muestran cómo obtener marcadores hijos de un documento PDF.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetChildBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetChildBookmarks.pdf"))
    {
        // Loop through all the bookmarks
        foreach (var outlineItem in document.Outlines)
        {
            Console.WriteLine(outlineItem.Title);
            Console.WriteLine(outlineItem.Italic);
            Console.WriteLine(outlineItem.Bold);
            Console.WriteLine(outlineItem.Color);

            if (outlineItem.Count > 0)
            {
                Console.WriteLine("Child Bookmarks");

                // There are child bookmarks then loop through that as well
                foreach (var childOutline in outlineItem)
                {
                    Console.WriteLine(childOutline.Title);
                    Console.WriteLine(childOutline.Italic);
                    Console.WriteLine(childOutline.Bold);
                    Console.WriteLine(childOutline.Color);
                }
            }
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetChildBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "GetChildBookmarks.pdf");

    // Loop through all the bookmarks
    foreach (var outlineItem in document.Outlines)
    {
        Console.WriteLine(outlineItem.Title);
        Console.WriteLine(outlineItem.Italic);
        Console.WriteLine(outlineItem.Bold);
        Console.WriteLine(outlineItem.Color);

        if (outlineItem.Count > 0)
        {
            Console.WriteLine("Child Bookmarks");

            // There are child bookmarks then loop through that as well
            foreach (var childOutline in outlineItem)
            {
                Console.WriteLine(childOutline.Title);
                Console.WriteLine(childOutline.Italic);
                Console.WriteLine(childOutline.Bold);
                Console.WriteLine(childOutline.Color);
            }
        }
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Actualizar Marcadores en un Documento PDF

Para actualizar un marcador en un archivo PDF, primero, obtén el marcador particular de la colección OutlineColletion del objeto Document especificando el índice del marcador. Una vez que hayas recuperado el marcador en el objeto [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection), puedes actualizar sus propiedades y luego guardar el archivo PDF actualizado utilizando el método Save. Los siguientes fragmentos de código muestran cómo actualizar marcadores en un documento PDF.

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateBookmarks.pdf"))
    {
        // Get a bookmark object
        var pdfOutline = document.Outlines[1];
        pdfOutline.Title = "Updated Outline";
        pdfOutline.Italic = true;
        pdfOutline.Bold = true;

        // Save PDF document
        document.Save(dataDir + "UpdateBookmarks_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "UpdateBookmarks.pdf");

    // Get a bookmark object
    var pdfOutline = document.Outlines[1];
    pdfOutline.Title = "Updated Outline";
    pdfOutline.Italic = true;
    pdfOutline.Bold = true;

    // Save PDF document
    document.Save(dataDir + "UpdateBookmarks_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Actualizar Marcadores Hijos en un Documento PDF

Para actualizar un marcador hijo:

1. Recupera el marcador hijo que deseas actualizar del archivo PDF obteniendo primero el marcador padre y luego el marcador hijo utilizando los valores de índice apropiados.
1. Guarda el archivo PDF actualizado utilizando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/1).

{{% alert color="primary" %}}

Obtén un marcador de la colección OutlineCollection del objeto Document especificando el índice del marcador, y luego obtén el marcador hijo especificando el índice de este marcador padre.

{{% /alert %}}

El siguiente fragmento de código te muestra cómo actualizar marcadores hijos en un documento PDF.

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateChildBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateChildBookmarks.pdf"))
    {
        // Get a bookmark object
        var pdfOutline = document.Outlines[1];

        // Get child bookmark object
        Aspose.Pdf.OutlineItemCollection childOutline = pdfOutline[1];
        childOutline.Title = "Updated Outline";
        childOutline.Italic = true;
        childOutline.Bold = true;

        // Save PDF document
        document.Save(dataDir + "UpdateChildBookmarks_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateChildBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "UpdateChildBookmarks.pdf");

    // Get a bookmark object
    var pdfOutline = document.Outlines[1];

    // Get child bookmark object
    Aspose.Pdf.OutlineItemCollection childOutline = pdfOutline[1];
    childOutline.Title = "Updated Outline";
    childOutline.Italic = true;
    childOutline.Bold = true;

    // Save PDF document
    document.Save(dataDir + "UpdateChildBookmarks_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Marcadores Expandido al Ver el Documento

Los marcadores se mantienen en la colección [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) del objeto Document, que a su vez está en la colección [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection). Sin embargo, podemos tener el requisito de que todos los marcadores estén expandidos al ver el archivo PDF.

Para cumplir con este requisito, podemos establecer el estado de apertura para cada elemento de contorno/marcador como Abierto. El siguiente fragmento de código te muestra cómo establecer el estado de apertura para cada marcador como expandido en un documento PDF.

{{< tabs tabID="6" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExpandBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Set page view mode i.e. show thumbnails, full-screen, show attachment panel
        document.PageMode = Aspose.Pdf.PageMode.UseOutlines;

        // Traverse through each Outline item in outlines collection of PDF file
        foreach (var item in document.Outlines)
        {
            // Set open status for outline item
            item.Open = true;
        }

        // Save PDF document
        document.Save(dataDir + "ExpandBookmarks_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExpandBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Set page view mode i.e. show thumbnails, full-screen, show attachment panel
    document.PageMode = Aspose.Pdf.PageMode.UseOutlines;

    // Traverse through each Outline item in outlines collection of PDF file
    foreach (var item in document.Outlines)
    {
        // Set open status for outline item
        item.Open = true;
    }

    // Save PDF document
    document.Save(dataDir + "ExpandBookmarks_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>