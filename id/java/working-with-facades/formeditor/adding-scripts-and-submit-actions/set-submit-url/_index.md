---
title: "Mengatur URL kirim"
linktitle: "Mengatur URL kirim"
type: docs
weight: 30
url: /id/java/set-submit-url/
description: Pelajari cara mengatur URL kirim untuk tombol formulir PDF di Java menggunakan façade FormEditor di Aspose.PDF.
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Mengonfigurasi URL kirim formulir PDF di Java"
Abstract: Artikel ini menunjukkan cara mengikat PDF yang ada, mengatur URL kirim dan flag kirim untuk bidang tombol, dan menyimpan dokumen yang diperbarui menggunakan façade FormEditor di Aspose.PDF for Java.
---
## Mengatur URL kirim

1. Ikat PDF sumber ke fasad `FormEditor`.
2. Panggil `setSubmitUrl(...)` untuk bidang tombol.
3. Terapkan flag submit untuk format pengiriman.
4. Simpan dokumen yang diperbarui.

```java
public static void setSubmitUrl(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setSubmitUrl("Script_Demo_Button", "http://www.example.com/submit");
        editor.setSubmitFlag("Script_Demo_Button", SubmitFormFlag.Xfdf);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
