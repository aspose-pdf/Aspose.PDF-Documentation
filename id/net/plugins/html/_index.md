---
title: HTML Converter
type: docs
weight: 70
url: id/net/plugins/html/
description: Cara Mengonversi File PDF ke dan dari File HTML menggunakan Plugin PdfHtml Aspose.PDF
lastmod: "2024-01-24"
draft: false
---

Dalam artikel ini, kami akan menunjukkan cara menggunakan [plugin PdfHtml](https://products.aspose.org/pdf/net/html-converter/), yang dapat mengonversi file PDF ke dan dari file HTML.

## Prasyarat

Anda akan memerlukan hal-hal berikut:

* Visual Studio 2019 atau lebih baru
* Aspose.PDF untuk .NET 21.1 atau lebih baru
* File PDF contoh dan file HTML contoh

Anda dapat mengunduh perpustakaan Aspose.PDF untuk .NET dari situs web resmi atau menginstalnya menggunakan NuGet Package Manager di Visual Studio.

## Langkah-langkah

Langkah dasar untuk mengonversi file PDF ke dan dari file HTML menggunakan plugin PdfHtml adalah:

1. Buat sebuah objek dari kelas PdfHtml
2. Buat sebuah objek dari kelas PdfToHtmlOptions atau HtmlToPdfOptions, tergantung pada arah konversi
3. Tambahkan sumber data masukan dan keluaran ke objek opsi
4.
### Langkah 1: Buat objek dari kelas PdfHtml

Kelas PdfHtml adalah kelas utama yang menyediakan fungsionalitas untuk mengonversi file PDF ke dan dari file HTML. Untuk menggunakannya, Anda perlu membuat sebuah instansi menggunakan konstruktor default:

```cs
// Buat sebuah instansi dari plugin PdfHtml
var plugin = new PdfHtml();
```

### Langkah 2: Buat objek dari kelas PdfToHtmlOptions atau HtmlToPdfOptions, tergantung pada arah konversi

Kelas PdfToHtmlOptions dan HtmlToPdfOptions adalah kelas bantuan yang memungkinkan Anda untuk menentukan berbagai opsi dan parameter untuk proses konversi, seperti format output, rentang halaman, pengkodean, font, dll. Untuk menggunakan kelas-kelas ini, Anda perlu membuat sebuah instansi dari kelas yang sesuai menggunakan konstruktor default atau dengan mengirim beberapa parameter. Sebagai contoh, untuk mengonversi file PDF ke file HTML dengan sumber daya tertanam, Anda dapat menggunakan kode berikut:

```cs
```cs
// Buat instance baru dari kelas PdfToHtmlOptions
var options = new PdfToHtmlOptions(PdfToHtmlOptions.SaveDataType.FileWithEmbeddedResources);
```

Untuk mengonversi file HTML ke file PDF dengan pengaturan default, Anda dapat menggunakan kode berikut:

```cs
// Buat instance baru dari kelas HtmlToPdfOptions
var options = new HtmlToPdfOptions();
```

Anda juga dapat mengatur opsi lainnya, seperti format output, rentang halaman, pengkodean, font, dll. menggunakan properti dari kelas opsi. Sebagai contoh, untuk mengonversi file PDF ke file HTML dengan pengkodean UTF-8 dan font Arial, Anda dapat menggunakan kode berikut:

```cs
// Buat instance baru dari kelas PdfToHtmlOptions
var options = new PdfToHtmlOptions(PdfToHtmlOptions.SaveDataType.FileWithEmbeddedResources);

// Set pengkodean ke UTF-8
options.Encoding = Encoding.UTF8;

// Set font ke Arial
options.Font = "Arial";
```

### Langkah 3: Tambahkan sumber data masukan dan keluaran ke objek opsi

Sumber data masukan dan keluaran adalah file PDF atau HTML yang ingin Anda konversi dan simpan.
Sumber data masukan dan keluaran adalah file PDF atau HTML yang ingin Anda konversi dan simpan.

```cs
// Tentukan jalur file masukan dan keluaran
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "sample.html");

// Tambahkan jalur file masukan dan keluaran ke dalam opsi
options.AddInput(new FileDataSource(inputPath));
options.AddOutput(new FileDataSource(outputPath));
```

### Langkah 4: Jalankan metode Process dari objek PdfHtml

Langkah terakhir adalah menjalankan metode Process dari objek PdfHtml, dengan melewatkan objek opsi sebagai parameter. Metode ini akan melakukan konversi dan mengembalikan objek ResultContainer, yang berisi hasil dari konversi, seperti status, pesan, sumber data keluaran, dan lainnya. Anda dapat mengakses hasilnya menggunakan properti dan metode dari kelas ResultContainer. Misalnya, untuk mendapatkan hasil pertama dari koleksi hasil dan mencetaknya ke konsol, Anda dapat menggunakan kode berikut:

```cs
// Proses konversi dan dapatkan kontainer hasil
var resultContainer = plugin.Process(options);

// Dapatkan hasil pertama dari koleksi hasil
var result = resultContainer.ResultCollection[0];

// Cetak hasil ke konsol
Console.WriteLine(result);
```
Hasilnya akan berisi informasi seperti jalur file keluaran.
