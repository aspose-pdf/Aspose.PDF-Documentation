---
title: Hiasi Bidang Formulir di PDF
type: docs
weight: 20
url: id/net/decorate-form-field/
description: Bagian ini menjelaskan cara menghiasi Bidang Formulir di PDF menggunakan Kelas FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Hiasi Bidang Formulir Tertentu dalam File PDF yang Ada

Metode [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield) yang ada di kelas [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) memungkinkan Anda untuk menghiasi bidang formulir tertentu dalam file PDF. Jika Anda ingin mendekorasi bidang tertentu maka Anda perlu memberikan nama bidang ke metode ini. Namun, sebelum memanggil metode ini, Anda perlu membuat objek dari kelas [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) dan [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Anda juga perlu menetapkan objek [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) ke properti [Facade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) dari objek [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Setelah itu, Anda dapat mengatur atribut apa pun yang disediakan oleh objek [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Setelah Anda mengatur atributnya, Anda dapat memanggil metode [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield) dan akhirnya menyimpan PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) dari kelas [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor).
Cuplikan kode berikut menunjukkan kepada Anda cara mendekorasi bidang formulir tertentu.

```csharp
public static void DecorateField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");

            var cityDecoration = new FormFieldFacade
            {
                Font = FontStyle.Courier,
                FontSize = 12,
                BorderColor = System.Drawing.Color.Black,
                BorderWidth = 2
            };

            editor.Facade = cityDecoration;
            editor.DecorateField("City");
            editor.Save(_dataDir + "Sample-Form-02.pdf");
        }
```
## Decorate All Fields of a Particular Type in an Existing PDF File

[DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) metode memungkinkan Anda untuk mendekorasi semua bidang formulir dari jenis tertentu dalam file PDF sekaligus. If you want to decorate all fields of a particular type then you need to pass the field type to this method.

Jika Anda ingin mendekorasi semua bidang dari tipe tertentu maka Anda perlu meneruskan tipe bidang ke metode ini. Namun, sebelum memanggil metode ini, Anda perlu membuat objek dari kelas [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) dan [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Anda juga perlu menetapkan objek [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) ke properti [Facade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) dari objek [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Setelah itu, Anda dapat mengatur atribut apa pun yang disediakan oleh objek [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Setelah Anda mengatur atribut, Anda dapat memanggil metode [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) dan akhirnya menyimpan PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) dari kelas [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Cuplikan kode berikut menunjukkan cara menghiasi semua bidang dari jenis tertentu.

```csharp
        public static void DecorateField2()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");

            var textFieldDecoration = new FormFieldFacade
            {
                Alignment = FormFieldFacade.AlignCenter,
            };

            editor.Facade = textFieldDecoration;
            editor.DecorateField(FieldType.Text);
            editor.Save(_dataDir + "Sample-Form-01-align-text.pdf");
        }
```