---
title: Manipulasi Dokumen PDF di C#
linktitle: Manipulasi Dokumen PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /id/net/manipulate-pdf-document/
description: Artikel ini berisi informasi tentang cara memvalidasi Dokumen PDF untuk Standar PDF A, cara bekerja dengan TOC, cara mengatur tanggal kedaluwarsa PDF, dan lain-lain.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipulate PDF Document in C#",
    "alternativeHeadline": "Enhanced PDF Manipulation Features in C# Library",
    "abstract": "Temukan kemampuan kuat untuk memanipulasi dokumen PDF di C#, termasuk validasi untuk standar PDF/A, kemampuan untuk membuat dan menyesuaikan tabel isi, dan mengatur tanggal kedaluwarsa untuk dokumen. Fitur ini tidak hanya meningkatkan manajemen dokumen tetapi juga memastikan kepatuhan terhadap standar industri, menjadikannya penting bagi pengembang yang mencari solusi penanganan PDF yang kuat.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "manipulate PDF, C#, validate PDF/A, TOC, set PDF expiry date, flatten fillable PDF, Aspose.PDF, PDF generation progress, customize page numbers, PDF encryption",
    "wordcount": "2499",
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
    "url": "/net/manipulate-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-pdf-document/"
    },
    "dateModified": "2025-04-04",
    "description": "Artikel ini berisi informasi tentang cara memvalidasi Dokumen PDF untuk Standar PDF A, cara bekerja dengan TOC, cara mengatur tanggal kedaluwarsa PDF, dan lain-lain."
}
</script>

## **Manipulasi Dokumen PDF di C#**

## Validasi Dokumen PDF untuk Standar PDF A (A 1A dan A 1B)

Untuk memvalidasi dokumen PDF untuk kompatibilitas PDF/A-1a atau PDF/A-1b, gunakan metode Validate dari kelas [Document](https://reference.aspose.com/pdf/id/net/aspose.pdf/document). Metode ini memungkinkan Anda untuk menentukan nama file tempat hasil akan disimpan dan jenis validasi yang diperlukan enumerasi [PdfFormat](https://reference.aspose.com/pdf/id/net/aspose.pdf/pdfformat): PDF_A_1A atau PDF_A_1B.

{{% alert color="primary" %}}

Format XML keluaran adalah format khusus Aspose. XML ini berisi koleksi tag dengan nama Problem; setiap tag berisi rincian dari masalah tertentu. Atribut ObjectID dari tag Problem mewakili ID dari objek tertentu yang terkait dengan masalah ini. Atribut Clause mewakili aturan yang sesuai dalam spesifikasi PDF.

{{% /alert %}}

Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

Potongan kode berikut menunjukkan cara memvalidasi dokumen PDF untuk PDF/A-1A.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ValidateToPdfA1aStandard()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ValidatePDFAStandard.pdf"))
    {
        // Validate PDF for PDF/A-1a
        document.Validate(dataDir + "validation-result-A1A.xml", Aspose.Pdf.PdfFormat.PDF_A_1A);
    }
}
```

Potongan kode berikut menunjukkan cara memvalidasi dokumen PDF untuk PDF/A-1b.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ValidateToPdfA1bStandard()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ValidatePDFAStandard.pdf"))
    {
        // Validate PDF for PDF/A-1b
        document.Validate(dataDir + "validation-result-A1B.xml", Aspose.Pdf.PdfFormat.PDF_A_1B);
    }
}
```

{{% alert color="primary" %}}

