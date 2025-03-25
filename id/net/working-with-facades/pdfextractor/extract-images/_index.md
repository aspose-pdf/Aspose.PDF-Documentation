---
title: Ekstrak Gambar menggunakan PdfExtractor
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /id/net/extract-images/
description: Bagian ini menjelaskan cara mengekstrak gambar dengan Aspose.PDF Facades menggunakan Kelas PdfExtractor.
lastmod: "2021-07-15"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Images using PdfExtractor",
    "alternativeHeadline": "Extract Images from PDF with PdfExtractor Class",
    "abstract": "Fitur PdfExtractor dari Aspose.PDF memungkinkan pengguna untuk mengekstrak gambar dari dokumen PDF secara efisien, menawarkan beberapa opsi seperti mengekstrak gambar dari seluruh dokumen, halaman tertentu, atau rentang yang ditentukan. Ini mendukung penyimpanan gambar langsung ke file atau aliran memori, meningkatkan fleksibilitas bagi pengembang yang bekerja dengan aset PDF. Fungsionalitas yang kuat ini memungkinkan kontrol yang tepat atas mode ekstraksi gambar, membuatnya lebih mudah untuk menangani berbagai jenis konten PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1789",
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
    "url": "/net/extract-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-images/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Ekstrak Gambar dari Seluruh PDF ke File (Facades)

