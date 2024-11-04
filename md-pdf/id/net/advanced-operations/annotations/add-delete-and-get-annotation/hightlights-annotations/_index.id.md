---
title: Anotasi Penyorotan PDF menggunakan C#
linktitle: Anotasi Penyorotan
type: docs
weight: 20
url: /net/highlights-annotation/
description: Anotasi markup disajikan dalam teks sebagai penyorotan, garis bawah, coretan, atau garis bawah bergigi pada teks dokumen.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Anotasi Penyorotan PDF menggunakan C#",
    "alternativeHeadline": "Cara Menambahkan Anotasi Penyorotan di PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, anotasi penyorotan, anotasi markup teks",
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
    "url": "/net/highlights-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/highlights-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Anotasi markup disajikan dalam teks sebagai penyorotan, garis bawah, coretan, atau garis bawah bergigi pada teks dokumen."
}
</script>

Anotasi Markup Teks akan muncul sebagai penyorotan, garis bawah, coretan, atau garis bawah bergelombang di teks dokumen. Ketika dibuka, mereka akan menampilkan jendela pop-up yang berisi teks catatan yang terkait.

Properti anotasi markup teks dalam dokumen PDF dapat diedit menggunakan jendela properti yang disediakan dalam kontrol penampil PDF. Warna, keburaman, penulis, dan subjek anotasi markup teks dapat dimodifikasi.

Memungkinkan untuk mendapatkan atau mengatur pengaturan anotasi penyorotan menggunakan properti highlightSettings. Properti highlightSettings digunakan untuk mengatur warna, keburaman, penulis, subjek, modifiedDate dan properti isLocked dari anotasi penyorotan.

Juga memungkinkan untuk mendapatkan atau mengatur pengaturan anotasi coretan menggunakan properti strikethroughSettings. Properti strikethroughSettings digunakan untuk mengatur warna, keburaman, penulis, subjek, modifiedDate, dan properti isLocked dari anotasi coretan.

Fitur selanjutnya adalah kemampuan untuk mendapatkan atau mengatur pengaturan anotasi garis bawah menggunakan properti underlineSettings.
Fitur berikutnya adalah kemampuan untuk mendapatkan atau mengatur pengaturan anotasi garis bawah menggunakan properti underlineSettings.

Potongan kode berikut ini juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Tambahkan Anotasi Markup Teks

Untuk menambahkan Anotasi Markup Teks ke dokumen PDF, kita perlu melakukan tindakan berikut:

1. Muat file PDF - objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) baru.
1. Buat anotasi:
    - [HighlightAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/highlightannotation) dan atur parameter (judul, warna).
    - [StrikeOutAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation) dan atur parameter (judul, warna).
    - [SquigglyAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squigglyannotation) dan atur parameter (judul, warna).
    - [UnderlineAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/underlineannotation) dan atur parameter (judul, warna).
- [UnderlineAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/underlineannotation) dan atur parameter (judul, warna).
1. Setelah itu kita harus menambahkan semua anotasi ke halaman.

```csharp
using Aspose.Pdf.Annotations;
using Aspose.Pdf.Text;
using System;
using System.Linq;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleTextMarkupAnnotation
    {
        // Jalur ke direktori dokumen.
        private const string _dataDir = "..\\..\\..\\..\\Samples";

        public static void AddTextMarkupAnnotation()
        {
            try
            {
                // Muat file PDF
                Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
                var tfa = new Aspose.Pdf.Text.TextFragmentAbsorber("PDF");
                tfa.Visit(document.Pages[1]);

                //Buat anotasi
                HighlightAnnotation highlightAnnotation = new HighlightAnnotation(document.Pages[1],
                   tfa.TextFragments[1].Rectangle )
                {
                    Title = "Pengguna Aspose",
                    Color = Color.LightGreen
                };

                StrikeOutAnnotation strikeOutAnnotation = new StrikeOutAnnotation(
                   document.Pages[1],
                   tfa.TextFragments[2].Rectangle)
                {
                    Title = "Pengguna Aspose",
                    Color = Color.Blue
                };
                SquigglyAnnotation squigglyAnnotation = new SquigglyAnnotation(document.Pages[1],
                    tfa.TextFragments[3].Rectangle)
                {
                    Title = "Pengguna Aspose",
                    Color = Color.Red
                };
                UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(document.Pages[1],
                    tfa.TextFragments[4].Rectangle)
                {
                    Title = "Pengguna Aspose",
                    Color = Color.Violet
                };
                // Tambahkan anotasi ke halaman
                document.Pages[1].Annotations.Add(highlightAnnotation);
                document.Pages[1].Annotations.Add(squigglyAnnotation);
                document.Pages[1].Annotations.Add(strikeOutAnnotation);
                document.Pages[1].Annotations.Add(underlineAnnotation);
                document.Save(System.IO.Path.Combine(_dataDir, "sample_mod.pdf"));
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
```
Jika Anda ingin menyoroti sebuah fragmen multi-baris, Anda harus menggunakan contoh yang lebih maju:

