---
title: Pemformatan Teks di dalam PDF menggunakan C#
linktitle: Pemformatan Teks di dalam PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /id/net/text-formatting-inside-pdf/
description: Pelajari cara memformat teks dalam dokumen PDF di .NET menggunakan Aspose.PDF untuk meningkatkan presentasi visual dokumen.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Text Formatting inside PDF using C#",
    "alternativeHeadline": "Enhance PDF Text Formatting with New C# Features",
    "abstract": "Temukan kemampuan pemformatan teks yang kuat dari Aspose.PDF for .NET, yang memungkinkan Anda menambahkan indentasi baris, batas teks, efek garis bawah, dan lainnya ke dokumen PDF Anda. Fitur ini memungkinkan kontrol yang tepat atas estetika dan tata letak teks, meningkatkan presentasi keseluruhan file PDF Anda. Optimalkan alur kerja pembuatan PDF Anda dengan opsi pemformatan yang serbaguna yang dirancang untuk pengembang.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1642",
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
    "url": "/net/text-formatting-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-formatting-inside-pdf/"
    },
    "dateModified": "2024-11-26",
    "description": "Halaman ini menjelaskan cara memformat teks di dalam file PDF Anda. Ada penambahan indentasi baris, penambahan batas teks, penambahan teks garis bawah, dan lain-lain."
}
</script>

Potongan kode berikut juga bekerja dengan [Aspose.PDF.Drawing](/pdf/id/net/drawing/) library.

## Cara menambahkan Indentasi Baris ke PDF

Aspose.PDF for .NET menawarkan properti SubsequentLinesIndent ke dalam kelas [TextFormattingOptions](https://reference.aspose.com/pdf/id/net/aspose.pdf.text/textformattingoptions). Yang dapat digunakan untuk menentukan indentasi baris dalam skenario pembuatan PDF dengan koleksi TextFragment dan Paragraphs.

Silakan gunakan potongan kode berikut untuk menggunakan properti tersebut:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void TextFormattingInsidePdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        string textFragment = string.Concat(Enumerable.Repeat("A quick brown fox jumped over the lazy dog. ", 10));

        Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment(textFragment);

        // Initilize TextFormattingOptions for the text fragment and specify SubsequentLinesIndent value
        text.TextState.FormattingOptions = new Aspose.Pdf.Text.TextFormattingOptions()
        {
            SubsequentLinesIndent = 20
        };

        page.Paragraphs.Add(text);

        text = new Aspose.Pdf.Text.TextFragment("Line2");
        page.Paragraphs.Add(text);

        text = new Aspose.Pdf.Text.TextFragment("Line3");
        page.Paragraphs.Add(text);

        text = new Aspose.Pdf.Text.TextFragment("Line4");
        page.Paragraphs.Add(text);

        text = new Aspose.Pdf.Text.TextFragment("Line5");
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "SubsequentIndent_out.pdf");
    }
}
```

## Cara menambahkan Batas Teks

Potongan kode berikut menunjukkan cara menambahkan batas pada teks menggunakan TextBuilder dan mengatur properti DrawTextRectangleBorder dari TextState:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextBorder()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get particular page
        var page = document.Pages.Add();
        // Create text fragment
        var textFragment = new Aspose.Pdf.Text.TextFragment("main text");
        textFragment.Position = new Aspose.Pdf.Text.Position(100, 600);
        // Set text properties
        textFragment.TextState.FontSize = 12;
        textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
        textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
        // Set StrokingColor property for drawing border (stroking) around text rectangle
        textFragment.TextState.StrokingColor = Aspose.Pdf.Color.DarkRed;
        // Set DrawTextRectangleBorder property value to true
        textFragment.TextState.DrawTextRectangleBorder = true;
        var tb = new Aspose.Pdf.Text.TextBuilder(page);
        tb.AppendText(textFragment);

        // Save PDF document
        document.Save(dataDir + "PDFWithTextBorder_out.pdf");
    }
}
```

## Cara menambahkan Teks Garis Bawah

