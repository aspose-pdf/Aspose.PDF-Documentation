---
title: "Mengekspor ke XFDF"
linktitle: "Mengekspor ke XFDF"
type: docs
weight: 20
url: /id/java/export-to-xfdf/
description: Pelajari cara mengekspor data bidang formulir PDF ke XFDF dalam Java menggunakan fasad Form di Aspose.PDF.
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Mengekspor data AcroForm ke XFDF dalam Java"
Abstract: Artikel ini menunjukkan cara mengikat formulir PDF dan mengekspor nilai bidangnya ke aliran XFDF dengan fasad Form di Aspose.PDF for Java.
---
Gunakan `FormExamples.exportXfdf(...)` untuk menulis data bidang formulir sebagai XFDF.

```java
public static void exportXfdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream outputStream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXfdf(outputStream);
    } finally {
        form.close();
    }
}
```
