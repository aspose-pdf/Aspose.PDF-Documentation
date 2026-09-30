---
title: Dekorasi Field
linktitle: Dekorasi Field
type: docs
weight: 10
url: /id/java/decorate-field/
description: "Pelajari cara menghias bidang formulir PDF dengan warna dan perataan dalam Java menggunakan fasad FormEditor di Aspose.PDF."
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Menghias bidang formulir PDF dalam Java"
Abstract: "Artikel ini menunjukkan cara mengikat PDF yang ada, mengonfigurasi FormFieldFacade dengan warna dan perataan, menghias sebuah bidang, dan menyimpan dokumen yang diperbarui menggunakan fasad FormEditor di Aspose.PDF for Java."
---
## Menghias sebuah bidang

1. Ikat PDF sumber ke fasad `FormEditor`.
2. Konfigurasikan `FormFieldFacade` dengan warna dan perataan yang diperlukan.
3. Berikan fasad ke editor dan panggil `decorateField(...)`.
4. Simpan dokumen yang diperbarui.

```java
public static void decorateField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        FormFieldFacade facade = new FormFieldFacade();
        facade.setBackgroundColor(Color.RED);
        facade.setTextColor(Color.BLUE);
        facade.setBorderColor(Color.GREEN);
        facade.setAlignment(FormFieldFacade.ALIGN_CENTER);
        editor.setFacade(facade);
        editor.decorateField("First Name");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
