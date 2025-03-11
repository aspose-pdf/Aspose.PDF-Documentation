---
title: Anotasi Tambahan menggunakan C#
linktitle: Anotasi Tambahan
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /id/net/extra-annotations/
description: Pelajari cara menambahkan anotasi tambahan ke file PDF di .NET menggunakan Aspose.PDF untuk fitur dokumen interaktif.
lastmod: "2023-09-12"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extra Annotations using C#",
    "alternativeHeadline": "Enhance PDF Annotations with C#",
    "abstract": "Memperkenalkan fitur Anotasi Tambahan di C#, yang memungkinkan pengembang untuk dengan mudah menambahkan, mengambil, dan menghapus berbagai anotasi dari dokumen PDF. Fungsionalitas yang kuat ini meningkatkan interaksi PDF dengan memungkinkan pengeditan teks yang tepat dan manipulasi dokumen, termasuk kemampuan untuk menambahkan anotasi caret dan redaksi secara efektif. Optimalkan penanganan PDF Anda dengan kemampuan canggih ini yang dirancang untuk manajemen dokumen yang intuitif.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Extra Annotations, Caret Annotation, PDF document manipulation, Aspose.PDF for .NET, Redaction Annotation, Markup annotation, Delete Caret Annotation, Get Caret Annotation, StrikeOutAnnotation, PdfAnnotationEditor",
    "wordcount": "929",
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
    "url": "/net/extra-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extra-annotations/"
    },
    "dateModified": "2024-11-25",
    "description": "Bagian ini menjelaskan cara menambahkan, mendapatkan, dan menghapus jenis anotasi tambahan dari dokumen PDF Anda."
}
</script>

## Cara menambahkan Anotasi Caret ke file PDF yang ada

Anotasi Caret adalah simbol yang menunjukkan pengeditan teks. Anotasi Caret juga merupakan anotasi markup, sehingga kelas Caret diturunkan dari kelas Markup dan juga menyediakan fungsi untuk mendapatkan atau mengatur properti Anotasi Caret dan mengatur ulang aliran tampilan Anotasi Caret.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

Langkah-langkah untuk membuat anotasi Caret:

1. Muat file PDF - baru [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Buat anotasi [Caret Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/caretannotation) baru dan atur parameter Caret (new Rectangle, title, Subject, Flags, color, width, StartingStyle dan EndingStyle). Anotasi ini digunakan untuk menunjukkan penyisipan teks.
1. Buat anotasi [Caret Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/caretannotation) baru dan atur parameter Caret (new Rectangle, title, Subject, Flags, color, width, StartingStyle dan EndingStyle). Anotasi ini digunakan untuk menunjukkan penggantian teks.
1. Buat [StrikeOutAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation) baru dan atur parameter (new Rectangle, title, color, new QuadPoints dan new points, Subject, InReplyTo, ReplyType).
1. Setelah itu, kita dapat menambahkan anotasi ke halaman.

Potongan kode berikut menunjukkan cara menambahkan Anotasi Caret ke file PDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddCaretAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Create Caret Annotation for text insertion
        var caretAnnotation1 = new Aspose.Pdf.Annotations.CaretAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(299.988, 713.664, 308.708, 720.769))
        {
            Title = "Aspose User",
            Subject = "Inserted text 1",
            Flags = Aspose.Pdf.Annotations.AnnotationFlags.Print,
            Color = Aspose.Pdf.Color.Blue
        };

        // Create Caret Annotation for text replacement
        var caretAnnotation2 = new Aspose.Pdf.Annotations.CaretAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(361.246, 727.908, 370.081, 735.107))
        {
            Flags = Aspose.Pdf.Annotations.AnnotationFlags.Print,
            Subject = "Inserted text 2",
            Title = "Aspose User",
            Color = Aspose.Pdf.Color.Blue
        };

        // Create StrikeOut Annotation
        var strikeOutAnnotation = new Aspose.Pdf.Annotations.StrikeOutAnnotation(document.Pages[1],
            new Rectangle(318.407, 727.826, 368.916, 740.098))
        {
            Color = Aspose.Pdf.Color.Blue,
            QuadPoints = new[] {
                new Point(321.66, 739.416),
                new Point(365.664, 739.416),
                new Point(321.66, 728.508),
                new Point(365.664, 728.508)
            },
            Subject = "Cross-out",
            InReplyTo = caretAnnotation2,
            ReplyType = Aspose.Pdf.Annotations.ReplyType.Group
        };

        document.Pages[1].Annotations.Add(caretAnnotation1);
        document.Pages[1].Annotations.Add(caretAnnotation2);
        document.Pages[1].Annotations.Add(strikeOutAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddCaretAnnotations_out.pdf");
    }
}
```

### Dapatkan Anotasi Caret

Silakan coba menggunakan potongan kode berikut untuk Mendapatkan Anotasi Caret dalam dokumen PDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetCaretAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample_caret.pdf"))
    {
        // Get Caret annotations from the first page
        var caretAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Caret)
            .Cast<Aspose.Pdf.Annotations.CaretAnnotation>();

        // Iterate through the annotations and print their details
        foreach (var ca in caretAnnotations)
        {
            Console.WriteLine($"{ca.Rect}");
        }
    }
}
```

