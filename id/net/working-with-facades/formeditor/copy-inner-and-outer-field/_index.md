---
title: Salin Field Dalam dan Luar
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /id/net/copy-inner-and-outer-field/
description: Bagian ini menjelaskan cara menyalin Field Dalam dan Luar dengan Aspose.PDF Facades menggunakan Kelas FormEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Copy Inner and Outer Field",
    "alternativeHeadline": "Seamlessly Copy Inner and Outer Fields in PDF",
    "abstract": "Fungsi Salin Field Dalam dan Luar dalam Aspose.PDF for .NET meningkatkan pengeditan formulir dengan memungkinkan pengguna untuk menduplikasi field dalam PDF yang sama atau mentransfernya dari file PDF eksternal. Dengan metode CopyInnerField dan CopyOuterField yang mudah digunakan yang disediakan oleh kelas FormEditor, pengguna dapat mengelola field formulir dengan efisien, memastikan konsistensi dan menghemat waktu dalam persiapan dokumen.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "337",
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
    "url": "/net/copy-inner-and-outer-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/copy-inner-and-outer-field/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

[CopyInnerField](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor/methods/copyinnerfield/index) metode memungkinkan Anda untuk menyalin sebuah field dalam file yang sama, pada koordinat yang sama, di halaman yang ditentukan. Metode ini memerlukan nama field yang ingin Anda salin, nama field baru, dan nomor halaman di mana field perlu disalin. Kelas [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) menyediakan metode ini. Cuplikan kode berikut menunjukkan kepada Anda cara menyalin field di lokasi yang sama dalam file yang sama.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CopyInnerField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor object
    using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "Sample-Form-01.pdf"))
        {
            // Add page
            document.Pages.Add();

            // Bind PDF document
            formEditor.BindPdf(document);

            // Copy the field "Last Name" from the first page to "Last Name 2" on the second page
            formEditor.CopyInnerField("Last Name", "Last Name 2", 2);

            // Save PDF document
            formEditor.Save(dataDir + "Sample-Form-01-mod.pdf");
        }
    }
}
```

## Salin Field Luar dalam File PDF yang Ada

[CopyOuterField](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor/methods/copyouterfield/index) metode memungkinkan Anda untuk menyalin sebuah field formulir dari file PDF eksternal dan kemudian menambahkannya ke file PDF input di lokasi yang sama dan nomor halaman yang ditentukan. Metode ini memerlukan file PDF dari mana field perlu disalin, nama field, dan nomor halaman di mana field perlu disalin. Metode ini disediakan oleh kelas [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Cuplikan kode berikut menunjukkan kepada Anda cara menyalin sebuah field dari file PDF eksternal.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CopyOuterField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor 
    using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Create empty document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            document.Pages.Add();

            // Bind PDF document
            formEditor.BindPdf(document);

            // Copy the outer field "First Name" from the original document to the new document
            formEditor.CopyOuterField(dataDir + "Sample-Form-01.pdf", "First Name", 1);

            // Copy the outer field "Last Name" from the original document to the new document
            formEditor.CopyOuterField(dataDir + "Sample-Form-01.pdf", "Last Name", 1);

            // Save PDF document
            formEditor.Save(dataDir + "Sample-Form-02-mod.pdf");
        }
    }
}
```