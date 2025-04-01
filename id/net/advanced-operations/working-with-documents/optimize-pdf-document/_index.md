---
title: Optimalkan, Kompres, atau Kurangi Ukuran PDF di C#
linktitle: Optimalkan PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /id/net/optimize-pdf/
description: Optimalkan file PDF, perkecil semua gambar, kurangi ukuran PDF, Lepaskan font, Hapus objek yang tidak digunakan dengan C#.
lastmod: "2022-02-17"
sitemap:
changefreq: "monthly"
priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Optimize, Compress or Reduce PDF Size in C#",
    "alternativeHeadline": "Optimize PDF Files Efficiently with C#",
    "abstract": "Fitur optimasi PDF baru di C# memungkinkan pengembang untuk secara signifikan mengurangi ukuran file PDF dengan menggunakan berbagai strategi, seperti mengompres gambar, melepaskan font, dan menghapus objek yang tidak digunakan. Peningkatan ini meningkatkan efisiensi untuk penerbitan web, berbagi email, dan penyimpanan, memberikan solusi efektif untuk mengelola dokumen PDF besar.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "optimize pdf, compress pdf size, reduce pdf size, optimize pdf c#, unembed fonts, remove unused objects, shrink images, optimization methods, pdf document generation, Aspose.PDF",
    "wordcount": "2682",
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
    "url": "/net/optimize-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/optimize-pdf/"
    },
    "dateModified": "2025-04-01",
    "description": "Optimalkan file PDF, perkecil semua gambar, kurangi ukuran PDF, Lepaskan font, Hapus objek yang tidak digunakan dengan C#."
}
</script>

Dokumen PDF terkadang dapat berisi data tambahan. Mengurangi ukuran file PDF akan membantu Anda mengoptimalkan transfer jaringan dan penyimpanan. Ini sangat berguna untuk penerbitan di halaman web, berbagi di jejaring sosial, mengirim melalui email, atau mengarsipkan di penyimpanan. Kita dapat menggunakan beberapa teknik untuk mengoptimalkan PDF:

- Optimalkan konten halaman untuk penelusuran online.
- Perkecil atau kompres semua gambar.
- Aktifkan penggunaan kembali konten halaman.
- Gabungkan aliran duplikat.
- Lepaskan font.
- Hapus objek yang tidak digunakan.
- Hapus atau ratakan bidang formulir.
- Hapus atau ratakan anotasi.

{{% alert color="primary" %}}

Penjelasan rinci tentang metode optimasi dapat ditemukan di halaman Ikhtisar Metode Optimasi.

{{% /alert %}}

## Optimalkan Dokumen PDF untuk Web

Optimasi, atau linearization untuk Web, mengacu pada proses membuat file PDF cocok untuk penelusuran online menggunakan browser web. Untuk mengoptimalkan file untuk tampilan web:

