---
title: Anotasi Sorotan PDF menggunakan C#
linktitle: Anotasi Sorotan
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /id/net/highlights-annotation/
description: Pelajari cara menambahkan anotasi sorotan ke dokumen PDF di .NET menggunakan Aspose.PDF untuk penekanan dan tinjauan teks.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Highlight Annotation using C#",
    "alternativeHeadline": "PDF Annotations with Customizable Highlighting Options",
    "abstract": "Fitur Anotasi Sorotan PDF baru menggunakan C# memungkinkan pengguna untuk dengan mudah menambahkan dan menyesuaikan anotasi markup teks dalam dokumen PDF mereka. Fungsionalitas ini mencakup opsi untuk sorotan, garis bawah, coretan, dan garis bawah bergerigi, yang semuanya dapat diedit untuk warna, opasitas, dan metadata, meningkatkan interaktivitas dan kejelasan dokumen.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF Highlight Annotation, C#, text markup annotation, highlight settings, strikethrough settings, underline settings, add annotation, delete annotation, Aspose.PDF.Drawing, markup annotations",
    "wordcount": "958",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "dateModified": "2024-11-25",
    "description": "Anotasi Markup disajikan dalam teks sebagai sorotan, garis bawah, coretan, atau garis bawah bergerigi dalam teks dokumen."
}
</script>

Anotasi Markup Teks akan muncul sebagai sorotan, garis bawah, coretan, atau garis bawah bergerigi (“squiggly”) dalam teks dokumen. Ketika dibuka, mereka akan menampilkan jendela pop-up yang berisi teks dari catatan terkait.

Properti anotasi markup teks dalam dokumen PDF dapat diedit menggunakan jendela properti yang disediakan dalam kontrol penampil PDF. Warna, opasitas, penulis, dan subjek anotasi markup teks dapat dimodifikasi.

Adalah mungkin untuk mendapatkan atau mengatur pengaturan anotasi sorotan menggunakan properti highlightSettings. Properti highlightSettings digunakan untuk mengatur warna, opasitas, penulis, subjek, modifiedDate, dan isLocked dari anotasi sorotan.

Juga mungkin untuk mendapatkan atau mengatur pengaturan anotasi coretan menggunakan properti strikethroughSettings. Properti strikethroughSettings digunakan untuk mengatur warna, opasitas, penulis, subjek, modifiedDate, dan isLocked dari anotasi coretan.

Fitur berikutnya adalah kemampuan untuk mendapatkan atau mengatur pengaturan anotasi garis bawah menggunakan properti underlineSettings. Properti underlineSettings digunakan untuk mengatur warna, opasitas, penulis, subjek, modifiedDate, dan isLocked dari anotasi garis bawah.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## Tambahkan Anotasi Markup Teks

Untuk menambahkan Anotasi Markup Teks ke dokumen PDF, kita perlu melakukan tindakan berikut:

