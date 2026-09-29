---
title: Ganti Nama Bidang Form
linktitle: Ganti Nama Bidang Form
type: docs
weight: 30
url: /id/java/rename-form-fields/
description: Pelajari cara mengganti nama bidang formulir PDF di Java menggunakan fasad Form dalam Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Ganti nama bidang Form dalam dokumen PDF dengan Java
Abstract: Artikel ini menunjukkan cara mengikat formulir PDF, mengganti nama bidang yang ada, dan menyimpan dokumen yang diperbarui dengan fasad Form dalam Aspose.PDF for Java.
---
Gunakan `FormExamples.renameFormFields(...)` untuk mengganti nama bidang dalam formulir PDF interaktif.

```java
public static void renameFormFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.renameField("First Name", "NewFirstName");
        form.renameField("Last Name", "NewLastName");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
