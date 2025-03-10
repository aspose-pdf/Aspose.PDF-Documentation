---
title: Bekerja dengan Formulir XFA
linktitle: Formulir XFA
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /id/net/xfa-forms/
description: Aspose.PDF for .NET API memungkinkan Anda bekerja dengan XFA dan bidang Acroform XFA dalam dokumen PDF. Aspose.Pdf.Facades.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with XFA Forms",
    "alternativeHeadline": "Enhance PDF handling with XFA form support",
    "abstract": "Aspose.PDF for .NET sekarang menawarkan kemampuan canggih untuk bekerja dengan formulir XFA, memungkinkan pengembang untuk mengisi, mengonversi, dan mengelola bidang Acroform XFA dalam dokumen PDF. Fitur ini menyederhanakan manipulasi formulir dinamis, memungkinkan akses yang mulus ke nilai dan properti bidang sambil memberikan konversi yang efisien dari XFA ke AcroForms standar. Tingkatkan alur kerja pemrosesan PDF Anda dengan solusi kuat ini untuk menangani struktur formulir yang kompleks",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "XFA Forms, Aspose.PDF for .NET, fill XFA form, convert XFA to Acroform, get XFA field properties, dynamic forms, XML Forms Architecture, manipulate XFA fields, AcroForm fields, PDF document generation",
    "wordcount": "684",
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
    "url": "/net/xfa-forms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/xfa-forms/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NET API memungkinkan Anda bekerja dengan XFA dan bidang Acroform XFA dalam dokumen PDF. Aspose.Pdf.Facades."
}
</script>

{{% alert color="primary" %}}

Formulir dinamis didasarkan pada spesifikasi XML yang dikenal sebagai XFA, “Arsitektur Formulir XML”. Ini juga dapat mengonversi formulir XFA dinamis ke Acroform standar. Informasi tentang formulir (sejauh PDF bersangkutan) sangat samar – ia menyatakan bahwa bidang ada, dengan properti, dan peristiwa JavaScript, tetapi tidak menentukan rendering apa pun. Objek formulir XFA digambar pada saat memuat dokumen.

{{% /alert %}}

Kelas Form menyediakan kemampuan untuk menangani AcroForm statis dan Anda dapat mendapatkan instance bidang tertentu menggunakan metode GetFieldFacade(..) dari kelas Form. Namun, bidang XFA tidak dapat diakses melalui metode Form.GetFieldFacade(..). Sebagai gantinya, gunakan [Document.Form.XFA](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form/properties/xfa) untuk mendapatkan/mengatur nilai bidang dan memanipulasi template bidang XFA (mengatur properti bidang).

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## Isi bidang XFA

Potongan kode berikut menunjukkan kepada Anda cara mengisi bidang dalam formulir XFA.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FillXFAFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FillXFAFields.pdf"))
    {
        // Get names of XFA form fields
        var names = document.Form.XFA.FieldNames;

        // Set field values
        if (names.Length > 0)
        {
            document.Form.XFA[names[0]] = "Field 0";
        }
        if (names.Length > 1)
        {
            document.Form.XFA[names[1]] = "Field 1";
        }

        // Save PDF document
        document.Save(dataDir + "FilledXfa_out.pdf");
    }
}
```

## Konversi XFA-ke-Acroform

{{% alert color="primary" %}}

Coba secara online
Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara online di tautan ini: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

Formulir dinamis didasarkan pada spesifikasi XML yang dikenal sebagai XFA, “Arsitektur Formulir XML”. Informasi tentang formulir (sejauh PDF bersangkutan) sangat samar – ia menyatakan bahwa bidang ada, dengan properti, dan peristiwa JavaScript, tetapi tidak menentukan rendering apa pun.

Saat ini, PDF mendukung dua metode berbeda untuk mengintegrasikan data dan formulir PDF:

- AcroForms (juga dikenal sebagai formulir Acrobat), diperkenalkan dan disertakan dalam spesifikasi format PDF 1.2.
- Formulir Arsitektur Formulir XML Adobe (XFA), diperkenalkan dalam spesifikasi format PDF 1.5 sebagai fitur opsional (Spesifikasi XFA tidak termasuk dalam spesifikasi PDF, hanya dirujuk.)

Kami tidak dapat mengekstrak atau memanipulasi halaman dari Formulir XFA, karena konten formulir dihasilkan pada waktu berjalan (selama tampilan formulir XFA) dalam aplikasi yang mencoba menampilkan atau merender formulir XFA. Aspose.PDF memiliki fitur yang memungkinkan pengembang untuk mengonversi formulir XFA ke AcroForms standar.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertDynamicXFAToAcroForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Load dynamic XFA form
    using (var document = new Aspose.Pdf.Document(dataDir + "DynamicXFAToAcroForm.pdf"))
    {
        // Set the form fields type as standard AcroForm
        document.Form.Type = Aspose.Pdf.Forms.FormType.Standard;

        // Save PDF document
        document.Save(dataDir + "StandardAcroForm_out.pdf");
    }
}
```

## Dapatkan properti bidang XFA

Untuk mengakses properti bidang, pertama gunakan Document.Form.XFA.Template untuk mengakses template bidang. Potongan kode berikut menunjukkan langkah-langkah untuk mendapatkan koordinat X dan Y dari bidang formulir XFA.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetXFAProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetXFAProperties.pdf"))
    {
        // Get names of XFA form fields
        var names = document.Form.XFA.FieldNames;

        // Set field values
        if (names.Length > 0)
        {
            document.Form.XFA[names[0]] = "Field 0";
        }
        if (names.Length > 1)
        {
            document.Form.XFA[names[1]] = "Field 1";
        }

        // Get field position
        if (names.Length > 0)
        {
            Console.WriteLine(document.Form.XFA.GetFieldTemplate(names[0]).Attributes["x"].Value);
            Console.WriteLine(document.Form.XFA.GetFieldTemplate(names[0]).Attributes["y"].Value);
        }

        // Save PDF document
        document.Save(dataDir + "FilledXfa_out.pdf");
    }
}
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