---
title: Bekerja dengan Item Daftar
type: docs
weight: 30
url: /net/working-with-list-item/
description: Bagian ini menjelaskan cara bekerja dengan Item Daftar menggunakan Aspose.PDF Facades menggunakan Kelas FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Tambahkan Item Daftar dalam File PDF yang Ada

Metode [AddListItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addlistitem) memungkinkan Anda menambahkan item dalam bidang [ListBox](https://reference.aspose.com/pdf/net/aspose.pdf.forms/listboxfield). Argumen pertama adalah nama bidang dan argumen kedua adalah item bidang. Anda dapat melewatkan satu item bidang atau Anda dapat melewatkan array string yang berisi daftar item. Metode ini disediakan oleh kelas [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Cuplikan kode berikut menunjukkan cara menambahkan item daftar dalam file PDF.

```csharp
  public static void AddListItem()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.AddField(FieldType.ListBox, "Country", 1, 232.56f, 476.75f, 352.28f, 514.03f);
            editor.AddListItem("Country", "USA");
            editor.AddListItem("Country", "Canada");
            editor.AddListItem("Country", "France");
            editor.AddListItem("Country", "Spain");
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```

## Hapus Item Daftar dari File PDF yang Ada

Metode [DelListItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/dellistitem) memungkinkan Anda untuk menghapus item tertentu dari [ListBox](https://reference.aspose.com/pdf/net/aspose.pdf.forms/listboxfield). Parameter pertama adalah nama bidang sementara parameter kedua adalah item yang ingin Anda hapus dari daftar. Metode ini disediakan oleh kelas [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Cuplikan kode berikut menunjukkan kepada Anda cara menghapus item daftar dari file PDF.

```csharp
      public static void DelListItem()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-04.pdf");
            //-----
            editor.DelListItem("Country", "France");
            //-----
            editor.Save(_dataDir + "Sample-Form-04-mod.pdf");
        }
```