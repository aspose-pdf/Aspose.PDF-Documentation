---
title: Mengirim Data AcroForm
linktitle: Mengirim AcroForm
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /id/net/posting-acroform-data/
description: Anda dapat mengimpor dan mengekspor data formulir ke dan dari file XML dengan namespace Aspose.Pdf.Facades di Aspose.PDF for .NET.
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
    "alternativeHeadline": "Post AcroForm Data",
    "abstract": "Memperkenalkan fitur baru yang kuat di Aspose.PDF for .NET, kemampuan untuk mengirim data AcroForm. Fungsionalitas ini memungkinkan pengembang untuk tidak hanya membuat dan mengedit AcroForms tetapi juga dengan mudah mengimpor dan mengekspor data formulir ke file XML, meningkatkan kemampuan pemrosesan dan penyimpanan data dalam aplikasi.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Posting AcroForm Data, Import and Export Form Data, Aspose.PDF for .NET, AcroForm Fields, Submit Button, External Web Page Integration, Form Data Posting, XML File Handling, FieldType.Text, Database Saving",
    "wordcount": "400",
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
    "url": "/net/posting-acroform-data/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/posting-acroform-data/"
    },
    "dateModified": "2024-11-25",
    "description": "Anda dapat mengimpor dan mengekspor data formulir ke dan dari file XML dengan namespace Aspose.Pdf.Facades di Aspose.PDF for .NET."
}
</script>

{{% alert color="primary" %}}

AcroForm adalah jenis penting dari dokumen PDF. Anda tidak hanya dapat membuat dan mengedit AcroForm menggunakan [namespace Aspose.Pdf.Facades](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace), tetapi juga mengimpor dan mengekspor data formulir ke dan dari file XML. Namespace Aspose.Pdf.Facades di Aspose.PDF for .NET memungkinkan Anda untuk menerapkan fitur lain dari AcroForm, yang membantu Anda mengirim data AcroForm ke halaman web eksternal. Halaman web ini kemudian membaca variabel yang dikirim dan menggunakan data ini untuk pemrosesan lebih lanjut. Fitur ini berguna dalam kasus ketika Anda tidak hanya ingin menyimpan data di file PDF, tetapi juga ingin mengirimnya ke server Anda dan kemudian menyimpannya di database, dll.

{{% /alert %}}

## Detail Implementasi

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

Dalam artikel ini, kami telah mencoba untuk membuat AcroForm menggunakan [namespace Aspose.Pdf.Facades](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace). Kami juga telah menambahkan tombol kirim dan mengatur URL targetnya. Potongan kode berikut menunjukkan kepada Anda bagaimana cara membuat formulir dan kemudian menerima data yang dikirim di halaman web.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateAcroFormWithFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create an instance of FormEditor class and bind input and output pdf files
    using (var editor = new Aspose.Pdf.Facades.FormEditor(dataDir + "input.pdf", dataDir + "output.pdf"))
    {
        // Create AcroForm fields - I have created only two fields for simplicity
        editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "firstname", 1, 100, 600, 200, 625);
        editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "lastname", 1, 100, 550, 200, 575);

        // Add a submit button and set target URL
        editor.AddSubmitBtn("submitbutton", 1, "Submit", "http://localhost/csharptesting/show.aspx", 100, 450, 150, 475);

        // Save PDF document
        editor.Save();
    }
}
```

{{% alert color="primary" %}}

Potongan kode berikut menunjukkan kepada Anda bagaimana menerima nilai yang dikirim di halaman web target. Dalam contoh ini, saya telah menggunakan halaman bernama Show.aspx, dan saya telah menambahkan kode satu baris sederhana di metode pemuatan halaman.

{{% /alert %}}

```csharp
// Show the posted values on the target web page
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