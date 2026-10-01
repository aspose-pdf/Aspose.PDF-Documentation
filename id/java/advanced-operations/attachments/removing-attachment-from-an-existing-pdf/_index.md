---
title: "Menghapus lampiran dari PDF di Java"
linktitle: Menghapus lampiran dari PDF yang ada
type: docs
weight: 30
url: /id/java/removing-attachment-from-an-existing-pdf/
description: Pelajari cara menghapus satu atau semua lampiran tersemat dari dokumen PDF dalam Java menggunakan Aspose.PDF.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menghapus lampiran PDF secara programatis dengan Java"
Abstract: Artikel ini menunjukkan cara menghapus lampiran dari file PDF menggunakan Aspose.PDF for Java. Contoh-contoh menunjukkan penghapusan satu file tersemat berdasarkan kunci dan membersihkan seluruh koleksi `EmbeddedFiles` sebelum menyimpan dokumen yang diperbarui.
---
Lampiran yang disimpan dalam dokumen PDF dapat dihapus secara individu atau sekaligus melalui `EmbeddedFiles` koleksi.

## Menghapus satu lampiran

Gunakan contoh ini ketika satu file tersemat yang bernama harus dihapus dari PDF.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Hapus lampiran berdasarkan kuncinya dari koleksi file tersemat.
1. Simpan dokumen output yang diperbarui.

```java
public static void removeAttachment(Path inputFile, String attachmentName, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getEmbeddedFiles().deleteByKey(attachmentName);
        document.save(outputFile.toString());
    }
}
```

## Menghapus semua lampiran

Gunakan pendekatan ini ketika seluruh koleksi file tersemat harus dibersihkan.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Hapus semua item dari koleksi file tersemat.
1. Simpan dokumen output yang telah dibersihkan.

```java
public static void removeAllAttachments(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getEmbeddedFiles().delete();
        document.save(outputFile.toString());
    }
}
```
