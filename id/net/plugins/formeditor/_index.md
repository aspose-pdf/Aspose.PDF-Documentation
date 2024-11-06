---
title: Form Editor
type: docs
weight: 40
url: id/net/plugins/formeditor/
description: Bagaimana Menambah, Memperbarui, dan Menghapus Bidang Formulir dalam File PDF menggunakan Plugin Aspose.PDF
lastmod: "2024-01-24"
draft: false
---

Dalam artikel ini, kami akan menunjukkan cara menggunakan [plugin Form Editor](https://products.aspose.org/pdf/net/form-editor/), yang dapat menambah, memperbarui, dan menghapus bidang formulir dalam file PDF.

## Prasyarat

Anda akan memerlukan hal-hal berikut:

* Visual Studio 2019 atau lebih baru
* Aspose.PDF untuk .NET 24.1 atau lebih baru
* File PDF contoh yang berisi beberapa bidang formulir

Anda dapat mengunduh pustaka Aspose.PDF untuk .NET dari situs web resmi atau menginstalnya menggunakan NuGet Package Manager di Visual Studio.

## Langkah-langkah

Langkah dasar untuk menambah, memperbarui, dan menghapus bidang formulir dalam file PDF menggunakan plugin FormEditor adalah:

1. Buat objek dari kelas FormEditor
1. Buat objek dari kelas FormEditorAddOptions, FormEditorSetOptions, atau FormRemoveSelectedFieldsOptions, tergantung pada operasi yang ingin Anda lakukan
1.
1. Jalankan metode Process dari objek FormEditor

Mari kita lihat cara mengimplementasikan langkah-langkah ini dalam kode C# untuk setiap operasi.

### Langkah 1: Buat objek dari kelas FormEditor

Kelas FormEditor adalah kelas utama yang menyediakan fungsionalitas menambah, memperbarui, dan menghapus bidang formulir di file PDF. Untuk menggunakannya, Anda perlu membuat instansi menggunakan konstruktor default:

```cs
// Buat instansi dari plugin FormEditor
var plugin = new FormEditor();
```

### Langkah 2: Buat objek dari kelas FormEditorAddOptions, FormEditorSetOptions, atau FormRemoveSelectedFieldsOptions, tergantung pada operasi yang ingin Anda lakukan

Kelas `FormEditorAddOptions`, `FormEditorSetOptions`, dan `FormRemoveSelectedFieldsOptions` adalah kelas bantuan yang memungkinkan Anda menentukan berbagai opsi dan parameter untuk operasi pengeditan formulir, seperti tipe bidang formulir, nilai, properti, predikat, dll.
Kelas `FormEditorAddOptions`, `FormEditorSetOptions`, dan `FormRemoveSelectedFieldsOptions` adalah kelas pembantu yang memungkinkan Anda untuk menentukan berbagai opsi dan parameter untuk operasi pengeditan formulir, seperti jenis bidang formulir, nilai, properti, predikat, dll.

```cs
    // Membuat opsi untuk menambahkan bidang formulir.
    var options = new FormEditorAddOptions(
        [
            // Membuat bidang formulir kotak centang.
            new FormCheckBoxFieldCreateOptions(1, new Rectangle(110, 700, 125, 715))
            {
                Value = "CheckBoxField 1",
                PartialName = "CheckBoxField_1",
                Color = Color.Blue,
            },
            // Membuat bidang formulir kotak kombinasi.
            new FormComboBoxFieldCreateOptions(1, new Rectangle(310, 600, 350, 615))
            {
                Color = Color.Red,
                Editable = true,
                DefaultAppearance = new DefaultAppearance("Arial Bold", 12, System.Drawing.Color.DarkGreen),
                Options = ["option1", "option2", "option3"],
                Selected = 2
            },
            // Membuat bidang formulir kotak teks.
            new FormTextBoxFieldCreateOptions(1, new Rectangle(10, 700, 90, 715))
            {
                MaxLen = 10,
                Value = "Some text",
                Color = Color.Chocolate
            }
        ]);
```
Untuk memperbarui nilai dari bidang formulir yang nilainya "a value" atau "an another value" menjadi "new value", Anda dapat menggunakan kode berikut:

```cs
    var options = new FormEditorSetOptions(
    (field) => { return field.Value == "a value" || field.Value == "an another value"; },
    new FormFieldSetOptions()
    {
        Value = "new value"
    });
```

Untuk menghapus bidang formulir yang koordinat x pojok kiri bawahnya lebih besar dari 300, Anda dapat menggunakan kode berikut:

```cs
// Buat opsi untuk menghapus bidang formulir
var options = new FormRemoveSelectedFieldsOptions((field) => field.Rect.LLX > 300);
```

### Langkah 3: Tambahkan sumber data masukan dan keluaran ke objek opsi

Sumber data masukan dan keluaran adalah file PDF yang ingin Anda edit dan simpan.
Sumber data input dan output adalah file PDF yang ingin Anda edit dan simpan.

```cs
// Tentukan jalur file input dan output
string inputPath = $@"C:\Samples\Output\sample_forms.pdf";
string outputPath = $@"C:\Samples\Output\sample_forms2.pdf";

// Buat instance baru dari kelas FileDataSource untuk file input dan output
FileDataSource inputData = new(inputPath);
FileDataSource outputData = new(outputPath);

// Tambahkan sumber data input dan output ke dalam opsi
options.AddInput(inputData);
options.AddOutput(outputData);
```

### Langkah 4: Jalankan metode Process dari objek FormEditor

Langkah terakhir adalah menjalankan metode Process dari objek FormEditor, dengan melewatkan objek opsi sebagai parameter.
Langkah terakhir adalah menjalankan metode Proses dari objek FormEditor, dengan melewatkan objek opsi sebagai parameter.

```cs
// Memproses operasi pengeditan formulir menggunakan plugin dan opsi
ResultContainer result = plugin.Process(options);

// Dapatkan hasil pertama dari kumpulan hasil
var result = resultContainer.ResultCollection[0];

// Cetak hasilnya
Console.WriteLine(result);
```

Hasilnya akan berisi informasi seperti jalur file keluaran.
