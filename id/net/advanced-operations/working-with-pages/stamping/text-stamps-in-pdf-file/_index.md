---
title: Menambahkan Cap Teks di PDF C#
linktitle: Cap Teks di File PDF
type: docs
weight: 20
url: id/net/text-stamps-in-the-pdf-file/
description: Menambahkan cap teks ke dokumen PDF menggunakan kelas TextStamp dengan pustaka Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Menambahkan Cap Teks di PDF C#",
    "alternativeHeadline": "Menambahkan Cap Teks di PDF C#",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pembuatan dokumen PDF",
    "keywords": "pdf, c#, pembuatan dokumen",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dok Aspose.PDF",
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
    "url": "/net/text-stamps-in-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-stamps-in-the-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Menambahkan cap teks ke dokumen PDF menggunakan kelas TextStamp dengan pustaka Aspose.PDF for .NET."
}
</script>

## Menambahkan Cap Teks dengan C#

Anda dapat menggunakan kelas [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/TextStamp) untuk menambahkan cap teks dalam file PDF. Kelas TextStamp menyediakan properti yang diperlukan untuk membuat cap berbasis teks seperti ukuran font, gaya font, dan warna font, dll. Untuk menambahkan cap teks, Anda perlu membuat objek Dokumen dan objek TextStamp menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode AddStamp dari Halaman untuk menambahkan cap dalam PDF.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

Potongan kode berikut menunjukkan cara menambahkan cap teks dalam file PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Buka dokumen
Document pdfDocument = new Document(dataDir+ "AddTextStamp.pdf");

// Buat cap teks
TextStamp textStamp = new TextStamp("Sample Stamp");
// Atur apakah cap adalah latar belakang
textStamp.Background = true;
// Atur asal
textStamp.XIndent = 100;
textStamp.YIndent = 100;
// Putar cap
textStamp.Rotate = Rotation.on90;
// Atur properti teks
textStamp.TextState.Font = FontRepository.FindFont("Arial");
textStamp.TextState.FontSize = 14.0F;
textStamp.TextState.FontStyle = FontStyles.Bold;
textStamp.TextState.FontStyle = FontStyles.Italic;
textStamp.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Aqua);
// Tambahkan cap ke halaman tertentu
pdfDocument.Pages[1].AddStamp(textStamp);

dataDir = dataDir + "AddTextStamp_out.pdf";
// Simpan dokumen keluaran
pdfDocument.Save(dataDir);
```
## Tentukan perataan untuk objek TextStamp

Menambahkan watermark ke dokumen PDF adalah salah satu fitur yang sering diminta dan Aspose.PDF untuk .NET sepenuhnya mampu menambahkan watermark Gambar serta Teks. Kami memiliki kelas bernama [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/textstamp) yang menyediakan fitur untuk menambahkan cap teks ke atas file PDF. Baru-baru ini telah ada kebutuhan untuk mendukung fitur untuk menentukan perataan teks saat menggunakan objek TextStamp. Jadi untuk memenuhi kebutuhan ini, kami telah memperkenalkan properti TextAlignment di kelas TextStamp. Menggunakan properti ini, kita dapat menentukan perataan teks Horizontal.

Potongan kode berikut menunjukkan contoh cara memuat dokumen PDF yang ada dan menambahkan TextStamp di atasnya.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Instansiasi objek Dokumen dengan file masukan
Document doc = new Document(dataDir+ "DefineAlignment.pdf");
// Instansiasi objek FormattedText dengan string contoh
FormattedText text = new FormattedText("This");
// Tambahkan baris teks baru ke FormattedText
text.AddNewLineText("is sample");
text.AddNewLineText("Center Aligned");
text.AddNewLineText("TextStamp");
text.AddNewLineText("Object");
// Buat objek TextStamp menggunakan FormattedText
TextStamp stamp = new TextStamp(text);
// Tentukan Perataan Horizontal dari cap teks sebagai Tengah
stamp.HorizontalAlignment = HorizontalAlignment.Center;
// Tentukan Perataan Vertikal dari cap teks sebagai Tengah
stamp.VerticalAlignment = VerticalAlignment.Center;
// Tentukan Perataan Teks Horizontal dari TextStamp sebagai Tengah
stamp.TextAlignment = HorizontalAlignment.Center;
// Setel margin atas untuk objek cap
stamp.TopMargin = 20;
// Tambahkan objek cap ke halaman pertama dokumen
doc.Pages[1].AddStamp(stamp);

dataDir = dataDir + "StampedPDF_out.pdf";
// Simpan dokumen yang telah diperbarui
doc.Save(dataDir);
```
## Mengisi Teks Garis Stroke sebagai Cap dalam Berkas PDF

Kami telah mengimplementasikan pengaturan mode rendering untuk skenario penambahan dan pengeditan teks. Untuk me-render teks garis stroke, silakan buat objek TextState dan atur RenderingMode ke TextRenderingMode.StrokeText dan juga pilih warna untuk properti StrokingColor. Kemudian, ikat TextState ke cap menggunakan metode BindTextState().

Potongan kode berikut menunjukkan penambahan Teks Garis Stroke:

```csharp
// Untuk contoh lengkap dan berkas data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
// Buat objek TextState untuk mentransfer properti lanjutan
TextState ts = new TextState();
// Atur warna untuk stroke
ts.StrokingColor = Color.Gray;
// Atur mode rendering teks
ts.RenderingMode = TextRenderingMode.StrokeText;
// Muat dokumen PDF masukan
Facades.PdfFileStamp fileStamp = new Facades.PdfFileStamp(new Aspose.Pdf.Document(dataDir + "input.pdf"));

Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
stamp.BindLogo(new Facades.FormattedText("LUNAS", System.Drawing.Color.Gray, "Arial", Facades.EncodingType.Winansi, true, 78));

// Ikat TextState
stamp.BindTextState(ts);
// Atur asal X,Y
stamp.SetOrigin(100, 100);
stamp.Opacity = 5;
stamp.BlendingSpace = Facades.BlendingColorSpace.DeviceRGB;
stamp.Rotation = 45.0F;
stamp.IsBackground = false;
// Tambahkan Cap
fileStamp.AddStamp(stamp);
fileStamp.Save(dataDir + "ouput_out.pdf");
fileStamp.Close();
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Perpustakaan Aspose.PDF untuk .NET",
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
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

