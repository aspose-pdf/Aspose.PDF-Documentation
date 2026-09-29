---
title: Buat AcroForm - Buat PDF yang dapat diisi di Java
linktitle: Buat AcroForm
type: docs
weight: 10
url: /id/java/create-form/
description: Buat field AcroForm dari awal dalam dokumen PDF menggunakan Aspose.PDF for Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Buat field AcroForm interaktif dalam file PDF dengan Java
Abstract: Artikel ini menjelaskan cara membuat bidang AcroForm menggunakan Aspose.PDF for Java. Ini mencakup kotak teks, bidang teks multi-widget, tombol radio, kotak kombo, kotak centang, kotak daftar, bidang tanda tangan, dan bidang kode batang untuk formulir PDF interaktif.
---
Aspose.PDF for Java memungkinkan Anda membuat berbagai jenis bidang AcroForm dari awal.

## Buat bidang kotak teks

Gunakan contoh ini saat Anda perlu menambahkan bidang input teks satu baris ke formulir PDF baru.

1. Buat PDF baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman.
1. Buat [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) dengan persegi panjang target dan mengonfigurasi tampilannya.
1. Tambahkan bidang ke formulir dan simpan dokumen.

```java
public static void addTextBoxField(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Rectangle rectangle = new Rectangle(10, 600, 110, 620, true);
        TextBoxField textBoxField = new TextBoxField(page, rectangle);
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("Text Box");
        textBoxField.setDefaultAppearance(new DefaultAppearance("Arial", 10, Color.getDarkBlue().toRgb()));

        Border border = new Border(textBoxField);
        border.setWidth(1);
        border.setStyle(BorderStyle.Dashed);
        border.setDash(new Dash(3, 3));
        textBoxField.setBorder(border);

        textBoxField.getCharacteristics().setBorder(Color.getRed());
        textBoxField.getCharacteristics().setBackground(Color.getYellow().toRgb());

        document.getForm().add(textBoxField, 1);
        document.save(outputFile.toString());
    }
}
```

## Buat bidang kotak teks dengan beberapa widget

Gunakan contoh ini ketika nilai bidang teks yang sama harus muncul di beberapa posisi pada halaman.

1. Buat PDF baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman.
1. Definisikan beberapa persegi panjang dan tampilan untuk widget bidang.
1. Buat [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/), konfigurasikan setiap widget, dan simpan dokumen.

```java
public static void addTextBoxFieldNt(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Rectangle[] rects = {
                new Rectangle(10, 600, 110, 620, true),
                new Rectangle(10, 630, 110, 650, true),
                new Rectangle(10, 660, 110, 680, true)
        };

        DefaultAppearance[] defaultAppearances = {
                new DefaultAppearance("Arial", 10, Color.getDarkBlue().toRgb()),
                new DefaultAppearance("Helvetica", 12, Color.getDarkGreen().toRgb()),
                new DefaultAppearance(FontRepository.findFont("Calibri"), 14, Color.getDarkMagenta().toRgb())
        };

        TextBoxField textBoxField = new TextBoxField(page, rects);
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("Some text");

        int index = 0;
        for (WidgetAnnotation widget : textBoxField) {
            widget.setDefaultAppearance(defaultAppearances[index]);
            index++;
        }

        Border border = new Border(textBoxField);
        border.setWidth(1);
        border.setStyle(BorderStyle.Dashed);
        border.setDash(new Dash(3, 3));
        textBoxField.setBorder(border);

        textBoxField.getCharacteristics().setBorder(Color.getRed());
        textBoxField.getCharacteristics().setBackground(Color.getYellow().toRgb());

        document.getForm().add(textBoxField);
        document.save(outputFile.toString());
    }
}
```

## Buat bidang tombol radio

Gunakan contoh ini ketika formulir harus memungkinkan pengguna memilih satu opsi dari sekumpulan yang telah ditentukan.

1. Buat PDF baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman.
1. Buat [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/radiobuttonfield/) dan tambahkan opsi yang diperlukan.
1. Tambahkan bidang ke Form dan simpan PDF.

