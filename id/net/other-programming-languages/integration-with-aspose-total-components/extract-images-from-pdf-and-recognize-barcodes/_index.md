---
title: Ekstrak Gambar dari PDF dan mengenali BarCode
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /id/net/extract-images-from-pdf-and-recognize-barcodes/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Images from PDF and recognize BarCodes",
    "alternativeHeadline": "Extract Images and Barcodes from PDF files in C#",
    "abstract": "Temukan cara untuk secara efisien mengekstrak gambar dari dokumen PDF dan mengenali barcode yang tertanam dengan akurat menggunakan Aspose.PDF for .NET. Fungsionalitas baru ini menyederhanakan proses identifikasi informasi barcode dengan memproses gambar yang diekstrak dari setiap halaman PDF, meningkatkan pengambilan dan pengelolaan data. Jelajahi langkah-langkah rinci dan implementasi kode untuk mengoptimalkan alur kerja penanganan dokumen Anda.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "317",
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
    "url": "/net/extract-images-from-pdf-and-recognize-barcodes/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-images-from-pdf-and-recognize-barcodes/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

{{% alert color="primary" %}}

Dokumen PDF biasanya terdiri dari Teks, Gambar, Tabel, Lampiran, Grafik, Anotasi, dan objek terkait lainnya. Ada kasus ketika Barcode tertanam di dalam file PDF dan beberapa pelanggan memiliki kebutuhan untuk mengidentifikasi Barcode yang ada di dalam file PDF. Artikel berikut menjelaskan langkah-langkah tentang cara mengekstrak gambar dari halaman PDF dan mengidentifikasi Barcode di dalamnya.

{{% /alert %}}

Menurut Model Objek Dokumen dari Aspose.PDF for .NET, file PDF berisi satu atau lebih halaman di mana setiap halaman berisi kumpulan Gambar, Formulir, dan Font dalam objek Sumber Daya. Jadi, untuk mengekstrak gambar dari file PDF, kita akan menjelajahi halaman-halaman individu dari file PDF, mendapatkan kumpulan Gambar dari halaman tertentu dan menyimpannya dalam objek MemoryStream untuk pemrosesan lebih lanjut dengan kelas BarCodeReader dari Aspose.BarCodeRecognition.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IdentifyBarcodes()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "IdentifyBarcodes.pdf"))
    {
        // Traverse through individual pages of PDF file
        for (int pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
        {
            // Traverse through each image extracted from PDF pages
            foreach (var xImage in document.Pages[pageCount].Resources.Images)
            {
                using (var imageStream = new MemoryStream())
                {
                    // Save PDF document image
                    xImage.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
        
                    // Set the stream position to the begining of Stream
                    imageStream.Position = 0;
        
                    // Instantiate BarCodeReader object
                    var barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);
        
                    while (barcodeReader.Read())
                    {
                        // Get BarCode text from BarCode image
                        var code = barcodeReader.GetCodeText();
        
                        // Write the BarCode text to Console output
                        Console.WriteLine("BARCODE : " + code);
                    }
        
                    // Close BarCodeReader object to release the Image file
                    barcodeReader.Close();
                }
            }
        }
    }
}
```

Untuk detail lebih lanjut tentang topik yang dibahas dalam artikel ini, kunjungi tautan berikut:

- [Ekstrak Gambar dari File PDF](/net/extract-images-from-the-pdf-file/)
- [Baca Barcodes](https://docs.aspose.com/barcode/net/barcode-recognition/)