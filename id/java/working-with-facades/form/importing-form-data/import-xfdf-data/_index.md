---
title: "Mengimpor data XFDF"
linktitle: "Mengimpor data XFDF"
type: docs
weight: 20
url: /id/java/import-xfdf-data/
description: Pelajari cara mengimpor data formulir XFDF ke dalam formulir PDF dengan Java menggunakan fasad Form di Aspose.PDF.
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Mengimpor data AcroForm dari XFDF dengan Java"
Abstract: Artikel ini menunjukkan cara mengaitkan formulir PDF, mengimpor nilai bidang dari aliran XFDF, dan menyimpan dokumen yang diperbarui dengan fasad Form di Aspose.PDF for Java.
---
Gunakan `FormExamples.importXfdf(...)` untuk mengisi formulir dari data XFDF.

```java
public static void importXfdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream inputStream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXfdf(inputStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
