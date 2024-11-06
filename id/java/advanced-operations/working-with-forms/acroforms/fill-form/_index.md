---
title: Isi AcroForms
linktitle: Isi AcroForms
type: docs
weight: 20
url: id/java/fill-form/
description: Bagian ini menjelaskan bagaimana mengisi bidang formulir dalam dokumen PDF dengan Aspose.PDF untuk Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Dokumen PDF sangat bagus, dan benar-benar jenis file yang disukai, untuk membuat Formulir.

Aspose.PDF untuk Java memungkinkan Anda mengisi bidang formulir, mendapatkan bidang dari koleksi Form objek Dokumen.

Mari kita lihat contoh berikut bagaimana menyelesaikan tugas ini:

```java
public class ExamplesFillForm {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void FillFormFieldPDFDocument() {
        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "TextField.pdf");
        Page page = pdfDocument.getPages().get_Item(1);
        // Buat sebuah bidang
        TextBoxField textBoxField = new TextBoxField(page, new Rectangle(100, 200, 300, 300));
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("Text Box");

        // TextBoxField.Border = new Border(
        Border border = new Border(textBoxField);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        textBoxField.setBorder(border);

        textBoxField.setColor(Color.getGreen());

        // Tambahkan bidang ke dokumen
        pdfDocument.getForm().add(textBoxField, 1);

        // Simpan PDF yang dimodifikasi
        pdfDocument.save(_dataDir + "TextBox_out.pdf");

    }

    
}
```