Aspose.PDF for .NET dapat digunakan untuk menentukan apakah dokumen yang dimuat adalah PDF yang valid dan juga [apakah terenkripsi atau tidak](https://docs.aspose.com/pdf/net/set-privileges-encrypt-and-decrypt-pdf-file/). Untuk lebih memperluas kemampuan kelas Document, properti *IsPdfaCompliant* ditambahkan untuk menentukan apakah file input sesuai dengan PDF/A dan sebuah properti bernama *PdfaFormat* untuk mengidentifikasi format PDF/A diperkenalkan.

{{% /alert %}}

## Bekerja dengan TOC

### Tambahkan TOC ke PDF yang Ada

API Aspose.PDF memungkinkan Anda untuk menambahkan tabel isi baik saat membuat PDF, atau ke file yang sudah ada. Kelas ListSection dalam namespace Aspose.Pdf.Generator memungkinkan Anda untuk membuat tabel isi saat membuat PDF dari awal. Untuk menambahkan judul, yang merupakan elemen dari TOC, gunakan kelas Aspose.Pdf.Generator.Heading.

Untuk menambahkan TOC ke file PDF yang ada, gunakan kelas Heading dalam namespace Aspose.PDF. Namespace Aspose.Pdf dapat membuat file PDF baru dan memanipulasi file PDF yang ada. Untuk menambahkan TOC ke PDF yang ada, gunakan namespace Aspose.PDF. Potongan kode berikut menunjukkan cara membuat tabel isi di dalam file PDF yang ada.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTOCToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddTOC.pdf"))
    {
        // Get access to the first page of PDF file
        var tocPage = document.Pages.Insert(1);

        // Create an object to represent TOC information
        var tocInfo = new Aspose.Pdf.TocInfo();
        var title = new Aspose.Pdf.Text.TextFragment("Table Of Contents");
        title.TextState.FontSize = 20;
        title.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Set the title for TOC
        tocInfo.Title = title;
        tocPage.TocInfo = tocInfo;

        // Create string objects which will be used as TOC elements
        string[] titles = { "First page", "Second page", "Third page", "Fourth page" };

        for (int i = 0; i < 2; i++)
        {
            // Create Heading object
            var heading = new Aspose.Pdf.Heading(1);
            var segment = new Aspose.Pdf.Text.TextSegment();
            heading.TocPage = tocPage;
            heading.Segments.Add(segment);

            // Specify the destination page for the heading object
            heading.DestinationPage = document.Pages[i + 2];

            // Destination page
            heading.Top = document.Pages[i + 2].Rect.Height;

            // Destination coordinate
            segment.Text = titles[i];

            // Add heading to the page containing TOC
            tocPage.Paragraphs.Add(heading);
        }

        // Save PDF document
        document.Save(dataDir + "TOC_out.pdf");
    }
}
```

### Atur TabLeaderType yang berbeda untuk Tingkat TOC yang berbeda

Aspose.PDF juga memungkinkan pengaturan TabLeaderType yang berbeda untuk tingkat TOC yang berbeda. Anda perlu mengatur properti LineDash dari FormatArray dengan nilai yang sesuai dari enum TabLeaderType sebagai berikut.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateTocWithCustomFormatting()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add a TOC page
        var tocPage = document.Pages.Add();

        // Create TOC information
        var tocInfo = new Aspose.Pdf.TocInfo();

        // Set LeaderType
        tocInfo.LineDash = Aspose.Pdf.Text.TabLeaderType.Solid;

        // Set the title for TOC
        var title = new Aspose.Pdf.Text.TextFragment("Table Of Contents");
        title.TextState.FontSize = 30;
        tocInfo.Title = title;

        // Add the TOC section to the document
        tocPage.TocInfo = tocInfo;

        // Define the format of the four levels list by setting the left margins
        // and text format settings of each level
        tocInfo.FormatArrayLength = 4;

        // Level 1
        tocInfo.FormatArray[0].Margin.Left = 0;
        tocInfo.FormatArray[0].Margin.Right = 30;
        tocInfo.FormatArray[0].LineDash = Aspose.Pdf.Text.TabLeaderType.Dot;
        tocInfo.FormatArray[0].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold | Aspose.Pdf.Text.FontStyles.Italic;

        // Level 2
        tocInfo.FormatArray[1].Margin.Left = 10;
        tocInfo.FormatArray[1].Margin.Right = 30;
        tocInfo.FormatArray[1].LineDash = Aspose.Pdf.Text.TabLeaderType.None;
        tocInfo.FormatArray[1].TextState.FontSize = 10;

        // Level 3
        tocInfo.FormatArray[2].Margin.Left = 20;
        tocInfo.FormatArray[2].Margin.Right = 30;
        tocInfo.FormatArray[2].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Level 4
        tocInfo.FormatArray[3].LineDash = Aspose.Pdf.Text.TabLeaderType.Solid;
        tocInfo.FormatArray[3].Margin.Left = 30;
        tocInfo.FormatArray[3].Margin.Right = 30;
        tocInfo.FormatArray[3].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Create a section in the Pdf document
        var page = document.Pages.Add();

        // Add four headings in the section
        for (int level = 1; level <= 4; level++)
        {
            var heading = new Aspose.Pdf.Heading(level);
            var segment = new Aspose.Pdf.Text.TextSegment();
            heading.Segments.Add(segment);
            heading.IsAutoSequence = true;
            heading.TocPage = tocPage;
            segment.Text = "Sample Heading " + level;
            heading.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial Unicode MS");

            // Add the heading into Table Of Contents.
            heading.IsInList = true;
            page.Paragraphs.Add(heading);
        }

        // Save PDF document
        document.Save(dataDir + "TOC_out.pdf");
    }
}
```

