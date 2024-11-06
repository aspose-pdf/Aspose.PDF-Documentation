---
title: Anotasi Ekstra menggunakan C#
linktitle: Anotasi Ekstra
type: docs
weight: 60
url: id/net/extra-annotations/
description: Bagian ini menjelaskan bagaimana menambahkan, mendapatkan, dan menghapus berbagai jenis anotasi ekstra dari dokumen PDF Anda.
lastmod: "2023-09-12"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Anotasi Ekstra menggunakan C#",
    "alternativeHeadline": "Cara Menambahkan Anotasi Ekstra dalam PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, anotasi link, anotasi caret",
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
    "url": "/net/extra-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extra-annotations/"
    },
    "dateModified": "2022-02-04",
    "description": "Bagian ini menjelaskan bagaimana menambahkan, mendapatkan, dan menghapus berbagai jenis anotasi ekstra dari dokumen PDF Anda."
}
</script>

## Cara Menambahkan Anotasi Caret ke dalam file PDF yang ada

Anotasi Caret adalah simbol yang menunjukkan penyuntingan teks. Anotasi Caret juga merupakan anotasi markup, sehingga kelas Caret berasal dari kelas Markup dan juga menyediakan fungsi untuk mendapatkan atau mengatur properti Anotasi Caret dan mengatur ulang alur tampilan Anotasi Caret.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

Langkah-langkah dalam membuat anotasi Caret:

1. Muat file PDF - new [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Buat Anotasi Caret baru [Caret Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/caretannotation) dan atur parameter Caret (Rectangle baru, judul, Subjek, Flags, warna, lebar, StartingStyle dan EndingStyle). Anotasi ini digunakan untuk menunjukkan penyisipan teks.
1. Buat [StrikeOutAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation) baru dan atur parameter (Rectangle baru, judul, warna, QuadPoints baru dan titik baru, Subjek, InReplyTo, ReplyType).
1. Setelah itu kita dapat menambahkan anotasi ke halaman.

Potongan kode berikut menunjukkan cara menambahkan Caret Annotation ke file PDF:

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleCaretAnnotation
    {
        // Jalur ke direktori dokumen.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddCaretAnnotation()
        {
            // Muat file PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
            // Anotasi ini digunakan untuk menunjukkan penyisipan teks
            var caretAnnotation1 = new CaretAnnotation(document.Pages[1], new Rectangle(299.988, 713.664, 308.708, 720.769))
            {
                Title = "Aspose User",
                Subject = "Inserted text 1",
                Flags = AnnotationFlags.Print,
                Color = Color.Blue
            };
            // Anotasi ini digunakan untuk menunjukkan penggantian teks
            var caretAnnotation2 = new CaretAnnotation(document.Pages[1], new Rectangle(361.246, 727.908, 370.081, 735.107))
            {
                Flags = AnnotationFlags.Print,
                Subject = "Inserted text 2",
                Title = "Aspose User",
                Color = Color.Blue
            };

            var strikeOutAnnotation = new StrikeOutAnnotation(document.Pages[1],
                new Rectangle(318.407, 727.826, 368.916, 740.098))
            {
                Color = Color.Blue,
                QuadPoints = new[] {
                new Point(321.66, 739.416),
                new Point(365.664, 739.416),
                new Point(321.66, 728.508),
                new Point(365.664, 728.508)
            },
                Subject = "Cross-out",
                InReplyTo = caretAnnotation2,
                ReplyType = ReplyType.Group
            };

            document.Pages[1].Annotations.Add(caretAnnotation1);
            document.Pages[1].Annotations.Add(caretAnnotation2);
            document.Pages[1].Annotations.Add(strikeOutAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
        }
```
### Dapatkan Anotasi Caret

Silakan coba menggunakan potongan kode berikut untuk Mendapatkan Anotasi Caret dalam dokumen PDF

```csharp
public static void GetCaretAnnotation()
{
    // Muat file PDF
    Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
    var caretAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Caret)
        .Cast<CaretAnnotation>();
    foreach (var ca in caretAnnotations)
    {
        Console.WriteLine($"{ca.Rect}");
    }
}
```

### Hapus Anotasi Caret

Potongan kode berikut menunjukkan cara Menghapus Anotasi Caret dari file PDF.

```csharp
public static void DeleteCaretAnnotation()
{
    // Muat file PDF
    Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
    var caretAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Caret)
        .Cast<CaretAnnotation>();

    foreach (var ca in caretAnnotations)
    {
        document.Pages[1].Annotations.Delete(ca);
    }
    document.Save(System.IO.Path.Combine(_dataDir, "sample_caret_del.pdf"));
}
```
## Redact area tertentu pada halaman dengan Redaction Annotation menggunakan Aspose.PDF untuk .NET

Aspose.PDF untuk .NET mendukung fitur untuk menambahkan serta memanipulasi Anotasi dalam file PDF yang ada. Baru-baru ini beberapa pelanggan kami mengajukan kebutuhan untuk meredaksi (menghapus teks, gambar, dan elemen lainnya dari) area halaman tertentu dari dokumen PDF. Untuk memenuhi kebutuhan ini, disediakan kelas bernama RedactionAnnotation, yang dapat digunakan untuk meredaksi area halaman tertentu atau dapat digunakan untuk memanipulasi RedactionAnnotations yang ada dan meredaksinya (yaitu meratakan anotasi dan menghapus teks di bawahnya).

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Buka dokumen
Document doc = new Document(dataDir + "input.pdf");

// Buat instance RedactionAnnotation untuk area halaman tertentu
RedactionAnnotation annot = new RedactionAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(200, 500, 300, 600));
annot.FillColor = Aspose.Pdf.Color.Green;
annot.BorderColor = Aspose.Pdf.Color.Yellow;
annot.Color = Aspose.Pdf.Color.Blue;
// Teks yang akan dicetak pada anotasi redaksi
annot.OverlayText = "REDACTED";
annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Ulangi teks Overlay di atas Anotasi Redaksi
annot.Repeat = true;
// Tambahkan anotasi ke koleksi anotasi halaman pertama
doc.Pages[1].Annotations.Add(annot);
// Meratakan anotasi dan meredaksi konten halaman (yaitu menghapus teks dan gambar
// di bawah anotasi yang telah diredaksi)
annot.Redact();
dataDir = dataDir + "RedactPage_out.pdf";
doc.Save(dataDir);
```
### Pendekatan Fasad

Namespace Aspose.PDF.Facades juga memiliki kelas bernama [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) yang menyediakan fitur untuk memanipulasi Anotasi yang ada di dalam file PDF. Kelas ini mengandung sebuah metode bernama [RedactArea(..)](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/redactarea) yang memberikan kemampuan untuk menghapus beberapa wilayah halaman tertentu.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Aspose.Pdf.Facades.PdfAnnotationEditor editor = new Aspose.Pdf.Facades.PdfAnnotationEditor();
// Redact wilayah halaman tertentu
editor.RedactArea(1, new Aspose.Pdf.Rectangle(100, 100, 20, 70), System.Drawing.Color.White);
editor.BindPdf(dataDir + "input.pdf");
editor.Save(dataDir + "FacadesApproach_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Perpustakaan Aspose.PDF untuk .NET",
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

