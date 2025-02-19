---
title: Optimalkan, Kompresi atau Kurangi Ukuran PDF di C#
linktitle: Optimalkan PDF
type: docs
weight: 30
url: /id/net/optimize-pdf/
description: Optimalkan file PDF, kecilkan semua gambar, kurangi ukuran PDF, lepaskan font yang tidak digunakan, hapus objek yang tidak digunakan dengan C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Optimalkan PDF menggunakan C#",
    "alternativeHeadline": "Cara mengoptimalkan PDF dengan .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, optimalkan pdf",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dokumen Aspose.PDF",
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
    "url": "/net/optimize-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/optimize-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Optimalkan file PDF, kecilkan semua gambar, kurangi ukuran PDF, lepaskan font yang tidak digunakan, hapus objek yang tidak digunakan dengan C#."
}
</script>
Dokumen PDF terkadang dapat mengandung data tambahan. Mengurangi ukuran file PDF akan membantu mengoptimalkan transfer jaringan dan penyimpanan. Ini sangat berguna untuk penerbitan di halaman web, berbagi di jejaring sosial, mengirim melalui e-mail, atau arsip di penyimpanan. Kita dapat menggunakan beberapa teknik untuk mengoptimalkan PDF:

- Mengoptimalkan konten halaman untuk penjelajahan online
- Mengompres atau mengurangi semua gambar
- Mengaktifkan penggunaan kembali konten halaman
- Menggabungkan aliran duplikat
- Tidak menyertakan font
- Menghapus objek yang tidak digunakan
- Menghapus penghalusan bidang formulir
- Menghapus atau meratakan anotasi

{{% alert color="primary" %}}

 Penjelasan rinci tentang metode optimasi dapat ditemukan di halaman Ikhtisar Metode Optimasi.

{{% /alert %}}

## Optimalkan Dokumen PDF untuk Web

Optimasi, atau linearisasi untuk Web, merujuk pada proses membuat file PDF cocok untuk penjelajahan online menggunakan browser web. Untuk mengoptimalkan file untuk tampilan web:

1. Buka dokumen masukan dalam objek [Dokumen](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1.
1. Simpan dokumen yang telah dioptimalkan menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save).

Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

Potongan kode berikut menunjukkan cara mengoptimalkan dokumen PDF untuk web.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");

// Optimalkan untuk web
pdfDocument.Optimize();

dataDir = dataDir + "OptimizeDocument_out.pdf";

// Simpan dokumen keluaran
pdfDocument.Save(dataDir);
```

## Kurangi Ukuran PDF

Metode [OptimizeResources()](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/optimizeresources) memungkinkan Anda untuk mengurangi ukuran dokumen dengan membuang informasi yang tidak perlu.
Metode [OptimizeResources()](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/optimizeresources) memungkinkan Anda untuk mengurangi ukuran dokumen dengan menghilangkan informasi yang tidak perlu.

- Sumber daya yang tidak digunakan di halaman dokumen dihapus
- Sumber daya yang sama digabungkan menjadi satu objek
- Objek yang tidak digunakan dihapus

Potongan kode di bawah ini adalah contoh. Namun, perlu dicatat bahwa metode ini tidak dapat menjamin penyusutan dokumen.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Buka dokumen
Document pdfDocument = new Document(dataDir + "ShrinkDocument.pdf");
// Optimalkan dokumen PDF. Perlu dicatat, meskipun, bahwa metode ini tidak dapat menjamin penyusutan dokumen
pdfDocument.OptimizeResources();
dataDir = dataDir + "ShrinkDocument_out.pdf";
// Simpan dokumen yang telah diperbarui
pdfDocument.Save(dataDir);
```

## Manajemen Strategi Optimisasi

Kita juga dapat menyesuaikan strategi optimisasi.
Kita juga dapat menyesuaikan strategi optimasi.

### Menyusutkan atau Mengompres Semua Gambar

Kita memiliki dua cara untuk bekerja dengan gambar: mengurangi kualitas gambar dan/atau mengubah resolusi mereka. Dalam hal ini, [ImageCompressionOptions](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions) harus diterapkan. Pada contoh berikut, kami menyusutkan gambar dengan mengurangi [ImageQuality](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions/properties/imagequality) menjadi 50.

`ImageQuality` bekerja mirip dengan kualitas JPEG, di mana nilai 0 adalah yang terendah dan nilai 100 adalah yang tertinggi.

