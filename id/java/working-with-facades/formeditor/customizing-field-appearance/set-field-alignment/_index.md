---
title: Atur Penjajaran Field
linktitle: Atur Penjajaran Field
type: docs
weight: 20
url: /id/java/set-field-alignment/
description: Pelajari cara mengatur penjajaran teks horizontal untuk field formulir PDF di Java menggunakan facade FormEditor di Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Atur penjajaran field formulir PDF di Java
Abstract: Artikel ini menunjukkan cara mengaitkan PDF yang ada, mengatur penjajaran field horizontal, dan menyimpan dokumen yang diperbarui menggunakan facade FormEditor di Aspose.PDF for Java.
---
## Atur penjajaran field horizontal

1. Hubungkan PDF sumber ke `FormEditor` fasad.
2. Panggilan `setFieldAlignment(...)` untuk bidang target dan konstanta perataan yang diinginkan.
3. Simpan dokumen yang diperbarui.

```java
public static void setFieldAlignment(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAlignment("First Name", FormFieldFacade.ALIGN_CENTER);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
