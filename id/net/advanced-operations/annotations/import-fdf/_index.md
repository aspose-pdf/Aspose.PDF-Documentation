---
title: Impor anotasi format FDF ke PDF melalui C#
linktitle: Impor anotasi format FDF ke PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /id/net/import-fdf/
description: Gunakan metode Form.ImportFdf() yang ada atau tambahkan PdfAnnotationEditor.ImportAnnotationsFromFdf() untuk mengimpor anotasi format FDF ke PDF dengan Aspose.PDF for .NET.
lastmod: "2024-09-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import FDF format annotations to PDF via C#",
    "alternativeHeadline": "Effortlessly Import FDF Annotations to PDF with C#",
    "abstract": "Impor anotasi format FDF ke file PDF dengan lancar menggunakan Aspose.PDF for .NET, meningkatkan kemampuan manajemen PDF Anda. Dengan metode Form.ImportFdf() dan PdfAnnotationEditor.ImportAnnotationsFromFdf(), Anda dapat dengan mudah mengintegrasikan data formulir dan komentar dari file FDF ringan ke dalam dokumen PDF Anda, menyederhanakan proses pengiriman data dan anotasi.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Import FDF, FDF format annotations, PDF annotations, Aspose.PDF for .NET, Form.ImportFdf(), PdfAnnotationEditor, import annotations from FDF, lightweight PDF, fill form fields, exchange annotations",
    "wordcount": "350",
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
    "url": "/net/import-fdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-fdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

{{% alert color="primary" %}}

FDF (Format Data Formulir) adalah format file yang menyimpan dan mentransmisikan data formulir dan anotasi dalam dokumen PDF. Ini adalah versi PDF ringan yang hanya berisi nilai bidang formulir atau komentar, tanpa konten lengkap dari file PDF asli. File FDF sering digunakan saat mengirimkan data formulir ke server, atau saat bertukar anotasi tanpa perlu mengirim seluruh file PDF. Mereka dapat diimpor kembali ke dalam PDF untuk mengisi bidang formulir atau menerapkan komentar.

{{% /alert %}}

[PDFAnnotationEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfannotationeditor/) kelas berisi metode untuk bekerja dengan impor anotasi dari file FDF. Metode [PdfAnnotationEditor.ImportAnnotationsFromFdf](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfannotationeditor/importannotationsfromfdf/) menyediakan fungsionalitas untuk mengimpor anotasi dari dokumen FDF ke file PDF.

Selain itu, [Kelas Form](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/form/) menyertakan metode [Form.ImportFdf](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/form/importfdf/) - mengimpor konten bidang dari file FDF dan menempatkannya ke dalam PDF baru.

Potongan kode berikut menunjukkan kepada Anda cara Mengimpor anotasi format FDF ke PDF dengan metode Form.ImportFdf():

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportFDFByForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form(dataDir + "input.pdf"))
    {
        // Open FDF file
        using (var fdfInputStream = new FileStream(dataDir + "student.fdf", FileMode.Open))
        {
            form.ImportFdf(fdfInputStream);
        }
        // Save PDF document
        form.Save(dataDir + "ImportDataFromPdf_Form_out.pdf");
    }
}
```

Potongan kode berikut menunjukkan cara mengimpor anotasi format FDF ke PDF dengan metode PdfAnnotationEditor.ImportAnnotationsFromFdf():

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportFdfByPdfAnnotationEditor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        var editor = new Aspose.Pdf.Facades.PdfAnnotationEditor();
        // Bind PDF document
        editor.BindPdf(dataDir + "input.pdf");
        editor.ImportAnnotationsFromFdf(dataDir + "student.fdf");
        // Save PDF document
        editor.Save(dataDir + "ImportDataFromPdf_AnnotationEditor_out.pdf");  
    }
}
```