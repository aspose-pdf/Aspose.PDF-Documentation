---
title: Ekspor ke XML
linktitle: Ekspor ke XML
type: docs
weight: 40
url: /id/java/export-to-xml/
description: Pelajari cara mengekspor data formulir PDF ke XML dalam Java menggunakan facade Form di Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Ekspor data AcroForm ke XML dalam Java
Abstract: Artikel ini menunjukkan cara mengikat formulir PDF dan mengekspor nilai bidangnya ke aliran XML dengan facade Form di Aspose.PDF for Java.
---
Gunakan `FormExamples.exportXml(...)` untuk menyimpan data field formulir sebagai XML.

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
