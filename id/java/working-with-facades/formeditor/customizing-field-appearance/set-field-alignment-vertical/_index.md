---
title: Atur Penjajaran Bidang Vertikal
linktitle: Atur Penjajaran Bidang Vertikal
type: docs
weight: 30
url: /id/java/set-field-alignment-vertical/
description: Pelajari cara mengatur penjajaran vertikal untuk bidang formulir PDF di Java menggunakan fasad FormEditor di Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Atur penjajaran vertikal untuk bidang formulir PDF di Java
Abstract: Artikel ini menunjukkan cara mengikat PDF yang ada, mengatur penjajaran bidang vertikal, dan menyimpan dokumen yang diperbarui menggunakan fasad FormEditor di Aspose.PDF for Java.
---
## Atur penjajaran bidang vertikal

1. Ikat PDF sumber ke `FormEditor` fasad.
2. Panggil `setFieldAlignmentV(...)` untuk bidang target dan konstanta penyelarasan vertikal yang diinginkan.
3. Simpan dokumen yang telah diperbarui.

```java
public static void setFieldAlignmentVertical(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAlignmentV("First Name", FormFieldFacade.ALIGN_BOTTOM);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
