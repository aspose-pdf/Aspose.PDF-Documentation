---
title: Menambahkan Gambar dan Teks
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/adding-images-and-text-using-pdffilemend-class/
description: Bagian ini menjelaskan cara Menambahkan Gambar dan Teks menggunakan kelas PdfFileMend.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding Images and Text",
    "alternativeHeadline": "Enhance PDF by Adding Images and Text Precisely",
    "abstract": "Tingkatkan dokumen PDF Anda dengan mudah menggunakan kelas PdfFileMend yang baru, yang memungkinkan Anda menambahkan gambar dan teks di lokasi tertentu dalam PDF yang ada. Manfaatkan metode AddImage dan AddText yang intuitif untuk mengintegrasikan berbagai format gambar dan teks terformat dengan mulus, memastikan ketepatan dalam penempatan dan pemilihan halaman. Permudah tugas manipulasi PDF Anda dengan kemampuan untuk menyesuaikan overlay gambar dan pembungkusan teks, menjadikan dokumen Anda menarik secara visual dan informatif.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1324",
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
    "url": "/net/adding-images-and-text-using-pdffilemend-class/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/adding-images-and-text-using-pdffilemend-class/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

[Kelas PdfFileMend](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffilemend) dapat membantu Anda menambahkan gambar dan teks dalam dokumen PDF yang ada, di lokasi yang ditentukan. Ini menyediakan dua metode dengan nama [AddImage](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) dan [AddText](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffilemend/methods/addtext/index). Metode [AddImage](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) memungkinkan Anda menambahkan gambar dengan tipe JPG, GIF, PNG, dan BMP. Metode [AddText](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffilemend/methods/addtext/index) mengambil argumen dari kelas [FormattedText](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formattedtext) dan menambahkannya ke dalam file PDF yang ada. Gambar dan teks dapat ditambahkan dalam wilayah persegi panjang yang ditentukan oleh koordinat titik kiri bawah dan kanan atas. Saat menambahkan gambar, Anda dapat menentukan baik jalur file gambar atau aliran file gambar. Untuk menentukan nomor halaman di mana gambar atau teks perlu ditambahkan, kedua metode ini menyediakan argumen nomor halaman. Jadi, Anda tidak hanya dapat menambahkan gambar dan teks di lokasi yang ditentukan tetapi juga di halaman yang ditentukan.

Gambar adalah bagian penting dari konten dokumen PDF. Memanipulasi gambar dalam file PDF yang ada adalah kebutuhan umum bagi orang-orang yang bekerja dengan file PDF. Dalam artikel ini, kita akan menjelajahi bagaimana gambar dapat dimanipulasi, dalam file PDF yang ada, dengan bantuan [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades) dari [Aspose.PDF for .NET](/pdf/id/net/). Semua operasi terkait gambar dari [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades) telah dikonsolidasikan dalam artikel ini.

## Detail Implementasi

[Namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades) memungkinkan Anda menambahkan gambar baru dalam file PDF yang ada. Anda juga dapat mengganti atau menghapus gambar yang ada. File PDF juga dapat dikonversi menjadi gambar. Anda dapat mengonversi setiap halaman individu menjadi satu gambar atau seluruh file PDF menjadi satu gambar. Ini memungkinkan Anda menggunakan format seperti JPEG, BMP, PNG, dan TIFF, dll. Anda juga dapat mengekstrak gambar dari file PDF. Anda dapat menggunakan empat kelas dari [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades) untuk menerapkan operasi ini, yaitu [PdfFileMend](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffilemend), [PdfContentEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfcontenteditor), [PdfExtractor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfextractor), dan [PdfConverter](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfconverter).

## Operasi Gambar

Dalam bagian ini, kita akan melihat lebih dalam tentang operasi gambar ini. Kita juga akan melihat potongan kode untuk menunjukkan penggunaan kelas dan metode terkait. Pertama-tama, mari kita lihat cara menambahkan gambar dalam file PDF yang ada. Kita dapat menggunakan metode [AddImage](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) dari kelas [PdfFileMend](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffilemend) untuk menambahkan gambar baru. Menggunakan metode ini, Anda tidak hanya dapat menentukan nomor halaman di mana Anda ingin menambahkan gambar, tetapi juga lokasi gambar dapat ditentukan.

## Tambahkan Gambar dalam File PDF yang Ada (Facades)

Anda dapat menggunakan metode [AddImage](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffilemend/methods/addimage) dari kelas [PdfFileMend](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffilemend). Metode [AddImage](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffilemend/methods/addimage) memerlukan gambar yang akan ditambahkan, nomor halaman di mana gambar perlu ditambahkan, dan informasi koordinat. Setelah itu, simpan file PDF yang diperbarui menggunakan metode [Close](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfcontenteditor/methods/close).

