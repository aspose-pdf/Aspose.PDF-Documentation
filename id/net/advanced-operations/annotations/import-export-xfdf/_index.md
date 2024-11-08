---
title: Impor dan Ekspor Anotasi ke XFDF
linktitle: Impor dan Ekspor Anotasi ke XFDF
type: docs
weight: 40
url: /id/net/import-export-xfdf/
description: Anda dapat mengimpor dan mengekspor anotasi dalam format XFDF dengan C# dan perpustakaan Aspose.PDF untuk .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Impor dan Ekspor Anotasi ke XFDF",
    "alternativeHeadline": "Metode untuk mengimpor dan mengekspor data anotasi ke file XFDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, impor ekspor ke XFDF",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dok Aspose.PDF",
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
    "url": "/net/import-export-xfdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-export-xfdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Anda dapat mengimpor dan mengekspor anotasi dalam format XFDF dengan C# dan perpustakaan Aspose.PDF untuk .NET."
}
</script>

{{% alert color="primary" %}}

XFDF adalah singkatan dari XML Forms Data Format. Ini adalah format file berbasis XML. Format file ini digunakan untuk merepresentasikan data formulir atau anotasi yang terkandung dalam formulir PDF. XFDF dapat digunakan untuk berbagai tujuan, namun dalam kasus kita, dapat digunakan untuk mengirim atau menerima data formulir atau anotasi ke komputer atau server lain, atau dapat digunakan untuk mengarsipkan data formulir atau anotasi. Dalam artikel ini, kita akan melihat bagaimana Aspose.Pdf.Facades telah mempertimbangkan konsep ini dan bagaimana kita dapat mengimpor dan mengekspor data anotasi ke file XFDF.

{{% /alert %}}

**Aspose.PDF for .NET** adalah komponen yang kaya fitur dalam hal mengedit dokumen PDF. Seperti kita ketahui XFDF adalah aspek penting dari manipulasi formulir PDF, namespace Aspose.Pdf.Facades di Aspose.PDF for .NET telah mempertimbangkan ini dengan sangat baik, dan telah menyediakan metode untuk mengimpor dan mengekspor data anotasi ke file XFDF.

Kelas [PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) berisi dua metode untuk bekerja dengan impor dan ekspor anotasi ke file XFDF.
Kelas [PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) berisi dua metode untuk bekerja dengan impor dan ekspor anotasi ke file XFDF.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

Potongan kode berikut menunjukkan cara mengekspor anotasi ke file XFDF:

```csharp
using Aspose.Pdf.Annotations;
using Aspose.Pdf.Facades;
using System.IO;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleAnnotationImportExport
    {
        // Jalur ke direktori dokumen.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        /// <summary>
        /// Mengimpor anotasi dari file XFDF
        /// File Format Data Formulir XML (XFDF) dibuat oleh Adobe Acrobat, aplikasi pembuat PDF;
        /// menyimpan deskripsi elemen formulir halaman dan nilai-nilainya, seperti nama dan nilai untuk
        /// bidang teks; digunakan untuk menyimpan data formulir yang dapat diimpor ke dalam dokumen PDF.
        /// Anda dapat mengimpor data anotasi dari file XFDF ke PDF menggunakan
        /// metode ImportAnnotationsFromXfdf di kelas PdfAnnotationEditor.
        /// </summary>       

        public static void ExportAnnotationXFDF()
        {
            // Buat objek PdfAnnotationEditor
            PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();

            // Mengikat dokumen PDF ke Editor Anotasi
            AnnotationEditor.BindPdf(Path.Combine(_dataDir, "AnnotationDemo1.pdf"));

            // Ekspor anotasi
            var fileStream = File.OpenWrite(Path.Combine(_dataDir, "exportannotations.xfdf"));
            var annotType = new AnnotationType[] { AnnotationType.Line, AnnotationType.Square };
            AnnotationEditor.ExportAnnotationsXfdf(fileStream, 1, 1, annotType);
            fileStream.Flush();
            fileStream.Close();
        }
        //...
    }
}
```
Potongan kode berikut menggambarkan cara mengimpor anotasi ke file XFDF:

```csharp
public static void ImportAnnotationXFDF()
{
    // Buat objek PdfAnnotationEditor
    PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
    // Buat dokumen PDF baru
    var document = new Document();
    document.Pages.Add();
    AnnotationEditor.BindPdf(document);

    var exportFileName = Path.Combine(_dataDir, "exportannotations.xfdf");
    if (!File.Exists(exportFileName))
        ExportAnnotationXFDF();

    // Impor anotasi
    AnnotationEditor.ImportAnnotationsFromXfdf(exportFileName);

    // Simpan PDF keluaran
    document.Save(Path.Combine(_dataDir, "AnnotationDemo2.pdf"));
}
```

## Cara lain untuk ekspor/impor anotasi sekaligus

Pada kode di bawah ini, metode ImportAnnotations memungkinkan impor anotasi langsung dari dokumen PDF lain.

```csharp
        /// <summary>
        /// Metode ImportAnnotations memungkinkan impor anotasi langsung dari dokumen PDF lain
        /// </summary>

        public static void ImportAnnotationFromPDF()
        {
            // Buat objek PdfAnnotationEditor
            PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
            // Buat dokumen PDF baru
            var document = new Document();
            document.Pages.Add();
            AnnotationEditor.BindPdf(document);
            var exportFileName = Path.Combine(_dataDir, "exportannotations.xfdf");
            if (!File.Exists(exportFileName))
                ExportAnnotationXFDF();

            // Annotation Editor memungkinkan impor anotasi dari beberapa dokumen PDF,
            // tetapi dalam contoh ini, kita hanya menggunakan satu.
            AnnotationEditor.ImportAnnotations(new[] { Path.Combine(_dataDir, "AnnotationDemo1.pdf") });

            // Simpan PDF keluaran
            document.Save(Path.Combine(_dataDir, "AnnotationDemo3.pdf"));
        }
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Perpustakaan Aspose.PDF untuk .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
                "contactType": "penjualan",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "penjualan",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "penjualan",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Perpustakaan Manipulasi PDF untuk .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

