---
title: Pemformatan Teks di Dalam PDF Menggunakan C#
linktitle: Pemformatan Teks di Dalam PDF
type: docs
weight: 30
url: /net/text-formatting-inside-pdf/
description: Halaman ini menjelaskan cara memformat teks di dalam file PDF Anda. Ada penambahan indentasi baris, penambahan batas teks, penambahan teks bergaris bawah, dan lain-lain.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Pemformatan Teks di Dalam PDF Menggunakan C#",
    "alternativeHeadline": "Cara memformat teks di dalam file PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, memformat teks di pdf",
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
    "url": "/net/text-formatting-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-formatting-inside-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Halaman ini menjelaskan cara memformat teks di dalam file PDF Anda. Ada penambahan indentasi baris, penambahan batas teks, penambahan teks bergaris bawah, dan lain-lain."
}
</script>

Kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Cara Menambahkan Indentasi Baris ke PDF

Aspose.PDF untuk .NET menawarkan properti SubsequentLinesIndent ke dalam kelas [TextFormattingOptions](https://reference.aspose.com/pdf/net/aspose.pdf.text/textformattingoptions). Yang dapat digunakan untuk menentukan indentasi baris dalam skenario pembuatan PDF dengan koleksi TextFragment dan Paragraphs.

Silakan gunakan kode berikut untuk menggunakan properti tersebut:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Buat objek dokumen baru
Aspose.Pdf.Document document = new Aspose.Pdf.Document();
Aspose.Pdf.Page page = document.Pages.Add();

string textFragment = string.Concat(Enumerable.Repeat("Seekor rubah cepat melompati anjing malas. ", 10));

Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment(textFragment);

// Inisialisasi TextFormattingOptions untuk fragmen teks dan tentukan nilai SubsequentLinesIndent
text.TextState.FormattingOptions = new Aspose.Pdf.Text.TextFormattingOptions()
{
    SubsequentLinesIndent = 20
};

page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Baris2");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Baris3");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Baris4");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Baris5");
page.Paragraphs.Add(text);

document.Save(dataDir + "SubsequentIndent_out.pdf");
```
## Cara Menambahkan Tepi Teks

Potongan kode berikut menunjukkan cara menambahkan border pada teks menggunakan TextBuilder dan mengatur properti DrawTextRectangleBorder dari TextState:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Buat objek dokumen baru
Document pdfDocument = new Document();
// Dapatkan halaman tertentu
Page pdfPage = (Page)pdfDocument.Pages.Add();
// Buat fragmen teks
TextFragment textFragment = new TextFragment("teks utama");
textFragment.Position = new Position(100, 600);
// Atur properti teks
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
// Atur properti StrokingColor untuk menggambar border (stroking) di sekitar kotak teks
textFragment.TextState.StrokingColor = Aspose.Pdf.Color.DarkRed;
// Atur nilai properti DrawTextRectangleBorder menjadi true
textFragment.TextState.DrawTextRectangleBorder = true;
TextBuilder tb = new TextBuilder(pdfPage);
tb.AppendText(textFragment);
// Simpan dokumen
pdfDocument.Save(dataDir + "PDFWithTextBorder_out.pdf");
```
## Cara Menambahkan Teks Bergaris Bawah

Potongan kode berikut menunjukkan cara menambahkan teks bergaris bawah saat membuat file PDF baru.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Buat objek dokumentasi
Document pdfDocument = new Document();
// Tambahkan halaman ke dokumen PDF
pdfDocument.Pages.Add();
// Buat TextBuilder untuk halaman pertama
TextBuilder tb = new TextBuilder(pdfDocument.Pages[1]);
// TextFragment dengan teks contoh
TextFragment fragment = new TextFragment("Pesan tes");
// Atur font untuk TextFragment
fragment.TextState.Font = FontRepository.FindFont("Arial");
fragment.TextState.FontSize = 10;
// Atur format teks sebagai Bergaris Bawah
fragment.TextState.Underline = true;
// Tentukan posisi di mana TextFragment harus ditempatkan
fragment.Position = new Position(10, 800);
// Tambahkan TextFragment ke file PDF
tb.AppendText(fragment);

dataDir = dataDir + "AddUnderlineText_out.pdf";

// Simpan dokumen PDF yang dihasilkan.
pdfDocument.Save(dataDir);
```
## Cara Menambahkan Garis Tepi pada Teks yang Ditambahkan

Anda memiliki kontrol atas tampilan dan nuansa teks yang Anda tambahkan. Contoh di bawah ini menunjukkan cara menambahkan garis tepi pada sepotong teks yang telah Anda tambahkan dengan menggambar persegi panjang di sekitarnya. Pelajari lebih lanjut tentang kelas [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor).

```csharp
// Untuk contoh lengkap dan berkas data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

PdfContentEditor editor = new PdfContentEditor();
editor.BindPdf(dataDir + "input.pdf");
LineInfo lineInfo = new LineInfo();
lineInfo.LineWidth = 2;
lineInfo.VerticeCoordinate = new float[] { 0, 0, 100, 100, 50, 100 };
lineInfo.Visibility = true;
editor.CreatePolygon(lineInfo, 1, new System.Drawing.Rectangle(0, 0, 0, 0), "");

dataDir = dataDir + "AddingBorderAroundAddedText_out.pdf";

