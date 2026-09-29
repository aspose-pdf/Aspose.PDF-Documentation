---
title: Tambahkan Lampiran
linktitle: Tambahkan Lampiran
type: docs
weight: 10
url: /id/java/add-attachment/
description: Pelajari cara melampirkan file eksternal ke dokumen PDF dalam Java menggunakan facade PdfContentEditor di Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Tambahkan lampiran file ke PDF dalam Java
Abstract: Artikel ini menunjukkan cara mengikat PDF, membuka lampiran sebagai stream, menambahkan lampiran dokumen dengan deskripsi, dan menyimpan file yang diperbarui menggunakan facade PdfContentEditor di Aspose.PDF for Java.
---
## Tambahkan lampiran dokumen

1. Lampirkan PDF sumber ke `PdfContentEditor` fasad.
2. Buka file lampiran sebagai aliran masukan.
3. Panggil `addDocumentAttachment(...)` dengan stream, nama file, dan deskripsi.
4. Simpan dokumen PDF yang diperbarui.

```java
public static void addAttachment(Path inputFile, Path attachmentFile, Path outputFile) throws Exception {
    PdfContentEditor editor = new PdfContentEditor();
    try (InputStream attachmentStream = Files.newInputStream(attachmentFile)) {
        editor.bindPdf(inputFile.toString());
        editor.addDocumentAttachment(attachmentStream, attachmentFile.getFileName().toString(), "Sample attachment.");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
