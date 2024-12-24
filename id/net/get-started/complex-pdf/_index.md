---
title: Membuat PDF Kompleks
linktitle: Membuat PDF Kompleks
type: docs
weight: 60
url: /id/net/complex-pdf-example/
description: Aspose.PDF untuk NET memungkinkan Anda untuk membuat dokumen yang lebih kompleks yang berisi gambar, fragmen teks, dan tabel dalam satu dokumen.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Contoh [Hello, World](/pdf/id/net/hello-world-example/) menunjukkan langkah-langkah sederhana untuk membuat dokumen PDF menggunakan C# dan Aspose.PDF. Dalam artikel ini, kita akan melihat pembuatan dokumen yang lebih kompleks dengan C# dan Aspose.PDF untuk .NET. Sebagai contoh, kita akan mengambil dokumen dari perusahaan fiktif yang mengoperasikan layanan feri penumpang.
Dokumen kita akan berisi sebuah gambar, dua fragmen teks (header dan paragraf), dan sebuah tabel. Untuk membangun dokumen seperti ini, kita akan menggunakan pendekatan berbasis DOM. Anda dapat membaca lebih lanjut di bagian [Dasar-dasar API DOM](/pdf/id/net/basics-of-dom-api/).

Jika kita membuat dokumen dari awal kita perlu mengikuti langkah-langkah tertentu:

1.
1. Tambahkan [Halaman](https://reference.aspose.com/pdf/net/aspose.pdf/page) ke objek dokumen. Jadi, sekarang dokumen kita akan memiliki satu halaman.
1. Tambahkan [Gambar](https://reference.aspose.com/pdf/net/aspose.pdf/image/methods/index) ke Halaman.
1. Buat [Fragmen Teks](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) untuk header. Untuk header kita akan menggunakan font Arial dengan ukuran font 24pt dan perataan tengah.
1. Tambahkan header ke [Paragraf](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) halaman.
1. Buat [Fragmen Teks](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) untuk deskripsi. Untuk deskripsi kita akan menggunakan font Arial dengan ukuran font 24pt dan perataan tengah.
1. Tambahkan (deskripsi) ke Paragraf halaman.
1. Buat tabel, tambahkan properti tabel.
1. Tambahkan (tabel) ke [Paragraf](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) halaman.
1. Simpan dokumen "Complex.pdf".

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).
Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

```csharp
using Aspose.Pdf.Text;
using System;
using System.IO;

namespace Aspose.Pdf.Examples
{
    public static class ExampleGetStarted
    {
        private static readonly string _dataDir = "..\\..\\..\\Samples";
public static void MakeComplexDocument()
        {
            // Inisialisasi objek dokumen
            Document document = new Document();
            // Tambah halaman
            Page page = document.Pages.Add();

            // -------------------------------------------------------------
            // Tambah gambar
            var imageFileName = System.IO.Path.Combine(_dataDir, "logo.png");
            page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

            // -------------------------------------------------------------
            // Tambah Header
            var header = new TextFragment("Rute feri baru pada Musim Gugur 2020");
            header.TextState.Font = FontRepository.FindFont("Arial");
            header.TextState.FontSize = 24;
            header.HorizontalAlignment = HorizontalAlignment.Center;
            header.Position = new Position(130, 720);
            page.Paragraphs.Add(header);

            // Tambah deskripsi
            var descriptionText = "Pengunjung harus membeli tiket secara online dan tiket terbatas hingga 5.000 per hari. Layanan feri beroperasi dengan kapasitas setengah dan jadwal yang dikurangi. Harapkan antrian.";
            var description = new TextFragment(descriptionText);
            description.TextState.Font = FontRepository.FindFont("Times New Roman");
            description.TextState.FontSize = 14;
            description.HorizontalAlignment = HorizontalAlignment.Left;
            page.Paragraphs.Add(description);


            // Tambah tabel
            var table = new Table
            {
                ColumnWidths = "200",
                Border = new BorderInfo(BorderSide.Box, 1f, Color.DarkSlateGray),
                DefaultCellBorder = new BorderInfo(BorderSide.Box, 0.5f, Color.Black),
                DefaultCellPadding = new MarginInfo(4.5, 4.5, 4.5, 4.5),
                Margin =
                {
                    Bottom = 10
                },
                DefaultCellTextState =
                {
                    Font =  FontRepository.FindFont("Helvetica")
                }
            };

            var headerRow = table.Rows.Add();
            headerRow.Cells.Add("Berangkat Kota");
            headerRow.Cells.Add("Berangkat Pulau");
            foreach (Cell headerRowCell in headerRow.Cells)
            {
                headerRowCell.BackgroundColor = Color.Gray;
                headerRowCell.DefaultCellTextState.ForegroundColor = Color.WhiteSmoke;
            }

            var time = new TimeSpan(6, 0, 0);
            var incTime = new TimeSpan(0, 30, 0);
            for (int i = 0; i < 10; i++)
            {
                var dataRow = table.Rows.Add();
                dataRow.Cells.Add(time.ToString(@"hh\:mm"));
                time=time.Add(incTime);
                dataRow.Cells.Add(time.ToString(@"hh\:mm"));
            }

            page.Paragraphs.Add(table);

            document.Save(System.IO.Path.Combine(_dataDir, "Complex.pdf"));

        }
    }
}
```

