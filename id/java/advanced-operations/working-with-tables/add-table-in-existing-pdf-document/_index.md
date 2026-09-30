---
title: "Menambahkan tabel ke PDF dalam Java"
linktitle: "Menambahkan tabel"
type: docs
weight: 10
url: /id/java/adding-tables/
description: Pelajari cara menambahkan dan mengkonfigurasi tabel dalam dokumen PDF yang ada di Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menambahkan dan format tabel dalam dokumen PDF dengan Java"
Abstract: Artikel ini menjelaskan cara menambahkan dan mengkonfigurasi tabel dalam dokumen PDF menggunakan Aspose.PDF for Java. Ini mencakup pembuatan tabel, batas, margin, padding, rentang baris dan kolom, perilaku AutoFit, penyisipan gambar dalam sel, baris dan kolom yang berulang, fragmen HTML dan LaTeX, serta kontrol rendering multi‑halaman.
---
Aspose.PDF for Java menyediakan yang kaya `Table` API untuk membangun tabel dengan penyesuaian tata letak dan konten.

## Membuat tabel dasar

Gunakan contoh ini ketika Anda perlu menambahkan tabel sederhana dengan batas seragam dan sel teks.

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman.
1. Buat sebuah [`Table`](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) dan konfigurasikan batasnya.
1. Tambahkan baris dan sel, lampirkan tabel ke halaman, dan simpan dokumen.

```java
public static void createTable(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, 5, Color.getLightGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 5, Color.getLightGray()));
        for (int rowCount = 0; rowCount < 10; rowCount++) {
            Row row = table.getRows().add();
            row.getCells().add("Column (" + rowCount + ", 1)");
            row.getCells().add("Column (" + rowCount + ", 2)");
            row.getCells().add("Column (" + rowCount + ", 3)");
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## Menambahkan sel dengan rentang baris dan rentang kolom

Gunakan contoh ini ketika tabel memerlukan sel yang digabungkan di antara baris atau kolom.

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman.
1. Buat sebuah [`Table`](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) dan tambahkan baris.
1. Konfigurasikan `ColSpan` dan `RowSpan` pada sel target, lalu simpan PDF.

```java
public static void addRowspanOrColspan(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getBlack()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getBlack()));

        Row row1 = table.getRows().add();
        for (int cellCount = 1; cellCount < 5; cellCount++) {
            row1.getCells().add("Test 1" + cellCount);
        }

        Row row2 = table.getRows().add();
        row2.getCells().add("Test 2 1");
        Cell cell = row2.getCells().add("Test 2 2");
        cell.setColSpan(2);
        row2.getCells().add("Test 2 4");

        Row row3 = table.getRows().add();
        row3.getCells().add("Test 3 1");
        row3.getCells().add("Test 3 2");
        row3.getCells().add("Test 3 3");
        row3.getCells().add("Test 3 4");

        Row row4 = table.getRows().add();
        row4.getCells().add("Test 4 1");
        cell = row4.getCells().add("Test 4 2");
        cell.setRowSpan(2);
        row4.getCells().add("Test 4 3");
        row4.getCells().add("Test 4 4");

        Row row5 = table.getRows().add();
        row5.getCells().add("Test 5 1");
        row5.getCells().add("Test 5 3");
        row5.getCells().add("Test 5 4");

        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## Menambahkan batas tabel dan padding sel

Gunakan contoh ini ketika Anda perlu mengonfigurasi batas, padding, dan perilaku pembungkus sel.

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman.
1. Buat sebuah [`Table`](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) dan konfigurasikan lebar, batas, dan padding.
1. Tambahkan baris dan simpan dokumen yang dihasilkan.

```java
public static void addBorders(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        page.getParagraphs().add(table);
        table.setColumnWidths("50 50 50");
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1f));
        table.setBorder(new BorderInfo(BorderSide.All, 1));
        table.setDefaultCellPadding(new MarginInfo(5, 5, 5, 5));

        Row row1 = table.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add();
        row1.getCells().get_Item(2).getParagraphs().add(new TextFragment("col3 with large text string"));
        row1.getCells().get_Item(2).setWordWrapped(false);

        Row row2 = table.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");
        document.save(outputFile.toString());
    }
}
```

## Mengaktifkan tata letak tabel auto-fit

Gunakan contoh ini ketika tabel harus secara otomatis menyesuaikan lebar halaman yang tersedia.

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman.
1. Buat sebuah [`Table`](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) dan setel `ColumnAdjustment.AutoFitToWindow`.
1. Tambahkan baris contoh dan simpan PDF.

