---
title: Integrasikan Tabel PDF dengan Sumber Data di Java
linktitle: Integrasikan Tabel
type: docs
weight: 30
url: /id/java/integrate-table/
description: Pelajari cara mengintegrasikan tabel PDF dengan sumber data terstruktur seperti file CSV di Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Buat tabel PDF dari data terstruktur dengan Java
Abstract: Artikel ini menjelaskan cara mengintegrasikan tabel PDF dengan data eksternal menggunakan Aspose.PDF for Java. Ini mencakup pembacaan data CSV, pemilihan kolom tertentu, membangun objek Table yang bergaya dari baris yang diurai, dan merender hasilnya ke dalam dokumen PDF.
---
Contoh Java ini membangun tabel PDF dari data CSV tanpa bergantung pada pustaka dataframe eksternal.

## Buat tabel dari baris CSV

Gunakan contoh ini ketika kolom CSV yang dipilih harus diubah menjadi tabel PDF yang bergaya.

1. Buat sebuah [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) dan konfigurasikan batasnya.
1. Deteksi indeks kolom yang diperlukan dari baris header CSV.
1. Tambahkan baris header dan jumlah baris data yang diminta, kemudian kembalikan tabel.

```java
public static Table createTableFromCsv(List<String[]> rows, int maxRows) {
    Table table = new Table();
    table.setBorder(new BorderInfo(BorderSide.All, 1, Color.getLightGray()));
    table.setDefaultCellBorder(new BorderInfo(BorderSide.Bottom, 1, Color.getLightGray()));

    String[] header = rows.get(0);
    int[] selectedColumns = findColumns(header, "city", "country", "population", "iso3");

    Row headerRow = table.getRows().add();
    headerRow.setRowBroken(false);
    for (int columnIndex : selectedColumns) {
        Cell cell = headerRow.getCells().add(header[columnIndex]);
        cell.setBackgroundColor(Color.getLightGray());
    }

    int limit = Math.min(maxRows, rows.size() - 1);
    for (int rowIndex = 1; rowIndex <= limit; rowIndex++) {
        Row row = table.getRows().add();
        String[] rowData = rows.get(rowIndex);
        for (int columnIndex : selectedColumns) {
            row.getCells().add(columnIndex < rowData.length ? rowData[columnIndex] : "");
        }
    }

    return table;
}
```

## Buat PDF dari data CSV

Gunakan contoh ini ketika input CSV harus diubah menjadi dokumen tabel PDF.

1. Baca baris CSV dari file input.
1. Pratinjau sebagian baris yang diurai di konsol.
1. Buat PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/), tambahkan tabel yang dihasilkan, dan simpan file output.

```java
public static void createPdfFromCsv(Path inputFile, Path outputFile, int maxRows) throws Exception {
    List<String[]> rows = readCsv(inputFile);
    for (int i = 0; i < Math.min(20, rows.size()); i++) {
        System.out.println(String.join(" | ", rows.get(i)));
    }

    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(createTableFromCsv(rows, maxRows));
        document.save(outputFile.toString());
    }
}
```

## Temukan indeks kolom CSV berdasarkan nama

Gunakan pembantu ini ketika kolom bernama tertentu harus ditemukan dalam baris header CSV.

1. Iterasi melalui nama kolom yang diminta.
1. Cari baris header untuk indeks yang cocok.
1. Kembalikan posisi kolom yang dikumpulkan.

```java
private static int[] findColumns(String[] header, String... names) {
    int[] indexes = new int[names.length];
    for (int i = 0; i < names.length; i++) {
        indexes[i] = 0;
        for (int j = 0; j < header.length; j++) {
            if (names[i].equals(header[j])) {
                indexes[i] = j;
                break;
            }
        }
    }
    return indexes;
}
```

## Baca baris CSV dari file

Gunakan pembantu ini ketika sumber CSV harus dimuat ke memori sebelum pembuatan tabel.

1. Baca semua baris dari file input.
1. Pisahkan setiap baris dengan pembantu parser CSV.
1. Kembalikan nilai baris yang dikumpulkan.

```java
private static List<String[]> readCsv(Path inputFile) throws Exception {
    List<String[]> rows = new ArrayList<>();
    for (String line : Files.readAllLines(inputFile)) {
        rows.add(splitCsvLine(line));
    }
    return rows;
}
```

## Pisahkan satu baris CSV menjadi nilai

Gunakan pembantu ini ketika baris CSV mungkin berisi nilai yang diapit tanda kutip dan karakter kutip yang di-escape.

1. Iterasikan karakter dalam baris.
1. Lacak apakah parser saat ini berada di dalam teks yang diapit tanda kutip.
1. Bangun daftar nilai akhir dan kembalikan sebagai array.

```java
private static String[] splitCsvLine(String line) {
    List<String> values = new ArrayList<>();
    StringBuilder current = new StringBuilder();
    boolean inQuotes = false;
    for (int i = 0; i < line.length(); i++) {
        char ch = line.charAt(i);
        if (ch == '"') {
            if (inQuotes && i + 1 < line.length() && line.charAt(i + 1) == '"') {
                current.append('"');
                i++;
            } else {
                inQuotes = !inQuotes;
            }
        } else if (ch == ',' && !inQuotes) {
            values.add(current.toString());
            current.setLength(0);
        } else {
            current.append(ch);
        }
    }
    values.add(current.toString());
    return values.toArray(String[]::new);
}
```
