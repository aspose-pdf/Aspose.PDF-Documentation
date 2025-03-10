---
title: Memutar cap tentang titik pusat
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /id/net/rotating-stamp-about-the-center-point/
description: Bagian ini menjelaskan cara memutar cap tentang titik pusat menggunakan Kelas Cap.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Rotating stamp about the center point",
    "alternativeHeadline": "Rotate Stamps Precisely Around Their Center Point",
    "abstract": "Fitur dalam Aspose.PDF for .NET memungkinkan pengguna untuk memutar cap dalam file PDF secara tepat di sekitar titik pusatnya. Dengan memanfaatkan kelas Cap, pengembang dapat dengan mudah mengatur nilai rotasi dari 0 hingga 360 derajat, meningkatkan fleksibilitas dan kustomisasi penempatan watermark dalam dokumen. Fungsionalitas ini ideal untuk membuat PDF yang dinamis secara visual dengan orientasi cap yang dipersonalisasi.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "339",
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
    "url": "/net/rotating-stamp-about-the-center-point/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/rotating-stamp-about-the-center-point/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

{{% alert color="primary" %}}

[Namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) dalam [Aspose.PDF for .NET](/pdf/net/) memungkinkan Anda untuk menambahkan cap dalam file PDF yang ada. Terkadang, pengguna perlu memutar cap. Dalam artikel ini, kita akan melihat cara memutar cap tentang titik pusatnya.

{{% /alert %}}

## Detail implementasi

Kelas [Cap](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) memungkinkan Anda untuk menambahkan watermark dalam file PDF. Anda dapat menentukan gambar yang akan ditambahkan sebagai cap menggunakan metode [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.stamp/bindimage/methods/1). Metode [SetOrigin](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setorigin) memungkinkan Anda untuk mengatur asal dari cap yang ditambahkan; asal ini adalah koordinat kiri-bawah dari cap. Anda juga dapat mengatur ukuran gambar menggunakan metode [SetImageSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setimagesize).

Sekarang, kita melihat bagaimana cap dapat diputar tentang pusat cap. Kelas [Cap](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) menyediakan properti bernama Rotation. Properti ini mengatur atau mendapatkan rotasi dari 0 hingga 360 dari konten cap. Kita dapat menentukan nilai rotasi apa pun dari 0 hingga 360. Dengan menentukan nilai rotasi, kita dapat memutar cap tentang titik pusatnya. Jika sebuah Cap adalah objek dari tipe Cap maka nilai rotasi dapat ditentukan sebagai aStamp.Rotation = 90. Dalam hal ini, cap akan diputar pada 90 derajat di sekitar pusat konten cap. Potongan kode berikut menunjukkan kepada Anda bagaimana cara memutar cap tentang titik pusat:


```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRotatingStampToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();  

    // Create PdfFileInfo object to get height and width of the pages
    using (var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "RotatingStamp.pdf"))
    {
        // Create Stamp object
        var aStamp = new Aspose.Pdf.Facades.Stamp();

        // Bind image file with the Stamp object
        aStamp.BindImage(dataDir + "RotatingStamp.jpg");

        // Specify whether the stamp will be added as a background or not
        aStamp.IsBackground = false;

        // Specifies at which pages to add the watermark
        aStamp.Pages = new int[] { 1 };

        // Specifies the watermark rotation - rotate at 90 degrees
        aStamp.Rotation = 90;

        // Specifies the position of stamp - lower left corner of the stamp
        aStamp.SetOrigin(fileInfo.GetPageWidth(1) / 2, fileInfo.GetPageHeight(1) / 2);

        // Set the size of the watermark
        aStamp.SetImageSize(100, 100);

        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "RotatingStamp_out.pdf"))
        {
            // Create PdfFileStamp class to bind input and output files
            using (var stamper = new Aspose.Pdf.Facades.PdfFileStamp(document))
            {
                // Add the stamp in the PDF file
                stamper.AddStamp(aStamp);
            }
        }
    }
}
```