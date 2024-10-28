---
title: Pindahkan dan Hapus Bidang Formulir
type: docs
weight: 50
url: /java/move-remove-form-field/
description: Bagian ini menjelaskan bagaimana Anda dapat memindahkan dan menghapus Bidang Formulir dengan Kelas FormEditor.
lastmod: "2021-06-05"
draft: false
---


## Pindahkan Bidang Formulir ke Lokasi Baru di File PDF yang Ada

Jika Anda ingin memindahkan bidang formulir ke lokasi baru maka Anda dapat menggunakan metode [moveField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#moveField-java.lang.String-float-float-float-float-) dari kelas [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor).
 Anda hanya perlu memberikan nama field dan lokasi baru dari field ini ke metode [moveField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#moveField-java.lang.String-float-float-float-float-). Anda juga perlu menyimpan file PDF yang telah diperbarui menggunakan metode Save dari kelas [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). Cuplikan kode berikut menunjukkan cara memindahkan field formulir ke lokasi baru dalam file PDF.

```java
 public static void MoveField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-05.pdf");
            editor.MoveField("Last Name", 262.56f, 496.75f, 382.28f, 514.03f);
            editor.Save(_dataDir + "Sample-Form-05-mod.pdf");
        }
```

## Hapus Field Formulir dari File PDF yang Ada

Untuk menghapus field formulir dari file PDF yang ada, Anda dapat menggunakan metode RemoveField dari kelas FormEditor. Metode ini hanya membutuhkan satu argumen: nama bidang. Anda perlu membuat objek dari kelas FormEditor, panggil metode [removeField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#removeField-java.lang.String-) untuk menghapus bidang tertentu dari PDF dan kemudian panggil metode Save untuk menyimpan file PDF yang telah diperbarui. Cuplikan kode berikut menunjukkan kepada Anda cara menghapus bidang formulir dari file PDF yang ada.

```java
 public static void RemoveFields()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.RemoveField("First Name");
            editor.RemoveField("Last Name");
            editor.Save(_dataDir + "Sample-Form-01-updated.pdf");
        }
```

## Ganti Nama Bidang Formulir di PDF

Anda juga dapat mengganti nama bidang Anda menggunakan metode [renameField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#renameField-java.lang.String-java.lang.String-) dari kelas [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor).
```java
    public static void RenameFields()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            // Mengganti nama bidang "Last Name" menjadi "LastName"
            editor.RenameField("Last Name", "LastName");
            // Mengganti nama bidang "First Name" menjadi "FirstName"
            editor.RenameField("First Name", "FirstName");
            editor.Save(_dataDir + "Sample-Form-01-updated.pdf");
        }
```