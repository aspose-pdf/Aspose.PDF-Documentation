---
title: Menggunakan Anotasi Tautan di PDF
linktitle: Anotasi Tautan
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /id/net/link-annotations/
description: Aspose.PDF for .NET memungkinkan Anda untuk Menambahkan, Mengambil, dan Menghapus Anotasi Tautan dari dokumen PDF Anda.
lastmod: "2024-07-28"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using Link Annotation for PDF",
    "alternativeHeadline": "How to add Link Annotation in PDF",
    "abstract": "Aspose.PDF for .NET memperkenalkan kemampuan yang kuat untuk mengelola anotasi tautan dalam dokumen PDF, memungkinkan pengguna untuk dengan mudah menambahkan, mengambil, dan menghapus hyperlink. Fitur ini meningkatkan interaktivitas dokumen dengan memungkinkan tautan membuka halaman tertentu, file eksternal, atau URL web, semuanya dapat disesuaikan dengan berbagai gaya dan tindakan. Buka kemungkinan baru untuk navigasi PDF dan keterlibatan pengguna dengan fungsionalitas anotasi yang kuat ini.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, text annotation",
    "wordcount": "302",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/link-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/link-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET memungkinkan Anda untuk Menambahkan, Mengambil, dan Menghapus Anotasi Teks dari dokumen PDF Anda."
}
</script>

## Menambahkan Anotasi Tautan ke file PDF yang ada

> Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

Anotasi [Tautan](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) mewakili hyperlink, tujuan di tempat lain, dan dokumen. Menurut Standar PDF, anotasi tautan dapat digunakan dalam tiga kasus: membuka tampilan halaman, membuka file, dan membuka halaman web.

### Menggunakan Anotasi Tautan untuk membuka tampilan halaman

Beberapa langkah tambahan dilakukan untuk membuat anotasi. Kami menggunakan 2 TextFragmentAbsorbers untuk menemukan fragmen untuk demo. Yang pertama adalah untuk teks anotasi tautan, dan yang kedua menunjukkan beberapa tempat di dokumen.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Link Annotation Demo.pdf"))
    {
        // Get first page
        var page = document.Pages[1];

        // Define regular expressions for text fragments
        var regEx1 = new Regex(@"Link Annotation Demo \d");
        var regEx2 = new Regex(@"Sample text \d");

        // Create TextFragmentAbsorber for the first regular expression
        var textFragmentAbsorber1 = new Aspose.Pdf.Text.TextFragmentAbsorber(regEx1);
        textFragmentAbsorber1.Visit(document);

        // Create TextFragmentAbsorber for the second regular expression
        var textFragmentAbsorber2 = new Aspose.Pdf.Text.TextFragmentAbsorber(regEx2);
        textFragmentAbsorber2.Visit(document);

        // Get the text fragments for both absorbers
        var linkFragments = textFragmentAbsorber1.TextFragments;
        var sampleTextFragments = textFragmentAbsorber2.TextFragments;

        // Create a LinkAnnotation
        var linkAnnotation1 = new Aspose.Pdf.Annotations.LinkAnnotation(page, linkFragments[1].Rectangle)
        {
            Action = new Aspose.Pdf.Annotations.GoToAction(
                new Aspose.Pdf.Annotations.XYZExplicitDestination(
                    sampleTextFragments[1].Page,
                    sampleTextFragments[1].Rectangle.LLX,
                    sampleTextFragments[1].Rectangle.URX, 1.5))
        };

        // Add the link annotation to the page
        page.Annotations.Add(linkAnnotation1);

        // Save PDF document
        document.Save(dataDir + "AddLinkAnnotation_out.pdf");
    }
}
```

Untuk membuat anotasi kami telah mengikuti langkah-langkah tertentu:

1. Buat `LinkAnnotation` dan lewati objek halaman serta persegi panjang dari fragmen teks yang sesuai dengan anotasi.
1. Atur `Action` sebagai `GoToAction` dan lewati `XYZExplicitDestination` sebagai tujuan yang diinginkan. Kami membuat `XYZExplicitDestination` berdasarkan halaman, koordinat kiri dan atas, serta zoom.
1. Tambahkan anotasi ke koleksi anotasi halaman.
1. Simpan dokumen.

### Menggunakan Anotasi Tautan dengan tujuan bernama

Saat memproses berbagai dokumen, muncul situasi ketika Anda mengetik dan tidak tahu ke mana anotasi akan menunjuk. Dalam hal ini, Anda dapat menggunakan tujuan khusus (bernama) dan kode akan terlihat seperti di sini:

```cs
var destinationName = "Link2";
var linkAnnotation2 = new LinkAnnotation(page, linkFragments[2].Rectangle)
{
    Action = new GoToAction(document, destinationName)
};
```

Di tempat lain Anda dapat membuat Tujuan Bernama.

```cs
document.NamedDestinations.Add(destinationName,
    new XYZExplicitDestination(
        sampleTextFragments[2].Page,
        sampleTextFragments[2].Rectangle.LLX,
        sampleTextFragments[2].Rectangle.URX, 1));
