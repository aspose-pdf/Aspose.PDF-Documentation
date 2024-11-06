---
title: ToC Generator
type: docs
weight: 150
url: id/net/plugins/tocgenerator/
description: Membuat daftar isi dengan Aspose.PDF ToC Generator untuk .NET
lastmod: "2024-01-24"
draft: false
---

Apakah Anda ingin meningkatkan dokumen PDF Anda dengan [menambahkan Daftar Isi (TOC)](https://products.aspose.org/pdf/net/toc-generator/) secara dinamis? Aspose.PDF untuk .NET menyediakan kelas `TocGenerator` yang kuat yang memungkinkan Anda untuk menghasilkan TOC dengan mudah. Dalam panduan ini, kami akan membahas langkah dasar untuk membuat TOC dalam dokumen PDF menggunakan Aspose.PDF, mencakup pembuatan objek `TocGenerator`, menambahkan jalur masukan/keluaran, dan menjalankan proses generasi TOC.

## Prasyarat

Anda akan membutuhkan hal-hal berikut:

* Visual Studio 2019 atau lebih baru
* Aspose.PDF untuk .NET 24.1 atau lebih baru
* Sebuah file PDF contoh

Selain itu, biasakan diri Anda dengan kelas `TocOptions` dan fungsionalitasnya. Informasi terperinci dapat ditemukan di [Referensi API Aspose.PDF](https://reference.aspose.com/pdf/net/aspose.pdf/TocOptions/).

Sekarang, mari kita menyelami kode dan jelajahi cara menghasilkan Daftar Isi untuk dokumen PDF Anda.
Sekarang, mari kita menyelami kode dan menjelajahi cara menghasilkan Daftar Isi untuk dokumen PDF Anda.

## Penjelajahan Kode

Kita akan menggunakan kelas `TocGeneratorDemo` dengan metode `Run` untuk mendemonstrasikan cara membuat ToC. Mari kita uraikan langkah-langkah kuncinya:

```csharp
using Aspose.Pdf.Plugins;

namespace AsposePluginsNet8.Documentation
{
    internal static class TocGeneratorDemo
    {
        private const string PathForSamples = @"C:\Samples\";

        // Menjalankan demo pembuatan TOC.
        internal static void Run()
        {
            // Membuat instansi baru dari kelas TocGenerator.
            TocGenerator generator = new();

            // Membuat instansi baru dari kelas TocOptions.
            TocOptions options = new();
            // Menambahkan jalur masukan dan keluaran ke TocOptions.
            options.AddInput(new FileDataSource(Path.Combine(PathForSamples, "sample.pdf")));
            options.AddOutput(new FileDataSource(Path.Combine(PathForSamples, "sample_toc.pdf")));

            // Memproses pembuatan TOC dan mendapatkan wadah hasil.
            var resultContainer = generator.Process(options);

            // Mendapatkan hasil dari wadah hasil.
            var result = resultContainer.ResultCollection[0];

            // Mencetak hasil ke konsol.
            Console.WriteLine(result);
        }
    }
}
```
### 1. Membuat Objek TocGenerator

Kode dimulai dengan membuat instance baru dari kelas `TocGenerator`. Kelas ini menyediakan metode untuk menghasilkan TOC untuk dokumen PDF.

```csharp
TocGenerator generator = new();
```

### 2. Membuat TocOptions

Selanjutnya, instance baru dari kelas `TocOptions` dibuat untuk mengonfigurasi proses pembuatan TOC. Jalur file masukan dan keluaran ditambahkan ke dalam opsi.

```csharp
TocOptions options = new();
options.AddInput(new FileDataSource(Path.Combine(PathForSamples, "sample.pdf")));
options.AddOutput(new FileDataSource(Path.Combine(PathForSamples, "sample_toc.pdf")));
```

### 3. Menjalankan Proses Pembuatan TOC

Metode `Process` kemudian dipanggil pada objek `TocGenerator`, dengan melewatkan opsi yang dikonfigurasi. Kontainer hasil menyimpan TOC yang telah dibuat, dan hasilnya dicetak ke konsol.

```csharp
var resultContainer = generator.Process(options);
var result = resultContainer.ResultCollection[0];
Console.WriteLine(result);
```
