---
title: Menggunakan Anotasi Teks untuk PDF
linktitle: Anotasi Teks
type: docs
weight: 10
url: /net/text-annotation/
description: Aspose.PDF untuk .NET memungkinkan Anda untuk Menambahkan, Mengambil, dan Menghapus Anotasi Teks dari dokumen PDF Anda.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Menggunakan Anotasi Teks untuk PDF",
    "alternativeHeadline": "Cara menambahkan Anotasi Teks dalam PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, anotasi teks",
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
    "url": "/net/text-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF untuk .NET memungkinkan Anda untuk Menambahkan, Mengambil, dan Menghapus Anotasi Teks dari dokumen PDF Anda."
}
</script>

## Cara Menambahkan Anotasi Teks ke dalam File PDF yang Ada

Potongan kode berikut juga berfungsi dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

Anotasi Teks adalah anotasi yang dilampirkan pada lokasi tertentu dalam dokumen PDF. Ketika ditutup, anotasi ditampilkan sebagai ikon; ketika dibuka, seharusnya menampilkan jendela pop-up yang berisi teks catatan dalam font dan ukuran yang dipilih oleh pembaca.

Anotasi terkandung oleh koleksi [Annotations](https://reference.aspose.com/pdf/net/aspose.pdf.annotations) dari sebuah Halaman tertentu. Koleksi ini hanya berisi anotasi untuk halaman tersebut; setiap halaman memiliki koleksi Annotations sendiri.

Untuk menambahkan anotasi ke halaman tertentu, tambahkan ke koleksi Annotations halaman tersebut dengan metode [Add](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection/methods/add).

1. Pertama, buat anotasi yang ingin Anda tambahkan ke PDF.
1. Kemudian buka PDF masukan.
1.
Kode berikut menunjukkan cara menambahkan anotasi pada halaman PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "AddAnnotation.pdf");

// Buat anotasi
TextAnnotation textAnnotation = new TextAnnotation(pdfDocument.Pages[1], new Aspose.Pdf.Rectangle(200, 400, 400, 600));
textAnnotation.Title = "Judul Anotasi Contoh";
textAnnotation.Subject = "Subjek Contoh";
textAnnotation.State = AnnotationState.Accepted;
textAnnotation.Contents = "Isi contoh untuk anotasi";
textAnnotation.Open = true;
textAnnotation.Icon = TextIcon.Key;

Border border = new Border(textAnnotation);
border.Width = 5;
border.Dash = new Dash(1, 1);
textAnnotation.Border = border;
textAnnotation.Rect = new Aspose.Pdf.Rectangle(200, 400, 400, 600);

// Tambahkan anotasi dalam koleksi anotasi halaman
pdfDocument.Pages[1].Annotations.Add(textAnnotation);
dataDir = dataDir + "AddAnnotation_out.pdf";
// Simpan file keluaran
pdfDocument.Save(dataDir);
```
## Cara Menambahkan Anotasi Popup

Anotasi Popup menampilkan teks dalam jendela popup untuk entri dan pengeditan. Ini tidak boleh muncul sendiri tetapi harus dikaitkan dengan anotasi markup, anotasi induknya, dan harus digunakan untuk mengedit teks induk.

Ini tidak boleh memiliki aliran penampilan atau tindakan terkait sendiri dan harus diidentifikasi oleh entri Popup dalam kamus anotasi induk.

Potongan kode berikut menunjukkan cara menambahkan [Anotasi Popup](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/popupannotation) di halaman PDF menggunakan contoh menambahkan anotasi [Garis induk](/pdf/net/figures-annotation/#how-to-add-line-annotation-into-existing-pdf-file).

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.Linq;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleLineAnnotation
    {
        // Jalur ke direktori dokumen.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddLineAnnotation()
        {
            try
            {
                // Muat file PDF
                Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments.pdf"));

                // Buat Anotasi Garis
                var lineAnnotation = new LineAnnotation(
                    document.Pages[1],
                    new Rectangle(550, 93, 562, 439),
                    new Point(556, 99), new Point(556, 443))
                {
                    Title = "John Smith",
                    Color = Color.Red,
                    Width = 3,
                    StartingStyle = LineEnding.OpenArrow,
                    EndingStyle = LineEnding.OpenArrow,
                    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 124, 1021, 266))
                };

                // Tambahkan anotasi ke halaman
                document.Pages[1].Annotations.Add(lineAnnotation);
                document.Save(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
```
## Bagaimana Menambahkan (atau Membuat) Anotasi Teks Bebas Baru

Anotasi teks bebas menampilkan teks langsung di halaman. Metode [PdfContentEditor.CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) memungkinkan pembuatan jenis anotasi ini. Dalam potongan berikut, kami menambahkan anotasi teks bebas di atas kemunculan pertama dari string.