```csharp
// Untuk contoh lengkap dan berkas data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// Buka dokumen
Document pdfDocument = new Document(dataDir + "Shrinkimage.pdf");
// Inisialisasi OptimizationOptions
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// Setel opsi CompressImages
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// Setel opsi ImageQuality
optimizeOptions.ImageCompressionOptions.ImageQuality = 50;
// Optimalkan dokumen PDF menggunakan OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "Shrinkimage_out.pdf";
// Simpan dokumen yang telah diperbarui
pdfDocument.Save(dataDir);
```
Cara lain adalah dengan mengubah ukuran gambar ke resolusi yang lebih rendah. Dalam hal ini, kita harus mengatur ResizeImages menjadi true dan MaxResolution ke nilai yang sesuai.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Inisialisasi Waktu
var time = DateTime.Now.Ticks;
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// Buka dokumen
Document pdfDocument = new Document(dataDir + "ResizeImage.pdf");
// Inisialisasi OptimizationOptions
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// Atur opsi CompressImages
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// Atur opsi ImageQuality
optimizeOptions.ImageCompressionOptions.ImageQuality = 75;
// Atur opsi ResizeImage
optimizeOptions.ImageCompressionOptions.ResizeImages = true;
// Atur opsi MaxResolution
optimizeOptions.ImageCompressionOptions.MaxResolution = 300;
// Optimalkan dokumen PDF menggunakan OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "ResizeImages_out.pdf";
// Simpan dokumen yang telah diperbarui
pdfDocument.Save(dataDir);
```
Masalah penting lainnya adalah waktu eksekusi. Namun, kita juga dapat mengatur pengaturan ini. Saat ini, kita dapat menggunakan dua algoritma - Standar dan Cepat. Untuk mengontrol waktu eksekusi kita harus mengatur properti [Versi](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions/properties/version). Cuplikan berikut menunjukkan algoritma Cepat:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Inisialisasi Waktu
var time = DateTime.Now.Ticks;
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// Buka dokumen
Document pdfDocument = new Document(dataDir + "Shrinkimage.pdf");
// Inisialisasi OptimizationOptions
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// Setel opsi CompressImages
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// Setel opsi ImageQuality
optimizeOptions.ImageCompressionOptions.ImageQuality = 75;
// Setel Versi Kompresi Gambar menjadi cepat
optimizeOptions.ImageCompressionOptions.Version = Pdf.Optimization.ImageCompressionVersion.Fast;
// Optimalkan dokumen PDF menggunakan OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "FastShrinkImages_out.pdf";
// Simpan dokumen yang telah diperbarui
pdfDocument.Save(dataDir);
Console.WriteLine("Ticks: {0}", DateTime.Now.Ticks - time);
```
### Menghapus Objek yang Tidak Digunakan

Dokumen PDF terkadang mengandung objek PDF yang tidak dirujuk oleh objek lain dalam dokumen. Hal ini dapat terjadi, misalnya, ketika sebuah halaman dihapus dari pohon halaman dokumen tetapi objek halaman itu sendiri tidak dihapus. Menghapus objek-objek ini tidak membuat dokumen menjadi tidak valid tetapi justru menyusutkannya.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Buka dokumen
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Setel opsi RemoveUsedObject
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    RemoveUnusedObjects = true
};
// Optimalkan dokumen PDF menggunakan OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// Simpan dokumen yang telah diperbarui
pdfDocument.Save(dataDir);
```

### Menghapus Aliran yang Tidak Digunakan

Terkadang dokumen mengandung aliran sumber daya yang tidak digunakan.
Terkadang dokumen mengandung aliran sumber daya yang tidak digunakan.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Buka dokumen
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Setel opsi RemoveUsedStreams
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    RemoveUnusedStreams = true
};
// Optimalkan dokumen PDF menggunakan OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// Simpan dokumen yang telah diperbarui
pdfDocument.Save(dataDir);
```

### Menghubungkan Aliran Duplikat

Beberapa dokumen dapat mengandung beberapa aliran sumber daya identik (seperti gambar, misalnya).
Beberapa dokumen dapat mengandung beberapa aliran sumber daya yang identik (seperti gambar, misalnya).

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Buka dokumen
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Setel opsi LinkDuplicateStreams
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    LinkDuplicateStreams = true
};
// Optimalkan dokumen PDF menggunakan OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// Simpan dokumen yang telah diperbarui
pdfDocument.Save(dataDir);
```

Selanjutnya, kita dapat menggunakan pengaturan [AllowReusePageContent](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/optimizationoptions/properties/allowreusepagecontent).
Selain itu, kita dapat menggunakan pengaturan [AllowReusePageContent](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/optimizationoptions/properties/allowreusepagecontent).

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Buka dokumen
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Mengatur opsi AllowReusePageContent
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    AllowReusePageContent = true
};
Console.WriteLine("Mulai");
// Mengoptimalkan dokumen PDF menggunakan OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
// Simpan dokumen yang telah diperbarui
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("Selesai");
var fi1 = new System.IO.FileInfo(dataDir + "OptimizeDocument.pdf");
var fi2 = new System.IO.FileInfo(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("Ukuran file asli: {0}. Ukuran file yang dikurangi: {1}", fi1.Length, fi2.Length);
```
### Mengeluarkan Font yang Tertanam

