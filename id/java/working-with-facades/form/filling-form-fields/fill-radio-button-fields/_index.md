---
title: Isi Bidang Tombol Radio
linktitle: Isi Bidang Tombol Radio
type: docs
weight: 30
url: /id/java/fill-radio-button-fields/
description: Pelajari cara memilih nilai tombol radio dalam formulir PDF dengan Java menggunakan facade Form di Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Pilih opsi bidang tombol radio di Java
Abstract: Artikel ini menunjukkan cara mengikat formulir PDF, memilih opsi tombol radio berdasarkan indeks, dan menyimpan dokumen yang diperbarui dengan facade Form di Aspose.PDF for Java.
---
Gunakan `FormExamples.fillRadioButtonFields(...)` untuk memilih opsi tombol radio.

```java
public static void fillRadioButtonFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("gender", 0);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
