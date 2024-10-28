---
title: Membuat PDF Bertag menggunakan C#
linktitle: Membuat PDF Bertag
type: docs
weight: 10
url: /net/create-tagged-pdf/
description: Artikel ini menjelaskan bagaimana cara membuat elemen struktur untuk dokumen PDF Bertag secara pemrograman menggunakan Aspose.PDF untuk .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Membuat PDF Bertag menggunakan C#",
    "alternativeHeadline": "Cara membuat PDF Bertag",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "membuat, bertag, pdf",
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
    "url": "/net/create-tagged-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-tagged-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Artikel ini menjelaskan bagaimana cara membuat elemen struktur untuk dokumen PDF Bertag secara pemrograman menggunakan Aspose.PDF untuk .NET."
}
</script>

Membuat PDF Bertag berarti menambahkan (atau menciptakan) elemen-elemen tertentu ke dalam dokumen yang akan memungkinkan dokumen untuk divalidasi sesuai dengan persyaratan PDF/UA. Elemen-elemen ini sering disebut sebagai Elemen Struktur.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Membuat PDF Bertag (Skenario Sederhana)

Untuk membuat elemen struktur dalam Dokumen PDF Bertag, Aspose.PDF menawarkan metode untuk membuat elemen struktur menggunakan antarmuka [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent). Potongan kode berikut menunjukkan cara membuat PDF Bertag yang mengandung 2 elemen: header dan paragraf.

```csharp
private static void CreateTaggedPdfDocument01()
{
    // Membuat Dokumen PDF
    var document = new Document();

    // Dapatkan Konten untuk bekerja dengan TaggedPdf
    ITaggedContent taggedContent = document.TaggedContent;
    var rootElement = taggedContent.RootElement;
    // Tetapkan Judul dan Bahasa untuk Dokumen
    taggedContent.SetTitle("Dokumen PDF Bertag");
    taggedContent.SetLanguage("en-US");

    // 
    HeaderElement mainHeader = taggedContent.CreateHeaderElement();
    mainHeader.SetText("Header Utama");

    ParagraphElement paragraphElement = taggedContent.CreateParagraphElement();
    paragraphElement.SetText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. " +
    "Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. " +
    "Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet" +
    "nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus." +
    "Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat" +
    "sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper" +
    "pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus" +
    "ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus," +
    "ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");

    rootElement.AppendChild(mainHeader);
    rootElement.AppendChild(paragraphElement);

    // Simpan Dokumen PDF Bertag
    document.Save("C:\\Samples\\TaggedPDF\\Sample1.pdf");
}
```
Kami akan mendapatkan dokumen berikut setelah penciptaan:

![Dokumen PDF Bertanda dengan 2 elemen - Header dan Paragraf](taggedpdf-01.png)

## Membuat PDF Bertanda dengan elemen bersarang (Membuat Struktur Pohon Elemen)

Dalam beberapa kasus, kita perlu membuat struktur yang lebih kompleks, misalnya, menempatkan kutipan dalam paragraf.
Untuk membuat pohon elemen struktur kita harus menggunakan metode [AppendChild](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/element/methods/appendchild).
Potongan kode berikut menunjukkan cara membuat pohon elemen struktur Dokumen PDF Bertanda:

```csharp
private static void CreateTaggedPdfDocument02()
{
    // Membuat Dokumen Pdf
    var document = new Document();

    // Mendapatkan Konten untuk bekerja dengan TaggedPdf
    ITaggedContent taggedContent = document.TaggedContent;
    var rootElement = taggedContent.RootElement;
    // Menetapkan Judul dan Bahasa untuk Dokumen
    taggedContent.SetTitle("Dokumen Pdf Bertanda");
    taggedContent.SetLanguage("en-US");

    HeaderElement header1 = taggedContent.CreateHeaderElement(1);
    header1.SetText("Header Level 1");

    ParagraphElement paragraphWithQuotes = taggedContent.CreateParagraphElement();
    paragraphWithQuotes.StructureTextState.Font = FontRepository.FindFont("Calibri");
    paragraphWithQuotes.StructureTextState.MarginInfo = new MarginInfo(10, 5, 10, 5);

    SpanElement spanElement1 = taggedContent.CreateSpanElement();
    spanElement1.SetText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. ");
    QuoteElement quoteElement = taggedContent.CreateQuoteElement();
    quoteElement.SetText("Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa.");
    quoteElement.StructureTextState.FontStyle = FontStyles.Bold | FontStyles.Italic;
    SpanElement spanElement2 = taggedContent.CreateSpanElement();
    spanElement2.SetText(" Sed non consectetur elit.");

    paragraphWithQuotes.AppendChild(spanElement1);
    paragraphWithQuotes.AppendChild(quoteElement);
    paragraphWithQuotes.AppendChild(spanElement2);

    rootElement.AppendChild(header1);
    rootElement.AppendChild(paragraphWithQuotes);

    // Menyimpan Dokumen Pdf Bertanda
    document.Save("C:\\Samples\\TaggedPDF\\Sample2.pdf");
}
```
Kami akan mendapatkan dokumen berikut setelah pembuatan:
![Dokumen PDF Bertanda dengan elemen bersarang - span dan kutipan](taggedpdf-02.png)

