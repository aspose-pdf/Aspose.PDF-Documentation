---
title: Form Exporter
type: docs
weight: 60
url: /net/plugins/formflattener/
description: Cara Meratakan Bidang Formulir dalam Berkas PDF menggunakan Plugin FormFlattener Aspose.PDF
lastmod: "2024-01-24"
---

Dalam artikel ini, kami akan menunjukkan cara menggunakan [plugin FormFlattener](https://products.aspose.org/pdf/net/form-flattener/), yang dapat meratakan bidang formulir dalam berkas PDF.

## Prasyarat

Anda akan membutuhkan hal-hal berikut:

* Visual Studio 2019 atau lebih baru
* Aspose.PDF untuk .NET 21.1 atau lebih baru
* Berkas PDF sampel yang mengandung beberapa bidang formulir

Anda dapat mengunduh pustaka Aspose.PDF untuk .NET dari situs web resmi atau menginstalnya menggunakan NuGet Package Manager di Visual Studio.

## Langkah-langkah

Langkah dasar untuk meratakan bidang formulir dalam berkas PDF menggunakan plugin FormFlattener adalah:

1. Buat objek dari kelas FormFlattener
1. Buat objek dari kelas FormFlattenAllFieldsOptions atau FormFlattenSelectedFieldsOptions, tergantung apakah Anda ingin meratakan semua atau beberapa bidang
1. Jalankan metode Process dari objek FormFlattener

Mari kita lihat bagaimana mengimplementasikan langkah-langkah ini dalam kode C#.

### Langkah 1: Buat objek dari kelas FormFlattener

Kelas FormFlattener adalah kelas utama yang menyediakan fungsionalitas untuk meratakan field formulir dalam file PDF. Untuk menggunakannya, Anda perlu membuat sebuah instansi menggunakan konstruktor default:

```cs
// Buat sebuah instansi dari plugin FormFlattener
var plugin = new FormFlattener();
```

### Langkah 2: Buat objek dari kelas FormFlattenAllFieldsOptions atau FormFlattenSelectedFieldsOptions, tergantung apakah Anda ingin meratakan semua atau beberapa field

Kelas FormFlattenAllFieldsOptions dan FormFlattenSelectedFieldsOptions adalah kelas bantuan yang memungkinkan Anda untuk menentukan berbagai opsi dan parameter untuk proses perataan.
Kelas FormFlattenAllFieldsOptions dan FormFlattenSelectedFieldsOptions adalah kelas bantuan yang memungkinkan Anda menentukan berbagai opsi dan parameter untuk proses perataan.

```cs
// Buat opsi untuk meratakan semua bidang
var options = new FormFlattenAllFieldsOptions();
```

Untuk meratakan hanya bidang formulir yang koordinat x kiri bawahnya lebih dari 300, Anda dapat menggunakan kode berikut:

```cs
// Buat opsi untuk meratakan bidang terpilih
var options = new FormFlattenSelectedFieldsOptions((field) => field.Rect.LLX > 300);
```

### Step 3: Add the input and output data sources to the options object

Sumber data masukan dan keluaran adalah file PDF yang ingin Anda ratakan dan simpan.
Sumber data masukan dan keluaran adalah file PDF yang ingin Anda datarkan dan simpan.

```cs
// Tambahkan sumber data masukan dan keluaran ke dalam opsi
options.Inputs.Add(new FileDataSource("sample.pdf"));
options.Outputs.Add(new FileDataSource("sample-flat.pdf"));
```

### Langkah 4: Jalankan method Process dari objek FormFlattener

Langkah terakhir adalah menjalankan method Process dari objek FormFlattener, dengan melewatkan objek opsi sebagai parameter. Method ini akan melakukan proses pendataran dan mengembalikan objek ResultContainer, yang mengandung hasil dari proses tersebut, seperti status, pesan, sumber data keluaran, dll. Anda dapat mengakses hasil menggunakan properti dan metode dari kelas ResultContainer. Misalnya, untuk mendapatkan hasil pertama dari koleksi hasil dan mencetaknya ke konsol, Anda dapat menggunakan kode berikut:

```cs
// Proses opsi dan dapatkan wadah hasil
var resultContainer = plugin.Process(options);

// Dapatkan hasil pertama dari wadah hasil
var result = resultContainer.ResultCollection[0];

// Cetak hasil
Console.WriteLine(result);
```
Hasilnya akan berisi informasi seperti jalur file keluaran.
