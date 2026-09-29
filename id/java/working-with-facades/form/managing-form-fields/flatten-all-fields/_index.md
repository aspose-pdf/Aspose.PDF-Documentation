---
title: Ratakan Semua Field
linktitle: Ratakan Semua Field
type: docs
weight: 10
url: /id/java/flatten-all-fields/
description: Pelajari cara meratakan semua field formulir PDF di Java menggunakan Form facade di Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Konversi semua field formulir interaktif menjadi konten statis di Java
Abstract: Artikel ini menunjukkan cara mengikat formulir PDF, meratakan setiap field formulir, dan menyimpan dokumen yang diperbarui dengan Form facade di Aspose.PDF for Java.
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
