---
title: Ekstrak Lampiran dari File PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/extract-attachments/
description: Temukan cara untuk mengekstrak dan mengelola lampiran dalam dokumen PDF di .NET menggunakan Aspose.PDF untuk penanganan dokumen yang lebih baik.
lastmod: "2021-06-05"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Attachments from PDF File",
    "alternativeHeadline": "Effortlessly Extract and Manage PDF Attachments",
    "abstract": "Fungsi ekstraksi lampiran baru dalam Aspose.PDF for .NET memungkinkan pengembang untuk dengan mudah mengambil dan mengelola lampiran file dalam dokumen PDF. Dengan memanfaatkan kelas PdfExtractor, pengguna dapat mengekstrak lampiran dan mendapatkan informasi penting, seperti nama dan detail lampiran, meningkatkan kemampuan pemrosesan dokumen",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "208",
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
    "url": "/net/extract-attachments/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-attachments/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

Salah satu kategori utama di bawah kemampuan ekstraksi dari [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) adalah ekstraksi lampiran. Kategori ini menyediakan serangkaian metode, yang tidak hanya membantu mengekstrak lampiran tetapi juga menyediakan metode yang dapat memberikan informasi terkait lampiran, yaitu metode [GetAttachmentInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachmentinfo) dan [GetAttachName](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachnames) yang memberikan informasi lampiran dan nama lampiran masing-masing. Untuk mengekstrak dan kemudian mendapatkan lampiran, kita menggunakan metode [ExtractAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractattachment) dan [GetAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachment).

Potongan kode berikut menunjukkan kepada Anda cara menggunakan metode PdfExtractor:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractAttachments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Create the extractor
    using (var pdfExtractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        pdfExtractor.BindPdf(dataDir + "GetAlltheAttachments.pdf");

        // Extract attachments
        pdfExtractor.ExtractAttachment();

        // Get attachment names
        if (pdfExtractor.GetAttachNames().Count > 0)
        {
            Console.WriteLine("Extracting and storing...");

            // Get extracted attachments
            pdfExtractor.GetAttachment(dataDir + "GetAlltheAttachments_out.pdf");
        }
    }
}
```