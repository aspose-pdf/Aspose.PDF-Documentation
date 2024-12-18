---
title: Ekstrak teks dari PDF C#
linktitle: Ekstrak teks dari PDF
type: docs
weight: 10
url: /id/net/extract-text-from-all-pdf/
description: Artikel ini menjelaskan berbagai cara untuk mengekstrak teks dari dokumen PDF menggunakan Aspose.PDF di C#. 
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ekstrak Teks Dari Semua Halaman Dokumen PDF

Mengekstrak teks dari dokumen PDF adalah kebutuhan umum. Dalam contoh ini, Anda akan melihat bagaimana Aspose.PDF untuk .NET memungkinkan mengekstrak teks dari semua halaman dokumen PDF. Anda perlu membuat objek dari kelas **TextAbsorber**. Setelah itu, buka PDF menggunakan kelas **Document** dan panggil metode **Accept** dari koleksi **Pages**. Kelas **TextAbsorber** menyerap teks dari dokumen dan mengembalikannya dalam properti **Text**. Potongan kode berikut menunjukkan cara mengekstrak teks dari semua halaman dokumen PDF.

Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "ExtractTextAll.pdf");

// Buat objek TextAbsorber untuk mengekstrak teks
TextAbsorber textAbsorber = new TextAbsorber();
// Terima absorber untuk semua halaman
pdfDocument.Pages.Accept(textAbsorber);
// Dapatkan teks yang diekstrak
string extractedText = textAbsorber.Text;
// Buat penulis dan buka file
TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt");
// Tulis baris teks ke file
tw.WriteLine(extractedText);
// Tutup aliran
tw.Close();
```
Panggil metode **Accept** pada halaman tertentu dari objek Dokumen. Indeks adalah nomor halaman tertentu dari mana teks perlu diekstrak.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

// Buat objek TextAbsorber untuk mengekstrak teks
TextAbsorber textAbsorber = new TextAbsorber();

// Terima absorber untuk halaman tertentu
pdfDocument.Pages[1].Accept(textAbsorber);

// Dapatkan teks yang diekstrak
string extractedText = textAbsorber.Text;

dataDir = dataDir + "extracted-text_out.txt";
// Buat penulis dan buka file
TextWriter tw = new StreamWriter(dataDir);

// Tulis baris teks ke file
tw.WriteLine(extractedText);

// Tutup aliran
tw.Close();
```

## Ekstrak Teks dari Halaman menggunakan Text Device

Anda dapat menggunakan kelas **TextDevice** untuk mengekstrak teks dari file PDF. TextDevice menggunakan TextAbsorber dalam implementasinya, sehingga, sebenarnya mereka melakukan hal yang sama tetapi TextDevice hanya diimplementasikan untuk menyatukan pendekatan "Device" untuk mengekstrak apa pun dari halaman ImageDevice, PageDevice, dll. TextAbsorber dapat mengekstrak teks dari Halaman, seluruh PDF atau XForm, TextAbsorber ini lebih universal

### Ekstrak teks dari semua halaman

Langkah-langkah berikut dan potongan kode menunjukkan cara mengekstrak teks dari PDF menggunakan text device.

1. Buat objek kelas Document dengan file PDF masukan yang ditentukan
1. Buat objek kelas TextDevice
1. Gunakan objek kelas TextExtractOptions untuk menentukan opsi ekstraksi
1. Gunakan metode Process dari kelas TextDevice untuk mengonversi isi ke dalam teks
1. Simpan teks ke file keluaran

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Buka dokumen
Document pdfDocument = new Document( dataDir + "input.pdf");
System.Text.StringBuilder builder = new System.Text.StringBuilder();
// String untuk menyimpan teks yang diekstrak
string extractedText = "";

foreach (Page pdfPage in pdfDocument.Pages)
{
    using (MemoryStream textStream = new MemoryStream())
    {
        // Buat text device
        TextDevice textDevice = new TextDevice();

        // Atur opsi ekstraksi teks - atur mode ekstraksi teks (Raw atau Pure)
        TextExtractionOptions textExtOptions = new
        TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        textDevice.ExtractionOptions = textExtOptions;

        // Konversi halaman tertentu dan simpan teks ke stream
        textDevice.Process(pdfPage, textStream);
        // Konversi halaman tertentu dan simpan teks ke stream
        textDevice.Process(pdfDocument.Pages[1], textStream);

        // Tutup memory stream
        textStream.Close();

        // Dapatkan teks dari memory stream
        extractedText = Encoding.Unicode.GetString(textStream.ToArray());
    }
    builder.Append(extractedText);
}

