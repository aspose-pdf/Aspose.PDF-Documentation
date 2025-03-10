---
title: Mettre à jour, supprimer et obtenir des signets
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /fr/net/update-delete-and-get-bookmarks/
description: Cette section explique comment mettre à jour, supprimer et obtenir des signets avec Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Update, Delete and Get Bookmarks",
    "alternativeHeadline": "Manage Bookmarks: Update, Delete, and Extract Functions",
    "abstract": "La fonctionnalité de gestion des signets dans les fichiers PDF utilisant Aspose.PDF Facades permet aux utilisateurs de mettre facilement à jour, supprimer et récupérer des signets. Avec des méthodes telles que ModifyBookmarks, DeleteBookmarks et ExtractBookmarks, les utilisateurs peuvent manipuler efficacement les signets, améliorant ainsi la navigation et l'organisation des PDF pour une meilleure expérience utilisateur. Cette fonctionnalité rationalise la gestion des signets grâce à une mise en œuvre de code simple, garantissant un traitement efficace des documents PDF.",
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
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Mettre à jour un signet existant dans le fichier PDF

Pour mettre à jour un signet existant dans un fichier PDF, vous devez utiliser la méthode [ModifyBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks). Cette méthode prend deux arguments : le titre source (le titre du signet à modifier), le titre de destination (le titre à remplacer). Vous devez créer un objet de la classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) et lier le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Après cela, vous devez appeler la méthode [ModifyBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks), puis enregistrer le PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Le code suivant vous montre comment modifier un signet existant dans un fichier PDF.

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

## Supprimer tous les signets du fichier PDF

Vous pouvez supprimer tous les signets du fichier PDF en utilisant la méthode [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) sans aucun paramètre. Tout d'abord, vous devez créer un objet de la classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) et lier le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Après cela, vous devez appeler la méthode [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) puis enregistrer le fichier PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Le code suivant vous montre comment supprimer tous les signets du fichier PDF.

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

## Supprimer un signet particulier d'un fichier PDF

Pour supprimer un signet particulier, vous devez appeler la méthode [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) avec un paramètre de chaîne (titre). Le *titre* ici représente le signet à supprimer du PDF. Créez un objet de la classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) et liez le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Après cela, appelez la méthode [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) puis enregistrez le fichier PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Le code suivant vous montre comment supprimer un signet particulier d'un fichier PDF.

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

## Obtenir des signets à partir des facades de documents PDF

La classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) fournit la fonctionnalité de manipulation des signets dans un fichier PDF existant. Elle offre diverses propriétés pour obtenir/définir des informations concernant les signets. Le code suivant montre comment obtenir des informations relatives à chaque signet dans le fichier PDF.

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

## Extraire des signets d'un fichier PDF existant

La méthode [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) vous permet d'extraire des signets d'un fichier PDF. Pour extraire les signets, vous devez créer un objet [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) et lier le fichier PDF en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Après cela, vous devez appeler la méthode [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3). La méthode [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) retourne un objet [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks/methods/index). Vous pouvez ensuite parcourir ces signets et obtenir des objets [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) individuels. Enfin, vous pouvez exporter les signets vers un fichier XML en utilisant la méthode [ExportBookmarksToXML](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/exportbookmarkstoxml). Le code suivant vous montre comment exporter des signets vers un fichier XML.

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