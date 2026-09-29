---
title: Gunakan FloatingBox untuk Tata Letak PDF di Java
linktitle: Menggunakan FloatingBox
type: docs
weight: 30
url: /id/java/floating-box/
description: Pelajari cara menggunakan FloatingBox untuk tata letak teks, konten multi‑kolom, dan penempatan yang tepat dalam dokumen PDF dengan Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Buat dan posisikan kontainer FloatingBox yang bergaya dalam PDF dengan Java
Abstract: Artikel ini menjelaskan cara menggunakan FloatingBox di Aspose.PDF for Java. Ini mencakup penempatan teks dalam kontainer mengambang berbingkai, membuat tata letak multi‑kolom berulang, menggunakan warna latar belakang, offset absolut, serta opsi penyelarasan horizontal atau vertikal.
---
Aspose.PDF for Java menggunakan `FloatingBox` untuk membuat kontainer teks yang dapat digunakan kembali dan tata letak berbasis kolom.

## Buat dan tambahkan kotak mengambang

Gunakan contoh ini ketika teks harus ditempatkan di dalam wadah mengambang yang berbingkai.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Buat sebuah `FloatingBox`, atur ukuran dan border-nya, serta tambahkan konten teks.
1. Tambahkan kotak ke halaman dan simpan dokumen.

```java
public static void createAndAddFloatingBox(Path outputFile) {
       try (Document document = new Document()) {
           Page page = document.getPages().add();

           FloatingBox box = new FloatingBox(400, 30);
           box.setBorder(new BorderInfo(BorderSide.All, 1.5f, Color.getDarkGreen()));
           box.setNeedRepeating(false);
           String phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi.";
           box.getParagraphs().add(new TextFragment(phrase));

           page.getParagraphs().add(box);
           document.save(outputFile.toString());
       }
   }
```

## Buat tata letak multi‑kolom berulang

Gunakan contoh ini ketika teks panjang harus mengalir melintasi beberapa kolom di dalam satu kotak mengambang.

1. Buat halaman dan konfigurasikan margin.
1. Hitung lebar kolom dan konfigurasikan `FloatingBox` pengaturan kolom.
1. Tambahkan fragmen teks berulang ke kotak dan simpan dokumen.

```java
public static void multiColumnLayout(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getPageInfo().setMargin(new MarginInfo(36, 18, 36, 18));

        int columnCount = 3;
        int spacing = 10;
        double width = page.getPageInfo().getWidth()
                - page.getPageInfo().getMargin().getLeft()
                - page.getPageInfo().getMargin().getRight()
                - (columnCount - 1) * spacing;
        double columnWidth = width / 3;

        FloatingBox box = new FloatingBox();
        box.setNeedRepeating(true);
        box.getColumnInfo().setColumnWidths(columnWidth + " " + columnWidth + " " + columnWidth);
        box.getColumnInfo().setColumnSpacing(String.valueOf(spacing));
        box.getColumnInfo().setColumnCount(3);

        String phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi.";
        for (int i = 0; i < 10; i++) {
            box.getParagraphs().add(new TextFragment(phrase));
        }

        page.getParagraphs().add(box);
        document.save(outputFile.toString());
    }
}
```

## Mulai setiap fragmen sebagai item pertama di kolom

Gunakan contoh ini ketika setiap fragmen yang disisipkan harus memulai segmen aliran kolom baru.

1. Buat halaman dan konfigurasikan multi-kolom `FloatingBox`.
1. Buat fragmen teks dan tandai dengan `setFirstParagraphInColumn(true)`.
1. Tambahkan kotak ke halaman dan simpan PDF.