### Sembunyikan Nomor Halaman di TOC

Jika Anda tidak ingin menampilkan nomor halaman, bersama dengan judul di TOC, Anda dapat menggunakan properti [IsShowPageNumbers](https://reference.aspose.com/pdf/id/net/aspose.pdf/tocinfo/properties/isshowpagenumbers) dari Kelas [TOCInfo](https://reference.aspose.com/pdf/id/net/aspose.pdf/tocinfo) sebagai false. Silakan periksa potongan kode berikut untuk menyembunyikan nomor halaman di tabel isi:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateTocWithHiddenPageNumbers()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add a TOC page
        var tocPage = document.Pages.Add();

        // Create TOC information
        var tocInfo = new Aspose.Pdf.TocInfo();

        // Set the title for TOC
        var title = new Aspose.Pdf.Text.TextFragment("Table Of Contents");
        title.TextState.FontSize = 20;
        title.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
        tocInfo.Title = title;

        // Add the TOC section to the document
        tocPage.TocInfo = tocInfo;

        // Hide page numbers in TOC
        tocInfo.IsShowPageNumbers = false;

        // Define the format of the four levels list by setting the left margins and
        // text format settings of each level
        tocInfo.FormatArrayLength = 4;

        // Level 1
        tocInfo.FormatArray[0].Margin.Right = 0;
        tocInfo.FormatArray[0].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold | Aspose.Pdf.Text.FontStyles.Italic;

        // Level 2
        tocInfo.FormatArray[1].Margin.Left = 30;
        tocInfo.FormatArray[1].TextState.Underline = true;
        tocInfo.FormatArray[1].TextState.FontSize = 10;

        // Level 3
        tocInfo.FormatArray[2].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Level 4
        tocInfo.FormatArray[3].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Create a section in the Pdf document
        var page = document.Pages.Add();

        // Add four headings in the section
        for (int level = 1; level <= 4; level++)
        {
            var heading = new Aspose.Pdf.Heading(level);
            var segment = new Aspose.Pdf.Text.TextSegment();
            heading.TocPage = tocPage;
            heading.Segments.Add(segment);
            heading.IsAutoSequence = true;
            segment.Text = "this is heading of level " + level;
            heading.IsInList = true;
            page.Paragraphs.Add(heading);
        }

        // Save PDF document
        document.Save(dataDir + "TOC_out.pdf");
    }
}
```

### Sesuaikan Nomor Halaman saat menambahkan TOC

Umum untuk menyesuaikan penomoran halaman di TOC saat menambahkan TOC dalam dokumen PDF. Misalnya, kita mungkin perlu menambahkan beberapa awalan sebelum nomor halaman seperti P1, P2, P3 dan seterusnya. Dalam hal ini, Aspose.PDF for .NET menyediakan properti PageNumbersPrefix dari kelas TocInfo yang dapat digunakan untuk menyesuaikan nomor halaman seperti yang ditunjukkan dalam contoh kode berikut.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CustomizePageNumbersAddingToC()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "CustomizePageNumbersAddingToC.pdf"))
    {
        // Get access to first page of PDF file
        Page tocPage = document.Pages.Insert(1);

        // Create object to represent TOC information
        var tocInfo = new Aspose.Pdf.TocInfo();
        var title = new Aspose.Pdf.Text.TextFragment("Table Of Contents");
        title.TextState.FontSize = 20;
        title.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Set the title for TOC
        tocInfo.Title = title;
        tocInfo.PageNumbersPrefix = "P";
        tocPage.TocInfo = tocInfo;

        // Loop through the pages to create TOC entries
        for (int i = 1; i < document.Pages.Count; i++)
        {
            // Create Heading object
            var heading2 = new Aspose.Pdf.Heading(1);
            var segment2 = new Aspose.Pdf.Text.TextSegment();
            heading2.TocPage = tocPage;
            heading2.Segments.Add(segment2);

            // Specify the destination page for heading object
            heading2.DestinationPage = document.Pages[i + 1];

            // Destination page
            heading2.Top = document.Pages[i + 1].Rect.Height;

            // Destination coordinate
            segment2.Text = "Page " + i.ToString();

            // Add heading to page containing TOC
            tocPage.Paragraphs.Add(heading2);
        }

        // Save PDF document
        document.Save(dataDir + "CustomizePageNumbersAddingToC_out.pdf");
    }
}
```

