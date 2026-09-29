---
title: Tambahkan Aksi Dokumen
linktitle: Tambahkan Aksi Dokumen
type: docs
weight: 10
url: /id/java/add-document-action/
description: Pelajari cara menambahkan aksi document-open ke PDF dalam Java menggunakan facade `PdfContentEditor` di Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Tambahkan aksi document-open ke PDF dalam Java
Abstract: Artikel ini menunjukkan cara mengikat PDF, melampirkan aksi JavaScript ke peristiwa document-open, dan menyimpan dokumen yang diperbarui menggunakan facade `PdfContentEditor` di Aspose.PDF for Java.
---
## Tambahkan aksi document-open

1. Ikat PDF sumber ke `PdfContentEditor` fasad.
2. Panggil `addDocumentAdditionalAction(...)` dengan `DOCUMENT_OPEN` peristiwa dan teks aksi JavaScript.
3. Simpan dokumen PDF yang diperbarui.

```java
public static void addDocumentAction(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addDocumentAdditionalAction(PdfContentEditor.DOCUMENT_OPEN, "app.alert('Document opened with PdfContentEditor action');");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
