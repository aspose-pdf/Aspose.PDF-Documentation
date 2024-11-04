---
title: Memformat Dokumen PDF menggunakan C#
linktitle: Memformat Dokumen PDF
type: docs
weight: 11
url: /net/formatting-pdf-document/
description: Buat dan format Dokumen PDF dengan Aspose.PDF untuk .NET. Gunakan potongan kode berikut untuk menyelesaikan tugas Anda.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Memformat Dokumen PDF menggunakan C#",
    "alternativeHeadline": "Cara memformat Dokumen PDF di .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, dotnet, format dokumen pdf",
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
    "url": "/net/formatting-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/formatting-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Buat dan format Dokumen PDF dengan Aspose.PDF untuk .NET. Gunakan potongan kode berikut untuk menyelesaikan tugas Anda."
}
</script>

## Memformat Dokumen PDF

### Mendapatkan Properti Jendela Dokumen dan Tampilan Halaman

Topik ini membantu Anda memahami bagaimana mendapatkan properti dari jendela dokumen, aplikasi penampil, dan bagaimana halaman ditampilkan. Untuk mengatur properti ini:

Buka file PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Sekarang, Anda dapat mengatur properti objek Document, seperti

- CenterWindow – Pusatkan jendela dokumen di layar. Default: false.
- Direction – Urutan baca. Ini menentukan bagaimana halaman disusun saat ditampilkan berdampingan. Default: dari kiri ke kanan.
- DisplayDocTitle – Tampilkan judul dokumen di bilah judul jendela dokumen. Default: false (judul ditampilkan).
- HideMenuBar – Sembunyikan atau tampilkan bilah menu jendela dokumen. Default: false (bilah menu ditampilkan).
- HideToolBar – Sembunyikan atau tampilkan bilah alat jendela dokumen. Default: false (bilah alat ditampilkan).
- HideWindowUI – Sembunyikan atau tampilkan elemen jendela dokumen seperti bilah gulir.
- HideWindowUI – Sembunyikan atau tampilkan elemen jendela dokumen seperti bilah gulir.
- NonFullScreenPageMode – Bagaimana dokumen ditampilkan saat tidak dalam mode halaman penuh.
- PageLayout – Tata letak halaman.
- PageMode – Bagaimana dokumen ditampilkan saat pertama kali dibuka. Opsi yang tersedia adalah tampilkan thumbnail, layar penuh, tampilkan panel lampiran.

Potongan kode berikut juga berfungsi dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

Potongan kode berikut menunjukkan cara mendapatkan properti menggunakan kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "GetDocumentWindow.pdf");

// Dapatkan berbagai properti dokumen
// Posisi jendela dokumen - Default: false
Console.WriteLine("CenterWindow : {0}", pdfDocument.CenterWindow);
  
// Urutan bacaan yang dominan; menentukan posisi halaman
// Saat ditampilkan berdampingan - Default: L2R
Console.WriteLine("Direction : {0}", pdfDocument.Direction);

// Apakah bilah judul jendela harus menampilkan judul dokumen
// Jika tidak, bilah judul menampilkan nama file PDF - Default: false
Console.WriteLine("DisplayDocTitle : {0}", pdfDocument.DisplayDocTitle);

// Apakah mengubah ukuran jendela dokumen untuk sesuai dengan ukuran
// Halaman yang ditampilkan pertama - Default: false
Console.WriteLine("FitWindow : {0}", pdfDocument.FitWindow);

// Apakah menyembunyikan bilah menu aplikasi penampil - Default: false
Console.WriteLine("HideMenuBar : {0}", pdfDocument.HideMenubar);

// Apakah menyembunyikan bilah alat aplikasi penampil - Default: false
Console.WriteLine("HideToolBar : {0}", pdfDocument.HideToolBar);

// Apakah menyembunyikan elemen UI seperti bilah gulir
// Dan hanya menampilkan konten halaman - Default: false
Console.WriteLine("HideWindowUI : {0}", pdfDocument.HideWindowUI);

// Mode halaman dokumen. Bagaimana menampilkan dokumen saat keluar dari mode layar penuh.
Console.WriteLine("NonFullScreenPageMode : {0}", pdfDocument.NonFullScreenPageMode);

// Tata letak halaman yaitu halaman tunggal, satu kolom
Console.WriteLine("PageLayout : {0}", pdfDocument.PageLayout);

