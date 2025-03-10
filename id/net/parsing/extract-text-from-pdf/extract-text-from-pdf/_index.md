---
title: Ekstrak Teks dari PDF C#
linktitle: Ekstrak Teks dari PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/extract-text-from-all-pdf/
description: Artikel ini menjelaskan berbagai cara untuk mengekstrak teks dari dokumen PDF menggunakan Aspose.PDF di C#.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Text from PDF C#",
    "alternativeHeadline": "Effortlessly Extract Text from PDFs in C#",
    "abstract": "Temukan fungsionalitas baru yang kuat di Aspose.PDF for .NET yang memungkinkan pengembang untuk dengan mudah mengekstrak teks dari dokumen PDF. Fitur ini mendukung ekstraksi dari semua halaman atau wilayah tertentu, mengakomodasi tata letak multi-kolom, dan bahkan memungkinkan pengambilan teks yang disorot hanya dengan beberapa baris kode. Tingkatkan kemampuan pemrosesan dokumen Anda dan permudah ekstraksi konten dengan alat serbaguna ini.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2005",
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
    "url": "/net/extract-text-from-all-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-text-from-all-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Ekstrak Teks Dari Semua Halaman Dokumen PDF

Mengekstrak teks dari dokumen PDF adalah kebutuhan umum. Dalam contoh ini, Anda akan melihat bagaimana Aspose.PDF for .NET memungkinkan ekstraksi teks dari semua halaman dokumen PDF. Anda perlu membuat objek dari kelas **TextAbsorber**. Setelah itu, buka PDF menggunakan kelas **Document** dan panggil metode **Accept** dari koleksi **Pages**. Kelas **TextAbsorber** menyerap teks dari dokumen dan mengembalikannya dalam properti **Text**. Potongan kode berikut menunjukkan cara mengekstrak teks dari semua halaman dokumen PDF.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextAll.pdf"))
    {
        // Create TextAbsorber object to extract text
        var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();

        // Accept the absorber for all the pages
        document.Pages.Accept(textAbsorber);

        // Get the extracted text
        string extractedText = textAbsorber.Text;

        // Create a writer and open the file
        using (TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt"))
        {
            // Write a line of text to the file
            tw.WriteLine(extractedText);
        }
    }
}
```

Panggil metode **Accept** pada halaman tertentu dari objek Document. Indeks adalah nomor halaman tertentu dari mana teks perlu diekstrak.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {

        // Create TextAbsorber object to extract text
        var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();

        // Accept the absorber for a particular page
        document.Pages[1].Accept(textAbsorber);

        // Get the extracted text
        string extractedText = textAbsorber.Text;

        // Create a writer and open the file
        using (TextWriter tw = new StreamWriter(dataDir + "extracted-text_out.txt"))
        {
            // Write a line of text to the file
            tw.WriteLine(extractedText);
        }
    }
}
```

## Ekstrak Teks dari Halaman Menggunakan Perangkat Teks

Anda dapat menggunakan kelas **TextDevice** untuk mengekstrak teks dari file PDF. **TextDevice** menggunakan **TextAbsorber** dalam implementasinya, sehingga, sebenarnya, mereka melakukan hal yang sama tetapi **TextDevice** hanya diimplementasikan untuk menyatukan pendekatan "Perangkat" untuk mengekstrak apa pun dari halaman seperti **ImageDevice**, **PageDevice**, dll. **TextAbsorber** dapat mengekstrak teks dari Halaman, seluruh PDF atau XForm, **TextAbsorber** ini lebih universal.

### Ekstrak teks dari semua halaman

Langkah-langkah dan potongan kode berikut menunjukkan cara mengekstrak teks dari PDF menggunakan perangkat teks.

