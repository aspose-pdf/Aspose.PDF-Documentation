---
title: Image Extractor
type: docs
weight: 80
url: /id/net/plugins/imageextractor/
description: Ekstraksi Gambar dari PDF dengan Mudah menggunakan Plugin ImageExtractor
lastmod: "2024-01-24"
draft: false
---

Jika Anda pernah membutuhkan untuk mengekstrak gambar dari file PDF menggunakan .NET, Aspose.PDF untuk .NET menyediakan solusi yang kuat dan mudah. Dalam panduan ini, kita akan membahas langkah dasar untuk membuat objek, menambahkan sumber data, dan menjalankan metode proses menggunakan [Aspose.PDF Image Extractor](https://products.aspose.org/pdf/net/image-extractor/).

## Prasyarat

Anda akan membutuhkan hal-hal berikut:

* Visual Studio 2019 atau lebih baru
* Aspose.PDF untuk .NET 21.1 atau lebih baru
* File PDF contoh

Anda dapat mengunduh perpustakaan Aspose.PDF untuk .NET dari situs web resmi atau menginstalnya menggunakan NuGet Package Manager di Visual Studio.
Sekarang, mari kita menyelami kode dan belajar cara menggunakan plugin ImageExtractor.

## Langkah-langkah

Kode yang disediakan menunjukkan penggunaan plugin `ImageExtractor` untuk mengekstrak gambar dari file PDF.
Kode yang disediakan mendemonstrasikan penggunaan plugin `ImageExtractor` untuk mengekstrak gambar dari file PDF.

### 1. Buat Objek (ImageExtractor)

Langkah pertama melibatkan pembuatan instance dari plugin `ImageExtractor`. Ini dicapai menggunakan kode berikut:

```csharp
using var plugin = new ImageExtractor();
```

Di sini, pernyataan `using` memastikan pemusnahan sumber daya yang tepat ketika operasi selesai.

### 2. Tambahkan Sumber Data

Selanjutnya, sebuah instance dari kelas `ImageExtractorOptions` dibuat untuk mengonfigurasi proses ekstraksi gambar. Jalur file input ditambahkan ke opsi menggunakan metode `AddInput`:

```csharp
var imageExtractorOptions = new ImageExtractorOptions();
imageExtractorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));
```

Pastikan untuk mengganti `"C:\Samples\"` dan `"sample.pdf"` dengan jalur dan nama file PDF yang sesuai.

### 3. Jalankan Metode Proses

Langkah terakhir adalah memproses ekstraksi gambar menggunakan plugin dan opsi:

```csharp
Hasilnya disimpan dalam `resultContainer`, yang berisi gambar yang telah diekstrak.

### 4. Tangani Gambar yang Diekstrak

Setelah menjalankan proses, Anda dapat mengambil gambar yang diekstrak dari wadah hasil. Kode di bawah ini menunjukkan cara menyimpan gambar yang diekstrak pertama ke lokasi sementara:

```csharp
var imageExtracted = resultContainer.ResultCollection[0].ToStream();
var someTemporaryPlace = File.OpenWrite("C:\\tmp\\tmp.jpg");
imageExtracted.CopyTo(someTemporaryPlace);
```

Pastikan Anda menyesuaikan jalur tujuan dan nama file sesuai dengan preferensi Anda.

Anda dapat menyalin contoh lengkap di bawah ini:

```cs
using Aspose.Pdf.Plugins;

namespace AsposePluginsNet8.Documentation;

internal static class ImageExtractorDemo
{
    // <summary>
    // Demonstrates the usage of the ImageExtractor plugin to extract images from a PDF file.
    // </summary>
    internal static void Run()
    {
        // Create an instance of the ImageExtractor plugin.
        using var plugin = new ImageExtractor();

        // Create an instance of the ImageExtractorOptions class.
        var imageExtractorOptions = new ImageExtractorOptions();

        // Add the input file path to the options.
        imageExtractorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));

        // Process the image extraction using the plugin and options.
        var resultContainer = plugin.Process(imageExtractorOptions);

        // Get the extracted image from the result container.
        var imageExtracted = resultContainer.ResultCollection[0].ToStream();
        var someTemporaryPlace = File.OpenWrite(Path.Combine(@"C:\Samples\","tmp.jpg"));
        imageExtracted.CopyTo(someTemporaryPlace);
    }
}
```

