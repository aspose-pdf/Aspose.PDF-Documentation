---
title: "Mengatur penjajaran Field"
linktitle: "Mengatur penjajaran Field"
type: docs
weight: 20
url: /id/java/set-field-alignment/
description: "Pelajari cara mengatur penjajaran teks horizontal untuk bidang formulir PDF di Java menggunakan fasad FormEditor di Aspose.PDF."
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Mengatur penjajaran bidang formulir PDF di Java"
Abstract: "Artikel ini menunjukkan cara mengaitkan PDF yang ada, mengatur penjajaran bidang horizontal, dan menyimpan dokumen yang diperbarui menggunakan fasad FormEditor di Aspose.PDF for Java."
---
## Mengatur penjajaran bidang horizontal

1. Hubungkan PDF sumber ke fasad `FormEditor`.
2. Panggil `setFieldAlignment(...)` untuk bidang target dan konstanta perataan yang diinginkan.
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
