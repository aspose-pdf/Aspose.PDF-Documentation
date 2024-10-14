---
title: Merger
type: docs
weight: 100
url: /net/plugins/merger/
description: Cara Menggabungkan Beberapa File PDF menjadi Satu Menggunakan Plugin Penggabungan Aspose.PDF
lastmod: "2024-01-24"
---

Dalam artikel ini, kami akan menunjukkan cara menggunakan [Plugin Penggabungan](https://products.aspose.org/pdf/net/merger/), yang dapat menggabungkan beberapa file PDF menjadi satu dan menyimpannya sebagai file baru.

## Prasyarat

Anda akan memerlukan hal berikut:

* Visual Studio 2019 atau lebih baru
* Aspose.PDF untuk .NET 21.1 atau lebih baru
* Tiga file PDF contoh yang ingin Anda gabungkan

Anda dapat mengunduh pustaka Aspose.PDF untuk .NET dari situs web resmi atau menginstalnya menggunakan NuGet Package Manager di Visual Studio.

## Langkah

Langkah dasar untuk menggabungkan beberapa file PDF menjadi satu menggunakan plugin Penggabungan adalah:

1. Buat objek dari kelas Merger
2. Buat objek dari kelas MergeOptions dan tambahkan jalur file masukan dan keluaran
3. Jalankan metode Process dari objek Merger

Mari kita lihat cara mengimplementasikan langkah-langkah ini dalam kode C#.

### Langkah 1: Buat objek dari kelas Merger
### Langkah 1: Buat objek dari kelas Merger

Kelas Merger adalah kelas utama yang menyediakan fungsionalitas untuk menggabungkan beberapa file PDF menjadi satu. Untuk menggunakannya, Anda perlu membuat sebuah instansi dari kelas tersebut menggunakan konstruktor default:

```cs
// Buat instansi baru dari Merger
var pdfMerger = new Merger();
```

### Langkah 2: Buat objek dari kelas MergeOptions dan tambahkan jalur file masukan dan keluaran

Kelas MergeOptions adalah kelas pembantu yang memungkinkan Anda untuk menentukan berbagai opsi dan parameter untuk proses penggabungan, seperti rentang halaman, urutan, keamanan, dll.
Kelas MergeOptions adalah kelas pembantu yang memungkinkan Anda untuk menentukan berbagai opsi dan parameter untuk proses penggabungan, seperti rentang halaman, urutan, keamanan, dll.

```cs
// Tentukan jalur file masukan dan keluaran
string inputFilePath1 = Path.Combine(@"C:\Samples\", "sample1.pdf");
string inputFilePath2 = Path.Combine(@"C:\Samples\", "sample2.pdf");
string inputFilePath3 = Path.Combine(@"C:\Samples\", "sample3.pdf");
var outputFilePath = "TestMerge.pdf";

// Buat sebuah instansi dari kelas MergeOptions
var mergeOptions = new MergeOptions();

// Tambahkan jalur file masukan dan keluaran ke dalam opsi
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath1));
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath2));
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath3));
mergeOptions.AddOutput(new FileDataSource(outputFilePath));
```

### Langkah 3: Jalankan metode Process dari objek Merger

Langkah terakhir adalah menjalankan metode Process dari objek Merger, dengan memasukkan objek mergeOptions sebagai parameter.
Langkah terakhir adalah menjalankan metode Process dari objek Merger, dengan memberikan objek mergeOptions sebagai parameter.

```cs
// Memproses penggabungan dan menyimpan file yang telah digabungkan
pdfMerger.Process(mergeOptions);

// Mencetak pesan konfirmasi
Console.WriteLine("File PDF telah berhasil digabungkan.");
```
