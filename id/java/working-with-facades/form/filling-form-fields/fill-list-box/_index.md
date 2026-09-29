---
title: Isi List Box
linktitle: Isi List Box
type: docs
weight: 40
url: /id/java/fill-list-box/
description: Pelajari cara mengisi bidang list box dalam formulir PDF dengan Java menggunakan facade Form di Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Setel nilai bidang list box dalam formulir PDF dengan Java
Abstract: Artikel ini menunjukkan cara mengaitkan formulir PDF, menetapkan nilai bidang list box, dan menyimpan dokumen yang diperbarui dengan facade Form di Aspose.PDF for Java.
---
Gunakan `FormExamples.fillListBoxFields(...)` untuk mengisi bidang kotak daftar.

```java
public static void fillListBoxFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("favorite_colors", "Red");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
