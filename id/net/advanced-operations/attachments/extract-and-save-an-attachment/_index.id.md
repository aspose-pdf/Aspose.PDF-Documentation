---
title: Ekstrak dan Simpan Lampiran
linktitle: Ekstrak dan Simpan Lampiran
type: docs
weight: 20
url: /net/extract-and-save-an-attachment/
description: Aspose.PDF untuk .NET memungkinkan Anda untuk mendapatkan semua lampiran dari dokumen PDF. Selain itu, Anda juga dapat mendapatkan lampiran individu dari dokumen Anda.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ekstrak dan Simpan Lampiran",
    "alternativeHeadline": "Bagaimana cara mengekstrak dan menyimpan lampiran",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, simpan lampiran, ekstrak lampiran",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dokumentasi Aspose.PDF",
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
    "url": "/net/extract-and-save-an-attachment/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-and-save-an-attachment/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF untuk .NET memungkinkan Anda untuk mendapatkan semua lampiran dari dokumen PDF. Selain itu, Anda juga dapat mendapatkan lampiran individu dari dokumen Anda."
}
</script>
## Dapatkan Semua Lampiran

Dengan Aspose.PDF, memungkinkan untuk mendapatkan semua lampiran dari dokumen PDF. Ini berguna baik ketika Anda ingin menyimpan dokumen secara terpisah dari PDF, atau jika Anda perlu menghilangkan lampiran dari PDF.

Untuk mendapatkan semua lampiran dari file PDF:

1. Melakukan perulangan melalui koleksi [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) pada objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Koleksi [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) berisi semua lampiran. Setiap elemen dari koleksi ini mewakili objek [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification). Setiap iterasi dari perulangan foreach melalui koleksi [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) menghasilkan objek [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification).
Potongan kode berikut menunjukkan bagaimana mendapatkan semua lampiran dari dokumen PDF.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "GetAlltheAttachments.pdf");

// Dapatkan koleksi file yang tertanam
EmbeddedFileCollection embeddedFiles = pdfDocument.EmbeddedFiles;

// Dapatkan jumlah file yang tertanam
Console.WriteLine("Total files : {0}", embeddedFiles.Count);

int count = 1;

// Loop melalui koleksi untuk mendapatkan semua lampiran
foreach (FileSpecification fileSpecification in embeddedFiles)
{
    Console.WriteLine("Name: {0}", fileSpecification.Name);
    Console.WriteLine("Description: {0}",
    fileSpecification.Description);
    Console.WriteLine("Mime Type: {0}", fileSpecification.MIMEType);

    // Periksa jika objek parameter mengandung parameter
    if (fileSpecification.Params != null)
    {
        Console.WriteLine("CheckSum: {0}",
        fileSpecification.Params.CheckSum);
        Console.WriteLine("Creation Date: {0}",
        fileSpecification.Params.CreationDate);
        Console.WriteLine("Modification Date: {0}",
        fileSpecification.Params.ModDate);
        Console.WriteLine("Size: {0}", fileSpecification.Params.Size);
    }

    // Dapatkan lampiran dan tulis ke file atau aliran
    byte[] fileContent = new byte[fileSpecification.Contents.Length];
    fileSpecification.Contents.Read(fileContent, 0,
    fileContent.Length);
    FileStream fileStream = new FileStream(dataDir + count + "_out" + ".txt",
    FileMode.Create);
    fileStream.Write(fileContent, 0, fileContent.Length);
    fileStream.Close();
    count+=1;
}
```
## Dapatkan Lampiran Individu

Untuk mendapatkan lampiran individu, kita dapat menentukan indeks lampiran dalam objek `EmbeddedFiles` dari instansi Dokumen. Silakan coba menggunakan potongan kode berikut.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "GetIndividualAttachment.pdf");

// Dapatkan file tertanam tertentu
FileSpecification fileSpecification = pdfDocument.EmbeddedFiles[1];

// Dapatkan properti file
Console.WriteLine("Nama: {0}", fileSpecification.Name);
Console.WriteLine("Deskripsi: {0}", fileSpecification.Description);
Console.WriteLine("Tipe MIME: {0}", fileSpecification.MIMEType);

// Periksa apakah objek parameter berisi parameter
if (fileSpecification.Params != null)
{
    Console.WriteLine("Checksum: {0}",
    fileSpecification.Params.CheckSum);
    Console.WriteLine("Tanggal Pembuatan: {0}",
    fileSpecification.Params.CreationDate);
    Console.WriteLine("Tanggal Modifikasi: {0}",
    fileSpecification.Params.ModDate);
    Console.WriteLine("Ukuran: {0}", fileSpecification.Params.Size);
}


// Dapatkan lampiran dan tulis ke file atau stream
byte[] fileContent = new byte[fileSpecification.Contents.Length];
fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);

FileStream fileStream = new FileStream(dataDir + "test_out" + ".txt", FileMode.Create);
fileStream.Write(fileContent, 0, fileContent.Length);
fileStream.Close();
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Perpustakaan Manipulasi PDF untuk .NET",
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
```

