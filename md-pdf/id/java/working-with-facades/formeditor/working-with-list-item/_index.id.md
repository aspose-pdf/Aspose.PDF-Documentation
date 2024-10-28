---
title: Bekerja dengan Item Daftar
type: docs
weight: 30
url: /java/working-with-list-item/
description: Bagian ini menjelaskan cara bekerja dengan Item Daftar menggunakan com.aspose.pdf.facades dengan Kelas FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Menambahkan Item Daftar dalam File PDF yang Ada

Metode [addListItem](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#addListItem-java.lang.String-java.lang.String-) memungkinkan Anda untuk menambahkan item dalam bidang ListBox. Argumen pertama adalah nama bidang dan argumen kedua adalah item bidang. Anda dapat mengirimkan satu item bidang atau Anda dapat mengirimkan array string yang berisi daftar item. Metode ini disediakan oleh kelas [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). Cuplikan kode berikut menunjukkan cara menambahkan item daftar dalam file PDF.

```java
public static void AddListItem() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");
        editor.addField(FieldType.ListBox, "Country", 1, 232.56f, 476.75f, 352.28f, 514.03f);
        editor.addListItem("Country", "USA");
        editor.addListItem("Country", "Canada");
        editor.addListItem("Country", "France");
        editor.addListItem("Country", "Spain");
        editor.save(_dataDir + "Sample-Form-01-mod.pdf");
    }
```


## Hapus Item Daftar dari File PDF yang Ada

Metode [delListItem](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#delListItem-java.lang.String-java.lang.String-) memungkinkan Anda menghapus item tertentu dari ListBox. Parameter pertama adalah nama bidang sedangkan parameter kedua adalah item yang ingin Anda hapus dari daftar. Metode ini disediakan oleh kelas [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). Cuplikan kode berikut menunjukkan cara menghapus item daftar dari file PDF.

```java
    public static void DelListItem() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-04.pdf");
        // -----
        editor.delListItem("Country", "France");
        // -----
        editor.save(_dataDir + "Sample-Form-04-mod.pdf");
    }
```