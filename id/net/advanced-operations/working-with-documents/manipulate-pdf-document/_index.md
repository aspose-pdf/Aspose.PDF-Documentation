---
title: Manipulasi Dokumen PDF di C#
linktitle: Manipulasi Dokumen PDF
type: docs
weight: 20
url: /id/net/manipulate-pdf-document/
description: Artikel ini berisi informasi tentang cara memvalidasi Dokumen PDF untuk Standar PDF A, cara bekerja dengan TOC, cara mengatur tanggal kedaluwarsa PDF, dan lainnya.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipulasi Dokumen PDF",
    "alternativeHeadline": "Cara memanipulasi file PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, dotnet, memanipulasi file pdf",
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
    "url": "/net/manipulate-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Artikel ini berisi informasi tentang cara memvalidasi Dokumen PDF untuk Standar PDF A, cara bekerja dengan TOC, cara mengatur tanggal kedaluwarsa PDF, dan lainnya."
}
</script>
## **Memanipulasi Dokumen PDF dalam C#**

## Validasi Dokumen PDF untuk Standar PDF A (A 1A dan A 1B)

Untuk memvalidasi dokumen PDF agar sesuai dengan kompatibilitas PDF/A-1a atau PDF/A-1b, gunakan metode Validate dari kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Metode ini memungkinkan Anda untuk menentukan nama file tempat hasil akan disimpan dan tipe validasi yang dibutuhkan dari enumerasi [PdfFormat](https://reference.aspose.com/pdf/net/aspose.pdf/pdfformat) : PDF_A_1A atau PDF_A_1B.

{{% alert color="primary" %}}

Format XML keluaran adalah format khusus Aspose. XML ini berisi kumpulan tag dengan nama Problem; setiap tag berisi detail dari masalah tertentu. Atribut ObjectID dari tag Problem mewakili ID dari objek tertentu yang terkait dengan masalah ini. Atribut Clause mewakili aturan yang sesuai dalam spesifikasi PDF.

{{% /alert %}}

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

Potongan kode berikut menunjukkan cara memvalidasi dokumen PDF untuk PDF/A-1A.
Potongan kode berikut menunjukkan cara memvalidasi dokumen PDF untuk PDF/A-1A.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "ValidatePDFAStandard.pdf");

// Validasi PDF untuk PDF/A-1a
pdfDocument.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1A);
```

Potongan kode berikut menunjukkan cara memvalidasi dokumen PDF untuk PDF/A-1b.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "ValidatePDFAStandard.pdf");

// Validasi PDF untuk PDF/A-1b
pdfDocument.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1B);
```
{{% alert color="primary" %}}

