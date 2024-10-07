---
title: Optimizer 
type: docs
weight: 80
url: /net/plugins/optimizer/
description: Cara Mengoptimalkan dan Memanipulasi File PDF dengan Aspose.PDF Optimizer
lastmod: "2024-01-24"
---

Dalam bab ini, kita akan menjelajahi cara menggunakan [Aspose.PDF Optimizer](https://products.aspose.org/pdf/net/optimizer/) untuk mengoptimalkan, mengubah ukuran, dan memutar file PDF dalam aplikasi C# Anda.
Mari kita mulai dan pelajari cara melakukan tugas-tugas ini langkah demi langkah.

## Prasyarat

Anda akan membutuhkan hal-hal berikut:

* Visual Studio 2019 atau lebih baru
* Aspose.PDF untuk .NET 24.1 atau lebih baru
* Sebuah file PDF sampel yang mengandung beberapa bidang formulir

## Mengoptimalkan File PDF

Mengoptimalkan file PDF melibatkan pengurangan ukurannya dan peningkatan kinerja. Cuplikan berikut menunjukkan cara mencapai tugas ini. Berikut cara Anda dapat mengoptimalkan file PDF:

* Buat sumber data file baru untuk file PDF masukan.
* Buat sumber data file baru untuk file PDF keluaran yang dioptimalkan.
* Buat sebuah instansi dari `OptimizeOptions`.
* Tambahkan sumber data masukan dan keluaran ke opsi optimasi.
* Tambahkan sumber data masukan dan keluaran ke opsi optimasi.
* Buat sebuah instansi dari `Optimizer` dan proses optimasi menggunakan opsi optimasi.

```cs
// Buat sumber data file baru untuk file PDF masukan.
var inputDataSource = new FileDataSource(inputPath);

// Buat sumber data file baru untuk file PDF keluaran yang dioptimalkan.
var outputDataSource = new FileDataSource("sample_optimized.pdf");

// Buat instansi baru dari OptimizeOptions.
var options = new OptimizeOptions();

// Tambahkan sumber data masukan dan keluaran ke opsi optimasi.
options.AddInput(inputDataSource);
options.AddOutput(outputDataSource);

// Buat instansi baru dari Optimizer.
var optimizer = new Optimizer();

// Proses optimasi menggunakan opsi optimasi.
optimizer.Process(options);
```

## Mengubah Ukuran File PDF

Mengubah ukuran file PDF melibatkan perubahan ukuran halamannya. Kode berikut menunjukkan cara melakukan tugas ini. Ikuti langkah-langkah ini untuk mengubah ukuran file PDF:

* Buat sumber data file baru untuk file PDF masukan.
* Buat sumber data file baru untuk file PDF masukan.
* Buat sumber data file baru untuk file PDF keluaran yang telah diubah ukurannya.
* Buat sebuah instansi dari `ResizeOptions` dan atur ukuran halaman yang diinginkan.
* Tambahkan sumber data masukan dan keluaran ke dalam opsi pengubahan ukuran.
* Buat sebuah instansi dari `Optimizer` dan proses pengubahan ukuran menggunakan opsi pengubahan ukuran.

```cs
// Buat sumber data file baru untuk file PDF masukan.
var inputDataSource = new FileDataSource("sample.pdf");

// Buat sumber data file baru untuk file PDF keluaran yang telah diubah ukurannya.
var outputDataSource = new FileDataSource("sample_resized.pdf");

// Buat instansi baru dari ResizeOptions dan atur ukuran halaman yang diinginkan.
var opt = new ResizeOptions
{
    PageSize = PageSize.PageLetter
};

// Tambahkan sumber data masukan dan keluaran ke dalam opsi pengubahan ukuran.
opt.AddInput(inputDataSource);
opt.AddOutput(outputDataSource);

// Buat instansi baru dari Optimizer.
var optimizer = new Optimizer();

// Proses pengubahan ukuran menggunakan opsi pengubahan ukuran.
optimizer.Process(opt);
```

## Memutar Halaman PDF
## Memutar Halaman PDF

Memutar halaman PDF memungkinkan Anda untuk mengubah orientasi halaman dalam dokumen PDF. Berikut cara memutar halaman PDF:

* Buat sumber data file baru untuk file PDF masukan.
* Buat sumber data file baru untuk file PDF keluaran.
* Buat sebuah instansi dari `RotateOptions` dan atur nilai rotasi.
* Tambahkan sumber data masukan dan keluaran ke opsi rotasi.
* Buat sebuah instansi dari `Optimizer` dan proses rotasi menggunakan opsi rotasi.

```cs
// Buat sumber data file baru untuk file PDF masukan.
var inputDataSource = new FileDataSource(inputPath);

// Buat sumber data file baru untuk file PDF keluaran yang dioptimalkan.
var outputDataSource = new FileDataSource("sample_optimized.pdf");

// Buat instansi baru dari OptimizeOptions.
var opt = new RotateOptions();

// Tambahkan sumber data masukan dan keluaran ke opsi optimasi.
opt.AddInput(inputDataSource);
opt.AddOutput(outputDataSource);

// Atur nilai rotasi
opt.Rotation = Rotation.on180;

// Buat instansi baru dari Optimizer.
var optimizer = new Optimizer();

// Proses optimasi menggunakan opsi optimasi.
optimizer.Process(opt)
```
## Kesimpulan

Anda telah belajar cara mengoptimalkan, mengubah ukuran, dan memutar file PDF menggunakan Plugin Optimizer Aspose.PDF dalam C#. Gabungkan teknik-teknik ini ke dalam aplikasi Anda untuk memanipulasi dokumen PDF secara efisien sesuai dengan kebutuhan Anda.
