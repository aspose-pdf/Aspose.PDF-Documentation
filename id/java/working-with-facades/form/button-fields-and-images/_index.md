---
title: Bidang Tombol dan Gambar
linktitle: Bidang Tombol dan Gambar
type: docs
weight: 40
url: /id/java/button-fields-and-images/
description: Pelajari cara menambahkan penampilan gambar ke bidang tombol dalam formulir PDF menggunakan antarmuka Form di Aspose.PDF for Java.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Tambahkan penampilan gambar ke bidang tombol PDF di Java
Abstract: Artikel ini menunjukkan cara menggunakan antarmuka Form di Aspose.PDF for Java untuk mengikat formulir PDF, memuat gambar sebagai aliran, mengisi bidang tombol gambar, dan menyimpan dokumen yang diperbarui.
---
Contoh Java dalam `FormExamples.addImageAppearanceToButtonField(...)` menunjukkan cara memperbarui tampilan bidang tombol dengan aliran gambar.

Alur kerja sederhana:

- ikat PDF input dengan `form.bindPdf(...)`
- buka file gambar dengan `Files.newInputStream(...)`
- panggilan `form.fillImageField(...)` untuk bidang tombol
- simpan PDF yang diperbarui

```java
public static void addImageAppearanceToButtonField(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        form.bindPdf(inputFile.toString());
        form.fillImageField("Image1_af_image", imageStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
