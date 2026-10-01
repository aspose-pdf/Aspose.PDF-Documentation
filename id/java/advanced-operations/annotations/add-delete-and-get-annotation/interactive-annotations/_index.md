---
title: "Anotasi interaktif menggunakan Java"
linktitle: "Anotasi interaktif"
type: docs
weight: 60
url: /id/java/interactive-annotations/
description: Pelajari cara menambahkan, memeriksa, dan menghapus anotasi tautan dalam dokumen PDF menggunakan Aspose.PDF for Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Bekerja dengan anotasi PDF interaktif di Java"
Abstract: Artikel ini menjelaskan cara bekerja dengan anotasi tautan interaktif dalam file PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup penemuan teks, pembuatan anotasi tautan di atas area teks yang cocok, membaca anotasi tautan yang ada, dan menghapusnya.
---
Anotasi interaktif dalam bagian ini berfokus pada alur kerja berbasis tautan dan tombol yang merespons tindakan pengguna di dalam penampil PDF.

## Menambahkan anotasi tautan

Gunakan contoh ini ketika Anda perlu menempatkan tautan yang dapat diklik di atas teks yang ditemukan di halaman.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Temukan fragmen teks target dan buat satu [`LinkAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) di atas persegi panjangnya.
1. Tetapkan sebuah [`GoToURIAction`](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/) dan simpan dokumen yang diperbarui.

```java
public static void linkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("file");
        document.getPages().get_Item(1).accept(textFragmentAbsorber);

        var phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);
        LinkAnnotation linkAnnotation = new LinkAnnotation(
                document.getPages().get_Item(1),
                phoneNumberFragment.getRectangle());
        linkAnnotation.setAction(new GoToURIAction("https://www.aspose.com"));

        document.getPages().get_Item(1).getAnnotations().add(linkAnnotation);
        document.save(outputFile.toString());
    }
}
```

## Mendapatkan anotasi tautan

Contoh ini memindai koleksi anotasi halaman dan melaporkan lokasi setiap anotasi tautan.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterasikan melalui anotasi pada halaman target.
1. Filter anotasi berdasarkan [`AnnotationType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Link` dan cetak persegi panjang mereka.

```java
public static void linkGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

## Menghapus anotasi tautan

Gunakan pendekatan ini ketika anotasi tautan yang ada harus dihapus dari halaman.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Kumpulkan anotasi yang tipenya adalah [`AnnotationType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Link`.
1. Hapus anotasi yang dikumpulkan dan simpan file output.

```java
public static void linkDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## Menambahkan anotasi garis

Contoh ini membuat anotasi garis interaktif dengan gaya panah, pengaturan batas, dan catatan popup.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`LineAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/lineannotation/) dengan titik awal dan akhir.
1. Konfigurasikan tampilannya dan anotasi popup, kemudian simpan dokumen.

```java
public static void lineAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        LineAnnotation lineAnnotation = new LineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(550, 93, 562, 439, true),
                new Point(556, 99),
                new Point(556, 443));

        lineAnnotation.setTitle("John Smith");
        lineAnnotation.setColor(Color.getRed());
        lineAnnotation.setStartingStyle(LineEnding.OpenArrow);
        lineAnnotation.setEndingStyle(LineEnding.OpenArrow);

        Border border = new Border(lineAnnotation);
        border.setWidth(3);
        lineAnnotation.setBorder(border);

        PopupAnnotation popup = new PopupAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(842, 124, 1021, 266, true));
        lineAnnotation.setPopup(popup);

        document.getPages().get_Item(1).getAnnotations().add(lineAnnotation);
        document.save(outputFile.toString());
    }
}
```

## Menambahkan tombol navigasi

Gunakan contoh ini ketika PDF harus menyertakan tombol halaman sebelumnya dan halaman berikutnya untuk navigasi interaktif.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan pastikan dokumen memiliki halaman yang diperlukan.
1. Buat [`ButtonField`](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) kontrol dengan tindakan navigasi yang telah ditentukan sebelumnya.
1. Tambahkan tombol ke koleksi formulir dan simpan dokumen yang diperbarui.

```java
public static void navigationButtonsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().add();

        record ButtonConfig(String name, double xPos, PredefinedAction action) {}
        List<ButtonConfig> buttonConfigs = List.of(
                new ButtonConfig("Previous Page", 120.0, PredefinedAction.PrevPage),
                new ButtonConfig("Next Page", 230.0, PredefinedAction.NextPage));

        for (Page page : document.getPages()) {
            for (ButtonConfig config : buttonConfigs) {
                Rectangle rect = new Rectangle(config.xPos(), 10.0, config.xPos() + 100, 40.0, true);
                ButtonField button = new ButtonField(page, rect);
                button.setPartialName(config.name());
                button.setValue(config.name());
                button.getCharacteristics().setBorder(Color.getRed());
                button.getCharacteristics().setBackground(Color.getOrange().toRgb());
                button.getAnnotationActions().setOnReleaseMouseBtn(new NamedAction(config.action()));
                document.getForm().add(button);
            }
        }
        document.save(outputFile.toString());
    }
}
```

## Menambahkan tombol cetak

Contoh ini membuat sebuah tombol yang memicu perintah cetak saat pengguna mengkliknya.

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman.
1. Buat [`ButtonField`](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) dan tetapkan tindakan cetak yang telah ditentukan sebelumnya.
1. Konfigurasikan batas dan latar belakang tombol, tambahkan ke formulir, dan simpan dokumen.

```java
public static void printButtonAdd(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Rectangle rect = new Rectangle(72, 748, 164, 768, true);
        ButtonField printButton = new ButtonField(page, rect);
        printButton.setAlternateName("Print current document");
        printButton.setColor(Color.getBlack());
        printButton.setPartialName("printBtn1");
        printButton.setValue("Print Document");
        printButton.getAnnotationActions().setOnReleaseMouseBtn(
                new NamedAction(PredefinedAction.File_Print));

        Border border = new Border(printButton);
        border.setStyle(BorderStyle.Solid);
        border.setWidth(2);
        printButton.setBorder(border);

        printButton.getCharacteristics().setBorder(Color.getBlue());
        printButton.getCharacteristics().setBackground(Color.getLightBlue().toRgb());

        document.getForm().add(printButton);
        document.save(outputFile.toString());
    }
}
```
