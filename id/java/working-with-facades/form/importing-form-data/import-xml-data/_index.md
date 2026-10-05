---
title: "Mengimpor data XML"
linktitle: "Mengimpor data XML"
type: docs
weight: 40
url: /id/java/import-xml-data/
description: Pelajari cara mengimpor data formulir XML ke dalam formulir PDF dengan Java menggunakan fasad Form di Aspose.PDF.
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Mengimpor data AcroForm dari XML di Java"
Abstract: Artikel ini menunjukkan cara mengaitkan formulir PDF, mengimpor nilai bidang dari aliran XML, dan menyimpan dokumen yang diperbarui dengan fasad Form di Aspose.PDF for Java.
---
Gunakan `FormExamples.importXml(...)` untuk mengisi formulir dari data XML.

```java
public static void importXml(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream inputStream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXml(inputStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