## Cara mengatur tanggal kedaluwarsa PDF

Kami menerapkan hak akses pada file PDF sehingga sekelompok pengguna tertentu dapat mengakses fitur/objek tertentu dari dokumen PDF. Untuk membatasi akses file PDF, kami biasanya menerapkan enkripsi dan kami mungkin memiliki kebutuhan untuk mengatur kedaluwarsa file PDF, sehingga pengguna yang mengakses/melihat dokumen mendapatkan prompt yang valid mengenai kedaluwarsa file PDF.

Untuk memenuhi kebutuhan yang dinyatakan di atas, kami dapat menggunakan objek *JavascriptAction*. Silakan lihat potongan kode berikut.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetExpiryDate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Add text fragment to paragraphs collection of page object
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World..."));

        // Create JavaScript object to set PDF expiry date
        var javaScript = new Aspose.Pdf.Annotations.JavascriptAction(
            "var year=2017;" +
            "var month=5;" +
            "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());" +
            "expiry = new Date(year, month);" +
            "if (today.getTime() > expiry.getTime())" +
            "app.alert('The file is expired. You need a new one.');"
        );

        // Set JavaScript as PDF open action
        document.OpenAction = javaScript;

        // Save PDF Document
        document.Save(dataDir + "SetExpiryDate_out.pdf");
    }
}
```

## Menentukan Kemajuan Generasi File PDF

Seorang pelanggan meminta kami untuk menambahkan fitur yang memungkinkan pengembang untuk menentukan kemajuan generasi file PDF. Berikut adalah tanggapan terhadap permintaan itu.

Bidang [CustomerProgressHandler](https://reference.aspose.com/pdf/id/net/aspose.pdf/docsaveoptions/fields/customprogresshandler) dari kelas [DocSaveOptions](https://reference.aspose.com/pdf/id/net/aspose.pdf/docsaveoptions) memungkinkan Anda untuk menentukan bagaimana kemajuan generasi PDF. Penangan memiliki jenis berikut:

- DocSaveOptions.ConversionProgessEventHandler.
- DocSaveOptions.ProgressEventHandlerInfo.
- DocSaveOptions.ProgressEventType.

Potongan kode di bawah ini menunjukkan cara menggunakan CustomerProgressHandler.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DetermineProgress()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddTOC.pdf"))
    {
        // Create DocSaveOptions instance and set custom progress handler
        var saveOptions = new Aspose.Pdf.DocSaveOptions();
        saveOptions.CustomProgressHandler = new Aspose.Pdf.UnifiedSaveOptions.ConversionProgressEventHandler(ShowProgressOnConsole);

        // Save PDF Document
        document.Save(dataDir + "DetermineProgress_out.pdf", saveOptions);
    }
}

// Method to handle progress and display it on the console
private static void ShowProgressOnConsole(Aspose.Pdf.UnifiedSaveOptions.ProgressEventHandlerInfo eventInfo)
{
    switch (eventInfo.EventType)
    {
        case Aspose.Pdf.ProgressEventType.TotalProgress:
            Console.WriteLine(String.Format("{0}  - Conversion progress : {1}% .", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString()));
            break;
        case Aspose.Pdf.ProgressEventType.SourcePageAnalysed:
            Console.WriteLine(String.Format("{0}  - Source page {1} of {2} analyzed.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case Aspose.Pdf.ProgressEventType.ResultPageCreated:
            Console.WriteLine(String.Format("{0}  - Result page's {1} of {2} layout created.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case Aspose.Pdf.ProgressEventType.ResultPageSaved:
            Console.WriteLine(String.Format("{0}  - Result page {1} of {2} exported.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        default:
            break;
    }
}
```

