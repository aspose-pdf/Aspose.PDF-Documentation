---
title: Splitter
type: docs
weight: 120
url: id/net/plugins/splitter/
description: Memisahkan dokumen PDF menjadi halaman terpisah
lastmod: "2024-01-24"
draft: false
---

Apakah Anda memiliki dokumen PDF besar yang ingin Anda pecah menjadi file yang lebih kecil dan lebih mudah dikelola? Dengan [Aspose.PDF Splitter untuk .NET](https://products.aspose.org/pdf/net/splitter/), Anda dapat dengan mudah mencapai tugas ini. Dalam artikel ini, kita akan menjelajahi proses memecah dokumen PDF menjadi beberapa file menggunakan plugin Aspose.PDF. Mari kita menyelami kode dan melalui langkah-langkahnya.

## Prasyarat

Anda akan membutuhkan hal berikut:

* Visual Studio 2019 atau lebih baru
* Aspose.PDF untuk .NET 24.1 atau lebih baru
* Sebuah file PDF sampel

Selain itu, biasakan diri Anda dengan kelas `SplitOptions` dan propertinya. Anda dapat menemukan informasi terperinci tentang kelas ini di [Referensi API](https://reference.aspose.com/pdf/net/aspose.pdf/SplitOptions/). Perhatikan bahwa setiap `FileDataSource` keluaran mewakili satu halaman dalam file PDF yang dipisahkan.

Sekarang, mari kita jelajahi kode yang disediakan dan memahami cara memecah dokumen PDF.
Sekarang, mari kita jelajahi kode yang disediakan dan pahami cara membagi dokumen PDF.

## Penjelasan Kode

Kode di bawah ini menunjukkan demo pemisahan PDF menggunakan Aspose.PDF.Plugins:

```csharp
using Aspose.Pdf.Plugins;
// ...........

// Tentukan jalur masukan dokumen PDF yang akan dipisah.
using var inputStream = File.OpenRead(Path.Combine(@"C:\Samples\", "sample.pdf"));

// Buat instance baru dari Splitter.
var splitter = new Splitter();

// Buat opsi untuk memisahkan dokumen.
var options = new SplitOptions();

// Tambahkan sumber data masukan dan keluaran ke dalam opsi.
options.AddInput(new StreamDataSource(inputStream));

var document = new Aspose.Pdf.Document(inputStream);

for (int i = 1; i <= document.Pages.Count; i++)
{
   var pageNum = string.Format("{0,3}", i.ToString("D3"));
   options.AddOutput(new FileDataSource(Path.Combine(@"C:\Samples\", $"splitter_{pageNum}.pdf")));
}

// Proses opsi untuk memisahkan dokumen.
var result = splitter.Process(options);
Console.WriteLine(result);
```

Mari kita uraikan langkah-langkah kuncinya:
Mari kita uraikan langkah-langkah kuncinya:

1. **Tetapkan PDF Input**

   Kode dimulai dengan menentukan jalur dokumen PDF input yang akan dipisahkan. Ini dilakukan menggunakan metode `File.OpenRead`.

2. **Buat Objek (Splitter dan SplitOptions)**

   Kode membuat instance dari kelas `Splitter` untuk menangani proses pemisahan. Selain itu, sebuah instance dari kelas `SplitOptions` dibuat untuk mengkonfigurasi operasi pemisahan.

3. **Tambahkan Sumber Data (Input dan Output)**

   Dokumen PDF input ditambahkan ke `SplitOptions` sebagai sumber data input menggunakan metode `AddInput`. Untuk setiap halaman dalam dokumen, jalur file output ditambahkan sebagai sumber data output menggunakan metode `AddOutput`.

4. **Jalankan Metode Proses**

   Proses pemisahan diinisiasi dengan memanggil metode `Process` pada kelas `Splitter`, dengan mengirimkan `SplitOptions` yang telah dikonfigurasi. Hasil operasi disimpan dalam variabel `result`.

5. **Tangani Hasil**

   Kode mencetak hasil ke konsol, memberikan informasi tentang proses pemisahan.
Kode tersebut mencetak hasil ke konsol, memberikan informasi tentang proses pemisahan.
