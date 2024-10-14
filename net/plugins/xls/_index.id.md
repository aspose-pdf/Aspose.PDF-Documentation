---
title: XLS Converter
type: docs
weight: 20
url: /net/plugins/xls/
description: Cara Mengonversi PDF ke spreadsheet Excel menggunakan plugin Aspose.Pdf
lastmod: "2024-01-24"
---

{{% alert color="primary" %}}

Dalam artikel ini, kami akan menunjukkan cara menggunakan [PdfXls plugin](https://products.aspose.org/pdf/net/xls-converter/), yang dapat mengonversi file PDF ke format Excel dengan kesetiaan dan akurasi yang tinggi.

{{% /alert %}}

## Prasyarat

Anda akan memerlukan hal berikut:

* Visual Studio 2019 atau lebih baru
* Aspose.PDF for .NET 24.1 atau lebih baru
* Sebuah file PDF sampel yang ingin Anda konversi ke format Excel

Anda dapat mengunduh pustaka Aspose.PDF for .NET dari situs web resmi atau menginstalnya menggunakan NuGet Package Manager di Visual Studio.

## Langkah-langkah

Langkah dasar untuk mengonversi file PDF ke format Excel menggunakan plugin PdfXls adalah:

1. Buat objek dari kelas PdfXls
1. Tambahkan sumber data masukan dan keluaran ke objek PdfToXlsOptions
1. Jalankan metode Process dari objek PdfXls

Mari kita lihat cara mengimplementasikannya dalam kode C#.
Mari kita lihat bagaimana mengimplementasikan langkah-langkah ini dalam kode C#.

### Langkah 1: Buat objek dari kelas PdfXls

Kelas PdfXls adalah kelas utama yang menyediakan fungsionalitas konversi PDF ke Excel. Untuk menggunakannya, Anda perlu membuat instance dari kelas ini menggunakan konstruktor default:

```csharp
// Buat instance dari plugin PdfXls
var plugin = new PdfXls();
```

### Langkah 2: Tambahkan sumber data masukan dan keluaran ke objek PdfToXlsOptions

Kelas PdfToXlsOptions adalah kelas pembantu yang memungkinkan Anda menentukan berbagai opsi dan parameter untuk proses konversi. Untuk menggunakannya, Anda perlu membuat instance dari kelas ini dan menambahkan sumber data masukan dan keluaran menggunakan metode `AddInput` dan `AddOutput`. Sumber data bisa berupa jalur file atau aliran. Sebagai contoh, untuk mengonversi file PDF bernama `sample.pdf` di folder `C:\Samples` menjadi file Excel bernama `sample.xlsx` di folder yang sama, Anda dapat menggunakan kode berikut:

```csharp
// Tentukan jalur file masukan dan keluaran
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "sample.xlsx");

// Buat instance dari kelas PdfToXlsOptions
var options = new PdfToXlsOptions();

// Tambahkan jalur file masukan dan keluaran ke opsi
options.AddInput(new FileDataSource(inputPath));
options.AddOutput(new FileDataSource(outputPath));
```
Anda juga dapat mengatur opsi lain, seperti format output, rentang halaman, nama lembar kerja, dll. menggunakan properti dari kelas PdfToXlsOptions. Misalnya, untuk mengonversi file PDF ke format XLSX, memasukkan kolom kosong di posisi pertama, dan menamai lembar kerja sebagai "MySheet", Anda dapat menggunakan kode berikut:

```csharp
// Setel format output ke XLSX
options.Format = PdfToXlsOptions.ExcelFormat.XLSX;

// Masukkan kolom kosong di posisi pertama
options.InsertBlankColumnAtFirst = true;
```

### Langkah 3: Jalankan metode Process dari objek PdfXls

Langkah terakhir adalah menjalankan metode Process dari objek PdfXls, dengan melewatkan objek PdfToXlsOptions sebagai parameter.
Langkah terakhir adalah menjalankan metode Process dari objek PdfXls, dengan memberikan objek PdfToXlsOptions sebagai parameter.

```csharp
// Memproses konversi PDF ke Excel menggunakan plugin dan opsi
var resultContainer = plugin.Process(options);

// Mendapatkan hasil pertama dari koleksi hasil
var result = resultContainer.ResultCollection[0];

// Mencetak hasil
Console.WriteLine(result);
```

Hasilnya akan berisi informasi seperti jalur file keluaran.
