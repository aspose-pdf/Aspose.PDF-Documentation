---
title: Kontrol Pengecualian File PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /id/net/control-exception/
description: Pelajari cara menangani pengecualian dalam pemrosesan PDF dan memastikan operasi yang lancar saat bekerja dengan PDF menggunakan Aspose.PDF di .NET.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Control Exception PDF File",
    "alternativeHeadline": "Manage PDF Exception Handling with New Security Control",
    "abstract": "Fitur Kontrol Pengecualian dalam kelas PdfFileSecurity memungkinkan Anda untuk mengelola penanganan kesalahan saat mendekripsi file PDF dengan mengubah properti AllowExceptions. Pengguna dapat memilih antara menerima hasil boolean untuk keberhasilan dekripsi atau menggunakan blok try-catch untuk manajemen pengecualian yang komprehensif, meningkatkan fleksibilitas dan kontrol atas operasi keamanan PDF",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "224",
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
    "url": "/net/control-exception/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/control-exception/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga mengatasi tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

[Kelas PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) memungkinkan Anda untuk mengontrol pengecualian. Untuk melakukan ini, Anda perlu mengatur properti [AllowExceptions](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) ke false atau true. Jika Anda mengatur operasi ke false, hasil dari [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile) akan mengembalikan true atau false tergantung pada kebenaran kata sandi.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ControlExceptionPDFFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "sample_encrypted.pdf");
        // Disallow exceptions
        fileSecurity.AllowExceptions = false;
        
        // Decrypt PDF document
        if (!fileSecurity.DecryptFile("IncorrectPassword"))
        {
            Console.WriteLine("Something wrong...");
            Console.WriteLine($"Last exception: {fileSecurity.LastException.Message}");
        }
        // Save PDF document
        fileSecurity.Save(dataDir + "SampleDecrtypted_out.pdf");
    }
}
```

Jika Anda mengatur properti [AllowExceptions](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) ke true, maka Anda dapat mendapatkan hasil dari operasi menggunakan operator try-catch.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ControlExceptionPDFFile2()
{   
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "sample_encrypted.pdf");
        // Allow exceptions
        fileSecurity.AllowExceptions = true;
        try
        {
            // Decrypt PDF document
            fileSecurity.DecryptFile("IncorrectPassword");
        }
        catch (Exception ex)
        {
            Console.WriteLine("Something wrong...");
            Console.WriteLine($"Exception: {ex.Message}");
        }
        // Save PDF document
        fileSecurity.Save(dataDir + "SampleDecrtypted_out.pdf");
    }
}
```