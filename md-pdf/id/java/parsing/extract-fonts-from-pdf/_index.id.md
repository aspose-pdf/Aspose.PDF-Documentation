---
title: Ekstrak font dari PDF 
linktitle: Ekstrak font
type: docs
weight: 30
url: /java/extract-fonts-from-pdf/
description: Cara mengekstrak font dari PDF menggunakan Aspose.PDF untuk Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Jika Anda ingin mendapatkan semua font dari dokumen PDF, Anda dapat menggunakan metode `Document.IDocumentFontUtilities.getAllFonts()` yang disediakan dalam kelas Document. Silakan cek potongan kode berikut untuk mendapatkan semua font dari dokumen PDF yang sudah ada:

```java
public static void Extract_Fonts() throws FileNotFoundException
{
    // Jalur ke direktori dokumen.
    String filePath = "<... masukkan nama file ...>";
    
    // Memuat dokumen PDF
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.Font[] fonts = pdfDocument.getFontUtilities().getAllFonts();

    for (com.aspose.pdf.Font font : fonts)
    {
        font.save(new FileOutputStream(font.getFontName()));
    }
}
```