```csharp
private static void AddFreeTextAnnotationDemo()
{
    _document = new Document(@"C:\tmp\pdf-sample.pdf");
    var pdfContentEditor = new PdfContentEditor(_document);

    tfa.Visit(_document.Pages[1]);
    if (tfa.TextFragments.Count <= 0) return;
    var rect = new System.Drawing.Rectangle
    {
        X = (int)tfa.TextFragments[1].Rectangle.LLX,
        Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
        Height = 18,
        Width = 100
    };

    pdfContentEditor.CreateFreeText(rect, "Demo Teks Bebas", 1); // parameter terakhir adalah nomor halaman
    pdfContentEditor.Save(@"C:\tmp\pdf-sample-0.pdf");
}
```

### Atur Properti Callout untuk FreeTextAnnotation
### Atur Properti Callout untuk FreeTextAnnotation

Untuk konfigurasi yang lebih fleksibel dari anotasi dalam dokumen PDF, Aspose.PDF untuk .NET menyediakan properti [Callout](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation/properties/callout) dari kelas [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) yang memungkinkan penentuan Array dari titik garis callout. Cuplikan kode berikut menunjukkan, bagaimana menggunakan fungsionalitas ini:

```csharp
// Untuk contoh lengkap dan berkas data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Document doc = new Document();
Page page = doc.Pages.Add();
DefaultAppearance da = new DefaultAppearance();
da.TextColor = System.Drawing.Color.Red;
da.FontSize = 10;
FreeTextAnnotation fta = new FreeTextAnnotation(page, new Rectangle(422.25, 645.75, 583.5, 702.75), da);
fta.Intent = FreeTextIntent.FreeTextCallout;
fta.EndingStyle = LineEnding.OpenArrow;
fta.Callout = new Point[]
{
    new Point(428.25,651.75), new Point(462.75,681.375), new Point(474,681.375)
};
page.Annotations.Add(fta);
fta.RichText = "<body xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:xfa=\"http://www.xfa.org/schema/xfa-data/1.0/\" xfa:APIVersion=\"Acrobat:11.0.23\" xfa:spec=\"2.0.2\"  style=\"color:#FF0000;font-weight:normal;font-style:normal;font-stretch:normal\"><p dir=\"ltr\"><span style=\"font-size:9.0pt;font-family:Helvetica\">Ini adalah contoh</span></p></body>";
doc.Save(dataDir + "SetCalloutProperty.pdf");
```
### Atur Properti Callout untuk File XFDF

Jika Anda menggunakan impor dari file XFDF, silakan gunakan nama callout-line daripada hanya Callout. Potongan kode berikut menunjukkan, bagaimana menggunakan fungsi ini:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
Document pdfDocument = new Document(dataDir + "AddAnnotation.pdf");
StringBuilder Xfdf = new StringBuilder();
Xfdf.AppendLine("<?xml version=\"1.0\" encoding=\"UTF-8\"?><xfdf xmlns=\"http://ns.adobe.com/xfdf/\" xml:space=\"preserve\"><annots>");
CreateXfdf(ref Xfdf);
Xfdf.AppendLine("</annots></xfdf>");
pdfDocument.ImportAnnotationsFromXfdf(new MemoryStream(Encoding.UTF8.GetBytes(Xfdf.ToString())));
pdfDocument.Save(dataDir + "SetCalloutPropertyXFDF.pdf");
```

Metode berikut digunakan untuk CreateXfdf:

```csharp
/// <summary>
/// Buat XFDF
/// </summary>
/// <param name="pXfdf"></param>

