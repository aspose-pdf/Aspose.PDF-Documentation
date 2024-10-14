---
title: Menambahkan Anotasi Figur menggunakan C#
linktitle: Anotasi Figur
type: docs
weight: 30
url: /net/figures-annotation/
description: Artikel ini menjelaskan cara menambahkan, mendapatkan, dan menghapus anotasi figur dari dokumen PDF Anda dengan Aspose.PDF untuk .NET
lastmod: "2023-09-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Menambahkan Anotasi Figur menggunakan C#",
    "alternativeHeadline": "Cara menambahkan Anotasi Figur dalam PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen PDF",
    "keywords": "pdf, c#, anotasi figur, anotasi poligon, anotasi garis, anotasi persegi, anotasi lingkaran",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dok Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/figures-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/figures-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Artikel ini menjelaskan cara menambahkan, mendapatkan, dan menghapus anotasi figur dari dokumen PDF Anda dengan Aspose.PDF untuk .NET"
}
</script>

Aplikasi manajemen dokumen PDF menyediakan berbagai alat untuk memberi anotasi pada dokumen. Dari perspektif struktur internal PDF, alat-alat ini adalah anotasi. Kami mendukung jenis alat gambar berikut.

* Line Annotation - alat untuk menggambar garis dan panah
* Square Annotation - untuk menggambar persegi dan persegi panjang
* Circle Annotation - untuk oval dan lingkaran
* FreeText Annotation - untuk komentar Callout
* Polygon Annotation - untuk poligon dan awan
* Polyline Annotation - untuk Garis yang Terhubung

## Menambahkan Bentuk dan Figur pada Halaman

Pendekatan untuk menambahkan anotasi adalah tipikal untuk semuanya.

Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

