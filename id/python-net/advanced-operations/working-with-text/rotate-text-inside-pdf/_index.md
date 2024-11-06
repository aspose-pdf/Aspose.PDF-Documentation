---
title: Memutar Teks di Dalam PDF menggunakan Python
linktitle: Memutar Teks di Dalam PDF
type: docs
weight: 50
url: id/python-net/rotate-text-inside-pdf/
description: Pelajari berbagai cara untuk memutar teks ke PDF. Aspose.PDF memungkinkan Anda memutar teks ke sudut mana pun, memutar fragmen teks atau seluruh paragraf.
lastmod: "2024-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Memutar Teks di Dalam PDF menggunakan Python",
    "alternativeHeadline": "Cara Memutar Teks dalam Berkas PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generasi dokumen pdf",
    "keywords": "pdf, python, generasi dokumen",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dokumen Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/rotate-text-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/rotate-text-inside-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "Pelajari berbagai cara untuk memutar teks ke PDF. Aspose.PDF memungkinkan Anda memutar teks ke sudut mana pun, memutar fragmen teks atau seluruh paragraf."
}
</script>


## Memutar Teks di Dalam PDF menggunakan Properti Rotasi

Dengan menggunakan properti Rotasi dari Kelas [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment), Anda dapat memutar teks pada berbagai sudut. Rotasi teks dapat digunakan dalam berbagai skenario pembuatan dokumen. Anda dapat menentukan sudut rotasi dalam derajat untuk memutar teks sesuai kebutuhan Anda. Silakan periksa skenario berbeda berikut, di mana Anda dapat menerapkan rotasi teks.

## Menerapkan Rotasi menggunakan TextFragment dan TextBuilder

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Inisialisasi objek dokumen
Document pdfDocument = new Document();
// Dapatkan halaman tertentu
Page pdfPage = (Page)pdfDocument.Pages.Add();
// Buat fragmen teks
TextFragment textFragment1 = new TextFragment("teks utama");
textFragment1.Position = new Position(100, 600);
// Atur properti teks
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Buat fragmen teks berotasi
TextFragment textFragment2 = new TextFragment("teks berotasi");
textFragment2.Position = new Position(200, 600);
// Atur properti teks
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment2.TextState.Rotation = 45;
// Buat fragmen teks berotasi
TextFragment textFragment3 = new TextFragment("teks berotasi");
textFragment3.Position = new Position(300, 600);
// Atur properti teks
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment3.TextState.Rotation = 90;
// buat objek TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);
// Tambahkan fragmen teks ke halaman PDF
textBuilder.AppendText(textFragment1);
textBuilder.AppendText(textFragment2);
textBuilder.AppendText(textFragment3);
// Simpan dokumen
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated1_out.pdf");
```


## Menerapkan Rotasi menggunakan TextParagraph dan TextBuilder (Fragmen Terputar)

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Inisialisasi objek dokumen
Document pdfDocument = new Document();
// Dapatkan halaman tertentu
Page pdfPage = (Page)pdfDocument.Pages.Add();
TextParagraph paragraph = new TextParagraph();
paragraph.Position = new Position(200, 600);
// Buat fragmen teks
TextFragment textFragment1 = new TextFragment("teks berputar");
// Atur properti teks
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Atur rotasi
textFragment1.TextState.Rotation = 45;
// Buat fragmen teks
TextFragment textFragment2 = new TextFragment("teks utama");
// Atur properti teks
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Buat fragmen teks
TextFragment textFragment3 = new TextFragment("teks berputar lain");
// Atur properti teks
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Atur rotasi
textFragment3.TextState.Rotation = -45;
// Tambahkan fragmen teks ke paragraf
paragraph.AppendLine(textFragment1);
paragraph.AppendLine(textFragment2);
paragraph.AppendLine(textFragment3);
// Buat objek TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);
// Tambahkan paragraf teks ke halaman PDF
textBuilder.AppendParagraph(paragraph);
// Simpan dokumen
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated2_out.pdf");
```


## Menerapkan Rotasi menggunakan TextFragment dan Page.Paragraphs

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Inisialisasi objek dokumen
Document pdfDocument = new Document();
// Dapatkan halaman tertentu
Page pdfPage = (Page)pdfDocument.Pages.Add();
// Buat fragmen teks
TextFragment textFragment1 = new TextFragment("teks utama");
// Atur properti teks
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Buat fragmen teks
TextFragment textFragment2 = new TextFragment("teks berotasi");
// Atur properti teks
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Atur rotasi
textFragment2.TextState.Rotation = 315;
// Buat fragmen teks
TextFragment textFragment3 = new TextFragment("teks berotasi");
// Atur properti teks
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Atur rotasi
textFragment3.TextState.Rotation = 270;
pdfPage.Paragraphs.Add(textFragment1);
pdfPage.Paragraphs.Add(textFragment2);
pdfPage.Paragraphs.Add(textFragment3);
// Simpan dokumen
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated3_out.pdf");
```


## Menerapkan Rotasi menggunakan TextParagraph dan TextBuilder (Seluruh Paragraf Diputar)

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Inisialisasi objek dokumen
Document pdfDocument = new Document();
// Dapatkan halaman tertentu
Page pdfPage = (Page)pdfDocument.Pages.Add();
for (int i = 0; i < 4; i++)
{
    TextParagraph paragraph = new TextParagraph();
    paragraph.Position = new Position(200, 600);
    // Tentukan rotasi
    paragraph.Rotation = i * 90 + 45;
    // Buat fragmen teks
    TextFragment textFragment1 = new TextFragment("Teks Paragraf");
    // Buat fragmen teks
    textFragment1.TextState.FontSize = 12;
    textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment1.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment1.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    // Buat fragmen teks
    TextFragment textFragment2 = new TextFragment("Baris kedua dari teks");
    // Atur properti teks
    textFragment2.TextState.FontSize = 12;
    textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment2.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment2.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    // Buat fragmen teks
    TextFragment textFragment3 = new TextFragment("Dan beberapa teks lagi...");
    // Atur properti teks
    textFragment3.TextState.FontSize = 12;
    textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment3.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment3.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    textFragment3.TextState.Underline = true;
    paragraph.AppendLine(textFragment1);
    paragraph.AppendLine(textFragment2);
    paragraph.AppendLine(textFragment3);
    // Buat objek TextBuilder
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // Tambahkan fragmen teks ke halaman PDF
    textBuilder.AppendParagraph(paragraph);
}
// Simpan dokumen
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated4_out.pdf");
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF untuk .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
                "contactType": "penjualan",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "penjualan",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "penjualan",
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
    "applicationCategory": "Perpustakaan Manipulasi PDF untuk .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>