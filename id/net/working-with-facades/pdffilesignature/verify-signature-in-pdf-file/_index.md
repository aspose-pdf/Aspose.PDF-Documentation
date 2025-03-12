---
title: Verifikasi Tanda Tangan dalam File PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /id/net/verify-signature-in-pdf/
description: Bagian ini menjelaskan cara memverifikasi tanda tangan dalam File PDF menggunakan kelas PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Verify Signature in PDF File",
    "alternativeHeadline": "Verify Signatures in PDF Files Efficiently",
    "abstract": "Fitur ini memungkinkan pengguna untuk memverifikasi tanda tangan dalam file PDF dengan efisien menggunakan kelas PdfFileSignature. Dengan metode untuk memeriksa baik keberadaan tanda tangan maupun validitasnya, fungsionalitas ini menyederhanakan proses memastikan keaslian dan integritas dokumen. Optimalkan manajemen dokumen dengan mengonfirmasi keamanan PDF Anda secara mulus.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "313",
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
    "url": "/net/verify-signature-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/verify-signature-in-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Verifikasi Apakah File PDF Ditandatangani Menggunakan Tanda Tangan

Untuk memverifikasi apakah file PDF ditandatangani menggunakan [tanda tangan tertentu](/pdf/id/net/working-with-signature-in-a-pdf-file/), gunakan metode VerifySigned dari kelas [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature). Metode ini memerlukan nama tanda tangan dan mengembalikan true jika PDF ditandatangani menggunakan nama tanda tangan tersebut. Juga dimungkinkan untuk memverifikasi bahwa [PDF ditandatangani](/pdf/id/net/working-with-signature-in-a-pdf-file/), tanpa memverifikasi tanda tangan mana yang digunakan.

### Memverifikasi bahwa PDF Ditandatangani dengan Tanda Tangan Tertentu

Potongan kode berikut menunjukkan cara memverifikasi apakah PDF ditandatangani menggunakan tanda tangan tertentu.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IsPdfSigned()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {      
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "signed_rsa.pdf");
        if (pdFileSignature.ContainsSignature())
        {
            Console.WriteLine("Document Signed");
        }
    }
}
```

### Memverifikasi bahwa PDF Ditandatangani

Untuk menentukan apakah sebuah file ditandatangani, tanpa memberikan nama tanda tangan, gunakan kode berikut.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IsPdfSignedWithGivenSignature()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "signed_rsa.pdf");
        if (pdFileSignature.VerifySignature("Signature1"))
        {
            Console.WriteLine("PDF Signed");
        }
    }
}
```

## Verifikasi Apakah Tanda Tangan Valid

Metode [VerifySignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/verifysignature) dari kelas [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) memungkinkan Anda untuk memvalidasi tanda tangan tertentu. Metode ini memerlukan nama tanda tangan sebagai input dan mengembalikan true jika tanda tangan tersebut valid. Potongan kode berikut menunjukkan cara memvalidasi tanda tangan.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IsPdfSignatureValid()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "signed_rsa.pdf");
        if (pdFileSignature.VerifySignature("Signature1"))
        {
            Console.WriteLine("Signature Verified");
        }
    }
}
```