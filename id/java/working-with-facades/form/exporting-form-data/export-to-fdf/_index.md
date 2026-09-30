---
title: "Mengekspor ke FDF"
linktitle: "Mengekspor ke FDF"
type: docs
weight: 10
url: /id/java/export-to-fdf/
description: "Pelajari cara mengekspor nilai bidang formulir PDF ke FDF dalam Java menggunakan fasad Form di Aspose.PDF."
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Mengekspor data AcroForm ke FDF dalam Java"
Abstract: "Artikel ini menunjukkan cara mengikat formulir PDF dan mengekspor data bidangnya ke aliran FDF dengan fasad Form di Aspose.PDF for Java."
---
Gunakan `FormExamples.exportFdf(...)` ketika Anda perlu menyerialkan data bidang AcroForm sebagai FDF.

```java
public static void exportFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream outputStream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(outputStream);
    } finally {
        form.close();
    }
}
```
