---
title: "Mengisi kolom kotak centang"
linktitle: "Mengisi kolom kotak centang"
type: docs
weight: 20
url: /id/java/fill-check-box-fields/
description: "Pelajari cara mengisi kolom kotak centang dalam formulir PDF dengan Java menggunakan fasad Form di Aspose.PDF."
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Mengatur nilai kolom kotak centang dalam formulir PDF dengan Java"
Abstract: "Artikel ini menunjukkan cara mengaitkan formulir PDF, mengatur kolom kotak centang berdasarkan nama, dan menyimpan dokumen yang diperbarui menggunakan fasad Form di Aspose.PDF for Java."
---
Gunakan `FormExamples.fillCheckBoxFields(...)` untuk mengatur nilai kotak centang dalam sebuah formulir.

```java
public static void fillCheckBoxFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("subscribe_newsletter", "Yes");
        form.fillField("accept_terms", "Yes");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
