---
title: Menggunakan FloatingBox untuk generasi teks
linktitle: Menggunakan FloatingBox
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /id/net/floating-box/
description: Halaman ini menjelaskan cara memformat teks di dalam floating box.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using FloatingBox for text generation",
    "alternativeHeadline": "FloatingBox Enhances PDF Text Layout Options",
    "abstract": "Fitur FloatingBox meningkatkan pemformatan teks PDF dengan memungkinkan pengguna mengelola penempatan teks dengan presisi, termasuk tata letak multi-kolom dan offset yang dapat disesuaikan. Ini mendukung pemotongan teks, warna latar belakang, dan opsi untuk mengulang konten di seluruh halaman, menjadikannya alat yang serbaguna untuk membuat dokumen yang terstruktur dan menarik secara visual.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "682",
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
    "url": "/net/floating-box/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/floating-box/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

Fitur ini juga berfungsi di [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## Dasar-dasar menggunakan alat FloatingBox

Alat Floating Box adalah alat khusus untuk menempatkan teks dan konten lainnya di halaman PDF. Fitur utamanya adalah pemotongan teks ketika melebihi ukuran FloatingBox.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateAndAddFloatingBox()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        // Create and fill box
        var box = new Aspose.Pdf.FloatingBox(400, 30)
        {
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1.5f, Aspose.Pdf.Color.DarkGreen),
            IsNeedRepeating = false,
        };
        box.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("text example"));
        // Add box
        page.Paragraphs.Add(box);
    }
}
```  

Dalam contoh di atas, kami membuat FloatingBox dengan lebar 400 pt dan tinggi 30 pt.
Selain itu, dalam contoh ini, lebih banyak teks sengaja dibuat daripada yang dapat muat dalam ukuran yang diberikan.
Akibatnya, teks terpotong.

![Gambar 1](image01.png)

Properti `IsNeedRepeating` dengan nilai `false` membatasi teks hanya pada 1 halaman.

Jika kami mengatur properti ini ke `true`, teks akan mengalir ke halaman berikutnya di posisi yang sama.

![Gambar 2](image02.png)

## Fitur lanjutan dari FloatingBox

### Dukungan multi-kolom

#### Tata letak multi-kolom (kasus sederhana)

`FloatingBox` mendukung tata letak multi-kolom. Untuk membuat tata letak seperti itu, Anda harus mendefinisikan nilai-nilai dari properti ColumnInfo.

* `ColumnWidths` adalah string dengan enumerasi lebar dalam pt.
* `ColumnSpacing` adalah string dengan lebar celah antara kolom.
* `ColumnCount` adalah jumlah kolom.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MultiColumnLayout()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tooltip();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Set margin settings
        page.PageInfo.Margin = new Aspose.Pdf.MarginInfo(36, 18, 36, 18);
        var columnCount = 3;
        var spacing = 10;
        var width = page.PageInfo.Width
            - page.PageInfo.Margin.Left
            - page.PageInfo.Margin.Right
            - (columnCount - 1) * spacing;
        var columnWidth = width / 3;
        // Create FloatingBox
        var box = new Aspose.Pdf.FloatingBox()
        {
            IsNeedRepeating = true
        };
        box.ColumnInfo.ColumnWidths = $"{columnWidth} {columnWidth} {columnWidth}";
        box.ColumnInfo.ColumnSpacing = $"{spacing}";
        box.ColumnInfo.ColumnCount = 3;

        var phrase = "text example";
        var paragraphs = new string[10]
        {
            phrase, phrase, phrase, phrase, phrase,
            phrase, phrase, phrase, phrase, phrase,
        };
        foreach (var paragraph in paragraphs)
        {
            box.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment(paragraph));
        }
        // Add a box to a page
        page.Paragraphs.Add(box);
        // Save PDF document
        document.Save(dataDir + "MultiColumnLayout_out.pdf");
    }
}
```

