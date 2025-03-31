---
title: Memperbarui, Menghapus, dan Mendapatkan Bookmark
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /id/net/update-delete-and-get-bookmarks/
description: Bagian ini menjelaskan cara memperbarui, menghapus, dan mendapatkan Bookmark dengan Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Update, Delete and Get Bookmarks",
    "alternativeHeadline": "Manage Bookmarks: Update, Delete, and Extract Functions",
    "abstract": "Fitur untuk mengelola bookmark dalam file PDF menggunakan Aspose.PDF Facades memungkinkan pengguna untuk dengan mudah memperbarui, menghapus, dan mengambil bookmark. Dengan metode seperti ModifyBookmarks, DeleteBookmarks, dan ExtractBookmarks, pengguna dapat secara efektif memanipulasi bookmark, meningkatkan navigasi dan organisasi PDF untuk pengalaman pengguna yang lebih baik. Fungsionalitas ini menyederhanakan manajemen bookmark melalui implementasi kode yang sederhana, memastikan penanganan dokumen PDF yang efisien.",
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
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Memperbarui Bookmark yang Ada dalam File PDF

Untuk memperbarui bookmark yang ada dalam file PDF, Anda perlu menggunakan metode [ModifyBookmarks](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks). Metode ini mengambil dua argumen: judul sumber (judul bookmark yang akan dimodifikasi), judul tujuan (judul yang akan diganti). Anda perlu membuat objek dari kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfbookmarkeditor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.facade/bindpdf/methods/3). Setelah itu, Anda perlu memanggil metode [ModifyBookmarks](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks), dan kemudian menyimpan PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/id/net/aspose.pdf/document/methods/save). Potongan kode berikut menunjukkan cara memodifikasi bookmark yang ada dalam file PDF.

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

## Menghapus Semua Bookmark dari File PDF

Anda dapat menghapus semua bookmark dari file PDF menggunakan metode [DeleteBookmarks](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) tanpa parameter apa pun. Pertama-tama, Anda perlu membuat objek dari kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfbookmarkeditor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.facade/bindpdf/methods/3). Setelah itu, Anda perlu memanggil metode [DeleteBookmarks](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) dan kemudian menyimpan file PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/id/net/aspose.pdf/document/methods/save). Potongan kode berikut menunjukkan cara menghapus semua bookmark dari file PDF.

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

## Menghapus Bookmark Tertentu dari File PDF

Untuk menghapus bookmark tertentu, Anda perlu memanggil metode [DeleteBookmarks](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) dengan parameter string (judul). *judul* di sini mewakili bookmark yang akan dihapus dari PDF. Buat objek dari kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfbookmarkeditor) dan ikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.facade/bindpdf/methods/3). Setelah itu, panggil metode [DeleteBookmarks](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) dan kemudian simpan file PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/id/net/aspose.pdf/document/methods/save). Potongan kode berikut menunjukkan cara menghapus bookmark tertentu dari file PDF.

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

## Mendapatkan Bookmark dari Facades Dokumen PDF

Kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfbookmarkeditor) menyediakan fitur untuk memanipulasi Bookmark dalam file PDF yang ada. Ini menyediakan berbagai properti untuk mendapatkan/mengatur informasi terkait bookmark. Potongan kode berikut menunjukkan cara mendapatkan informasi terkait setiap bookmark dalam file PDF.

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

## Mengekstrak Bookmark dari File PDF yang Ada

Metode [ExtractBookmarks](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) memungkinkan Anda untuk mengekstrak bookmark dari file PDF. Untuk mengekstrak bookmark, Anda perlu membuat objek [PdfBookmarkEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfbookmarkeditor) dan mengikat file PDF menggunakan metode [BindPdf](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.facade/bindpdf/methods/3). Setelah itu, Anda perlu memanggil metode [ExtractBookmarks](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3). Metode [ExtractBookmarks](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) mengembalikan objek [Bookmarks](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/bookmarks/methods/index). Anda kemudian dapat melakukan loop melalui bookmark ini dan mendapatkan objek [Bookmark](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/bookmark) individu. Akhirnya, Anda dapat mengekspor bookmark ke file XML menggunakan metode [ExportBookmarksToXML](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfbookmarkeditor/exportbookmarkstoxml). Potongan kode berikut menunjukkan cara mengekspor bookmark ke file XML.

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