1. Buka dokumen input dalam objek [Document](https://reference.aspose.com/pdf/id/net/aspose.pdf/document).
1. Gunakan metode [Optimize](https://reference.aspose.com/pdf/id/net/aspose.pdf/document/methods/optimize).
1. Simpan dokumen yang telah dioptimalkan menggunakan metode [Save](https://reference.aspose.com/pdf/id/net/aspose.pdf/document/methods/save).

Cuplikan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

Cuplikan kode berikut menunjukkan cara mengoptimalkan dokumen PDF untuk web.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizeDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Optimize for web
        document.Optimize();

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

## Kurangi Ukuran PDF

Metode [OptimizeResources()](https://reference.aspose.com/pdf/id/net/aspose.pdf/document/methods/optimizeresources) memungkinkan Anda untuk mengurangi ukuran dokumen dengan menghapus informasi yang tidak perlu. Secara default, metode ini bekerja sebagai berikut:

- Sumber daya yang tidak digunakan di halaman dokumen dihapus.
- Sumber daya yang sama digabungkan menjadi satu objek.
- Objek yang tidak digunakan dihapus.

Cuplikan di bawah ini adalah contohnya. Namun, perlu dicatat bahwa metode ini tidak dapat menjamin pengurangan ukuran dokumen.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShrinkDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ShrinkDocument.pdf"))
    {
        // Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
        document.OptimizeResources();

        // Save PDF document
        document.Save(dataDir + "ShrinkDocument_out.pdf");
    }
}
```

## Manajemen Strategi Optimasi

Kita juga dapat menyesuaikan strategi optimasi. Saat ini, metode [OptimizeResources()](https://reference.aspose.com/pdf/id/net/aspose.pdf.document/optimizeresources/methods/1) menggunakan 5 teknik. Teknik-teknik ini dapat diterapkan menggunakan metode OptimizeResources() dengan parameter [OptimizationOptions](https://reference.aspose.com/pdf/id/net/aspose.pdf.optimization/optimizationoptions).

### Mengurangi atau Mengompres Semua Gambar

Kita memiliki dua cara untuk bekerja dengan gambar: mengurangi kualitas gambar dan/atau mengubah resolusinya. Dalam hal ini, [ImageCompressionOptions](https://reference.aspose.com/pdf/id/net/aspose.pdf.optimization/imagecompressionoptions) harus diterapkan. Dalam contoh berikut, kita memperkecil gambar dengan mengurangi [ImageQuality](https://reference.aspose.com/pdf/id/net/aspose.pdf.optimization/imagecompressionoptions/properties/imagequality) menjadi 50.

`ImageQuality` bekerja mirip dengan kualitas JPEG, di mana nilai 0 adalah yang terendah dan nilai 100 adalah yang tertinggi.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShrinkImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Shrinkimage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // Set CompressImages option
        // If this flag is set to true images will be compressed in the document
        optimizeOptions.ImageCompressionOptions.CompressImages = true;

        // Set ImageQuality option
        // Specifies level of image compression when CompressImages flag is used
        optimizeOptions.ImageCompressionOptions.ImageQuality = 50;

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "Shrinkimage_out.pdf");
    }
}
```

Cara lain adalah dengan mengubah ukuran gambar dengan resolusi yang lebih rendah. Dalam hal ini, kita harus mengatur ResizeImages menjadi true dan MaxResolution ke nilai yang sesuai.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ResizeImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ResizeImage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // Set CompressImages option
        // If this flag is set to true images will be compressed in the document
        optimizeOptions.ImageCompressionOptions.CompressImages = true;

        // Set ImageQuality option
        // Specifies level of image compression when CompressImages flag is used
        optimizeOptions.ImageCompressionOptions.ImageQuality = 75;

        // Set ResizeImage option
        // If this flag set to true and CompressImages is true images will be resized if image resoultion is greater then specified MaxResolution parameter
        optimizeOptions.ImageCompressionOptions.ResizeImages = true;

        // Set MaxResolution option
        // Specifies maximum resolution of images. If image has higher resolition it will be scaled
        optimizeOptions.ImageCompressionOptions.MaxResolution = 300;

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "ResizeImages_out.pdf");
    }
}
```

Masalah penting lainnya adalah waktu eksekusi. Namun, kita juga dapat mengelola pengaturan ini. Saat ini, kita dapat menggunakan dua algoritma - Standar dan Cepat. Untuk mengontrol waktu eksekusi, kita harus mengatur properti [Version](https://reference.aspose.com/pdf/id/net/aspose.pdf.optimization/imagecompressionoptions/properties/version). Cuplikan berikut menunjukkan algoritma Cepat:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FastShrinkImages()
{
    // Initialize Time
    var time = DateTime.Now.Ticks;

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Shrinkimage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // Set CompressImages option
        // If this flag is set to true images will be compressed in the document
        optimizeOptions.ImageCompressionOptions.CompressImages = true;

        // Set ImageQuality option
        // Specifies level of image compression when CompressImages flag is used
        optimizeOptions.ImageCompressionOptions.ImageQuality = 75;

        // Set Image Compression Version to fast
        // Version of compression algorithm. Possible values are:
        // 1. standard compression
        // 2. fast (improved compression which is faster then standard but may be applicable not for all images)
        // 3. mixed (standard compression is applied to images which can not be compressed by faster algorithm, 
        // this may give best compression but more slow then "fast" algorithm. Version "Fast" is not applicable for 
        // resizing images (standard method will be used). Default is "Standard"
        optimizeOptions.ImageCompressionOptions.Version = Aspose.Pdf.Optimization.ImageCompressionVersion.Fast;

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "FastShrinkImages_out.pdf");
    }

    // Output the time taken for the operation
    Console.WriteLine("Ticks: {0}", DateTime.Now.Ticks - time);
}
```

### Menghapus Objek yang Tidak Digunakan