### Hapus Anotasi Caret

Potongan kode berikut menunjukkan cara Menghapus Anotasi Caret dari file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteCaretAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample_caret.pdf"))
    {
        // Get Caret annotations from the first page
        var caretAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Caret)
            .Cast<Aspose.Pdf.Annotations.CaretAnnotation>();

        // Delete each Caret annotation
        foreach (var ca in caretAnnotations)
        {
            document.Pages[1].Annotations.Delete(ca);
        }

        // Save PDF document after deleting annotations
        document.Save(dataDir + "DeleteCaretAnnotation_out.pdf");
    }
}
```

## Redaksi wilayah halaman tertentu dengan Anotasi Redaksi menggunakan Aspose.PDF for .NET

Aspose.PDF for .NET mendukung fitur untuk menambahkan serta memanipulasi Anotasi dalam file PDF yang ada. Baru-baru ini beberapa pelanggan kami mengajukan permintaan untuk meredaksi (menghapus teks, gambar, dll elemen dari) wilayah halaman tertentu dari dokumen PDF. Untuk memenuhi permintaan ini, sebuah kelas bernama RedactionAnnotation disediakan, yang dapat digunakan untuk meredaksi wilayah halaman tertentu atau dapat digunakan untuk memanipulasi RedactionAnnotations yang ada dan meredaksinya (yaitu, meratakan anotasi dan menghapus teks di bawahnya).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RedactPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create RedactionAnnotation instance for a specific page region
        var annot = new Aspose.Pdf.Annotations.RedactionAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(200, 500, 300, 600));
        annot.FillColor = Aspose.Pdf.Color.Green;
        annot.BorderColor = Aspose.Pdf.Color.Yellow;
        annot.Color = Aspose.Pdf.Color.Blue;

        // Text to be printed on the redact annotation
        annot.OverlayText = "REDACTED";
        annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;

        // Repeat Overlay text over the redact Annotation
        annot.Repeat = true;

        // Add annotation to the annotations collection of the first page
        document.Pages[1].Annotations.Add(annot);

        // Flattens annotation and redacts page contents (i.e., removes text and image under the redacted annotation)
        annot.Redact();

        // Save the result document
        document.Save(dataDir + "RedactPage_out.pdf");
    }
}
```

### Pendekatan Facades

Namespace Aspose.Pdf.Facades juga memiliki kelas bernama [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) yang menyediakan fitur untuk memanipulasi Anotasi yang ada di dalam file PDF. Kelas ini berisi metode bernama [RedactArea(..)](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/redactarea) yang menyediakan kemampuan untuk menghapus wilayah halaman tertentu.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RedactPageWithFacadesApproach()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create an instance of PdfAnnotationEditor
    using (var editor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Redact a specific page region
        editor.RedactArea(1, new Aspose.Pdf.Rectangle(100, 100, 20, 70), System.Drawing.Color.White);

        // Bind PDF document
        editor.BindPdf(dataDir + "input.pdf");

        // Save the result document
        editor.Save(dataDir + "FacadesApproach_out.pdf");
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