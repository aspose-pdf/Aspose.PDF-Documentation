---
title: Enkripsi File PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/encrypt-pdf-file/
description: Topik ini menjelaskan cara Enkripsi File PDF menggunakan Kelas PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Encrypt PDF File",
    "alternativeHeadline": "Secure PDF Encryption with C#",
    "abstract": "Temukan cara untuk meningkatkan keamanan dokumen sensitif Anda dengan fitur enkripsi PDF baru menggunakan Kelas PdfFileSecurity. Fungsionalitas ini memungkinkan Anda untuk melindungi file PDF Anda dengan kata sandi, memastikan bahwa hanya pengguna yang berwenang yang dapat mengaksesnya. Jelajahi berbagai jenis dan algoritma enkripsi, termasuk AES dengan panjang kunci hingga 256 bit, untuk perlindungan yang kuat selama berbagi dan pengarsipan file.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "273",
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
    "url": "/net/encrypt-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/encrypt-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

Mengenkripsi dokumen PDF melindungi isinya dari akses tidak sah dari luar, terutama selama berbagi atau pengarsipan file.

Dokumen PDF yang bersifat rahasia dapat dienkripsi dan dilindungi dengan kata sandi. Hanya pengguna yang mengetahui kata sandi yang akan dapat mendekripsi, membuka, dan melihat dokumen ini.

Mari kita lihat bagaimana enkripsi PDF bekerja dengan pustaka Aspose.PDF.

## Enkripsi File PDF menggunakan Berbagai Jenis dan Algoritma Enkripsi

Untuk mengenkripsi file PDF, Anda perlu membuat objek [PdfFileSecurity](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffilesecurity) dan kemudian memanggil metode [EncryptFile](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile). Anda dapat melewatkan kata sandi pengguna, kata sandi pemilik, dan hak istimewa ke metode [EncryptFile](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile). Anda juga perlu melewatkan nilai KeySize dan Algorithm ke metode ini.

Tinjau daftar kemungkinan dari [CryptoAlgorithm](https://reference.aspose.com/pdf/id/net/aspose.pdf/cryptoalgorithm):

|**Nama Anggota**|**Nilai**|**Deskripsi**|
| :- | :- | :- |
|RC4x40|0|RC4 dengan panjang kunci 40.|
|RC4x128|1|RC4 dengan panjang kunci 128.|
|AESx128|2|AES dengan panjang kunci 128.|
|AESx256|3|AES dengan panjang kunci 256.|

Cuplikan kode berikut menunjukkan kepada Anda cara mengenkripsi file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EncryptPDFFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "input.pdf");
        // Encrypt file using 256-bit encryption
        fileSecurity.EncryptFile("User_P@ssw0rd", "OwnerP@ssw0rd", Aspose.Pdf.Facades.DocumentPrivilege.Print, Aspose.Pdf.Facades.KeySize.x256,
            Aspose.Pdf.Facades.Algorithm.AES);
        // Save PDF document
        fileSecurity.Save(dataDir + "SampleEncrypted_out.pdf");
    }
}
```