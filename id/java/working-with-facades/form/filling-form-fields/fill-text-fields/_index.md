---
title: Isi Bidang Teks
linktitle: Isi Bidang Teks
type: docs
weight: 10
url: /id/java/fill-text-fields/
description: Pelajari cara mengisi bidang teks dalam formulir PDF dengan Java menggunakan fasad Form di Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Isi bidang formulir teks dalam PDF dengan Java
Abstract: Artikel ini menunjukkan cara mengikat formulir PDF, mengatur nilai bidang teks berdasarkan nama, dan menyimpan dokumen yang diperbarui dengan fasad Form di Aspose.PDF for Java.
---
Gunakan `FormExamples.fillTextFields(...)` untuk mengisi bidang formulir berbasis teks.

```java
public static void fillTextFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("name", "John Doe");
        form.fillField("address", "123 Main St, Anytown, USA");
        form.fillField("email", "john.doe@example.com");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