```

### Menggunakan Anotasi Tautan untuk membuka file

Pendekatan yang sama digunakan saat membuat anotasi untuk membuka file, seperti dalam contoh di atas.

```cs
var linkAnnotation3 = new LinkAnnotation(page, linkFragments[3].Rectangle)
{
    Action = new GoToRemoteAction("another.pdf", 2)
};
```

Perbedaannya adalah bahwa kami akan menggunakan `GoToRemoteAction` alih-alih `GoToAction`. Konstruktor GoToRemoteAction mendapatkan dua parameter: nama file dan nomor halaman. Anda juga dapat menggunakan bentuk lain dan melewatkan nama file serta beberapa tujuan. Jelas, Anda perlu membuat tujuan tersebut sebelum menggunakannya.

### Menggunakan Anotasi Tautan untuk membuka halaman web

Untuk membuka halaman web, cukup atur `Action` dengan objek `GoToURIAction`. Anda dapat melewatkan hyperlink sebagai parameter konstruktor atau jenis URI lainnya. Misalnya, Anda dapat menggunakan `callto` untuk menerapkan tindakan dengan nomor telepon.

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),
    // Create Link Annotation and set the action to call a phone number
    //Action = new GoToURIAction("callto:678-555-0103")
    Color = Color.Blue
};
```

## Menambahkan Anotasi Tautan yang dihias

Anda dapat menyesuaikan Anotasi Tautan menggunakan batas. Dalam contoh di bawah ini, kami akan membuat batas putus-putus biru dengan lebar 3pt.

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),    
    Color = Color.Blue
};

linkAnnotation4.Border = new Border(linkAnnotation4)
{
    Style = BorderStyle.Dashed,
    Dash = new Dash(5, 5),
    Width = 3
};
```

Contoh lain menunjukkan bagaimana mensimulasikan gaya browser dan menggunakan Garis Bawah untuk tautan.

```cs
var linkAnnotation5 = new LinkAnnotation(page, linkFragments[5].Rectangle)
{
    Color = Color.Blue
};
linkAnnotation5.Border = new Border(linkAnnotation5)
{
    Style = BorderStyle.Underline,
    Width = 3
};
```

### Mendapatkan Anotasi Tautan

Silakan coba menggunakan potongan kode berikut untuk Mengambil LinkAnnotation dari dokumen PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetLinkAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume_mod.pdf"))
    {
        // Get all Link annotations from the first page
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Link);

        // Iterate through each Link annotation
        foreach (Aspose.Pdf.Annotations.Annotation annot in linkAnnotations)
        {
            // Print the URL of each Link Annotation
            Console.WriteLine("URI: " + ((annot as Aspose.Pdf.Annotations.LinkAnnotation).Action as Aspose.Pdf.Annotations.GoToURIAction).URI);

            // Create a TextAbsorber to extract text within the annotation's rectangle
            var absorber = new Aspose.Pdf.Text.TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;

            // Accept the absorber for the first page
            document.Pages[1].Accept(absorber);

            // Extract and print the text associated with the hyperlink
            string extractedText = absorber.Text;
            Console.WriteLine(extractedText);
        }
    }
}
```

### Menghapus Anotasi Tautan

Potongan kode berikut menunjukkan cara Menghapus Anotasi Tautan dari file PDF. Untuk ini, kami perlu menemukan dan menghapus semua anotasi tautan di halaman 1. Setelah ini, kami akan menyimpan dokumen dengan anotasi yang dihapus.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteLinkAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume_mod.pdf"))
    {
        // Find and delete all link annotations on the 1st page
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Link);

        foreach (var la in linkAnnotations)
        {
            document.Pages[1].Annotations.Delete(la);
        }

        // Save PDF document
        document.Save(dataDir + "DeleteLinkAnnotations_out.pdf");
    }
}
```