1. Buat objek dari kelas Document dengan file PDF input yang ditentukan.
1. Buat objek dari kelas TextDevice.
1. Gunakan objek dari kelas TextExtractOptions untuk menentukan opsi ekstraksi.
1. Gunakan metode Process dari kelas TextDevice untuk mengonversi konten menjadi teks.
1. Simpan teks ke file output.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromPagesWithTextDevice()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    var builder = new System.Text.StringBuilder();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {
        // String to hold extracted text
        string extractedText = "";

        foreach (var page in document.Pages)
        {
            using (MemoryStream textStream = new MemoryStream())
            {
                // Create text device
                var textDevice = new Aspose.Pdf.Devices.TextDevice();

                // Set text extraction options - set text extraction mode (Raw or Pure)
                var textExtOptions = new Aspose.Pdf.Text.TextExtractionOptions(Aspose.Pdf.Text.TextExtractionOptions.TextFormattingMode.Pure);
                textDevice.ExtractionOptions = textExtOptions;

                // Convert a particular page and save text to the stream
                textDevice.Process(page, textStream);
                // Convert a particular page and save text to the stream
                textDevice.Process(document.Pages[1], textStream);

                // Get text from memory stream
                extractedText = System.Text.Encoding.Unicode.GetString(textStream.ToArray());
            }
            builder.Append(extractedText);
        }
    }

    // Save the extracted text in text file
    File.WriteAllText(dataDir + "input_Text_Extracted_out.txt", builder.ToString());
}
```

## Ekstrak Teks dari Wilayah Halaman Tertentu

Kelas **TextAbsorber** menyediakan kemampuan untuk mengekstrak teks dari halaman tertentu atau semua halaman dokumen PDF. Kelas ini mengembalikan teks yang diekstrak dalam properti **Text**. Namun, jika kita memiliki kebutuhan untuk mengekstrak teks dari wilayah halaman tertentu, kita dapat menggunakan properti **Rectangle** dari **TextSearchOptions**. Properti Rectangle mengambil objek Rectangle sebagai nilai dan menggunakan properti ini, kita dapat menentukan wilayah halaman dari mana kita perlu mengekstrak teks.

Metode **Accept** dari sebuah halaman dipanggil untuk mengekstrak teks. Buat objek dari kelas **Document** dan **TextAbsorber**. Panggil metode **Accept** pada halaman individu, sebagai Indeks **Page**, dari objek **Document**. **Index** adalah nomor halaman tertentu dari mana teks perlu diekstrak. Anda dapat mendapatkan teks dari properti **Text** dari kelas **TextAbsorber**. Potongan kode berikut menunjukkan cara mengekstrak teks dari halaman individu.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromParticularPageRegion()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextAll.pdf"))
    {
        // Create TextAbsorber object to extract text
        var absorber = new Aspose.Pdf.Text.TextAbsorber();
        absorber.TextSearchOptions.LimitToPageBounds = true;
        absorber.TextSearchOptions.Rectangle = new Aspose.Pdf.Rectangle(100, 200, 250, 350);

        // Accept the absorber for first page
        document.Pages[1].Accept(absorber);

        // Get the extracted text
        string extractedText = absorber.Text;

        // Create a writer and open the file
        using (TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt"))
        {
            // Write a line of text to the file
            tw.WriteLine(extractedText);
        }
    }
}
```

## Ekstrak teks berdasarkan kolom

File PDF dapat terdiri dari elemen Teks, Gambar, Anotasi, Lampiran, Grafik, dll dan Aspose.PDF for .NET menawarkan fitur untuk Menambahkan serta memanipulasi semua elemen ini. API ini luar biasa ketika datang ke penambahan dan ekstraksi Teks dari dokumen PDF dan kita mungkin menghadapi skenario di mana dokumen PDF terdiri dari lebih dari satu kolom (multi-kolom) dan kita perlu mengekstrak konten halaman sambil menghormati tata letak yang sama, maka Aspose.PDF for .NET adalah pilihan yang tepat untuk memenuhi kebutuhan ini. Salah satu pendekatan adalah mengurangi ukuran font konten di dalam dokumen PDF dan kemudian melakukan ekstraksi teks. Potongan kode berikut menunjukkan langkah-langkah untuk mengurangi ukuran teks dan kemudian mencoba mengekstrak teks dari dokumen PDF.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextBasedOnColumns()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    var extractedText = string.Empty;
    // Open PDF document
    using (var sourceDocument = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {

        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        sourceDocument.Pages.Accept(textFragmentAbsorber);
        Aspose.Pdf.Text.TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
        foreach (Aspose.Pdf.Text.TextFragment textFragment in textFragmentCollection)
        {
            // Need to reduce font size at least for 70%
            textFragment.TextState.FontSize = textFragment.TextState.FontSize * 0.7f;
        }
        using (Stream sourceStream = new MemoryStream())
        {
            sourceDocument.Save(sourceStream);
            using (var destDocument = new Aspose.Pdf.Document(sourceStream))
            {
                var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();
                destDocument.Pages.Accept(textAbsorber);
                extractedText = textAbsorber.Text;
                textAbsorber.Visit(destDocument);
            }
        }

        // Save the extracted text in text file
        File.WriteAllText(dataDir + "ExtractColumnsText_out.txt", extractedText);
    }
}
```

### Pendekatan Kedua - Menggunakan ScaleFactor

Dalam rilis baru ini, kami juga telah memperkenalkan beberapa perbaikan dalam **TextAbsorber** dan dalam mekanisme pemformatan teks internal. Jadi sekarang selama ekstraksi teks menggunakan mode 'Pure', Anda dapat menentukan opsi **ScaleFactor** dan ini bisa menjadi pendekatan lain untuk mengekstrak teks dari dokumen PDF multi-kolom selain pendekatan yang disebutkan di atas. Faktor skala ini dapat diatur untuk menyesuaikan grid yang digunakan untuk mekanisme pemformatan teks internal selama ekstraksi teks. Menentukan nilai **ScaleFactor** antara 1 dan 0.1 (termasuk 0.1) memiliki efek yang sama seperti pengurangan font.

Menentukan nilai **ScaleFactor** antara 0.1 dan -0.1 dianggap sebagai nilai nol, tetapi ini membuat algoritma menghitung faktor skala yang diperlukan selama ekstraksi teks secara otomatis. Perhitungan didasarkan pada lebar glyph rata-rata dari font yang paling populer di halaman, tetapi kami tidak dapat menjamin bahwa dalam teks yang diekstrak tidak ada string kolom yang mencapai awal kolom berikutnya. Harap dicatat bahwa jika nilai **ScaleFactor** tidak ditentukan, nilai default 1.0 akan digunakan. Ini berarti tidak ada penskalaan yang akan dilakukan. Jika nilai **ScaleFactor** yang ditentukan lebih dari 10 atau kurang dari -0.1, nilai default 1.0 akan digunakan.

Kami menyarankan penggunaan auto-scaling (**ScaleFactor = 0**) saat memproses sejumlah besar file PDF untuk ekstraksi konten teks. Atau secara manual mengatur pengurangan lebar grid yang berlebihan (sekitar **ScaleFactor = 0.5**). Namun, Anda tidak boleh menentukan apakah penskalaan diperlukan untuk dokumen tertentu atau tidak. Jika Anda mengatur pengurangan lebar grid yang berlebihan untuk dokumen (yang tidak membutuhkannya), konten teks yang diekstrak akan tetap sepenuhnya memadai. Harap lihat potongan kode berikut.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExctractTextWithScaleFactor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {

        var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();
        textAbsorber.ExtractionOptions = new Aspose.Pdf.Text.TextExtractionOptions(Aspose.Pdf.Text.TextExtractionOptions.TextFormattingMode.Pure);
        // Setting scale factor to 0.5 is enough to split columns in the majority of documents
        // Setting of zero allows to algorithm choose scale factor automatically
        textAbsorber.ExtractionOptions.ScaleFactor = 0.5; /* 0; */
        document.Pages.Accept(textAbsorber);
        var extractedText = textAbsorber.Text;

        // Save the extracted text in text file
        File.WriteAllText(dataDir + "ExtractTextUsingScaleFactor_out.text", extractedText);
    }
}
```

