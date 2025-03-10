---
title: Simpan dokumen PDF secara programatik
linktitle: Simpan PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /id/net/save-pdf-document/
description: Pelajari cara menyimpan file PDF di C# Aspose.PDF for .NET pustaka PDF. Simpan dokumen PDF ke sistem file, ke aliran, dan dalam aplikasi Web.
aliases:
    - /net/saving/
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Save PDF document programmatically",
    "alternativeHeadline": "Programmatic PDF Saving with C#",
    "abstract": "Temukan bagaimana pengembang menyimpan dokumen PDF secara programatik dengan mudah menggunakan Aspose.PDF for .NET. Fitur ini mendukung penyimpanan PDF ke sistem file, aliran, dan langsung dalam aplikasi web, mengakomodasi berbagai kasus penggunaan sambil memastikan kepatuhan terhadap standar PDF/A dan PDF/X untuk pengarsipan jangka panjang dan pertukaran grafik. Optimalkan kemampuan penanganan PDF Anda dengan mekanisme penyimpanan yang kuat ini.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "471",
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
    "url": "/net/save-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/save-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

Potongan kode berikut juga bekerja dengan [Aspose.Drawing](/pdf/net/drawing/) pustaka.

## Simpan dokumen PDF ke sistem file

Anda dapat menyimpan dokumen PDF yang dibuat atau dimanipulasi ke sistem file menggunakan metode `Save` dari kelas `Document`.
Ketika Anda tidak menyediakan tipe format (opsi), maka dokumen disimpan dalam format Aspose.PDF v.1.7 (*.pdf).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Make some manipation, i.g add new empty page
        document.Pages.Add();
        // Save PDF document
        document.Save(dataDir + "SimpleResume_out.pdf");
    }
}
```

## Simpan dokumen PDF ke aliran

Anda juga dapat menyimpan dokumen PDF yang dibuat atau dimanipulasi ke aliran dengan menggunakan overload dari metode `Save`.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveDocumentStream()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Make some manipation, i.g add new empty page
        document.Pages.Add();
        // Save PDF document
        document.Save(dataDir + "SimpleResume_out.pdf");
    }
}
```

Untuk penjelasan yang lebih rinci, silakan ikuti bagian [Showcase](/pdf/net/showcases/).

## Simpan format PDF/A atau PDF/X

PDF/A adalah versi standar ISO dari Portable Document Format (PDF) untuk digunakan dalam pengarsipan dan pelestarian jangka panjang dokumen elektronik.
PDF/A berbeda dari PDF karena melarang fitur yang tidak cocok untuk pengarsipan jangka panjang, seperti tautan font (berlawanan dengan penyematan font) dan enkripsi. Persyaratan ISO untuk pemirsa PDF/A mencakup pedoman manajemen warna, dukungan font yang disematkan, dan antarmuka pengguna untuk membaca anotasi yang disematkan.

PDF/X adalah subset dari standar ISO PDF. Tujuan PDF/X adalah untuk memfasilitasi pertukaran grafik, dan oleh karena itu memiliki serangkaian persyaratan terkait pencetakan yang tidak berlaku untuk file PDF standar.

Dalam kedua kasus, metode `Save` digunakan untuk menyimpan dokumen, sementara dokumen harus disiapkan menggunakan metode `Convert`.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveDocumentAsPDFx()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Add page
        document.Pages.Add();
        // Convert a document to a PDF/X-3 format
        document.Convert(new Aspose.Pdf.PdfFormatConversionOptions(Aspose.Pdf.PdfFormat.PDF_X_3));
        // Save PDF document
        document.Save(dataDir + "SimpleResume_X3.pdf");
    }
}
```