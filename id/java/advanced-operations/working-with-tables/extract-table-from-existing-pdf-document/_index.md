---
title: Ekstrak Tabel dari PDF dengan Java
linktitle: Ekstrak Tabel
type: docs
weight: 20
url: /id/java/extracting-table/
description: Pelajari cara mengekstrak data tabel dari dokumen PDF yang ada dengan Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ekstrak data tabel dari file PDF dengan Java
Abstract: Artikel ini menjelaskan cara mengekstrak tabel dari dokumen PDF menggunakan Aspose.PDF for Java. Artikel ini menunjukkan cara menggunakan TableAbsorber untuk mendeteksi tabel per halaman, mengiterasi baris dan sel, serta mengumpulkan teks sel untuk pemrosesan selanjutnya.
---
Gunakan `TableAbsorber` ketika Anda perlu mendeteksi struktur tabel dalam PDF yang ada dan membaca isinya.

## Ekstrak teks dari tabel yang terdeteksi

Gunakan contoh ini ketika Anda perlu menemukan tabel pada setiap halaman dan mengumpulkan teks selnya.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Kunjungi setiap halaman dengan [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/).
1. Iterasi melalui tabel yang diserap, baris, dan sel, kemudian output teks yang diekstrak.

```java
public static void extract(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            TableAbsorber absorber = new TableAbsorber();
            absorber.visit(page);
            for (AbsorbedTable table : absorber.getTableList()) {
                System.out.println("Table ----");
                for (AbsorbedRow row : table.getRowList()) {
                    System.out.println("Row:");
                    StringBuilder rowText = new StringBuilder();
                    for (AbsorbedCell cell : row.getCellList()) {
                        StringBuilder cellText = new StringBuilder();
                        for (TextFragment fragment : cell.getTextFragments()) {
                            for (TextSegment segment : fragment.getSegments()) {
                                cellText.append(segment.getText());
                            }
                        }
                        rowText.append(" | ").append(cellText);
                    }
                    System.out.println(rowText);
                }
            }
        }
    }
}
```