Potongan kode berikut menunjukkan kepada Anda cara menambahkan teks garis bawah saat membuat file PDF baru.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddUnderlineText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add age page to PDF document
        document.Pages.Add();
        // Create TextBuilder for first page
        var tb = new Aspose.Pdf.Text.TextBuilder(document.Pages[1]);
        // TextFragment with sample text
        var fragment = new Aspose.Pdf.Text.TextFragment("Test message");
        // Set the font for TextFragment
        fragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        fragment.TextState.FontSize = 10;
        // Set the formatting of text as Underline
        fragment.TextState.Underline = true;
        // Specify the position where TextFragment needs to be placed
        fragment.Position = new Aspose.Pdf.Text.Position(10, 800);
        // Append TextFragment to PDF file
        tb.AppendText(fragment);

        // Save PDF document
        document.Save(dataDir + "AddUnderlineText_out.pdf");
    }
}
```

## Cara menambahkan Batas di Sekitar Teks yang Ditambahkan

Anda memiliki kontrol atas tampilan dan nuansa teks yang Anda tambahkan. Contoh di bawah ini menunjukkan cara menambahkan batas di sekitar sepotong teks yang telah Anda tambahkan dengan menggambar persegi panjang di sekitarnya. Temukan lebih lanjut tentang kelas [PdfContentEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfcontenteditor).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBorder()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    
    // Open PDF document
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "AddBorder.pdf");
        var lineInfo = new Aspose.Pdf.Facades.LineInfo();
        lineInfo.LineWidth = 2;
        lineInfo.VerticeCoordinate = new float[] { 0, 0, 100, 100, 50, 100 };
        lineInfo.Visibility = true;
        // Add border
        editor.CreatePolygon(lineInfo, 1, new System.Drawing.Rectangle(0, 0, 0, 0), "");

        // Save PDF document
        editor.Save(dataDir + "AddingBorderAroundAddedText_out.pdf");
    }
}
```

## Cara menambahkan Umpan NewLine

TextFragment tidak mendukung umpan baris di dalam teks. Namun, untuk menambahkan teks dengan umpan baris, silakan gunakan TextFragment dengan TextParagraph:

- Gunakan "\r\n" atau Environment.NewLine di TextFragment sebagai pengganti "\n" tunggal.
- Buat objek TextParagraph. Ini akan menambahkan teks dengan pemisahan baris.
- Tambahkan TextFragment dengan TextParagraph.AppendLine.
- Tambahkan TextParagraph dengan TextBuilder.AppendParagraph.

Silakan gunakan potongan kode di bawah ini.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddNewLine()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        // Initialize new TextFragment with text containing required newline markers
        var textFragment = new Aspose.Pdf.Text.TextFragment("Applicant Name: " + Environment.NewLine + " Joe Smoe");

        // Set text fragment properties if necessary
        textFragment.TextState.FontSize = 12;
        textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
        textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

        // Create TextParagraph object
        var par = new Aspose.Pdf.Text.TextParagraph();

        // Add new TextFragment to paragraph
        par.AppendLine(textFragment);

        // Set paragraph position
        par.Position = new Aspose.Pdf.Text.Position(100, 600);

        // Create TextBuilder object
        var textBuilder = new Aspose.Pdf.Text.TextBuilder(page);
        // Add the TextParagraph using TextBuilder
        textBuilder.AppendParagraph(par);

        // Save PDF document
        document.Save(dataDir + "AddNewLineFeed_out.pdf");
    }
}
```

## Cara menambahkan Teks StrikeOut

Kelas TextState menyediakan kemampuan untuk mengatur pemformatan untuk TextFragments yang ditempatkan di dalam dokumen PDF. Anda dapat menggunakan kelas ini untuk mengatur pemformatan teks sebagai Bold, Italic, Garis Bawah dan mulai rilis ini, API telah menyediakan kemampuan untuk menandai pemformatan teks sebagai Strikeout. Silakan coba menggunakan potongan kode berikut untuk menambahkan TextFragment dengan pemformatan Strikeout.

Silakan gunakan potongan kode lengkap:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddStrikeoutText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get particular page
        var page = document.Pages.Add();

        // Create text fragment
        var textFragment = new Aspose.Pdf.Text.TextFragment("main text");
        textFragment.Position = new Aspose.Pdf.Text.Position(100, 600);

        // Set text properties
        textFragment.TextState.FontSize = 12;
        textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
        textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
        // Set StrikeOut property
        textFragment.TextState.StrikeOut = true;
        // Mark text as Bold
        textFragment.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Create TextBuilder object
        var textBuilder = new Aspose.Pdf.Text.TextBuilder(page);
        // Append the text fragment to the PDF page
        textBuilder.AppendText(textFragment);

        // Save PDF document
        document.Save(dataDir + "AddStrikeOutText_out.pdf");
    }
}
```

