---
title: Impor Data FDF
linktitle: Impor Data FDF
type: docs
weight: 10
url: /id/java/import-fdf-data/
description: Pelajari cara mengimpor data formulir FDF ke dalam formulir PDF dengan Java menggunakan façade Form di Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Impor data AcroForm dari FDF dengan Java
Abstract: Artikel ini menunjukkan cara mengikat formulir PDF, mengimpor nilai bidang dari aliran FDF, dan menyimpan dokumen yang diperbarui dengan façade Form di Aspose.PDF for Java.
---
Gunakan `FormExamples.importFdf(...)` untuk menerapkan nilai bidang dari file FDF.

```java
public static void importFdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream inputStream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importFdf(inputStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