1. Muat file PDF - objek [Document](https://reference.aspose.com/pdf/id/net/aspose.pdf/document) baru.
1. Buat anotasi:
    - [HighlightAnnotation](https://reference.aspose.com/pdf/id/net/aspose.pdf.annotations/highlightannotation) dan atur parameter (judul, warna).
    - [StrikeOutAnnotation](https://reference.aspose.com/pdf/id/net/aspose.pdf.annotations/strikeoutannotation) dan atur parameter (judul, warna).
    - [SquigglyAnnotation](https://reference.aspose.com/pdf/id/net/aspose.pdf.annotations/squigglyannotation) dan atur parameter (judul, warna).
    - [UnderlineAnnotation](https://reference.aspose.com/pdf/id/net/aspose.pdf.annotations/underlineannotation) dan atur parameter (judul, warna).
1. Setelah itu, kita harus menambahkan semua anotasi ke halaman.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextMarkupAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Create a TextFragmentAbsorber to find the text "PDF"
        var tfa = new Aspose.Pdf.Text.TextFragmentAbsorber("PDF");
        tfa.Visit(document.Pages[1]);

        // Create annotations for the found text fragments
        var highlightAnnotation = new Aspose.Pdf.Annotations.HighlightAnnotation(document.Pages[1], tfa.TextFragments[1].Rectangle)
        {
            Title = "Aspose User",
            Color = Aspose.Pdf.Color.LightGreen
        };

        var strikeOutAnnotation = new Aspose.Pdf.Annotations.StrikeOutAnnotation(document.Pages[1], tfa.TextFragments[2].Rectangle)
        {
            Title = "Aspose User",
            Color = Aspose.Pdf.Color.Blue
        };

        var squigglyAnnotation = new Aspose.Pdf.Annotations.SquigglyAnnotation(document.Pages[1], tfa.TextFragments[3].Rectangle)
        {
            Title = "Aspose User",
            Color = Aspose.Pdf.Color.Red
        };

        var underlineAnnotation = new Aspose.Pdf.Annotations.UnderlineAnnotation(document.Pages[1], tfa.TextFragments[4].Rectangle)
        {
            Title = "Aspose User",
            Color = Aspose.Pdf.Color.Violet
        };

        // Add annotations to the page
        document.Pages[1].Annotations.Add(highlightAnnotation);
        document.Pages[1].Annotations.Add(squigglyAnnotation);
        document.Pages[1].Annotations.Add(strikeOutAnnotation);
        document.Pages[1].Annotations.Add(underlineAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddTextMarkupAnnotations_out.pdf");
    }
}
```

Jika Anda ingin menyoroti fragmen multi-baris, Anda harus menggunakan contoh lanjutan:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHighlightAnnotationAdvanced()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample_mod.pdf"))
    {
        var page = document.Pages[1];
        var tfa = new TextFragmentAbsorber(@"Adobe\W+Acrobat\W+Reader", new TextSearchOptions(true));
        tfa.Visit(page);
        foreach (var textFragment in tfa.TextFragments)
        {
            var highlightAnnotation = HighLightTextFragment(page, textFragment, Color.Yellow);
            page.Annotations.Add(highlightAnnotation);
        }

        // Save PDF document
        document.Save(dataDir + "AddHighlightAnnotationAdvanced_out.pdf");
    }
}

private static HighlightAnnotation HighLightTextFragment(Page page,
    Aspose.Pdf.Text.TextFragment textFragment, Aspose.Pdf.Color color)
{
    if (textFragment.Segments.Count == 1)
    {
        return new Aspose.Pdf.Annotations.HighlightAnnotation(page, textFragment.Segments[1].Rectangle)
        {
            Title = "Aspose User",
            Color = color,
            Modified = DateTime.Now,
            QuadPoints = new Aspose.Pdf.Point[]
            {
                new Aspose.Pdf.Point(textFragment.Segments[1].Rectangle.LLX, textFragment.Segments[1].Rectangle.URY),
                new Aspose.Pdf.Point(textFragment.Segments[1].Rectangle.URX, textFragment.Segments[1].Rectangle.URY),
                new Aspose.Pdf.Point(textFragment.Segments[1].Rectangle.LLX, textFragment.Segments[1].Rectangle.LLY),
                new Aspose.Pdf.Point(textFragment.Segments[1].Rectangle.URX, textFragment.Segments[1].Rectangle.LLY)
            }
        };
    }

    var offset = 0;
    var quadPoints = new Aspose.Pdf.Point[textFragment.Segments.Count * 4];
    foreach (Aspose.Pdf.Text.TextSegment segment in textFragment.Segments)
    {
        quadPoints[offset + 0] = new Aspose.Pdf.Point(segment.Rectangle.LLX, segment.Rectangle.URY);
        quadPoints[offset + 1] = new Aspose.Pdf.Point(segment.Rectangle.URX, segment.Rectangle.URY);
        quadPoints[offset + 2] = new Aspose.Pdf.Point(segment.Rectangle.LLX, segment.Rectangle.LLY);
        quadPoints[offset + 3] = new Aspose.Pdf.Point(segment.Rectangle.URX, segment.Rectangle.LLY);
        offset += 4;
    }

    var llx = quadPoints.Min(pt => pt.X);
    var lly = quadPoints.Min(pt => pt.Y);
    var urx = quadPoints.Max(pt => pt.X);
    var ury = quadPoints.Max(pt => pt.Y);
    return new Aspose.Pdf.Annotations.HighlightAnnotation(page, new Aspose.Pdf.Rectangle(llx, lly, urx, ury))
    {
        Title = "Aspose User",
        Color = color,
        Modified = DateTime.Now,
        QuadPoints = quadPoints
    };
}

private static void GetHighlightedText()
{
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample_mod.pdf"))
    {
        var highlightAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Highlight)
            .Cast<Aspose.Pdf.Annotations.HighlightAnnotation>();
        foreach (var ta in highlightAnnotations)
        {
            Console.WriteLine($"[{ta.GetMarkedText()}]");
        }
    }
}
```

## Dapatkan Anotasi Markup Teks

Silakan coba menggunakan potongan kode berikut untuk Mendapatkan Anotasi Markup Teks dari dokumen PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetTextMarkupAnnotation()
{
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample_mod.pdf"))
    {
        var textMarkupAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Highlight
            || a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Squiggly)
            .Cast<Aspose.Pdf.Annotations.TextMarkupAnnotation>();
        foreach (var ta in textMarkupAnnotations)
        {
            Console.WriteLine($"[{ta.AnnotationType} {ta.Rect}]");
        }
    }
}
```

## Hapus Anotasi Markup Teks

Potongan kode berikut menunjukkan cara Menghapus Anotasi Markup Teks dari file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteTextMarkupAnnotation()
{
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample_mod.pdf"))
    {
        var textMarkupAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Highlight
            ||a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Squiggly)
            .Cast<Aspose.Pdf.Annotations.TextMarkupAnnotation>();
        foreach (var ta in textMarkupAnnotations)
        {
            document.Pages[1].Annotations.Delete(ta);
        }
        
        // Save PDF document
        document.Save(dataDir + "DeleteTextMarkupAnnotation_out.pdf");
    }
}
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
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