---
title: Buat AcroForms - Buat PDF yang Dapat Diisi di Java
linktitle: Buat AcroForms
type: docs
weight: 10
url: id/java/create-forms/
description: Bagian ini menjelaskan cara membuat AcroForms dari awal dalam dokumen PDF Anda dengan Aspose.PDF untuk Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Tambahkan Form Field dalam Dokumen PDF

Kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) menyediakan koleksi bernama Form yang membantu mengelola form field dalam dokumen PDF.

Untuk menambahkan form field:

1. Buat form field yang ingin Anda tambahkan.
2. Panggil metode add dari koleksi [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/Form).

Contoh ini menunjukkan cara menambahkan TextBoxField. Anda dapat menambahkan form field apa pun dengan pendekatan yang sama:

1. Pertama, buat objek field dan atur propertinya.
2. Kemudian, tambahkan field ke koleksi Form.

### Menambahkan TextBoxField

Text field adalah elemen formulir yang memungkinkan penerima untuk memasukkan teks ke dalam formulir Anda.
 Ini akan digunakan kapan saja Anda ingin memberikan kebebasan kepada pengguna untuk mengetik apa yang mereka inginkan.

Potongan kode berikut menunjukkan cara menambahkan TextBoxField ke dokumen PDF.

```java
public class ExamplesCreateForm {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void AddingTextBoxField() {

        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "TextField.pdf");
        Page page = pdfDocument.getPages().get_Item(1);
        // Buat sebuah field
        TextBoxField textBoxField = new TextBoxField(page, new Rectangle(100, 200, 300, 300));
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("Kotak Teks");

        // TextBoxField.Border = new Border(
        Border border = new Border(textBoxField);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        textBoxField.setBorder(border);

        textBoxField.setColor(Color.getGreen());

        // Tambahkan field ke dokumen
        pdfDocument.getForm().add(textBoxField, 1);

        // Simpan PDF yang telah diubah
        pdfDocument.save(_dataDir + "TextBox_out.pdf");

    }
```

## Menambahkan RadioButtonField

Radio Button paling sering digunakan untuk pertanyaan pilihan ganda, dalam skenario di mana hanya satu jawaban yang dapat dipilih.

Cuplikan kode berikut menunjukkan cara menambahkan [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) dalam dokumen PDF.

```java
public static void AddingRadioButton() {
        Document pdfDocument = new Document();
        // tambahkan halaman ke file PDF
        pdfDocument.getPages().add();

        // instansiasi objek RadioButtonField dengan nomor halaman sebagai argumen
        RadioButtonField radio = new RadioButtonField(pdfDocument.getPages().get_Item(1));

        // tambahkan opsi radio button pertama dan juga tentukan posisinya menggunakan
        // objek Rectangle
        radio.addOption("Test", new Rectangle(20, 720, 40, 740));
        // tambahkan opsi radio button kedua
        radio.addOption("Test1", new Rectangle(120, 720, 140, 740));
        // tambahkan radio button ke objek form dari objek Document
        pdfDocument.getForm().add(radio);
        // simpan file PDF
        pdfDocument.save("RadioButtonSample.pdf");

    }
```


Cuplikan kode berikut menunjukkan langkah-langkah untuk menambahkan [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) dengan tiga opsi dan menempatkannya di dalam sel Tabel.

```java
public static void AddingRadioButtonAdvanced() {
        Document doc = new Document();
        Page page = doc.getPages().add();
        Table table = new Table();
        table.setColumnWidths("120 120 120");
        page.getParagraphs().add(table);
        Row r1 = table.getRows().add();
        Cell c1 = r1.getCells().add();
        Cell c2 = r1.getCells().add();
        Cell c3 = r1.getCells().add();

        RadioButtonField rf = new RadioButtonField(page);
        rf.setPartialName("radio");
        doc.getForm().add(rf, 1);

        RadioButtonOptionField opt1 = new RadioButtonOptionField();
        RadioButtonOptionField opt2 = new RadioButtonOptionField();
        RadioButtonOptionField opt3 = new RadioButtonOptionField();

        opt1.setOptionName("Item1");
        opt2.setOptionName("Item2");
        opt3.setOptionName("Item3");

        opt1.setWidth(15);
        opt1.setHeight(15);
        opt2.setWidth(15);
        opt2.setHeight(15);
        opt3.setWidth(15);
        opt3.setHeight(15);

        rf.add(opt1);
        rf.add(opt2);
        rf.add(opt3);

        opt1.setBorder(new Border(opt1));
        opt1.getBorder().setWidth(1);
        opt1.getBorder().setStyle(BorderStyle.Solid);
        opt1.getCharacteristics().setBorder(Color.getBlack());
        opt1.getDefaultAppearance().setTextColor(java.awt.Color.RED);
        opt1.setCaption(new TextFragment("Item1"));
        opt2.setBorder(new Border(opt2));
        opt2.getBorder().setWidth(1);
        opt2.getBorder().setStyle(BorderStyle.Solid);
        opt2.getCharacteristics().setBorder(java.awt.Color.BLACK);
        opt2.getDefaultAppearance().setTextColor(java.awt.Color.RED);
        opt2.setCaption(new TextFragment("Item2"));
        opt3.setBorder(new Border(opt3));
        opt3.getBorder().setWidth(1);
        opt3.getBorder().setStyle(BorderStyle.Solid);
        opt3.getCharacteristics().setBorder(java.awt.Color.BLACK);
        opt3.getDefaultAppearance().setTextColor(java.awt.Color.RED);
        opt3.setCaption(new TextFragment("Item3"));
        c1.getParagraphs().add(opt1);
        c2.getParagraphs().add(opt2);
        c3.getParagraphs().add(opt3);

        doc.save("RadioButtonField.pdf");
    }
```


