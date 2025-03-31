---
title: Buat Bookmark
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/create-bookmarks/
description: Bagian ini menjelaskan cara membuat bookmark pada file PDF Anda dengan Aspose.PDF Facades menggunakan Kelas PdfBookmarkEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create Bookmarks",
    "alternativeHeadline": "Effortlessly Manage PDF Bookmarks with PdfBookmarkEditor",
    "abstract": "Memperkenalkan fungsionalitas bookmark di Aspose.PDF for .NET, dirancang untuk meningkatkan navigasi PDF dengan memungkinkan pengguna untuk membuat bookmark untuk seluruh halaman, halaman tertentu, atau rentang halaman dengan properti yang dapat disesuaikan. Fitur ini memungkinkan organisasi dokumen PDF yang mulus, membuatnya lebih mudah untuk mengakses dan mengelola konten secara efektif. Apakah Anda perlu menambahkan bookmark sederhana atau bookmark anak yang rumit, kelas Aspose.PDF PdfBookmarkEditor menyediakan alat untuk meningkatkan pengalaman PDF Anda",
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
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Buat Bookmark dari Semua Halaman

Untuk membuat bookmark dari semua halaman, Anda perlu menggunakan metode [CreateBookmarks](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) tanpa parameter apapun. Kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfbookmarkeditor) memungkinkan Anda untuk membuat bookmark dari semua halaman file PDF. Pertama, Anda perlu membuat objek dari kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfbookmarkeditor) dan mengikat PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.facade/bindpdf/methods/3). Kemudian, Anda harus memanggil metode [CreateBookmarks](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) dan menyimpan file PDF output menggunakan metode [Save](https://reference.aspose.com/pdf/id/net/aspose.pdf/document/methods/save). Potongan kode berikut menunjukkan cara membuat Bookmark.

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

## Buat Bookmark dari Semua Halaman dengan Properti

Kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfbookmarkeditor) memungkinkan Anda untuk membuat bookmark dari semua halaman file PDF dan menentukan properti (Warna, Tebal, Miring). Anda dapat melakukan itu dengan bantuan metode [CreateBookmarks](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2). Pertama, Anda perlu membuat objek dari kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfbookmarkeditor) dan mengikat PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.facade/bindpdf/methods/3). Kemudian, Anda harus memanggil metode [CreateBookmarks](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) dan menyimpan file PDF output menggunakan metode [Save](https://reference.aspose.com/pdf/id/net/aspose.pdf/document/methods/save). Potongan kode berikut menunjukkan cara membuat bookmark dari semua halaman dengan properti.

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

## Buat Bookmark dari Halaman Tertentu

Anda dapat membuat bookmark dari halaman tertentu dalam file PDF yang ada menggunakan metode [CreateBookmarkOfPage](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1). Metode ini mengambil dua argumen: judul bookmark dan nomor halaman. Pertama, Anda perlu membuat objek dari kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfbookmarkeditor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.facade/bindpdf/methods/3). Kemudian, Anda harus memanggil metode [CreateBookmarkOfPage](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) dan menyimpan file PDF output menggunakan metode [Save](https://reference.aspose.com/pdf/id/net/aspose.pdf/document/methods/save). Potongan kode berikut menunjukkan cara membuat bookmark dari halaman tertentu.

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

## Buat Bookmark dari Rentang Halaman

Kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfbookmarkeditor) memungkinkan Anda untuk membuat bookmark dari rentang halaman. Anda dapat menggunakan metode [CreateBookmarkOfPage](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) dengan dua parameter: daftar bookmark (daftar judul bookmark) dan daftar halaman (daftar halaman untuk dibookmark). Pertama, Anda perlu membuat objek dari kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfbookmarkeditor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.facade/bindpdf/methods/3). Kemudian, Anda harus memanggil metode [CreateBookmarkOfPage](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) dan menyimpan PDF output menggunakan metode [Save](https://reference.aspose.com/pdf/id/net/aspose.pdf/document/methods/save). Potongan kode berikut menunjukkan cara membuat bookmark dari rentang halaman.

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

## Tambahkan Bookmark di File PDF yang Ada

Anda dapat menambahkan bookmark di file PDF yang ada menggunakan kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfbookmarkeditor). Untuk membuat bookmark, Anda perlu membuat objek [Bookmark](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/bookmark) dan mengatur atribut yang diperlukan dari bookmark. Setelah itu, Anda perlu mengirimkan objek [Bookmark](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/bookmark) ke metode [CreateBookmarks](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) dari kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfbookmarkeditor). Akhirnya, Anda perlu menyimpan file PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/id/net/aspose.pdf/document/methods/save). Potongan kode berikut menunjukkan cara menambahkan bookmark di file PDF yang ada.

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

## Tambahkan Bookmark Anak di File PDF yang Ada

Anda dapat menambahkan bookmark anak di file PDF yang ada menggunakan kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfbookmarkeditor). Untuk menambahkan bookmark anak, Anda perlu membuat objek [Bookmark](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/bookmark). Anda dapat menambahkan objek [Bookmark](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/bookmark) individu ke dalam objek [Bookmarks](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/bookmarks). Anda juga perlu membuat objek [Bookmark](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/bookmark) dan mengatur propertinya [ChildItem](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/bookmark/properties/childitem) ke objek [Bookmarks](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/bookmarks). Anda kemudian perlu mengirimkan objek [Bookmark](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/bookmark) ini dengan [ChildItem](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/bookmark/properties/childitem) ke metode [CreateBookmarks](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2). Akhirnya, Anda perlu menyimpan PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/id/net/aspose.pdf/document/methods/save) dari kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfbookmarkeditor). Potongan kode berikut menunjukkan cara menambahkan bookmark anak di file PDF yang ada.

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