## Struktur Teks Gaya

Untuk mengatur struktur teks dalam Dokumen PDF Bertanda, Aspose.PDF menawarkan properti [Font](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/font), [FontSize](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/fontsize), [FontStyle](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/fontstyle), dan [ForegroundColor](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/foregroundcolor) dari Kelas [StructureTextState](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate). Cuplikan kode berikut menunjukkan cara mengatur struktur teks dalam Dokumen PDF Bertanda:

```csharp
// Untuk contoh lengkap dan file data, silahkan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Buat Dokumen Pdf
Document document = new Document();

// Dapatkan Konten untuk bekerja dengan TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Atur Judul dan Bahasa untuk Dokumen
taggedContent.SetTitle("Dokumen Pdf Bertanda");
taggedContent.SetLanguage("en-US");

ParagraphElement p = taggedContent.CreateParagraphElement();
taggedContent.RootElement.AppendChild(p);

// Dalam Pengembangan
p.StructureTextState.FontSize = 18F;
p.StructureTextState.ForegroundColor = Color.Red;
p.StructureTextState.FontStyle = FontStyles.Italic;

p.SetText("Teks miring merah.");

// Simpan Dokumen Pdf Bertanda
document.Save(dataDir + "StyleTextStructure.pdf");
```
## Menggambarkan Elemen Struktur

Untuk menggambarkan elemen struktur dalam Dokumen PDF Bertag, Aspose.PDF menawarkan kelas [IllustrationElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/illustrationelement). Cuplikan kode berikut menunjukkan cara menggambarkan elemen struktur dalam Dokumen PDF Bertag:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Path ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Membuat Dokumen Pdf
Document document = new Document();

// Mendapatkan Konten untuk bekerja dengan TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Mengatur Judul dan Bahasa untuk Dokumen
taggedContent.SetTitle("Dokumen Pdf Bertag");
taggedContent.SetLanguage("en-US");

// Dalam Pengembangan
IllustrationElement figure1 = taggedContent.CreateFigureElement();
taggedContent.RootElement.AppendChild(figure1);
figure1.AlternativeText = "Gambar Satu";
figure1.Title = "Gambar 1";
figure1.SetTag("Fig1");
figure1.SetImage("image.png");

// Menyimpan Dokumen Pdf Bertag
document.Save(dataDir + "IllustrationStructureElements.pdf");

```
## Validasi PDF Bertag

Aspose.PDF untuk .NET menyediakan kemampuan untuk memvalidasi Dokumen PDF/UA Bertag. Validasi standar PDF/UA mendukung:

- Pemeriksaan untuk XObjects
- Pemeriksaan untuk Aksi
- Pemeriksaan untuk Konten Opsional
- Pemeriksaan untuk File yang Tersemat
- Pemeriksaan untuk Bidang Acroform (Memvalidasi Bahasa Alami dan Nama Alternatif serta Tanda Tangan Digital)
- Pemeriksaan untuk Bidang Formulir XFA
- Pemeriksaan untuk Pengaturan Keamanan
- Pemeriksaan untuk Navigasi
- Pemeriksaan untuk Anotasi

Potongan kode di bawah ini menunjukkan cara memvalidasi Dokumen PDF Bertag. Masalah yang sesuai akan ditampilkan dalam laporan log XML.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string inputFileName = dataDir + "StructureElements.pdf";
string outputLogName = dataDir + "ua-20.xml";

using (var document = new Aspose.Pdf.Document(inputFileName))
{
    bool isValid = document.Validate(outputLogName, Aspose.Pdf.PdfFormat.PDF_UA_1);

}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF untuk .NET Library",
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

