---
title: Ekstrak Data AcroForms
linktitle: Ekstrak Data AcroForms
type: docs
weight: 30
url: /id/java/extract-form/
description: Bagian ini menjelaskan bagaimana mengekstrak formulir dari dokumen PDF Anda dengan Aspose.PDF untuk Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Mendapatkan Nilai dari Bidang Individual Dokumen PDF

Metode [getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) dari bidang formulir memungkinkan Anda untuk mendapatkan nilai dari bidang tertentu.

Untuk mendapatkan nilainya, ambil bidang formulir dari koleksi Form objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Contoh ini memilih [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) dan mengambil nilainya menggunakan [metode getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Document;
import com.aspose.pdf.Field;
import com.aspose.pdf.TextBoxField;

public class ExamplesExtractFormData {
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void GetValueFromIndividualFieldPDFDocument() {
        // Buka dokumen
        Document pdfDocument = new Document(_dataDir+"GetValueFromField.pdf");

        // Dapatkan bidang
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // Dapatkan nama bidang
        System.out.printf("PartialName :-" + textBoxField.getPartialName());

        // Dapatkan nilai bidang
        System.out.printf("Value :-" + textBoxField.getValue());
    }
```


## Mendapatkan Nilai dari Semua Bidang dalam Dokumen PDF

Untuk mendapatkan nilai dari semua bidang dalam dokumen PDF, Anda perlu menavigasi melalui semua bidang formulir dan kemudian mendapatkan nilainya menggunakan [metode getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--). Dapatkan setiap bidang dari koleksi Form menggunakan [objek Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) [metode getForm()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) dan dapatkan daftar bidang formulir ke dalam array Field menggunakan getFields() dan telusuri array untuk mendapatkan nilai dari bidang.

Cuplikan kode berikut menunjukkan cara mendapatkan nilai dari semua bidang dalam dokumen PDF.

```java
    public static void GetValuesFromAllFieldsPDFDocument() {
        // Buka dokumen
        Document document = new Document(_dataDir + "GetValuesFromAllFields.pdf");

        Field[] fields = document.getForm().getFields();
        for (int i = 0; i < fields.length; i++) {

            System.out.println("Bidang formulir: " + fields[i].getFullName());
            System.out.println("Bidang formulir: " + fields[i].getValue());
        }

    }
}
```


## Mendapatkan Bidang Formulir dari Wilayah Tertentu pada File PDF

Dalam beberapa kasus, diperlukan untuk mendapatkan data tidak dari seluruh formulir, tetapi, misalnya, hanya dari seperempat kiri atas dari lembar cetak.
Dengan Aspose.PDF untuk Java, ini bukan masalah. Anda dapat menentukan wilayah untuk memfilter bidang yang berada di luar wilayah tertentu dari file PDF. Untuk mendapatkan bidang formulir dari area tertentu pada file PDF:

1. Buka file PDF menggunakan objek Document.
2. Dapatkan formulir dari koleksi Forms dokumen.
3. Tentukan wilayah persegi panjang dan berikan ke metode [getFieldsInRect](https://reference.aspose.com/pdf/java/com.aspose.pdf/Form#getFieldsInRect-com.aspose.pdf.Rectangle-) dari objek Form. Koleksi [Fields](https://reference.aspose.com/pdf/java/com.aspose.pdf/Field) akan dikembalikan.
4. Gunakan ini untuk memanipulasi bidang.

Cuplikan kode berikut menunjukkan cara mendapatkan bidang formulir dalam wilayah persegi panjang tertentu dari file PDF.

```java
public static void GetValuesFromSpecificRegion() {
    // Buka file pdf
    Document doc = new Document(_dataDir + "GetFieldsFromRegion.pdf");

    // Buat objek persegi panjang untuk mendapatkan bidang dalam area tersebut
    Rectangle rectangle = new Rectangle(35, 30, 500, 500);

    // Dapatkan formulir PDF
    com.aspose.pdf.Form form = doc.getForm();

    // Dapatkan bidang dalam area persegi panjang
    Field[] fields = form.getFieldsInRect(rectangle);

    // Tampilkan nama dan nilai Field
    for (Field field : fields)
    {
        // Tampilkan properti penempatan gambar untuk semua penempatan
        System.out.println("Field Name: " + field.getFullName() + "-" + "Field Value: " + field.getValue());
    }
}
```