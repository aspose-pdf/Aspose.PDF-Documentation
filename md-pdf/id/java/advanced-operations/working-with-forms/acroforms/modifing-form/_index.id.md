---
title: Memodifikasi AcroForms
linktitle: Memodifikasi AcroForms
type: docs
weight: 40
url: /java/modifing-form/
description: Bagian ini menjelaskan bagaimana memodifikasi formulir dalam dokumen PDF Anda dengan Aspose.PDF untuk Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Mengatur Font Bidang Formulir Khusus

Bidang formulir dalam file PDF Adobe dapat dikonfigurasi untuk menggunakan font default tertentu. Aspose.PDF memungkinkan pengembang untuk menerapkan font apa pun sebagai font default bidang, baik salah satu dari 14 font inti atau font khusus.
Untuk mengatur dan memperbarui font default yang digunakan untuk bidang formulir, Aspose.PDF memiliki kelas DefaultAppearance (Font font, double size, Color color). Kelas ini dapat diakses menggunakan com.aspose.pdf.DefaultAppearance. Untuk menggunakan objek ini, gunakan metode setDefaultAppearance(..) dari kelas Field.

Cuplikan kode berikut menunjukkan cara mengatur font default untuk bidang formulir PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.DefaultAppearance;
import com.aspose.pdf.Document;
import com.aspose.pdf.Field;
import com.aspose.pdf.Font;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.Rectangle;
import com.aspose.pdf.TextBoxField;

public class ExamplesModifying {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void SetFormFieldFontOtherThan14CorePDFFonts() {
        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "FormFieldFont14.pdf");
        // Dapatkan bidang formulir tertentu dari dokumen
        Field field = (Field) pdfDocument.getForm().get("textbox1");

        // Buat objek font
        Font font = FontRepository.findFont("ComicSansMS");

        // Atur informasi font untuk bidang formulir
        field.setDefaultAppearance (new DefaultAppearance(font, 10, java.awt.Color.BLACK));
        
        // Simpan dokumen yang diperbarui
        pdfDocument.save(_dataDir + "FormFieldFont14_out.pdf");
    }
```


## Get/Set FieldLimit

Metode SetFieldLimit kelas FormEditor memungkinkan Anda untuk menetapkan batasan bidang, jumlah maksimum karakter yang dapat dimasukkan ke dalam suatu bidang.

```java
    public static void GettingMaximumFieldLimit()
    {
        // Mendapatkan batas maksimum bidang menggunakan DOM
        Document doc = new Document(_dataDir + "FieldLimit.pdf");
        TextBoxField field = (TextBoxField)doc.getForm().get("textbox1");
        System.out.println("Limit: " +field.getMaxLen());
    }
```

Anda juga dapat mendapatkan nilai yang sama menggunakan namespace Aspose.PDF.Facades dengan menggunakan potongan kode berikut.

```java
    public static void GettingMaximumFieldLimitFacades()
    {
        // Mendapatkan batas maksimum bidang menggunakan Facades
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form();
        form.bindPdf(_dataDir + "FieldLimit.pdf");
        System.out.println("Limit: " + form.getFieldLimit("textbox1"));
    }
```

Demikian pula, Aspose.PDF memiliki metode yang mendapatkan batasan bidang menggunakan pendekatan DOM.
 Cuplikan kode berikut menunjukkan langkah-langkahnya.

```java
    public static void SettingMaximumFieldLimit()
    {
        // Mendapatkan batas maksimum bidang menggunakan DOM
        Document doc = new Document(_dataDir + "FieldLimit.pdf");
        TextBoxField field = (TextBoxField)doc.getForm().get("textbox1");
        field.setMaxLen(10);
        System.out.println("Limit: " +field.getMaxLen());       
    }
```

## Menghapus Bidang Formulir Tertentu dari Dokumen PDF

Semua bidang formulir terdapat dalam koleksi Form objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Koleksi ini menyediakan berbagai metode yang mengelola bidang formulir, termasuk metode hapus. Jika Anda ingin menghapus bidang tertentu, berikan nama bidang sebagai parameter ke metode hapus dan kemudian simpan dokumen PDF yang telah diperbarui.

Cuplikan kode berikut menunjukkan cara menghapus bidang bernama dari dokumen PDF.

```java
    public static void DeleteParticularFormField()
    {    
        // Membuka dokumen
        Document pdfDocument = new Document("input.pdf");

        // Menghapus bidang bernama berdasarkan nama
        pdfDocument.getForm().delete("textbox1");

        // Simpan PDF yang telah dimodifikasi
        pdfDocument.save("output.pdf");
    }
```

## Memodifikasi Bidang Formulir dalam Dokumen PDF

Koleksi Form objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) memungkinkan Anda mengelola bidang formulir dalam dokumen PDF.

Untuk memodifikasi bidang formulir, dapatkan bidang dari koleksi Form dan atur propertinya. Kemudian simpan dokumen PDF yang telah diperbarui.

Cuplikan kode berikut menunjukkan cara memodifikasi bidang formulir yang ada dalam dokumen PDF.

```java
    public static void ModifyFormField()
    {
        Document pdfDocument = new Document("input.pdf");
        // Dapatkan bidang
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // Modifikasi nilai bidang
        textBoxField.setValue("Nilai Diperbarui");

        // Atur bidang sebagai hanya baca
        textBoxField.setReadOnly(true);

        // Simpan dokumen yang telah diperbarui
        pdfDocument.save("output.pdf");
    }
```

### Memindahkan Bidang Formulir ke Lokasi Baru dalam Berkas PDF

Jika Anda ingin memindahkan bidang formulir ke lokasi baru pada halaman PDF, pertama dapatkan objek bidang dan kemudian tentukan nilai baru untuk metode setRect-nya.
 A [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) object dengan koordinat baru ditetapkan ke metode setRect(..). Kemudian simpan PDF yang diperbarui menggunakan metode simpan dari objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Cuplikan kode berikut menunjukkan kepada Anda cara memindahkan bidang formulir ke lokasi baru.

```java
    public static void ModifyMoveFormFieldNewLocation()
    {    
        // Buka dokumen
        Document pdfDocument = new Document(_dataDir+"input.pdf");
        // Dapatkan bidang
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // Ubah lokasi bidang
        textBoxField.setRect(new Rectangle(300, 400, 600, 500));

        // Simpan dokumen yang telah dimodifikasi
        pdfDocument.save("output.pdf");
    }
}
```