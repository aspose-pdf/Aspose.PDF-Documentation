---
title: Tambahkan Stempel Teks dan Gambar
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /id/net/add-text-and-image-stamp/
description: Bagian ini menjelaskan cara menambahkan Stempel Teks dan Gambar dengan Aspose.PDF Facades menggunakan Kelas PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Text and Image Stamp",
    "alternativeHeadline": "Add Custom Text and Image Stamps in PDFs",
    "abstract": "Fitur Tambahkan Stempel Teks dan Gambar di Aspose.PDF for .NET memungkinkan pengguna untuk menerapkan stempel teks dan gambar yang disesuaikan secara mulus di semua atau halaman tertentu dari dokumen PDF. Fungsionalitas ini meningkatkan personalisasi dokumen, memungkinkan kontrol yang lebih rinci atas atribut stempel seperti posisi, rotasi, dan kualitas, yang pada akhirnya meningkatkan presentasi dan branding file PDF Anda.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1435",
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
    "url": "/net/add-text-and-image-stamp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-text-and-image-stamp/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Tambahkan Stempel Teks di Semua Halaman dalam File PDF

Kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) memungkinkan Anda untuk menambahkan stempel teks di semua halaman file PDF. Untuk menambahkan stempel teks, Anda pertama-tama perlu membuat objek dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) dan [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Anda juga perlu membuat stempel teks menggunakan metode [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) dari kelas [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Anda dapat mengatur atribut lain seperti asal, rotasi, latar belakang, dll. menggunakan objek [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) juga. Kemudian Anda dapat menambahkan stempel ke file PDF menggunakan metode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Terakhir, simpan file PDF keluaran menggunakan metode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Potongan kode berikut menunjukkan cara menambahkan stempel teks di semua halaman dalam file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampOnAllPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Hello World!",
            System.Drawing.Color.Blue,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.Helvetica,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            true,
            14));

        stamp.SetOrigin(10, 400);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddTextStampOnAllPages_out.pdf");
    }
}
```

## Tambahkan Stempel Teks di Halaman Tertentu dalam File PDF

Kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) memungkinkan Anda untuk menambahkan stempel teks di halaman tertentu dari file PDF. Untuk menambahkan stempel teks, Anda pertama-tama perlu membuat objek dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) dan [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Anda juga perlu membuat stempel teks menggunakan metode [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) dari kelas [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Anda dapat mengatur atribut lain seperti asal, rotasi, latar belakang, dll. menggunakan objek [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) juga. Karena Anda ingin menambahkan stempel teks di halaman tertentu dari file PDF, Anda juga perlu mengatur properti [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) dari kelas [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Properti ini memerlukan array integer yang berisi nomor halaman di mana Anda ingin menambahkan stempel. Kemudian Anda dapat menambahkan stempel ke file PDF menggunakan metode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Terakhir, simpan file PDF keluaran menggunakan metode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Potongan kode berikut menunjukkan cara menambahkan stempel teks di halaman tertentu dalam file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampOnParticularPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Hello World!",
            System.Drawing.Color.Blue,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.Helvetica,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            true,
            14));
        stamp.SetOrigin(10, 400);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Set particular pages (page 2)
        stamp.Pages = new[] { 2 };

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddTextStampOnParticularPages_out.pdf");
    }
}
```

## Tambahkan Stempel Gambar di Semua Halaman dalam File PDF

Kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) memungkinkan Anda untuk menambahkan stempel gambar di semua halaman file PDF. Untuk menambahkan stempel gambar, Anda pertama-tama perlu membuat objek dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) dan [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Anda juga perlu membuat stempel gambar menggunakan metode [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) dari kelas [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Anda dapat mengatur atribut lain seperti asal, rotasi, latar belakang, dll. menggunakan objek [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) juga. Kemudian Anda dapat menambahkan stempel ke file PDF menggunakan metode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Terakhir, simpan file PDF keluaran menggunakan metode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Potongan kode berikut menunjukkan cara menambahkan stempel gambar di semua halaman dalam file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageStampOnAllPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindImage(dataDir + "StampImage.png");
        stamp.SetOrigin(10, 200);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Set particular pages (page 2)
        stamp.Pages = new[] { 2 };

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddImageStampOnAllPages_out.pdf");
    }
}
```

### Kontrol kualitas gambar saat menambahkan sebagai stempel

Saat menambahkan Gambar sebagai objek stempel, Anda juga dapat mengontrol kualitas gambar. Untuk memenuhi persyaratan ini, properti Quality ditambahkan untuk kelas [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Ini menunjukkan kualitas gambar dalam persen (nilai yang valid adalah 0..100).

## Tambahkan Stempel Gambar di Halaman Tertentu dalam File PDF

Kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) memungkinkan Anda untuk menambahkan stempel gambar di halaman tertentu dari file PDF. Untuk menambahkan stempel gambar, Anda pertama-tama perlu membuat objek dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) dan [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Anda juga perlu membuat stempel gambar menggunakan metode [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) dari kelas [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Anda dapat mengatur atribut lain seperti asal, rotasi, latar belakang, dll. menggunakan objek [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) juga. Karena Anda ingin menambahkan stempel gambar di halaman tertentu dari file PDF, Anda juga perlu mengatur properti [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) dari kelas [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Properti ini memerlukan array integer yang berisi nomor halaman di mana Anda ingin menambahkan stempel. Kemudian Anda dapat menambahkan stempel ke file PDF menggunakan metode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Terakhir, simpan file PDF keluaran menggunakan metode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Potongan kode berikut menunjukkan cara menambahkan stempel gambar di halaman tertentu dalam file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageStampOnParticularPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindImage(dataDir + "StampImage.png");
        stamp.SetOrigin(10, 200);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddImageStampOnParticularPages_out.pdf");
    }
}
```