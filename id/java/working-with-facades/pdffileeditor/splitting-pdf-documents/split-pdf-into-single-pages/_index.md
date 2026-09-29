---
title: Bagi PDF menjadi Halaman Tunggal
linktitle: Bagi PDF menjadi Halaman Tunggal
type: docs
weight: 30
url: /id/java/split-pdf-into-single-pages/
description: Pisahkan PDF menjadi file output satu halaman dalam Java dengan facade PdfFileEditor.
lastmod: "2026-09-29"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ekspor setiap halaman PDF ke file terpisah dengan Java
Abstract: Pelajari cara membagi PDF menjadi file satu halaman dengan Aspose.PDF for Java. Contoh Java tersebut menggunakan PdfFileEditor untuk menulis setiap halaman ke PDF output terpisah berdasarkan pola nama file.
---
## Bagi PDF menjadi halaman tunggal

Gunakan alur kerja ini ketika setiap halaman sumber harus menjadi file PDF terpisah.

### Langkah

1. Buat `PdfFileEditor` instansi.
2. Siapkan pola file output yang menyertakan placeholder halaman seperti `%NUM%`.
3. Panggil `splitToPages` dengan file sumber dan pola output.
4. Simpan file satu halaman yang dihasilkan.

```java
public static void splitPdfIntoSinglePages(Path inputFile, Path outputFilePattern) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToPages(inputFile.toString(), outputFilePattern.toString());
}
```
