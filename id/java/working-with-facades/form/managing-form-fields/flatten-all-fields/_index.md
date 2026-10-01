---
title: "Meratakan semua Field"
linktitle: "Meratakan semua Field"
type: docs
weight: 10
url: /id/java/flatten-all-fields/
description: "Pelajari cara meratakan semua bidang formulir PDF di Java menggunakan fasad Form di Aspose.PDF."
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Mengonversi semua bidang formulir interaktif menjadi konten statis di Java"
Abstract: "Artikel ini menunjukkan cara mengikat formulir PDF, meratakan setiap bidang formulir, dan menyimpan dokumen yang diperbarui dengan fasad Form di Aspose.PDF for Java."
---
Gunakan `FormExamples.flattenAllFields(...)` ketika Anda perlu mengonversi semua bidang interaktif menjadi konten halaman statis.

```java
public static void flattenAllFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.flattenAllFields();
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