Aspose.PDF untuk .NET dapat digunakan untuk menentukan apakah dokumen yang dimuat adalah PDF yang valid serta [apakah ia terenkripsi atau tidak](https://docs.aspose.com/pdf/net/set-privileges-encrypt-and-decrypt-pdf-file/). Untuk memperluas kemampuan kelas Dokumen, properti *IsPdfaCompliant* ditambahkan untuk menentukan apakah file masukan mematuhi PDF/A dan properti yang bernama *PdfaFormat* untuk mengidentifikasi format PDF/A diperkenalkan.

{{% /alert %}}

## Bekerja dengan TOC

### Menambahkan TOC ke PDF yang Ada

API Aspose.PDF memungkinkan Anda menambahkan daftar isi baik saat membuat PDF, maupun ke file yang sudah ada. Kelas ListSection dalam namespace Aspose.Pdf.Generator memungkinkan Anda untuk membuat daftar isi saat membuat PDF dari awal. Untuk menambahkan judul, yang merupakan elemen dari TOC, gunakan kelas Aspose.Pdf.Generator.Heading.

Untuk menambahkan TOC ke file PDF yang sudah ada, gunakan kelas Heading dalam namespace Aspose.Pdf.
Untuk menambahkan TOC ke file PDF yang sudah ada, gunakan kelas Heading di namespace Aspose.Pdf.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Muat file PDF yang sudah ada
Document doc = new Document(dataDir + "AddTOC.pdf");

// Dapatkan akses ke halaman pertama file PDF
Page tocPage = doc.Pages.Insert(1);

// Buat objek untuk mewakili informasi TOC
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("Daftar Isi");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;

// Tetapkan judul untuk TOC
tocInfo.Title = title;
tocPage.TocInfo = tocInfo;

// Buat objek string yang akan digunakan sebagai elemen TOC
string[] titles = new string[4];
titles[0] = "Halaman pertama";
titles[1] = "Halaman kedua";
titles[2] = "Halaman ketiga";
titles[3] = "Halaman keempat";
for (int i = 0; i < 2; i++)
{
    // Buat objek Heading
    Aspose.Pdf.Heading heading2 = new Aspose.Pdf.Heading(1);
    TextSegment segment2 = new TextSegment();
    heading2.TocPage = tocPage;
    heading2.Segments.Add(segment2);

    // Tentukan halaman tujuan untuk objek heading
    heading2.DestinationPage = doc.Pages[i + 2];

    // Halaman tujuan
    heading2.Top = doc.Pages[i + 2].Rect.Height;

    // Koordinat tujuan
    segment2.Text = titles[i];

    // Tambahkan heading ke halaman yang berisi TOC
    tocPage.Paragraphs.Add(heading2);
}
dataDir = dataDir + "TOC_out.pdf";
// Simpan dokumen yang telah diperbarui
doc.Save(dataDir);
```
### Mengatur TabLeaderType yang Berbeda untuk Berbagai Level TOC

Aspose.PDF juga memungkinkan pengaturan TabLeaderType yang berbeda untuk berbagai level TOC. Anda perlu mengatur properti LineDash dari FormatArray dengan nilai yang sesuai dari enum TabLeaderType sebagai berikut.

```csharp
string outFile = "TOC.pdf";

Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
Page tocPage = doc.Pages.Add();
TocInfo tocInfo = new TocInfo();

//set LeaderType
tocInfo.LineDash = TabLeaderType.Solid;
TextFragment title = new TextFragment("Daftar Isi");
title.TextState.FontSize = 30;
tocInfo.Title = title;

//Tambahkan bagian daftar ke koleksi bagian dari dokumen Pdf
tocPage.TocInfo = tocInfo;
//Tentukan format dari empat level daftar dengan mengatur margin kiri
//dan
//pengaturan format teks dari setiap level

tocInfo.FormatArrayLength = 4;
tocInfo.FormatArray[0].Margin.Left = 0;
tocInfo.FormatArray[0].Margin.Right = 30;
tocInfo.FormatArray[0].LineDash = TabLeaderType.Dot;
tocInfo.FormatArray[0].TextState.FontStyle = FontStyles.Bold | FontStyles.Italic;
tocInfo.FormatArray[1].Margin.Left = 10;
tocInfo.FormatArray[1].Margin.Right = 30;
tocInfo.FormatArray[1].LineDash = TabLeaderType.None;
tocInfo.FormatArray[1].TextState.FontSize = 10;
tocInfo.FormatArray[2].Margin.Left = 20;
tocInfo.FormatArray[2].Margin.Right = 30;
tocInfo.FormatArray[2].TextState.FontStyle = FontStyles.Bold;
tocInfo.FormatArray[3].LineDash = TabLeaderType.Solid;
tocInfo.FormatArray[3].Margin.Left = 30;
tocInfo.FormatArray[3].Margin.Right = 30;
tocInfo.FormatArray[3].TextState.FontStyle = FontStyles.Bold;

//Buat sebuah bagian dalam dokumen Pdf
Page page = doc.Pages.Add();

//Tambahkan empat judul dalam bagian
for (int Level = 1; Level <= 4; Level++)
{

    Aspose.Pdf.Heading heading2 = new Aspose.Pdf.Heading(Level);
    TextSegment segment2 = new TextSegment();
    heading2.Segments.Add(segment2);
    heading2.IsAutoSequence = true;
    heading2.TocPage = tocPage;
    segment2.Text = "Judul Contoh" + Level;
    heading2.TextState.Font = FontRepository.FindFont("Arial Unicode MS");

    //Tambahkan judul ke dalam Daftar Isi.
    heading2.IsInList = true;
    page.Paragraphs.Add(heading2);
}

// simpan Pdf

doc.Save(outFile);
```
### Sembunyikan Nomor Halaman di TOC

Jika Anda tidak ingin menampilkan nomor halaman, bersama dengan judul dalam TOC, Anda dapat menggunakan properti [IsShowPageNumbers](https://reference.aspose.com/pdf/net/aspose.pdf/tocinfo/properties/isshowpagenumbers) dari Kelas [TOCInfo](https://reference.aspose.com/pdf/net/aspose.pdf/tocinfo) sebagai false. Silakan periksa cuplikan kode berikut untuk menyembunyikan nomor halaman dalam daftar isi:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "HiddenPageNumbers_out.pdf";
Document doc = new Document();
Page tocPage = doc.Pages.Add();
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("Daftar Isi");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;
tocInfo.Title = title;
//Tambahkan bagian daftar ke koleksi bagian dari dokumen Pdf
tocPage.TocInfo = tocInfo;
//Tentukan format dari empat level daftar dengan mengatur margin kiri dan
//pengaturan format teks dari setiap level

tocInfo.IsShowPageNumbers = false;
tocInfo.FormatArrayLength = 4;
tocInfo.FormatArray[0].Margin.Right = 0;
tocInfo.FormatArray[0].TextState.FontStyle = FontStyles.Bold | FontStyles.Italic;
tocInfo.FormatArray[1].Margin.Left = 30;
tocInfo.FormatArray[1].TextState.Underline = true;
tocInfo.FormatArray[1].TextState.FontSize = 10;
tocInfo.FormatArray[2].TextState.FontStyle = FontStyles.Bold;
tocInfo.FormatArray[3].TextState.FontStyle = FontStyles.Bold;
Page page = doc.Pages.Add();
//Tambahkan empat judul dalam bagian
for (int Level = 1; Level != 5; Level++)

{ Heading heading2 = new Heading(Level); TextSegment segment2 = new TextSegment(); heading2.TocPage = tocPage; heading2.Segments.Add(segment2); heading2.IsAutoSequence = true; segment2.Text = "ini adalah judul level " + Level; heading2.IsInList = true; page.Paragraphs.Add(heading2); }
doc.Save(outFile);
```
### Sesuaikan Nomor Halaman saat menambahkan TOC

Umum untuk menyesuaikan penomoran halaman dalam TOC saat menambahkan TOC dalam dokumen PDF. Misalnya, kita mungkin perlu menambahkan beberapa awalan sebelum nomor halaman seperti P1, P2, P3, dan seterusnya. Dalam kasus seperti itu, Aspose.PDF untuk .NET menyediakan properti PageNumbersPrefix dari kelas TocInfo yang dapat digunakan untuk menyesuaikan nomor halaman seperti yang ditunjukkan dalam contoh kode berikut.

```csharp
// Untuk contoh lengkap dan berkas data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string inFile = RunExamples.GetDataDir_AsposePdf_WorkingDocuments() + "42824.pdf";
string outFile = RunExamples.GetDataDir_AsposePdf_WorkingDocuments() + "42824_out.pdf";
// Memuat berkas PDF yang sudah ada
Document doc = new Document(inFile);
// Mendapatkan akses ke halaman pertama dari berkas PDF
Aspose.Pdf.Page tocPage = doc.Pages.Insert(1);
// Membuat objek untuk mewakili informasi TOC
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("Daftar Isi");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;
// Menetapkan judul untuk TOC
tocInfo.Title = title;
tocInfo.PageNumbersPrefix = "P";
tocPage.TocInfo = tocInfo;
for (int i = 1; i<doc.Pages.Count; i++)
{
    // Membuat objek Heading
    Aspose.Pdf.Heading heading2 = new Aspose.Pdf.Heading(1);
    TextSegment segment2 = new TextSegment();
    heading2.TocPage = tocPage;
    heading2.Segments.Add(segment2);
    // Menentukan halaman tujuan untuk objek heading
    heading2.DestinationPage = doc.Pages[i + 1];
    // Halaman tujuan
    heading2.Top = doc.Pages[i + 1].Rect.Height;
    // Koordinat tujuan
    segment2.Text = "Halaman " + i.ToString();
    // Menambahkan heading ke halaman yang mengandung TOC
    tocPage.Paragraphs.Add(heading2);
}

// Menyimpan dokumen yang telah diperbarui
doc.Save(outFile);
```
## Cara Mengatur Tanggal Kadaluarsa PDF

Kami menerapkan hak akses pada file PDF sehingga sekelompok pengguna tertentu dapat mengakses fitur/objek tertentu dari dokumen PDF. Untuk membatasi akses file PDF, kami biasanya menerapkan enkripsi dan kami mungkin memiliki kebutuhan untuk mengatur tanggal kadaluarsa file PDF, sehingga pengguna yang mengakses/melihat dokumen mendapatkan pemberitahuan yang valid mengenai kadaluarsa file PDF.

Untuk mencapai persyaratan yang dinyatakan di atas, kami dapat menggunakan objek *JavascriptAction*. Silakan perhatikan potongan kode berikut.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Instansiasi objek Dokumen
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
// Tambahkan halaman ke koleksi halaman file PDF
doc.Pages.Add();
// Tambahkan fragmen teks ke koleksi paragraf objek halaman
doc.Pages[1].Paragraphs.Add(new TextFragment("Hello World..."));
// Buat objek JavaScript untuk mengatur tanggal kadaluarsa PDF
JavascriptAction javaScript = new JavascriptAction(
"var year=2017;"
+ "var month=5;"
+ "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
+ "expiry = new Date(year, month);"
+ "if (today.getTime() > expiry.getTime())"
+ "app.alert('File ini telah kadaluarsa. Anda memerlukan yang baru.');");
// Tetapkan JavaScript sebagai tindakan buka PDF
doc.OpenAction = javaScript;

dataDir = dataDir + "SetExpiryDate_out.pdf";
// Simpan Dokumen PDF
doc.Save(dataDir);
```
## Tentukan Progres Pembuatan File PDF

Seorang pelanggan meminta kami untuk menambahkan fitur yang memungkinkan pengembang untuk menentukan progres pembuatan file PDF. Berikut adalah tanggapan untuk permintaan tersebut.

Bidang [CustomerProgressHandler](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/fields/customprogresshandler) dari kelas [DocSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) memungkinkan Anda menentukan bagaimana proses pembuatan PDF berlangsung. Handler tersebut memiliki tipe-tipe berikut:

- DocSaveOptions.ConversionProgessEventHandler
- DocSaveOptions.ProgressEventHandlerInfo
- DocSaveOptions.ProgressEventType

Potongan kode di bawah ini menunjukkan bagaimana menggunakan CustomerProgressHandler.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "AddTOC.pdf");
DocSaveOptions saveOptions = new DocSaveOptions();
saveOptions.CustomProgressHandler = new UnifiedSaveOptions.ConversionProgressEventHandler(ShowProgressOnConsole);

dataDir = dataDir + "DetermineProgress_out.pdf";
pdfDocument.Save(dataDir, saveOptions);
Console.ReadLine();
```
```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
public static void ShowProgressOnConsole(DocSaveOptions.ProgressEventHandlerInfo eventInfo)
{
    switch (eventInfo.EventType)
    {
        case DocSaveOptions.ProgressEventType.TotalProgress:
            Console.WriteLine(String.Format("{0}  - Progres konversi : {1}% .", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.SourcePageAnalized:
            Console.WriteLine(String.Format("{0}  - Halaman sumber {1} dari {2} dianalisis.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.ResultPageCreated:
            Console.WriteLine(String.Format("{0}  - Layout halaman hasil {1} dari {2} dibuat.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.ResultPageSaved:
            Console.WriteLine(String.Format("{0}  - Halaman hasil {1} dari {2} diekspor.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        default:
            break;
    }

}
```
## Meratakan PDF yang Dapat Diisi di C#

Dokumen PDF sering mencakup formulir dengan widget yang dapat diisi seperti tombol radio, kotak centang, kotak teks, daftar, dll. Untuk membuatnya tidak dapat diedit untuk berbagai keperluan aplikasi, kita perlu meratakan file PDF.
Aspose.PDF menyediakan fungsi untuk meratakan PDF Anda di C# hanya dengan beberapa baris kode:

```csharp

// Memuat formulir PDF sumber
Document doc = new Document(dataDir + "input.pdf");

// Meratakan PDF yang Dapat Diisi
if (doc.Form.Fields.Count() > 0)
{
    foreach (var item in doc.Form.Fields)
    {
        item.Flatten();
    }
}

dataDir = dataDir + "FlattenForms_out.pdf";
// Menyimpan dokumen yang telah diperbarui
doc.Save(dataDir);
```

