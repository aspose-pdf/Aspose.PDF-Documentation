---
title: Menambahkan tanda tangan digital atau menandatangani PDF secara digital dalam C#
linktitle: Menandatangani PDF secara digital
type: docs
weight: 10
url: id/net/digitally-sign-pdf-file/
description: Menandatangani dokumen PDF secara digital menggunakan C# atau VB.NET. Verifikasi atau validasi PDF yang ditandatangani secara digital menggunakan C# atau VB.NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Cara menandatangani PDF secara digital",
    "alternativeHeadline": "Bekerja dengan PDF yang ditandatangani secara digital",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen PDF",
    "keywords": "pdf, c#, tanda tangan digital pdf",
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
    "url": "/net/digitally-sign-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/digitally-sign-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Menandatangani dokumen PDF secara digital menggunakan C# atau VB.NET. Verifikasi atau validasi PDF yang ditandatangani secara digital menggunakan C# atau VB.NET."
}
</script>

Aspose.PDF untuk .NET mendukung fitur untuk menandatangani digital file PDF menggunakan kelas SignatureField. Anda juga dapat mensertifikasi file PDF dengan PKCS12-Certificate. Sesuatu yang serupa dengan [Menambahkan Tanda Tangan dan Keamanan di Adobe Acrobat](https://www.adobepress.com/articles/article.asp?p=1272495&seqNum=6).

Ketika menandatangani dokumen PDF menggunakan tanda tangan, Anda pada dasarnya mengkonfirmasi isi dokumen "apa adanya". Akibatnya, perubahan lain yang dibuat setelahnya akan membatalkan tanda tangan dan dengan demikian, Anda akan tahu jika dokumen tersebut telah diubah. Sedangkan, mensertifikasi dokumen terlebih dahulu memungkinkan Anda untuk menentukan perubahan apa yang dapat dilakukan pengguna pada dokumen tanpa membatalkan sertifikasi.

Dengan kata lain, dokumen tersebut masih dianggap mempertahankan integritasnya dan penerima masih dapat mempercayai dokumen tersebut. Untuk detail lebih lanjut, silakan kunjungi Sertifikasi dan penandatanganan PDF. Secara umum, mensertifikasi dokumen dapat dibandingkan dengan menandatangani kode sebuah eksekutabel .NET.

Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).
Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Fitur tanda tangan Aspose.PDF untuk .NET

Kita dapat menggunakan kelas dan metode berikut untuk penandatanganan PDF

- Kelas [DocMDPSignature](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpsignature)
- Enumerasi [DocMDPAccessPermissions](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpaccesspermissions)
- Properti [IsCertified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/properties/iscertified) di kelas [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature)

## Tandatangani PDF dengan tanda tangan digital

```csharp
public static void SignDocument()
{
    string inFile = System.IO.Path.Combine(_dataDir,"DigitallySign.pdf");
    string outFile = System.IO.Path.Combine(_dataDir,"DigitallySign_out.pdf");
    using (Document document = new Document(inFile))
    {
        using (PdfFileSignature signature = new PdfFileSignature(document))
        {
            PKCS7 pkcs = new PKCS7(@"C:\Keys\test.pfx", "Pa$$w0rd2020"); // Gunakan objek PKCS7/PKCS7Detached
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200),pkcs);
            // Simpan file PDF keluaran
            signature.Save(outFile);
        }
    }
}
```
## Tambahkan timestamp ke tanda tangan digital

### Cara menandatangani PDF secara digital dengan timestamp

Aspose.PDF untuk .NET mendukung penandatanganan digital PDF dengan server timestamp atau layanan Web.

Untuk mencapai persyaratan ini, kelas [TimestampSettings](https://reference.aspose.com/pdf/net/aspose.pdf/timestampsettings) telah ditambahkan ke namespace Aspose.PDF. Silakan lihat potongan kode berikut yang mendapatkan timestamp dan menambahkannya ke dokumen PDF:

```csharp
public static void SignWithTimeStampServer()
{
    using (Document document = new Document(System.IO.Path.Combine(_dataDir,"SimpleResume.pdf")))
    {
        using (PdfFileSignature signature = new PdfFileSignature(document))
        {
            PKCS7 pkcs = new PKCS7(@"C:\Keys\test.pfx", "Start2020");
            TimestampSettings timestampSettings = new TimestampSettings("https://freetsa.org/tsr", string.Empty); // User/Password dapat dihilangkan
            pkcs.TimestampSettings = timestampSettings;
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(100, 100, 200, 100);
            // Buat salah satu dari tiga jenis tanda tangan
            signature.Sign(1, "Alasan Tanda Tangan", "Kontak", "Lokasi", true, rect, pkcs);
            // Simpan file PDF keluaran
            signature.Save(System.IO.Path.Combine(_dataDir, "DigitallySignWithTimeStamp_out.pdf"));
        }
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF untuk Pustaka .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organisasi",
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
    "applicationCategory": "Pustaka Manipulasi PDF untuk .NET",
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

