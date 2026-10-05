---
title: "Mengekspor ke XML"
linktitle: "Mengekspor ke XML"
type: docs
weight: 40
url: /id/java/export-to-xml/
description: "Pelajari cara mengekspor data formulir PDF ke XML dalam Java menggunakan fasad Form di Aspose.PDF."
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Mengekspor data AcroForm ke XML dalam Java"
Abstract: "Artikel ini menunjukkan cara mengikat formulir PDF dan mengekspor nilai bidangnya ke aliran XML dengan fasad Form di Aspose.PDF for Java."
---
Gunakan `FormExamples.exportXml(...)` untuk menyimpan data bidang formulir sebagai XML.

```java
public static void exportXml(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream outputStream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXml(outputStream);
    } finally {
        form.close();
    }
}
```