## Ratakan PDF yang Dapat Diisi

Dokumen PDF sering kali menyertakan formulir dengan widget interaktif yang dapat diisi seperti tombol radio, kotak centang, kotak teks, daftar, dll. Untuk membuatnya tidak dapat diedit untuk berbagai tujuan aplikasi, kami perlu meratakan file PDF.
Aspose.PDF menyediakan fungsi untuk meratakan PDF Anda di C# hanya dengan beberapa baris kode:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenForms()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Flatten Fillable PDF
        if (document.Form.Fields.Count() > 0)
        {
            foreach (var item in document.Form.Fields)
            {
                item.Flatten();
            }
        }

        // Save PDF document
        document.Save(dataDir + "FlattenForms_out.pdf");
    }
}
```

## Menganalisis dokumen PDF untuk Pembaruan Inkremental
Untuk memeriksa apakah dokumen telah diperbarui secara inkremental, gunakan metode `HasIncrementalUpdate` dari kelas [Document](https://reference.aspose.com/pdf/id/net/aspose.pdf/document). Metode ini menganalisis file PDF dan mengembalikan nilai boolean yang menunjukkan apakah pembaruan inkremental terdeteksi. Perhatikan bahwa ketika dokumen disimpan menggunakan metode [Save](https://reference.aspose.com/pdf/id/net/aspose.pdf/document/save/#save) tanpa parameter, dokumen disimpan secara inkremental.

Potongan kode C# berikut menunjukkan cara menggunakan metode `HasIncrementalUpdate`:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IncrementalUpdatesCheck()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Check for incremental updates
        bool updatedIncrementally = document.HasIncrementalUpdate();

        // Output the result
        if (updatedIncrementally)
        {
            Console.WriteLine("This document has been incrementally updated.");
        }
        else
        {
            Console.WriteLine("This document has no incremental updates.");
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IncrementalUpdatesCheck()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Check for incremental updates
    bool updatedIncrementally = document.HasIncrementalUpdate();

    // Output the result
    if (updatedIncrementally)
    {
        Console.WriteLine("This document has been incrementally updated.");
    }
    else
    {
        Console.WriteLine("This document has no incremental updates.");
    }
}
```
{{< /tab >}}
{{< /tabs >}}

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