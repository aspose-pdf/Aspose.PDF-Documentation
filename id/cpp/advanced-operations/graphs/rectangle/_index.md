---
title: Tambahkan Objek Persegi Panjang ke File PDF
linktitle: Tambahkan Persegi Panjang
type: docs
weight: 50
url: /id/cpp/add-rectangle/
description: Artikel ini menjelaskan cara membuat objek Persegi Panjang ke PDF Anda menggunakan Aspose.PDF untuk C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Tambahkan objek Persegi Panjang

Aspose.PDF untuk C++ mendukung fitur untuk menambahkan objek grafis (misalnya grafik, garis, persegi panjang dll.) ke dokumen PDF. Anda juga mendapatkan keleluasaan untuk menambahkan objek [Persegi Panjang](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) di mana Anda juga menawarkan fitur untuk mengisi objek persegi panjang dengan warna tertentu, mengontrol Z-Order, menambahkan isi warna gradasi dan lain-lain.

Pertama, mari kita lihat kemungkinan membuat objek Persegi Panjang.

Ikuti langkah-langkah di bawah ini:

1. Buat [Dokumen](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) PDF baru

1. Tambahkan [Halaman](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page/) ke koleksi halaman file PDF

1. Tambahkan [Fragmen Teks](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/) ke koleksi paragraf dari instance halaman

1. Buat instance [Grafik](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph/)

1. Atur batas untuk [Objek Gambar](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing)

1. Buat instance Persegi Panjang

1. Tambahkan objek [Persegi Panjang](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) ke koleksi bentuk dari objek Grafik

1. Tambahkan objek grafik ke koleksi paragraf dari instance halaman

1. Tambahkan [Fragmen Teks](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/) ke koleksi paragraf dari instance halaman

1. Dan simpan file PDF Anda

```csharp
 private static void AddRectangle(Page page, float x, float y, float width, float height, Color color, int zindex)
        {
            // Buat objek grafik dengan dimensi yang sama seperti yang ditentukan untuk objek Persegi Panjang
            Aspose.Pdf.Drawing.Graph graph = new Aspose.Pdf.Drawing.Graph(width, height)
            {
                // Bisakah kita mengubah posisi instance grafik
                IsChangePosition = false,
                // Atur posisi koordinat Kiri untuk instance Grafik
                Left = x,
                // Atur posisi koordinat Atas untuk objek Grafik
                Top = y
            };
            // Tambahkan persegi panjang di dalam "grafik"
            Rectangle rect = new Rectangle(0, 0, width, height);
            // Atur warna isi persegi panjang
            rect.GraphInfo.FillColor = color;
            // Warna dari objek grafik
            rect.GraphInfo.Color = color;
            // Tambahkan persegi panjang ke koleksi bentuk dari instance grafik
            graph.Shapes.Add(rect);
            // Atur Z-Index untuk objek persegi panjang
            graph.ZIndex = zindex;
            // Tambahkan grafik ke koleksi paragraf dari objek halaman
            page.Paragraphs.Add(graph);
        }
```
![Buat Persegi Panjang](create_rectangle.png)

## Membuat Objek Persegi Panjang Berisi

Aspose.PDF untuk C++ juga menawarkan fitur untuk mengisi objek persegi panjang dengan warna tertentu.

Cuplikan kode berikut menunjukkan cara menambahkan objek [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) yang diisi dengan warna.

```csharp
    {
        private const string _dataDir = "C:\\Samples\\";
        public static void RectangleFilled()
        {
            // Membuat instance Dokumen
            var doc = new Document();

            // Menambahkan halaman ke koleksi halaman file PDF
            var page = doc.Pages.Add();
            // Membuat instance Grafik
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

            // Menambahkan objek grafik ke koleksi paragraf dari instance halaman
            page.Paragraphs.Add(graph);

            // Membuat instance Persegi Panjang
            var rect = new Rectangle(100, 100, 200, 120);

            // Menentukan warna isi untuk objek Grafik
            rect.GraphInfo.FillColor = Color.Red;

            // Menambahkan objek persegi panjang ke koleksi bentuk dari objek Grafik
            graph.Shapes.Add(rect);

            // Menyimpan file PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```

Lihat hasil dari persegi panjang yang diisi dengan warna solid:

![Persegi Panjang Terisi](fill_rectangle.png)

## Tambahkan Gambar dengan Isi Gradasi

Aspose.PDF untuk C++ mendukung fitur untuk menambahkan objek grafik ke dokumen PDF dan terkadang diperlukan untuk mengisi objek grafik dengan Warna Gradasi. Untuk Mengisi objek grafik dengan Warna Gradasi, Kita perlu mengatur setPatterColorSpace dengan objek gradientAxialShading sebagai berikut.

Cuplikan kode berikut menunjukkan cara menambahkan objek [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) yang diisi dengan Warna Gradasi.

