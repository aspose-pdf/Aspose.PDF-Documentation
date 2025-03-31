---
title: Mendekripsi File PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /id/net/decrypt-pdf-file/
description: Jelajahi metode untuk mendekripsi file PDF yang dilindungi kata sandi di .NET, memastikan akses ke konten dokumen menggunakan Aspose.PDF.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Decrypt PDF File",
    "alternativeHeadline": "Unlock Encrypted PDFs with Ease Using PdfFileSecurity",
    "abstract": "Buka dokumen PDF Anda dengan mudah menggunakan fitur baru Mendekripsi File PDF dengan kelas PdfFileSecurity. Fungsionalitas ini memungkinkan pengguna untuk menghapus perlindungan kata sandi dari PDF terenkripsi, memungkinkan akses dan manipulasi dokumen yang lancar. Rasakan pendekatan yang sederhana untuk manajemen dokumen dengan memanfaatkan metode DecryptFile yang kuat untuk penanganan PDF yang aman.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "235",
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
    "url": "/net/decrypt-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/decrypt-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat mengatasi tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

Dokumen PDF yang dienkripsi dengan kata sandi atau sertifikat harus dibuka kuncinya sebelum operasi lain dapat dilakukan padanya. Jika Anda mencoba untuk beroperasi pada dokumen PDF yang terenkripsi, Anda akan melemparkan pengecualian. Setelah membuka kunci PDF yang terenkripsi, Anda dapat melakukan satu atau lebih operasi padanya.

## Mendekripsi File PDF menggunakan Kata Sandi Pemilik

{{% alert color="primary" %}}
Coba secara online <br>
Anda dapat mencoba membuka kunci dokumen menggunakan Aspose.PDF dan mendapatkan hasilnya secara online di tautan ini:
[products.aspose.app/pdf/unlock](https://products.aspose.app/pdf/unlock)

{{% /alert %}}

Untuk mendekripsi file PDF, Anda perlu membuat objek [PdfFileSecurity](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffilesecurity) dan kemudian memanggil metode [DecryptFile](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile). Anda juga perlu melewatkan kata sandi pemilik ke metode [DecryptFile](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile). Potongan kode berikut menunjukkan kepada Anda cara mendekripsi file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DecryptPDFFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdfFileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample_encrypted.pdf"))
    {
        if (pdfFileInfo.IsEncrypted)
        {
            using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
            {
                // Bind PDF document
                fileSecurity.BindPdf(dataDir + "sample_encrypted.pdf");
                // Decrypt PDF document
                fileSecurity.DecryptFile("P@ssw0rd");
                // Save PDF document
                fileSecurity.Save(dataDir + "SampleDecrtypted_out.pdf");
            }
        }
    }
}
```