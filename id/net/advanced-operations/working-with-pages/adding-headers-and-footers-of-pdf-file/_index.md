---
title: Add Header and Footer to PDF
linktitle: Add Header and Footer to PDF
type: docs
weight: 70
url: id/net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF untuk .NET memungkinkan Anda menambahkan header dan footer ke file PDF Anda menggunakan kelas TextStamp.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/manage-header-and-footer-of-pdf-file/
    - /net/manage-header-and-footer/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Header and Footer to PDF",
    "alternativeHeadline": "How to add Header and Footer to PDF File",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, add header, add footer in pdf",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/add-headers-and-footers-of-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-headers-and-footers-of-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF untuk .NET memungkinkan Anda menambahkan header dan footer ke file PDF Anda menggunakan kelas TextStamp."
}
</script>
**Aspose.PDF for .NET** memungkinkan Anda untuk menambahkan header dan footer dalam file PDF yang sudah ada. Anda dapat menambahkan gambar atau teks ke dalam dokumen PDF. Juga, cobalah untuk menambahkan header yang berbeda dalam satu file PDF dengan C#.

Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Menambahkan Teks di Header File PDF

Anda dapat menggunakan kelas [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/textstamp) untuk menambahkan teks di header file PDF. Kelas TextStamp menyediakan properti yang diperlukan untuk membuat stempel berbasis teks seperti ukuran font, gaya font, dan warna font, dll. Untuk menambahkan teks di header, Anda perlu membuat objek Dokumen dan objek TextStamp menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode AddStamp dari halaman untuk menambahkan teks di header PDF.

Anda perlu mengatur properti TopMargin sedemikian rupa sehingga menyesuaikan teks di area header PDF Anda. Anda juga perlu mengatur HorizontalAlignment ke Center dan VerticalAlignment ke Top.

Potongan kode berikut menunjukkan cara menambahkan teks di header file PDF dengan C#.
Potongan kode berikut menunjukkan cara menambahkan teks di header file PDF dengan C#.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Buka dokumen
Document pdfDocument = new Document(dataDir+ "TextinHeader.pdf");

// Buat header
TextStamp textStamp = new TextStamp("Teks Header");
// Atur properti dari stempel
textStamp.TopMargin = 10;
textStamp.HorizontalAlignment = HorizontalAlignment.Center;
textStamp.VerticalAlignment = VerticalAlignment.Top;
// Tambahkan header di semua halaman
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(textStamp);
}
// Simpan dokumen yang telah diperbarui
pdfDocument.Save(dataDir+ "TextinHeader_out.pdf");
```

## Menambahkan Teks di Footer File PDF

Anda dapat menggunakan kelas TextStamp untuk menambahkan teks di footer file PDF.
Anda dapat menggunakan kelas TextStamp untuk menambahkan teks di footer file PDF.

{{% alert color="primary" %}}

Anda perlu mengatur properti Bottom Margin sedemikian rupa sehingga menyesuaikan teks di area footer PDF Anda. Anda juga perlu mengatur HorizontalAlignment ke Center dan VerticalAlignment ke Bottom

{{% /alert %}}

Potongan kode berikut menunjukkan cara menambahkan teks di footer file PDF dengan C#.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Buka dokumen
Document pdfDocument = new Document(dataDir+ "TextinFooter.pdf");
// Buat footer
TextStamp textStamp = new TextStamp("Teks Footer");
// Atur properti stempel
textStamp.BottomMargin = 10;
textStamp.HorizontalAlignment = HorizontalAlignment.Center;
textStamp.VerticalAlignment = VerticalAlignment.Bottom;
// Tambahkan footer di semua halaman
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(textStamp);
}
// Simpan file keluaran
doc.Save(dataDir + "TextinFooter_out.pdf");
```
## Menambahkan Gambar di Header File PDF