Jika dokumen menggunakan font yang tertanam, ini berarti semua data font disimpan dalam dokumen tersebut. Keuntungannya adalah dokumen dapat dilihat tanpa memandang apakah font tersebut terinstal di mesin pengguna atau tidak. Namun, menanamkan font membuat ukuran dokumen menjadi lebih besar. Metode mengeluarkan font menghapus semua font yang tertanam. Dengan demikian, ukuran dokumen berkurang tetapi dokumen itu sendiri mungkin menjadi tidak terbaca jika font yang benar tidak terinstal.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Buka dokumen
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Setel opsi UnembedFonts
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    UnembedFonts = true
};
Console.WriteLine("Mulai");
// Optimalkan dokumen PDF menggunakan OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
// Simpan dokumen yang telah diperbarui
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("Selesai");
var fi1 = new System.IO.FileInfo(dataDir + "OptimizeDocument.pdf");
var fi2 = new System.IO.FileInfo(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("Ukuran file asli: {0}. Ukuran file yang dikurangi: {1}", fi1.Length, fi2.Length);
```
Sumber daya optimisasi menerapkan metode-metode ini pada dokumen. Jika salah satu dari metode ini diterapkan, ukuran dokumen kemungkinan besar akan berkurang. Jika tidak ada metode yang diterapkan, ukuran dokumen tidak akan berubah yang mana ini adalah hal yang jelas.

## Cara Tambahan untuk Mengurangi Ukuran Dokumen PDF

### Menghapus atau Meratakan Anotasi

Anotasi dapat dihapus ketika tidak diperlukan. Ketika diperlukan tetapi tidak memerlukan pengeditan tambahan, anotasi dapat diratakan. Kedua teknik ini akan mengurangi ukuran file.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Buka dokumen
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Ratakan anotasi
foreach (var page in pdfDocument.Pages)
{
    foreach (var annotation in page.Annotations)
    {
        annotation.Flatten();
    }

}
// Simpan dokumen yang telah diperbarui
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
```
### Menghapus Isi Formulir

Jika dokumen PDF mengandung AcroForms, kita dapat mencoba mengurangi ukuran file dengan meratakan isi form.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Muat formulir PDF sumber
Document doc = new Document(dataDir + "input.pdf");

// Meratakan Formulir
if (doc.Form.Fields.Count() > 0)
{
    foreach (var item in doc.Form.Fields)
    {
        item.Flatten();
    }
}

dataDir = dataDir + "FlattenForms_out.pdf";
// Simpan dokumen yang telah diperbarui
doc.Save(dataDir);
```

### Mengkonversi PDF dari ruang warna RGB ke skala abu-abu

Sebuah file PDF terdiri dari Teks, Gambar, Lampiran, Anotasi, Grafik, dan objek lainnya.
Berkas PDF terdiri dari Teks, Gambar, Lampiran, Anotasi, Grafik, dan objek lainnya.

```csharp
// Untuk contoh lengkap dan berkas data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Muat berkas PDF sumber
using (Document document = new Document(dataDir + "input.pdf"))
{
    Aspose.Pdf.RgbToDeviceGrayConversionStrategy strategy = new Aspose.Pdf.RgbToDeviceGrayConversionStrategy();
    for (int idxPage = 1; idxPage <= document.Pages.Count; idxPage++)
    {
        // Dapatkan instansi halaman tertentu di dalam PDF
        Page page = document.Pages[idxPage];
        // Ubah gambar color space RGB menjadi GrayScale color space
        strategy.Convert(page);
    }
    // Simpan berkas hasil
    document.Save(dataDir + "Test-gray_out.pdf");
}
```

### Kompresi FlateDecode

{{% alert color="primary" %}}

Fitur ini didukung oleh versi 18.12 atau lebih tinggi.

{{% /alert %}}

Aspose.PDF for .NET menyediakan dukungan kompresi FlateDecode untuk fungsi Optimisasi PDF.
Aspose.PDF untuk .NET menyediakan dukungan kompresi FlateDecode untuk fungsi Optimisasi PDF.

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-FlateDecodeCompression-1.cs" >}}

### **Simpan Gambar dalam XImageCollection**

Aspose.PDF untuk .NET memberikan kemampuan untuk menyimpan gambar baru ke dalam **XImageCollection** dengan kompresi FlateDecode. Untuk mengaktifkan opsi ini Anda dapat menggunakan bendera **ImageFilterType.Flate**. Cuplikan kode berikut menunjukkan cara menggunakan fungsionalitas ini:

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-StoreImageInXImageCollection-1.cs" >}}

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

