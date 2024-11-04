---
title: Render WebForms DataGridView ke PDF
linktitle: Render WebForms DataGridView ke PDF
type: docs
weight: 20
url: /net/render-webforms-datagridview-to-pdf/
description: Contoh ini menunjukkan bagaimana menggunakan perpustakaan Aspose.PDF untuk me-render WebForm ke PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Bagaimana mengekspor WebForm ke PDF menggunakan Aspose.PDF/Aspose.HTML

### Pendahuluan

Secara umum, untuk mengonversi WebForm ke dokumen PDF menggunakan alat tambahan. Contoh ini menunjukkan bagaimana menggunakan perpustakaan Aspose.PDF untuk me-render WebForm ke PDF. Aspose Export GridView To Pdf Control juga termasuk dalam contoh ini untuk menunjukkan cara me-render _GridView control ke dokumen PDF._

## Bagaimana me-render WebForm ke PDF

Ide asli untuk me-render WebForm ke PDF adalah dengan membuat kelas helper, yang diwarisi dari [System.Web.UI.Page](https://msdn.microsoft.com/en-US/library/System.Web.UI.Page.aspx), dan menimpa metode Render.</em></p>

```csharp
void Render(HtmlTextWriter writer)
{
    if (RenderToPDF)
    {
        // me-render halaman web untuk dokumen PDF
    }
    else
    {
        // me-render halaman web di browser
        base.Render(writer);
    }
}
```
Ada dua alat Aspose yang dapat digunakan untuk merender HTML ke PDF:

- Aspose.PDF untuk .NET
- Aspose Export GridView control (berbasis Aspose.PDF)

## Berkas Sumber

Dalam contoh ini kami memiliki 2 laporan demo.

- _Default.aspx_ menunjukkan ekspor ke PDF menggunakan Aspose.PDF
- _Report2.aspx_ menunjukkan ekspor ke PDF menggunakan Aspose Export GridView control (berbasis Aspose.PDF)

## Berkas Tambahan

`Helpers\PdfPage.cs` - berisi kelas bantuan, yang menunjukkan cara menggunakan API Aspose.PDF.

Proyek Aspose.Pdf.GridViewExport berisi kontrol GridView yang diperluas untuk demonstrasi di `Report2.aspx`