Dalam contoh berikut, kita menambahkan gambar ke halaman menggunakan imageStream:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImage01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images(); 

    // Create PDF document and PdfFileMend objects
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Load image into stream
            using (var imageStream = File.OpenRead(dataDir + "AddImage.png"))
            {
                // Bind PDF document
                mender.BindPdf(document);

                // Add image to first page
                mender.AddImage(imageStream, 1, 10, 650, 110, 750);

                // Save PDF document
                mender.Save(dataDir + "AddImage_out.pdf");
            }
        }
    }
}
```

![Tambahkan Gambar](/pdf/id/net/images/add_image1.png)

Dengan bantuan [CompositingParameters](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.pdffilemend/addimage/methods/1), kita dapat menumpuk satu gambar di atas gambar lainnya:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImage02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document and PdfFileMend objects
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Load image into stream
            using (var imageStream = File.OpenRead(dataDir + "AddImage.png"))
            {
                // Bind PDF document
                mender.BindPdf(document);

                int pageNum = 1;
                int lowerLeftX = 10;
                int lowerLeftY = 650;
                int upperRightX = 110;
                int upperRightY = 750;

                // Use compositing parameters for the image
                var compositingParameters = new Aspose.Pdf.CompositingParameters(Aspose.Pdf.BlendMode.Multiply);

                mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

                // Save PDF document
                mender.Save(dataDir + "AddImage_out.pdf");
            }
        }
    }
}
```

![Tambahkan Gambar](/pdf/id/net/images/add_image2.png)

Ada beberapa cara untuk menyimpan gambar dalam file PDF. Kami akan mendemonstrasikan salah satunya dalam contoh berikut:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImage03()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Load image into stream
            using (var imageStream = File.OpenRead(dataDir + "AddImage.png"))
            {
                // Bind PDF document
                mender.BindPdf(document);

                int pageNum = 1;
                int lowerLeftX = 10;
                int lowerLeftY = 650;
                int upperRightX = 110;
                int upperRightY = 750;

                // Use compositing parameters with BlendMode.Exclusion and ImageFilterType.Flate
                var compositingParameters = new Aspose.Pdf.CompositingParameters(
                    Aspose.Pdf.BlendMode.Exclusion,
                    Aspose.Pdf.ImageFilterType.Flate);

                mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

                // Save PDF document
                mender.Save(dataDir + "AddImage_out.pdf");
            }
        }
    }
}
```

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImage04()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Load image into stream
            using (var imageStream = File.OpenRead(dataDir + "AddImage.png"))
            {
                // Bind PDF document
                mender.BindPdf(document);

                int pageNum = 1;
                int lowerLeftX = 10;
                int lowerLeftY = 650;
                int upperRightX = 110;
                int upperRightY = 750;

                // Use compositing parameters with BlendMode.Multiply, ImageFilterType.Flate and false
                var compositingParameters = new Aspose.Pdf.CompositingParameters(
                    Aspose.Pdf.BlendMode.Multiply,
                    Aspose.Pdf.ImageFilterType.Flate,
                    false);

                mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

                // Save PDF document
                mender.Save(dataDir + "AddImage_outp.pdf");
            }
        }
    }
}
```

## Tambahkan Teks dalam File PDF yang Ada (facades)

Kita dapat menambahkan teks dengan beberapa cara. Pertimbangkan yang pertama. Kita mengambil [FormattedText](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formattedtext) dan menambahkannya ke Halaman. Setelah itu, kita menunjukkan koordinat sudut kiri bawah, dan kemudian kita menambahkan teks kita ke Halaman.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddText01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileMend object
    using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
    {
        // Bind PDF document
        mender.BindPdf(dataDir + "AddImage.pdf");

        // Create formatted text
        var message = new Aspose.Pdf.Facades.FormattedText("Welcome to Aspose!");

        // Add text to the first page at position (10, 750)
        mender.AddText(message, 1, 10, 750);

        // Save PDF document
        mender.Save(dataDir + "AddText_out.pdf");
    }
}
```

Periksa bagaimana tampilannya:

![Tambahkan Teks](/pdf/id/net/images/add_text.png)

Cara kedua untuk menambahkan [FormattedText](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formattedtext). Selain itu, kita menunjukkan sebuah persegi panjang di mana teks kita harus muat.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddText02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileMend object
    using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
    {
        // Bind PDF document
        mender.BindPdf(dataDir + "AddImage.pdf");

        // Create formatted text
        var message = new Aspose.Pdf.Facades.FormattedText("Welcome to Aspose! Welcome to Aspose!");

        // Add text to the first page at the specified position with wrapping
        mender.AddText(message, 1, 10, 700, 55, 810);

        // Set word wrapping mode to wrap by words
        mender.WrapMode = Aspose.Pdf.Facades.WordWrapMode.ByWords;

        // Save PDF document
        mender.Save(dataDir + "AddText_out.pdf");
    }
}
```

Contoh ketiga memberikan kemampuan untuk Menambahkan Teks ke halaman yang ditentukan. Dalam contoh kita, mari kita tambahkan keterangan di halaman 1 dan 3 dari dokumen.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddText03()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        document.Pages.Add();
        document.Pages.Add();
        document.Pages.Add();

        // Create PdfFileMend object
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Bind PDF document
            mender.BindPdf(document);

            // Create formatted text
            var message = new Aspose.Pdf.Facades.FormattedText("Welcome to Aspose!");

            // Specify the pages where text should be added
            int[] pageNums = new int[] { 1, 3 };

            // Add text to the specified pages at the specified coordinates
            mender.AddText(message, pageNums, 10, 750, 310, 760);

            // Save PDF document
            mender.Save(dataDir + "AddText_out.pdf");
        }
    }
}
```