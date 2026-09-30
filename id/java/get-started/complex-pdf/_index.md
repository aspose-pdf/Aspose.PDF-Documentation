---
title: Membuat PDF yang kompleks
linktitle: Membuat PDF yang kompleks
type: docs
weight: 30
url: /id/java/complex-pdf-example/
description: Aspose.PDF for Java memungkinkan Anda membuat dokumen PDF yang lebih kompleks yang berisi gambar, fragmen teks, dan tabel dalam satu file.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Membuat PDF yang kompleks menggunakan Java"
Abstract: Artikel ini menunjukkan cara membuat PDF yang lebih kompleks di Java menggunakan Aspose.PDF. Contohnya menambahkan sebuah gambar, judul yang diformat, blok teks deskriptif, dan sebuah tabel dengan sel header yang bergaya serta baris jadwal yang dihasilkan, kemudian menyimpan hasilnya sebagai dokumen PDF.
---
The [Halo Dunia](/pdf/id/java/hello-world-example/) contoh mencakup jalur pembuatan PDF paling sederhana. contoh ini membangun di atas alur kerja itu dan membuat dokumen yang lebih kaya yang menggabungkan grafik, teks, dan konten tabel.

Untuk membuat dokumen PDF yang lebih kompleks di Java:

1. Buat sebuah [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan sebuah [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Tambahkan gambar ke [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) dengan `page.addImage(...)` dan sebuah [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) target.
1. Buat header [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) dan atur font, ukuran, perataan, dan [`Position`](https://reference.aspose.com/pdf/java/com.aspose.pdf/position/).
1. Buat yang kedua [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) untuk paragraf deskripsi.
1. Buat sebuah [`Table`](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) dengan batas, padding, dan gaya header.
1. Tambahkan baris jadwal yang dihasilkan ke [`Table`](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/).
1. Tambahkan [`Table`](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) ke [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) paragraf.
1. Simpan PDF keluaran [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

Kode Java berikut didasarkan pada `GetStartedExamples.java`.

```java
public static void complexExample(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        page.addImage(imageFile.toString(), new Rectangle(20, 730, 120, 830, true));

        TextFragment header = new TextFragment("New ferry routes in Fall 2029");
        header.getTextState().setFont(FontRepository.findFont("Arial"));
        header.getTextState().setFontSize(24);
        header.setHorizontalAlignment(HorizontalAlignment.Center);
        header.setPosition(new Position(130, 720));
        page.getParagraphs().add(header);

        String descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. "
                + "Ferry service is operating at half capacity and on a reduced schedule. "
                + "Expect lineups.";
        TextFragment description = new TextFragment(descriptionText);
        description.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        description.getTextState().setFontSize(14);
        description.setHorizontalAlignment(HorizontalAlignment.Left);
        page.getParagraphs().add(description);

        page.getParagraphs().add(createScheduleTable());

        document.save(outputFile.toString());
    }
}
```

Contoh yang sama menggunakan metode pembantu untuk menyiapkan tabel jadwal dengan pemformatan header dan waktu keberangkatan yang dihasilkan:

```java
private static Table createScheduleTable() {
    Table table = new Table();
    table.setColumnWidths("200 200");
    table.setBorder(new BorderInfo(BorderSide.Box, 1.0f, Color.getDarkSlateGray()));
    table.setDefaultCellBorder(new BorderInfo(BorderSide.Box, 0.5f, Color.getBlack()));
    table.setDefaultCellPadding(new MarginInfo(4.5, 4.5, 4.5, 4.5));
    table.getMargin().setBottom(10);
    table.getDefaultCellTextState().setFont(FontRepository.findFont("Helvetica"));

    Row headerRow = table.getRows().add();
    Cell departsCityCell = headerRow.getCells().add("Departs City");
    Cell departsIslandCell = headerRow.getCells().add("Departs Island");
    styleHeaderCell(departsCityCell);
    styleHeaderCell(departsIslandCell);

    Duration time = Duration.ofHours(6);
    Duration increment = Duration.ofMinutes(30);
    for (int index = 0; index < 10; index++) {
        Row dataRow = table.getRows().add();
        dataRow.getCells().add(formatTime(time));
        time = time.plus(increment);
        dataRow.getCells().add(formatTime(time));
    }

    return table;
}
```