Dokumen PDF terkadang mengandung objek PDF yang tidak dirujuk dari objek lain di dokumen. Ini dapat terjadi, misalnya, ketika sebuah halaman dihapus dari pohon halaman dokumen tetapi objek halaman itu sendiri tidak dihapus. Menghapus objek-objek ini tidak membuat dokumen menjadi tidak valid tetapi justru memperkecilnya.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizeDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set RemoveUsedObject option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            RemoveUnusedObjects = true
        };
        
        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

### Menghapus Aliran yang Tidak Digunakan

Terkadang dokumen mengandung aliran sumber daya yang tidak digunakan. Aliran ini bukan "objek yang tidak digunakan" karena mereka dirujuk dari kamus sumber daya halaman. Oleh karena itu, mereka tidak dihapus dengan metode "hapus objek yang tidak digunakan". Namun, aliran ini tidak pernah digunakan dengan konten halaman. Ini dapat terjadi dalam kasus ketika sebuah gambar telah dihapus dari halaman tetapi tidak dari sumber daya halaman. Selain itu, situasi ini sering terjadi ketika halaman diekstrak dari dokumen dan halaman dokumen memiliki sumber daya "umum", yaitu, objek Sumber Daya yang sama. Konten halaman dianalisis untuk menentukan apakah aliran sumber daya digunakan atau tidak. Aliran yang tidak digunakan dihapus. Ini terkadang mengurangi ukuran dokumen. Penggunaan teknik ini mirip dengan langkah sebelumnya:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set RemoveUsedStreams option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            RemoveUnusedStreams = true
        };

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

### Menghubungkan Aliran Duplikat

Beberapa dokumen dapat mengandung beberapa aliran sumber daya identik (seperti gambar, misalnya). Ini dapat terjadi, misalnya, ketika sebuah dokumen digabungkan dengan dirinya sendiri. Dokumen keluaran mengandung dua salinan independen dari aliran sumber daya yang sama. Kita menganalisis semua aliran sumber daya dan membandingkannya. Jika aliran tersebut duplikat, mereka digabungkan, yaitu, hanya satu salinan yang tersisa. Referensi diubah sesuai, dan salinan objek dihapus. Dalam beberapa kasus, ini membantu mengurangi ukuran dokumen.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocumentWithLinkDuplicateStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set LinkDuplicateStreams option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            LinkDuplicateStreams = true
        };

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

Selain itu, kita dapat menggunakan pengaturan [AllowReusePageContent](https://reference.aspose.com/pdf/id/net/aspose.pdf.optimization/optimizationoptions/properties/allowreusepagecontent). Jika properti ini diatur ke true, konten halaman akan digunakan kembali saat mengoptimalkan dokumen untuk halaman yang identik.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocumentWithReusePageContent()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set AllowReusePageContent option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            AllowReusePageContent = true
        };

        Console.WriteLine("Start");

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }

    Console.WriteLine("Finished");

    // Calculate and display file sizes
    var fi1 = new FileInfo(dataDir + "OptimizeDocument.pdf");
    var fi2 = new FileInfo(dataDir + "OptimizeDocument_out.pdf");
    Console.WriteLine("Original file size: {0}. Reduced file size: {1}", fi1.Length, fi2.Length);
}
```

### Melepaskan Font

Jika dokumen menggunakan font yang disematkan, itu berarti semua data font disimpan dalam dokumen. Keuntungannya adalah dokumen dapat dilihat terlepas dari apakah font diinstal di mesin pengguna atau tidak. Namun, menyematkan font membuat dokumen lebih besar. Metode melepaskan font menghapus semua font yang disematkan. Dengan demikian, ukuran dokumen berkurang tetapi dokumen itu sendiri mungkin menjadi tidak terbaca jika font yang benar tidak diinstal.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocumentWithUnembedFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set UnembedFonts option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            UnembedFonts = true
        };

        Console.WriteLine("Start");

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");	
    }
	
    Console.WriteLine("Finished");

    // Calculate and display file sizes
    var fi1 = new FileInfo(dataDir + "OptimizeDocument.pdf");
    var fi2 = new FileInfo(dataDir + "OptimizeDocument_out.pdf");
    Console.WriteLine("Original file size: {0}. Reduced file size: {1}", fi1.Length, fi2.Length);
}
```

Sumber daya optimasi menerapkan metode ini ke dokumen. Jika salah satu dari metode ini diterapkan, ukuran dokumen kemungkinan besar akan berkurang. Jika tidak ada dari metode ini yang diterapkan, ukuran dokumen tidak akan berubah yang jelas.

## Cara Tambahan untuk Mengurangi Ukuran Dokumen PDF

### Menghapus atau Meratakan Anotasi

