---
title: "Menambahkan tooltip ke teks PDF di Java"
linktitle: Tooltip PDF
type: docs
weight: 20
url: /id/java/pdf-tooltip/
description: Pelajari cara menambahkan tooltip ke fragmen teks dalam dokumen PDF menggunakan Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menambahkan tooltip interaktif ke fragmen teks PDF menggunakan Java"
Abstract: Artikel ini menunjukkan cara menambahkan bantuan interaktif ke teks PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup cara melampirkan teks tooltip ke button fields tak terlihat yang ditempatkan di atas fragmen teks yang cocok dan membuat bidang teks tersembunyi yang muncul ketika pointer masuk ke trigger area.
---
Aspose.PDF for Java memungkinkan Anda menambahkan bantuan interaktif dengan menempatkan bidang Form di atas fragmen teks.

## Menambahkan tooltip ke teks yang cocok

Gunakan contoh ini ketika teks yang ada dalam PDF harus menampilkan tooltip saat dihover.

1. Buat PDF contoh dan buka kembali untuk penyuntingan.
1. Cari fragmen teks target dengan `TextFragmentAbsorber`.
1. Tempatkan `ButtonField` menambahkan overlay pada teks yang cocok dan menetapkan teks tooltip.
1. Simpan dokumen yang diperbarui.

```java
public static void addToolTipToSearchedText(Path outputFile) {
        Document document = new Document();
        document.getPages().add().getParagraphs()
                .add(new TextFragment("Move the mouse cursor here to display a tooltip"));
        document.getPages().get_Item(1).getParagraphs()
                .add(new TextFragment("Move the mouse cursor here to display a very long tooltip"));
        document.save(outputFile.toString());
        document.close();

        document = new Document(outputFile.toString());
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(
                "Move the mouse cursor here to display a tooltip");
        document.getPages().accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            field.setAlternateName("Tooltip for text.");
            document.getForm().add(field);
        }

        absorber = new TextFragmentAbsorber("Move the mouse cursor here to display a very long tooltip");
        document.getPages().accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            field.setAlternateName("Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
                    + " sed do eiusmod tempor incididunt ut labore et dolore magna"
                    + " aliqua. Ut enim ad minim veniam, quis nostrud exercitation"
                    + " ullamco laboris nisi ut aliquip ex ea commodo consequat."
                    + " Duis aute irure dolor in reprehenderit in voluptate velit"
                    + " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint"
                    + " occaecat cupidatat non proident, sunt in culpa qui officia"
                    + " deserunt mollit anim id est laborum.");
            document.getForm().add(field);
        }

        document.save(outputFile.toString());
        document.close();
    }
```

## Menampilkan blok teks mengambang saat mengarahkan kursor

Gunakan contoh ini ketika mengarahkan kursor ke area teks akan menampilkan bidang teks tersembunyi.

1. Buat PDF contoh dan buka kembali untuk penyuntingan.
1. Temukan fragmen teks pemicu dengan `TextFragmentAbsorber`.
1. Buat yang tersembunyi `TextBoxField` dan satu `ButtonField` dengan tindakan masuk dan keluar.
1. Simpan PDF akhir.

```java
public static void createHiddenTextBlock(Path outputFile) {
    Document document = new Document();
    document.getPages().add().getParagraphs()
            .add(new TextFragment("Move the mouse cursor here to display floating text"));
    document.save(outputFile.toString());
    document.close();

    document = new Document(outputFile.toString());
    TextFragmentAbsorber absorber = new TextFragmentAbsorber(
            "Move the mouse cursor here to display floating text");
    document.getPages().accept(absorber);
    TextFragment fragment = absorber.getTextFragments().get_Item(1);

    TextBoxField floatingField = new TextBoxField(
            fragment.getPage(), new Rectangle(100.0, 700.0, 220.0, 740.0, false));
    floatingField.setValue("This is the \"floating text field\".");
    floatingField.setReadOnly(true);
    floatingField.setFlags(floatingField.getFlags() | AnnotationFlags.Hidden);
    floatingField.setPartialName("FloatingField_1");
    floatingField.setDefaultAppearance(new DefaultAppearance("Helv", 10, java.awt.Color.BLUE));
    floatingField.getCharacteristics().setBackground(java.awt.Color.CYAN);
    floatingField.getCharacteristics().setBorder(java.awt.Color.BLUE);
    floatingField.setBorder(new Border(floatingField));
    floatingField.getBorder().setWidth(1);
    floatingField.setMultiline(true);

    document.getForm().add(floatingField);

    ButtonField buttonField = new ButtonField(fragment.getPage(), fragment.getRectangle());
    buttonField.getAnnotationActions().setOnEnter(new HideAction(floatingField, false));
    buttonField.getAnnotationActions().setOnExit(new HideAction(floatingField));

    document.getForm().add(buttonField);
    document.save(outputFile.toString());
    document.close();
}
```
