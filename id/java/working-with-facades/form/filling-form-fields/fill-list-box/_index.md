---
title: "Mengisi List Box"
linktitle: "Mengisi List Box"
type: docs
weight: 40
url: /id/java/fill-list-box/
description: "Pelajari cara mengisi bidang list box dalam formulir PDF dengan Java menggunakan fasad Form di Aspose.PDF."
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Mengatur nilai bidang list box dalam formulir PDF dengan Java"
Abstract: "Artikel ini menunjukkan cara mengaitkan formulir PDF, menetapkan nilai bidang list box, dan menyimpan dokumen yang diperbarui dengan fasad Form di Aspose.PDF for Java."
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
