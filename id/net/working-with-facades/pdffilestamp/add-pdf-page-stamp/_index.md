---
title: Tambahkan Stempel Halaman PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/add-pdf-page-stamp/
description: Temukan cara menambahkan stempel ke halaman PDF di .NET, termasuk teks dan gambar, untuk watermarking atau branding menggunakan Aspose.PDF.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add PDF Page Stamp",
    "alternativeHeadline": "Enhance PDFs with Custom Stamps and Page Numbers",
    "abstract": "Memperkenalkan fitur Stempel Halaman PDF yang memungkinkan pengguna untuk dengan mudah menambahkan stempel kustom pada semua atau halaman tertentu dari dokumen PDF menggunakan kelas PdfFileStamp. Fungsionalitas ini meningkatkan personalisasi dokumen dengan memungkinkan berbagai atribut seperti rotasi, latar belakang, dan gaya penomoran kustom untuk stempel halaman, menjadikan file PDF Anda tidak hanya unik tetapi juga terlihat profesional.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1309",
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
    "url": "/net/add-pdf-page-stamp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-pdf-page-stamp/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF tidak hanya dapat melakukan tugas sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Tambahkan Stempel Halaman PDF di Semua Halaman dalam File PDF

Kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) memungkinkan Anda untuk menambahkan stempel halaman PDF di semua halaman file PDF. Untuk menambahkan stempel halaman PDF, Anda pertama-tama perlu membuat objek dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) dan [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Anda juga perlu membuat stempel halaman PDF menggunakan metode [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) dari kelas [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Anda dapat mengatur atribut lain seperti asal, rotasi, latar belakang, dll. menggunakan objek [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) juga. Kemudian Anda dapat menambahkan stempel ke dalam file PDF menggunakan metode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Terakhir, simpan file PDF keluaran menggunakan metode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Potongan kode berikut menunjukkan kepada Anda cara menambahkan stempel halaman PDF di semua halaman dalam file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageStampOnAllPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "SourcePDF.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        // Bind PDF document
        stamp.BindPdf(dataDir + "AddPageStampOnAllPages.pdf", 1);
        stamp.SetOrigin(20, 20);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "PageStampOnAllPages_out.pdf");
    }
}
```

## Tambahkan Stempel Halaman PDF di Halaman Tertentu dalam File PDF

Kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) memungkinkan Anda untuk menambahkan stempel halaman PDF di halaman tertentu dari file PDF. Untuk menambahkan stempel halaman PDF, Anda pertama-tama perlu membuat objek dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) dan [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Anda juga perlu membuat stempel halaman PDF menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) dari kelas [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Anda dapat mengatur atribut lain seperti asal, rotasi, latar belakang, dll. menggunakan objek [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) juga. Karena Anda ingin menambahkan stempel halaman PDF di halaman tertentu dari file PDF, Anda juga perlu mengatur properti [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) dari kelas [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Properti ini memerlukan array integer yang berisi nomor halaman di mana Anda ingin menambahkan stempel. Kemudian Anda dapat menambahkan stempel ke dalam file PDF menggunakan metode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Terakhir, simpan file PDF keluaran menggunakan metode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Potongan kode berikut menunjukkan kepada Anda cara menambahkan stempel halaman PDF di halaman tertentu dalam file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageStampOnCertainPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "SourcePDF.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        // Bind PDF document
        stamp.BindPdf(dataDir + "PageStampOnCertainPages.pdf", 1);
        stamp.SetOrigin(20, 20);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;
        stamp.Pages = new[] { 1, 3 };  // Apply stamp to specific pages (1 and 3)

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "PageStampOnCertainPages_out.pdf");
    }
}
```

## Tambahkan Nomor Halaman dalam File PDF

Kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) memungkinkan Anda untuk menambahkan nomor halaman dalam file PDF. Untuk menambahkan nomor halaman, Anda pertama-tama perlu membuat objek dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Jika Anda ingin menampilkan nomor halaman seperti “Halaman X dari N” di mana X adalah nomor halaman saat ini dan N adalah total jumlah halaman dalam file PDF, maka Anda pertama-tama perlu mendapatkan jumlah halaman menggunakan properti [NumberOfpages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/numberofpages) dari kelas [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo). Untuk mendapatkan nomor halaman saat ini, Anda dapat menggunakan tanda **#** di teks Anda di mana saja Anda suka. Anda dapat memformat teks nomor halaman menggunakan kelas [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). Jika Anda ingin memulai penomoran halaman dari nomor tertentu, maka Anda dapat mengatur properti [StartingNumber](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/properties/startingnumber). Setelah Anda siap untuk menambahkan nomor halaman dalam file, Anda perlu memanggil metode [AddPageNumber](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addpagenumber/methods/7) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Terakhir, simpan file PDF keluaran menggunakan metode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Potongan kode berikut menunjukkan kepada Anda cara menambahkan nomor halaman dalam file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageNumberInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "StampPDF.pdf");

        // Get total number of pages
        int totalPages = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "StampPDF.pdf").NumberOfPages;

        // Create formatted text for page number
        var formattedText = new Aspose.Pdf.Facades.FormattedText($"Page # of {totalPages}",
            System.Drawing.Color.AntiqueWhite,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.TimesBoldItalic,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            false, 12);

        // Set starting number for first page; you might want to start from 2 or more
        fileStamp.StartingNumber = 1;
        // Add page number in upper right corner
        fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

        // Save PDF document
        fileStamp.Save(dataDir + "AddPageNumber_out.pdf");
    }
}

// Add PDF Page Numbers
public enum PageNumPosition
{
    PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
}
```

### Gaya Penomoran Kustom

Kelas PdfFileStamp menawarkan fitur untuk menambahkan informasi Nomor Halaman sebagai objek stempel di dalam dokumen PDF. Sebelum rilis ini, kelas hanya mendukung gaya penomoran halaman 1,2,3,4. Namun, ada permintaan dari beberapa pelanggan untuk menggunakan gaya penomoran kustom saat menempatkan stempel nomor halaman di dalam dokumen PDF. Untuk memenuhi permintaan ini, properti [NumberingStyle](https://reference.aspose.com/pdf/net/aspose.pdf/numberingstyle) telah diperkenalkan, yang menerima nilai dari enumerasi [NumberingStyle](https://reference.aspose.com/pdf/net/aspose.pdf/numberingstyle). Nilai yang ditentukan di bawah ini adalah nilai yang ditawarkan dalam enumerasi ini.

- HurufKecil.
- HurufBesar.
- AngkaArab.
- AngkaRomawiKecil.
- AngkaRomawiBesar.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddCustomPageNumberInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "StampPDF.pdf");

        // Get total number of pages
        int totalPages = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "StampPDF.pdf").NumberOfPages;

        // Create formatted text for page number
        var formattedText = new Aspose.Pdf.Facades.FormattedText($"Page # of {totalPages}",
            System.Drawing.Color.AntiqueWhite,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.TimesBoldItalic,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            false, 12);

        // Specify numbering style as Numerals Roman UpperCase
        fileStamp.NumberingStyle = Aspose.Pdf.NumberingStyle.NumeralsRomanUppercase;

        // Set starting number for first page; you might want to start from 2 or more
        fileStamp.StartingNumber = 1;

        // Add page number in upper right corner
        fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

        // Save PDF document
        fileStamp.Save(dataDir + "AddCustomPageNumber_out.pdf");
    }
}

// Add PDF Page Numbers
public enum PageNumPosition
{
    PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
}
```