Kami menggunakan library tambahan LoremNET dalam contoh di atas dan membuat 20 paragraf. Paragraf-paragraf ini dibagi menjadi tiga kolom dan mengisi halaman berikutnya hingga teks habis.

#### Tata letak multi-kolom dengan pemaksaan awal kolom

Kami akan melakukan hal yang sama dengan contoh berikut seperti yang sebelumnya. Perbedaannya adalah kami membuat 3 paragraf. Kami dapat memaksa FloatingBox untuk merender setiap paragraf di kolom baru. Untuk melakukan itu, kami perlu mengatur `IsFirstParagraphInColumn` saat kami menambahkan teks ke objek FloatingBox.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MultiColumnLayout2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tooltip();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Set margin settings
        page.PageInfo.Margin = new Aspose.Pdf.MarginInfo(36, 18, 36, 18);
        var columnCount = 3;
        var spacing = 10;
        var width = page.PageInfo.Width
            - page.PageInfo.Margin.Left
            - page.PageInfo.Margin.Right
            - (columnCount - 1) * spacing;
        var columnWidth = width / 3;
        // Create the FloatingBox
        var box = new Aspose.Pdf.FloatingBox()
        {
            IsNeedRepeating = true
        };
        box.ColumnInfo.ColumnWidths = $"{columnWidth} {columnWidth} {columnWidth}";
        box.ColumnInfo.ColumnSpacing = $"{spacing}";
        box.ColumnInfo.ColumnCount = 3;

        var phrase = "text example";
        var paragraphs = new string[10]
        {
            phrase, phrase, phrase, phrase, phrase,
            phrase, phrase, phrase, phrase, phrase,
        };
        foreach (var paragraph in paragraphs)
        {
            var text = new Aspose.Pdf.Text.TextFragment(paragraph)
            {
                IsFirstParagraphInColumn = true
            };
            box.Paragraphs.Add(text);
        }

        // Add a box to a page
        page.Paragraphs.Add(box);
        // Save PDF document
        document.Save(dataDir + "MultiColumnLayout2_out.pdf");
    }
}
```

### Dukungan latar belakang

Anda dapat mengatur warna latar belakang yang diinginkan dengan menggunakan properti `BackgroundColor`.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void BackgroundSupport()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var box = new Aspose.Pdf.FloatingBox(400, 60)
        {
            IsNeedRepeating = false,
            BackgroundColor = Aspose.Pdf.Color.LightGreen,
        };
        var text = "text example";
        box.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment(text));
        page.Paragraphs.Add(box);
    }
}
```

### Dukungan penempatan

Lokasi FloatingBox di halaman yang dihasilkan ditentukan oleh properti `PositioningMode`, `Left`, `Top`.
Ketika nilai `PositioningMode` adalah
- `ParagraphPositioningMode.Default` (nilai default)
    Lokasi ditentukan oleh elemen yang ditempatkan sebelumnya.
    Penambahan elemen diperhitungkan saat menentukan lokasi elemen berikutnya.
    Jika nilai dari setidaknya satu dari properti Left, Top tidak nol, maka mereka juga diperhitungkan, tetapi ini menggunakan logika yang tidak sepenuhnya jelas dan sebaiknya tidak digunakan.

- `ParagraphPositioningMode.Absolute`
    Lokasi ditentukan oleh nilai Left dan Top, tidak tergantung pada elemen sebelumnya dan tidak mempengaruhi lokasi elemen berikutnya.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OffsetSupport()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create FloatingBox
        var box = new Aspose.Pdf.FloatingBox()
        {
            Top = 45,
            Left = 15,
            PositioningMode = Aspose.Pdf.ParagraphPositioningMode.Absolute
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1.5f, Aspose.Pdf.Color.DarkGreen)
        };
        box.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("text example 1"));

        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("text example 2"));
        // Add the box to the page
        page.Paragraphs.Add(box);
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("text example 3"));
    }
}
```