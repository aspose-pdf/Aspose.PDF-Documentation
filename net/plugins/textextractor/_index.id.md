---
title: Text Extractor
type: docs
weight: 140
url: /net/plugins/textextractor/
description: Mengekstrak konten teks dari dokumen PDF.
lastmod: "2024-01-24"
---

Apakah Anda memiliki dokumen PDF yang perlu Anda [ekstrak teks secara programatik](https://products.aspose.org/pdf/net/text-extractor/)? Dengan Aspose.PDF untuk .NET, Anda dapat dengan mudah mencapai tugas ini menggunakan kelas TextExtractor. Dalam artikel ini, kami akan membahas langkah-langkah dasar untuk membuat aplikasi ekstraksi teks di .NET, mencakup pembuatan objek TextExtractor, menambahkan sumber data, dan menjalankan proses ekstraksi teks.

## Prasyarat

Anda akan memerlukan hal berikut:

* Visual Studio 2019 atau lebih baru
* Aspose.PDF untuk .NET 24.1 atau lebih baru
* Sebuah file PDF contoh

Selain itu, biasakan diri Anda dengan kelas `TextExtractorOptions` dan fungsionalitasnya. Informasi rinci dapat ditemukan di [Referensi API Aspose.PDF](https://reference.aspose.com/pdf/net/aspose.pdf/TextExtractorOptions/).

Sekarang, mari kita masuk ke dalam kode dan jelajahi cara mengekstrak teks dari dokumen PDF.
Sekarang, mari kita telusuri kode dan jelajahi cara mengekstrak teks dari dokumen PDF.

## Tinjauan Kode

Kode berikut menunjukkan kemampuan ekstraksi teks. Mari kita pecahkan langkah kuncinya:

### 1. Buat Objek TextExtractor

Kode dimulai dengan membuat instance baru dari kelas `TextExtractor`. Kelas ini menyediakan metode untuk mengekstrak teks dari dokumen PDF.

```csharp
using TextExtractor extractor = new();
```

### 2. Tambahkan Sumber Data

Selanjutnya, `FileDataSource` dibuat untuk file PDF masukan. Ini adalah file dari mana teks akan diekstraksi.

```csharp
FileDataSource fileSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));
```

### 3. Buat TextExtractorOptions

Objek `TextExtractorOptions` dibuat untuk mengonfigurasi proses ekstraksi teks. Sumber file masukan ditambahkan ke opsi.

```csharp
TextExtractorOptions textExtractorOptions = new();
textExtractorOptions.AddInput(fileSource);
```

### 4. Jalankan Proses Ekstraksi Teks

Metode `Process` kemudian dipanggil pada objek `TextExtractor`, dengan mengirimkan opsi yang telah dikonfigurasi.
Metode `Process` kemudian dipanggil pada objek `TextExtractor`, dengan mengirimkan opsi yang telah dikonfigurasi.

```csharp
var resultContainer = extractor.Process(textExtractorOptions);
var results = resultContainer.ResultCollection;
Console.WriteLine(results[0]);
```

Anda dapat melihat kode lengkap di bawah ini:

``````cs
using Aspose.Pdf.Plugins;
// ...

// Buat instance baru dari TextExtractor.
using TextExtractor extractor = new();

// Buat FileDataSource untuk file PDF masukan.
FileDataSource fileSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));

// Buat TextExtractorOptions.
TextExtractorOptions textExtractorOptions = new();
textExtractorOptions.AddInput(fileSource);

// Proses ekstraksi teks.
var resultContainer = extractor.Process(textExtractorOptions);
var results = resultContainer.ResultCollection;

// Cetak teks yang telah diekstrak.
Console.WriteLine(results[0]);

```

