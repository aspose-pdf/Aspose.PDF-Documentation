---
title: Actualizar, Eliminar y Obtener Marcadores
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /es/net/update-delete-and-get-bookmarks/
description: Esta sección explica cómo actualizar, eliminar y obtener marcadores con Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Update, Delete and Get Bookmarks",
    "alternativeHeadline": "Manage Bookmarks: Update, Delete, and Extract Functions",
    "abstract": "La función para gestionar marcadores dentro de archivos PDF utilizando Aspose.PDF Facades permite a los usuarios actualizar, eliminar y recuperar marcadores fácilmente. Con métodos como ModifyBookmarks, DeleteBookmarks y ExtractBookmarks, los usuarios pueden manipular eficazmente los marcadores, mejorando la navegación y organización del PDF para una mejor experiencia del usuario. Esta funcionalidad simplifica la gestión de marcadores a través de una implementación de código sencilla, asegurando un manejo eficiente de los documentos PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "761",
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
    "url": "/net/update-delete-and-get-bookmarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/update-delete-and-get-bookmarks/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Actualizar un Marcador Existente en el Archivo PDF

Para actualizar un marcador existente en un archivo PDF, necesitas usar el método [ModifyBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks). Este método toma dos argumentos: título de origen (el título del marcador a modificar), título de destino (el título que se va a reemplazar). Necesitas crear un objeto de la clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) y vincular el archivo PDF de entrada usando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Después de eso, necesitas llamar al método [ModifyBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks) y luego guardar el PDF actualizado usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). El siguiente fragmento de código te muestra cómo modificar un marcador existente en un archivo PDF.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void UpdateExistingBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "UpdateBookmark.pdf");

        // Modify the existing bookmark, assigning a new title
        bookmarkEditor.ModifyBookmarks("New Bookmark", "New Title");

        // Save PDF document
        bookmarkEditor.Save(dataDir + "UpdateBookmark_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void UpdateExistingBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor();

    // Bind PDF document
    bookmarkEditor.BindPdf(dataDir + "UpdateBookmark.pdf");

    // Modify the existing bookmark, assigning a new title
    bookmarkEditor.ModifyBookmarks("New Bookmark", "New Title");

    // Save PDF document
    bookmarkEditor.Save(dataDir + "UpdateBookmark_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Eliminar Todos los Marcadores del Archivo PDF

Puedes eliminar todos los marcadores del archivo PDF usando el método [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) sin ningún parámetro. Primero que nada, necesitas crear un objeto de la clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) y vincular el archivo PDF de entrada usando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Después de eso, necesitas llamar al método [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) y luego guardar el archivo PDF actualizado usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). El siguiente fragmento de código te muestra cómo eliminar todos los marcadores del archivo PDF.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DeleteAllBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "DeleteAllBookmarks.pdf");

        // Delete all bookmarks in the document
        bookmarkEditor.DeleteBookmarks();

        // Save PDF document
        bookmarkEditor.Save(dataDir + "DeleteAllBookmarks_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DeleteAllBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor();

    // Bind PDF document
    bookmarkEditor.BindPdf(dataDir + "DeleteAllBookmarks.pdf");

    // Delete all bookmarks in the document
    bookmarkEditor.DeleteBookmarks();

    // Save PDF document
    bookmarkEditor.Save(dataDir + "DeleteAllBookmarks_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Eliminar un Marcador Particular de un Archivo PDF

Para eliminar un marcador particular, necesitas llamar al método [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) con el parámetro de cadena (título). El *título* aquí representa el marcador que se va a eliminar del PDF. Crea un objeto de la clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) y vincula el archivo PDF de entrada usando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Después de eso, llama al método [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) y luego guarda el archivo PDF actualizado usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). El siguiente fragmento de código te muestra cómo eliminar un marcador particular de un archivo PDF.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DeleteParticularBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "DeleteABookmark.pdf");

        // Delete a bookmark with the title "Page2"
        bookmarkEditor.DeleteBookmarks("Page2");

        // Save PDF document
        bookmarkEditor.Save(dataDir + "DeleteABookmark_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DeleteParticularBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor();

   // Bind PDF document
    bookmarkEditor.BindPdf(dataDir + "DeleteABookmark.pdf");

    // Delete a bookmark with the title "Page2"
    bookmarkEditor.DeleteBookmarks("Page2");

    // Save PDF document
    bookmarkEditor.Save(dataDir + "DeleteABookmark_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Obtener Marcadores del Facades del Documento PDF

La clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) proporciona la función para manipular marcadores en un archivo PDF existente. Proporciona varias propiedades para obtener/establecer información relacionada con los marcadores. El siguiente fragmento de código muestra cómo obtener información relacionada con cada marcador en el archivo PDF.

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void GetBookmarksFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "GetFromPDF.PDF");

        // Extract all bookmarks from the document
        Aspose.Pdf.Facades.Bookmarks bookmarks = bookmarkEditor.ExtractBookmarks();

        // Iterate through each bookmark and display information
        foreach (Aspose.Pdf.Facades.Bookmark bookmark in bookmarks)
        {
            // Get the title information of bookmark item
            Console.WriteLine("Title: {0}", bookmark.Title);

            // Get the destination page for bookmark
            Console.WriteLine("Page Number: {0}", bookmark.PageNumber);

            // Get the information related to associated action with bookmark
            Console.WriteLine("Bookmark Action: " + bookmark.Action);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void GetBookmarksFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor();

    // Bind PDF document
    bookmarkEditor.BindPdf(dataDir + "GetFromPDF.PDF");

    // Extract all bookmarks from the document
    Aspose.Pdf.Facades.Bookmarks bookmarks = bookmarkEditor.ExtractBookmarks();

    // Iterate through each bookmark and display information
    foreach (Aspose.Pdf.Facades.Bookmark bookmark in bookmarks)
    {
        // Get the title information of bookmark item
        Console.WriteLine("Title: {0}", bookmark.Title);

        // Get the destination page for bookmark
        Console.WriteLine("Page Number: {0}", bookmark.PageNumber);

        // Get the information related to associated action with bookmark
        Console.WriteLine("Bookmark Action: " + bookmark.Action);
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Extraer Marcadores de un Archivo PDF Existente

El método [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) te permite extraer marcadores de un archivo PDF. Para extraer los marcadores, necesitas crear un objeto [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) y vincular el archivo PDF usando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Después de eso, necesitas llamar al método [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3). El método [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) devuelve un objeto [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks/methods/index). Luego puedes recorrer estos marcadores y obtener objetos individuales [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) . Finalmente, puedes exportar los marcadores a un archivo XML usando el método [ExportBookmarksToXML](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/exportbookmarkstoxml). El siguiente fragmento de código te muestra cómo exportar marcadores a un archivo XML.

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ExtractBookmarksFromPDFFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "ExtractBookmarks.pdf");

        // Extract bookmarks from the document
        Aspose.Pdf.Facades.Bookmarks bookmarks = bookmarkEditor.ExtractBookmarks();

        // Iterate through each extracted bookmark
        foreach (Aspose.Pdf.Facades.Bookmark bookmark in bookmarks)
        {
            // Get the title information of bookmark item
            Console.WriteLine("Title: {0}", bookmark.Title);

            // Get the destination page for bookmark
            Console.WriteLine("Page Number: {0}", bookmark.PageNumber);
        }

        // Export bookmarks to an XML file
        bookmarkEditor.ExportBookmarksToXML(dataDir + "bookmarks.xml");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ExtractBookmarksFromPDFFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor();

    // Bind PDF document
    bookmarkEditor.BindPdf(dataDir + "ExtractBookmarks.pdf");

    // Extract bookmarks from the document
    Aspose.Pdf.Facades.Bookmarks bookmarks = bookmarkEditor.ExtractBookmarks();

    // Iterate through each extracted bookmark
    foreach (Aspose.Pdf.Facades.Bookmark bookmark in bookmarks)
    {
        // Get the title information of bookmark item
        Console.WriteLine("Title: {0}", bookmark.Title);

        // Get the destination page for bookmark
        Console.WriteLine("Page Number: {0}", bookmark.PageNumber);
    }

    // Export bookmarks to an XML file
    bookmarkEditor.ExportBookmarksToXML(dataDir + "bookmarks.xml");
}
```
{{< /tab >}}
{{< /tabs >}}