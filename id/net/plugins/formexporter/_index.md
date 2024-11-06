---
title: Form Exporter
type: docs
weight: 50
url: id/net/plugins/formexpoter/
description: Cara Mengekspor Nilai Bidang Formulir ke File CSV menggunakan Plugin Form Exporter Aspose.PDF
lastmod: "2024-01-24"
draft: false
---

Dalam artikel ini, kami akan menunjukkan cara menggunakan [plugin Form Exporter](https://products.aspose.org/pdf/net/form-exporter/), yang dapat mengekspor nilai bidang formulir dari file PDF ke file CSV.

## Prasyarat

Anda akan membutuhkan hal-hal berikut:

* Visual Studio 2019 atau lebih baru
* Aspose.PDF untuk .NET 21.1 atau lebih baru
* Sebuah file PDF contoh yang mengandung beberapa bidang formulir

Anda dapat mengunduh pustaka Aspose.PDF untuk .NET dari situs web resmi atau menginstalnya menggunakan NuGet Package Manager di Visual Studio.

## Langkah-langkah

Langkah-langkah dasar untuk mengekspor nilai bidang formulir ke file CSV menggunakan plugin FormExporter adalah:

1. Buat sebuah objek dari kelas `FormExporter`
1. Buat sebuah objek dari kelas `FormExporterValuesToCsvOptions` dan tentukan predikat serta pemisah
1.
1. Jalankan metode `Process` dari objek `FormExporter`

Mari kita lihat bagaimana mengimplementasikan langkah-langkah ini dalam kode C#.

### Langkah 1: Buat objek dari kelas FormExporter

Kelas FormExporter adalah kelas utama yang menyediakan fungsionalitas ekspor nilai field formulir ke file CSV. Untuk menggunakannya, Anda perlu membuat instance dari kelas ini menggunakan konstruktor default:

```cs
// Buat instance dari plugin FormExporter
var plugin = new FormExporter();
```

### Langkah 2: Buat objek dari kelas FormExporterValuesToCsvOptions dan tentukan predikat serta delimiter

Kelas FormExporterValuesToCsvOptions adalah kelas pembantu yang memungkinkan Anda menentukan berbagai opsi dan parameter untuk proses ekspor, seperti predikat dan delimiter.
Kelas FormExporterValuesToCsvOptions adalah kelas bantuan yang memungkinkan Anda untuk menentukan berbagai opsi dan parameter untuk proses ekspor, seperti predikat dan pemisah.

```cs
// Buat opsi untuk mengekspor nilai-nilai bidang formulir ke CSV
var options = new FormExporterValuesToCsvOptions(
(field) => { return field is TextBoxField && field.PageIndex == 2; }, ';');
```

### Langkah 3: Tambahkan sumber data masukan dan keluaran ke objek opsi

Sumber data masukan dan keluaran adalah file PDF yang ingin Anda ekspor dari dan file CSV yang ingin Anda simpan.
Sumber data masukan dan keluaran adalah file PDF yang ingin Anda ekspor dan file CSV yang ingin Anda simpan.

```cs
// Tambahkan file masukan dan keluaran ke dalam opsi
options.AddInput(new FileDataSource("inputFileNameWithFields-1.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-2.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-3.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-4.pdf"));
options.AddOutput(new FileDataSource("outputFileName.csv"));

```

### Langkah 4: Jalankan metode Process dari objek FormExporter

Langkah terakhir adalah menjalankan metode Process dari objek FormExporter, dengan mempassing objek opsi sebagai parameter.
Langkah terakhir adalah menjalankan metode Process dari objek FormExporter, dengan mengoper objek opsi sebagai parameter.

```cs
// Memproses nilai-nilai field formulir menggunakan plugin
var resultContainer = plugin.Process(options);
var result = resultContainer.ResultCollection[0];
Console.WriteLine(result);

```

Hasilnya akan berisi informasi seperti jalur file masukan dan keluaran.
