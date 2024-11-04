---
title: DOC Converter
type: docs
weight: 10
url: /net/plugins/doc/
description: Mengubah PDF ke Word Dibuat Sederhana dengan Plugin PdfDoc
lastmod: "2024-01-24"
---

Artikel ini akan memandu Anda menggunakan [Aspose.Pdf DOC Converter untuk .NET](https://products.aspose.org/pdf/net/doc-converter/) untuk mengonversi dokumen PDF menjadi format Microsoft Word (.doc / .docx).

## Prasyarat

Anda akan membutuhkan hal-hal berikut:

* Visual Studio 2019 atau lebih baru
* Aspose.PDF untuk .NET 24.1 atau lebih baru
* Sebuah file PDF contoh yang mengandung beberapa bidang formulir

Anda dapat mengunduh pustaka Aspose.PDF untuk .NET dari situs web resmi atau menginstalnya menggunakan NuGet Package Manager di Visual Studio.

## Langkah-langkah

### 1. Menyiapkan Konversi Anda (tangkapan layar dari kelas FileDataSource)

Proses konversi melibatkan tiga langkah utama: mendefinisikan file masukan dan keluaran, membuat objek `PdfDoc`, dan menentukan opsi konversi.

#### 1.1. Mendefinisikan Sumber Data

* **File Masukan:** Kami akan menggunakan kelas `FileDataSource` untuk menentukan lokasi file PDF yang ingin Anda konversi.
* **Berkas Masukan:** Kita akan menggunakan kelas `FileDataSource` untuk menentukan lokasi berkas PDF yang ingin Anda konversi.

```csharp
  FileDataSource inputDataSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));
```

  * Ganti `"C:\Samples\sample.pdf"` dengan jalur sebenarnya ke berkas PDF Anda.

* **Berkas Keluaran:** Sama seperti itu, gunakan objek `FileDataSource` lain untuk menentukan lokasi dan nama berkas untuk dokumen Word hasil konversi.

```csharp
  FileDataSource outputDataSource = new(Path.Combine(@"C:\Samples\", "sample.docx"));
```

* Ganti `"C:\Samples\sample.docx"` dengan jalur keluaran dan nama berkas yang Anda inginkan.

### 2. Membuat Objek Plugin PdfDoc (tangkapan layar kelas PdfDoc)

Selanjutnya, kita membuat sebuah instansi dari kelas `PdfDoc` untuk melakukan konversi.

```csharp
  var plugin = new PdfDoc();
```

Objek ini berfungsi sebagai mesin untuk proses konversi.

### 3. Mengkonfigurasi Opsi Konversi

Kelas `PdfToDocOptions` memungkinkan Anda untuk menyempurnakan proses konversi.
Kelas `PdfToDocOptions` memungkinkan Anda untuk menyesuaikan proses konversi.

* **Save Format:** Tentukan format keluaran yang diinginkan untuk dokumen Word. Dalam hal ini, kita menggunakan `SaveFormat.DocX` untuk menghasilkan dokumen yang kompatibel dengan Microsoft Word 2007 atau lebih baru (.docx).

* **Conversion Mode:** Tentukan bagaimana plugin menginterpretasikan struktur PDF selama konversi. Kita akan menggunakan `ConversionMode.EnhancedFlow` untuk mengoptimalkan dokumen Word yang dihasilkan dalam hal tata letak dan pemformatan.

Berikut adalah potongan kode untuk mengonfigurasi opsi:

```csharp
  PdfToDocOptions options = new()
  {
      SaveFormat = SaveFormat.DocX,
      ConversionMode = ConversionMode.EnhancedFlow
  };
```

**Menambahkan Input dan Output:**

Terakhir, kita mengaitkan sumber data yang telah didefinisikan sebelumnya dengan opsi konversi menggunakan metode `AddInput` dan `AddOutput`:

```csharp
  options.AddInput(inputDataSource);
  options.AddOutput(outputDataSource);
```

Ini menghubungkan PDF input dan dokumen Word keluaran yang diinginkan ke proses konversi.

### 4.
### 4.

Dengan semuanya sudah diatur, mari kita mulai konversi dengan memanggil metode `Process` dari plugin `PdfDoc` dan mengoper parameter yang telah dikonfigurasi:

```csharp
  var resultContainer = plugin.Process(options);
```

Metode ini melakukan konversi dan mengembalikan objek `ResultContainer` yang berisi detail tentang proses tersebut.

**Mengambil Hasil:**

Meskipun tidak esensial untuk konversi dasar, Anda dapat mengakses hasil melalui properti `ResultCollection` dari objek `ResultContainer`. Ini mungkin berguna untuk debugging atau melacak detail konversi tertentu.

```csharp
  var result = resultContainer.ResultCollection[0];

  // Cetak hasil (opsional untuk tujuan demonstrasi)
  Console.WriteLine(result);
```

Dengan langkah terakhir ini, dokumen PDF Anda akan dikonversi ke format Word yang ditentukan dan disimpan ke lokasi output yang telah ditentukan.

