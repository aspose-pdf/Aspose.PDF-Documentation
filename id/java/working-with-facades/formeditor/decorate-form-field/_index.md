---
title: Hias Bidang Formulir di PDF
type: docs
weight: 20
url: /id/java/decorate-form-field/
description: Bagian ini menjelaskan cara menghias Bidang Formulir di PDF menggunakan Kelas FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Menghias Bidang Formulir Tertentu dalam File PDF yang Ada

Metode [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) yang ada dalam kelas [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) memungkinkan Anda untuk menghias bidang formulir tertentu dalam file PDF.
 Jika Anda ingin mendekorasi bidang tertentu maka Anda perlu mengirimkan nama bidang ke metode ini. Namun, sebelum memanggil metode ini, Anda perlu membuat objek dari kelas [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) dan [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade). Setelah itu, Anda dapat mengatur atribut apa pun yang disediakan oleh objek [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade). Setelah Anda mengatur atributnya, Anda dapat memanggil metode [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) dan akhirnya menyimpan PDF yang diperbarui menggunakan metode Save dari kelas [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor).
Cuplikan kode berikut menunjukkan kepada Anda cara mendekorasi bidang formulir tertentu.

```java
public static void DecorateField() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");

        FormFieldFacade cityDecoration = new FormFieldFacade();
        cityDecoration.setFont(FontStyle.Courier);
        cityDecoration.setFontSize(12);
        cityDecoration.setBorderColor(Color.BLACK);
        cityDecoration.setBorderWidth(2);

        editor.setFacade(cityDecoration);
        editor.decorateField("City");
        editor.save(_dataDir + "Sample-Form-02.pdf");
    }
```

## Dekorasi Semua Bidang dari Jenis Tertentu dalam File PDF yang Ada

Metode [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) memungkinkan Anda untuk mendekorasi semua bidang formulir dari jenis tertentu dalam file PDF sekaligus.
 Jika Anda ingin menghias semua bidang dari jenis tertentu maka Anda perlu melewatkan jenis bidang ke metode ini. Namun, sebelum memanggil metode ini, Anda perlu membuat objek dari kelas [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) dan [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade). Setelah itu, Anda dapat mengatur atribut apa pun yang disediakan oleh objek [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade). Setelah Anda mengatur atribut, Anda dapat memanggil metode [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) dan akhirnya menyimpan PDF yang diperbarui menggunakan metode Save dari kelas [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). Potongan kode berikut menunjukkan kepada Anda cara menghias semua bidang dari jenis tertentu.

```java
   public static void DecorateFields() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");

        FormFieldFacade textFieldDecoration = new FormFieldFacade();
        // Mengatur perataan teks ke tengah
        textFieldDecoration.setAlignment(FormFieldFacade.ALIGN_CENTER);

        editor.setFacade(textFieldDecoration);
        // Menghias bidang teks
        editor.decorateField(FieldType.Text);
        editor.save(_dataDir + "Sample-Form-01-align-text.pdf");
    }
```