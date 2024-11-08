---
title: Mengisi AcroForm - Mengisi Formulir PDF menggunakan C#
linktitle: Mengisi AcroForm
type: docs
weight: 20
url: /id/net/fill-form/
keywords: Mengisi Formulir PDF C#
description: Anda dapat mengisi formulir dalam dokumen PDF Anda dengan perpustakaan Aspose.PDF untuk .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Mengisi AcroForm",
    "alternativeHeadline": "Cara mengisi AcroForm di PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, mengisi acroform",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dokumen Aspose.PDF",
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
    "url": "/net/fill-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/fill-form/"
    },
    "dateModified": "2022-02-04",
    "description": "Anda dapat mengisi formulir dalam dokumen PDF Anda dengan perpustakaan Aspose.PDF untuk .NET."
}
</script>

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## Mengisi Kolom Formulir dalam Dokumen PDF

Untuk mengisi kolom formulir, dapatkan kolom dari koleksi Form objek Dokumen. kemudian atur nilai kolom menggunakan properti Value kolom tersebut.

Contoh ini memilih TextBoxField dan mengatur nilainya menggunakan properti Value.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "FillFormField.pdf");

// Dapatkan kolom
TextBoxField textBoxField = pdfDocument.Form["textbox1"] sebagai TextBoxField;

// Modifikasi nilai kolom
textBoxField.Value = "Nilai yang akan diisi dalam kolom";
dataDir = dataDir + "FillFormField_out.pdf";
// Simpan dokumen yang telah diperbarui
pdfDocument.Save(dataDir);
```

