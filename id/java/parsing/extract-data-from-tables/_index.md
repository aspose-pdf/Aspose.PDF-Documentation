---
title: Ekstrak Data dari Tabel dalam PDF dengan Java
linktitle: Ekstrak Data dari Tabel
type: docs
weight: 40
url: /id/java/extract-data-from-table-in-pdf/
description: Pelajari cara mengekstrak data tabel dari file PDF dengan Aspose.PDF for Java dan mengekspor tabel yang terdeteksi untuk pemrosesan lebih lanjut.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara Mengekstrak Data dari Tabel dalam PDF via Java
Abstract: Artikel ini menjelaskan cara mengekstrak dan memproses data tabel dari dokumen PDF dengan Aspose.PDF for Java. Ini menunjukkan cara memindai halaman dengan `TableAbsorber`, membaca baris dan sel dari tabel yang terdeteksi, membatasi ekstraksi ke wilayah beranotasi tertentu, dan mengekspor hasilnya ke Excel.
---
## Ekstrak tabel dari PDF

Gunakan `TableAbsorber` untuk menemukan tabel pada setiap halaman dan mengiterasi baris, sel, fragmen teks, dan segmen teks.

1. Buka PDF sumber dalam a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instansi.
1. Iterasi melalui dokumen [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) objek karena tabel terdeteksi halaman per halaman.
1. Buat sebuah [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) untuk setiap halaman dan panggil `visit(page)` untuk mengisi daftar tabel yang terdeteksi.
1. Iterasi melalui yang terdeteksi [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/), [AbsorbedRow](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/), [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/), [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/), dan `TextSegment` objek.
1. Bangun teks baris yang diekstrak dari konten fragmen dan cetak data tabel.

```java
public static void extractTablesFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            TableAbsorber absorber = new TableAbsorber();
            absorber.visit(page);

            for (AbsorbedTable table : absorber.getTableList()) {
                System.out.println("Table");
                for (AbsorbedRow row : table.getRowList()) {
                    StringBuilder rowText = new StringBuilder();
                    for (AbsorbedCell cell : row.getCellList()) {
                        if (rowText.length() > 0) {
                            rowText.append("|");
                        }
                        StringBuilder cellText = new StringBuilder();
                        for (TextFragment fragment : cell.getTextFragments()) {
                            StringBuilder fragmentText = new StringBuilder();
                            for (TextSegment segment : fragment.getSegments()) {
                                fragmentText.append(segment.getText());
                            }
                            if (cellText.length() > 0) {
                                cellText.append("|");
                            }
                            cellText.append(fragmentText);
                        }
                        rowText.append(cellText);
                    }
                    System.out.println(rowText);
                }
            }
        }
    }
}
```

## Ekstrak tabel dari area yang ditandai secara spesifik

Contoh ini menemukan anotasi persegi, membandingkan persegiannya dengan setiap tabel yang terdeteksi, dan hanya menghasilkan tabel yang berada di dalam wilayah yang ditandai.

1. Buka PDF sumber dalam a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instansi.
1. Dapatkan target [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) dan temukan kotak [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) yang menandai wilayah ekstraksi.
1. Buat sebuah [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) dan panggil `visit(page)` untuk mendeteksi tabel pada halaman itu.
1. Bandingkan setiap yang terdeteksi [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/) [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) dengan batas persegi panjang anotasi.
1. Iterasi melalui yang cocok [AbsorbedRow](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/) dan [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/) objek dan membangun kembali teks baris.
1. Cetak data tabel hanya untuk wilayah yang ditandai.

```java
public static void extractTableFromSpecificArea(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        Annotation squareAnnotation = null;
        for (Annotation annotation : page.getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Square) {
                squareAnnotation = annotation;
                break;
            }
        }

        if (squareAnnotation == null) {
            System.out.println("No square annotation found.");
            return;
        }

        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(page);

        for (AbsorbedTable table : absorber.getTableList()) {
            Rectangle tableRect = table.getRectangle();
            Rectangle annotationRect = squareAnnotation.getRect();

            boolean isInRegion = annotationRect.getLLX() < tableRect.getLLX()
                    && annotationRect.getLLY() < tableRect.getLLY()
                    && annotationRect.getURX() > tableRect.getURX()
                    && annotationRect.getURY() > tableRect.getURY();

            if (isInRegion) {
                for (AbsorbedRow row : table.getRowList()) {
                    StringBuilder rowText = new StringBuilder();
                    for (AbsorbedCell cell : row.getCellList()) {
                        if (rowText.length() > 0) {
                            rowText.append("|");
                        }
                        StringBuilder cellText = new StringBuilder();
                        for (TextFragment fragment : cell.getTextFragments()) {
                            StringBuilder fragmentText = new StringBuilder();
                            for (TextSegment segment : fragment.getSegments()) {
                                fragmentText.append(segment.getText());
                            }
                            if (cellText.length() > 0) {
                                cellText.append("|");
                            }
                            cellText.append(fragmentText);
                        }
                        rowText.append(cellText);
                    }
                    System.out.println(rowText);
                }
            }
        }
    }
}
```

## Ekspor tabel ke Excel

1. Buka PDF sumber dalam a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instansi.
1. Buat [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) untuk ekspor.
1. Atur format keluaran Excel ke `XLSX` jadi tata letak tabel yang terdeteksi ditulis sebagai buku kerja Excel.
1. Panggil `document.save(outputFile.toString(), excelSave)` untuk mengekspor dokumen dalam format Excel.

```java
public static void exportTablesToExcel(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions excelSave = new ExcelSaveOptions();
        excelSave.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        document.save(outputFile.toString(), excelSave);
    }
}
```
