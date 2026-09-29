---
title: Memanipulasi Tabel dalam Dokumen PDF yang Ada
linktitle: Manipulasi Tabel
type: docs
weight: 40
url: /id/java/manipulating-tables/
description: Pelajari cara memeriksa dan memodifikasi tabel dalam dokumen PDF yang ada menggunakan Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Periksa dan modifikasi tabel PDF yang ada dengan Java
Abstract: Artikel ini menjelaskan cara memanipulasi tabel yang sudah ada dalam dokumen PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup cara menemukan tabel dengan TableAbsorber, memperbarui teks di dalam sel, serta mengganti tabel yang terdeteksi dengan objek Table baru.
---
Gunakan `TableAbsorber` ketika Anda perlu menemukan tabel yang ada dan memperbarui kontennya.

## Ganti teks di dalam sel tabel

Gunakan contoh ini ketika teks dalam sel yang terdeteksi harus diperbarui tanpa membangun ulang seluruh tabel.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan kunjungi halaman dengan [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/).
1. Validasi bahwa fragmen teks tabel dan sel target ada.
1. Ganti teks sel dan simpan dokumen yang diperbarui.

```java
public static void replaceCells(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        if (absorber.getTableList().isEmpty()) {
            throw new IllegalStateException("No tables were found on page 1.");
        }
        if (absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0).getTextFragments().size() == 0) {
            throw new IllegalStateException("The target cell has no text fragments.");
        }

        absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0)
                .getTextFragments().get_Item(1).setText("New Value");
        document.save(outputFile.toString());
    }
}
```

## Ganti tabel yang terdeteksi dengan tabel baru

Gunakan contoh ini ketika tabel asli harus sepenuhnya diganti oleh tabel yang baru dibuat.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan deteksi tabel pada halaman.
1. Buat yang baru [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) dengan struktur yang diinginkan.
1. Ganti tabel yang diserap dan simpan PDF keluaran.

```java
public static void replaceTable(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        if (absorber.getTableList().isEmpty()) {
            throw new IllegalStateException("No tables were found on page 1.");
        }

        AbsorbedTable oldTable = absorber.getTableList().get(0);
        Table newTable = new Table();
        newTable.setColumnWidths("100 100 100");
        newTable.setDefaultCellBorder(new BorderInfo(BorderSide.All, 1.0f));

        Row row = newTable.getRows().add();
        row.getCells().add("Col 1");
        row.getCells().add("Col 2");
        row.getCells().add("Col 3");
        row = newTable.getRows().add();
        row.getCells().add("Col 12");
        row.getCells().add("Col 22");
        row.getCells().add("Col 32");

        absorber.replace(document.getPages().get_Item(1), oldTable, newTable);
        document.save(outputFile.toString());
    }
}
```