```java
public static void multiColumnLayout2(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getPageInfo().setMargin(new MarginInfo(36, 18, 36, 18));

        int columnCount = 3;
        int spacing = 10;
        double width = page.getPageInfo().getWidth()
                - page.getPageInfo().getMargin().getLeft()
                - page.getPageInfo().getMargin().getRight()
                - (columnCount - 1) * spacing;
        double columnWidth = width / 3;

        FloatingBox box = new FloatingBox();
        box.setNeedRepeating(true);
        box.getColumnInfo().setColumnWidths(columnWidth + " " + columnWidth + " " + columnWidth);
        box.getColumnInfo().setColumnSpacing(String.valueOf(spacing));
        box.getColumnInfo().setColumnCount(3);

        String phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi.";
        for (int i = 0; i < 10; i++) {
            TextFragment text = new TextFragment(phrase);
            text.setFirstParagraphInColumn(true);
            box.getParagraphs().add(text);
        }

        page.getParagraphs().add(box);
        document.save(outputFile.toString());
    }
}
```

## Tambahkan kotak mengambang dengan warna latar belakang

Gunakan contoh ini ketika kontainer mengambang harus memiliki latar belakang yang terlihat.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Buat sebuah `FloatingBox`, atur warna latar belakangnya, dan tambahkan teks.
1. Tempatkan kotak pada halaman dan simpan dokumen.

```java
public static void backgroundSupport(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        FloatingBox box = new FloatingBox(400, 30);
        box.setBackgroundColor(Color.getLightGreen());
        box.setNeedRepeating(false);
        box.getParagraphs().add(new TextFragment("text example"));

        page.getParagraphs().add(box);
        document.save(outputFile.toString());
    }
}
```

## Posisikan kotak mengambang dengan offset absolut

Gunakan contoh ini ketika kotak mengambang harus muncul pada offset yang tepat di halaman.

1. Buat halaman dan siapkan konten teks di sekitarnya.
1. Buat sebuah `FloatingBox`, atur posisi absolut, dan tetapkan offset atas dan kiri.
1. Tambahkan konten ke halaman dan simpan dokumen.

```java
public static void offsetSupport(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        FloatingBox box = new FloatingBox(400, 30);
        box.setTop(45);
        box.setLeft(15);
        box.setPositioningMode(ParagraphPositioningMode.Absolute);
        box.setBorder(new BorderInfo(BorderSide.All, 1.5f, Color.getDarkGreen()));
        box.getParagraphs().add(new TextFragment("text example 1"));

        page.getParagraphs().add(new TextFragment("text example 2"));
        page.getParagraphs().add(box);
        page.getParagraphs().add(new TextFragment("text example 3"));

        document.save(outputFile.toString());
    }
}
```

## Ratakan teks di dalam kotak mengambang

Gunakan contoh ini ketika kotak mengambang harus menunjukkan penyelarasan vertikal yang berbeda dengan penyelarasan horizontal yang sama.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Buat beberapa `FloatingBox` objek dengan pengaturan perataan yang berbeda.
1. Tambahkan mereka ke halaman dan simpan hasilnya.

```java
public static void alignTextToFloat(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        FloatingBox floatBox = new FloatingBox(100, 100);
        floatBox.setVerticalAlignment(VerticalAlignment.Bottom);
        floatBox.setHorizontalAlignment(HorizontalAlignment.Right);
        floatBox.getParagraphs().add(new TextFragment("FloatingBox_bottom"));
        floatBox.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
        page.getParagraphs().add(floatBox);

        FloatingBox floatBox2 = new FloatingBox(100, 100);
        floatBox2.setVerticalAlignment(VerticalAlignment.Center);
        floatBox2.setHorizontalAlignment(HorizontalAlignment.Right);
        floatBox2.getParagraphs().add(new TextFragment("FloatingBox_center"));
        floatBox2.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
        page.getParagraphs().add(floatBox2);

        FloatingBox floatBox3 = new FloatingBox(100, 100);
        floatBox3.setVerticalAlignment(VerticalAlignment.Top);
        floatBox3.setHorizontalAlignment(HorizontalAlignment.Right);
        floatBox3.getParagraphs().add(new TextFragment("FloatingBox_top"));
        floatBox3.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
        page.getParagraphs().add(floatBox3);

        document.save(outputFile.toString());
    }
}
```
