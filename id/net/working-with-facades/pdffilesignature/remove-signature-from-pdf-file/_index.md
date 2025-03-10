---
title: Hapus Tanda Tangan dari File PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /id/net/remove-signature-from-pdf/
description: Bagian ini menjelaskan cara menghapus tanda tangan dari File PDF menggunakan kelas PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Remove Signature from PDF File",
    "alternativeHeadline": "Effortlessly Remove Signatures from PDF Files",
    "abstract": "Fungsionalitas ini memungkinkan pengguna untuk secara efisien menghapus tanda tangan digital dari file PDF menggunakan kelas PdfFileSignature. Fitur ini memberikan fleksibilitas, memungkinkan penghapusan tanda tangan tertentu sambil secara opsional mempertahankan kolom tanda tangan untuk digunakan di masa depan, meningkatkan kemampuan manajemen dokumen.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "434",
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
    "url": "/net/remove-signature-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/remove-signature-from-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Hapus Tanda Tangan Digital dari File PDF

Ketika sebuah tanda tangan telah ditambahkan ke file PDF, adalah mungkin untuk menghapusnya. Anda dapat menghapus tanda tangan tertentu, atau semua tanda tangan dalam sebuah file. Metode tercepat untuk menghapus tanda tangan juga menghapus kolom tanda tangan, tetapi dimungkinkan untuk hanya menghapus tanda tangan, menjaga kolom tanda tangan sehingga file dapat ditandatangani lagi.

Metode RemoveSignature dari kelas [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) memungkinkan Anda untuk menghapus tanda tangan dari file PDF. Metode ini mengambil nama tanda tangan sebagai input. Anda dapat menentukan nama tanda tangan secara langsung, untuk menghapus semua tanda tangan, dapatkan nama tanda tangan menggunakan metode [GetSignNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/getsignername).

Potongan kode berikut menunjukkan cara menghapus tanda tangan digital dari file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveSignature()
{  
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "signed_rsa.pdf");
        // Get list of signature names
        var sigNames = pdFileSignature.GetSignNames();
        // Remove all the signatures from the PDF file
        for (int index = 0; index < sigNames.Count; index++)
        {
            Console.WriteLine($"Removed {sigNames[index]}");
            pdFileSignature.RemoveSignature(sigNames[index]);
        }

        // Save PDF document
        pdFileSignature.Save(dataDir + "RemoveSignature_out.pdf");
    }
}
```

### Hapus Tanda Tangan tetapi Pertahankan Kolom Tanda Tangan

Seperti yang ditunjukkan di atas, metode [RemoveSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/removesignature) dari kelas [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) memungkinkan Anda untuk menghapus kolom tanda tangan dari file PDF. Ketika menggunakan metode ini dengan versi sebelum 9.3.0, baik tanda tangan maupun kolom tanda tangan dihapus. Beberapa pengembang ingin hanya menghapus tanda tangan dan mempertahankan kolom tanda tangan sehingga dapat digunakan untuk menandatangani ulang dokumen. Untuk mempertahankan kolom tanda tangan dan hanya menghapus tanda tangan, silakan gunakan potongan kode berikut.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveSignatureButKeepField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {       
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "signed_rsa.pdf");

        pdFileSignature.RemoveSignature("Signature1", false);

        // Save PDF document
        pdFileSignature.Save(dataDir + "RemoveSignature_out.pdf");
    }
}
```

Contoh berikut menunjukkan cara menghapus semua tanda tangan dari kolom.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveSignatureButKeepField2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {       
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "signed_rsa.pdf");

        var sigNames = pdFileSignature.GetSignatureNames();
        foreach (var sigName in sigNames)
        {
            pdFileSignature.RemoveSignature(sigName, false);
        }

        // Save PDF document
        pdFileSignature.Save(dataDir + "RemoveSignature_out.pdf");
    }
}
```