---
title: Tambahkan Header dan Footer PDF di Java
linktitle: Menambahkan Header dan Footer ke PDF
type: docs
weight: 50
url: /id/java/add-headers-and-footers-of-pdf-file/
description: Pelajari cara menambahkan header dan footer ke file PDF dalam Java menggunakan teks, gambar, dan konten terstruktur.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan header dan footer ke file PDF dengan Java
Abstract: Artikel ini menunjukkan cara menambahkan header dan footer ke dokumen PDF menggunakan Aspose.PDF for Java. Ini mencakup teks, penomoran halaman, HTML, gambar, tabel, dan konten header dan footer berbasis LaTeX.
---
Aspose.PDF for Java memungkinkan Anda menetapkan `HeaderFooter` objek ke setiap halaman dan mengisinya dengan berbagai jenis konten.

## Tambahkan teks header dan footer

Gunakan contoh ini ketika Anda membutuhkan konten teks sederhana di bagian atas dan bawah setiap halaman.

1. Buat [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) objek dan menambahkan fragmen teks.
1. Konfigurasikan margin untuk header dan footer.
1. Terapkan mereka ke setiap halaman PDF sumber dan simpan hasilnya.

```java
public static void addHeaderAndFooterAsText(Path inputFile, Path outputFile) {
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(new TextFragment("Demo header"));

    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(new TextFragment("Demo footer"));

    MarginInfo margin = new MarginInfo();
    margin.setLeft(50);
    margin.setTop(20);
    header.setMargin(margin);
    footer.setMargin(margin);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## Tambahkan header dan footer dengan penomoran halaman

Gunakan contoh ini ketika header atau footer harus menampilkan nomor halaman saat ini dan total jumlah halaman.

1. Buat [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) objek dengan placeholder penomoran halaman.
1. Konfigurasikan margin untuk kedua objek.
1. Terapkan mereka ke setiap halaman dan simpan PDF yang diperbarui.

```java
public static void usingHeaderAndFooterForPageNumbering(Path inputFile, Path outputFile) {
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(new TextFragment("Page $p from $P"));

    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(new TextFragment("Page $p / $P"));

    MarginInfo margin = new MarginInfo();
    margin.setLeft(50);
    margin.setTop(20);
    header.setMargin(margin);
    footer.setMargin(margin);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## Tambahkan header dan footer HTML

Gunakan contoh ini ketika konten header dan footer harus menyertakan pemformatan HTML inline.

1. Buat [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) objek dan tambahkan [HtmlFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlfragment/) konten.
1. Konfigurasikan margin untuk penempatan.
1. Tugaskan header dan footer ke setiap halaman dan simpan dokumen.

```java
public static void addHeaderAndFooterAsHtml(Path inputFile, Path outputFile) {
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(new HtmlFragment("This is an HTML <strong>Header</strong>"));

    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(new HtmlFragment("Powered by <i>Aspose.PDF</i>"));

    MarginInfo margin = new MarginInfo();
    margin.setLeft(50);
    margin.setTop(20);
    header.setMargin(margin);
    footer.setMargin(margin);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## Tambahkan header dan footer gambar

Gunakan contoh ini ketika header dan footer harus menampilkan gambar pada setiap halaman.

1. Buat [Image](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) objek dan tambahkan mereka ke dalam kontainer header dan footer.
1. Konfigurasikan margin dan tetapkan kontainer ke setiap halaman.
1. Simpan PDF yang diperbarui.

```java
public static void addHeaderAndFooterAsImage(Path inputFile, Path imageFile, Path outputFile) {
    Image headerImage = new Image();
    headerImage.setFile(imageFile.toString());
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(headerImage);

    Image footerImage = new Image();
    footerImage.setFile(imageFile.toString());
    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(footerImage);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            MarginInfo margin = new MarginInfo();
            margin.setLeft(50);
            header.setMargin(margin);
            footer.setMargin(margin);
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## Tambahkan header dan footer berbasis tabel

Gunakan contoh ini ketika konten header dan footer harus menggunakan tata letak tabel dan gaya teks.

1. Buat gaya teks yang diperlukan dan objek tabel.
1. Tambahkan tabel ke [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) kontainer.
1. Terapkan header dan footer ke setiap halaman dan simpan dokumen.

```java
public static void addHeaderAndFooterAsTable(Path inputFile, Path outputFile) {
    TextState textStateHeader = new TextState();
    textStateHeader.setFont(FontRepository.findFont("Arial"));
    textStateHeader.setFontSize(12);
    textStateHeader.setHorizontalAlignment(HorizontalAlignment.Center);

    TextState textStateFooter = new TextState();
    textStateFooter.setFont(FontRepository.findFont("Arial"));
    textStateFooter.setFontSize(12);
    textStateFooter.setHorizontalAlignment(HorizontalAlignment.Left);

    HeaderFooter header = new HeaderFooter();
    HeaderFooter footer = new HeaderFooter();

    Table tableHeader = new Table();
    tableHeader.setColumnWidths(String.valueOf(594 - header.getMargin().getLeft() - header.getMargin().getRight()));
    tableHeader.getRows().add().getCells().add("This is a Table Header", textStateHeader);

    Table table = new Table();
    table.setColumnWidths(String.valueOf(594 - footer.getMargin().getLeft() - footer.getMargin().getRight()));
    table.getRows().add().getCells().add("Powered by Aspose.PDF", textStateFooter);

    header.getParagraphs().add(tableHeader);
    footer.getParagraphs().add(table);
    footer.getMargin().setLeft(150);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## Tambahkan header dan footer LaTeX

Gunakan contoh ini ketika header dan footer harus menampilkan konten TeX atau LaTeX.

1. Buka PDF sumber dan tentukan total jumlah halaman.
1. Buat [TeXFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/texfragment/) konten untuk header dan footer setiap halaman.
1. Tetapkan konten dan simpan dokumen.

```java
public static void addHeaderAndFooterAsLatex(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        int pageCount = document.getPages().size();
        for (int i = 1; i <= pageCount; i++) {
            HeaderFooter header = new HeaderFooter();
            header.getParagraphs().add(new TeXFragment("This is a LaTeX Header. \\today\\", true));

            HeaderFooter footer = new HeaderFooter();
            footer.getParagraphs().add(new TeXFragment("\\copyright\\ 2025 My Company -- Page \\thepage\\ is " + pageCount, true));

            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```
