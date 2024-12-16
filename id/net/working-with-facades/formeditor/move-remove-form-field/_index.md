---
title: Memindahkan dan Menghapus Bidang Formulir
type: docs
weight: 50
url: /id/net/move-remove-form-field/
description: Bagian ini menjelaskan bagaimana Anda dapat memindahkan dan menghapus Bidang Formulir dengan Kelas FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Memindahkan Bidang Formulir ke Lokasi Baru dalam File PDF yang Ada

Jika Anda ingin memindahkan bidang formulir ke lokasi baru, Anda dapat menggunakan metode [MoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield) dari kelas [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Anda hanya perlu menyediakan nama field dan lokasi baru dari field ini ke metode [MoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield). Anda juga perlu menyimpan file PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) dari kelas [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Cuplikan kode berikut menunjukkan kepada Anda bagaimana memindahkan field formulir ke lokasi baru dalam file PDF.

```csharp
public static void MoveField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-05.pdf");
            editor.MoveField("Last Name", 262.56f, 496.75f, 382.28f, 514.03f);
            editor.Save(_dataDir + "Sample-Form-05-mod.pdf");
        }
```

## Menghapus Field Formulir dari File PDF yang Ada

Untuk menghapus field formulir dari file PDF yang ada, Anda dapat menggunakan metode RemoveField dari kelas FormEditor. Metode ini hanya membutuhkan satu argumen: nama field. Anda perlu membuat objek dari kelas FormEditor, memanggil metode [RemoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/removefield) untuk menghapus field tertentu dari PDF dan kemudian memanggil metode Save untuk menyimpan file PDF yang telah diperbarui. Cuplikan kode berikut menunjukkan cara menghapus field formulir dari file PDF yang ada.

```csharp
  public static void RemoveFields()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.RemoveField("First Name");
            editor.RemoveField("Last Name");
            editor.Save(_dataDir + "Sample-Form-01-updated.pdf");
        }
```

## Mengganti Nama Field Formulir di PDF

Anda juga dapat mengganti nama field Anda menggunakan metode [RenameField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/renamefield) dari kelas [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor).

```csharp

        public static void RenameFields()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.RenameField("Last Name", "LastName");
            editor.RenameField("First Name", "FirstName");
            editor.Save(_dataDir + "Sample-Form-01-updated.pdf");
        }
```