## Terapkan Gradasi Bayangan pada Teks

Pemformatan teks telah ditingkatkan lebih lanjut dalam API untuk skenario pengeditan teks dan sekarang Anda dapat menambahkan teks dengan ruang warna pola di dalam dokumen PDF. Kelas Aspose.Pdf.Color telah ditingkatkan lebih lanjut dengan memperkenalkan properti baru dari PatternColorSpace, yang dapat digunakan untuk menentukan warna bayangan untuk teks. Properti baru ini menambahkan Gradasi Bayangan yang berbeda pada teks, misalnya Gradasi Axial, Gradasi Radial (Tipe 3) seperti yang ditunjukkan dalam potongan kode berikut:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ApplyGradientShadingToText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "text_sample4.pdf"))
    {
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("Lorem ipsum");
        document.Pages.Accept(absorber);

        var textFragment = absorber.TextFragments[1];

        // Create new color with pattern colorspace
        textFragment.TextState.ForegroundColor = new Aspose.Pdf.Color()
        {
            PatternColorSpace = new Aspose.Pdf.Drawing.GradientAxialShading(Aspose.Pdf.Color.Red, Aspose.Pdf.Color.Blue)
        };
        textFragment.TextState.Underline = true;

        // Save PDF document
        document.Save(dataDir +"ApplyGradientShadingToText_out.pdf");
    }
}
```

>Untuk menerapkan Gradasi Radial, Anda dapat mengatur properti ‘PatternColorSpace’ sama dengan ‘Aspose.Pdf.Drawing.GradientRadialShading(startingColor, endingColor)’ dalam potongan kode di atas.

## Cara menyelaraskan teks dengan konten mengambang

Aspose.PDF mendukung pengaturan penyelarasan teks untuk konten di dalam elemen Floating Box. Properti penyelarasan dari instance Aspose.Pdf.FloatingBox dapat digunakan untuk mencapai ini seperti yang ditunjukkan dalam contoh kode berikut.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AlignTextToFloat()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        // Create float box
        Aspose.Pdf.FloatingBox floatBox = new Aspose.Pdf.FloatingBox(100, 100);
        // Set settings to float box
        floatBox.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Bottom;
        floatBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
        floatBox.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("FloatingBox_bottom"));
        floatBox.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
        // Add float box
        page.Paragraphs.Add(floatBox);

        // Create float box
        Aspose.Pdf.FloatingBox floatBox1 = new Aspose.Pdf.FloatingBox(100, 100);
        // Set settings to float box
        floatBox1.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Center;
        floatBox1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
        floatBox1.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("FloatingBox_center"));
        floatBox1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
        // Add float box
        page.Paragraphs.Add(floatBox1);

        // Create float box
        Aspose.Pdf.FloatingBox floatBox2 = new Aspose.Pdf.FloatingBox(100, 100);
        // Set settings to float box
        floatBox2.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        floatBox2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
        floatBox2.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("FloatingBox_top"));
        floatBox2.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
        // Add float box
        page.Paragraphs.Add(floatBox2);

        // Save PDF document
        document.Save(dataDir + "FloatingBox_alignment_review_out.pdf");
    }
}
```

## Cara menghapus teks tersembunyi dari file PDF

Pertama, potongan kode membuat objek Document dari sebuah file. Kemudian, ia menambahkan TextFragmentAbsorber untuk menemukan dan mengedit teks. Kemudian, ia memeriksa teks tersembunyi dan menghapusnya. Akhirnya, ia menyimpan dokumen yang diperbarui.

Metode ini menjaga teks yang terlihat tetap utuh dan mempertahankan tata letak.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveHiddenText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "HiddenText.pdf"))
    {
        var textAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();

        // This option can be used to prevent other text fragments from moving after hidden text replacement
        textAbsorber.TextReplaceOptions = new Aspose.Pdf.Text.TextReplaceOptions(Aspose.Pdf.Text.TextReplaceOptions.ReplaceAdjustment.None);

        document.Pages.Accept(textAbsorber);

        // Remove hidden text
        foreach (var fragment in textAbsorber.TextFragments)
        {
            if (fragment.TextState.Invisible)
            {
                fragment.Text = "";
            }
        }

        // Save PDF document
        document.Save(dataDir + "HiddenText_out.pdf");
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