[Kelas PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) memungkinkan Anda untuk mengekstrak gambar dari file PDF. Pertama-tama, Anda perlu membuat objek dari [Kelas PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Setelah itu, panggil metode [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) untuk mengekstrak semua gambar ke dalam memori. Setelah gambar diekstrak, Anda dapat mendapatkan gambar tersebut dengan bantuan metode [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) dan [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Anda perlu melakukan loop melalui semua gambar yang diekstrak menggunakan loop while. Untuk menyimpan gambar ke disk, Anda dapat memanggil overload dari metode [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) yang mengambil jalur file sebagai argumen. Potongan kode berikut menunjukkan cara mengekstrak gambar dari seluruh PDF ke file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesWholePDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Extract all the images
        extractor.ExtractImage();

        // Get all the extracted images
        while (extractor.HasNextImage())
        {
            extractor.GetNextImage(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg");
        }
    }
}
```

## Ekstrak Gambar dari Seluruh PDF ke Aliran (Facades)

[Kelas PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) memungkinkan Anda untuk mengekstrak gambar dari file PDF ke dalam aliran. Pertama-tama, Anda perlu membuat objek dari [Kelas PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Setelah itu, panggil metode [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) untuk mengekstrak semua gambar ke dalam memori. Setelah gambar diekstrak, Anda dapat mendapatkan gambar tersebut dengan bantuan metode [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) dan [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Anda perlu melakukan loop melalui semua gambar yang diekstrak menggunakan loop while. Untuk menyimpan gambar ke aliran, Anda dapat memanggil overload dari metode [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) yang mengambil Stream sebagai argumen. Potongan kode berikut menunjukkan cara mengekstrak gambar dari seluruh PDF ke aliran.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesWholePDFStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Extract images
        extractor.ExtractImage();
        // Get all the extracted images
        while (extractor.HasNextImage())
        {
            // Read image into memory stream
            MemoryStream memoryStream = new MemoryStream();
            extractor.GetNextImage(memoryStream);

            // Write to disk, if you like, or use it otherwise
            using (FileStream fileStream = new FileStream(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create))
            {
                memoryStream.WriteTo(fileStream);
            }
        }
    }
}
```

## Ekstrak Gambar dari Halaman Tertentu dari PDF (Facades)

Anda dapat mengekstrak gambar dari halaman tertentu dari file PDF. Untuk melakukan itu, Anda perlu mengatur properti [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) dan [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) ke halaman tertentu yang ingin Anda ekstrak gambarnya. Pertama-tama, Anda perlu membuat objek dari [Kelas PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Kedua, Anda harus mengatur properti [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) dan [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage). Setelah itu, panggil metode [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) untuk mengekstrak semua gambar ke dalam memori. Setelah gambar diekstrak, Anda dapat mendapatkan gambar tersebut dengan bantuan metode [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) dan [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Anda perlu melakukan loop melalui semua gambar yang diekstrak menggunakan loop while. Anda dapat menyimpan gambar ke disk atau aliran. Anda hanya perlu memanggil overload yang sesuai dari metode [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Potongan kode berikut menunjukkan cara mengekstrak gambar dari halaman tertentu dari PDF ke aliran.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesParticularPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Set StartPage and EndPage properties to the page number to
        // You want to extract images from
        extractor.StartPage = 2;
        extractor.EndPage = 2;

        // Extract images
        extractor.ExtractImage();
        // Get extracted images
        while (extractor.HasNextImage())
        {
            // Read image into memory stream
            MemoryStream memoryStream = new MemoryStream();
            extractor.GetNextImage(memoryStream);

            // Write to disk, if you like, or use it otherwise
            using (FileStream fileStream = new FileStream(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create))
            {
                memoryStream.WriteTo(fileStream);
            }
        }
    }
}
```

## Ekstrak Gambar dari Rentang Halaman dari PDF (Facades)

Anda dapat mengekstrak gambar dari rentang halaman dari file PDF. Untuk melakukan itu, Anda perlu mengatur properti [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) dan [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) ke rentang halaman yang ingin Anda ekstrak gambarnya. Pertama-tama, Anda perlu membuat objek dari [Kelas PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Kedua, Anda harus mengatur properti [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) dan [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage). Setelah itu, panggil metode [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) untuk mengekstrak semua gambar ke dalam memori. Setelah gambar diekstrak, Anda dapat mendapatkan gambar tersebut dengan bantuan metode [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) dan [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Anda perlu melakukan loop melalui semua gambar yang diekstrak menggunakan loop while. Anda dapat menyimpan gambar ke disk atau aliran. Anda hanya perlu memanggil overload yang sesuai dari metode [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Potongan kode berikut menunjukkan cara mengekstrak gambar dari rentang halaman PDF ke aliran.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesRangePages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open input PDF
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Set StartPage and EndPage properties to the page number to
        // You want to extract images from
        extractor.StartPage = 2;
        extractor.EndPage = 2;

        // Extract images
        extractor.ExtractImage();

        // Get extracted images
        while (extractor.HasNextImage())
        {
            // Read image into memory stream
            MemoryStream memoryStream = new MemoryStream();
            extractor.GetNextImage(memoryStream);

            // Write to disk, if you like, or use it otherwise
            using (FileStream fileStream = new
            FileStream(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create))
            {
                memoryStream.WriteTo(fileStream);
            }
        }
    }
}
```

## Ekstrak Gambar menggunakan Mode Ekstraksi Gambar (Facades)

[Kelas PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) memungkinkan Anda untuk mengekstrak gambar dari file PDF. Aspose.PDF mendukung dua mode ekstraksi; yang pertama adalah ActuallyUsedImage yang mengekstrak gambar yang sebenarnya digunakan dalam dokumen PDF. Mode kedua adalah [DefinedInResources](https://reference.aspose.com/pdf/net/aspose.pdf/extractimagemode) yang mengekstrak gambar yang didefinisikan dalam sumber daya dokumen PDF (mode ekstraksi default). Pertama, Anda perlu membuat objek dari [Kelas PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Setelah itu, tentukan mode ekstraksi gambar menggunakan properti [PdfExtractor.ExtractImageMode](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/extractimagemode). Kemudian panggil metode [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) untuk mengekstrak semua gambar ke dalam memori tergantung pada mode yang Anda tentukan. Setelah gambar diekstrak, Anda dapat mendapatkan gambar tersebut dengan bantuan metode [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) dan [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Anda perlu melakukan loop melalui semua gambar yang diekstrak menggunakan loop while. Untuk menyimpan gambar ke disk, Anda dapat memanggil overload dari metode [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) yang mengambil jalur file sebagai argumen.

Potongan kode berikut menunjukkan cara mengekstrak gambar dari file PDF menggunakan opsi ExtractImageMode.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesImageExtractionMode()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Specify Image Extraction Mode
        //extractor.ExtractImageMode = ExtractImageMode.ActuallyUsed;
        extractor.ExtractImageMode = Aspose.Pdf.ExtractImageMode.DefinedInResources;

        // Extract Images based on Image Extraction Mode
        extractor.ExtractImage();

        // Get all the extracted images
        while (extractor.HasNextImage())
        {
            extractor.GetNextImage(dataDir + DateTime.Now.Ticks.ToString() + "_out.png", System.Drawing.Imaging.ImageFormat.Png);
        }
    }
}
```

Untuk memeriksa apakah PDF berisi Teks atau Gambar, gunakan potongan kode berikut:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckIfPdfContainsTextOrImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Instantiate a memoryStream object to hold the extracted text from Document
    MemoryStream ms = new MemoryStream();
    // Instantiate PdfExtractor object
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "FilledForm.pdf");
        // Extract text from the input PDF document
        extractor.ExtractText();
        // Save the extracted text to a text file
        extractor.GetText(ms);
        // Check if the MemoryStream length is greater than or equal to 1

        bool containsText = ms.Length >= 1;

        // Extract images from the input PDF document
        extractor.ExtractImage();

        // Calling HasNextImage method in while loop. When images will finish, loop will exit
        bool containsImage = extractor.HasNextImage();

        // Now find out whether this PDF is text only or image only

        if (containsText && !containsImage)
        {
            Console.WriteLine("PDF contains text only");
        }
        else if (!containsText && containsImage)
        {
            Console.WriteLine("PDF contains image only");
        }
        else if (containsText && containsImage)
        {
            Console.WriteLine("PDF contains both text and image");
        }
        else if (!containsText && !containsImage)
        {
            Console.WriteLine("PDF contains neither text or nor image");
        }
    }
}
```