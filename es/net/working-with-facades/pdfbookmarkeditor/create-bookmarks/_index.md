---
title: Crear Marcadores
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/create-bookmarks/
description: Esta sección explica cómo crear marcadores en su archivo PDF con Aspose.PDF Facades utilizando la clase PdfBookmarkEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create Bookmarks",
    "alternativeHeadline": "Effortlessly Manage PDF Bookmarks with PdfBookmarkEditor",
    "abstract": "Presentamos la funcionalidad de marcadores en Aspose.PDF for .NET, diseñada para mejorar la navegación en PDF al permitir a los usuarios crear marcadores para páginas completas, páginas específicas o rangos de páginas con propiedades personalizables. Esta característica permite una organización fluida de los documentos PDF, facilitando el acceso y la gestión efectiva del contenido. Ya sea que necesite agregar marcadores simples o marcadores secundarios intrincados, la clase Aspose.PDF PdfBookmarkEditor proporciona las herramientas para elevar su experiencia PDF",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1124",
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
    "url": "/net/create-bookmarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-bookmarks/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulte la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Crear Marcadores de Todas las Páginas

Para crear marcadores de todas las páginas, necesita usar el método [CreateBookmarks](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) sin ningún parámetro. La clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfbookmarkeditor) le permite crear marcadores de todas las páginas de un archivo PDF. Primero, necesita crear un objeto de la clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfbookmarkeditor) y vincular el PDF de entrada utilizando el método [BindPdf](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.facade/bindpdf/methods/3). Luego, debe llamar al método [CreateBookmarks](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) y guardar el archivo PDF de salida utilizando el método [Save](https://reference.aspose.com/pdf/es/net/aspose.pdf/document/methods/save). El siguiente fragmento de código le muestra cómo crear marcadores.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateBookmarksOfAllPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "CreateBookmarksAll.pdf");
        // Create bookmark of all pages
        bookmarkEditor.CreateBookmarks();
        // Save PDF document
        bookmarkEditor.Save(dataDir + "CreateBookmarksOfAllPages_out.pdf");
    }
} 
```

## Crear Marcadores de Todas las Páginas con Propiedades

La clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfbookmarkeditor) le permite crear marcadores de todas las páginas de un archivo PDF y especificar las propiedades (Color, Negrita, Cursiva). Puede hacerlo con la ayuda del método [CreateBookmarks](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2). Primero, necesita crear un objeto de la clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfbookmarkeditor) y vincular el PDF de entrada utilizando el método [BindPdf](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.facade/bindpdf/methods/3). Luego, debe llamar al método [CreateBookmarks](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) y guardar el archivo PDF de salida utilizando el método [Save](https://reference.aspose.com/pdf/es/net/aspose.pdf/document/methods/save). El siguiente fragmento de código le muestra cómo crear marcadores de todas las páginas con propiedades.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateBookmarksOfAllPagesWithProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "CreateBookmarks-PagesProperties.pdf");
        // Create bookmark of all pages
        bookmarkEditor.CreateBookmarks(System.Drawing.Color.Green, true, true);
        // Save PDF document
        bookmarkEditor.Save(dataDir + "CreateBookmarks-PagesProperties_out.pdf");
    }
}
```

## Crear Marcador de una Página Particular

Puede crear un marcador de una página particular en un archivo PDF existente utilizando el método [CreateBookmarkOfPage](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1). Este método toma dos argumentos: el título del marcador y el número de página. Primero, necesita crear un objeto de la clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfbookmarkeditor) y vincular el archivo PDF de entrada utilizando el método [BindPdf](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.facade/bindpdf/methods/3). Luego, debe llamar al método [CreateBookmarkOfPage](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) y guardar el archivo PDF de salida utilizando el método [Save](https://reference.aspose.com/pdf/es/net/aspose.pdf/document/methods/save). El siguiente fragmento de código le muestra cómo crear un marcador de una página particular.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateBookmarkOfAParticularPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "CreateBookmark-Page.pdf");
        // Create bookmark of a particular page
        bookmarkEditor.CreateBookmarkOfPage("Bookmark Name", 2);
        // Save PDF document
        bookmarkEditor.Save(dataDir + "CreateBookmark-Page_out.pdf");
    }
}
```

## Crear Marcadores de un Rango de Páginas

La clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfbookmarkeditor) le permite crear marcadores de un rango de páginas. Puede usar el método [CreateBookmarkOfPage](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) con dos parámetros: la lista de marcadores (la lista de títulos de marcadores) y la lista de páginas (la lista de páginas a marcar). Primero, necesita crear un objeto de la clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfbookmarkeditor) y vincular el archivo PDF de entrada utilizando el método [BindPdf](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.facade/bindpdf/methods/3). Luego, debe llamar al método [CreateBookmarkOfPage](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) y guardar el PDF de salida utilizando el método [Save](https://reference.aspose.com/pdf/es/net/aspose.pdf/document/methods/save). El siguiente fragmento de código le muestra cómo crear marcadores de un rango de páginas.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateBookmarksOfARangeOfPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "CreateBookmark-Page.pdf");
        // Bookmark name list
        string[] bookmarkList = { "First" };
        // Page list
        int[] pageList = { 1 };
        // Create bookmark of a range of pages
        bookmarkEditor.CreateBookmarkOfPage(bookmarkList, pageList);
        // Save PDF document
        bookmarkEditor.Save(dataDir + "CreateBookmarkPageRange_out.pdf");
    }
}
```