## Menambahkan Keterangan ke RadioButtonField

Cuplikan kode berikut menunjukkan cara menambahkan keterangan yang akan dikaitkan dengan [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField):

```java
public static void AddingCaptionToRadioButtonField() {
        // Memuat formulir PDF sumber
        com.aspose.pdf.facades.Form form1 = new com.aspose.pdf.facades.Form(_dataDir + "RadioButtonField.pdf");
        Document document = new Document(_dataDir + "RadioButtonField.pdf");
        for (String item : form1.getFieldNames()) {
            System.out.println(item.toString());
            if (item.contains("radio1")) {
                RadioButtonField field0 = (RadioButtonField) document.getForm().get(item);
                RadioButtonOptionField fieldoption = new RadioButtonOptionField();
                fieldoption.setOptionName("Yes");
                fieldoption.setPartialName("Yesname");

                var updatedFragment = new TextFragment("test123");
                updatedFragment.getTextState().setFont(FontRepository.findFont("Arial"));
                updatedFragment.getTextState().setFontSize(10);
                updatedFragment.getTextState().setLineSpacing(6.32f);

                // Membuat objek TextParagraph
                TextParagraph par = new TextParagraph();

                // Mengatur posisi paragraf
                par.setPosition(new Position(field0.getRect().getLLX(),
                        field0.getRect().getLLY() + updatedFragment.getTextState().getFontSize()));
                // Menentukan mode pembungkusan kata
                par.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);

                // Menambahkan TextFragment baru ke paragraf
                par.appendLine(updatedFragment);

                // Menambahkan TextParagraph menggunakan TextBuilder
                TextBuilder textBuilder = new TextBuilder(document.getPages().get_Item(1));
                textBuilder.appendParagraph(par);

                field0.deleteOption("item1");
            }
        }
        document.save(_dataDir + "RadioButtonField_out.pdf");

    }
```


## Menambahkan bidang ComboBox

Combo Box adalah bidang formulir yang akan menambahkan menu dropdown ke dokumen Anda.

Cuplikan kode berikut menunjukkan cara menambahkan bidang [ComboBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/ComboBoxField) dalam dokumen PDF.

```java
public static void AddingComboboxField() {
        // buat objek Dokumen
        Document doc = new Document();
        // tambahkan halaman ke objek dokumen
        doc.getPages().add();
        // instansiasi objek ComboBox Field
        ComboBoxField combo = new ComboBoxField(doc.getPages().get_Item(1), new Rectangle(100, 600, 150, 616));
        // tambahkan opsi ke ComboBox
        combo.addOption("Red");
        combo.addOption("Yellow");
        combo.addOption("Green");
        combo.addOption("Blue");
        // tambahkan objek combo box ke koleksi bidang formulir dari objek dokumen
        doc.getForm().add(combo);
        // simpan dokumen PDF
        doc.save("ComboBox_Added.pdf");
    }
```

## Menambahkan Tooltip ke Formulir

Kelas Document menyediakan koleksi bernama Form yang mengelola bidang formulir dalam dokumen PDF.
 Untuk menambahkan tooltip ke bidang formulir, gunakan kelas Field AlternateName. Adobe Acrobat menggunakan ‘nama alternatif’ sebagai tooltip bidang.

Cuplikan kode berikut menunjukkan cara menambahkan tooltip ke bidang formulir dengan Java.

```java
public static void AddTooltipToFormField() {
        // Muat formulir PDF sumber
        Document doc = new Document(_dataDir + "AddTooltipToField.pdf");

        // Dapatkan sebuah bidang
        TextBoxField textBoxField = (TextBoxField) doc.getForm().get("textbox1");

        // Atur tooltip untuk textfield
        textBoxField.setAlternateName("Tooltip kotak teks");

        // Simpan dokumen yang telah dimodifikasi
        doc.save("output.pdf");
    }
```