---
title: Isi Bidang Barcode
linktitle: Isi Bidang Barcode
type: docs
weight: 50
url: /id/java/fill-barcode-fields/
description: Pelajari cara mengisi bidang formulir barcode di Java menggunakan fasad Form di Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Isi bidang barcode dalam formulir PDF dengan Java
Abstract: Artikel ini menunjukkan cara mengikat formulir PDF, mengatur nilai bidang barcode, dan menyimpan dokumen yang diperbarui dengan fasad Form di Aspose.PDF for Java.
---
Gunakan `FormExamples.fillBarcodeFields(...)` untuk mengisi bidang kode batang dalam formulir PDF.

```java
public static void fillBarcodeFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillBarcodeField("product_barcode", "123456789012");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
