---
title: Dapatkan Nilai Opsi Tombol
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /id/net/get-button-option-value/
description: Bagian ini menjelaskan cara mendapatkan Nilai Opsi Tombol dengan Aspose.PDF Facades menggunakan Kelas Form.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get Button Option Value",
    "alternativeHeadline": "Retrieve Button Option Values from PDF Efficiently",
    "abstract": "Temukan cara untuk mengambil nilai opsi tombol dari file PDF yang ada dengan efisien menggunakan Aspose.PDF Facades. Dengan metode GetButtonOptionValues dan GetButtonOptionCurrentValue dari kelas Form, Anda dapat dengan mudah memperoleh semua opsi yang tersedia untuk tombol radio, serta nilai yang dipilih saat ini, meningkatkan kemampuan manajemen formulir PDF Anda.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "275",
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
    "url": "/net/get-button-option-value/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-button-option-value/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Dapatkan Nilai Opsi Tombol dari File PDF yang Ada

Tombol radio menyediakan cara untuk menunjukkan berbagai opsi. Kelas [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) memungkinkan Anda untuk mendapatkan semua nilai opsi tombol untuk tombol radio tertentu. Anda dapat mendapatkan nilai-nilai ini menggunakan metode [GetButtonOptionValues](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptionvalues). Metode ini memerlukan nama tombol radio sebagai parameter input dan mengembalikan sebuah Hashtable. Anda dapat mengiterasi melalui Hashtable ini untuk mendapatkan nilai opsi. Cuplikan kode berikut menunjukkan cara mendapatkan nilai opsi tombol dari file PDF yang ada.
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void GetButtonOptions()
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "FormField.pdf");

        // Get button option values
        var optionValues = pdfForm.GetButtonOptionValues("Gender");

        IDictionaryEnumerator optionValueEnumerator = optionValues.GetEnumerator();

        while (optionValueEnumerator.MoveNext())
        {
            Console.WriteLine("Key : {0} , Value : {1} ", optionValueEnumerator.Key, optionValueEnumerator.Value);
        }
    }
}
```

## Dapatkan Nilai Opsi Tombol Saat Ini dari File PDF yang Ada

Tombol radio menyediakan cara untuk mengatur nilai opsi, namun hanya satu dari mereka yang dapat dipilih pada satu waktu. Jika Anda ingin mendapatkan nilai opsi yang dipilih saat ini, maka Anda dapat menggunakan metode [GetButtonOptionCurrentValue](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptioncurrentvalue). Kelas [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) menyediakan metode ini. Metode [GetButtonOptionCurrentValue](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptioncurrentvalue) memerlukan nama tombol radio sebagai parameter input dan mengembalikan nilai sebagai string. Cuplikan kode berikut menunjukkan cara mendapatkan nilai opsi tombol saat ini dari file PDF yang ada.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void GetCurremtButtonOptionValue()
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "FormField.pdf");

        // Get button option values
        string optionValue = pdfForm.GetButtonOptionCurrentValue("Gender");

        Console.WriteLine("Current Value : {0} ", optionValue);
    }
}
```