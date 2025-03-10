---
title: Impor dan Ekspor Anotasi ke XFDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /id/net/import-export-annotations/
description: Bagian ini menjelaskan cara mengimpor dan mengekspor anotasi dari file PDF ke XFDF dengan Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Annotations to XFDF",
    "alternativeHeadline": "Import and Export PDF Annotations with XFDF",
    "abstract": "Aspose.PDF for .NET memperkenalkan fungsionalitas yang kuat untuk mengimpor dan mengekspor anotasi ke XFDF, meningkatkan kemampuan manipulasi PDF. Fitur ini memungkinkan pengguna untuk secara selektif mentransfer data anotasi dalam Format Data Formulir XML, memungkinkan integrasi dan pengarsipan yang mulus untuk manajemen dokumen yang lebih baik. Dengan metode khusus untuk menentukan jenis anotasi, pengguna dapat mengelola anotasi PDF mereka dengan efisiensi dan presisi.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "548",
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
    "url": "/net/import-export-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-export-annotations/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

XFDF adalah singkatan dari Format Data Formulir XML. Ini adalah format file berbasis XML. Format file ini digunakan untuk merepresentasikan data formulir atau anotasi yang terdapat dalam formulir PDF. XFDF dapat digunakan untuk berbagai tujuan yang berbeda, tetapi dalam kasus kami, dapat digunakan untuk mengirim atau menerima data formulir atau anotasi ke komputer atau server lain, atau dapat digunakan untuk mengarsipkan data formulir atau anotasi. Dalam artikel ini, kita akan melihat bagaimana Aspose.Pdf.Facades mempertimbangkan konsep ini dan bagaimana kita dapat mengimpor dan mengekspor data anotasi ke file XFDF.

## Mengimpor dan Mengekspor Anotasi ke XFDF

[Aspose.PDF for .NET](/pdf/net/) adalah komponen kaya fitur ketika datang untuk mengedit dokumen PDF. Seperti yang kita ketahui, XFDF adalah aspek penting dari manipulasi formulir PDF, [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) dalam [Aspose.PDF for .NET](/pdf/net/) telah mempertimbangkan ini dengan baik, dan telah menyediakan metode untuk mengimpor dan mengekspor data anotasi ke file XFDF.

Kelas [PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) berisi dua metode untuk bekerja dengan impor dan ekspor anotasi ke file XFDF. Metode [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/exportannotationsxfdf/index) menyediakan fungsionalitas untuk mengekspor anotasi dari dokumen PDF ke file XFDF, sementara metode [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/importannotationfromxfdf/index) memungkinkan Anda untuk mengimpor anotasi dari file XFDF yang ada. Untuk mengimpor atau mengekspor anotasi, kita perlu menentukan jenis anotasi. Kita dapat menentukan jenis ini dalam bentuk enumerasi dan kemudian mengoper enumerasi ini sebagai argumen ke salah satu metode ini. Dengan cara ini, anotasi dari jenis yang ditentukan hanya akan diimpor atau diekspor ke file XFDF.

Potongan kode berikut menunjukkan kepada Anda bagaimana cara mengimpor anotasi ke file XFDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    // Sources of PDF with annotations           
    var sources = new string[] { dataDir + "ImportAnnotations.pdf" };
            
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "input.pdf");
        annotationEditor.ImportAnnotations(sources);
        // Save PDF document
        annotationEditor.Save(dataDir + "ImportAnnotations_out.pdf");
    }
}
```

Potongan kode berikut menjelaskan bagaimana mengimpor/mengeskpor anotasi ke file XFDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportExportXFDF01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "ExportAnnotations.pdf");
        using (FileStream xmlOutputStream = File.OpenWrite(dataDir + "exportannotations_out.xfdf"))
        {
            annotationEditor.ExportAnnotationsToXfdf(xmlOutputStream);
        }

        // Create PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            document.Pages.Add();
            // Bind PDF document
            annotationEditor.BindPdf(document);
            annotationEditor.ImportAnnotationsFromXfdf(File.OpenRead(dataDir + "exportannotations_out.xfdf"));
            // Save PDF document
            annotationEditor.Save(dataDir + "ImportedAnnotation_out.pdf");
        }
    }
}
```

Dengan cara ini, anotasi dari jenis yang ditentukan hanya akan diimpor atau diekspor ke file XFDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportExportXFDF02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();
    
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "ExportAnnotations.pdf");

        // Export annotations
        using (FileStream xmlOutputStream = File.OpenWrite(dataDir + "exportannotations_out.xfdf"))
        {
            var annotationTypes = new[] {AnnotationType.FreeText, AnnotationType.Text};
            annotationEditor.ExportAnnotationsXfdf(xmlOutputStream, 1, 5, annotationTypes);
        }

        // Import annotations
        using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
        {
            // Add page
            document.Pages.Add();
            // Bind PDF document
            annotationEditor.BindPdf(document);
            annotationEditor.ImportAnnotationsFromXfdf(File.OpenRead(dataDir + "annotations.xfdf"));
            // Save PDF document
            annotationEditor.Save(dataDir + "ImportedAnnotation_XFDF02_out.pdf");
        }
    }
}
```