{{% alert color="primary" %}}

Harap dicatat bahwa tidak ada korespondensi langsung antara **ScaleFactor** baru dan koefisien lama pengurangan font secara manual. Namun, secara default algoritma mempertimbangkan nilai ukuran font yang telah dikurangi karena beberapa alasan internal. Misalnya, mengurangi ukuran font dari 10 menjadi 7 memiliki efek yang sama seperti mengatur faktor skala menjadi 5/8 (= 0.625).

{{% /alert %}}

## Ekstrak Teks yang Disorot dari Dokumen PDF

Dalam berbagai skenario ekstraksi teks dari dokumen PDF, Anda mungkin menghadapi kebutuhan untuk mengekstrak hanya teks yang disorot dari dokumen PDF. Untuk menerapkan fungsionalitas ini, kami telah menambahkan metode **TextMarkupAnnotation.GetMarkedText()** dan **TextMarkupAnnotation.GetMarkedTextFragments()** dalam API. Anda dapat mengekstrak teks yang disorot dari dokumen PDF dengan memfilter **TextMarkupAnnotation** dan menggunakan metode yang disebutkan. Potongan kode berikut menunjukkan bagaimana Anda dapat mengekstrak teks yang disorot dari dokumen PDF.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractHighlightedTextFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractHighlightedText.pdf"))
    {
        // Loop through all the annotations
        foreach (Aspose.Pdf.Annotations.Annotation annotation in document.Pages[1].Annotations)
        {
            // Filter TextMarkupAnnotation
            if (annotation is Aspose.Pdf.Annotations.TextMarkupAnnotation)
            {
                var highlightedAnnotation = annotation as Aspose.Pdf.Annotations.TextMarkupAnnotation;
                // Retrieve highlighted text fragments
                Aspose.Pdf.Text.TextFragmentCollection collection = highlightedAnnotation.GetMarkedTextFragments();
                foreach (Aspose.Pdf.Text.TextFragment textFragment in collection)
                {
                    // Display highlighted text
                    Console.WriteLine(textFragment.Text);
                }
            }
        }
    }
}
```

## Akses Elemen Fragmen Teks dan Segmen dari XML

Terkadang kita perlu mengakses item **TextFragment** atau **TextSegment** saat memproses dokumen PDF yang dihasilkan dari XML. Aspose.PDF for .NET menyediakan akses ke item-item tersebut berdasarkan nama. Potongan kode di bawah ini menunjukkan cara menggunakan fungsionalitas ini.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AccessTextFragmentAndSegmentElementsFromXML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.BindXml(dataDir + "40014.xml");

        // Get page
        var page = (Aspose.Pdf.Page)document.GetObjectById("mainSection");

        // Get elements by Id
        var segment = (Aspose.Pdf.Text.TextSegment)document.GetObjectById("boldHtml");
        segment = (Aspose.Pdf.Text.TextSegment)document.GetObjectById("strongHtml");

        // Save PDF document
        document.Save(dataDir + "DocumentFromXML_out.pdf");
    }
}
```