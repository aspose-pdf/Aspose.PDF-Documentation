---
title: Mengonversi Halaman PDF ke Gambar dan Mengenali Kode Batang
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/convert-pdf-pages-to-images-and-recognize-barcodes/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF Pages to Images and Recognize Barcodes",
    "alternativeHeadline": "Convert PDF Pages to Images with Barcode Recognition in C#",
    "abstract": "Fitur baru ini memungkinkan konversi halaman PDF ke berbagai format gambar, memfasilitasi identifikasi kode batang yang tertanam menggunakan Aspose.Barcode untuk .NET. Fungsionalitas ini memperlancar pemrosesan dokumen dengan memungkinkan pengguna mengubah konten PDF menjadi gambar dan mengenali kode batang dengan akurat untuk penanganan data yang efisien.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "858",
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
    "url": "/net/convert-pdf-pages-to-images-and-recognize-barcodes/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-pages-to-images-and-recognize-barcodes/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

{{% alert color="primary" %}}

Dokumen PDF biasanya terdiri dari teks, gambar, tabel, lampiran, grafik, anotasi, dan objek lainnya. Beberapa pelanggan kami perlu menyematkan kode batang dalam dokumen dan kemudian mengidentifikasi kode batang dalam file PDF. Artikel berikut menjelaskan cara mengubah halaman dalam file PDF menjadi gambar dan mengidentifikasi kode batang dalam gambar dengan Aspose.Barcode untuk .NET.

{{% /alert %}}

## Mengonversi Halaman ke Gambar dan Mengenali Kode Batang

{{% alert color="primary" %}}

Aspose.PDF for .NET adalah produk yang sangat kuat untuk mengelola dokumen PDF. Ini memudahkan untuk mengonversi halaman dalam dokumen PDF menjadi gambar. Aspose.BarCode untuk .NET adalah produk yang sama kuatnya untuk menghasilkan dan mengenali kode batang.

Kelas PdfConverter di bawah namespace Aspose.Pdf.Facades mendukung konversi halaman PDF ke berbagai format gambar. PngDevice di bawah namespace Aspose.Pdf.Devices mendukung konversi halaman PDF ke file PNG. Salah satu dari kelas ini dapat digunakan untuk mengubah halaman file PDF menjadi gambar.

Ketika halaman telah dikonversi ke format gambar, kita dapat menggunakan Aspose.BarCode untuk .NET untuk mengidentifikasi kode batang di dalamnya. Contoh kode di bawah ini menunjukkan cara mengonversi halaman menggunakan PdfConverter atau PngDevice.

{{% /alert %}}

### Menggunakan Aspose.Pdf.Facades

{{% alert color="primary" %}}

Kelas PdfConverter memiliki metode bernama GetNextImage yang menghasilkan gambar dari halaman PDF saat ini. Untuk menentukan format gambar keluaran, metode ini menerima argumen dari enumerasi System.Drawing.Imaging.ImageFormat.

Aspose.Barcode memiliki namespace, BarCodeRecognition, yang berisi kelas BarCodeReader. Kelas BarCodeReader memungkinkan Anda membaca, menentukan, dan mengidentifikasi kode batang dari file gambar.

Untuk tujuan contoh ini, pertama-tama konversikan halaman dalam file PDF menjadi gambar dengan Aspose.Pdf.Facades.PdfConverter. Kemudian gunakan kelas Aspose.BarCodeRecognition.BarCodeReader untuk mengenali kode batang dalam gambar.

{{% /alert %}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IdentifyBarcodesConverter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Create a PdfConverter object
    var converter = new Aspose.Pdf.Facades.PdfConverter();

    // Bind PDF document
    converter.BindPdf(dataDir + "IdentifyBarcodes.pdf");

    // Specify the start page to be processed
    converter.StartPage = 1;

    // Specify the end page for processing
    converter.EndPage = 1;

    // Create a Resolution object to specify the resolution of resultant image
    converter.Resolution = new Aspose.Pdf.Devices.Resolution(300);

    // Initialize the convertion process
    converter.DoConvert();

    // Create a MemoryStream object to hold the resultant image
    using (var imageStream = new MemoryStream())
    {
        // Check if pages exist and then convert to image one by one
        while (converter.HasNextImage())
        {
            // Save the image in the given image Format
            converter.GetNextImage(imageStream, System.Drawing.Imaging.ImageFormat.Png);

            // Set the stream position to the beginning of the stream
            imageStream.Position = 0;

            // Instantiate a BarCodeReader object
            var barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

            // String txtResult.Text = "";
            while (barcodeReader.Read())
            {
                // Get the barcode text from the barcode image
                var code = barcodeReader.GetCodeText();

                // Write the barcode text to Console output
                Console.WriteLine("BARCODE : " + code);
            }

            // Close the BarCodeReader object to release the image file
            barcodeReader.Close();
        }

        // Close the PdfConverter instance and release the resources
        converter.Close();
    }
}
```

{{% alert color="primary" %}}

Dalam cuplikan kode di atas, gambar keluaran disimpan ke objek MemoryStream. Gambar juga dapat disimpan ke disk. Untuk melakukannya, ganti objek MemorStream dengan objek string yang mewakili jalur file ke metode GetNextImage kelas PdfConverter.

{{% /alert %}}

#### Menggunakan Kelas PngDevice

Di dalam Aspose.Pdf.Devices, terdapat PngDevice. Kelas ini memungkinkan Anda mengonversi halaman dalam dokumen PDF menjadi gambar PNG.

Untuk tujuan contoh ini, muat file PDF sumber ke dalam halaman dokumen dan ubah halaman tersebut menjadi gambar PNG. Ketika gambar telah dibuat, gunakan kelas BarCodeReader di bawah Aspose.BarCodeRecognition untuk mengidentifikasi dan membaca kode batang dalam gambar.

{{% alert color="primary" %}}

Contoh kode yang diberikan di sini menjelajahi halaman dokumen PDF dan mencoba mengidentifikasi kode batang di setiap halaman.

{{% /alert %}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IdentifyBarcodes()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "IdentifyBarcodes.pdf"))
    {
        // Traverse through the individual pages of the PDF file
        for (int pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
        {
            using (var imageStream = new MemoryStream())
            {
                // Create a Resolution object
                var resolution = new Aspose.Pdf.Devices.Resolution(300);

                // Instantiate a PngDevice object while passing a Resolution object as an argument to its constructor
                var pngDevice = new Aspose.Pdf.Devices.PngDevice(resolution);

                // Convert a particular page and save the image to stream
                pngDevice.Process(document.Pages[pageCount], imageStream);

                // Set the stream position to the beginning of Stream
                imageStream.Position = 0;

                // Instantiate a BarCodeReader object
                var barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

                // String txtResult.Text = "";
                while (barcodeReader.Read())
                {
                    // Get the barcode text from the barcode image
                    var code = barcodeReader.GetCodeText();

                    // Write the barcode text to Console output
                    Console.WriteLine("BARCODE : " + code);
                }

                // Close the BarCodeReader object to release the image file
                barcodeReader.Close();
            }
        }
    }
}
```

{{% alert color="primary" %}}

Untuk informasi lebih lanjut tentang topik yang dibahas dalam artikel ini, kunjungi:

- Mengonversi Halaman PDF ke Format Gambar yang Berbeda (Facades)
- Mengonversi semua halaman PDF ke Gambar PNG
- [Baca Kode Batang](https://docs.aspose.com/barcode/net/barcode-recognition/)

{{% /alert %}}