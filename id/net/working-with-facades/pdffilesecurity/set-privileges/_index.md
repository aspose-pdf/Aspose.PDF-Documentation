---
title: Atur Hak Akses pada PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /id/net/set-privileges/
description: Temukan cara untuk memodifikasi hak akses pengguna dalam file PDF, membatasi tindakan tertentu menggunakan Aspose.PDF di .NET.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set Privileges on PDF",
    "alternativeHeadline": "Set Custom Permissions for PDF Document Security",
    "abstract": "Memperkenalkan kemampuan baru untuk mengatur hak akses pada file PDF yang ada menggunakan kelas PdfFileSecurity, memungkinkan pengguna untuk menentukan izin untuk tindakan seperti mencetak dan menyalin. Selain itu, pengguna sekarang dapat dengan mudah menghapus hak istimewa dari dokumen PDF, memastikan kontrol yang lebih besar atas modifikasi dan keamanan dokumen. Fungsionalitas ini menyederhanakan manajemen PDF sambil meningkatkan kepatuhan keamanan.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "436",
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
    "url": "/net/set-privileges/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-privileges/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Atur Hak Akses pada File PDF yang Ada

Untuk mengatur hak akses file PDF, buat objek [PdfFileSecurity](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffilesecurity) dan panggil metode SetPrivilege. Anda dapat menentukan hak akses menggunakan objek DocumentPrivilege dan kemudian mengoper objek ini ke metode SetPrivilege. Potongan kode berikut menunjukkan cara mengatur hak akses file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrivilege1()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Create DocumentPrivileges object and set needed privileges
    var privilege = Aspose.Pdf.Facades.DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "sample.pdf");
        // Set privilege
        fileSecurity.SetPrivilege(privilege);
        // Save PDF document
        fileSecurity.Save(dataDir + "SamplePrivileges_out.pdf");
    }
}
```

Lihat metode berikut dengan menentukan kata sandi:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrivilegeWithPassword()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Create DocumentPrivileges object and set needed privileges
    var privilege = Aspose.Pdf.Facades.DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "sample.pdf");
        // Set privilege and passwords
        fileSecurity.SetPrivilege(string.Empty, "P@ssw0rd", privilege);
        // Save PDF document
        fileSecurity.Save(dataDir + "SamplePrivilegesPassword_out.pdf");
    }
}
```

## Hapus Fitur Hak Istimewa dari PDF

Dokumen PDF mendukung fitur hak istimewa untuk memungkinkan pengguna akhir mengisi data ke dalam kolom formulir dengan menggunakan Adobe Acrobat Reader dan kemudian menyimpan salinan formulir yang telah diisi. Namun, ini memastikan bahwa file PDF tidak dimodifikasi dan jika ada modifikasi pada struktur PDF, fitur hak istimewa hilang. Saat melihat dokumen semacam itu, pesan kesalahan ditampilkan, menyatakan bahwa hak istimewa dihapus karena dokumen telah dimodifikasi. Baru-baru ini, kami menerima permintaan untuk menghapus hak istimewa dari dokumen PDF.

Untuk menghapus hak istimewa dari file PDF, metode baru bernama RemoveUsageRights() telah ditambahkan ke kelas PdfFileSignature. Metode lain bernama ContainsUsageRights() ditambahkan untuk menentukan apakah PDF sumber mengandung hak istimewa.

{{% alert color="primary" %}}
Mulai Aspose.PDF for .NET 9.5.0, nama metode berikut telah diperbarui. Harap dicatat bahwa metode sebelumnya masih ada di API tetapi telah ditandai sebagai usang dan akan dihapus. Oleh karena itu, disarankan untuk mencoba menggunakan metode yang diperbarui.

- Metode IsContainSignature(.) diubah namanya menjadi ContainsSignature(..).
- Metode IsCoversWholeDocument(..) diubah namanya menjadi CoversWholeDocument(..).
{{% /alert %}}

Kode berikut menunjukkan cara menghapus hak penggunaan dari dokumen:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveExtendedRights()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_SecuritySignatures();
    
    using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfSign.BindPdf(dataDir + "DigitallySign.pdf");
        if (pdfSign.ContainsUsageRights())
        {
            pdfSign.RemoveUsageRights();
        }
        // Save PDF document
        pdfSign.Document.Save(dataDir + "RemoveRights_out.pdf");
    }
}
```