// Bagaimana dokumen seharusnya ditampilkan saat dibuka
// Misalnya tampilkan thumbnail, layar penuh, tampilkan panel lampiran
Console.WriteLine("pageMode : {0}", pdfDocument.PageMode);
```
### Atur Properti Jendela Dokumen dan Tampilan Halaman

Topik ini menjelaskan cara mengatur properti jendela dokumen, aplikasi penampil, dan tampilan halaman. Untuk mengatur properti yang berbeda:

1. Buka file PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Atur properti objek Document.
1. Simpan file PDF yang telah diperbarui menggunakan metode Save.

Properti yang tersedia adalah:

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

Masing-masing digunakan dan dijelaskan dalam kode di bawah ini. Cuplikan kode berikut menunjukkan cara mengatur properti menggunakan kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "SetDocumentWindow.pdf");

// Atur berbagai properti dokumen
// Tentukan posisi jendela dokumen - Default: false
pdfDocument.CenterWindow = true;

// Urutan baca dominan; menentukan posisi halaman
// Saat ditampilkan berdampingan - Default: L2R
pdfDocument.Direction = Direction.R2L;

// Tentukan apakah bilah judul jendela harus menampilkan judul dokumen
// Jika tidak, bilah judul menampilkan nama file PDF - Default: false
pdfDocument.DisplayDocTitle = true;

// Tentukan apakah mengubah ukuran jendela dokumen untuk menyesuaikan ukuran
// Halaman pertama yang ditampilkan - Default: false
pdfDocument.FitWindow = true;

// Tentukan apakah menyembunyikan bilah menu aplikasi penampil - Default: false
pdfDocument.HideMenubar = true;

// Tentukan apakah menyembunyikan bilah alat aplikasi penampil - Default: false
pdfDocument.HideToolBar = true;

// Tentukan apakah menyembunyikan elemen UI seperti bilah gulir
// Dan hanya menampilkan konten halaman - Default: false
pdfDocument.HideWindowUI = true;

// Mode halaman dokumen. tentukan cara menampilkan dokumen saat keluar mode layar penuh.
pdfDocument.NonFullScreenPageMode = PageMode.UseOC;

// Tentukan tata letak halaman, misalnya halaman tunggal, satu kolom
pdfDocument.PageLayout = PageLayout.TwoColumnLeft;

// Tentukan bagaimana dokumen harus ditampilkan saat dibuka
// Misalnya menampilkan thumbnail, layar penuh, menampilkan panel lampiran
pdfDocument.PageMode = PageMode.UseThumbs;

dataDir = dataDir + "SetDocumentWindow_out.pdf";
// Simpan file PDF yang telah diperbarui
pdfDocument.Save(dataDir);
```
### Menanamkan Font dalam file PDF yang ada

