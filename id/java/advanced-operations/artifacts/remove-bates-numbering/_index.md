---
title: Menghapus penomoran Bates dari PDF dengan Java
linktitle: Menghapus penomoran Bates
type: docs
weight: 100
url: /id/java/remove-bates-numbering/
description: Hapus penomoran Bates dari semua halaman PDF dalam Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menghapus penomoran Bates dari PDF dengan Java
Abstract: Hapus penomoran Bates dari semua halaman PDF dalam Java.
---
Hapus penomoran Bates dari semua halaman PDF dalam Java.

## Menghapus penomoran Bates

Gunakan pendekatan ini ketika artefak penomoran Bates yang ada harus dihapus dari dokumen.

1. Buka PDF sumber dengan [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Panggil metode pembantu untuk menghapus penomoran Bates dari koleksi halaman.
1. Simpan hasilnya sebagai file PDF.

```java
public static void deleteBatesNumbering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageCollectionExtensions.deleteBatesNumbering(document.getPages());
        document.save(outputFile.toString());
    }
}
```

## Topik terkait

- [Menambahkan penomoran Bates](/pdf/id/java/add-bates-numbering/)
- [Artefak PDF](/pdf/id/java/artifacts/)
