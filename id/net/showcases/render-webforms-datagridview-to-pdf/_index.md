---
title: Render WebForms DataGridView ke PDF
linktitle: Render WebForms DataGridView ke PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /id/net/render-webforms-datagridview-to-pdf/
description: Contoh ini menunjukkan cara menggunakan pustaka Aspose.PDF untuk merender WebForm ke PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Render WebForms DataGridView to PDF",
    "alternativeHeadline": "Effortlessly Convert WebForms DataGridView to PDF",
    "abstract": "Fitur ini memungkinkan konversi tanpa hambatan dari WebForms DataGridView ke PDF menggunakan pustaka Aspose.PDF for .NET. Fungsionalitas ini menyederhanakan proses ekspor data dengan mengintegrasikan kontrol ekspor GridView yang didedikasikan, memastikan rendering PDF berkualitas tinggi langsung dari aplikasi web. Sempurna untuk pengembang yang mencari solusi pembuatan dokumen yang efisien",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "266",
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
    "url": "/net/render-webforms-datagridview-to-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/render-webforms-datagridview-to-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Cara mengekspor WebForm ke PDF menggunakan Aspose.PDF/Aspose.HTML

### Pendahuluan

Secara umum, untuk mengonversi WebForm ke dokumen PDF menggunakan alat tambahan. Contoh ini menunjukkan cara menggunakan pustaka Aspose.PDF untuk merender WebForm ke PDF. Kontrol Aspose Export GridView To Pdf juga disertakan dalam contoh ini untuk menunjukkan cara merender _kontrol GridView ke dokumen PDF._

## Cara merender WebForm ke PDF

Ide asli untuk merender WebForm ke PDF adalah dengan membuat kelas pembantu, yang diwarisi dari [System.Web.UI.Page](https://msdn.microsoft.com/en-US/library/System.Web.UI.Page.aspx), dan menimpa metode Render.</em></p>

```csharp
void Render(HtmlTextWriter writer)
{
    if (RenderToPDF)
    {
        // render web page for PDF document
    }
    else
    {
        // render web page in browser
        base.Render(writer);
    }
}
```

Ada dua alat Aspose yang dapat digunakan untuk merender HTML ke PDF:

- Aspose.PDF for .NET.
- Kontrol Aspose Export GridView (berbasis Aspose.PDF).

## Berkas Sumber

Dalam contoh ini kami memiliki 2 laporan demo.

- _Default.aspx_ mendemonstrasikan ekspor ke PDF menggunakan Aspose.PDF.
- _Report2.aspx_ mendemonstrasikan ekspor ke PDF menggunakan kontrol Aspose Export GridView (berbasis Aspose.PDF).

## Berkas Tambahan

`Helpers\PdfPage.cs` - berisi kelas pembantu, yang menunjukkan cara menggunakan API Aspose.PDF.</em>

Proyek Aspose.Pdf.GridViewExport berisi kontrol GridView yang diperluas untuk demonstrasi di `Report2.aspx`