```java
public static void addRadioButton(Path outputFile) {
    try (Document document = new Document()) {
        document.getPages().add();

        RadioButtonField radio = new RadioButtonField(document.getPages().get_Item(1));
        radio.addOption("Option 1", new Rectangle(100, 640, 120, 680, true));
        radio.addOption("Option 2", new Rectangle(140, 640, 160, 680, true));

        document.getForm().add(radio);
        document.save(outputFile.toString());
    }
}
```

## Buat bidang combo box

Gunakan contoh ini ketika pengguna harus memilih satu nilai dari daftar drop-down.

1. Buat PDF baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman.
1. Buat [ComboBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/comboboxfield/) dan tambahkan opsi yang dapat dipilih.
1. Atur pilihan default dan simpan dokumen.

```java
public static void addComboBox(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        ComboBoxField combo = new ComboBoxField(page, new Rectangle(100, 640, 150, 656, true));
        combo.addOption("Red");
        combo.addOption("Yellow");
        combo.addOption("Green");
        combo.addOption("Blue");
        combo.setSelected(3);

        document.getForm().add(combo);
        document.save(outputFile.toString());
    }
}
```

## Buat bidang kotak centang

Gunakan contoh ini ketika formulir memerlukan opsi benar atau salah seperti persetujuan atau pemilihan fitur.

1. Buat PDF baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman.
1. Buat [CheckboxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/checkboxfield/) dan konfigurasikan tampilannya.
1. Tambahkan kotak centang ke formulir dan simpan file output.

```java
public static void addCheckboxFieldToPdf(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        CheckboxField checkbox = new CheckboxField(page, new Rectangle(50, 620, 100, 650, true));
        checkbox.getCharacteristics().setBackground(Color.getAqua().toRgb());
        checkbox.setStyle(BoxStyle.Circle);

        document.getForm().add(checkbox);
        document.save(outputFile.toString());
    }
}
```

## Buat bidang kotak daftar

Gunakan contoh ini ketika Form harus menampilkan beberapa pilihan yang tersedia dalam daftar yang terlihat.

1. Buat PDF baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman.
1. Buat [ListBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/listboxfield/) dan tambahkan opsi yang tersedia.
1. Tambahkan bidang ke formulir dan simpan dokumen.

```java
public static void addListBoxFieldToPdf(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        ListBoxField listBox = new ListBoxField(page, new Rectangle(50, 650, 100, 700, true));
        listBox.setPartialName("list");
        listBox.addOption("Red");
        listBox.addOption("Green");
        listBox.addOption("Blue");

        document.getForm().add(listBox);
        document.save(outputFile.toString());
    }
}
```

## Buat bidang tanda tangan

Gunakan contoh ini ketika dokumen harus menyisakan area yang terlihat untuk tanda tangan digital.

1. Buat PDF baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman.
1. Buat [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/signaturefield/) di dalam persegi panjang yang diperlukan.
1. Tambahkan bidang ke formulir dan simpan PDF keluaran.

```java
public static void addSignatureField(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        SignatureField signatureField = new SignatureField(page, new Rectangle(100, 700, 200, 800, true));
        signatureField.setPartialName("Signature1");
        document.getForm().add(signatureField);
        document.save(outputFile.toString());
    }
}
```

## Buat bidang barcode

Gunakan contoh ini ketika formulir harus menampilkan data yang dapat dibaca mesin di dalam bidang kode batang.

1. Buat PDF baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman.
1. Buat [BarcodeField](https://reference.aspose.com/pdf/java/com.aspose.pdf/barcodefield/) dan tambahkan nilai barcode.
1. Tambahkan bidang ke formulir dan simpan dokumen.

```java
public static void addBarcodeField(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        BarcodeField barcode = new BarcodeField(page, new Rectangle(100, 700, 200, 740, true));
        barcode.setPartialName("Barcode1");
        barcode.addBarcode("1234567890");
        document.getForm().add(barcode);
        document.save(outputFile.toString());
    }
}
```