// Simpan dokumen PDF yang dihasilkan.
editor.Save(dataDir);
```

## Cara Menambahkan Umpan Baris Baru
## Cara Menambahkan Umpan Baris Baru

TextFragment tidak mendukung umpan baris di dalam teks. Namun, untuk menambahkan teks dengan umpan baris, silakan gunakan TextFragment dengan TextParagraph:

- gunakan "\r\n" atau Environment.NewLine di TextFragment bukan "\n" tunggal;
- buat objek TextParagraph. Ini akan menambahkan teks dengan pemisahan baris;
- tambahkan TextFragment dengan TextParagraph.AppendLine;
- tambahkan TextParagraph dengan TextBuilder.AppendParagraph.
Silakan gunakan potongan kode di bawah ini.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// Inisialisasi TextFragment baru dengan teks yang mengandung penanda baris baru yang diperlukan
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Nama Pelamar: " + Environment.NewLine + " Joe Smoe");

// Atur properti fragmen teks jika perlu
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// Buat objek TextParagraph
TextParagraph par = new TextParagraph();

// Tambahkan TextFragment baru ke paragraf
par.AppendLine(textFragment);

// Atur posisi paragraf
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// Buat objek TextBuilder
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// Tambahkan TextParagraph menggunakan TextBuilder
textBuilder.AppendParagraph(par);

dataDir = dataDir + "AddNewLineFeed_out.pdf";

// Simpan dokumen PDF hasilnya.
pdfApplicationDoc.Save(dataDir);
```
## Cara Menambahkan Teks Coretan

Kelas TextState menyediakan kemampuan untuk mengatur format teks pada TextFragments yang ditempatkan di dalam dokumen PDF. Anda dapat menggunakan kelas ini untuk mengatur format teks seperti Bold, Italic, Underline dan mulai rilis ini, API telah menyediakan kemampuan untuk menandai format teks sebagai Coretan. Silakan coba gunakan cuplikan kode berikut untuk menambahkan TextFragment dengan format Coretan.

Silakan gunakan cuplikan kode lengkap:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Buka dokumen
Document pdfDocument = new Document();
// Dapatkan halaman tertentu
Page pdfPage = (Page)pdfDocument.Pages.Add();

// Buat fragmen teks
TextFragment textFragment = new TextFragment("teks utama");
textFragment.Position = new Position(100, 600);

// Atur properti teks
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
// Atur properti Coretan
textFragment.TextState.StrikeOut = true;
// Tandai teks sebagai Bold
textFragment.TextState.FontStyle = FontStyles.Bold;

// Buat objek TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);
// Tambahkan fragmen teks ke halaman PDF
textBuilder.AppendText(textFragment);


dataDir = dataDir + "AddStrikeOutText_out.pdf";

// Simpan dokumen PDF yang dihasilkan.
pdfDocument.Save(dataDir);
```
## Terapkan Bayangan Gradien pada Teks

Pemformatan teks telah ditingkatkan lebih lanjut dalam API untuk skenario pengeditan teks dan sekarang Anda dapat menambahkan teks dengan ruang warna pola di dalam dokumen PDF. Kelas Aspose.Pdf.Color telah ditingkatkan lebih lanjut dengan memperkenalkan properti baru dari PatternColorSpace, yang dapat digunakan untuk menentukan warna bayangan untuk teks. Properti baru ini menambahkan Bayangan Gradien yang berbeda pada teks misalnya Bayangan Aksial, Bayangan Radial (Tipe 3) seperti yang ditunjukkan pada cuplikan kode berikut:

```csharp
// Untuk contoh lengkap dan berkas data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

using (Document pdfDocument = new Document(dataDir + "text_sample4.pdf"))
{
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("Lorem ipsum");
    pdfDocument.Pages.Accept(absorber);

    TextFragment textFragment = absorber.TextFragments[1];

    // Buat warna baru dengan ruang warna pola
    textFragment.TextState.ForegroundColor = new Aspose.Pdf.Color()
    {
        PatternColorSpace = new Aspose.Pdf.Drawing.GradientAxialShading(Color.Red, Color.Blue)
    };
    textFragment.TextState.Underline = true;

    pdfDocument.Save(dataDir + "text_out.pdf");
}
```
>Untuk menerapkan Gradient Radial, Anda dapat mengatur properti 'PatternColorSpace' sama dengan 'Aspose.Pdf.Drawing.GradientRadialShading(warnaAwal, warnaAkhir)' pada potongan kode di atas.

## Cara mengatur teks agar sejajar dengan konten mengambang

Aspose.PDF mendukung pengaturan penjajaran teks untuk konten di dalam elemen Floating Box. Properti penjajaran dari instansi Aspose.Pdf.FloatingBox dapat digunakan untuk mencapai ini seperti yang ditunjukkan pada contoh kode berikut.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Document doc = new Document();
doc.Pages.Add();

Aspose.Pdf.FloatingBox floatBox = new Aspose.Pdf.FloatingBox(100, 100);
floatBox.VerticalAlignment = VerticalAlignment.Bottom;
floatBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox.Paragraphs.Add(new TextFragment("FloatingBox_bottom"));
floatBox.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox);

Aspose.Pdf.FloatingBox floatBox1 = new Aspose.Pdf.FloatingBox(100, 100);
floatBox1.VerticalAlignment = VerticalAlignment.Center;
floatBox1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox1.Paragraphs.Add(new TextFragment("FloatingBox_center"));
floatBox1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox1);

Aspose.Pdf.FloatingBox floatBox2 = new Aspose.Pdf.FloatingBox(100, 100);
floatBox2.VerticalAlignment = VerticalAlignment.Top;
floatBox2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox2.Paragraphs.Add(new TextFragment("FloatingBox_top"));
floatBox2.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox2);

doc.Save(dataDir + "FloatingBox_alignment_review_out.pdf");
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

