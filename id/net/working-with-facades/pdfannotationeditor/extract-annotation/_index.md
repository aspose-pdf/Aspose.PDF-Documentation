---
title: Ekstrak Anotasi dari PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /id/net/extract-annotation/
description: Bagian ini menjelaskan cara mengekstrak anotasi dari file PDF ke XFDF dengan Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Annotations from PDF",
    "alternativeHeadline": "Effortlessly Extract PDF Annotations to XFDF Format",
    "abstract": "Buka potensi dokumen PDF Anda dengan fitur Ekstrak Anotasi baru, yang memungkinkan ekstraksi anotasi ke format XFDF dengan menggunakan Aspose.PDF for .NET. Fungsionalitas ini memungkinkan pengambilan jenis anotasi tertentu dengan mudah, meningkatkan manajemen dokumen dan efisiensi kolaborasi. Temukan cara untuk menyederhanakan alur kerja PDF Anda dengan mengekstrak dan menyimpan data anotasi penting dengan mudah",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "254",
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
    "url": "/net/extract-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

[ExtractAnnotations](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) metode memungkinkan Anda untuk mengekstrak anotasi dari file PDF. Untuk mengekstrak anotasi, Anda perlu membuat objek [PdfAnnotationEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfannotationeditor) dan mengikat file PDF menggunakan metode [BindPdf](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.facade/bindpdf/methods/3). Setelah itu, Anda perlu membuat enumerasi jenis anotasi yang ingin Anda ekstrak dari file PDF.

Anda kemudian dapat menggunakan metode [ExtractAnnotations](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) untuk mengekstrak anotasi ke dalam ArrayList. Setelah itu, Anda dapat melakukan loop melalui daftar ini dan mendapatkan anotasi individu. Dan akhirnya, simpan file PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/id/net/aspose.pdf/document/methods/save) dari objek [PdfAnnotationEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfannotationeditor). Potongan kode berikut menunjukkan kepada Anda cara mengekstrak anotasi dari file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AnnotationsInput.pdf"))
    {
        using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
        {
            // Bind PDF document
            annotationEditor.BindPdf(document);
            // Extract annotations
            var annotationTypes = new[] { Aspose.Pdf.Annotations.AnnotationType.FreeText, Aspose.Pdf.Annotations.AnnotationType.Text };
            var annotations = annotationEditor.ExtractAnnotations(1, 2, annotationTypes);
            foreach (var annotation in annotations)
            {
                Console.WriteLine(annotation.Contents);
            }
        }
    }
}
```