1. Muat file PDF atau buat baru oleh [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Buat anotasi baru dan atur parameter (Rectangle baru, Point baru, judul, warna, lebar, dll).
1. Hubungkan anotasi popup dengan aslinya.
1. Tambahkan anotasi ke halaman

## Menambahkan Garis atau Panah

Tujuan dari anotasi garis adalah untuk menampilkan garis lurus atau panah di halaman.
Untuk membuat Garis kita perlu objek LineAnnotation baru.
Konstruktor kelas LineAnnotation mengambil empat parameter:

* halaman tempat anotasi akan ditambahkan,
* persegi panjang yang mendefinisikan batas anotasi,
* dan dua titik yang mendefinisikan awal dan akhir garis.

Juga kita perlu menginisialisasi beberapa properti:

* `Title` - biasanya, ini adalah nama pengguna yang membuat komentar ini
* `Subject` - bisa berupa string apa saja, tetapi dalam kasus umum adalah nama anotasi

Untuk mengatur gaya garis kita perlu mengatur warna, lebar, gaya awal, dan gaya akhir.
Untuk memberikan gaya pada garis kita, kita perlu mengatur warna, lebar, gaya awal, dan gaya akhir.

Potongan kode berikut menunjukkan cara menambahkan Anotasi Garis ke file PDF:

```csharp
// Memuat file PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments.pdf"));

// Membuat Anotasi Garis
var lineAnnotation = new LineAnnotation(
    document.Pages[1],
    new Rectangle(550, 93, 562, 439),
    new Point(556, 99), new Point(556, 443))
{
    Title = "John Smith",
    Color = Color.Red,
    Width = 3,
    StartingStyle = LineEnding.OpenArrow,
    EndingStyle = LineEnding.OpenArrow,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 124, 1021, 266))
};

// Menambahkan anotasi ke halaman
document.Pages[1].Annotations.Add(lineAnnotation);
document.Save(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
```

## Menambahkan Persegi atau Lingkaran

Anotasi [Square](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squareannotation) dan [Circle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/circleannotation) akan menampilkan persegi atau elips di halaman.
[Square](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squareannotation) dan [Circle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/circleannotation) akan menampilkan persegi atau elips di halaman.

### Menambahkan Anotasi Lingkaran

Untuk menggambar anotasi lingkaran atau elips baru, kita perlu membuat objek CircleAnnotation baru. Konstruktor kelas `CircleAnnotation` memiliki dua parameter:

* halaman tempat anotasi akan ditambahkan,
* dan persegi panjang yang mendefinisikan batas anotasi

Kita juga dapat mengatur beberapa properti dari objek `CircleAnnotation`, seperti judul, warna, warna interior, opasitas. Properti-properti ini mengontrol bagaimana anotasi akan terlihat dan berperilaku di penampil PDF. Di sini dan selanjutnya di Square warna `InteriorColor` adalah warna pengisian dan `Color` adalah warna batas.

### Menambahkan Anotasi Persegi

Menggambar persegi sama seperti menggambar lingkaran.
Menggambar persegi panjang sama dengan menggambar lingkaran.

```csharp
var dataDir = "<path-to-file>";
// Memuat file PDF
Document document = new Document(System.IO.Path.Combine(dataDir, "appartments.pdf"));

// Membuat Anotasi Lingkaran
var circleAnnotation = new CircleAnnotation(document.Pages[1], new Rectangle(270, 160, 483, 383))
{
    Title = "John Smith",
    Subject = "Lingkaran",
    Color = Color.Red,
    InteriorColor = Color.MistyRose,
    Opacity = 0.5,        
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 316, 1021, 459))
};

// Membuat Anotasi Persegi
var squareAnnotation = new SquareAnnotation(document.Pages[1], new Rectangle(67, 317, 261, 459))
{
    Title = "John Smith",
    Subject = "Persegi Panjang",
    Color = Color.Blue,
    InteriorColor = Color.BlueViolet,
    Opacity = 0.25,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// Menambahkan anotasi ke halaman
document.Pages[1].Annotations.Add(circleAnnotation);
document.Pages[1].Annotations.Add(squareAnnotation);
document.Save(System.IO.Path.Combine(dataDir, "appartments_mod.pdf"));
```
Sebagai contoh, kita akan melihat hasil berikut dari penambahan anotasi Persegi dan Lingkaran ke dokumen PDF:

![Demo Anotasi Lingkaran dan Persegi](circle_demo.png)

## Menambahkan Anotasi Poligon dan Polilin

Alat Poly- memungkinkan Anda untuk membuat bentuk dan garis besar dengan jumlah sisi sembarang pada dokumen.

**Anotasi Poligon** mewakili poligon di halaman. Mereka dapat memiliki jumlah verteks yang dihubungkan oleh garis lurus.
**Anotasi Polilin** juga serupa dengan poligon, perbedaan satu-satunya adalah verteks pertama dan terakhir tidak dihubungkan secara implisit.

### Menambahkan Anotasi Poligon

PolygonAnnotation bertanggung jawab atas anotasi poligon. Konstruktor kelas PolygonAnnotation mengambil tiga parameter:

* halaman di mana anotasi akan ditambahkan,
* persegi panjang yang mendefinisikan batas anotasi,
* dan array titik yang mendefinisikan verteks poligon.

`Color` dan `InteriorColor` digunakan untuk warna batas dan warna isian masing-masing.

### Menambahkan Anotasi Polilin
### Menambahkan Anotasi Polyline

PolygonAnnotation bertanggung jawab untuk anotasi poligon. Konstruktor dari kelas PolygonAnnotation memiliki tiga parameter:

* halaman di mana anotasi akan ditambahkan,
* persegi panjang yang mendefinisikan batas anotasi,
* dan array titik yang mendefinisikan titik-titik sudut poligon.

Alih-alih `PolygonAnnotation` kita tidak dapat mengisi bentuk ini, sehingga kita tidak perlu menggunakan `InteriorColor`.

Potongan kode berikut menunjukkan cara menambahkan Anotasi Poligon dan Poliline ke file PDF:

```csharp
// Memuat file PDF
Document document = new Document(System.IO.Path.Combine(dataDir, "appartments.pdf"));

// Membuat Anotasi Poligon
var polygonAnnotation = new PolygonAnnotation(document.Pages[1],
    new Rectangle(270, 193, 571, 383),
    new Point[] {
        new Point(274, 381),
        new Point(555, 381),
        new Point(555, 304),
        new Point(570, 304),
        new Point(570, 195),
        new Point(274, 195)})
{
    Title = "John Smith",
    Color = Color.Blue,
    InteriorColor = Color.BlueViolet,
    Opacity = 0.25,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// Membuat Anotasi Poliline
var polylineAnnotation = new PolylineAnnotation(document.Pages[1],
    new Rectangle(270, 193, 571, 383),
    new Point[] {
        new Point(545,150),
        new Point(545,190),
        new Point(667,190),
        new Point(667,110),
        new Point(626,111)
        })
{
    Title = "John Smith",
    Color = Color.Red,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// Menambahkan anotasi ke halaman
document.Pages[1].Annotations.Add(polygonAnnotation);
document.Pages[1].Annotations.Add(polylineAnnotation);
document.Save(System.IO.Path.Combine(dataDir, "appartments_mod.pdf"));
```
## Mendapatkan Figur

Semua anotasi disimpan dalam koleksi `Annotations`. Setiap anotasi dapat memperkenalkan tipe melalui properti `AnnotationType`. Oleh karena itu, kita dapat membuat query LINQ untuk menyaring anotasi yang diinginkan.

### Mendapatkan Anotasi Garis

Contoh di bawah ini menjelaskan bagaimana mendapatkan semua Anotasi Garis dari halaman pertama dokumen PDF.

```csharp
// Memuat file PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var lineAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<LineAnnotation>();
foreach (var la in lineAnnotations)
{
    Console.WriteLine($"[{la.Starting.X},{la.Starting.Y}]-[{la.Ending.X},{la.Ending.Y}]");
}   
```

### Mendapatkan Anotasi Lingkaran

Contoh di bawah ini menjelaskan bagaimana mendapatkan semua Anotasi Polilin dari halaman pertama dokumen PDF.

```csharp
// Memuat file PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var circleAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<CircleAnnotation>();
foreach (var ca in circleAnnotations)
{
    Console.WriteLine($"[{ca.Rect}]");
}   
```
### Mendapatkan Anotasi Square

Contoh di bawah ini menjelaskan bagaimana mendapatkan semua Anotasi Poligon dari halaman pertama dokumen PDF.

```csharp
// Memuat file PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var squareAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Square)
    .Cast<SquareAnnotation>();
foreach (var sq in squareAnnotations)
{
    Console.WriteLine($"[{sq.Rect}]");
}
```

### Mendapatkan Anotasi Polyline

Contoh di bawah ini menjelaskan bagaimana mendapatkan semua Anotasi Polyline dari halaman pertama dokumen PDF.

```csharp
// Memuat file PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var polyAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.PolyLine)
    .Cast<PolylineAnnotation>();
foreach (var pa in polyAnnotations)
{
    Console.WriteLine($"[{pa.Rect}]");
}     
```

### Mendapatkan Anotasi Polygon
Contoh di bawah ini menjelaskan bagaimana mendapatkan semua Anotasi Poligon dari halaman pertama dokumen PDF.

```csharp
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var polyAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Polygon)
    .Cast<PolygonAnnotation>();
foreach (var pa in polyAnnotations)
{
    Console.WriteLine($"[{pa.Rect}]");
} 
```

## Menghapus Figur

Cara menghapus anotasi dari PDF cukup sederhana:

* Pilih anotasi yang akan dihapus (buat beberapa koleksi)
* Iterasi melalui koleksi menggunakan loop foreach, dan menghapus setiap anotasi dari koleksi anotasi menggunakan metode Delete.

### Menghapus Anotasi Garis

```csharp
// Memuat file PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var lineAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<LineAnnotation>();

foreach (var la in lineAnnotations)
{
    document.Pages[1].Annotations.Delete(la);
}
```
### Hapus Anotasi Lingkaran dan Kotak

```csharp
// Memuat file PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var figures = document.Pages[1].Annotations
    .Where(a =>
        a.AnnotationType == AnnotationType.Circle
        || a.AnnotationType == AnnotationType.Square);

foreach (var fig in figures)
{
    document.Pages[1].Annotations.Delete(fig);
}
document.Save(System.IO.Path.Combine(_dataDir, "Appartments_del.pdf"));
```

### Hapus Anotasi Poligon dan Polilin

Kode berikut menunjukkan cara menghapus Anotasi Poligon dan Polilin dari file PDF.

```csharp
// Memuat file PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var polyAnnotations = document.Pages[1].Annotations
                .Where(a => a.AnnotationType == AnnotationType.PolyLine
                || a.AnnotationType == AnnotationType.Polygon);

foreach (var pa in polyAnnotations)
{
    document.Pages[1].Annotations.Delete(pa);
}
document.Save(System.IO.Path.Combine(_dataDir, "Appartments_del.pdf"));
```
## Bagaimana Menambahkan Anotasi Tinta pada Berkas PDF

Anotasi Tinta merepresentasikan "coretan" bebas yang terdiri dari satu atau lebih jalur yang terpisah. Ketika dibuka, akan menampilkan jendela pop-up yang berisi teks dari catatan yang terkait.

Anotasi Tinta merepresentasikan coretan bebas yang terdiri dari satu atau lebih titik yang terpisah. Silakan coba menggunakan potongan kode berikut untuk menambahkan Anotasi Tinta dalam dokumen PDF.

```csharp
// Muat berkas PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "appartments.pdf"));
Page page = document.Pages[1];

Rectangle arect = new Rectangle(156.574, 521.316, 541.168, 575.703);

IList<Point[]> inkList = new List<Point[]>();
Point[] arrpt = new[]
{
    new Point(209.727,542.263),
    new Point(209.727,541.94),
    new Point(209.727,541.616)
};
inkList.Add(arrpt);

InkAnnotation ia = new InkAnnotation(page, arect, inkList)
{
    Title = "John Smith",
    Subject = "Pencil",
    Color = Color.LightBlue,
    CapStyle = CapStyle.Rounded,
    Opacity = 0.5
};
Border border = new Border(ia)
{
    Width = 25
};
ia.Border = border;
page.Annotations.Add(ia);

// Simpan berkas keluaran
document.Save(System.IO.Path.Combine(_dataDir, "appartments_mod.pdf"));
```
### Mengatur Lebar Garis dari InkAnnotation

Lebar dari [InkAnnottion](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation) dapat diubah menggunakan objek LineInfo dan Border.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Document doc = new Document();
doc.Pages.Add();
IList<Point[]> inkList = new List<Point[]>();
LineInfo lineInfo = new LineInfo();
lineInfo.VerticeCoordinate = new float[] { 55, 55, 70, 70, 70, 90, 150, 60 };
lineInfo.Visibility = true;
lineInfo.LineColor = System.Drawing.Color.Red;
lineInfo.LineWidth = 2;
int length = lineInfo.VerticeCoordinate.Length / 2;
Aspose.Pdf.Point[] gesture = new Aspose.Pdf.Point[length];
for (int i = 0; i < length; i++)
{
   gesture[i] = new Aspose.Pdf.Point(lineInfo.VerticeCoordinate[2 * i], lineInfo.VerticeCoordinate[2 * i + 1]);
}

inkList.Add(gesture);
InkAnnotation a1 = new InkAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), inkList);
a1.Subject = "Test";
a1.Title = "Title";
a1.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
Border border = new Border(a1);
border.Width = 3;
border.Effect = BorderEffect.Cloudy;
border.Dash = new Dash(1, 1);
border.Style = BorderStyle.Solid;
doc.Pages[1].Annotations.Add(a1);

dataDir = dataDir + "lnkAnnotationLineWidth_out.pdf";
// Simpan file keluaran
doc.Save(dataDir);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "penjualan",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "penjualan",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "penjualan",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Perpustakaan Manipulasi PDF untuk .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```
### Hapus Anotasi Lingkaran

Berikut ini adalah potongan kode yang menunjukkan cara Menghapus Anotasi Lingkaran dari file PDF.

```csharp
public static void DeleteCircleAnnotation()
{
    // Memuat file PDF
    Document document = new Document(System.IO.Path.Combine(dataDir, "Appartments_mod.pdf"));
    var circleAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Circle)
        .Cast<CircleAnnotation>();

    foreach (var ca in circleAnnotations)
    {
        document.Pages[1].Annotations.Delete(ca);
    }
    document.Save(System.IO.Path.Combine(dataDir, "Appartments_del.pdf"));
}
```