```csharp
 public static void CreateFilledRectangletGradientFill()
        {
            // Buat instance Dokumen
            var doc = new Document();

            // Tambahkan halaman ke koleksi halaman dari file PDF
            var page = doc.Pages.Add();
            // Buat instance Grafis
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // Tambahkan objek grafik ke koleksi paragraf dari instance halaman
            page.Paragraphs.Add(graph);
            // Buat instance Persegi Panjang
            var rect = new Rectangle(0, 0, 300, 300);
            // Tentukan warna isi untuk objek Grafis
            var gradientColor = new Color();
            var gradientSettings = new GradientAxialShading(Color.Red, Color.Blue)
            {
                Start = new Point(0, 0),
                End = new Point(350, 350)
            };
            gradientColor.PatternColorSpace = gradientSettings;
            rect.GraphInfo.FillColor = gradientColor;

            // Tambahkan objek persegi panjang ke koleksi bentuk dari objek Grafis
            graph.Shapes.Add(rect);

            // Simpan file PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```

![Gradient Rectangle](gradient.png)

## Membuat Persegi Panjang dengan Saluran Warna Alpha

Aspose.PDF untuk C+++ mendukung pengisian objek persegi panjang dengan warna tertentu. Objek persegi panjang juga dapat memiliki saluran warna Alpha untuk memberikan tampilan transparan. Cuplikan kode berikut menunjukkan cara menambahkan objek [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) dengan saluran warna Alpha.

Piksel dari gambar dapat menyimpan informasi tentang opasitas mereka bersama dengan nilai warna. Ini memungkinkan pembuatan gambar dengan area transparan atau semi-transparan.

Alih-alih membuat warna transparan, setiap piksel menyimpan informasi tentang seberapa buram itu. Data opasitas ini disebut saluran alpha dan biasanya disimpan setelah saluran warna dari piksel.

```csharp
     public static void RectangleFilled_AlphaChannel()
        {
            // Buat instance Dokumen
            var doc = new Document();

            // Tambahkan halaman ke koleksi halaman file PDF
            var page = doc.Pages.Add();
            // Buat instance Grafik
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);
            // Tambahkan objek grafik ke koleksi paragraf dari halaman
            page.Paragraphs.Add(graph);
            // Buat instance Persegi Panjang
            var rect = new Rectangle(100, 100, 200, 120);
            // Tentukan warna pengisian untuk objek Grafik
            rect.GraphInfo.FillColor = Color.FromArgb(128, 244, 180, 0);

            // Tambahkan objek persegi panjang ke koleksi bentuk dari objek Grafik
            graph.Shapes.Add(rect);

            // Buat objek persegi panjang kedua
            var rect1 = new Rectangle(200, 150, 200, 100);
            rect1.GraphInfo.FillColor = Color.FromArgb(160, 120, 0, 120);
            graph.Shapes.Add(rect1);

            // Tambahkan instance grafik ke koleksi paragraf dari objek halaman
            page.Paragraphs.Add(graph);

            // Simpan file PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```

![Rectangle Alpha Channel Color](rectangle_color.png)

## Kontrol Z-Order dari Persegi Panjang

Aspose.PDF untuk C++ mendukung fitur untuk menambahkan objek grafis (misalnya grafik, garis, persegi panjang dll.) ke dokumen PDF. Ketika menambahkan lebih dari satu instance dari objek yang sama dalam file PDF, kita dapat mengontrol rendering mereka dengan menentukan Z-Order. Z-Order juga digunakan ketika kita perlu merender objek saling tumpang tindih.

Cuplikan kode berikut menunjukkan langkah-langkah untuk merender objek [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) saling tumpang tindih.

```csharp
 public static void AddRectangleZOrder()
        {
            // Instansiasi objek kelas Document
            Document doc1 = new Document();
            /// Tambahkan halaman ke koleksi halaman dari file PDF
            Page page1 = doc1.Pages.Add();
            // Atur ukuran halaman PDF
            page1.SetPageSize(375, 300);
            // Atur margin kiri untuk objek halaman sebagai 0
            page1.PageInfo.Margin.Left = 0;
            // Atur margin atas dari objek halaman sebagai 0
            page1.PageInfo.Margin.Top = 0;
            // Buat persegi panjang baru dengan Warna Merah, Z-Order 0 dan dimensi tertentu
            AddRectangle(page1, 50, 40, 60, 40, Color.Red, 2);
            // Buat persegi panjang baru dengan Warna Biru, Z-Order 0 dan dimensi tertentu
            AddRectangle(page1, 20, 20, 30, 30, Color.Blue, 1);
            // Buat persegi panjang baru dengan Warna Hijau, Z-Order 0 dan dimensi tertentu
            AddRectangle(page1, 40, 40, 60, 30, Color.Green, 0);
            // Simpan file PDF hasil
            doc1.Save(_dataDir + "ControlRectangleZOrder_out.pdf");
        }
```

```
![Mengontrol Urutan Z](control.png)
```