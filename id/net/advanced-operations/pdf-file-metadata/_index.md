---
title: Bekerja dengan Metadata File PDF | C#
linktitle: Metadata File PDF
type: docs
weight: 140
url: /id/net/pdf-file-metadata/
description: Bagian ini menjelaskan cara mendapatkan informasi file PDF, cara mendapatkan Metadata XMP dari file PDF, mengatur Informasi File PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Bekerja dengan Metadata File PDF | C#",
    "alternativeHeadline": "Cara Mendapatkan Metadata File PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, metadata file pdf",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dok Aspose.PDF",
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
                "contactType": "penjualan",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "penjualan",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "penjualan",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/pdf-file-metadata/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-file-metadata/"
    },
    "dateModified": "2022-02-04",
    "description": "Bagian ini menjelaskan cara mendapatkan informasi file PDF, cara mendapatkan Metadata XMP dari file PDF, mengatur Informasi File PDF."
}
</script>
Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## Dapatkan Informasi File PDF

Untuk mendapatkan informasi spesifik file dari file PDF, Anda pertama-tama perlu mendapatkan objek [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo) menggunakan properti [Info](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/info) dari objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Setelah objek [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo) diambil, Anda dapat mendapatkan nilai dari properti individu. Potongan kode berikut menunjukkan cara mendapatkan informasi file PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "GetFileInfo.pdf");
// Dapatkan informasi dokumen
DocumentInfo docInfo = pdfDocument.Info;
// Tampilkan informasi dokumen
Console.WriteLine("Author: {0}", docInfo.Author);
Console.WriteLine("Creation Date: {0}", docInfo.CreationDate);
Console.WriteLine("Keywords: {0}", docInfo.Keywords);
Console.WriteLine("Modify Date: {0}", docInfo.ModDate);
Console.WriteLine("Subject: {0}", docInfo.Subject);
Console.WriteLine("Title: {0}", docInfo.Title);
```
## Menetapkan Informasi Berkas PDF

Aspose.PDF untuk .NET memungkinkan Anda untuk menetapkan informasi spesifik berkas untuk PDF, informasi seperti penulis, tanggal pembuatan, subjek, dan judul. Untuk menetapkan informasi ini:

1. Buat objek [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo).
1. Tetapkan nilai dari properti.
1. Simpan dokumen yang telah diperbarui menggunakan metode Save dari kelas Dokumen.

{{% alert color="primary" %}}

Harap dicatat bahwa Anda tidak dapat menetapkan nilai terhadap bidang *Application* dan *Producer*, karena Aspose Ltd. dan Aspose.PDF untuk .NET x.x.x akan ditampilkan di bidang ini.

{{% /alert %}}

Potongan kode berikut menunjukkan cara menetapkan informasi berkas PDF.

```csharp
// Untuk contoh lengkap dan berkas data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "SetFileInfo.pdf");

// Tentukan informasi dokumen
DocumentInfo docInfo = new DocumentInfo(pdfDocument);

docInfo.Author = "Aspose";
docInfo.CreationDate = DateTime.Now;
docInfo.Keywords = "Aspose.Pdf, DOM, API";
docInfo.ModDate = DateTime.Now;
docInfo.Subject = "Informasi PDF";
docInfo.Title = "Menetapkan Informasi Dokumen PDF";

dataDir = dataDir + "SetFileInfo_out.pdf";
// Simpan dokumen keluaran
pdfDocument.Save(dataDir);
```
## Mendapatkan Metadata XMP dari File PDF

Aspose.PDF memungkinkan Anda untuk mengakses metadata XMP dari file PDF. Untuk mendapatkan metadata file PDF:

1. Buat objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) dan buka file PDF yang diinginkan.
1. Dapatkan metadata file tersebut menggunakan properti [Metadata](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/metadata).

Potongan kode berikut menunjukkan cara mendapatkan metadata dari file PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "GetXMPMetadata.pdf");

// Dapatkan properti
Console.WriteLine(pdfDocument.Metadata["xmp:CreateDate"]);
Console.WriteLine(pdfDocument.Metadata["xmp:Nickname"]);
Console.WriteLine(pdfDocument.Metadata["xmp:CustomProperty"]);
```

## Mengatur Metadata XMP dalam File PDF

Aspose.PDF memungkinkan Anda untuk mengatur metadata dalam file PDF.
Aspose.PDF memungkinkan Anda untuk mengatur metadata dalam file PDF.

1. Buat objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Atur nilai metadata menggunakan properti [Metadata](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/metadata).
1. Simpan dokumen yang telah diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) dari objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

Potongan kode berikut menunjukkan cara mengatur metadata dalam file PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Path ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "SetXMPMetadata.pdf");

// Atur properti
pdfDocument.Metadata["xmp:CreateDate"] = DateTime.Now;
pdfDocument.Metadata["xmp:Nickname"] = "Nickname";
pdfDocument.Metadata["xmp:CustomProperty"] = "Custom Value";

dataDir = dataDir + "SetXMPMetadata_out.pdf";
// Simpan dokumen
pdfDocument.Save(dataDir);
```
## Menyisipkan Metadata dengan Prefiks

Beberapa pengembang perlu membuat ruang nama metadata baru dengan prefiks. Cuplikan kode berikut menunjukkan cara menyisipkan metadata dengan prefiks.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "SetXMPMetadata.pdf");
pdfDocument.Metadata.RegisterNamespaceUri("xmp", "http:// Ns.adobe.com/xap/1.0/"); // Prefiks Xmlns dihapus
pdfDocument.Metadata["xmp:ModifyDate"] = DateTime.Now;

dataDir = dataDir + "SetPrefixMetadata_out.pdf";
// Simpan dokumen
pdfDocument.Save(dataDir);
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


