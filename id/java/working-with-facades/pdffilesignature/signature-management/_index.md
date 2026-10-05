---
title: "Manajemen tanda tangan"
linktitle: "Manajemen tanda tangan"
type: docs
weight: 80
url: /id/java/signature-management/
description: "Pelajari cara menghapus tanda tangan PDF yang ada di Java dengan fasad PdfFileSignature."
lastmod: "2026-09-30"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menghapus tanda tangan PDF di Java"
Abstract: Pelajari cara menghapus tanda tangan dari PDF yang ditandatangani dengan Aspose.PDF for Java. Set contoh Java saat ini mencakup penghapusan tanda tangan yang ada berdasarkan nama dan menyimpan dokumen yang diperbarui. Ini tidak menyertakan contoh terpisah untuk membersihkan bidang tanda tangan yang terkait.
---
## Menghapus tanda tangan

Gunakan Workflow ini ketika tanda tangan digital yang ada harus dihapus dari dokumen.

### Langkah

1. Buat instans `PdfFileSignature` dan mengikat PDF yang ditandatangani.
2. Baca koleksi tanda tangan dan pilih nama tanda tangan.
3. Panggil `removeSignature` dengan nama itu.
4. Simpan file yang diperbarui dan tutup objek fasad.

### Contoh Java

```java
public static void removeSignature(Path inputFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        pdfSignature.removeSignature(signatureName);
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```

Set contoh Java saat ini tidak menyertakan metode terpisah untuk menghapus bidang tanda tangan yang terkait setelah menghapus tanda tangan.