```java
public static void autoFit(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        page.getParagraphs().add(table);
        table.setColumnWidths("50 50 50");
        table.setColumnAdjustment(ColumnAdjustment.AutoFitToWindow);
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1f));
        table.setBorder(new BorderInfo(BorderSide.All, 1));
        table.setDefaultCellPadding(new MarginInfo(5, 5, 5, 5));

        Row row1 = table.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add("col3");
        Row row2 = table.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");
        document.save(outputFile.toString());
    }
}
```

## Menambahkan gambar di dalam sel tabel

Gunakan contoh ini ketika tabel perlu menampilkan konten gambar raster di dalam salah satu selnya.

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman.
1. Buat sebuah [`Table`](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) dan tambahkan baris dengan sel teks dan gambar.
1. Konfigurasikan [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) ukuran dan simpan dokumen.

```java
public static void addImage(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setColumnWidths("200 100");

        Row row = table.getRows().add();
        row.getCells().add().getParagraphs().add(new TextFragment(imageFile.toString()));
        Image image = new Image();
        image.setFile(imageFile.toString());
        image.setFixWidth(50);
        image.setFixHeight(50);
        row.getCells().add().getParagraphs().add(image);

        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## Menambahkan gambar SVG di dalam sel tabel

Gunakan contoh ini ketika tabel harus merender file SVG baris per baris.

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman.
1. Buat sebuah [`Table`](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) dan iterasi melalui file SVG.
1. Tambahkan satu baris per gambar, konfigurasikan SVG [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/), dan simpan PDF.

```java
public static void addSvgImage(List<Path> imageFiles, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setColumnWidths("200 100");
        for (Path imageFile : imageFiles) {
            Row row = table.getRows().add();
            row.getCells().add().getParagraphs().add(new TextFragment(imageFile.toString()));
            Image image = new Image();
            image.setFileType(ImageFileType.Svg);
            image.setFile(imageFile.toString());
            image.setFixWidth(50);
            image.setFixHeight(50);
            row.getCells().add().getParagraphs().add(image);
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## Menambahkan fragmen HTML ke sel tabel

Gunakan contoh ini ketika konten tabel harus menyertakan pemformatan HTML inline.

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman.
1. Buat sebuah [`Table`](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) dan mengatur batas.
1. Tambah objek [`HtmlFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlfragment/) ke sel dan simpan dokumen.

```java
public static void addHtmlFragments(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getLightGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getLightGray()));
        for (int rowCount = 1; rowCount < 10; rowCount++) {
            Row row = table.getRows().add();
            row.getCells().add().getParagraphs().add(new HtmlFragment("Column <strong>(" + rowCount + ", 1)</strong>"));
            row.getCells().add().getParagraphs().add(new HtmlFragment("Column <span style='color:red'>(" + rowCount + ", 2)</span>"));
            row.getCells().add().getParagraphs().add(new HtmlFragment("Column <span style='text-decoration: underline'>(" + rowCount + ", 3)</span>"));
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## Menambahkan fragmen LaTeX ke sel tabel

Gunakan contoh ini ketika konten tabel harus menampilkan ekspresi TeX atau LaTeX.

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman.
1. Buat sebuah [`Table`](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) dengan batas.
1. Tambah objek [`TeXFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/texfragment/) ke sel dan simpan file output.

```java
public static void addLatexFragments(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getLightGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getLightGray()));
        for (int rowCount = 1; rowCount < 10; rowCount++) {
            Row row = table.getRows().add();
            row.getCells().add().getParagraphs().add(new TeXFragment("Column $\\mathbf{(" + rowCount + ", 1)}$"));
            row.getCells().add().getParagraphs().add(new TeXFragment("Column $\\textcolor{red}{(" + rowCount + ", 2)}$"));
            row.getCells().add().getParagraphs().add(new TeXFragment("Column $\\underline{(" + rowCount + ", 3)}$"));
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## Memaksa tabel ke halaman baru

Gunakan contoh ini ketika tabel kedua harus dimulai pada halaman terpisah setelah tabel besar.

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan atur pengaturan halaman.
1. Bangun yang pertama besar [`Table`](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) dan tambahkan itu ke halaman.
1. Buat tabel kedua, atur `InNewPage`, dan simpan dokumen.

```java
public static void addTableOnNewPage(Path outputFile) {
    try (Document document = new Document()) {
        document.getPageInfo().getMargin().setLeft(37);
        document.getPageInfo().getMargin().setRight(37);
        document.getPageInfo().getMargin().setTop(37);
        document.getPageInfo().getMargin().setBottom(37);
        document.getPageInfo().setLandscape(true);

        Page page = document.getPages().add();
        Table table = new Table();
        table.setColumnWidths("50 100");
        for (int i = 1; i < 121; i++) {
            Row row = table.getRows().add();
            row.setFixedRowHeight(15);
            row.getCells().add().getParagraphs().add(new TextFragment("Content 1"));
            row.getCells().add().getParagraphs().add(new TextFragment("Content 2"));
        }
        page.getParagraphs().add(table);

        Table table1 = new Table();
        table1.setColumnWidths("100 100");
        for (int i = 1; i < 11; i++) {
            Row row = table1.getRows().add();
            row.getCells().add().getParagraphs().add(new TextFragment("Content 3"));
            row.getCells().add().getParagraphs().add(new TextFragment("Content 4"));
        }
        table1.setInNewPage(true);
        page.getParagraphs().add(table1);
        document.save(outputFile.toString());
    }
}
```

## Membuat tabel terputus secara vertikal dengan kolom yang berulang

Gunakan contoh ini ketika tabel lebar harus dilanjutkan secara vertikal dan mengulangi kolom kunci.

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman.
1. Buat sebuah [`Table`](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) dan mengonfigurasi pemutusan vertikal dengan kolom berulang.
1. Tambahkan header dan baris data, lalu simpan dokumen.

```java
public static void addTableHideBorders(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBroken(TableBroken.Vertical);
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All));
        table.setRepeatingColumnsCount(2);
        page.getParagraphs().add(table);

        Row row = table.getRows().add();
        Cell cell = row.getCells().add("header 1");
        cell.setColSpan(2);
        cell.setBackgroundColor(Color.getLightGray());
        row.getCells().add("header 3");
        Cell cell2 = row.getCells().add("header 4");
        cell2.setColSpan(2);
        cell2.setBackgroundColor(Color.getLightBlue());
        row.getCells().add("header 6");
        Cell cell3 = row.getCells().add("header 7");
        cell3.setColSpan(2);
        cell3.setBackgroundColor(Color.getLightGreen());
        Cell cell4 = row.getCells().add("header 9");
        cell4.setColSpan(3);
        cell4.setBackgroundColor(Color.getLightCoral());
        for (int i = 12; i < 18; i++) {
            row.getCells().add("header " + i);
        }

        for (int rowCounter = 0; rowCounter < 3; rowCounter++) {
            Row row1 = table.getRows().add();
            for (int i = 1; i < 18; i++) {
                row1.getCells().add("col " + rowCounter + ", " + i);
            }
        }
        document.save(outputFile.toString());
    }
}
```

## Menggunakan kembali contoh batas dan padding

Gunakan helper ini ketika skenario margin dan padding harus didelegasikan ke contoh border bersama.

1. Panggil metode border dan padding tabel yang ada.
1. Gunakan kembali logika tata letak tabel yang sama tanpa menduplikasi kode.

```java
public static void addMarginsOrPadding(Path outputFile) {
    addBorders(outputFile);
}
```

## Membuat tabel dengan sudut melengkung

Gunakan contoh ini ketika tabel harus menggunakan gaya sudut membulat alih-alih batas persegi panjang standar.

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman.
1. Buat sebuah [`Table`](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) dan mengonfigurasi pengaturan batas melengkung.
1. Tambahkan baris ke tabel dan simpan PDF.

```java
public static void createTableWithRoundCorner(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        BorderInfo borderInfo = new BorderInfo(BorderSide.All);
        borderInfo.setRoundedBorderRadius(15);
        table.setCornerStyle(BorderCornerStyle.Round);
        table.setBorder(borderInfo);
        for (int rowCount = 0; rowCount < 10; rowCount++) {
            Row row = table.getRows().add();
            row.getCells().add("Column (" + rowCount + ", 1)");
            row.getCells().add("Column (" + rowCount + ", 2)");
            row.getCells().add("Column (" + rowCount + ", 3)");
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## Menambahkan baris header berulang

Gunakan contoh ini ketika tabel multi‑halaman harus mengulangi baris header mereka pada setiap halaman lanjutan.

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman.
1. Buat terputus secara vertikal [`Table`](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) dan konfigurasikan jumlah baris berulang serta gaya.
1. Tambahkan baris header dan baris data, lalu simpan dokumen.

```java
public static void addRepeatingRows(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBroken(TableBroken.Vertical);
        table.setRepeatingRowsCount(2);
        TextState textState = new TextState();
        textState.setFontSize(12);
        textState.setFont(FontRepository.findFont("TimesNewRoman"));
        textState.setForegroundColor(Color.getRed());
        table.setRepeatingRowsStyle(textState);
        table.setColumnWidths("100 100 100");
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getBlack()));
        table.setBorder(new BorderInfo(BorderSide.All, 1, Color.getBlack()));

        Row headerRow1 = table.getRows().add();
        headerRow1.getCells().add("Header 1-1");
        headerRow1.getCells().add("Header 1-2");
        headerRow1.getCells().add("Header 1-3");
        for (Cell cell : headerRow1.getCells()) {
            cell.setBackgroundColor(Color.getLightGray());
        }
        Row headerRow2 = table.getRows().add();
        headerRow2.getCells().add("Header 2-1");
        headerRow2.getCells().add("Header 2-2");
        headerRow2.getCells().add("Header 2-3");
        for (Cell cell : headerRow2.getCells()) {
            cell.setBackgroundColor(Color.getLightBlue());
        }
        for (int i = 1; i < 101; i++) {
            Row row = table.getRows().add();
            row.getCells().add("Data " + i + "-1");
            row.getCells().add("Data " + i + "-2");
            row.getCells().add("Data " + i + "-3");
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## Menambahkan kolom berulang dalam tabel lebar

Gunakan contoh ini ketika kolom pertama harus diulang sementara tabel terputus secara vertikal pada halaman yang sama.

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan atur ukuran halaman.
1. Buat sebuah [`Table`](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) dan atur kolom yang berulang serta perilaku auto-fit.
1. Tambahkan header dan baris data, lalu simpan PDF.

```java
public static void addRepeatingColumns(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.setPageSize(PageSize.getA5().getHeight(), PageSize.getA5().getWidth());
        BorderInfo border = new BorderInfo(BorderSide.All, 0.5f, Color.getLightGray());
        Table table = new Table();
        table.setBroken(TableBroken.VerticalInSamePage);
        table.setColumnAdjustment(ColumnAdjustment.AutoFitToContent);
        table.setRepeatingColumnsCount(5);
        table.setBorder(border);
        table.setDefaultCellBorder(border);
        page.getParagraphs().add(table);

        Row row = table.getRows().add();
        for (int i = 1; i < 6; i++) {
            Cell cell = row.getCells().add("header " + i);
            cell.setBackgroundColor(Color.getLightGray());
        }
        for (int i = 6; i < 18; i++) {
            row.getCells().add("header " + i);
        }

        for (int rowCounter = 1; rowCounter < 6; rowCounter++) {
            row = table.getRows().add();
            for (int i = 1; i < 6; i++) {
                Cell cell = row.getCells().add("cell " + rowCounter + "," + i);
                cell.setBackgroundColor(Color.getLightGray());
            }
            for (int i = 6; i < 18; i++) {
                row.getCells().add("cell " + rowCounter + "," + i);
            }
        }
        document.save(outputFile.toString());
    }
}
```

## Menyisipkan jeda halaman antara baris tabel

Gunakan contoh ini ketika baris tabel tertentu harus dimulai pada halaman baru.

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman.
1. Buat sebuah [`Table`](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) dan mengisi banyak baris.
1. Tandai baris yang dipilih dengan `InNewPage` dan simpan dokumen.

```java
public static void insertPageBreak(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, Color.getRed()));
        table.setColumnWidths("100 100");
        for (int counter = 0; counter < 201; counter++) {
            Row row = new Row();
            table.getRows().add(row);
            row.getCells().add().getParagraphs().add(new TextFragment("Cell " + counter + ", 0"));
            row.getCells().add().getParagraphs().add(new TextFragment("Cell " + counter + ", 1"));
            if (counter % 10 == 0 && counter != 0) {
                row.setInNewPage(true);
            }
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## Memutar teks di dalam sel tabel

Gunakan contoh ini ketika teks sel harus ditampilkan pada sudut rotasi yang berbeda.

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman.
1. Buat sebuah [`Table`](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) dan tambahkan baris dengan beberapa sel.
1. Buat diputar objek [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/), tambahkan ke sel, dan simpan PDF.

```java
public static void rotatedTextTable(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getBlack()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getBlack()));
        Row row = table.getRows().add();
        row.setMinRowHeight(200);
        for (int cellCount = 0; cellCount < 4; cellCount++) {
            Cell cell = row.getCells().add();
            TextFragment textFragment = new TextFragment("Cell 1 " + (cellCount - 1));
            textFragment.getTextState().setRotation(90 * cellCount);
            textFragment.setHorizontalAlignment(HorizontalAlignment.Center);
            cell.getParagraphs().add(textFragment);
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```
