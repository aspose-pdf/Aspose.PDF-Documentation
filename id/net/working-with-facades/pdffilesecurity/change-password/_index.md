---
title: Ubah Kata Sandi File PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /id/net/change-password/
description: Jelajahi cara mengubah kata sandi dokumen PDF di .NET untuk meningkatkan keamanan file dengan Aspose.PDF.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Change Password of PDF File",
    "alternativeHeadline": "Securely Change PDF Passwords with Ease",
    "abstract": "Tingkatkan keamanan PDF Anda dengan mudah dengan mengubah kata sandinya menggunakan kelas PdfFileSecurity. Fungsionalitas ini memungkinkan pengguna untuk memodifikasi kata sandi pengguna dan pemilik, memastikan perlindungan yang kuat terhadap akses tidak sah sambil mengelola izin secara efektif. Optimalkan pengaturan keamanan dokumen Anda dengan mudah melalui implementasi yang sederhana.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "250",
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
    "url": "/net/change-password/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/change-password/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF tidak hanya dapat melakukan tugas sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Ubah Kata Sandi File PDF

Untuk mengubah kata sandi file PDF, Anda perlu membuat objek [PdfFileSecurity](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffilesecurity) dan kemudian memanggil metode [ChangePassword](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2). Anda perlu memberikan kata sandi pemilik yang ada dan kata sandi pengguna serta pemilik yang baru ke metode [ChangePassword](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2).

{{% alert color="primary" %}}

- **Kata sandi pengguna**, jika diatur, adalah yang perlu Anda berikan untuk membuka PDF. Acrobat/Reader akan meminta pengguna untuk memasukkan kata sandi pengguna. Jika tidak benar, dokumen tidak akan terbuka.
- **Kata sandi pemilik**, jika diatur, mengontrol izin, seperti mencetak, mengedit, mengekstrak, mengomentari, dll. Acrobat/Reader akan melarang hal-hal ini berdasarkan pengaturan izin. Acrobat akan memerlukan kata sandi ini jika Anda ingin mengatur/mengubah izin.

{{% /alert %}}

Potongan kode berikut menunjukkan kepada Anda cara mengubah kata sandi file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangePassword()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdfFileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample_encrypted.pdf"))
    {
        // Create PdfFileSecurity object if the document is encrypted
        if (pdfFileInfo.IsEncrypted)    
        {
            using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
            {
                // Bind PDF document
                fileSecurity.BindPdf(dataDir + "sample_encrypted.pdf");
                fileSecurity.ChangePassword("OwnerP@ssw0rd", "Pa$$w0rd1", "Pa$$w0rd2", Aspose.Pdf.Facades.DocumentPrivilege.Print, Aspose.Pdf.Facades.KeySize.x256);
                // Save PDF document
                fileSecurity.Save(dataDir + "sample_encrtypted1.pdf");
            }
        }
    }
}
```