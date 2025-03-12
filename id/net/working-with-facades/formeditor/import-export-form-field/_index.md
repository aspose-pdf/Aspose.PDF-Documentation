---
title: Impor dan Ekspor Bidang Formulir
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /id/net/import-export-form-field/
description: Isi bidang formulir menggunakan DataTable dengan Kelas FormEditor oleh Aspose.PDF for .NET
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Form Field",
    "alternativeHeadline": "Streamline PDF Form Management with Import/Export Features",
    "abstract": "Fitur Impor dan Ekspor Bidang Formulir di Aspose.PDF for .NET memungkinkan pengguna untuk mengisi dan memanipulasi bidang formulir PDF dengan lancar menggunakan berbagai sumber data seperti FDF, XFDF, XML, dan bahkan objek System.Data.DataTable. API yang kuat ini memungkinkan penanganan data otomatis, meningkatkan efisiensi manajemen formulir PDF dan memperlancar proses input data.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "252",
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
    "url": "/net/import-export-form-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-export-form-field/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

Aspose.PDF for .NET menyediakan kemampuan hebat untuk membuat/memanipulasi bidang formulir di dalam dokumen PDF. Menggunakan API ini, Anda dapat mengisi bidang formulir di dalam file PDF secara programatis, mengisi bidang formulir dengan [Impor Data dari FDF ke File PDF](/pdf/id/net/import-and-export-data/), [Impor Data dari XFDF ke File PDF](/pdf/id/net/import-and-export-data/), [Impor Data dari XML ke File PDF](/pdf/id/net/import-and-export-data/) atau bahkan Anda dapat mengimpor data dari objek [System.Data.DataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ImportData()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Import data fdf
        using (var xfdfInputStream  = new FileStream(dataDir + "student.fdf", FileMode.Open))
        {
            form.ImportFdf(xfdfInputStream);
        }
                
        // Import data XML
        using (var xfdfInputStream  = new FileStream(dataDir + "input.xml", FileMode.Open))
        {
            form.ImportXml(xfdfInputStream);
        }
                
        // Import data XFDF
        using (var xfdfInputStream  = new FileStream(dataDir + "input.xfdf", FileMode.Open))
        {
            form.ImportXfdf(xfdfInputStream);
        }
                
        // Save PDF document
        form.Save(dataDir + "ImportDataUpdated_out.pdf");
    }
}
```

## Ekspor Data dari FDF ke File PDF

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ExportData()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");
                
        // Create FDF file
        using (var fdfOutputStream = new FileStream(dataDir + "data_out.fdf", FileMode.Create))
        {
            form.ExportXfdf(fdfOutputStream);
        }
                
        // Create XML file
        using (var xmlOutputStream = new FileStream(dataDir + "data_out.xml", FileMode.Create))
        {
            form.ExportXfdf(xmlOutputStream);
        }
            
        // Create XFDF file
        using (var xfdfOutputStream = new FileStream(dataDir + "data_out.xfdf", FileMode.Create))
        {
            form.ExportXfdf(xfdfOutputStream);
        }              
    }
} 
```