Pembaca PDF mendukung [inti dari 14 font](https://en.wikipedia.org/wiki/PDF#Text) sehingga dokumen dapat ditampilkan dengan cara yang sama terlepas dari platform tempat dokumen tersebut ditampilkan. Ketika PDF mengandung font yang bukan salah satu dari 14 font inti, tanamkan font tersebut ke dalam file PDF untuk menghindari penggantian font.

Aspose.PDF untuk .NET mendukung penanaman font dalam file PDF yang sudah ada. Anda dapat menanamkan font lengkap atau sebagian dari font tersebut. Untuk menanamkan font, buka file PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Kemudian gunakan kelas [Aspose.Pdf.Text.Font](https://reference.aspose.com/pdf/net/aspose.pdf.text) untuk menanamkan font ke dalam file PDF. Untuk menanamkan font secara penuh, gunakan properti IsEmbeded dari kelas Font; untuk menggunakan sebagian dari font, gunakan properti IsSubset.

{{% alert color="primary" %}}

Sebuah subset font hanya menanamkan karakter yang digunakan dan berguna di mana font digunakan untuk kalimat pendek atau slogan, contohnya di mana font perusahaan digunakan untuk logo, tetapi tidak untuk teks utama.
Sebuah subset font hanya menanamkan karakter yang digunakan dan berguna ketika font digunakan untuk kalimat pendek atau slogan, misalnya ketika font perusahaan digunakan untuk logo, tetapi tidak untuk teks utama.

{{% /alert %}}

Potongan kode berikut menunjukkan cara menanamkan font dalam file PDF.

### Menanamkan Font Standar Type 1

Beberapa dokumen PDF memiliki font dari set font Adobe khusus. Font dari set ini disebut "Font Standar Type 1". Set ini mencakup 14 font dan menanamkan jenis font ini memerlukan penggunaan bendera khusus yaitu [Aspose.Pdf.Document.EmbedStandardFonts](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/embedstandardfonts). Berikut adalah potongan kode yang dapat digunakan untuk mendapatkan dokumen dengan semua font yang ditambahkan termasuk Font Standar Type 1:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Memuat Dokumen PDF yang ada
Document pdfDocument = new Document(dataDir + "input.pdf");
// Atur properti EmbedStandardFonts dari dokumen
pdfDocument.EmbedStandardFonts = true;
foreach (Aspose.Pdf.Page page in pdfDocument.Pages)
{
    if (page.Resources.Fonts != null)
    {
        foreach (Aspose.Pdf.Text.Font pageFont in page.Resources.Fonts)
        {
// Periksa apakah font sudah tertanam
if (!pageFont.IsEmbedded)
{
    pageFont.IsEmbedded = true;
}
        }
    }
}
pdfDocument.Save(dataDir + "EmbeddedFonts-updated_out.pdf");
```
### Menyisipkan Font saat membuat PDF

Jika Anda perlu menggunakan font selain 14 font inti yang didukung oleh Adobe Reader, Anda harus menyisipkan deskripsi font saat menghasilkan file Pdf. Jika informasi font tidak disisipkan, Adobe Reader akan mengambilnya dari Sistem Operasi jika terpasang di sistem, atau akan membuat font pengganti sesuai dengan deskriptor font dalam Pdf.

>Harap diperhatikan bahwa font yang disisipkan harus terpasang di mesin host yaitu dalam hal kode berikut ini font ‘Univers Condensed’ terpasang di sistem.

Kita menggunakan properti IsEmbedded dari kelas Font untuk menyisipkan informasi font ke dalam file Pdf. Mengatur nilai properti ini menjadi ‘True’ akan menyisipkan file font lengkap ke dalam Pdf, mengetahui fakta bahwa ini akan meningkatkan ukuran file Pdf. Berikut adalah potongan kode yang dapat digunakan untuk menyisipkan informasi font ke dalam Pdf.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Instansiasi objek Pdf dengan memanggil konstruktornya yang kosong
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();

// Buat sebuah seksi dalam objek Pdf
Aspose.Pdf.Page page = doc.Pages.Add();

Aspose.Pdf.Text.TextFragment fragment = new Aspose.Pdf.Text.TextFragment("");

Aspose.Pdf.Text.TextSegment segment = new Aspose.Pdf.Text.TextSegment(" Ini adalah teks contoh menggunakan font Kustom.");
Aspose.Pdf.Text.TextState ts = new Aspose.Pdf.Text.TextState();
ts.Font = FontRepository.FindFont("Arial");
ts.Font.IsEmbedded = true;
segment.TextState = ts;
fragment.Segments.Add(segment);
page.Paragraphs.Add(fragment);

dataDir = dataDir + "EmbedFontWhileDocCreation_out.pdf";
// Simpan Dokumen PDF
doc.Save(dataDir);
```
### Tetapkan Nama Font Default saat Menyimpan PDF

Ketika dokumen PDF mengandung font yang tidak tersedia dalam dokumen itu sendiri dan pada perangkat, API menggantinya dengan font default. Ketika font tersedia (terinstal pada perangkat atau tertanam dalam dokumen), PDF keluaran harus memiliki font yang sama (tidak boleh diganti dengan font default). Nilai dari font default harus berisi nama font (bukan jalur ke file font). Kami telah mengimplementasikan fitur untuk menetapkan nama font default saat menyimpan dokumen sebagai PDF. Cuplikan kode berikut dapat digunakan untuk menetapkan font default:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Muat dokumen PDF yang ada dengan font yang hilang
string documentName = dataDir + "input.pdf";
string newName = "Arial";
using (System.IO.FileStream fs = new System.IO.FileStream(documentName, System.IO.FileMode.Open))
using (Document document = new Document(fs))
{
    PdfSaveOptions pdfSaveOptions = new PdfSaveOptions();
    // Tentukan Nama Font Default
    pdfSaveOptions.DefaultFontName = newName;
    document.Save(dataDir + "output_out.pdf", pdfSaveOptions);
}
```
### Mendapatkan Semua Font dari Dokumen PDF

Jika Anda ingin mendapatkan semua font dari sebuah dokumen PDF, Anda dapat menggunakan metode FontUtilities.GetAllFonts() yang disediakan di kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Silakan periksa cuplikan kode berikut untuk mendapatkan semua font dari dokumen PDF yang ada:

```csharp
// Untuk contoh lengkap dan berkas data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
Aspose.Pdf.Text.Font[] fonts = doc.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine(font.FontName);
}
```

### Mendapatkan Peringatan untuk Substitusi Font

Aspose.PDF untuk .NET menyediakan metode untuk mendapatkan notifikasi tentang substitusi font untuk menangani kasus substitusi font. Cuplikan kode di bawah menunjukkan bagaimana menggunakan fungsionalitas yang sesuai.

```csharp
// Untuk contoh lengkap dan berkas data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

Document doc = new Document(dataDir + "input.pdf");

doc.FontSubstitution += new Document.FontSubstitutionHandler(OnFontSubstitution);
```
Metode **OnFontSubstitution** tercantum seperti di bawah ini.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-NET
Console.WriteLine(string.Format("Font '{0}' digantikan dengan font lain '{1}'",
oldFont.FontName, newFont.FontName));
```

### Meningkatkan Penyertaan Font dengan Menggunakan FontSubsetStrategy

Fitur untuk menyertakan font sebagai subset dapat dicapai dengan menggunakan properti IsSubset, namun terkadang Anda ingin mengurangi set font yang sepenuhnya disertakan hanya menjadi subset yang digunakan dalam dokumen. Aspose.Pdf.Document memiliki properti FontUtilities yang mencakup metode SubsetFonts(FontSubsetStrategy subsetStrategy). Dalam metode SubsetFonts(), parameter subsetStrategy membantu menyetel strategi subset. FontSubsetStrategy mendukung dua varian subsetting font berikut.

- SubsetAllFonts - Ini akan menyertakan subset semua font yang digunakan dalam dokumen.
- SubsetEmbeddedFontsOnly - Ini akan menyertakan subset hanya untuk font-font yang sepenuhnya disertakan ke dalam dokumen.

Potongan kode berikut menunjukkan cara mengatur FontSubsetStrategy:
Snippet kode berikut menunjukkan cara mengatur FontSubsetStrategy:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
// Semua font akan tertanam sebagai subset ke dalam dokumen dalam kasus SubsetAllFonts.
doc.FontUtilities.SubsetFonts(FontSubsetStrategy.SubsetAllFonts);
// Subset font akan tertanam untuk font yang sepenuhnya tertanam tetapi font yang tidak tertanam ke dalam dokumen tidak akan terpengaruh.
doc.FontUtilities.SubsetFonts(FontSubsetStrategy.SubsetEmbeddedFontsOnly);
doc.Save(dataDir + "Output_out.pdf");
```

### Mengatur-Mendapatkan Faktor Zoom dari File PDF

Terkadang, Anda ingin mengetahui faktor zoom saat ini dari dokumen PDF. Dengan Aspose.Pdf, Anda dapat mengetahui nilai saat ini serta mengaturnya.

Properti Destination kelas [GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction) memungkinkan Anda untuk mendapatkan nilai zoom yang terkait dengan file PDF.
Kelas [GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction) memiliki properti Destination yang memungkinkan Anda mendapatkan nilai zoom yang terkait dengan file PDF.

#### Mengatur Faktor Zoom

Potongan kode berikut menunjukkan cara mengatur faktor zoom dari file PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Membuat objek Dokumen baru
Document doc = new Document(dataDir + "SetZoomFactor.pdf");

GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0, 0, .5));
doc.OpenAction = action;
dataDir = dataDir + "Zoomed_pdf_out.pdf";
// Simpan dokumen
doc.Save(dataDir);
```

#### Mendapatkan Faktor Zoom

Potongan kode berikut menunjukkan cara mendapatkan faktor zoom dari file PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Membuat objek Dokumen baru
Document doc = new Document(dataDir + "Zoomed_pdf.pdf");

// Membuat objek GoToAction
GoToAction action = doc.OpenAction as GoToAction;

// Mendapatkan faktor Zoom dari file PDF
System.Console.WriteLine((action.Destination as XYZExplicitDestination).Zoom); // Nilai zoom dokumen;
```
### Mengatur Properti Preset Dialog Cetak

Aspoose.PDF memungkinkan pengaturan properti Preset Dialog Cetak dari dokumen PDF. Ini memungkinkan Anda untuk mengubah properti DuplexMode untuk dokumen PDF yang secara default diatur ke simplex. Ini dapat dicapai menggunakan dua metodologi berbeda seperti yang ditunjukkan di bawah ini.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

using (Document doc = new Document())
{
    doc.Pages.Add();
    doc.Duplex = PrintDuplex.DuplexFlipLongEdge;
    doc.Save(dataDir + "35297_out.pdf", SaveFormat.Pdf);
}
```

### Mengatur Properti Preset Dialog Cetak menggunakan Editor Konten PDF

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

string outputFile = dataDir + "input.pdf";
using (PdfContentEditor ed = new PdfContentEditor())
{
    ed.BindPdf(outputFile);
    if ((ed.GetViewerPreference() & ViewerPreference.DuplexFlipShortEdge) > 0)
    {
        Console.WriteLine("File memiliki duplex flip short edge");
    }

    ed.ChangeViewerPreference(ViewerPreference.DuplexFlipShortEdge);
    ed.Save(dataDir + "SetPrintDlgPropertiesUsingPdfContentEditor_out.pdf");
}
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

