---
title: Posting AcroForm Data
linktitle: Posting AcroForm
type: docs
weight: 50
url: /id/net/posting-acroform-data/
description: Anda dapat mengimpor dan mengekspor data formulir ke dan dari file XML dengan namespace Aspose.Pdf.Facades di Aspose.PDF untuk .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Posting AcroForm Data",
    "alternativeHeadline": "Import and Export form data to XML file",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, posting acroform data",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
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
    "url": "/net/posting-acroform-data/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/posting-acroform-data/"
    },
    "dateModified": "2022-02-04",
    "description": "Anda dapat mengimpor dan mengekspor data formulir ke dan dari file XML dengan namespace Aspose.Pdf.Facades di Aspose.PDF untuk .NET."
}
</script>
{{% alert color="primary" %}}

AcroForm adalah tipe penting dari dokumen PDF. Anda tidak hanya dapat membuat dan mengedit AcroForm menggunakan [Aspose.Pdf.Facades namespace](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace), tetapi juga mengimpor dan mengekspor data formulir ke dan dari file XML. Namespace Aspose.Pdf.Facades dalam Aspose.PDF untuk .NET memungkinkan Anda mengimplementasikan fitur lain dari AcroForm, yang membantu Anda mengirimkan data AcroForm ke halaman web eksternal. Halaman web ini kemudian membaca variabel post dan menggunakan data ini untuk pemrosesan lebih lanjut. Fitur ini berguna dalam kasus ketika Anda tidak hanya ingin menyimpan data dalam file PDF, melainkan Anda ingin mengirimkannya ke server Anda dan kemudian menyimpannya dalam database, dll.

{{% /alert %}}

## Detail Implementasi

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

Dalam artikel ini, kami telah mencoba membuat AcroForm menggunakan [Aspose.Pdf.Facades namespace](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace).
Dalam artikel ini, kami telah mencoba membuat AcroForm menggunakan [Aspose.Pdf.Facades namespace](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace).

```csharp
// Buat sebuah instance dari kelas FormEditor dan ikat file pdf input dan output
Aspose.Pdf.Facades.FormEditor editor = new Aspose.Pdf.Facades.FormEditor("input.pdf","output.pdf");

// Buat field AcroForm - Saya hanya membuat dua field untuk kesederhanaan
editor.AddField(Aspose.PDF.Facades.FieldType.Text, "firstname", 1, 100, 600, 200, 625);
editor.AddField(Aspose.PDF.Facades.FieldType.Text, "lastname", 1, 100, 550, 200, 575);

// Tambahkan tombol submit dan atur URL target
editor.AddSubmitBtn("submitbutton", 1, "Submit", "http://localhost/csharptesting/show.aspx", 100, 450, 150, 475);

// Simpan file pdf output
editor.Save();
```

{{% alert color="primary" %}}

Potongan kode berikut menunjukkan bagaimana Anda menerima nilai yang diposting di halaman web target.
Potongan kode berikut menunjukkan cara menerima nilai yang diposting di halaman web tujuan.
{{% /alert %}}

```csharp
// Tampilkan nilai yang diposting di halaman web tujuan
Response.Write("Hello " + Request.Form.Get("firstname") + " " + Request.Form.Get("lastname"));
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


