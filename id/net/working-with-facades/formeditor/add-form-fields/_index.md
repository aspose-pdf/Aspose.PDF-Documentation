---
title: Add PDF Form Fields
type: docs
weight: 10
url: id/net/add-form-fields/
description: Topik ini menjelaskan cara bekerja dengan Form Fields menggunakan Aspose.PDF Facades dengan menggunakan Kelas FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Menambahkan Form Field dalam file PDF yang Ada

Untuk menambahkan form field dalam file PDF yang ada, Anda perlu menggunakan metode [AddField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfield/index) dari kelas [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Metode ini mengharuskan Anda untuk menentukan jenis bidang yang ingin Anda tambahkan beserta nama dan lokasi bidang tersebut. Anda perlu membuat objek dari kelas [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor), gunakan metode [AddField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfield/index) untuk menambahkan bidang baru dalam PDF, Anda juga dapat menentukan batas jumlah karakter dalam bidang Anda dengan [SetFieldLimit](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldlimit) dan akhirnya gunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) untuk menyimpan file PDF yang telah diperbarui. Cuplikan kode berikut menunjukkan kepada Anda bagaimana menambahkan bidang formulir dalam file PDF yang sudah ada.

```csharp
   public static void AddField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir+"Sample-Form-01.pdf");
            editor.AddField(FieldType.Text, "Country", 1, 232.56f, 496.75f, 352.28f, 514.03f);
            editor.SetFieldLimit("Country", 20);
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```
## Tambahkan URL Tombol Kirim dalam File PDF yang Ada 

Metode [AddSubmitBtn](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) memungkinkan Anda untuk mengatur URL tombol kirim dalam file PDF. Ini adalah URL di mana data diposting ketika tombol kirim diklik. Dalam contoh kode kami, kami menentukan URL, nama bidang kami, nomor halaman tempat kami ingin menambahkan, dan koordinat penempatan tombol. Metode [AddSubmitBtn](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) memerlukan nama bidang tombol kirim dan URL. Metode ini disediakan oleh kelas [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Cuplikan kode berikut menunjukkan kepada Anda cara mengatur URL tombol kirim.

```csharp
public static void AddSubmitBtn()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.AddSubmitBtn("Submit", 1, "Submit", "http://localhost:3000", 232.56f, 466.75f, 352.28f, 484.03f);
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```

## Tambahkan JavaScript untuk Tombol Tekan

Metode [AddFieldScript](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfieldscript) memungkinkan Anda menambahkan JavaScript ke tombol tekan dalam file PDF. Metode ini memerlukan nama tombol tekan dan JavaScript. Metode ini disediakan oleh kelas [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Cuplikan kode berikut menunjukkan kepada Anda cara mengatur JavaScript ke tombol tekan.

```csharp
     public static void AddFieldScript()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.AddFieldScript("Last Name", "app.alert(\"Only one last name\",3);");
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```