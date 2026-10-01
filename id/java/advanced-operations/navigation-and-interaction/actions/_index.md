---
title: "Bekerja dengan tindakan PDF di Java"
linktitle: Tindakan
type: docs
weight: 20
url: /id/java/actions/
description: Pelajari cara menambahkan, memperbarui, dan menghapus tindakan dokumen, halaman, dan formulir dalam file PDF menggunakan Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: "Menambahkan tindakan dokumen, halaman, dan formulir ke file PDF menggunakan Java"
Abstract: Artikel ini menjelaskan cara bekerja dengan aksi dalam dokumen PDF menggunakan Aspose.PDF for Java. Ini mencakup aksi bernama untuk mencetak dan navigasi halaman, menyembunyikan bidang formulir, mengirimkan formulir, menetapkan aksi peluncuran JavaScript, serta menambahkan atau menghapus aksi buka dan tutup halaman.
---
Aspose.PDF for Java memungkinkan Anda menetapkan aksi pada tombol, dokumen, dan halaman untuk membuat file PDF menjadi interaktif.

## Menambahkan tindakan cetak bernama

Gunakan contoh ini ketika tombol pada halaman harus memicu perintah cetak.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan pilih halaman target.
1. Buat [`ButtonField`](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) dan tetapkan sebuah [`NamedAction`](https://reference.aspose.com/pdf/java/com.aspose.pdf/namedaction/) untuk mencetak.
1. Tambahkan tombol ke formulir dan simpan dokumen.

```java
public static void addNamedActionPrint(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        Rectangle rect = new Rectangle(10, 10, 100, 40, true);
        ButtonField printButton = new ButtonField(page, rect);
        printButton.setPartialName("printButton");
        printButton.setValue("Print");
        printButton.getAnnotationActions().setOnReleaseMouseBtn(
                new NamedAction(PredefinedAction.File_Print));

        Border border = new Border(printButton);
        border.setWidth(1);
        printButton.setBorder(border);

        document.getForm().add(printButton, 1);
        document.save(outputFile.toString());
    }
}
```

## Menambahkan aksi sembunyikan

Gunakan contoh ini ketika tombol harus menampilkan atau menyembunyikan sekumpulan bidang formulir, seperti kotak centang.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan kumpulkan widget formulir target.
1. Buat sebuah tombol dan tetapkan sebuah [`HideAction`](https://reference.aspose.com/pdf/java/com.aspose.pdf/hideaction/) ke itu.
1. Tambahkan tombol ke formulir dan simpan dokumen yang diperbarui.

```java
public static void addNamedActionHide(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<WidgetAnnotation> checkboxes = new ArrayList<>();
        for (WidgetAnnotation field : document.getForm()) {
            if (field instanceof CheckboxField) {
                checkboxes.add(field);
            }
        }

        Rectangle rect = new Rectangle(10, 410, 140, 440, true);
        ButtonField hideButton = new ButtonField(document.getPages().get_Item(1), rect);
        hideButton.setPartialName("HideButton");
        hideButton.setValue("Hide Checkboxes");
        hideButton.getAnnotationActions().setOnReleaseMouseBtn(
                new HideAction(checkboxes.toArray(new WidgetAnnotation[0]), true));

        document.getForm().add(hideButton, 1);
        document.save(outputFile.toString());
    }
}
```

## Menambahkan tombol navigasi halaman

Contoh ini membuat tombol halaman pertama, sebelumnya, berikutnya, dan terakhir di seluruh dokumen.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat tombol navigasi untuk setiap halaman dan tetapkan aksi bawaan yang cocok.
1. Tambahkan tombol ke formulir dan simpan dokumen.

```java
public static void addNavigationButtons(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();

        for (Page page : document.getPages()) {
            ButtonField firstPageButton = new ButtonField(page, new Rectangle(10, 10, 110, 40, true));
            firstPageButton.setPartialName("First Page");
            firstPageButton.setValue("First Page");
            firstPageButton.getCharacteristics().setBorder(com.aspose.pdf.Color.getRed());
            firstPageButton.getCharacteristics().setBackground(com.aspose.pdf.Color.getOrange().toRgb());
            firstPageButton.setReadOnly(document.getPages().indexOf(page) == 1);
            firstPageButton.getAnnotationActions().setOnReleaseMouseBtn(
                    new NamedAction(PredefinedAction.FirstPage));
            document.getForm().add(firstPageButton);

            ButtonField previousPageButton = new ButtonField(page, new Rectangle(120, 10, 220, 40, true));
            previousPageButton.setPartialName("Previous Page");
            previousPageButton.setValue("Previous Page");
            previousPageButton.getCharacteristics().setBorder(com.aspose.pdf.Color.getRed());
            previousPageButton.getCharacteristics().setBackground(com.aspose.pdf.Color.getOrange().toRgb());
            previousPageButton.setReadOnly(document.getPages().indexOf(page) == 1);
            previousPageButton.getAnnotationActions().setOnReleaseMouseBtn(
                    new NamedAction(PredefinedAction.PrevPage));
            document.getForm().add(previousPageButton);

            ButtonField nextPageButton = new ButtonField(page, new Rectangle(230, 10, 330, 40, true));
            nextPageButton.setPartialName("Next Page");
            nextPageButton.setValue("Next Page");
            nextPageButton.getCharacteristics().setBorder(com.aspose.pdf.Color.getRed());
            nextPageButton.getCharacteristics().setBackground(com.aspose.pdf.Color.getOrange().toRgb());
            nextPageButton.setReadOnly(document.getPages().indexOf(page) == totalPages);
            nextPageButton.getAnnotationActions().setOnReleaseMouseBtn(
                    new NamedAction(PredefinedAction.NextPage));
            document.getForm().add(nextPageButton);

            ButtonField lastPageButton = new ButtonField(page, new Rectangle(340, 10, 440, 40, true));
            lastPageButton.setPartialName("Last Page");
            lastPageButton.setValue("Last Page");
            lastPageButton.getCharacteristics().setBorder(com.aspose.pdf.Color.getRed());
            lastPageButton.getCharacteristics().setBackground(com.aspose.pdf.Color.getOrange().toRgb());
            lastPageButton.setReadOnly(document.getPages().indexOf(page) == totalPages);
            lastPageButton.getAnnotationActions().setOnReleaseMouseBtn(
                    new NamedAction(PredefinedAction.LastPage));
            document.getForm().add(lastPageButton);
        }

        document.save(outputFile.toString());
    }
}
```

## Menambahkan aksi submit

Gunakan contoh ini ketika tombol harus mengirim data formulir ke URL.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`SubmitFormAction`](https://reference.aspose.com/pdf/java/com.aspose.pdf/submitformaction/) dengan URL target dan flag.
1. Tetapkan aksi ke bidang tombol dan simpan dokumen.

```java
public static void addSubmitAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        SubmitFormAction submitAction = new SubmitFormAction();
        FileSpecification submitUrl = new FileSpecification();
        submitUrl.setFileSystem("URL");
        submitUrl.setName("http://localhost:3000/submit");
        submitAction.setUrl(submitUrl);
        submitAction.setFlags(SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES);

        Rectangle rect = new Rectangle(10, 10, 100, 40, true);
        ButtonField submitButton = new ButtonField(document.getPages().get_Item(1), rect);
        submitButton.setPartialName("SubmitButton");
        submitButton.setValue("Submit");
        submitButton.getAnnotationActions().setOnReleaseMouseBtn(submitAction);

        document.getForm().add(submitButton, 1);
        document.save(outputFile.toString());
    }
}
```

## Menambahkan tindakan peluncuran tingkat dokumen

Contoh ini menetapkan aksi JavaScript yang dijalankan ketika dokumen dibuka, disimpan, atau dicetak.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat yang diperlukan objek [`JavascriptAction`](https://reference.aspose.com/pdf/java/com.aspose.pdf/javascriptaction/) untuk peristiwa dokumen.
1. Tetapkan tindakan dan simpan dokumen.

```java
public static void addLaunchActions(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setOpenAction(new JavascriptAction("app.launchURL('http://localhost:3000/open');"));
        document.getActions().setBeforeSaving(
                new JavascriptAction("app.launchURL('http://localhost:3000/save');"));
        document.getActions().setBeforePrinting(
                new JavascriptAction("app.launchURL('http://localhost:3000/print');"));

        document.save(outputFile.toString());
    }
}
```

## Menambahkan aksi buka dan tutup halaman

Gunakan contoh ini ketika halaman tertentu harus memicu aksi saat dibuka dan ditutup.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan pastikan halaman target ada.
1. Buat navigasi halaman dan aksi JavaScript.
1. Tetapkan aksi halaman dan simpan dokumen.

```java
public static void addPageActions(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getPages().size() < 3) {
            System.out.println("Error: The document does not have at least 3 pages.");
            return;
        }

        Page page = document.getPages().get_Item(3);
        GoToAction action = new GoToAction(page);
        action.setDestination(new XYZExplicitDestination(page, 0, page.getPageInfo().getHeight(), 1));
        page.getActions().setOnOpen(action);
        page.getActions().setOnClose(
                new JavascriptAction("app.launchURL('http://localhost:3000/page/3');"));

        document.save(outputFile.toString());
    }
}
```

## Menghapus tindakan halaman

Gunakan pendekatan ini ketika aksi buka dan tutup yang sebelumnya ditetapkan harus dihapus dari halaman.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan pastikan halaman target ada.
1. Hapus semua aksi dari halaman tersebut.
1. Simpan dokumen yang diperbarui.

```java
public static void removePageActions(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getPages().size() < 3) {
            System.out.println("Error: The document does not have at least 3 pages.");
            return;
        }

        Page page = document.getPages().get_Item(3);
        page.getActions().removeActions();

        document.save(outputFile.toString());
    }
}
```
