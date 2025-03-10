---
title: Bekerja dengan Judul di PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
url: /id/net/working-with-headings/
weight: 70
description: Buat penomoran di judul dokumen PDF Anda dengan C#. Aspose.PDF for .NET menawarkan berbagai jenis gaya penomoran.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Headings in PDF",
    "alternativeHeadline": "Enhance PDF Headings with Custom Numbering Styles",
    "abstract": "Tingkatkan dokumen PDF Anda dengan penomoran judul yang dapat disesuaikan menggunakan Aspose.PDF for .NET. Fitur baru ini memungkinkan Anda menerapkan berbagai gaya penomoran yang telah ditentukan sebelumnya, seperti angka Romawi dan daftar alfabet, untuk mengatur judul Anda secara efektif, meningkatkan keterbacaan dan struktur dokumen. Permudah proses pembuatan PDF Anda dengan mengintegrasikan fungsionalitas serbaguna ini ke dalam aplikasi C# Anda",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF, C#, headings in PDF, numbering style, Aspose.PDF for .NET, pre-defined numbering styles, NumberingStyle enumeration, document generation, Heading class, pdf document manipulation",
    "wordcount": "453",
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
    "url": "/net/working-with-headings/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-headings/"
    },
    "dateModified": "2024-11-25",
    "description": "Buat penomoran di judul dokumen PDF Anda dengan C#. Aspose.PDF for .NET menawarkan berbagai jenis gaya penomoran."
}
</script>

## Terapkan Gaya Penomoran di Judul

Judul adalah bagian penting dari dokumen apa pun. Penulis selalu berusaha untuk membuat judul lebih menonjol dan bermakna bagi pembacanya. Jika ada lebih dari satu judul dalam sebuah dokumen, penulis memiliki beberapa opsi untuk mengatur judul-judul ini. Salah satu pendekatan yang paling umum untuk mengatur judul adalah dengan menulis judul dalam Gaya Penomoran.

[Aspose.PDF for .NET](/pdf/id/net/) menawarkan banyak gaya penomoran yang telah ditentukan sebelumnya. Gaya penomoran yang telah ditentukan sebelumnya ini disimpan dalam sebuah enumerasi, NumberingStyle. Nilai-nilai yang telah ditentukan sebelumnya dari enumerasi NumberingStyle dan deskripsinya diberikan di bawah ini:

|**Tipe Judul**|**Deskripsi**|
| :- | :- |
|NumeralsArabic|Tipe Arab, misalnya, 1,1.1,...|
|NumeralsRomanUppercase|Tipe Romawi besar, misalnya, I,I.II, ...|
|NumeralsRomanLowercase|Tipe Romawi kecil, misalnya, i,i.ii, ...|
|LettersUppercase|Tipe Inggris besar, misalnya, A,A.B, ...|
|LettersLowercase|Tipe Inggris kecil, misalnya, a,a.b, ...|
Properti **Style** dari kelas **Aspose.Pdf.Heading** digunakan untuk mengatur gaya penomoran dari judul-judul.

|**Gambar: Gaya penomoran yang telah ditentukan sebelumnya**|
| :- |
Kode sumber, untuk mendapatkan output yang ditunjukkan dalam gambar di atas, diberikan di bawah ini dalam contoh.

Cuplikan kode berikut juga bekerja dengan pustaka [Aspose.Drawing](/pdf/id/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ApplyNumberStyleToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.PageInfo.Width = 612.0;
        document.PageInfo.Height = 792.0;
        document.PageInfo.Margin = new Aspose.Pdf.MarginInfo();
        document.PageInfo.Margin.Left = 72;
        document.PageInfo.Margin.Right = 72;
        document.PageInfo.Margin.Top = 72;
        document.PageInfo.Margin.Bottom = 72;

        // Add page
        var pdfPage = document.Pages.Add();
        pdfPage.PageInfo.Width = 612.0;
        pdfPage.PageInfo.Height = 792.0;
        pdfPage.PageInfo.Margin = new Aspose.Pdf.MarginInfo();
        pdfPage.PageInfo.Margin.Left = 72;
        pdfPage.PageInfo.Margin.Right = 72;
        pdfPage.PageInfo.Margin.Top = 72;
        pdfPage.PageInfo.Margin.Bottom = 72;

        // Create a floating box with the same margin as the page
        var floatBox = new Aspose.Pdf.FloatingBox();
        floatBox.Margin = pdfPage.PageInfo.Margin;

        // Add the floating box to the page
        pdfPage.Paragraphs.Add(floatBox);

        // Add headings with numbering styles
        var heading = new Aspose.Pdf.Heading(1);
        heading.IsInList = true;
        heading.StartNumber = 1;
        heading.Text = "List 1";
        heading.Style = Aspose.Pdf.NumberingStyle.NumeralsRomanLowercase;
        heading.IsAutoSequence = true;
        floatBox.Paragraphs.Add(heading);

        var heading2 = new Aspose.Pdf.Heading(1);
        heading2.IsInList = true;
        heading2.StartNumber = 13;
        heading2.Text = "List 2";
        heading2.Style = Aspose.Pdf.NumberingStyle.NumeralsRomanLowercase;
        heading2.IsAutoSequence = true;
        floatBox.Paragraphs.Add(heading2);

        var heading3 = new Aspose.Pdf.Heading(2);
        heading3.IsInList = true;
        heading3.StartNumber = 1;
        heading3.Text = "the value, as of the effective date of the plan, of property to be distributed under the plan on account of each allowed";
        heading3.Style = Aspose.Pdf.NumberingStyle.LettersLowercase;
        heading3.IsAutoSequence = true;
        floatBox.Paragraphs.Add(heading3);

        // Save PDF document
        document.Save(dataDir + "ApplyNumberStyle_out.pdf");
    }
}
```

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