static void CreateXfdf(ref StringBuilder pXfdf)
{
    pXfdf.Append("<freetext");
    pXfdf.Append(" page=\"0\"");
    pXfdf.Append(" rect=\"422.25,645.75,583.5,702.75\"");
    pXfdf.Append(" intent=\"FreeTextCallout\"");
    pXfdf.Append(" callout-line=\"428.25,651.75,462.75,681.375,474,681.375\"");
    pXfdf.Append(" tail=\"OpenArrow\"");
    pXfdf.AppendLine(">");
    pXfdf.Append("<contents-richtext><body ");
    pXfdf.Append(" style=\"font-size:10.0pt;text-align:left;color:#FF0000;font-weight:normal;font-style:normal;font-family:Helvetica;font-stretch:normal\">");
    pXfdf.Append("<p dir=\"ltr\">Ini adalah contoh</p>");
    pXfdf.Append("</body></contents-richtext>");
    pXfdf.AppendLine("<defaultappearance>/Helv 12 Tf 1 0 0 rg</defaultappearance>");
    pXfdf.AppendLine("</freetext>");
}
```
### Membuat Anotasi Teks Bebas Menjadi Tidak Terlihat

Terkadang, diperlukan untuk membuat watermark yang tidak terlihat dalam dokumen saat dilihat tetapi harus terlihat saat dokumen dicetak. Gunakan bendera anotasi untuk tujuan ini. Cuplikan kode berikut menunjukkan caranya.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Buka dokumen
Document doc = new Document(dataDir + "input.pdf");

FreeTextAnnotation annotation = new FreeTextAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(50, 600, 250, 650), new DefaultAppearance("Helvetica", 16, System.Drawing.Color.Red));
annotation.Contents = "ABCDEFG";
annotation.Characteristics.Border = System.Drawing.Color.Red;
annotation.Flags = AnnotationFlags.Print | AnnotationFlags.NoView;
doc.Pages[1].Annotations.Add(annotation);

dataDir = dataDir + "InvisibleAnnotation_out.pdf";
// Simpan file keluaran
doc.Save(dataDir);
```
### Mengatur Format Teks pada FreeTextAnnotation

Bagian ini membahas cara memformat teks dalam anotasi teks bebas.

Anotasi terdapat dalam koleksi [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) dari objek [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page). Saat menambahkan [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) ke dalam dokumen PDF, Anda dapat menentukan informasi format seperti font, ukuran, warna, dan sebagainya menggunakan kelas [DefaultAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/defaultappearance/methods/index). Anda juga dapat menentukan informasi format menggunakan properti TextStyle. Selain itu, Anda dapat memperbarui format dari FreeTextAnnotation yang sudah ada dalam dokumen PDF.

Kelas [TextStyle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/textstyle) mendukung kerja dengan entri gaya default.
Kelas [TextStyle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/textstyle) mendukung penggunaan entri gaya default.

- Properti FontName mendapatkan atau mengatur nama font (string).
- Properti FontSize mendapatkan dan mengatur ukuran teks default (double).
- Properti System.Drawing.Color mendapatkan dan mengatur warna teks (color).
- Properti TextAlignment mendapatkan dan mengatur penyelarasan teks anotasi (alignment).

Potongan kode berikut menunjukkan cara menambahkan FreeTextAnnotation dengan format teks tertentu.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Annotations-SetFreeTextAnnotationFormatting-SetFreeTextAnnotationFormatting.cs" >}}

{{% alert color="primary" %}}

Ketika Anda mengubah isi atau gaya teks dari anotasi teks bebas, tampilan anotasi diregenerasi untuk mencerminkan perubahan.

{{% /alert %}}

### Coret Kata menggunakan StrikeOutAnnotation

Aspose.PDF untuk .NET memungkinkan Anda menambah, menghapus, dan memperbarui anotasi dalam dokumen PDF.
Aspose.PDF for .NET memungkinkan Anda untuk menambah, menghapus, dan memperbarui anotasi dalam dokumen PDF.

Untuk mencoret TextFragment tertentu:

1. Cari TextFragment dalam file PDF.
1. Dapatkan koordinat objek TextFragment.
1. Gunakan koordinat untuk menginstansiasi objek StrikeOutAnnotation.

Potongan kode berikut menunjukkan cara mencari TextFragment tertentu dan menambahkan StrikeOutAnnotation ke objek tersebut.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Annotations-StrikeOutWords-StrikeOutWords.cs" >}}

{{% alert color="primary" %}}

Fitur ini didukung oleh versi 19.6 atau lebih tinggi.

{{% /alert %}}

## Hapus Semua Anotasi dari Halaman File PDF

Koleksi [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) dari objek [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) berisi semua anotasi untuk halaman tersebut.
Koleksi [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) dari objek [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) berisi semua anotasi untuk halaman tersebut.

Berikut adalah cuplikan kode yang menunjukkan cara menghapus semua anotasi dari halaman tertentu.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "DeleteAllAnnotationsFromPage.pdf");

// Hapus anotasi tertentu
pdfDocument.Pages[1].Annotations.Delete();