## Agregar Marcador en un Archivo PDF Existente

Puede agregar un marcador en un archivo PDF existente utilizando la clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfbookmarkeditor). Para crear el marcador, necesita crear un objeto [Bookmark](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/bookmark) y establecer los atributos requeridos del marcador. Después de eso, necesita pasar el objeto [Bookmark](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/bookmark) al método [CreateBookmarks](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) de la clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfbookmarkeditor). Finalmente, necesita guardar el archivo PDF actualizado utilizando el método [Save](https://reference.aspose.com/pdf/es/net/aspose.pdf/document/methods/save). El siguiente fragmento de código le muestra cómo agregar el marcador en un archivo PDF existente.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBookmarkInAnExistingPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();
    // Create bookmark
    var bookmark = new Aspose.Pdf.Facades.Bookmark();
    bookmark.PageNumber = 1;
    bookmark.Title = "New Bookmark";
    // Create PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "AddBookmark.pdf");
        // Create bookmarks
        bookmarkEditor.CreateBookmarks(bookmark);
        // Save PDF document
        bookmarkEditor.Save(dataDir + "AddBookmark_out.pdf");
    }
}
```

## Agregar Marcador Secundario en un Archivo PDF Existente

Puede agregar marcadores secundarios en un archivo PDF existente utilizando la clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfbookmarkeditor). Para agregar marcadores secundarios, necesita crear objetos [Bookmark](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/bookmark). Puede agregar objetos individuales [Bookmark](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/bookmark) en el objeto [Bookmarks](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/bookmarks). También necesita crear un objeto [Bookmark](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/bookmark) y establecer su propiedad [ChildItem](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/bookmark/properties/childitem) al objeto [Bookmarks](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/bookmarks). Luego, necesita pasar este objeto [Bookmark](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/bookmark) con [ChildItem](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/bookmark/properties/childitem) al método [CreateBookmarks](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2). Finalmente, necesita guardar el PDF actualizado utilizando el método [Save](https://reference.aspose.com/pdf/es/net/aspose.pdf/document/methods/save) de la clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfbookmarkeditor). El siguiente fragmento de código le muestra cómo agregar marcadores secundarios en un archivo PDF existente.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddChildBookmarkInAnExistingPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();
    // Create bookmarks
    var bookmarks = new Aspose.Pdf.Facades.Bookmarks();
    var childBookmark1 = new Aspose.Pdf.Facades.Bookmark();
    childBookmark1.PageNumber = 1;
    childBookmark1.Title = "First Child";
    var childBookmark2 = new Aspose.Pdf.Facades.Bookmark();
    childBookmark2.PageNumber = 2;
    childBookmark2.Title = "Second Child";
    bookmarks.Add(childBookmark1);
    bookmarks.Add(childBookmark2);
    var bookmark = new Aspose.Pdf.Facades.Bookmark();
    bookmark.Action = "GoTo";
    bookmark.PageNumber = 1;
    bookmark.Title = "Parent";
    bookmark.ChildItems = bookmarks;
    // Create PdfBookmarkEditor class
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "AddChildBookmark.pdf");
        // Create bookmarks
        bookmarkEditor.CreateBookmarks(bookmark);
        // Save PDF document
        bookmarkEditor.Save(dataDir + "AddChildBookmark_out.pdf");
    }
}
```