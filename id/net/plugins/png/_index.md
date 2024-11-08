---
title: PNG converter
type: docs
weight: 110
url: /id/net/plugins/png/
description: Mengonversi Dokumen PDF menjadi Gambar PNG dengan Plugin Aspose.PDF PNG
lastmod: "2024-01-24"
---

Jika Anda ingin [mengonversi dokumen PDF menjadi gambar PNG](https://products.aspose.org/pdf/net/png-converter/) menggunakan .NET, Aspose.PDF untuk .NET menyediakan solusi yang kuat. Dalam artikel ini, kita akan membahas langkah-langkah penting untuk membuat objek, menambahkan sumber data, dan menjalankan metode proses menggunakan pustaka Aspose.PDF.

## Prasyarat

Anda akan memerlukan hal berikut:

* Visual Studio 2019 atau lebih baru
* Aspose.PDF untuk .NET 24.1 atau lebih baru
* Sebuah file PDF contoh

## Penjelasan Kode

Kode di bawah ini mendemonstrasikan demo konversi PNG menggunakan Plugin Aspose.PDF PNG:

```csharp
using Aspose.Pdf.Plugins;

//....

// Buat instance baru dari kelas PngOptions.
var convertorOptions = new PngOptions();

// Tambahkan jalur input dan output ke PngOptions.
convertorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));
convertorOptions.AddOutput(new FileDataSource(Path.Combine(@"C:\Samples\", "images")));

// Atur resolusi output menjadi 300 DPI.
convertorOptions.OutputResolution = 300;

// Buat instance baru dari kelas Png.
Png converter = new ();

// Proses konversi PNG dan dapatkan wadah hasil.
ResultContainer resultContainer = converter.Process(convertorOptions);

// Cetak hasil ke konsol.
foreach (FileResult operationResult in resultContainer.ResultCollection.Cast<FileResult>())
{
      Console.WriteLine(operationResult.Data.ToString());
}
```
Mari kita uraikan langkah-langkah kunci:

1. **Buat sebuah Objek (PngOptions dan Png)**

   Kode dimulai dengan membuat sebuah instansi dari kelas `PngOptions` untuk mengkonfigurasi konversi PNG. Selain itu, sebuah instansi dari kelas `Png` dibuat untuk proses lebih lanjut.

2. **Tambahkan Sumber Data**

   Jalur file PDF input ditambahkan ke `PngOptions` menggunakan metode `AddInput`. Secara serupa, jalur keluaran untuk gambar PNG ditambahkan menggunakan metode `AddOutput`.

3. **Atur Resolusi Keluaran**

   Kode mengatur resolusi keluaran menjadi 300 DPI menggunakan properti `OutputResolution` dari kelas `PngOptions`.

4. **Jalankan Metode Proses**

   Konversi PNG diinisiasi dengan memanggil metode `Process` pada kelas `Png`, dengan mengoper kembali `PngOptions` yang telah dikonfigurasi. Hasilnya disimpan di dalam `resultContainer`.

5. **Tangani Hasil**

   Kode mencetak hasil ke konsol, menampilkan jalur file yang telah dikonversi.
