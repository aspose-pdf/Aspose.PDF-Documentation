---
title: JPEG Converter
type: docs
weight: 90
url: id/net/plugins/jpeg/
description: Cara Mengonversi Halaman PDF ke Gambar JPEG menggunakan Aspose.PDF JPEG Converter
lastmod: "2024-01-24"
draft: false
---

Dalam artikel ini, kami akan menunjukkan cara menggunakan [JPEG Converter](https://products.aspose.org/pdf/net/jpeg-converter/), yang dapat mengonversi halaman PDF menjadi gambar JPEG dan menyimpannya sebagai file terpisah.

## Prasyarat

Anda akan membutuhkan hal-hal berikut:

* Visual Studio 2019 atau lebih baru
* Aspose.PDF untuk .NET 24.1 atau lebih baru
* File PDF contoh yang berisi beberapa halaman

Anda dapat mengunduh pustaka Aspose.PDF untuk .NET dari situs web resmi atau menginstalnya menggunakan NuGet Package Manager di Visual Studio.

## Langkah-langkah

Langkah dasar untuk mengonversi halaman PDF menjadi gambar JPEG menggunakan JPEG Converter adalah:

1. Buat objek dari kelas Jpeg
1. Buat objek dari kelas JpegOptions dan tambahkan jalur file masukan dan keluaran
1. Jalankan metode Process dari objek Jpeg dan dapatkan wadah hasil
1.
Mari kita lihat bagaimana mengimplementasikan langkah-langkah ini dalam kode C#.

### Langkah 1: Buat objek dari kelas Jpeg

Kelas Jpeg adalah kelas utama yang menyediakan fungsionalitas untuk mengonversi halaman PDF menjadi gambar JPEG. Untuk menggunakannya, Anda perlu membuat sebuah instansi dari kelas tersebut menggunakan konstruktor default:

```cs
// Buat instansi baru dari Jpeg
var converter = new Jpeg();
```

### Langkah 2: Buat objek dari kelas JpegOptions dan tambahkan jalur file masukan dan keluaran

Kelas JpegOptions adalah kelas pembantu yang memungkinkan Anda menentukan berbagai opsi dan parameter untuk proses konversi, seperti resolusi keluaran, rentang halaman, kualitas gambar, dll.
Kelas JpegOptions adalah kelas pembantu yang memungkinkan Anda menentukan berbagai opsi dan parameter untuk proses konversi, seperti resolusi keluaran, rentang halaman, kualitas gambar, dll.

```cs
// Tentukan jalur file masukan dan keluaran
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "images");

// Buat instance dari kelas JpegOptions
var converterOptions = new JpegOptions();

// Tambahkan jalur file masukan dan keluaran ke dalam opsi
converterOptions.AddInput(new FileDataSource(inputPath));
converterOptions.AddOutput(new FileDataSource(outputPath));
```

Anda juga dapat mengatur opsi lain, seperti resolusi keluaran, rentang halaman, kualitas gambar, dll. menggunakan properti dari kelas JpegOptions. Misalnya, untuk mengonversi hanya halaman pertama dari file PDF menjadi gambar JPEG dengan resolusi 300 dpi, Anda dapat menggunakan kode berikut:

```cs
// Atur resolusi keluaran menjadi 300 dpi
converterOptions.OutputResolution = 300;

// Atur rentang halaman ke halaman pertama
converterOptions.PageRange = new PageRange(1);
```
### Langkah 3: Jalankan metode Process dari objek Jpeg dan dapatkan kontainer hasil

Langkah terakhir adalah menjalankan metode Process dari objek Jpeg, dengan memasukkan objek converterOptions sebagai parameter. Metode ini akan melakukan konversi dan mengembalikan objek ResultContainer, yang berisi hasil dari konversi, seperti status, pesan, jalur file keluaran, dll. Anda dapat mengakses hasilnya menggunakan properti dan metode dari kelas ResultContainer. Misalnya, untuk mendapatkan kontainer hasil dan mencetak status konversi, Anda dapat menggunakan kode berikut:

```cs
// Proses konversi dan dapatkan kontainer hasil
ResultContainer resultContainer = converter.Process(converterOptions);

// Cetak status konversi
Console.WriteLine(resultContainer.Status);
```

Status konversi bisa berupa Sukses atau Gagal, tergantung apakah konversi berhasil diselesaikan atau tidak.

### Langkah 4: Cetak jalur dari gambar JPEG yang telah dikonversi

Kontainer hasil berisi kumpulan hasil, satu untuk setiap jalur file keluaran.
Kontainer hasil berisi koleksi hasil, satu untuk setiap jalur file keluaran.

```cs
// Print the paths of the converted JPEG images
foreach (FileResult operationResult in resultContainer.ResultCollection.Cast<FileResult>())
{
  Console.WriteLine(operationResult.Data.ToString());
}
```

Jalur file keluaran akan memiliki format {outputPath}{pageNumber}.jpg, di mana {outputPath} adalah direktori keluaran dan {pageNumber} adalah nomor halaman dari file PDF. Sebagai contoh, jika direktori keluaran adalah C:\Samples\images dan file PDF memiliki tiga halaman, jalur file keluaran akan menjadi:

```text
C:\Samples\images\1.jpg
C:\Samples\images\2.jpg
C:\Samples\images\3.jpg
```
