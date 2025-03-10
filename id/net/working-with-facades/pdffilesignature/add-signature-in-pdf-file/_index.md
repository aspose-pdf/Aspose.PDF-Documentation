---
title: Tambahkan Tanda Tangan di File PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/add-signature-in-pdf/
description: Bagian ini menjelaskan cara menambahkan tanda tangan ke File PDF menggunakan kelas PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Signature in PDF File",
    "alternativeHeadline": "Add Custom Digital Signatures to PDF Files",
    "abstract": "Tingkatkan dokumen PDF Anda dengan kemampuan baru untuk menambahkan tanda tangan digital menggunakan kelas PdfFileSignature. Fitur ini memungkinkan pengguna untuk menerapkan berbagai jenis tanda tangan, termasuk PKCS#1, PKCS#7, dan PKCS#7Detached, sambil menyesuaikan penampilan tanda tangan dengan gambar dan atribut tertentu. Permudah proses verifikasi dokumen Anda dengan menggabungkan beberapa tanda tangan di berbagai halaman dengan mudah",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "838",
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
    "url": "/net/add-signature-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-signature-in-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Tambahkan Tanda Tangan Digital di File PDF

[Kelas PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) memungkinkan Anda untuk menambahkan tanda tangan di file PDF. Anda perlu membuat objek dari [Kelas PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) menggunakan file PDF input dan output. Anda juga perlu membuat objek [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle) di mana Anda ingin menambahkan tanda tangan dan untuk mengatur penampilan Anda dapat menentukan gambar menggunakan properti [SignatureAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/properties/signatureappearance) dari objek [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature). Aspose.Pdf.Facades juga menyediakan berbagai jenis tanda tangan seperti PKCS#1, PKCS#7, dan PKCS#7Detached. Untuk membuat tanda tangan dari jenis tertentu, Anda perlu membuat objek dari kelas tertentu seperti **PKCS1**, **PKCS7**, atau **PKCS7Detached** menggunakan file sertifikat dan kata sandi.

Setelah objek dari jenis tanda tangan tertentu dibuat, Anda dapat menggunakan metode [Sign](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/sign/index) dari kelas [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) untuk menandatangani PDF dan meneruskan objek tanda tangan tertentu ke kelas ini. Anda juga dapat menentukan atribut lain untuk metode ini. Akhirnya, Anda perlu menyimpan PDF yang ditandatangani menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) dari kelas [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature). Potongan kode berikut menunjukkan kepada Anda cara menambahkan tanda tangan di file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPdfFileSignature()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "input.pdf");

        // Create a rectangle for signature location
        System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
    
        // Set signature appearance
        pdFileSignature.SignatureAppearance = dataDir + "aspose-logo.png";

        // Create any of the three signature types
        var signature = new PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1

        pdFileSignature.Sign(1, "I'm document author", "test01@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect, signature);
        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```

Contoh kode berikut menunjukkan kepada kita kemampuan untuk menandatangani dokumen dengan dua tanda tangan. Dalam contoh kami, kami menempatkan tanda tangan pertama di halaman pertama, dan yang kedua di halaman kedua. Anda dapat menentukan halaman yang Anda butuhkan.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTwoSignature()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "input.pdf");

        // Create a rectangle for 1st signature location
        System.Drawing.Rectangle rect1 = new System.Drawing.Rectangle(10, 10, 300, 50);

        // Create 1st signature object
        var signature1 = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1

        pdFileSignature.Sign(1, "I'm document author", "test@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect1, signature1);
        pdFileSignature.Save(dataDir + "DigitallySign_out.pdf");

        // Sign with 2nd signature
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "DigitallySign_out.pdf");

        // Create a rectangle for 2nd signature location
        System.Drawing.Rectangle rect2 = new System.Drawing.Rectangle(10, 10, 300, 50);

        // Create 2nd signature object
        var signature2 = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1

        pdFileSignature.Sign(2, "I'm document reviewer", "test02@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect2, signature2);

        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign2_out.pdf");
    }
}
```

Untuk dokumen dengan formulir atau acroforms yang perlu ditandatangani, lihat contoh berikut. Anda perlu membuat objek dari [Kelas PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) menggunakan file PDF input dan output. Gunakan [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesignature/bindpdf/methods/1) untuk mengikat. Buat tanda tangan dengan kemampuan untuk menambahkan properti yang diperlukan. Dalam contoh kami, mereka adalah 'Alasan' dan 'PenampilanKustom'.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPdfFileSignatureField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "input.pdf");

        // Create any of the three signature types
        var signature = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345")
        {
            Reason = "Sign as Author",
            CustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance
            {
                FontSize = 6,
                FontFamilyName = "Calibri"
            }
        }; // PKCS#1
        
        pdFileSignature.Sign("Signature1", signature);
        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```

Jika dokumen kami memiliki dua bidang, algoritma untuk menandatanganinya mirip dengan contoh pertama.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPdfFileSignatureField2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "input.pdf");

        // Create any of the three signature types
        var signature1 = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345")
        {
            Reason = "Sign as Author",
            CustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance
            {
                FontSize = 6
            }
        }; // PKCS#1
        pdFileSignature.Sign("Signature1", signature1);
        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign_out.pdf");
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "DigitallySign_out.pdf");

        // Create any of the three signature types
        var signature2 = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345")
        {
            Reason = "Sign as Reviwer",
            CustomAppearance = new SignatureCustomAppearance
            {
                FontSize = 6
            }
        }; // PKCS#1
        
        pdFileSignature.Sign("Signature2", signature2);
        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign2_out.pdf");
    }
}
```