Anotasi dapat dihapus ketika tidak diperlukan. Ketika mereka diperlukan tetapi tidak memerlukan pengeditan tambahan, mereka dapat diratakan. Kedua teknik ini akan mengurangi ukuran file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenAnnotationsInPdfDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Flatten annotations
        foreach (var page in document.Pages)
        {
            foreach (var annotation in page.Annotations)
            {
                annotation.Flatten();
            }
        }

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

### Menghapus Bidang Formulir

Jika dokumen PDF mengandung AcroForms, kita dapat mencoba mengurangi ukuran file dengan meratakan bidang formulir.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenPdfForms()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Load source PDF form
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Flatten Forms
        if (document.Form.Fields.Lenght > 0)
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

### Mengonversi PDF dari ruang warna RGB ke grayscale

File PDF terdiri dari Teks, Gambar, Lampiran, Anotasi, Grafik, dan objek lainnya. Anda mungkin menemui kebutuhan untuk mengonversi PDF dari ruang warna RGB ke grayscale sehingga lebih cepat saat mencetak file PDF tersebut. Selain itu, ketika file dikonversi ke grayscale, ukuran dokumen juga berkurang, tetapi ini juga dapat menyebabkan penurunan kualitas dokumen. Fitur ini saat ini didukung oleh fitur Pre-Flight dari Adobe Acrobat, tetapi ketika berbicara tentang otomatisasi Office, Aspose.PDF adalah solusi terbaik untuk memberikan keuntungan tersebut untuk manipulasi dokumen. Untuk memenuhi kebutuhan ini, cuplikan kode berikut dapat digunakan.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertRgbToGrayScale()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create RGB to DeviceGray conversion strategy
        var strategy = new Aspose.Pdf.RgbToDeviceGrayConversionStrategy();

        // Iterate through each page
        for (int idxPage = 1; idxPage <= document.Pages.Count; idxPage++)
        {
            // Get instance of particular page inside PDF
            var page = document.Pages[idxPage];

            // Convert the RGB colorspace image to GrayScale colorspace
            strategy.Convert(page);
        }

        // Save PDF document
        document.Save(dataDir + "TestGray_out.pdf");
    }
}
```

### Kompresi FlateDecode

{{% alert color="primary" %}}

Fitur ini didukung oleh versi 18.12 atau lebih tinggi.

{{% /alert %}}

Aspose.PDF for .NET menyediakan dukungan kompresi FlateDecode untuk fungsionalitas Optimasi PDF. Cuplikan kode berikut menunjukkan cara menggunakan opsi dalam Optimasi untuk menyimpan gambar dengan kompresi **FlateDecode**:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizeDocumentImagesWithFlateCompression()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizationOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // To optimize images using FlateDecode compression, set optimization options to Flate
        optimizationOptions.ImageCompressionOptions.Encoding = Aspose.Pdf.Optimization.ImageEncoding.Flate;

        // Set optimization options
        document.OptimizeResources(optimizationOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocumentImagesWithFlateCompression_out.pdf");
    }
}
```

### Simpan Gambar dalam XImageCollection

Aspose.PDF for .NET menyediakan kemampuan untuk menyimpan gambar baru ke dalam **XImageCollection** dengan kompresi FlateDecode. Untuk mengaktifkan opsi ini, Anda dapat menggunakan bendera **ImageFilterType.Flate**. Cuplikan kode berikut menunjukkan cara menggunakan fungsionalitas ini:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageToPdfWithFlateCompression()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Open the image file stream
        using (var imageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open))
        {
            // Add the image to the page resources with Flate compression
            page.Resources.Images.Add(imageStream, Aspose.Pdf.ImageFilterType.Flate);
        }

        // Get the added image
        var ximage = page.Resources.Images[page.Resources.Images.Count];

        // Save the current graphics state
        page.Contents.Add(new Aspose.Pdf.Operators.GSave());

        // Set coordinates for the image placement
        int lowerLeftX = 0;
        int lowerLeftY = 0;
        int upperRightX = 600;
        int upperRightY = 600;

        var rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        var matrix = new Aspose.Pdf.Matrix(new double[]
        {
            rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY
        });

        // Use ConcatenateMatrix operator to define how the image must be placed
        page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));
        page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));

        // Restore the graphics state
        page.Contents.Add(new Aspose.Pdf.Operators.GRestore());

        // Save the document
        document.Save(dataDir + "AddImageToPdfWithFlateCompression_out.pdf");
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