dataDir = dataDir + "DeleteAllAnnotationsFromPage_out.pdf";
// Simpan dokumen yang telah diperbarui
pdfDocument.Save(dataDir);
```

## Hapus Anotasi Tertentu dari File PDF

{{% alert color="primary" %}}

Anda dapat memeriksa kualitas Aspose.PDF dan mendapatkan hasil secara online di tautan ini:
[products.aspose.app/pdf/annotation](https://products.aspose.app/pdf/annotation)
[products.aspose.app/pdf/annotation](https://products.aspose.app/pdf/annotation)

{{% /alert %}}

Aspose.PDF memungkinkan Anda untuk menghapus Anotasi tertentu dari file PDF. Topik ini menjelaskan caranya.

Untuk menghapus anotasi tertentu dari PDF, panggil [metode Delete dari kumpulan AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations.annotationcollection/delete/methods/1). Koleksi ini merupakan bagian dari objek [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page). Metode Delete memerlukan indeks dari anotasi yang ingin Anda hapus. Kemudian, simpan file PDF yang telah diperbarui. Cuplikan kode berikut menunjukkan cara menghapus anotasi tertentu.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "DeleteParticularAnnotation.pdf");

// Hapus anotasi tertentu
pdfDocument.Pages[1].Annotations.Delete(1);

dataDir = dataDir + "DeleteParticularAnnotation_out.pdf";
// Simpan dokumen yang diperbarui
pdfDocument.Save(dataDir);
```

## Dapatkan Semua Anotasi dari Halaman Dokumen PDF

Aspose.PDF memungkinkan Anda untuk mendapatkan anotasi dari seluruh dokumen, atau dari halaman tertentu. Untuk mendapatkan semua anotasi dari halaman dalam dokumen PDF, lakukan perulangan melalui koleksi [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) dari sumber halaman yang diinginkan. Cuplikan kode berikut menunjukkan cara mendapatkan semua anotasi dari sebuah halaman.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "GetAllAnnotationsFromPage.pdf");

// Lakukan perulangan melalui semua anotasi
foreach (MarkupAnnotation annotation in pdfDocument.Pages[1].Annotations)
{
    // Dapatkan properti anotasi
    Console.WriteLine("Judul : {0} ", annotation.Title);
    Console.WriteLine("Subjek : {0} ", annotation.Subject);
    Console.WriteLine("Konten : {0} ", annotation.Contents);
}
```
Harap diperhatikan bahwa untuk mendapatkan semua anotasi dari seluruh PDF, Anda harus melakukan perulangan melalui koleksi kelas PageCollection dari dokumen sebelum menavigasi melalui koleksi kelas AnnotationCollection. Anda dapat mendapatkan setiap anotasi dari koleksi tersebut dalam tipe dasar anotasi yang disebut kelas MarkupAnnotation dan kemudian menampilkan propertinya.

## Dapatkan Anotasi Tertentu dari File PDF

Anotasi terkait dengan halaman individu dan disimpan dalam koleksi [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) dari objek [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
Anotasi terkait dengan halaman individu dan disimpan dalam koleksi [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) dari objek [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "GetParticularAnnotation.pdf");

// Dapatkan anotasi tertentu
TextAnnotation textAnnotation = (TextAnnotation)pdfDocument.Pages[1].Annotations[1];

// Dapatkan properti anotasi
Console.WriteLine("Judul : {0} ", textAnnotation.Title);
Console.WriteLine("Subjek : {0} ", textAnnotation.Subject);
Console.WriteLine("Isi : {0} ", textAnnotation.Contents);
```

## Dapatkan Sumber Anotasi

Aspose.PDF memungkinkan Anda untuk mendapatkan sumber anotasi dari seluruh dokumen, atau dari halaman tertentu.
Aspose.PDF memungkinkan Anda untuk mendapatkan sumber daya anotasi dari seluruh dokumen, atau dari halaman tertentu.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Buka dokumen
Document doc = new Document(dataDir + "AddAnnotation.pdf");
//Buat anotasi
ScreenAnnotation sa = new ScreenAnnotation(doc.Pages[1], new Rectangle(100, 400, 300, 600), dataDir + "AddSwfFileAsAnnotation.swf");
doc.Pages[1].Annotations.Add(sa);
// Simpan Dokumen
doc.Save(dataDir + "GetResourceOfAnnotation_Out.pdf");

// Buka dokumen
Document doc1 = new Document(dataDir + "GetResourceOfAnnotation_Out.pdf");

//Dapatkan aksi dari anotasi
RenditionAction action = (doc.Pages[1].Annotations[1] as ScreenAnnotation).Action as RenditionAction;

//Dapatkan perwujudan dari aksi perwujudan
Rendition rendition = ((doc.Pages[1].Annotations[1] as ScreenAnnotation).Action as RenditionAction).Rendition;

//Klip Media
MediaClip clip = (rendition as MediaRendition).MediaClip;
FileSpecification data = (clip as MediaClipData).Data;
MemoryStream ms = new MemoryStream();
byte[] buffer = new byte[1024];
int read = 0;
//Data media dapat diakses di FileSpecification.Contents
Stream source = data.Contents;
while ((read = source.Read(buffer, 0, buffer.Length)) > 0)
{
    ms.Write(buffer, 0, read);
}
Console.WriteLine(rendition.Name);
Console.WriteLine(action.RenditionOperation);
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