```csharp
        /// <summary>
        /// Contoh lanjutan untuk Anda yang ingin menyorot fragmen multi-baris
        /// </summary>
        public static void AddHighlightAnnotationAdvanced()
        {
            var document = new Document(System.IO.Path.Combine(_dataDir, "sample_mod.pdf"));
            var page = document.Pages[1];
            var tfa = new TextFragmentAbsorber(@"Adobe\W+Acrobat\W+Reader", new TextSearchOptions(true));
            tfa.Visit(page);
            foreach (var textFragment in tfa.TextFragments)
            {
                var highlightAnnotation = HighLightTextFragment(page, textFragment, Color.Yellow);
                page.Annotations.Add(highlightAnnotation);
            }
            document.Save(System.IO.Path.Combine(_dataDir, "sample_mod.pdf"));
        }
        private static HighlightAnnotation HighLightTextFragment(Aspose.Pdf.Page page,
            TextFragment textFragment, Color color)
        {
            if (textFragment.Segments.Count == 1)
                return new HighlightAnnotation(page, textFragment.Segments[1].Rectangle)
                {
                    Title = "Pengguna Aspose",
                    Color = color,
                    Modified = DateTime.Now,
                    QuadPoints = new Point[]
                    {
                        new Point(textFragment.Segments[1].Rectangle.LLX, textFragment.Segments[1].Rectangle.URY),
                        new Point(textFragment.Segments[1].Rectangle.URX, textFragment.Segments[1].Rectangle.URY),
                        new Point(textFragment.Segments[1].Rectangle.LLX, textFragment.Segments[1].Rectangle.LLY),
                        new Point(textFragment.Segments[1].Rectangle.URX, textFragment.Segments[1].Rectangle.LLY)
                    }
                };

            var offset = 0;
            var quadPoints = new Point[textFragment.Segments.Count * 4];
            foreach (var segment in textFragment.Segments)
            {
                quadPoints[offset + 0] = new Point(segment.Rectangle.LLX, segment.Rectangle.URY);
                quadPoints[offset + 1] = new Point(segment.Rectangle.URX, segment.Rectangle.URY);
                quadPoints[offset + 2] = new Point(segment.Rectangle.LLX, segment.Rectangle.LLY);
                quadPoints[offset + 3] = new Point(segment.Rectangle.URX, segment.Rectangle.LLY);
                offset += 4;
            }

            var llx = quadPoints.Min(pt => pt.X);
            var lly = quadPoints.Min(pt => pt.Y);
            var urx = quadPoints.Max(pt => pt.X);
            var ury = quadPoints.Max(pt => pt.Y);
            return new HighlightAnnotation(page, new Rectangle(llx, lly, urx, ury))
            {
                Title = "Pengguna Aspose",
                Color = color,
                Modified = DateTime.Now,
                QuadPoints = quadPoints
            };
        }

        /// <summary>
        /// Bagaimana mendapatkan Teks yang Disorot
        /// </summary>
        public static void GetHighlightedText()
        {
            // Muat file PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_mod.pdf"));
            var highlightAnnotations = document.Pages[1].Annotations
                .Where(a => a.AnnotationType == AnnotationType.Highlight)
                .Cast<HighlightAnnotation>();
            foreach (var ta in highlightAnnotations)
            {
                Console.WriteLine($"[{ta.GetMarkedText()}]");
            }
        }
```
## Dapatkan Anotasi Markup Teks

Silakan coba menggunakan cuplikan kode berikut untuk Mendapatkan Anotasi Markup Teks dari dokumen PDF.

```csharp
    public static void GetTextMarkupAnnotation()
    {
        // Muat file PDF
        Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_mod.pdf"));
        var textMarkupAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == AnnotationType.Highlight
            || a.AnnotationType == AnnotationType.Squiggly)
            .Cast<TextMarkupAnnotation>();
            foreach (var ta in textMarkupAnnotations)
            {
                Console.WriteLine($"[{ta.AnnotationType} {ta.Rect}]");
            }
    }
```

## Hapus Anotasi Markup Teks

Cuplikan kode berikut menunjukkan cara Menghapus Anotasi Markup Teks dari file PDF.

```csharp
    public static void DeleteTextMarkupAnnotation()
    {
        // Muat file PDF
        Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_mod.pdf"));
        var textMarkupAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == AnnotationType.Highlight
            ||a.AnnotationType == AnnotationType.Squiggly)
            .Cast<TextMarkupAnnotation>();
            foreach (var ta in textMarkupAnnotations)
            {
            document.Pages[1].Annotations.Delete(ta);
            }
            document.Save(System.IO.Path.Combine(_dataDir, "sample_del.pdf"));
    }
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Pustaka Aspose.PDF untuk .NET",
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
    "applicationCategory": "Pustaka Manipulasi PDF untuk .NET",
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