dataDir = dataDir + "input_Text_Extracted_out.txt";
// Simpan teks yang diekstrak di file teks
File.WriteAllText(dataDir, builder.ToString());
```
## Ekstrak Teks dari Area Halaman Tertentu

Kelas **TextAbsorber** menyediakan kemampuan untuk mengekstrak teks dari area tertentu atau semua halaman dari dokumen PDF. Kelas ini mengembalikan teks yang diekstrak dalam properti **Text**. Namun, jika kita memiliki kebutuhan untuk mengekstrak teks dari area halaman tertentu, kita dapat menggunakan properti **Rectangle** dari **TextSearchOptions**. Properti Rectangle menerima objek Rectangle sebagai nilai dan menggunakan properti ini, kita dapat menentukan area halaman dari mana kita perlu mengekstrak teks.

Metode **Accept** dari halaman dipanggil untuk mengekstrak teks. Buat objek dari kelas **Document** dan **TextAbsorber**. Panggil metode **Accept** pada halaman individu, sebagai **Page** Index, dari objek **Document**. **Index** adalah nomor halaman tertentu dari mana teks perlu diekstrak. Anda dapat mendapatkan teks dari properti **Text** dari kelas **TextAbsorber**. Potongan kode berikut menunjukkan cara mengekstrak teks dari halaman individu.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).
Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

```csharp
// Untuk contoh lengkap dan berkas data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "ExtractTextAll.pdf");

// Buat objek TextAbsorber untuk mengekstrak teks
TextAbsorber absorber = new TextAbsorber();
absorber.TextSearchOptions.LimitToPageBounds = true;
absorber.TextSearchOptions.Rectangle = new Aspose.Pdf.Rectangle(100, 200, 250, 350);

// Terima absorber untuk halaman pertama
pdfDocument.Pages[1].Accept(absorber);

// Dapatkan teks yang diekstrak
string extractedText = absorber.Text;
// Buat penulis dan buka berkasnya
TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt");
// Tulis sebaris teks ke dalam berkas
tw.WriteLine(extractedText);
// Tutup aliran
tw.Close();
```

## Ekstrak teks berdasarkan kolom

Sebuah berkas PDF mungkin terdiri dari elemen Teks, Gambar, Anotasi, Lampiran, Grafik, dll dan Aspose.PDF untuk .NET menawarkan fitur untuk Menambahkan serta memanipulasi semua elemen ini.
Sebuah file PDF dapat terdiri dari elemen Teks, Gambar, Anotasi, Lampiran, Grafik, dll dan Aspose.PDF untuk .NET menawarkan fitur untuk Menambahkan serta memanipulasi semua elemen ini.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

TextFragmentAbsorber tfa = new TextFragmentAbsorber();
pdfDocument.Pages.Accept(tfa);
TextFragmentCollection tfc = tfa.TextFragments;
foreach (TextFragment tf in tfc)
{
    // Perlu mengurangi ukuran font setidaknya sebesar 70%
    tf.TextState.FontSize = tf.TextState.FontSize * 0.7f;
}
Stream st = new MemoryStream();
pdfDocument.Save(st);
pdfDocument = new Document(st);
TextAbsorber textAbsorber = new TextAbsorber();
pdfDocument.Pages.Accept(textAbsorber);
String extractedText = textAbsorber.Text;
textAbsorber.Visit(pdfDocument);

dataDir = dataDir + "ExtractColumnsText_out.txt";

System.IO.File.WriteAllText(dataDir, extractedText);
```
### Pendekatan Kedua - Menggunakan ScaleFactor

Dalam rilis baru ini, kami juga telah memperkenalkan beberapa peningkatan pada TextAbsorber dan pada mekanisme pemformatan teks internal. Jadi sekarang selama ekstraksi teks menggunakan mode ‘Pure’, Anda dapat menentukan opsi ScaleFactor dan ini bisa menjadi pendekatan lain untuk mengekstrak teks dari dokumen PDF multi-kolom selain pendekatan yang telah disebutkan di atas. Faktor skala ini dapat diatur untuk menyesuaikan grid yang digunakan untuk mekanisme pemformatan teks internal selama ekstraksi teks. Menentukan nilai ScaleFactor antara 1 dan 0.1 (termasuk 0.1) memiliki efek yang sama dengan pengurangan ukuran font.

