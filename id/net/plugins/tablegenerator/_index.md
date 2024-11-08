---
title: Table Generator
type: docs
weight: 130
url: /id/net/plugins/tablegenerator/
description: Memungkinkan menambahkan/memasukkan tabel pada nomor halaman tertentu dari dokumen PDF.
lastmod: "2024-01-24"
draft: false
---

Apakah Anda perlu membuat tabel yang dinamis dan visual menarik di dokumen PDF Anda menggunakan .NET? Aspose.PDF untuk .NET menyediakan kelas TableGenerator yang mempermudah prosesnya. Dalam bab ini, kita akan membahas langkah-langkah untuk menghasilkan tabel dalam dokumen PDF menggunakan [Aspose.PDF Table Generator](https://products.aspose.org/pdf/net/table-generator/), mulai dari membuat dokumen demo hingga menghasilkan tabel dengan kelas TableGenerator.
Mari selami dan pelajari cara menghasilkan tabel langkah demi langkah.

## Prasyarat

Anda akan memerlukan yang berikut ini:

* Visual Studio 2019 atau lebih baru
* Aspose.PDF untuk .NET 24.3 atau lebih baru
* Sebuah file PDF contoh

## Membuat Dokumen Demo

Sebelum kita mulai menghasilkan tabel, mari kita buat dokumen demo dengan halaman kosong di mana tabel kita akan dimasukkan.
Sebelum kita mulai membuat tabel, mari kita buat dokumen demo dengan halaman kosong di mana tabel kita akan dimasukkan.

* Buat dokumen PDF baru.
* Tambahkan halaman kosong ke dalam dokumen.
* Simpan dokumen ke file yang ditentukan.

```cs
// <summary>
// Membuat dokumen demo dengan halaman kosong.
//
// Parameter:
// - fileName: Jalur dan nama file keluaran.
// </summary>
internal static void CreateDemoDocument(string fileName)
{
    // Buat dokumen PDF baru.
    var document = new Aspose.Pdf.Document();

    // Tambahkan empat halaman kosong ke dalam dokumen.
    for (int i = 0; i < 2; i++)
    {
        document.Pages.Add();
    }

    // Simpan dokumen ke file yang ditentukan.
    document.Save(fileName);
}
```

## Membuat Tabel

Setelah dokumen demo kita siap, kita dapat mulai membuat tabel menggunakan kelas `TableGenerator`. Cuplikan berikut menunjukkan cara membuat tabel dengan berbagai jenis konten dan opsi pemformatan. Berikut cara membuat tabel:

* Buat instance baru dari kelas `TableGenerator`.
* Buat instance baru dari kelas `TableGenerator`.
* Buat opsi tabel dan tentukan sumber data file masukan dan keluaran.
* Tambahkan tabel dengan baris dan sel ke dalam opsi, menentukan konten dan format.
* Proses pembuatan tabel menggunakan metode `Process` dan dapatkan kontainer hasilnya.

### Membuat Tabel

Untuk membuat tabel menggunakan Aspose.PDF, ikuti langkah-langkah berikut:

```cs
// Buat instance baru dari kelas TableGenerator.
var generator = new TableGenerator();

// Buat opsi tabel dan tambahkan tabel demo.
var options = new TableOptions();

// Tambahkan sumber data file masukan dan keluaran ke dalam opsi.
options.AddInput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));
options.AddOutput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));

// Tambahkan tabel pertama ke dalam opsi.
options
    .InsertPageAfter(1)
    .AddTable()
```

Dalam kode di atas, kita membuat instance dari `TableOptions` dan menentukan sumber data file masukan dan keluaran untuk dokumen PDF.
Dalam kode di atas, kami membuat sebuah instance dari `TableOptions` dan menentukan sumber data file masukan dan keluaran untuk dokumen PDF.

### Menambahkan Konten ke Tabel

Setelah tabel dibuat, Anda dapat mengisinya dengan baris dan sel yang berisi berbagai jenis konten, seperti teks, HTML, gambar, dll. Berikut cara menambahkan konten ke tabel:

```csharp
options
    .AddTable()
        .AddRow()
            .AddCell()
                .AddParagraph(new HtmlFragment("<h1>Header 1</h1>")) // Menambahkan konten HTML ke sel.
            .AddCell()
                .AddParagraph(new HtmlFragment("<h2>Header 2</h2>"))
            .AddCell()
                .AddParagraph(new HtmlFragment("<h3>Header 3</h3>"));
```

Dalam contoh ini, kami menambahkan sebuah baris ke tabel dan mengisinya dengan sel yang berisi fragmen HTML yang mewakili header.

Metode yang berguna:

* **InsertPageAfter**: Menyisipkan halaman setelah nomor halaman yang ditentukan.
* **InsertPageBefore**: Menyisipkan halaman setelah nomor halaman yang ditentukan.
* **AddTable**: Menambahkan tabel ke dokumen.
* **AddTable**: Menambahkan tabel ke dokumen.
* **AddRow**: Menambahkan baris ke tabel.
* **AddCell**: Menambahkan sel ke baris.
* **AddParagraph**: Menambahkan konten ke sel.

Anda dapat menambahkan jenis konten berikut sebagai paragraf:

* **HtmlFragment** - konten berbasis markup HTML
* **TeXFragment** - konten berbasis markup TeX/LaTeX
* **TextFragment** - konten teks sederhana
* **Image** - grafis

## Melakukan pembuatan tabel

Setelah menambahkan konten, kita dapat mulai membuat tabel.

```cs
// Proses pembuatan tabel dan dapatkan wadah hasil.
var resultContainer = generator.Process(options);

// Print jumlah hasil di koleksi hasil.
Console.WriteLine(resultContainer.ResultCollection.Count);
```

Metode `Process` melakukan pembuatan tabel. Metode ini juga dapat dibungkus dengan try-catch untuk menangani kesalahan.

Di bawah ini Anda dapat melihat kode lengkap dari contoh:

```cs
using Aspose.Pdf;
using Aspose.Pdf.Plugins;
using Aspose.Pdf.Text;

namespace AsposePluginsNet8.Documentation
{
    // <summary>
    // Mewakili kelas yang mendemonstrasikan penggunaan pembuatan tabel di Aspose.Pdf.
    // </summary>
    internal static class TableDemo
    {
        // <summary>
        // Menjalankan demo pembuatan tabel.
        // </summary>
        internal static void Run()
        {
            // Membuat dokumen demo dan menghasilkan tabel.
            CreateDemoDocument(@"C:\Samples\Results\table-generator-demo.pdf");
            CreateDemoTable();
        }

        // <summary>
        // Membuat dokumen demo dengan empat halaman kosong.
        //
        // Parameters:
        // - fileName: Jalur dan nama file keluaran.
        // </summary>
        internal static void CreateDemoDocument(string fileName)
        {
            // Membuat dokumen PDF baru.
            var document = new Aspose.Pdf.Document();

            // Menambahkan empat halaman kosong ke dokumen.
            for (int i = 0; i < 2; i++)
            {
                document.Pages.Add();
            }

            // Menyimpan dokumen ke file yang ditentukan.
            document.Save(fileName);
        }

        // <summary>
        // Menghasilkan tabel menggunakan kelas TableGenerator.
        // </summary>
        internal static void CreateDemoTable()
        {
            // Membuat instance baru dari kelas TableGenerator.
            var generator = new TableGenerator();

            // Membuat opsi tabel dan menambahkan tabel demo.
            var options = new TableOptions();

            // Menambahkan sumber data file input dan output ke opsi.
            options.AddInput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));
            options.AddOutput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));

            // Menambahkan tabel pertama ke opsi.
            options
                .InsertPageAfter(1)
                .AddTable()
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h1>Header 1</h1>"))
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h2>Header 2</h2>"))
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h3>Header 3</h3>"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TeXFragment("{\\small The equation $E=mc^2$, discovered in 1905 by Albert Einstein.}", true))
                        .AddCell()
                            .AddParagraph(new TextFragment("Sel 2 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Sel 2 3"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TextFragment("Sel 3 1a"))
                            .AddParagraph(new TextFragment("Sel 3 1b"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Sel 3 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Sel 3 3"));

            // Menambahkan tabel kedua ke opsi.
            options
                .InsertPageBefore(2)
                .AddTable()
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TextFragment("Header 1 1"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Header 1 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Header 1 3"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                File = @"C:\Samples\logo.png",
                                FixWidth = 75,
                                FixHeight = 75,
                            })
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                File = @"C:\Samples\sample.svg",
                                FileType = ImageFileType.Svg,
                                FixWidth = 75,
                                FixHeight = 75
                            })
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                ImageStream = File.OpenRead(@"C:\Samples\Conversion\Demo.dcm"),
                                FileType = ImageFileType.Dicom,
                                FixWidth = 75,
                                FixHeight = 75
                            });

            // Proses pembuatan tabel dan dapatkan wadah hasil.
            var resultContainer = generator.Process(options);

            // Print jumlah hasil di koleksi hasil.
            Console.WriteLine(resultContainer.ResultCollection.Count);
        }
    }
}
```