Anda dapat menggunakan kelas [ImageStamp](https://reference.aspose.com/pdf/net/aspose.pdf/ImageStamp) untuk menambahkan gambar di header file PDF. Kelas Image Stamp menyediakan properti yang diperlukan untuk membuat stempel berbasis gambar seperti ukuran font, gaya font, dan warna font dll. Untuk menambahkan gambar di header, Anda perlu membuat objek Dokumen dan objek Image Stamp menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) dari Halaman untuk menambahkan gambar di header PDF.

{{% alert color="primary" %}}

Anda perlu mengatur properti TopMargin sedemikian rupa sehingga menyesuaikan gambar di area header PDF Anda. Anda juga perlu mengatur HorizontalAlignment ke Center dan VerticalAlignment ke Top.

{{% /alert %}}

Potongan kode berikut menunjukkan cara menambahkan gambar di header file PDF dengan C#.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Buka dokumen
Document pdfDocument = new Document(dataDir+ "ImageinHeader.pdf");

// Buat header
ImageStamp imageStamp = new ImageStamp(dataDir+ "aspose-logo.jpg");
// Atur properti stempel
imageStamp.TopMargin = 10;
imageStamp.HorizontalAlignment = HorizontalAlignment.Center;
imageStamp.VerticalAlignment = VerticalAlignment.Top;
// Tambahkan header di semua halaman
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(imageStamp);
}
// Simpan file keluaran
doc.Save(dataDir + "ImageinHeader_out.pdf");
```
## Menambahkan Gambar di Footer File PDF

Anda dapat menggunakan kelas Image Stamp untuk menambahkan gambar di footer file PDF. Kelas Image Stamp menyediakan properti yang diperlukan untuk membuat stempel berbasis gambar seperti ukuran font, gaya font, dan warna font, dll. Untuk menambahkan gambar di footer, Anda perlu membuat objek Document dan objek Image Stamp dengan menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode AddStamp dari Page untuk menambahkan gambar di footer PDF.

{{% alert color="primary" %}}

Anda perlu mengatur properti [BottomMargin](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/bottommargin) sedemikian rupa sehingga menyesuaikan gambar di area footer PDF Anda. Anda juga perlu mengatur [HorizontalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/horizontalalignment) menjadi `Center` dan [VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/verticalalignment) menjadi `Bottom`.

{{% /alert %}}

Berikut ini cuplikan kode yang menunjukkan cara menambahkan gambar di footer file PDF dengan C#.
Potongan kode berikut menunjukkan cara menambahkan gambar di footer file PDF dengan C#.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Buka dokumen
Document pdfDocument = new Document(dataDir+ "ImageInFooter.pdf");
// Buat footer
ImageStamp imageStamp = new ImageStamp(dataDir+ "aspose-logo.jpg");
// Atur properti dari stempel
imageStamp.BottomMargin = 10;
imageStamp.HorizontalAlignment = HorizontalAlignment.Center;
imageStamp.VerticalAlignment = VerticalAlignment.Bottom;
// Tambahkan footer di semua halaman
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(imageStamp);
}
// Simpan file keluaran
doc.Save(dataDir + "ImageInFooter_out.pdf");
```

## Menambahkan Berbagai Header dalam Satu File PDF

Kita tahu bahwa kita dapat menambahkan TextStamp di bagian Header/Footer dokumen dengan menggunakan properti TopMargin atau Bottom Margin, tetapi terkadang kita mungkin memiliki kebutuhan untuk menambahkan beberapa header/footer dalam satu dokumen PDF.
Kami tahu bahwa kita dapat menambahkan TextStamp di bagian Header/Footer dokumen dengan menggunakan properti TopMargin atau Bottom Margin, tetapi terkadang kita mungkin perlu menambahkan beberapa header/footer dalam satu dokumen PDF.

Untuk mencapai kebutuhan ini, kita akan membuat objek TextStamp individu (jumlah objek tergantung pada jumlah Header/Footer yang diperlukan) dan akan menambahkannya ke dokumen PDF. Kita juga dapat menentukan informasi pemformatan yang berbeda untuk setiap objek cap. Dalam contoh berikut, kita telah membuat objek Dokumen dan tiga objek TextStamp dan kemudian kita telah menggunakan metode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) dari Halaman untuk menambahkan teks di bagian header PDF. Potongan kode berikut menunjukkan cara menambahkan gambar di footer file PDF dengan Aspose.PDF untuk .NET.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Buka dokumen sumber
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "AddingDifferentHeaders.pdf");

// Buat tiga cap
Aspose.Pdf.TextStamp stamp1 = new Aspose.Pdf.TextStamp("Header 1");
Aspose.Pdf.TextStamp stamp2 = new Aspose.Pdf.TextStamp("Header 2");
Aspose.Pdf.TextStamp stamp3 = new Aspose.Pdf.TextStamp("Header 3");

// Atur penyelarasan cap (tempatkan cap di atas halaman, dipusatkan secara horizontal)
stamp1.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
stamp1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Tentukan gaya font sebagai Bold
stamp1.TextState.FontStyle = FontStyles.Bold;
// Atur informasi warna latar depan teks sebagai merah
stamp1.TextState.ForegroundColor = Color.Red;
// Tentukan ukuran font sebagai 14
stamp1.TextState.FontSize = 14;

// Sekarang kita perlu mengatur penyelarasan vertikal objek cap kedua sebagai Atas
stamp2.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
// Atur informasi penyelarasan Horizontal untuk cap sebagai Tengah
stamp2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Atur faktor pembesaran untuk objek cap
stamp2.Zoom = 10;

// Atur pemformatan objek cap ketiga
// Tentukan informasi Penyelarasan Vertikal untuk objek cap sebagai ATAS
stamp3.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
// Atur informasi Penyelarasan Horizontal untuk objek cap sebagai Tengah
stamp3.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Atur sudut rotasi untuk objek cap
stamp3.RotateAngle = 35;
// Atur pink sebagai warna latar belakang untuk cap
stamp3.TextState.BackgroundColor = Color.Pink;
// Ubah informasi jenis huruf untuk cap menjadi Verdana
stamp3.TextState.Font = FontRepository.FindFont("Verdana");
// Cap pertama ditambahkan di halaman pertama;
doc.Pages[1].AddStamp(stamp1);
// Cap kedua ditambahkan di halaman kedua;
doc.Pages[2].AddStamp(stamp2);
// Cap ketiga ditambahkan di halaman ketiga.
doc.Pages[3].AddStamp(stamp3);
// Simpan dokumen yang telah diperbarui
doc.Save(dataDir + "MultiHeader_out.pdf");
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