Menentukan nilai ScaleFactor antara 0.1 dan -0.1 dianggap sebagai nilai nol, tetapi ini membuat algoritma untuk menghitung faktor skala yang dibutuhkan selama mengekstrak teks secara otomatis.
Menentukan nilai ScaleFactor antara 0.1 dan -0.1 dianggap sebagai nilai nol, namun hal itu membuat algoritma menghitung faktor skala yang dibutuhkan saat mengekstrak teks secara otomatis.

Kami menyarankan penggunaan penskalaan otomatis (ScaleFactor = 0) saat memproses sejumlah besar file PDF untuk ekstraksi konten teks. Atau secara manual mengatur pengurangan redundan lebar grid (sekitar ScaleFactor = 0.5). Namun, Anda tidak boleh menentukan apakah penskalaan diperlukan untuk dokumen konkret atau tidak. Jika Anda mengatur pengurangan redundan lebar grid untuk dokumen (yang tidak memerlukannya), konten teks yang diekstrak akan tetap sepenuhnya memadai. Silakan lihat cuplikan kode berikut.

Cuplikan kode berikut juga berfungsi dengan perpustakaan [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

TextAbsorber textAbsorber = new TextAbsorber();
textAbsorber.ExtractionOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
// Mengatur faktor skala menjadi 0.5 cukup untuk memisahkan kolom di sebagian besar dokumen
// Pengaturan nol memungkinkan algoritma memilih faktor skala secara otomatis
textAbsorber.ExtractionOptions.ScaleFactor = 0.5; /* 0; */
pdfDocument.Pages.Accept(textAbsorber);
String extractedText = textAbsorber.Text;
System.IO.File.WriteAllText( dataDir + "ExtractTextUsingScaleFactor_out.text", extractedText);
```
{{% alert color="primary" %}}

Harap diperhatikan bahwa tidak ada korespondensi langsung antara ScaleFactor baru dan koefisien lama pengurangan font secara manual. Namun, algoritma secara default memperhitungkan nilai ukuran font yang telah berkurang karena beberapa alasan internal. Misalnya, mengurangi ukuran font dari 10 menjadi 7 memiliki efek yang sama seperti mengatur faktor skala menjadi 5/8 (= 0.625).

{{% /alert %}}

## Ekstrak Teks yang Diberi Sorotan dari Dokumen PDF

Dalam berbagai skenario ekstraksi teks dari dokumen PDF, Anda mungkin membutuhkan fungsi untuk hanya mengekstrak teks yang diberi sorotan dari dokumen PDF. Untuk mengimplementasikan fungsionalitas ini, kami telah menambahkan metode TextMarkupAnnotation.GetMarkedText() dan TextMarkupAnnotation.GetMarkedTextFragments() dalam API. Anda dapat mengekstrak teks yang diberi sorotan dari dokumen PDF dengan memfilter TextMarkupAnnotation dan menggunakan metode yang disebutkan. Potongan kode berikut menunjukkan bagaimana Anda dapat mengekstrak teks yang diberi sorotan dari dokumen PDF.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).
Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
Document doc = new Document(dataDir + "ExtractHighlightedText.pdf");
// Melakukan perulangan pada semua anotasi
foreach (Annotation annotation in doc.Pages[1].Annotations)
{
    // Menyaring TextMarkupAnnotation
    if (annotation is TextMarkupAnnotation)
    {
        TextMarkupAnnotation highlightedAnnotation = annotation as TextMarkupAnnotation;
        // Mengambil fragmen teks yang di-highlight
        TextFragmentCollection collection = highlightedAnnotation.GetMarkedTextFragments();
        foreach (TextFragment tf in collection)
        {
            // Menampilkan teks yang di-highlight
            Console.WriteLine(tf.Text);
        }
    }
}
```

## Akses Fragmen Teks dan Elemen Segmen dari XML

Terkadang kita memerlukan akses ke item TextFragement atau TextSegment saat memproses dokumen PDF yang dihasilkan dari XML.
Terkadang kita membutuhkan akses ke item TextFragement atau TextSegment ketika memproses dokumen PDF yang dihasilkan dari XML.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string inXml = "40014.xml";
string outFile = "40014_out.pdf";

Document doc = new Document();
doc.BindXml(dataDir + inXml);

Page page = (Page)doc.GetObjectById("mainSection");

TextSegment segment = (TextSegment)doc.GetObjectById("boldHtml");
segment = (TextSegment)doc.GetObjectById("strongHtml");
doc.Save(dataDir + outFile);
```
