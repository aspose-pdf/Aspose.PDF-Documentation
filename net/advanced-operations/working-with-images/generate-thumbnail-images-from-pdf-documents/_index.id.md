---
title: Membuat Gambar Thumbnail dari PDF
linktitle: Membuat Gambar Thumbnail
type: docs
weight: 110
url: /net/generate-thumbnail-images-from-pdf-documents/
description: Bagian ini menjelaskan cara membuat gambar thumbnail dari dokumen PDF
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Membuat Gambar Thumbnail dari PDF",
    "alternativeHeadline": "Cara membuat Gambar Thumbnail dari file PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, membuat gambar thumbnail",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/generate-thumbnail-images-from-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/generate-thumbnail-images-from-pdf-documents/"
    },
    "dateModified": "2022-02-04",
    "description": "Bagian ini menjelaskan cara membuat gambar thumbnail dari dokumen PDF"
}
</script>
{{% alert color="primary" %}}

Adobe Acrobat SDK adalah seperangkat alat yang membantu Anda mengembangkan perangkat lunak yang berinteraksi dengan teknologi Acrobat. SDK ini berisi file header, pustaka tipe, utilitas sederhana, contoh kode, dan dokumentasi.

Dengan menggunakan Acrobat SDK, Anda dapat mengembangkan perangkat lunak yang terintegrasi dengan Acrobat dan Adobe Reader dengan beberapa cara:

- **JavaScript** — Menulis skrip, baik dalam dokumen PDF individu atau secara eksternal, untuk memperluas fungsionalitas Acrobat atau Adobe Reader.
- **Plug-ins** — Membuat plug-in yang terhubung secara dinamis dan memperluas fungsionalitas Acrobat atau Adobe Reader.
- **Komunikasi antaraplikasi** — Menulis proses aplikasi terpisah yang menggunakan komunikasi antaraplikasi (IAC) untuk mengontrol fungsionalitas Acrobat. DDE dan OLE didukung di Microsoft® Windows®, dan acara Apple/AppleScript di Mac OS®. IAC tidak tersedia di UNIX®.

Aspose.PDF untuk .NET menyediakan banyak fungsi yang sama, membebaskan Anda dari ketergantungan pada Otomasi Adobe Acrobat.
Aspose.PDF untuk .NET menyediakan banyak fungsi yang sama, membebaskan Anda dari ketergantungan pada Otomasi Adobe Acrobat.

{{% /alert %}}

## Mengembangkan Aplikasi menggunakan API Komunikasi Antar Aplikasi Acrobat

Bayangkan API Acrobat memiliki dua lapisan yang menggunakan objek Komunikasi Antar Aplikasi (IAC) Acrobat:

- Lapisan aplikasi Acrobat (AV). Lapisan AV memungkinkan Anda mengontrol bagaimana dokumen ditampilkan. Sebagai contoh, tampilan dari objek dokumen berada di lapisan yang terkait dengan Acrobat.
- Lapisan dokumen portabel (PD). Lapisan PD memberikan akses ke informasi di dalam dokumen, seperti halaman. Dari lapisan PD Anda dapat melakukan manipulasi dasar dokumen PDF, seperti menghapus, memindahkan, atau mengganti halaman, serta mengubah atribut anotasi. Anda juga dapat mencetak halaman PDF, memilih teks, mengakses teks yang dimanipulasi, dan membuat atau menghapus thumbnail.

Karena tujuan kami adalah mengonversi halaman PDF menjadi gambar thumbnail, jadi kami lebih fokus pada IAC.
### Pendekatan Acrobat

Untuk menghasilkan gambar thumbnail untuk setiap dokumen, kami telah menggunakan Adobe Acrobat 7.0 SDK dan Microsoft .NET 2.0 Framework.

[Acrobat SDK](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/) dikombinasikan dengan versi penuh Adobe Acrobat menghadirkan perpustakaan objek COM (sayangnya Adobe Reader gratis tidak mengekspos antarmuka COM) yang dapat digunakan untuk memanipulasi dan mengakses informasi PDF. Menggunakan objek COM ini melalui COM Interop, muat dokumen PDF, dapatkan halaman pertama dan render halaman tersebut ke clipboard. Kemudian, dengan .NET Framework, salin ini ke bitmap, skalakan dan gabungkan gambar tersebut dan simpan hasilnya sebagai file GIF atau PNG.

Setelah Adobe Acrobat terinstal, gunakan regedit.exe dan lihat di bawah HKEY_CLASSES_ROOT untuk entri yang disebut AcroExch.PDDoc.

**Registri yang menunjukkan entri AcroExch.PDDDoc**

![todo:image_alt_text](generate-thumbnail-images-from-pdf-documents_1.png)
![todo:image_alt_text](generate-thumbnail-images-from-pdf-documents_1.png)

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-CreateThumbnailImagesUsingAdobe-CreateThumbnailImagesUsingAdobe.cs" >}}

## Pendekatan Aspose.PDF untuk .NET

Aspose.PDF untuk .NET menyediakan dukungan luas dalam menangani dokumen PDF. Ini juga mendukung kemampuan untuk mengonversi halaman dokumen PDF ke berbagai format gambar. Fungsionalitas yang dijelaskan di atas dapat dengan mudah dicapai menggunakan Aspose.PDF untuk .NET.

Aspose.PDF memiliki beberapa keuntungan:

- Anda tidak perlu memiliki Adobe Acrobat terinstal di sistem Anda untuk bekerja dengan file PDF.
- Menggunakan Aspose.PDF untuk .NET itu sederhana dan mudah dipahami dibandingkan dengan Otomatisasi Acrobat.

Jika kita perlu mengonversi halaman PDF menjadi JPEG, namespace [Aspose.PDF.Devices](https://reference.aspose.com/pdf/net/aspose.pdf.devices) menyediakan kelas yang bernama [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice) untuk merender halaman PDF menjadi gambar JPEG.
Jika kita perlu mengonversi halaman PDF menjadi JPEG, ruang nama [Aspose.PDF.Devices](https://reference.aspose.com/pdf/net/aspose.pdf.devices) menyediakan kelas bernama [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice) untuk merender halaman PDF menjadi gambar JPEG.

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-CreateThumbnailImages-CreateThumbnailImages.cs" >}}

{{% alert color="primary" %}}

- Terima kasih kepada CodeProject untuk [Generate Thumbnail Image from PDF document](https://www.codeproject.com/Articles/5887/Generate-Thumbnail-Images-from-PDF-Documents).
- Terima kasih kepada Acrobat untuk [Acrobat SDK reference](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/documentation.html).

{{% /alert %}}

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
Sure, I will help translate the document to Bahasa Indonesia while maintaining the markdown formatting and adhering to the specific instructions provided. Please share the content of the document that you need to be translated.
