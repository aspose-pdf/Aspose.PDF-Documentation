---
title: "Menghapus tabel dari dokumen PDF yang ada"
linktitle: "Menghapus tabel"
description: Pelajari cara menghapus satu atau lebih tabel dari dokumen PDF yang ada dengan Java.
lastmod: "2026-09-30"
type: docs
weight: 50
url: /id/java/removing-tables/
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menghapus satu atau beberapa tabel dari file PDF dengan Java"
Abstract: Artikel ini menjelaskan cara menghapus tabel dari dokumen PDF yang ada menggunakan Aspose.PDF for Java. Artikel ini memperkenalkan TableAbsorber untuk menemukan tabel dan menunjukkan cara menghapus satu tabel atau menghapus semua tabel yang terdeteksi dari sebuah halaman.
---
Gunakan `TableAbsorber` ketika Anda perlu menghapus satu atau lebih tabel yang terdeteksi dari PDF yang ada.

## Menghapus satu tabel yang terdeteksi

Gunakan contoh ini ketika hanya tabel pertama yang cocok pada halaman yang harus dihapus.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Kunjungi halaman target dengan [`TableAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/).
1. Hapus tabel pertama yang terdeteksi dan simpan dokumen.

```java
public static void removeOneTable(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        absorber.remove(absorber.getTableList().get(0));
        document.save(outputFile.toString());
    }
}
```

## Menghapus semua tabel yang terdeteksi dari halaman

Gunakan contoh ini ketika setiap tabel yang cocok pada halaman harus dihapus.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Kunjungi halaman target dengan [`TableAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) dan salin tabel yang terdeteksi ke dalam daftar.
1. Hapus setiap tabel yang terdeteksi dan simpan PDF yang diperbarui.

```java
public static void removeAllTables(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        List<AbsorbedTable> tables = new ArrayList<>(absorber.getTableList());
        for (AbsorbedTable table : tables) {
            absorber.remove(table);
        }
        document.save(outputFile.toString());
    }
}
```
